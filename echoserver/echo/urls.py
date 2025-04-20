from django.urls import path
from .views import homepage_view, my_cats_view, ApiCatsView, ViewSetCat

urlpatterns = [
    path('', homepage_view, name='home'),
    path('my_view/cat', my_cats_view, name='my_view_cat'),
    path('api_view/cat', ApiCatsView.as_view(), name='api_view_cat'),
    path('viewset/cat', ViewSetCat.as_view({'get': 'list', 'post': 'create'}), name='viewset_cat_get'),
    path('viewset/cat/<str:name>', ViewSetCat.as_view({'put': 'update',
                                                       'patch': 'partial_update',
                                                       'delete': 'destroy'}), name='viewset_cat'),
]
