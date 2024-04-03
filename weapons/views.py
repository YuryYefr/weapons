from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Weapon
from django.contrib.sessions.models import Session
from django.views.generic import DetailView as DV, ListView as LV, CreateView as CV
from .filter import WeaponsFilter
from .forms import WeaponForm
# from User.models import User
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
        return len(user_id_list)
        # return User.objects.filter(id__in=user_id_list)


def online_users():
    queryset = get_current_users()
    if queryset is None:
        ctx = 0
    else:
        ctx = queryset
    return ctx


def viewers_counter(request):
    return JsonResponse({'counter': Session.objects.filter(expire_date__lte=timezone.now()).count()})


def about(request):
    return render(request, 'weapons/about.html')


class WeaponsList(LV):
    """List of models with pagination"""
    model = Weapon
    template_name = 'weapons/home.html'
    context_object_name = 'model'
    paginate_by = 5
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(WeaponsList, self).get_context_data(**kwargs)
        return ctx

    def get_queryset(self):
        ctx = super(WeaponsList, self).get_queryset()
        return ctx.filter(weapon_type=self.request.path.replace('/', '') or 'hand_carried_gun')


class FilterList(LV):
    """search logic"""
    model = Weapon
    template_name = 'weapons/search.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter'] = WeaponsFilter(self.request.GET, queryset=self.get_queryset())
        return ctx


class WeaponDetail(DV):
    """detailed view of every model"""
    model = Weapon
    template_name = 'weapons/detail.html'


class WeaponCreate(CV):
    model = Weapon
    template_name_suffix = '_create_form'
    form_class = WeaponForm
