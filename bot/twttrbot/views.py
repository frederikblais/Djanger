from typing import Reversible
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
import json

# Returns index.html
class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

# Returns bot.html
class Bot(View):
    template = 'bot.html'

    def get(self, request):
        return render(request, self.template)

    # Bot POST

    # (TODO) Fred: send parameters (num of tweets) -> run_script
    # 
    def post(self, request):
        if request.method == 'POST' and 'run_script' in request.POST:
            json_stuff = json.dumps({"list_of_jsonstuffs" : ["a", "b"]})  
              
        return HttpResponse(json_stuff, content_type ="application/json")
        