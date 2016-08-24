
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

    url(r'meal-view/$', views.meal_view, name="meal-view"),
    url(r'send-comment/$', views.send_comment, name="send-comment"),
    url(r'client-profile/$', views.client_profile, name="client-profile"),

    url(r'staff-list/$', views.staff_list, name="staff-list"),

    url(r'register-staff/$', views.register_staff, name="register-staff"),
    url(r'check-staff/$', views.check_staff, name="check-staff"),
    url(r'edit-staff/$', views.edit_staff, name="edit-staff"),
]
