from django.forms import ModelForm
from .models import Reminder

class Redimerform(ModelForm):

    class Meta:
        model = Reminder
        fields = ["context","important" ]
    