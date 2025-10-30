from transformers import pipeline

def transcribe_audio(file_path):
    """
    Transcrit un fichier audio (WAV, MP3...) en texte
    en utilisant le modèle Whisper de Hugging Face.
    """
    print("🔊 Chargement du modèle de transcription (Whisper)...")
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    print("🎙️ Transcription en cours...")
    result = transcriber(file_path,return_timestamps=True)
    return result["text"]
