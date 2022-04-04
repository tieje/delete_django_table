from django.contrib import admin
from .models import Shape
# Register your models here.

models = [
    Shape
]

admin.site.register(models)
