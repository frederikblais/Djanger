from typing import Reversible
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

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
