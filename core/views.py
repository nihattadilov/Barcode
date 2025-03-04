from django.http import HttpResponse, Http404
from core.models import *
from core.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OneClickOrderForm
from django.http import HttpResponse
from django.contrib import messages


def one_click_order(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Məhsul tapılmadı!")

    if request.method == "POST":
        form = OneClickOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Sifarişiniz uğurla göndərildi!")
            return HttpResponse("Sifarişiniz uğurla göndərildi!")
    else:
        form = OneClickOrderForm()

    return render(request, "one_click_order.html", {"form": form, "product": product})



def index(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "index.html", context=context)


def product(request):
    from django.db.models import Q

    products = Product.objects.filter(is_active=True).order_by("-created_at")
    categories = Category.objects.all()

    start_date = None
    end_date = None

    if request.method == "POST":
        user_input = request.POST.get("product_search")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        if user_input:
            products = products.filter(name__icontains=user_input)
        if start_date and end_date:
            products = products.filter(
                Q(created_at__date__gte=start_date), Q(created_at__date__lte=end_date)
            )

    active_category = request.GET.get("category", "")
    if active_category:
        products = products.filter(category__slug=active_category)

    if len(products) == 0:
        no_result = "Product tapılmadı"
    else:
        no_result = None

    paginator = Paginator(products, 8)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
        "title": "Product Page",
        "no_result": no_result,
        "categories": categories,
        "active_category": active_category,
    }
    return render(request, "product.html", context=context)


def product_single(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Məhsul tapılmadı!")  

    context = {
        "title": "Product Single Page",
        "product_single": product,
        "products": Product.objects.all().order_by("created_at"),
    }
    return render(request, "product-detail.html", context=context)


def blog(request):
    blogs = Blog.objects.filter(is_active=True).order_by("-created_at")
    products = Product.objects.all()
    items_per_page = 2
    paginator = Paginator(blogs, items_per_page)
    page = request.GET.get("page")

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        "title": Setting.objects.first().blog_title,
        "blogs": blogs,
        "products": products,
    }
    return render(request, "blog.html", context=context)


def blog_details(request, blog_slug):
    try:
        blog = Blog.objects.get(slug=blog_slug)
    except Blog.DoesNotExist:
        raise Http404("Bloq tapılmadı!")

    products = Product.objects.all()
    context = {"title": blog.title, "products": products, "blog": blog}
    return render(request, "blog-detail.html", context=context)



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request, "contact.html", context={"contact_form": ContactForm()}
            )

    contacts = Contact.objects.filter(is_active=True).order_by("-created_at")

    # Əgər `contacts` boş olarsa, `contact = None` təyin edirik
    contact = contacts.first() if contacts.exists() else None

    context = {
        "contact_form": ContactForm(),
        "title": "Contact page",
        "contact": contact,  # Boş olarsa, səhifədə xəta verməyəcək
    }
    return render(request, "contact.html", context=context)



def search(request):
    blogs = Blog.objects.none()  # Boş QuerySet
    products = Product.objects.none()

    if request.method == "POST":
        user_input = request.POST.get("search")
        if user_input:
            blogs = Blog.objects.filter(title__icontains=user_input)
            products = Product.objects.filter(name__icontains=user_input)

    context = {
        "title": "search",
        "blogs": blogs,
        "products": products,
    }
    return render(request, "search.html", context=context)

