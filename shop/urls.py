from django.urls import path
from . import views

urlpatterns = [
    path('shop/greetings/', views.greetings),
    path('shop/', views.list_item),
    path('shop/<id>/', views.detail_item)

]