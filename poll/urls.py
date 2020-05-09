
from django.urls import path
#instead of writing vews.method name simply import the view
from poll.views import index,details

urlpatterns = [
    path('', index,name='poll_list'),
    path('<int:id>/details',details,name='poll_details'), #<int:id> is an data passed with the argument ,refer view page
    
]

