from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from riceapp.models import Category,Product,Brand

# Create your views here.

def index(request):
    return render(request,'riceapp/index.html')

# category
class add_category(TemplateView,APIView):
    template_name = "riceapp/add_category.html"

    def post(self , request):
        category_name = request.POST['category_name']
        user = Category()
        user.category_name = category_name
        user.save()
        return JsonResponse({'status':"Success"})

class categoryListView(ListView):
    model = Category
    template_name = "riceapp/view_category.html"


# product
class add_product(TemplateView,APIView):
    template_name = "riceapp/add_product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context = {'category': list(category)}
        return context
    
    def post(self , request):
        category_id = request.POST['category_id'] 
        product_name = request.POST['product_name']
        try:
            category_instance = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'})

        # Create a new Product instance with the obtained Category instance
        product_instance = Product(category=category_instance, product_name=product_name)
        product_instance.save()
        return JsonResponse({'status': 'Success'})
    
class productListView(ListView):
    model = Product
    template_name = "riceapp/view_product.html"
    

# brand
class add_brand(TemplateView,APIView):
    template_name = "riceapp/add_brand.html"

    def post(self , request):
        category_id = request.POST['category_id']
        product_id = request.POST['product_id']
        brand_name = request.POST['brand_name']
        try:
            category_instance = Category.objects.get(pk=category_id)
            product_instance = Product.objects.get(pk=product_id)
        except Category.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID '})

        # Create a new Product instance with the obtained Category instance
        brand_instance = Brand(category=category_instance, product_id=product_id,brand_name=brand_name)
        brand_instance.save()
        return JsonResponse({'status': 'Success'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        product = Product.objects.all()
        context = {'category': list(category),'product': list(product)}
        return context
    
class brandListView(ListView):
    model = Brand
    template_name = "riceapp/view_brand.html"