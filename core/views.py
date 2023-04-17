from django.shortcuts import redirect, render
from .models import Pessoa
from .forms import PessoaForm
from googlesearch import search


def home(request): 
    res = None
    if request.method == "POST":
        pergunta = request.POST.get('pergunta')

        for res in search(pergunta):
            resposta = res
    return render(request, 'home.html', {'resposta': res})


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    return redirect('core_lista_pessoas')

def editar_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'editar_pessoa.html', data)


def deletar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    return render(request, 'pessoa-deleta-confirm.html', {'pessoa': pessoa})

def funny(request):
    funny = 'imagem'
    return render(request, 'funny.html', {'funny': funny})



