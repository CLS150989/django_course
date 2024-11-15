from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import ProductForm
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AddProductView(generic.FormView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    