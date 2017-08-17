from django.shortcuts import render
from .models import Autoras

def index(request):
    autoras = Autoras.objects.all()
    return render(request, 'autoras/base.html', {'autoras': autoras})
