from django.conf.urls import url

from .views import CustomProfileViewSet

item_list = CustomProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

item_details = CustomProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', item_list, name='item_lists '),
    url(r'^(?P<pk>\d+)/$', item_details, name='item_details '),
]
