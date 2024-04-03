from django.urls import path
from . import views
from .views import WeaponDetail, WeaponsList, FilterList, WeaponCreate

app_name = 'weapons'
urlpatterns = [
    path('', WeaponsList.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('model/<int:pk>/', WeaponDetail.as_view(), name='detail'),
    path('search', FilterList.as_view(), name='search'),
    path('create', WeaponCreate.as_view(), name='model_create'),
    path('count-viewers', views.viewers_counter),
    path('<str>', WeaponsList.as_view(), name='weapon_type'),
]
