
from django.conf.urls import url, include

urlpatterns = [
    url('^app/', include('contact.app.urls')),
    url('^admin/', include('contact.admin.urls'))
]
