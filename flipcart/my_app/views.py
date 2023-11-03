from _decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView

from .models import products, Cart, CartItems


# Create your views here.
class ProductList(ListView):
    model = products
    template_name = 'productlist.html'


class Details(DetailView):
    model = products
    context_object_name = 'list'
    template_name = 'details.html'


class SearchResultView(ListView):
    model = products
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q', )
        return products.objects.filter(
            Q(title=query)
        )


class BookCheckout(DetailView):
    model = products
    template_name = 'checkout.html'


@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItems.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []
    context = {
        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'cart/mycart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(products, id=product_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user, total_price=Decimal('0.00'))
    cart_item, created = CartItems.objects.get_or_create(book=product, cart=cart_obj)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    cart_obj.total_price += Decimal(str(product.price))
    cart_obj.save()
    return redirect('mycart')

def remove_from_cart(request,product_id):
    product = get_object_or_404(products, id=product_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = CartItems.objects.filter(book=product, cart=cart_obj)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity>1:
                cart_item.quantity -=1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price -= Decimal(str(product.price))
            cart_obj.save()
        return redirect('mycart')

