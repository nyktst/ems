from django.contrib import admin
from poll.models import *

# Register your models here.
admin.site.register(question)
admin.site.register(Choice)
