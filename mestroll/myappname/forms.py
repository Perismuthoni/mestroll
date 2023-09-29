from django.forms import ModelForm
from .models import Classe


class ClasseForm(ModelForm):
    class Meta:
        model = Classe
        fields = ("user_id", "classroom", "lat", "long", "elevation")
