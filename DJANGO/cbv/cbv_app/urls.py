from django.conf.urls import url
from . import views

app_name = 'cbv_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name="list"),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
]