from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json
import urllib
import requests


def home_view(req):
    return  HttpResponse("hello teja")

@csrf_exempt
def compile(request,code="",language="-1",input=""):
    if request.method=="POST":
        data_from_post = json.load(request)['post_data']
        #print(data_from_post)
        code=data_from_post.get('code',"")
        user_input=data_from_post.get('input',"")
        language=data_from_post.get('language',"")
        print("user input",user_input)
        COMPILE_URL = 'https://api.hackerearth.com/v3/code/compile/'
        RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
        CLIENT_SECRET="7b9e5877ccb804b9ae5e690c33e47fcfc72d31ec"
        source="print(20)"
        data = {
            'client_secret': CLIENT_SECRET,
            'async': 0,
            'source': code,
            'lang': language,
            'time_limit': 5,
            'memory_limit': 262144,
            'input':user_input
        }

        r = requests.post(RUN_URL, data=data)
        print(r.json(),type(r.json()))
        resp=r.json()
        return JsonResponse(resp)
    
    return JsonResponse({"msg":"get req"})


