from django.urls import path
from .views import index, about, blog, contact, detail, feature, product, service, team, testimonial, productDetail, productUpdate, productDelete, productCreate

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("blog", blog, name="blog"),
    path("contact", contact, name="contact"),
    path("detail", detail, name="detail"),
    path("feature", feature, name="feature"),
    path("product", product, name="product"),
    path("service", service, name="service"),
    path("team", team, name="team"),
    path("testimonial", testimonial, name="testimonial"),
    path("product/<slug:product>", productDetail, name="productDetail"),
    path("product/edit/<slug>/", productUpdate.as_view(), name="productUpdate"),
    path("product/delete/<slug>/", productDelete.as_view(), name="productDelete"),
    path("product/create/", productCreate.as_view(), name="productCreate"),
]
