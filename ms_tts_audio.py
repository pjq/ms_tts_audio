import argparse
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def ms_tts(text, filename, subscription_key, service_region):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

    audio_config = AudioOutputConfig(filename=f"{filename}.mp3")
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")


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

    ms_tts(text, options.filename, options.subscription_key, options.service_region)
