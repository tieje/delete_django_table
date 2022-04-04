from django.db.models import Model, AutoField, IntegerField
from django.forms import CharField

# Create your models here.
class Shape(Model):
    id: AutoField = AutoField(primary_key=True)
    name: CharField = CharField(max_length=100)
    points: IntegerField = IntegerField(null=True, blank=True)

class DeleteThisTable(Model):
    id: AutoField = AutoField(primary_key=True)
    name: CharField = CharField(max_length=10)
