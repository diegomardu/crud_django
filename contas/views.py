from django.shortcuts import render
from .models import Transacao

# Create your views here.
def home(request):
    return render(request, 'contas/home.html')

def listar(request):
    transacoes = Transacao.objects.all()
    return render(request, 'contas/listar.html', {'transacoes':transacoes})