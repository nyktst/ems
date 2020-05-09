from django.contrib import admin
from poll.models import *

# Register your models here.
admin.site.register(Question) #this is to create menus in admin panel and the name should of in the models page
admin.site.register(Choice)
admin.site.register(Answer)

