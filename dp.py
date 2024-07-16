# -*- coding: utf-8 -*-

from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import json
import config

def recognize_local(filename):
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(config.DEEPGRAM_SECRET_KEY)

        with open(filename, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language="ru",
            diarize=True,
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        #print(response.to_json(indent=4))
        with open('result.json', 'w') as f:
            f.write(response.to_json(indent=4))
        #res  = response.to_json(indent=4)['results']['channels'][0]['alternatives'][0]['paragraphs']
        res  = response.to_json()
        paragrafs = json.loads(res)['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
        
        #print(res)
        #for word in res:
        #    speeker = word['speaker']
        #    word = word['punctuated_word']
        #    print(f'{speeker}: {word}')
        return paragrafs

    except Exception as e:
        print(f"Exception: {e}")
    
def recognize_url(url):
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(config.DEEPGRAM_SECRET_KEY)

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language="ru",
            diarize=True,
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_url(url, options)

        res  = response.to_json()
        paragrafs = json.loads(res)['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
        
        return paragrafs

    except Exception as e:
        print(f"Exception: {e}")
