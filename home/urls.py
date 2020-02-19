from django.urls import path
from home import views
from home.views import (
    ListMenuView,
    CreateMenuView,
    UpdateMenuView,
    DetailMenuView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', ListMenuView.as_view(), name='list-menus'),
    path('create-menu/', CreateMenuView.as_view(), name='create-menu'),
    path('update-menu/<int:pk>', UpdateMenuView.as_view(), name='update-menu'),
    path('detail-menu/<int:pk>/', DetailMenuView.as_view(), name='detail-menu'),
]
