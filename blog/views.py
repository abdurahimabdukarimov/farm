from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Product, Team, Blog
from blog.forms import ContactForm, NewsForm
# Create your views here.
def index(request):
    pro = Product.objects.all()
    team = Team.objects.all()
    blog = Blog.objects.all()
    form = NewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")

    context = {
        'pro': pro,
        'team': team,
        'blog': blog,
        "form": form
    }
    return render(request, "index.html", context=context)

def about(request):
    form = NewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")
    context = {
        "form": form
    }
    return render(request, "about.html", context=context)

def blog(request):
    form = NewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")
    blog = Blog.objects.all()
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, "blog.html", context=context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")
    context = {
        "form": form
    }
    return render(request, "contact.html", context=context)

def detail(request):
    return render(request, "detail.html", context={})

def feature(request):
    return render(request, "feature.html", context={})

def product(request):
    form = NewsForm(request.POST or None)
    pro = Product.objects.all()
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")
    context = {
        'pro': pro,
        'form': form
    }
    return render(request, "product.html", context=context)

def service(request):
    return render(request, "service.html", context={})

def team(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, "team.html", context=context)

def testimonial(request):
    return render(request, "testimonial.html", context={})

def base(request):
    form = NewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'ro'vingiz muvafaqiyatli tarzda amalga oshirildi</h2>")
    context = {
        "form": form
    }
    return render(request, "base.html", context=context)

def productDetail(request, product):
    product = get_object_or_404(Product, slug=product)
    context = {
        "product": product
    }
    return render(request, 'productDetail.html', context=context)

class productUpdate(UpdateView):
    model = Product
    fields = ['name', 'slug']
    template_name = 'productEdit.html'

class productDelete(DeleteView):
    model = Product
    template_name = 'productDelete.html'
    success_url = reverse_lazy(index)

class productCreate(CreateView):
    models = Product
    template_name = "productCreate.html"
    fields = ('name', 'slug', 'img', 'price')