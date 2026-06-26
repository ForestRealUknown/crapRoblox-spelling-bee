import pyaudio
import wave
import sys
import transcriber
import typeOut
from pynput.keyboard import Key, Listener


CHUNK = 2048
FORMAT = pyaudio.paInt24
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 4
OUTPUT_FILENAME = "desktop_audio.wav"

p = pyaudio.PyAudio()



def show(key):
        if key == Key.ctrl_l:
                print("Finding G432 Gaming Headset...")
                
                # Enumerate all devices to find G432 Gaming Headset
                device_index = None
                for i in range(p.get_device_count()):
                        info = p.get_device_info_by_index(i)
                        if info['maxInputChannels'] > 0:
                                device_name = info['name'].lower()
                                # Look for G432 Gaming Headset
                                if 'g432' in device_name:
                                        device_index = i
                                        print(f"Found G432 Gaming Headset: {info['name']}")
                                        break
                
                if device_index is None:
                        print("G432 Gaming Headset not found. Make sure it's connected.")
                        return

                print("Recording from: G432 Gaming Headset")

                stream = p.open(
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=CHUNK
                )

                print("Recording...")
                frames = []

                for _ in range(int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK, exception_on_overflow=False)
                    frames.append(data)

                print("Done")

                stream.stop_stream()
                stream.close()

                with wave.open(OUTPUT_FILENAME, "wb") as wf:
                    wf.setnchannels(CHANNELS)
                    wf.setsampwidth(p.get_sample_size(FORMAT))
                    wf.setframerate(RATE)
                    wf.writeframes(b"".join(frames))

                print(f"Saved to {OUTPUT_FILENAME}")

                try:
                        transcript = transcriber.transcribe()

                        print(transcript)

                        transcript = transcript.split()
                        typeOut.type(transcript[-1])
                except:
                        print("Transcription failed")
        if key == Key.esc:
                return False
        
with Listener(on_press=show) as listener:
       listener.join()