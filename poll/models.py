#from django.db import models
#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class question(models.Model):
    title = models.TextField(null=True,blank=True)
    status = models.CharField(default='inactive',max_length=10)
    Start_date =models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    created_by =models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title

class Choice(models.Model):
    Question = models.ForeignKey('poll.question', on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    




