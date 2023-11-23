import argparse
from ms_tts_service import service as text2mp3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", dest="text", type=str, default=None, help="text to synthesize")
    parser.add_argument("--filename", dest="filename", type=str, default="output", help="output audio file name")
    parser.add_argument("--subscription_key", dest="subscription_key", type=str, required=True, help="subscription key")
    parser.add_argument("--service_region", dest="service_region", type=str, required=True, help="service region")
    options = parser.parse_args()

    if options.text:
        text = options.text
    else:
        filename = options.filename
        with open(filename, "r") as file:
            text = file.read()

    # text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-XiaoxiaoNeural")
    # text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-liaoning-XiaobeiNeural")
    text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-YunyangNeural")
