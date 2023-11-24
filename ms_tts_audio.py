import argparse
from ms_tts_service import service as text2mp3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", dest="text", type=str, default=None, help="text to synthesize")
    parser.add_argument("--input", dest="inputfile", type=str, default=None, help="input file to read text from")
    parser.add_argument("--output", dest="output", type=str, default="output", help="output audio file name")
    parser.add_argument("--subscription_key", dest="subscription_key", type=str, required=True, help="subscription key")
    parser.add_argument("--service_region", dest="service_region", type=str, required=True, help="service region")
    options = parser.parse_args()

    if options.text:
        text = options.text
    elif options.inputfile:
        with open(options.inputfile, "r") as file:
            text = file.read()
    else:
        raise ValueError("Either a text or a valid inputfile must be provided.")



import argparse
from ms_tts_service import service as text2mp3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", dest="text", type=str, default=None, help="text to synthesize")
    parser.add_argument("--input", dest="inputfile", type=str, default=None, help="input file to read text from")
    parser.add_argument("--output", dest="output", type=str, default="output", help="output audio file name")
    parser.add_argument("--subscription_key", dest="subscription_key", type=str, required=True, help="subscription key")
    parser.add_argument("--service_region", dest="service_region", type=str, required=True, help="service region")
    parser.add_argument("--voice_name", dest="voice_name", type=str, default="zh-CN-YunyangNeural", help="voice name for tts engine")
    options = parser.parse_args()

    if options.text:
        text = options.text
    elif options.inputfile:
        with open(options.inputfile, "r") as file:
            text = file.read()
    else:
        raise ValueError("Either a text or a valid inputfile must be provided.")

    # text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-XiaoxiaoNeural")
    # text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-liaoning-XiaobeiNeural")
    # text2mp3.ms_tts(text, options.filename, options.subscription_key, options.service_region, "zh-CN-YunyangNeural")
    # text2mp3.ms_tts(text, options.output, options.subscription_key, options.service_region, "zh-CN-YunyangNeural")
    text2mp3.ms_tts(text, options.output, options.subscription_key, options.service_region, options.voice_name)
