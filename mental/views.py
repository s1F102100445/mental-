import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import wave
import pyaudio
import json
# Create your views here.



def openWave():
    wf = wave.open("./test.wav", "r")

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    chunk = 1024
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()

@csrf_exempt
def index(request):
    voicevox_api_key = 'Q_71a0y24-E_607'
    openai.api_key = 'vFdJode_WToN5fvInVNyaYdkuZ88-BRSSNI-r6nSRqb8bTOl8erUZ_vYfI4XGtwqgujt5JtJp5baJSUeMvVZErg'
    openai.api_base = 'https://api.openai.iniad.org/api/v1'

    user_message = request.POST.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは会話相手の心を癒してください。また、会話を続けるようにユーザーに質問を問うてください。つらい、しんどいなどの言葉がきたら、大丈夫と言ってください,敬語を控えるように明るくふるまってください)"},
            {"role": "user", "content": user_message}
        ],
    )
    bot_response = response.choices[0].message["content"]

    # Use the VOICEVOX API to convert the text response into speech
    voicevox_response = requests.get(
    'https://deprecatedapis.tts.quest/v2/voicevox/audio/',
    params={
        'key': voicevox_api_key,
        'speaker': 0,
        'pitch': 0,
        'intonationScale': 1,
        'speed': 1,
        'text': bot_response
    }
)

    if voicevox_response.status_code == 200:
        # If the response is successful, get the audio URL
        audio_data = voicevox_response.content  # 音声データを取得

        with open('./test.wav', 'wb') as audio_file:
            audio_file.write(audio_data)
        openWave()
        return HttpResponse(json.dumps({'message': bot_response}), content_type="application/json")

def index_view(request):
    return render(request, 'mental/index.html')