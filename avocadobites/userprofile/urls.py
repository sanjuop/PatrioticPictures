
from django.urls import path
from userprofile.views import usersList, userDetail


urlpatterns = [
   path('', usersList, name="users_list"),
   path('<int:id>/', userDetail, name="user_detail"),
]