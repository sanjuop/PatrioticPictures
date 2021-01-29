from django.shortcuts import render, get_object_or_404
from userprofile.models import Profile
from django.views.generic import (View, ListView, DetailView)
from django.contrib.auth.models import User
                                

# Create your views here.


class UsersList(ListView):
    context_object_name = 'all_users'
    model = Profile
    paginate_by = 2

class UserDetail(DetailView):
    context_object_name = 'user'
    model = Profile
    template_name = 'userprofile/user_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, id=self.kwargs["id"]-1)


# def userDetail(request, id):
#     Puser = Profile.objects.get(user__id=id)
#     context_data = {
#             'user': Puser
#             }
#     return render(request, 'userprofile/user_detail.html', context_data)



# def usersList(request):
#     all_users = Profile.objects.all()
#     context_data = {
#             'all_users': all_users
#             }
#     return render(request, 'userprofile/users_list.html', context_data)


# def userDetail(request, id):
#     Puser = Profile.objects.get(user__id=id)
#     context_data = {
#             'user': Puser
#             }
#     return render(request, 'userprofile/user_detail.html', context_data)