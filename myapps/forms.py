from django import forms

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200, required=True)