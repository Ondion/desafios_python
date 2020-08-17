from django import forms
from genero.models import Genero

class GeneroForm(forms.ModelForm):

    class Meta:
        model = Genero
        fields = '__all__'


    # def __init__(self, *args, **kwargs):
    #     super(GeneroForm, self).__init__(*args, **kwargs)
    #     self.fields['descricao'].error_messages = {'required' : 'Campo Obrigatório'}
    #
    # descricao = forms.CharField(label='Gênero', required=True)