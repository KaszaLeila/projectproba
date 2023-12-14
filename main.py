from sys import byteorder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pyaudio
from array import array
from struct import pack
import wave
import os
import pickle
import soundfile
import numpy as np
import librosa
from sklearn.neural_network import MLPClassifier


class SpeechEmotionRecognitionApp(App):
    def build(self):
        self.title = 'Speech Emotion Recognition'

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.record_button = Button(text='Start Recording', on_press=self.toggle_recording)
        layout.add_widget(self.record_button)

        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        self.recording = False
        self.filename = 'test.wav'

        self.p = pyaudio.PyAudio()
        self.stream = None  # Hozzáadva a stream változó

        return layout

    def extract_feature(self, file_name, **kwargs):
        mfcc = kwargs.get("mfcc")
        chroma = kwargs.get("chroma")
        mel = kwargs.get("mel")
        contrast = kwargs.get("contrast")
        tonnetz = kwargs.get("tonnetz")

        with soundfile.SoundFile(file_name) as sound_file:
            X = sound_file.read(dtype="float32")
            sample_rate = sound_file.samplerate

            if chroma or contrast:
                stft = np.abs(librosa.stft(X))

            result = np.array([])

            if mfcc:
                mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
                result = np.hstack((result, mfccs))

            if chroma:
                chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
                result = np.hstack((result, chroma))

            if mel:
                mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
                result = np.hstack((result, mel))

            if contrast:
                contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
                result = np.hstack((result, contrast))

            if tonnetz:
                tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T, axis=0)
                result = np.hstack((result, tonnetz))

        return result

    def toggle_recording(self, instance):
        if self.recording:
            self.stop_recording()
            self.show_result()
        else:
            self.start_recording()

    def start_recording(self):
        self.record_button.text = 'Stop Recording'
        self.recording = True

        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        RATE = 16000

        self.stream = self.p.open(format=FORMAT, channels=1, rate=RATE,
                                  input=True, output=True,
                                  frames_per_buffer=CHUNK_SIZE)

        self.record_to_file(self.filename)

    def stop_recording(self):
        self.record_button.text = 'Start Recording'
        self.recording = False

        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()

    def record_to_file(self, path):
        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        RATE = 16000
        SILENCE = 30
        THRESHOLD = 500  # Hozzáadva a THRESHOLD változó

        def normalize(snd_data):
            MAXIMUM = 16384
            times = float(MAXIMUM) / max(abs(i) for i in snd_data)

            r = array('h')
            for i in snd_data:
                r.append(int(i * times))
            return r

        def trim(snd_data):
            snd_started = False
            r = array('h')

            for i in snd_data:
                if not snd_started and abs(i) > THRESHOLD:
                    snd_started = True
                    r.append(i)
                elif snd_started:
                    r.append(i)
            return r

        def add_silence(snd_data, seconds):
            r = array('h', [0 for i in range(int(seconds * RATE))])
            r.extend(snd_data)
            r.extend([0 for i in range(int(seconds * RATE))])
            return r

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=1, rate=RATE,
                        input=True, output=True,
                        frames_per_buffer=CHUNK_SIZE)

        num_silent = 0
        snd_started = False
        r = array('h')

        while 1:
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            silent = max(snd_data) < THRESHOLD

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True
                r.append(snd_data[0])
            elif snd_started:
                r.append(snd_data[0])

            if snd_started and num_silent > SILENCE:
                break

        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = normalize(r)
        r = trim(r)
        r = add_silence(r, 0.5)
        data = pack('<' + ('h' * len(r)), *r)

        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()

    def show_result(self):
        features = self.extract_feature(self.filename, mfcc=True, chroma=True, mel=True).reshape(1, -1)
        result = model.predict(features)[0]
        self.result_label.text = f'Result: {result}'


if __name__ == '__main__':
    model_path = "result/mlp_classifier.model"
    model = pickle.load(open(model_path, "rb"))
    SpeechEmotionRecognitionApp().run()
