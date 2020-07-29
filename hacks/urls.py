from django.urls import path
from . import views

app_name = 'hack'

urlpatterns = [
    path('', views.all_hacks, name='all_hacks'),
    path('<int:hack_id>', views.detail, name='detail'),
]