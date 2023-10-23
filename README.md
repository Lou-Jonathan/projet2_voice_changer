# Projet 2 Voice Changer

## Technologies prévues à être utilisées :

- Github (Repo)
- VSCode (IDE)
- API Elevenlabs (Text-To-Speech)
- Python
    - SpeechRecognition (Fichier Audio)
    - Pydub (Speech-To-Text)
    - Module Python VLC (Lecture Audio)
    - Tkinter (Interface Graphique)
    - PyAudio (Pour prendre le micro de l'utilisateur : http://people.csail.mit.edu/hubert/pyaudio/#downloads)

## Répartition des tâches pour la première semaine

### Lou 

- Utiliser l'API d'Elevenlabs pour convertir une chaîne de texte en fichier audio.
- Recevoir ce fichier audio et le jouer à l'utilisateur.
- Créer des options modifiables pour l'utilisateur, notamment en ce qui concerne le personnage qui parle et d'autres paramètres pour les requêtes à l'API.

### Bernard

- Utiliser SpeechRecognition pour enregistrer un clip audio de l'utilisateur.
  - Trouver le micro par défaut de l'utilisateur (En utilisant PyAudio)
  - Commencer l'enregistrement de l'audio avec SpeechRecognition. (https://realpython.com/python-speech-recognition/)
  - Arrêter l'enregistrement de l'audio d'un moyen quelconque.
  - Faire un HUD pour fermer enregistrer l'audio.
- Utiliser Pydub pour transformer le clip audio en texte.
- Créer une interface graphique comprenant un bouton pour enregistrer et jouer, ainsi que des champs d'entrée pour modifier les paramètres des requêtes à l'API.
