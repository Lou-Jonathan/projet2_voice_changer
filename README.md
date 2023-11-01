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
 - Trouver quel librairie utilisé pour le HUD : Tkinter
 - Trouver comment faire des boutons et, si possible, avec des icons. (https://stackoverflow.com/questions/39054156/tkinter-custom-create-buttons et https://www.pythontutorial.net/tkinter/tkinter-button/)
 - Comment bien placer mes boutons : (https://www.geeksforgeeks.org/python-grid-method-in-tkinter/)
 - faire jouer le son non-modifier pour voir si la personne veut se son ou recommencer son enregistrement. 
 - Faire un genre de slider qui se complète jusqu'à la fin de l'audio. (https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Progressbar.html)
  Erreurs rencontrer : 
   - L'image est trop gros.
   - Tkinter freeze quand l'enregistrement commence.
   - Tkinter freeze quand le slider commence.
   - Ça m'a pris beaucoup de temps pour trouver la plupart des erreurs évidentes que les usagers peuvent faire en intéragissent avec le HUD.
   - Les boutons ne s'updatent pas après un nouvel enregistrement si le fichier n'existait pas à la base. 
  Solutions trouvés :
   - Appris comment me servir des global, cependant, je pense en avoir abuser un peu, alors je ne sais pas trop si c'est bon. (https://www.w3schools.com/python/python_variables_global.asp)
   - Pour que le tkinter ne freeze pas quand il lance l'enregistrement, j'ai fait un thread pour qu'il ne puisse pas être bloqué par ça. (pour faire mes threads : https://docs.python.org/3/library/threading.html)
   - Le problème du slider c'est régler en faisant un autre thread lié avec le son de l'enregistrement.
   - Pour que l'image ne soit pas gros, je l'ai changé moi-même avec Paint.
- Modifier le code pour que ça soit plus "eye candy"
 - J'ai appris pas mal de chose avec Python pour faire des classes (https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes) et (https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/)
 - Problèmes :
  - Le temps commence à manquer pour faire tout le programme. Il aurait fallu le faire un peu plus d'avance.
 - Solutions :
  - Je vais faire ce que je peux et envoyer le fichier que j'ai fait déjà, mais ça ne sera pas le programme final malheureusement. 

