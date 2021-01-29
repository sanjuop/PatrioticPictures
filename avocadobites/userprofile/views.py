from django.shortcuts import render

# Create your views here.

def usersList(request):
    return render(request, 'userprofile/test.html')
