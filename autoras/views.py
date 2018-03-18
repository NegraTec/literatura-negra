from django.shortcuts import render
from .models import Autoras

def index(request):
    # caso de uso retorna tipo info
    # servico deveria saber como converter info para django model?
    autoras = Autoras.objects.all()
    return render(request, 'autoras/base.html', {'autoras': autoras})
