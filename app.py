from service.stt_service import transcrever_para_texto
from service.tts_service import transcrever_para_audio
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Annotated


class TTSRequest(BaseModel):
    content: str = Field(..., min_length=1, example="Olá, como vai?")

class Message(BaseModel):
    detail: str

app = FastAPI()


@app.post(
        "/tts",
    responses={
        200: {"description": "Sucesso no processamento do evento"},
        500: {"model": Message, "description": "Erro interno no motor de voz"}
    }
    )
async def tts(data: TTSRequest):
    audio = transcrever_para_audio(data.content)
    audio.seek(0)
    return StreamingResponse(audio, media_type="audio/wav")


@app.post(
        "/stt",
    responses={
        200: {"description": "Sucesso no processamento do evento"},
        500: {"model": Message, "description": "Erro interno no modelo de conversão"}
    }
    )
async def stt(file: Annotated[UploadFile, File()]):
    content_bytes = await file.read()
    content_binary_io = io.BytesIO(content_bytes)
    texto = transcrever_para_texto(content_binary_io)
    return {"filename": file.filename, "transcription": texto}


@app.get("/")
def health():
    return {"status": "tudo certo com a api!"}