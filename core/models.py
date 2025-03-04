from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import Truncator
from core.utils.replace_letter import replace_letter


class OneClickOrder(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.name}"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Catagories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Category name is required")

        if not self.slug or self.slug != replace_letter(self.name.lower()):
            self.slug = replace_letter(self.name.lower())

        return super(Category, self).save(*args, **kwargs)


class Product(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.FloatField()
    like = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/shop/")
    image2 = models.ImageField(upload_to="media/shop/")
    image3 = models.ImageField(upload_to="media/shop/")
    image_min = models.ImageField(upload_to="media/shop/")

    class Meta:
        verbose_name = _("Protuct")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Product name is required")

        if not self.slug or self.slug != replace_letter(self.name.lower()):
            self.slug = replace_letter(self.name.lower())

        return super(Product, self).save(*args, **kwargs)


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="attributes"
    )
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.product.name} - {self.key}: {self.value}"


class Blog(BaseModel):
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="media/blog/")

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def truncated_title(self):
        title_words = self.title.split(" ")
        truncated_title = " ".join(title_words)
        return Truncator(truncated_title).chars(100)

    def save(self, *args, **kwargs):
        if not self.title:
            raise ValueError("Product title is required")

        if not self.slug or self.slug != replace_letter(self.title.lower()):
            self.slug = replace_letter(self.title.lower())

        return super(Blog, self).save(*args, **kwargs)


class Contact(BaseModel):
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.adress


class ContactMail(BaseModel):
    email = models.EmailField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name = _("ContactMail")
        verbose_name_plural = _("ContactMails")

    def __str__(self):
        return self.email


class Setting(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    mail = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to="media/logo/")
    background_photo1 = models.ImageField(upload_to="media/background")
    background_photo2 = models.ImageField(upload_to="media/background")
    background_photo3 = models.ImageField(upload_to="media/background")
    blog_title = models.CharField(max_length=100)


class Subscriber(BaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
