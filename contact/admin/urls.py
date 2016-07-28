
from django.conf.urls import url
from contact.admin import views

urlpatterns = [
    url(r'login/$', views.login, name="admin-login"),
    url(r'logout/$', views.logout, name="admin-logout"),

    url(r'client-management/$', views.client_management, name="client-management"),
    url(r'client-list/$', views.client_list, name="client-list"),
    url(r'delete-client/$', views.delete_client, name="delete-client"),
    url(r'check-client/$', views.check_client, name="check-client"),

    url(r'staff-management/$', views.staff_management, name="staff-management"),

    url(r'get-client/$', views.get_client, name="get-client"),

    url(r'meal-management/$', views.meal_management, name="meal-management"),
    url(r'meal-list/$', views.meal_list, name="meal-list"),
    url(r'delete-meal/$', views.delete_meal, name="delete-meal"),

    url(r'rosters/$', views.roster_management, name="rosters"),
    url(r'roster-list/$', views.roster_list, name="roster-list"),
    url(r'delete-roster/$', views.delete_roster, name="delete-roster"),

    url(r'get-meal/$', views.get_meal, name="get-meal"),

]
