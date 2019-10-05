import json

from django.shortcuts import render


def home(request):
    p1 = open("app/static/data/eurocv.json", "r")
    p2 = open("app/static/data/eurocv2.json", "r")
    person1 = json.loads(p1.readlines())
    tparams = {
        'person1': person1["personalInfo"]["name"]["Fernanda"],
        'person2': 'Miguel'
    }
    return render(request, "layout.html", tparams)
