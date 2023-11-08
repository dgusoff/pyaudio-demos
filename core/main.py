import wave
import time
import sys

import pyaudio

p = pyaudio.PyAudio()
print('hey')

info = p.get_device_count()
#info = p.get_default_output_device_info()
print(info)

for x in range(0, info):
    #print("We're on time %d" % (x))
    data = p.get_device_info_by_index(x)
    print(data)
    print(f"{x} - {data['defaultSampleRate']} - {data['name']} - {data['hostApi']}")
