from django.urls import re_path, path

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.post_list, name='post_list'),
    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

]
