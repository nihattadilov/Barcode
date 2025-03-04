from django.urls import include, path
from django.conf import settings
from core.views import (
    index,
    product,
    blog,
    contact,
    blog_details,
    search,
    product_single,
    one_click_order,
)


urlpatterns = [
    path("", index, name="index"),
    path("product/", product, name="product"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("blog-detail/<str:blog_slug>/", blog_details, name="blog-detail"),
    path("search/", search, name="search"),
    path("product/<str:product_slug>/", product_single, name="product_single"),
    path("one-click-order/<int:product_id>/", one_click_order, name="one_click_order"),
]
