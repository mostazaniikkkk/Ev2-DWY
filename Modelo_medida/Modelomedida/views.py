from django.http import HttpResponse
import datetime
from django.template import Template, Context

def modeloMedida(request):

    doc_externo=open("C:/Users/Renato/Desktop/Modelo Medida/plantillas/miplantilla.html")
    
    plt=Template(doc_externo.read())

    ctx=Context()

    documento=plt.render(ctx)

    documento=plt.render(ctx)
    return HttpResponse(documento)