## Text-to-Speech with Microsoft Azure Cognitive Services
This script allows you to convert text to speech(mp3) using Microsoft Azure Cognitive Services.

## Requirements
- Python 3.x
- azure-cognitiveservices-speech library

```shell
pip install -r requirements.txt
```
## Usage
```shell
usage: main.py [-h] --subscription_key SUBSCRIPTION_KEY --service_region SERVICE_REGION [--text TEXT] [--filename FILENAME]
optional arguments:
  -h, --help            show this help message and exit
  --text TEXT           text to synthesize
  --filename FILENAME   output audio file name
  --subscription_key SUBSCRIPTION_KEY
                        subscription key
  --service_region SERVICE_REGION
                        service region
```
## Example
```shell
python ms_tts_audio.py --subscription_key "xxxxxxxxxxxxxxxxxxxxxxxxx" --service_region "eastasia" --text "hello world"
```

```shell
python ms_tts_audio.py  --subscription_key "xxxxxxxxxxxxxxxxxxxxxxxx" --service_region "eastasia" --file input.txt
```
This will create an audio file named output.mp3 with the speech synthesis of the text hello world.