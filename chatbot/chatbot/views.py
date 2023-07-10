from django.http import HttpResponse
from django.shortcuts import render
import openai

openai.api_key = "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"  # supply your API key however you choose\

temp_chat=[]
def chat(request):
    chats=""
    answer=""
    if (request.method == 'POST'):
        temp_chat =request.POST.get("chatSubmit",False)

        chats=temp_chat

        context = 'You are a grocery suggesting bot which suggests vegetables based on dish and its required recipe. You output only the items required not the recipe. \
                Hello,\
                We delivery between 10:00am - 7:00pm. \
                Return policy includes door step verification then followed by the transfer of the funds within 2-3 bussiness days.\
                Today special discount on all grains, buy 1 get 1 free, \
                We have three delivery categories namely - Instant Delivery(fastest),\
                One Day Delivery(semi-fast),Standard Delivery.'

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "system", "content": context},
                                                             {"role": "user",
                                                             "content": chats}])
        answer = completion.choices[0].message.content





    return render(request, "index.html",{'context':chats, "answer":answer})