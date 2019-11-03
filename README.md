# Matric Voice Skill

## How to enable matrix voice on Onyx

First, you need to install all Matrix Voice dependencies : 

```
curl https://apt.matrix.one/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.matrix.one/raspbian $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/matrixlabs.list
sudo apt-get update
sudo apt-get upgrade
sudo reboot
sudo apt install matrixio-kernel-modules
sudo reboot
```

In onyx/client/speech/assets you have to modify snowboydecoder.py : 

From

```
self.stream_in = self.audio.open(
input=True, output=False,
format=self.audio.get_format_from_width(
self.detector.BitsPerSample() / 8),
channels=self.detector.NumChannels(),
rate=self.detector.SampleRate(),
frames_per_buffer=2048,
stream_callback=audio_callback)
```

To 

```
self.stream_in = self.audio.open(
input=True, output=False,
format=self.audio.get_format_from_width(
self.detector.BitsPerSample() / 8),
channels=MV_CHANNELS,
rate=self.detector.SampleRate(),
frames_per_buffer=2048,
stream_callback=audio_callback,
input_device_index = MV_INDEX)
```

And change MV_INDEX (3 for me), and MV_CHANNELS (1 for me)

Finally, you have to select the device in onyx/client/speech/main.py

```
sr.Microphone(device_index=3)
```