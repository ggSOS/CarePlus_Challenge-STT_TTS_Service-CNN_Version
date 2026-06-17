# TTS(Text To Speech) e STT(Speech To Text) para Sistemas Automatizados De Atendimento por Whatsapp

Solução para Challenge da CarePlus baseada na implementação de uma feature de transcrição e envio de áudios para usuários da Caren(Assistente virtual do Whatsapp da CarePlus)

## Integrantes

- rm553187 - Gabriel Borba
- rm553842 - Gustavo Gouvêa Soares
- rm553945 - Henrique Rafael Gomes de Souza
- rm554223 - Pedro Henrique Mello

## Problema

A CarePlus possui um sistema de atendimento automatizado por IA por whatsapp(Caren) que recebe e responde apenas mensagens de texto. A nossa solução seria implementar uma funcionalidade de leitura e resposta por áudio, trazendo conforto para os usuário que preferem se comunicar por áudio e acessibilidade para os usuários que não sabem ler, mas utilizam o whatsapp(86% dos Analfabetos Funcionais, que representam 30% da população brasileira entre 15 e 64 anos).

## O que a IA faz no projeto?

Para a funcionalidade de Speech-to-Text (STT), o projeto utiliza o modelo Whisper Turbo da OpenAI, um modelo de reconhecimento automático de fala (ASR) treinado para múltiplos idiomas e capaz de transcrever áudios diretamente para texto. Sua arquitetura combina processamento espectral de áudio, camadas convolucionais (CNN) e mecanismos de atenção baseados em Transformers.

A arquitetura pode ser resumida da seguinte forma:

```
Áudio
   ↓
Mel Spectrogram
   ↓
CNN (Conv1D)
   ↓
Transformer Encoder
   ↓
Transformer Decoder
   ↓
Texto
```

O Whisper Turbo foi escolhido por apresentar:

- suporte nativo ao idioma português;
- alta precisão para transcrição de fala;
- robustez em ambientes com ruído moderado;
- capacidade de reconhecimento para diferentes locutores;
- eliminação da necessidade de treinamento
- próprio do modelo;
- processamento local, sem dependência de serviços externos.

A utilização das camadas convolucionais permite uma extração eficiente das características acústicas do sinal de voz, enquanto os Transformers fornecem a capacidade de compreender dependências temporais e semânticas de longo alcance, resultando em transcrições mais precisas e robustas.

Enquanto a conversão de texto para fala(TTS) fica com a biblioteca pyttsx3, que transcreve de forma offline e através de um mecanismo de síntese de fala baseado em regras ou concatenativo(sem IA).

## De onde vieram os dados

O dataset é próprio da OpenAI, construído através da internet pública por meio de web scraping, expandindo esse volume de áudio pareados com texto para 1 milhão de horas de áudios rotulados.

## Ferramenta Utilizada

- STT (Speech To Text)
  - Whisper Turbo (OpenAI Whisper)
  - Processamento de áudio com Librosa
  - Inferência local sem necessidade de serviços externos
- TTS (Text To Speech)
  - pyttsx3
  - Síntese de fala offline

## Estrutura Básica do Modelo

- stt_service.py
  - realiza o carregamento do modelo Whisper Turbo
  - recebe um arquivo de áudio enviado pelo usuário
  - converte o áudio para 16 kHz mono
  - realiza a transcrição para texto

- tts_service.py
  - utiliza o mecanismo de concatenação da pyttsx3 para criar um áudio

- app.py
  - back-end que fornece os serviços
    - GET /
      - health-check
    - POST /stt
      - speech-to-text
    - POST /tts
      - text-to-speech

## Resultados

O Whisper Turbo apresentou resultados significativamente superiores aos experimentos realizados anteriormente com modelos treinados localmente sob restrições de hardware.

Além de eliminar a necessidade de treinamento próprio, o modelo oferece suporte nativo ao português, boa robustez para diferentes locutores e boa qualidade de transcrição mesmo em ambientes com ruído moderado.


## Requisitos para Utilização do Programa

- Python 3.12

- Instalar dependências em requirements.txt

```bash
pip install -r .\requirements.txt
```

- [ffmpeg](https://www.ffmpeg.org/download.html)

- um arquivo de áudio compatível (wav, mp3, m4a, ogg ou formatos suportados pelo Whisper) ou um texto para ser transcrito
> conferir exemplos disponibilizados em `examples/`

## Descrição do Código

Para iniciar o servidor:

```bash
uvicorn app:app --reload --port 5000
```

> O modelo Whisper Turbo será baixado automaticamente durante a primeira execução e armazenado localmente em: `IA_model/`

Após a inicialização, os endpoints estarão disponíveis em: `http://localhost:5000`

>Os endpoints podem ser testados através da coleção Postman disponibilizada no projeto.
