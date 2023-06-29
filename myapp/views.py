from django.shortcuts import render

# importamos los datos de la base de datos
from .models import TestSistemSolar

# Create your views here.
from django.shortcuts import render
from .forms import TestSistemSolar, TestMercurio

# librerias para desabilitar la memoria cache del navegador
from django.views.decorators.cache import never_cache
from django.http import HttpResponse


@never_cache
def deleteCache(request):
    response = HttpResponse("Contenido de la vista")
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


# Create your views here.
def index(request):
    return render(request, "index.html")


def planets(request):
    respuestas = {
        "ask1": "mercurio",
        "ask2": "57.91",
        "ask3": "4.879",
        "ask4": "427°C",
        "ask5": "5,43",
    }
    # si request.POST es un diccionario no vacio se guarda en form
    forms = TestMercurio(request.POST or None)
    answer = {}
    if request.method == "POST" and forms.is_valid():
        datosRespuesta = forms.cleaned_data
        for keys in datosRespuesta.keys():
            print(keys)
            answer[keys] = respuestas[keys] == datosRespuesta[keys]
            print(answer)
    else:
        forms = TestMercurio()

    return render(request, "layouts/planets.html", {"forms": TestMercurio(), "respuesta":answer})


def moons(request):
    return render(request, "layouts/moons.html")


def solarSistem(request):
    respuestas = {
        "ask1": "sol",
        "ask2": "1400000",
        "ask3": "75_hidrógeno_20_helio_5_oxígeno",
        "ask4": "saturno_jupiter",
        "ask5": "4568",
    }
    
    # si request.POST es un diccionario no vacio se guarda en form
    form = TestSistemSolar(request.POST or None)
    answer = {}
    if request.method == "POST" and form.is_valid():
        datosRespuesta = form.cleaned_data
        for keys in datosRespuesta.keys():
            answer[keys] = respuestas[keys] == datosRespuesta[keys]
    else:
        form = TestSistemSolar()

    return render(
        request,
        "layouts/solarSistem.html",
        {
            "form": form,
            "respuesta": answer,
        },
    )
