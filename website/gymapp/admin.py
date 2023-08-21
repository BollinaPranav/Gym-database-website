from django.contrib import admin
from .models import Client
from .models import Trainers

# Register your models here.
admin.site.register(Client)
admin.site.register(Trainers)
