from django.shortcuts import render
from home.models import Menu

# Create your views here.

def index(request):

    menuParents = Menu.objects.filter(id_parent = 0)

    context = {
        'parents': menuParents
    }
    return render(request, 'home/index.html', context)
