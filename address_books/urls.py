from django.conf.urls import url

from . import views

# from .views import CategoryViewSet, EntryViewSet, UserViewSet

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^categorys/(?P<categorys_page>\d+)/$', views.categorys, name='categorys'),
    # url(r'^category/(?P<category_id>\d+)/(?P<category_page>\d+)/$', views.category, name='category'),
    # url(r'^new_category$', views.new_category, name='new_category'),
    # url(r'^edit_category/(?P<category_id>\d+)/$', views.edit_category, name='edit_category'),
    # url(r'^new_entry/(?P<category_id>\d+)/$', views.new_entry, name='new_entry'),
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # url(r'^delete_entry/(?P<category_id>\d+)/(?P<category_page>\d+)/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),
    # url(r'^delete_category/(?P<categorys_page>\d+)/(?P<category_id>\d+)/$', views.delete_category, name='delete_category'),
    # url(r'^test$', views.test, name='test'),
    # url(r'^search$', views.search, name='search'),


    url(r'^categorys/$', views.CategoryList.as_view()),
    url(r'^categorys/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),

    url(r'^entrys/$', views.EntryList.as_view()),
    url(r'^entrys/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view()),

    url(r'^entry/$', views.EntryList.as_view()),
    url(r'^entry/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# category_list = CategoryViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# category_detail = CategoryViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
#
#
# entry_list = EntryViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# entry_detail = EntryViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
#
#
# user_list = UserViewSet.as_view({
#     'get': 'list',
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
# })
#
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^categorys/$', category_list, name='category-list'),
#     url(r'^categorys/(?P<pk>[0-9])/$', category_detail, name='category-detail'),
#     url(r'^entrys/$', entry_list, name='entry-list'),
#     url(r'^entrys/(?P<pk>[0-9])/$', entry_detail, name='entry-detail'),
#     url(r'^users/$', user_list, name='entry-list'),
#     url(r'^users/(?P<pk>[0-9])/$', user_detail, name='entry-detail'),
# ])


























