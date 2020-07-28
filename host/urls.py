from django.urls import path,include
from host import views


urlpatterns = [
    path('', views.index, name='index'),
    path('disk/',views.disk,name='disk'),
    path('users/',views.users,name='users'),
    path('diff/',views.diff,name='diff')
]
