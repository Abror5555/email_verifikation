from xml.etree.ElementInclude import include
from django.urls import path
from .views import my_functional_view, confirm_needed, hompage


urlpatterns = [
    path('', hompage, name='home'),
    path('signup/', my_functional_view, name='signup'),
    path('confirm_needed/<int:id>', confirm_needed, name='confirm_needed'),
]