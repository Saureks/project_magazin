from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} - {phone} - {message}")
        context = {
            "name": name,
            "phone": phone,
            "message": message
        }
        return render(request, self.template_name, context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"{name} ({phone}): {message}")
#     return render(request, 'catalog/contact.html')


# def product(request, pk):
#     context = {'object': Product.objects.get(pk=pk)}
#     return render(request, 'catalog/product.html', context)
