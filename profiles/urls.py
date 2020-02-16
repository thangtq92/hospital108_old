from django.urls import path
from profiles import views

urlpatterns = [
    # path('', views.HomeView.as_view(), name='index'),
    path('login/', views.SiteLoginView.as_view(), name='login'),
    path('logout/', views.SiteLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileEditView.as_view(), name='profile'),
]
