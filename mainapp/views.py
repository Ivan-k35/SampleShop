from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Notebook, Smartphone, LatestProducts


class BaseView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        products = LatestProducts.objects.get_products_for_main_page('notebook', 'smartphone')
        context = {
            'products': products
        }
        return render(request, 'mainapp/base.html', context)


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'mainapp/product_detail.html'
    slug_url_kwarg = 'slug'
