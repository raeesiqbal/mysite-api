import imp
from multiprocessing import context
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Data
import requests
from requests.auth import HTTPBasicAuth


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            if Data.objects.all()[:1].get():
                get_data = Data.objects.all()[:1].get()
                url = get_data.domain + get_data.api
                print(url)
                response = requests.get(
                    url, auth=HTTPBasicAuth(username=username, password=password)
                )
                print(response)
                if response.status_code == 200:
                    context = {"status_code": response.status_code}
                    return render(request, "filepicker.html", context=context)
                else:
                    context = {"msg": "Please provide valid credentials"}
                    return render(request, "home.html", context=context)
            else:
                return render(request, "home.html")
