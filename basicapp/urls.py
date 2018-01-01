from django.urls import path, re_path, include
from basicapp import views

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'all', views.api)
urlpatterns=[
# path('',views.index,name='home'),
# path('api/',include(router.urls)),
path('',views.shorten,name='shorten'),
path('api/create',views.CreateShortURL.as_view(),name='create'),
re_path(r'^(?P<URLid>[0-9a-zA-Z]+)/$',views.target,name='target')
]
