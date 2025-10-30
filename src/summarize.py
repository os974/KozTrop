from transformers import pipeline

def summarize_text(text):
    """
    Génère un résumé d’un texte donné.
    Utilise le modèle mT5 multilingue pour supporter le français.
    """
    print("🧠 Chargement du modèle de résumé (mT5)...")
    summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")
    print("✍️ Résumé en cours...")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
