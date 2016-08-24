
from django.conf.urls import url
from contact.app import views

urlpatterns = [
    url(r'login$', views.login, name="user-login"),
    url(r'logout/$', views.logout, name="user-logout"),
]
