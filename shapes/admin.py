from django.contrib import admin
from .models import Shape, DeleteThisTable
# Register your models here.

models = [
    Shape,
    DeleteThisTable
]

admin.site.register(models)
