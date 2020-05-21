from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import url, include
from CB_app import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^app/',include('CB_app.urls',namespace = 'CB_app')),
    path('admin/', admin.site.urls),
]
