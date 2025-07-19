from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Product, Comment, User
from django.db.models import Q
from .forms import ProductForm
from django.http import HttpResponseForbidden
@login_required
def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('home')
    return render(request, 'product_create.html', {'form': form})

@login_required
def update_product(request, pk):
    post = get_object_or_404(Product, pk=pk, user=request.user)
    if post.user != request.user:
        return HttpResponseForbidden("Siz bu mahsulotni o'chirishga ruxsatga ega emassiz.")
    form = ProductForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product_update.html', {'form': form})

@login_required
def delete_product(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("Siz bu mahsulotni o'chirishga ruxsatga ega emassiz.")
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'product_confirm_delete.html', {'post': post})


def qidiruv(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query)
        )
    context = {
        'results': results,
        'query': query
    }
    return render(request, 'search.html', context)


def index(request):
    categories = Category.objects.all()
    first_products = []

    for category in categories:
        category_first_product = Product.objects.filter(category=category).order_by('-id').first()
        if category_first_product:
            first_products.append(category_first_product)

    if len(first_products) < 4:
        all_products = Product.objects.all().order_by('-id')
        additional = all_products.exclude(id__in=[p.id for p in first_products])[:4 - len(first_products)]
        first_products.extend(additional)

    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'categories': categories,
        'first_products': first_products,
        'products': products
    })


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category-01.html', {
        'category': category,
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        comment_text = request.POST.get('msg')
        if request.user.is_authenticated:
            Comment.objects.create(
                product=product,
                pos_text=comment_text,
                user=request.user
            )
            messages.success(request, 'Fikr-mulohaza uchun rahmat!')
        else:
            messages.error(request, 'Fikr qoldirish uchun tizimga kiring.')
            return redirect('login')

    comments = Comment.objects.filter(product=product).order_by('-id')

    return render(request, 'product-detail.html', {
        'product': product,
        'comments': comments
    })


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')



@login_required(login_url='login')
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})
