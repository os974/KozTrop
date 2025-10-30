from gtts import gTTS

texte = """Une phrase comme « C’est vrai que ce n’est pas faux » s’appelle — selon le point de vue linguistique — plusieurs choses possibles :

🌀 1. Une litote

C’est une figure de style qui atténue une idée pour mieux la faire comprendre.
Ici, dire « ce n’est pas faux » revient à dire « c’est vrai » — mais de manière ironique, modeste ou prudente.
👉 Exemple classique : « Ce n’est pas un génie » (pour dire « il est bête »).

🧩 2. Une double négation atténuative

Sur le plan grammatical, la phrase joue avec la négation et l’affirmation pour créer une ambiguïté ou une nuance.
« Ce n’est pas faux » n’est pas exactement « c’est vrai » : c’est une vérité partielle ou nuancée.

😏 3. Une tournure ironique ou paradoxale

Dans le langage courant, on parle souvent d’une phrase paradoxale ou d’un pléonasme ironique, car elle affirme en niant.
C’est typique de l’humour à la Kaamelott, par exemple :

« C’est pas faux » — Perceval.
"""

# Création de la synthèse vocale
tts = gTTS(text=texte, lang='fr')

# Sauvegarde dans un fichier MP3
nom_fichier = "ce_nest_pas_faux.mp3"
tts.save(nom_fichier)

print(f"✅ Fichier audio généré : {nom_fichier}")