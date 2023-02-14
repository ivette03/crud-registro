from django.forms import ModelForm
from .models import estudiantes

class estudiantesForm(ModelForm):
    class Meta():
        model=estudiantes
        exclude=('date',)