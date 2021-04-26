from django.views.generic import View, ListView
from webapp.models import Order, ProductInBasket, OrderProduct
from webapp.form import OrderForm
from django.shortcuts import render, reverse, redirect




class CreateOrder(View):

    def post(self, request, *args, **kwargs):
        print('bvbvbv')
        form = OrderForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name_user')
            telephone = form.cleaned_data.get('telephone')
            adress = form.cleaned_data.get('adress')
            session = self.request.session.get('basket', [])
            print(session)
            order = Order.objects.create(name_user=name, telephone=telephone, adress=adress, user=request.user )
            # for cart in ProductInBasket.objects.all():


            for cart in ProductInBasket.objects.filter(pk__in=session):
                OrderProduct.objects.create(order=order, product=cart.product, quantity=cart.quantity)
                cart.delete()
            return redirect('product:view_cart')
        return render(request, 'basket/basket.html', context={'form': form})


class OrderView(ListView):
    template_name = 'product/list_order.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user__pk=self.request.user.pk)




