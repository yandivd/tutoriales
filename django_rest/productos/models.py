from django.db import models
from base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion', max_length=50, unique=True)
    historical = HistoricalRecords()

    def __str__(self):
        return self.description
    