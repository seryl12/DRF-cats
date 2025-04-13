from django.urls import path
from .views import homepage_view, cats_view

urlpatterns = [
    path('', homepage_view, name='home'),
    path('cats', cats_view, name='cats'),
]
