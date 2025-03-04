from django.contrib import admin
from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin
from django_summernote.widgets import SummernoteWidget
from django.db import models
from core.models import (
    Category,
    Product,
    Blog,
    Contact,
    ContactMail,
    Setting,
    Subscriber,
    OneClickOrder,
    ProductAttribute,
)


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductAdmin(TranslationAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name", "price", "category__name")
    readonly_fields = ("like",)
    inlines = [ProductAttributeInline]
    fieldsets = (
        (
            "Main Information",
            {
                "fields": (
                    "name",
                    "price",
                    "category",
                    "image",
                    "image2",
                    "image3",
                    "slug",
                )
            },
        ),
        ("Main Information", {"fields": ("like",)}),
    )
    ordering = ("-created_at",)


class BlogAdmin(TranslationAdmin):
    list_display = ("title", "created_at")
    search_fields = (
        "title",
        "description",
    )
    last_filter = ("created_at",)
    fields = ("title", "description", "description2", "slug", "is_active", "image")
    ordering = ("-created_at",)
    formfield_overrides = {
        models.TextField: {"widget": SummernoteWidget},
    }


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(ContactMail)
admin.site.register(Setting)
admin.site.register(OneClickOrder)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Subscriber)
