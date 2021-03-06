from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.db.models import Q
from django.utils.http import urlencode
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import Product, categories
from webapp.form import ProductForm, SearchForm, ProductBasketForm
# Create your views here


class ProductList(ListView):
    template_name = 'product/list_product.html'
    model = Product
    context_object_name = 'lists'
    paginate_by = 5
    paginate_orphans = 1


    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset.exclude(remainder=0).order_by("category", "name")

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None


    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['form'] = ProductBasketForm()
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        print(context)
        return context


class ProductDetailView(DetailView):
    template_name = 'product/view_product.html'
    context_key = 'product'
    model = Product


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'product/create_product.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.add_product'
    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm
    context_key = 'product'
    permission_required = 'webapp.change_product'
    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )


class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_key = 'product'
    success_url = reverse_lazy('product:list')
    permission_required = 'webapp.delete_product'


