from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
# Create your views here.
@csrf_exempt
def index(request):
    openai.api_key = 'vFdJode_WToN5fvInVNyaYdkuZ88-BRSSNI-r6nSRqb8bTOl8erUZ_vYfI4XGtwqgujt5JtJp5baJSUeMvVZErg'
    openai.api_base = 'https://api.openai.iniad.org/api/v1'
   
    user_message = request.POST.get('message') 
    conversation = request.session.get('conversation', [])     # これまでの会話をセッションから取得
    conversation.append(user_message)     # ユーザーのメッセージを会話に追加
    prompt = " ".join(conversation)     # コンテキストとしてプロンプトを作成
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    bot_response = response.choices[0].message["content"]     # Botの応答を会話に追加
    conversation.append(bot_response)
    request.session['conversation'] = conversation     # 更新された会話をセッションに保存
    return JsonResponse({'message': bot_response})

def index_view(request):
    return render(request, 'mental/index.html')