import os
from transcribe import transcribe_audio
from summarize import summarize_text

# === CONFIG ===
AUDIO_FILE = "audio/ce_nest_pas_faux.mp3"
OUTPUT_TRANSCRIPT = "output/transcription.txt"
OUTPUT_SUMMARY = "output/summary.txt"

def main():
    # Vérifie les dossiers
    os.makedirs("output", exist_ok=True)
    if not os.path.exists(AUDIO_FILE):
        print(f"❌ Le fichier audio {AUDIO_FILE} est introuvable.")
        return

    # Étape 1 : Transcription
    print("⏳ Étape 1 : Transcription audio → texte")
    transcription = transcribe_audio(AUDIO_FILE)
    print("✅ Transcription terminée.")

    # Sauvegarde de la transcription
    with open(OUTPUT_TRANSCRIPT, "w", encoding="utf-8") as f:
        f.write(transcription)

    # Étape 2 : Résumé
    print("\n⏳ Étape 2 : Résumé du texte")
    summary = summarize_text(transcription)
    print("✅ Résumé terminé.")

    # Sauvegarde du résumé
    with open(OUTPUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write(summary)

    # Affichage final
    print("\n📄 Résumé généré :")
    print(summary)

if __name__ == "__main__":
    main()