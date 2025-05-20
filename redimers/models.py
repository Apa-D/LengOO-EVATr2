import uuid
import time
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def default_time():
    return int(time.time() * 1000)

def validate(value):
    #Valida que el contenido no este vacio
    if not value.strip():
        raise ValidationError(_('El contenido no puede estar vacío ni consistir solo de espacios.'),code='empty_or_spaces')

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.CharField(max_length=120,validators=[validate])
    createdAt = models.BigIntegerField(default=default_time)
    important = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.id}-{self.createdAt} - {self.content} - Completado:{self.important} "
