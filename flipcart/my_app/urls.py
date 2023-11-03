
from django.urls import path
from . import views
from .views import ProductList, SearchResultView, BookCheckout, add_to_cart,cart,remove_from_cart
from .views import Details

urlpatterns = [
    path('', ProductList.as_view(),name='list'),
    path('details/<int:pk>/',Details.as_view(),name = 'details'),
    path('search/',SearchResultView.as_view(),name='search'),
    path('checkout/<int:pk>/',BookCheckout.as_view(),name = 'checkout'),
    path('cart/',cart,name='mycart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart, name='remove_from_cart')

]
