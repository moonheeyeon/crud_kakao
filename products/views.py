from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
import pdb #pyhton debuging

# Create your views here.

def list(request):
    products = Product.objects.all() #model의 Products에서 모든 것을 받아 온다. 그리고 products라는 변수에 담는다
    return render(request, 'products/list.html', {'products': products}) #3번째 key값으로 dictionary 타입


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        location = request.POST.get('location')
        # product = Product(title=title, price=price, description=description)
        # product.save()
        # pdb.set_trace() #여기서 멈춰서 python 디버깅 실시
        image = request.FILES.get('image') #POST가 아니라 FILES로 받아야함
        product = Product.objects.create(title=title, price=price, description=description, location=location, image=image)
        return redirect('list')
    return render(request, 'products/create.html')


def show(request, id):
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    default_view_count = product.view_count
    product.view_count = default_view_count +1
    product.save()
    return render(request, 'products/show.html', {'product': product})
    #object를 가져와서 3번째 인자로 show에 넘긴다
    #각 상품마다의 pk로 구분
    #2를 이용해서 Product에서 pk(id)가 2인 녀석을 찾아서 show.html로 넘긴다
    #주소로 pk값을 넘긴다


def edit(request, id):  #edit 역시 특정 상품의 id를 받아올 수 있어야 한다
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/edit.html', {'product': product})


def update(request, id):
    if request.method == "POST":
        # product = Product.objects.get(pk=id)
        product = get_object_or_404(Product, pk=id)
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        product.title = title
        product.price = price
        product.description = description
        product.save()
        return redirect('products:show', product.pk)


#create와 비슷하나 edit과 update로 나눴다
#edit은 POST방식이니 if문이 들어감 (create와 비슷)


def delete(request, id):
    if request.method == "POST":
        # product = Product.objects.get(pk=id)
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('list')
