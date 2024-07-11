# main.py (python example)

import os
from dotenv import load_dotenv

from deepgram import DeepgramClient, PrerecordedOptions, FileSource

load_dotenv()

# URL to the audio file
AUDIO_URL = {
    "url": "https://api.zadarma.com/v1/pbx/record/download/b16ad7b9429f9a02989e940f6a83eadcc82f7b07af98fed25cf42c310efd85e7/423a0bc27e0d90ad23e131d0f996ece1c3712c521ea80961066ee480ede95979/384776-1720099131.1157906-102-2024-07-04-161851.ogg"
}

#API_KEY = os.getenv("DG_API_KEY")
API_KEY = 'bbf312f3611a87b961cb1ceb1eff1710a18eea99'

def recognize_local(filename):
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        with open(filename, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")
        
def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_url method with the audio payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    #main()
    recognize_local('call.ogg')
