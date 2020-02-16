from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request):
        #object_list = ProfileEditView.objects.all()
        return render(request, 'home/home.html', )


class SiteLoginView(LoginView):
    template_name = 'profile/login.html'

class SiteLogoutView(LogoutView):
    next_page='/'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('full_name', 'address', 'dob', 'gender', 'about', 'phone_number')
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('profile')  # Trả về 1 chuỗi, chuỗi đó là đường dẫn và chuyển tới trang profile

    def get_object(self, queryset=None):
        return self.request.user




