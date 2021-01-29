
from django.urls import path
from userprofile.views import usersList


urlpatterns = [
   path('', usersList, name="users_list")
]