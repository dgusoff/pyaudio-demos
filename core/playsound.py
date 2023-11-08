"""PyAudio Example: Play a wave file."""

import wave
import sys

import pyaudio

CHUNK = 1024

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    ch = wf.getnchannels()
    print(ch)
    index = 0
    data = p.get_device_info_by_index(index)

    def2 = p.get_default_output_device_info()
    print(def2)
    

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=int(data['defaultSampleRate']),
                    output=True
                    ,output_device_index=0
                    )

    # Play samples from the wave file (3)
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()