from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from users.views import ELoginView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/login/', ELoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    path('', include('core.urls')),
]
