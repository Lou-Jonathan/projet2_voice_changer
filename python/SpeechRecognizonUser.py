import threading

import speech_recognition as sr
import pyaudio
import wave
import tkinter as tk
import threading


chunk = 1024  # Nombre de frames par bloc
sample_format = pyaudio.paInt16  # 16 bits par échantillon
channels = 1  # Un canal pour l'enregistrement mono
fs = 44100  # Fréquence d'échantillonnage (en Hz)
p = pyaudio.PyAudio()
enregistrement_en_cours = False
racine = tk.Tk()
image_start = tk.PhotoImage(file="./images/Start-Button.png")
recording_thread = None


def get_default_mic():
    default_mic = p.get_default_input_device_info()
    return default_mic


def interface_graphique():
    mic = get_default_mic()
    bouton_enregistrement = tk.Button(racine, image=image_start, command=lambda: start_recording_thread(mic['index']))
    bouton_arret_enregistrement = tk.Button(racine, text="Fin de l'enregistrement", command=stop_recording)

    bouton_enregistrement.pack(ipadx=5, ipady=5, expand=True)
    bouton_arret_enregistrement.pack()
    racine.mainloop()


def start_recording_thread(microphone_index):
    global recording_thread
    recording_thread = threading.Thread(target=record_audio, args=(microphone_index,))
    recording_thread.start()


def stop_recording():
    global enregistrement_en_cours, recording_thread
    try:
        enregistrement_en_cours = False
        if recording_thread.is_alive():
            recording_thread.join()
            recording_thread = None
    except AttributeError:
        print("Vous ne pouvez pas arêter un enregistrement quand il n'y a pas d'enregistrement.")



def record_audio(microphone_index):
    global enregistrement_en_cours
    if not enregistrement_en_cours:
        enregistrement_en_cours = True
        print("Enregistrement en cours")
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True,
                        input_device_index=microphone_index)
        frames = []
        try:
            while enregistrement_en_cours:
                data = stream.read(chunk)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        stream.stop_stream()
        stream.close()
        print("Enregistrement terminé")
        return frames
    print("Vous ne pouvez pas arêter un enregistrement quand il y a déjà un enregistrement en cours.")


def save_audio(microphone_index):
    frames = record_audio(microphone_index)
    wf = wave.open('enregistrement.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


def resize_image(img, new_width, new_height):
    old_width = img.width()
    old_height = img.height()
    new_photo_image = tk.PhotoImage(width=new_width, height=new_height)
    for x in range(new_width):
        for y in range(new_height):
            x_old = int(x*old_width/new_width)
            y_old = int(y*old_height/new_height)
            rgb = '#%02x%02x%02x' % img.get(x_old, y_old)
            new_photo_image.put(rgb, (x, y))
    return new_photo_image


image_start = resize_image(image_start, 50, 50)
interface_graphique()
