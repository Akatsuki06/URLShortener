from django.urls import path, re_path, include
from basicapp import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('create', views.CreateAPI,base_name='create')

urlpatterns=[
        path('',views.shorten,name='shorten'),
        path('create/',views.CreateAPI.as_view(),name='create'),
        re_path(r'^(?P<URLid>[0-9a-zA-Z]+)/$',views.target,name='target')
]
