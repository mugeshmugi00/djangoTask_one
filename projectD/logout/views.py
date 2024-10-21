from django.shortcuts import render

# Create your views here.
def logout(req):
    return render(req,"index_logout.html")