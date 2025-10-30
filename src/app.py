import streamlit as st
from transcribe import transcribe_audio
from summarize import summarize_text
import time

st.title("🧠 Transcripteur & Résumeur vocal IA")

uploaded_file = st.file_uploader("Dépose ton fichier audio", type=["wav", "mp3", "m4a"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Transcription en cours...")
    
    # Créer une barre de progression
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Ici, simuler une progression si transcribe_audio ne supporte pas de callback
    # Si transcribe_audio permet un callback, remplacer cette boucle par un vrai suivi
    for percent_complete in range(0, 101, 10):
        progress_bar.progress(percent_complete)
        status_text.text(f"Transcription : {percent_complete}%")
        time.sleep(0.2)  # ajuster selon durée réelle ou supprimer si transcribe_audio bloque
    
    # Transcrire l'audio
    text = transcribe_audio("temp.wav")
    
    # Indiquer que la transcription est terminée
    st.success("✅ Transcription terminée !")
    st.text_area("Transcription", text, height=200)
    
    if st.button("Générer un résumé"):
        st.info("Résumé en cours de génération...")
        summary = summarize_text(text)
        st.success("Résumé généré !")
        st.text_area("Résumé", summary, height=150)
