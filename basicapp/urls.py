from django.urls import path, re_path
from basicapp import views

urlpatterns=[
# path('',views.index,name='home'),
path('',views.shorten,name='shorten'),
re_path(r'^(?P<URLid>[0-9a-zA-Z]+)/$',views.target,name='target')
]
