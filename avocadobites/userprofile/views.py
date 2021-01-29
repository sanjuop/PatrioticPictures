from django.shortcuts import render
from userprofile.models import Profile

# Create your views here.

def usersList(request):
    all_users = Profile.objects.all()
    context_data = {
            'all_users': all_users
            }
    return render(request, 'userprofile/users_list.html', context_data)


def userDetail(request, id):
    Puser = Profile.objects.get(user__id=id)
    context_data = {
            'user': Puser
            }
    return render(request, 'userprofile/user_detail.html', context_data)