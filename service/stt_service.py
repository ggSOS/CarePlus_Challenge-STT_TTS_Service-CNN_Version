from pathlib import Path
import librosa
import os
import io
import whisper
from typing import Union, BinaryIO
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")


def download_model():
    """Baixar o modelo do Whisper escolhido
    """
    ## tipo(qualidade - tiny/base/small/medium/turbo/large) da IA de Speech to Text
    model_type = "turbo"

    model_dir = Path(__file__).parent.parent / "IA_model"
    model_dir.mkdir(exist_ok=True)
    return whisper.load_model(model_type, download_root=str(model_dir))

def transcrever_para_texto(audio_file: Union[BinaryIO, str, os.PathLike]) -> str:
    language = "pt"
    model = download_model()
    
    dados_audio, _ = librosa.load(
        io.BytesIO(audio_file.read()),
        sr=16000,
        mono=True
    )

    result = model.transcribe(
        dados_audio,
        language=language,
        temperature=0,
        best_of=5,
        beam_size=5
    )
    return str(result["text"])