from django.shortcuts import render
from home.models import Menu
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

from .forms import CreateMenuForm


# Create your views here.

def index(request):
    menuParents = Menu.objects.filter(id_parent=0)

    context = {
        'parents': menuParents
    }
    return render(request, 'home/index.html', context)


class ListMenuView(ListView):
    model = Menu
    paginate_by = 2
    def get(self, request, *args, **kwargs):
        template_name = 'menus/list-menu.html'  # sẽ được tạo ở phần dưới
        # Rename Model objects default to namenew
        obj = {
            'menus': Menu.objects.all()
        }
        return render(request, template_name, obj)


class CreateMenuView(SuccessMessageMixin, CreateView):
    template_name = 'menus/create-menu.html'
    form_class = CreateMenuForm
    success_message = 'Create Menu successfully!'


class UpdateMenuView(SuccessMessageMixin, UpdateView):
    template_name = 'menus/update-menu.html'
    model = Menu
    fields = ['name', 'description', ]
    success_message = 'Update Menu successfully!'

    def get_success_url(self):
        return reverse('list-menus', kwargs={})


class DetailMenuView(SuccessMessageMixin, DetailView):
    # Default model is object
    model = Menu
    template_name = 'menus/detail-menu.html'
