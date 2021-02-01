
from django.urls import path
from userprofile.views import UsersList, UserDetail


urlpatterns = [
   path('', UsersList.as_view(), name="users_list"),
   path('<employee_code>/', UserDetail.as_view(), name="user_detail"),
]