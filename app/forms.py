from django.forms import ModelForm

from app.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['modelo', 'marca', 'ano']
