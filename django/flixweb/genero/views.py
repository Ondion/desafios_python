from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponseNotAllowed

# Create your views here.

def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
        else:
            print('ERROR')
    generos_list = models.Genero.objects.order_by('descricao')
    data_dict = {'form': form, 'generos_records': generos_list}
    return render(request, 'genero/genero.html', data_dict)


def delete(request, id):
    try:
        models.Genero.objects.filter(id=id).delete()
        form = forms.GeneroForm()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()
