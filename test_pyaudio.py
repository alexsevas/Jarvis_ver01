import pyaudio
import wave

# Открытие файла WAV
filename = "test.wav"

# Открытие WAV файла
wf = wave.open(filename, 'rb')

# Инициализация PyAudio
p = pyaudio.PyAudio()

# Открытие потока для воспроизведения
stream = p.open(format=pyaudio.paInt16,
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

print("Воспроизведение...")

# Чтение и воспроизведение данных по частям
chunk = 1024
data = wf.readframes(chunk)

while data:
    stream.write(data)
    data = wf.readframes(chunk)

# Завершение воспроизведения
stream.stop_stream()
stream.close()
p.terminate()

print("Воспроизведение завершено")