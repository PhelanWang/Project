from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^categorys/(?P<categorys_page>\d+)/$', views.categorys, name='categorys'),
    url(r'^category/(?P<category_id>\d+)/(?P<category_page>\d+)/$', views.category, name='category'),
    url(r'^new_category$', views.new_category, name='new_category'),
    url(r'^edit_category/(?P<category_id>\d+)/$', views.edit_category, name='edit_category'),
    url(r'^new_entry/(?P<category_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^delete_entry/(?P<category_id>\d+)/(?P<category_page>\d+)/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),
    url(r'^delete_category/(?P<categorys_page>\d+)/(?P<category_id>\d+)/$', views.delete_category, name='delete_category'),
    url(r'^test$', views.test, name='test'),
    url(r'^search$', views.search, name='search'),
]
