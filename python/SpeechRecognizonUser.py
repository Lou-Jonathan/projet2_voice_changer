import threading

import speech_recognition as sr
import pyaudio
import wave


chunk = 1024  # Nombre de frames par bloc
sample_format = pyaudio.paInt16  # 16 bits par échantillon
channels = 1  # Un canal pour l'enregistrement mono
fs = 44100  # Fréquence d'échantillonnage (en Hz)
p = pyaudio.PyAudio()
enregistrement_en_cours = True

def get_default_mic():
    default_mic = p.get_default_input_device_info()
    return default_mic

def wait_user_entry():
    global enregistrement_en_cours
    input("Appuyez sur Entrée pour arrêter l'enregistrement...")
    enregistrement_en_cours = False


def record_audio(microphone_index):
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


def save_audio(microphone_index):
    frames = record_audio(microphone_index)
    wf = wave.open('enregistrement.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


mic = get_default_mic()
thread = threading.Thread(target=wait_user_entry)
thread.start()
save_audio(mic['index'])

thread.join()
