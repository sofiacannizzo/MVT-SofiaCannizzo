from django.shortcuts import render
from django.http import HttpResponse
from EntregaCoderApp.models import *
from django.template import Template, Context

# Create your views here.
def familia(request):
    familiares = Familiar.objects.all()
    print(familiares)
    return render(request, "index.html", {"familia": familiares})