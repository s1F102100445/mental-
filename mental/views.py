import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import wave
import pyaudio
import json
MAX_TOKENS = 200
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

def openWave2():
    wf = wave.open("./test2.wav", "r")

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
            {"role": "system", "content": "Please keep your answers short and concise (40 words or less). You are the kind sister who heals the user's mental health. Please use polite language. Please comfort the user when negative words such as hard, tough, etc. come, and sympathize with the user's words. Please speak in Japanese."},
            {"role": "user", "content": user_message},
        ],
        max_tokens = MAX_TOKENS
    )
    bot_response = response.choices[0].message["content"]

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
    if bot_response.endswith(('.', '。', '?', '？', '!', '！')):
        if voicevox_response.status_code == 200:
            audio_data = voicevox_response.content  # 音声データを取得

            with open('./test.wav', 'wb') as audio_file:
                audio_file.write(audio_data)
            openWave()
            return HttpResponse(json.dumps({'message': bot_response}), content_type="application/json")
    else:
        if voicevox_response.status_code == 200:
            audio_data = voicevox_response.content  # 音声データを取得

            with open('./test.wav', 'wb') as audio_file:
                audio_file.write(audio_data)
            openWave()
            return HttpResponse(json.dumps({'message': bot_response + "...(続く)"}), content_type="application/json")

def index2(request):
    voicevox_api_key = 'Q_71a0y24-E_607'
    openai.api_key = 'vFdJode_WToN5fvInVNyaYdkuZ88-BRSSNI-r6nSRqb8bTOl8erUZ_vYfI4XGtwqgujt5JtJp5baJSUeMvVZErg'
    openai.api_base = 'https://api.openai.iniad.org/api/v1'

    user_message = request.POST.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a jolly nice young man. Please speak in Japanese. Please stop using polite language. Talk to me in a friendly way like a friend Also, please keep your output short and concise."},
            {"role": "user", "content": user_message}
        ],
        max_tokens = MAX_TOKENS
    )
    bot_response = response.choices[0].message["content"]

    voicevox_response = requests.get(
    'https://deprecatedapis.tts.quest/v2/voicevox/audio/',
    params={
        'key': voicevox_api_key,
        'speaker': 11,
        'pitch': 0.07,
        'intonationScale': 1,
        'speed': 1,
        'text': bot_response
    }
)

    if bot_response.endswith(('.', '。', '?', '？', '!', '！')):
        if voicevox_response.status_code == 200:
            audio_data = voicevox_response.content  # 音声データを取得

            with open('./test.wav', 'wb') as audio_file:
                audio_file.write(audio_data)
            openWave()
            return HttpResponse(json.dumps({'message': bot_response}), content_type="application/json")
    else:
        if voicevox_response.status_code == 200:
            audio_data = voicevox_response.content  # 音声データを取得

            with open('./test.wav', 'wb') as audio_file:
                audio_file.write(audio_data)
            openWave()
            return HttpResponse(json.dumps({'message': bot_response + "...(続く)"}), content_type="application/json")
            
def index_view(request):
    return render(request, 'mental/index.html')

def index_view2(request):
    return render(request, 'mental/index2.html')

def index_main(request):
    return render(request, 'mental/main.html')

def index_char(request):
    return render(request, 'mental/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'mental/register.html', {'form': form})
