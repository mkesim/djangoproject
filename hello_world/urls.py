# urls.py
from django.contrib import admin
from django.urls import path, include
from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.index, name='index'),
    path("calculate/", core_views.calculate, name="calculate"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
