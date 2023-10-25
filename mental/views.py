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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは会話相手の心を癒してください。また、会話を続けるようにユーザーに質問を問うてください。つらい、しんどいなどの言葉がきたら、大丈夫と言ってください。"},
            {"role": "user", "content": user_message}
        ],
    )
    bot_response = response.choices[0].message["content"]
    return JsonResponse({'message': bot_response})

def index_view(request):
    return render(request, 'mental/index.html')