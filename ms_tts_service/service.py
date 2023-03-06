import argparse
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

def ms_tts(text, output_filename, subscription_key, service_region, speech_synthesis_voice_name="zh-CN-XiaoxiaoNeural"):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    # speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
    speech_config.speech_synthesis_voice_name = speech_synthesis_voice_name

    audio_config = AudioOutputConfig(filename=f"{output_filename}.mp3")
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

