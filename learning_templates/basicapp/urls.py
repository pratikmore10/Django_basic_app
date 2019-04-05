from django.conf.urls import url
from django.urls import path, include
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('other/', views.other, name = 'other'),
    path('relative/', views.relative, name = 'relative')
]
