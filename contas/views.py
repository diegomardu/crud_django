from django.shortcuts import redirect, render
from .models import Transacao
from .form import TransacaoForm

# Create your views here.
def home(request):
    return render(request, 'contas/home.html')

def listar(request):
    transacoes = Transacao.objects.all()
    return render(request, 'contas/listar.html', {'transacoes':transacoes})

def nova_despesa(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'contas/form.html', {'form':form})

def atualizar(request,pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'contas/form.html', {'form':form, 'transacao':transacao})

def deletar(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('listar')

    
