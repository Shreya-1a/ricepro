from django.urls import path
from riceapp.views import *

urlpatterns=[
    path('',index,name='index'),

    # category
    # path('create_category',create_category.as_view(),name="create_category"),
    path('add_category',add_category.as_view(),name='add_category'),
    path('categoryListView',categoryListView.as_view(),name='categoryListView'),

    # product
    path('add_product',add_product.as_view(),name='add_product'),
    path('productListView',productListView.as_view(),name='productListView'), 

    # brand
    path('add_brand',add_brand.as_view(),name='add_brand'),
    path('brandListView',brandListView.as_view(),name='brandListView'),    


]