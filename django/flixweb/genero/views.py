from django.shortcuts import render
from . import forms

# Create your views here.

def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'Post':
        print('Vou salvar os dados')
        form = forms.GeneroForm(request.POST)
        print(form)
        if form.is_valid():
            form.save(commit = True)
        else:
            print('ERROR')
    data_dict = {'form': form}
    return render(request, 'genero/genero.html', data_dict)
