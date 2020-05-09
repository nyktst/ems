#from django.db import models
#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#it is the class created to get and put data in db
class Question(models.Model):
    title = models.TextField(null=True,blank=True)
    status = models.CharField(default='inactive',max_length=10)
    Start_date =models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    created_by =models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE) #on delete is used to delete all data under this section if it deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #print title as string

    @property
    def choices(self):
        return self.choice_set.all() #to return all the choices


class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text #print text as string
    
    @property
    def votes(self):
        return self.answer_set.count()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name +'-'+ self.choice.text #print first name and text from choice class as string
    




