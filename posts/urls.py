from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>', category_view, name='category'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', qidiruv, name='qidiruv'),
    path('create/', create_product, name='product_create'),
    path('update/<int:pk>/', update_product, name='product_update'),
    path('delete/<int:pk>/', delete_product, name='product_delete'),

]