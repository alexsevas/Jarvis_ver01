import os
import torch

# print(f'Your PyTorch work on CUDA device: {torch.cuda.get_device_name(0)}')

device = torch.device('cuda')
torch.set_num_threads(4)
local_file = 'model.pt'

# Если в папке с проектом отсутствует model.pt, то качаем
if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text = 'В недрах тундры выдры в г+етрах т+ырят в вёдра +ядра к+едров. Раз, два, три, четыри, пять - вышел зайчик погулять!'
sample_rate = 48000
speaker = 'xenia' # aidar, baya, kseniya, xenia, eugene, random

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)
