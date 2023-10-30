import os
from tkinter import ttk
import speech_recognition as sr
import pyaudio
import wave
import tkinter as tk
import threading


wf = None
stream = None
chunk = 1024  # Nombre de frames par bloc
sample_format = pyaudio.paInt16  # 16 bits par échantillon
channels = 1  # Un canal pour l'enregistrement mono
fs = 44100  # Fréquence d'échantillonnage (en Hz)
p = pyaudio.PyAudio()
en_cours = False
racine = tk.Tk()
progress = ttk.Progressbar(racine, length=300, mode='determinate')
image_start = tk.PhotoImage(file="./images/Start-Button.png")
recording_thread = None
audio_thread = None
can_read_audio = False


def get_default_mic():
    default_mic = p.get_default_input_device_info()
    return default_mic


def play_sound():
    global wf, stream, en_cours
    if not en_cours:
        en_cours = True
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
    else:
        print("Vous ne pouvez pas jouer un son quand il y a un enregistrement en cours.")


def audio_file_exists():
    return os.path.isfile("enregistrement.wav")


def update_progress():
    global stream, wf, progress, en_cours
    progress['value'] = wf.tell() / wf.getnframes() * 100  # Met à jour la barre de progression avec la position de la musique
    if wf.tell() < wf.getnframes():
        racine.after(100, update_progress)  # Appelle la fonction après 100 millisecondes
    else:
        print("Fin de la lecture")
        progress['value'] = 0  # Met à 100% lorsque le son est terminé
        stream.stop_stream()
        en_cours = False


def play_audio_in_thread():
    global audio_thread, wf, en_cours
    wf = wave.open("enregistrement.wav", 'rb')
    audio_thread = threading.Thread(target=play_sound)
    audio_thread.start()
    update_progress()


def graphic_interface():
    global progress, en_cours
    mic = get_default_mic()
    bouton_enregistrement = tk.Button(racine, image=image_start, command=lambda: start_recording_thread(mic['index']))
    bouton_arret_enregistrement = tk.Button(racine, text="Fin de l'enregistrement", command=stop_recording)

    def quitter():
        if not en_cours:
            racine.quit()
            racine.destroy()
            exit()
        else:
            print("Vous ne pouvez pas quitter l'application quand il y a un enregistrement en cours.")

    bouton_quitter = tk.Button(racine, text="Quitter", command=quitter)

    if audio_file_exists():
        bouton_joue_enregistrement = tk.Button(racine, text="Jouer l'enregistrement", command=play_audio_in_thread)
    else:
        bouton_joue_enregistrement = tk.Button(racine, text="Jouer l'enregistrement", state=tk.DISABLED)

    bouton_enregistrement.grid(row=0, column=0, padx=(0, 10))
    bouton_arret_enregistrement.grid(row=2, column=0, padx=(0, 10))
    bouton_joue_enregistrement.grid(row=3, column=0, padx=(0, 10))
    progress.grid(row=3, column=1, padx=(0, 10))
    bouton_quitter.grid(row=4, column=0, padx=(0, 10))
    racine.mainloop()


def start_recording_thread(microphone_index):
    global recording_thread
    recording_thread = threading.Thread(target=record_audio, args=(microphone_index,))
    recording_thread.start()


def stop_recording():
    global en_cours, recording_thread
    try:
        en_cours = False
        if recording_thread.is_alive():
            recording_thread.join()
            recording_thread = None
    except AttributeError:
        print("Vous ne pouvez pas arêter un enregistrement quand il n'y a pas d'enregistrement.")


def record_audio(microphone_index):
    global en_cours
    if not en_cours:
        en_cours = True
        print("Enregistrement en cours...")
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True,
                        input_device_index=microphone_index)
        frames = []
        try:
            while en_cours:
                data = stream.read(chunk)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        stream.stop_stream()
        print("Enregistrement terminé !")
        save_audio(frames)
    print("Vous ne pouvez pas partir un enregistrement quand il y a déjà un enregistrement en cours.")


def save_audio(frames):
    global wf, can_read_audio
    wf = wave.open('enregistrement.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    can_read_audio = audio_file_exists()


graphic_interface()
