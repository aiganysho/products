from webapp.models import ProductInBasket, Product
from django.views.generic import CreateView, DetailView, View, ListView, DeleteView
from django.shortcuts import reverse, get_object_or_404, redirect, render
from webapp.form import ProductBasketForm, OrderForm
from django.urls import reverse_lazy


class ProductBasketCreate(CreateView):
    template_name = 'basket/create.html'
    model = ProductInBasket
    form_class = ProductBasketForm

    def get_success_url(self):
        return reverse('list-product')

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        try:
            basket = ProductInBasket.objects.get(product__id=product.id)
        except ProductInBasket.DoesNotExist:
            basket = None
        if product.remainder >= form.cleaned_data.get("quantity"):
            if basket:
                basket.quantity += form.cleaned_data.get("quantity")
                basket.save()
            else:
                basket = form.save(commit=False)
                basket.product = product

                basket.save()
            product.remainder -= form.cleaned_data.get("quantity")
            product.save()
        else:
            form.add_error('quantity', 'error')
            return render(self.request, 'product/list_product.html', {**self.kwargs})
        return redirect(self.get_success_url())


class ProductBasketView(ListView):
    template_name = 'basket/basket.html'
    model = ProductInBasket
    context_object_name = 'baskets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        total_product = []

        for product in ProductInBasket.objects.all():
            total += product.product.price * product.quantity
            total_product.append({"basket":product, 'total': product.product.price * product.quantity})
        context['total'] = total
        context['total_products'] = total_product
        context['form'] = OrderForm()
        return context


class ProductBasketDelete(DeleteView):
    template_name = 'basket/delete.html'
    model = ProductInBasket
    context_key = 'basket'
    success_url = reverse_lazy('view_cart')
