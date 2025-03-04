from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
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
from core.forms import OneClickOrderForm, ContactForm


class ModelTests(TestCase):
    def setUp(self):
        # Create a category for testing
        self.category = Category.objects.create(name="Test Category", slug="test-category")

        # Create a product for testing
        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product",
            price=100.0,
            category=self.category,
            image=SimpleUploadedFile(
                "test_image.jpg", b"file_content", content_type="image/jpeg"
            ),
            image2=SimpleUploadedFile(
                "test_image2.jpg", b"file_content", content_type="image/jpeg"
            ),
            image3=SimpleUploadedFile(
                "test_image3.jpg", b"file_content", content_type="image/jpeg"
            ),
            image_min=SimpleUploadedFile(
                "test_image_min.jpg", b"file_content", content_type="image/jpeg"
            ),
        )

        # Create a blog for testing
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            description="Test Description",
            image=SimpleUploadedFile(
                "test_blog_image.jpg", b"file_content", content_type="image/jpeg"
            ),
        )

        # Create a contact for testing
        self.contact = Contact.objects.create(
            adress="Test Address", phone="123456789", mail="test@example.com"
        )

        # Create a contact mail for testing
        self.contact_mail = ContactMail.objects.create(
            email="test@example.com", message="Test Message"
        )

        # Create a setting for testing
        self.setting = Setting.objects.create(
            adress="Test Address",
            phone="123456789",
            logo=SimpleUploadedFile(
                "test_logo.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo1=SimpleUploadedFile(
                "test_bg1.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo2=SimpleUploadedFile(
                "test_bg2.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo3=SimpleUploadedFile(
                "test_bg3.jpg", b"file_content", content_type="image/jpeg"
            ),
            blog_title="Test Blog Title",
        )

        # Create a subscriber for testing
        self.subscriber = Subscriber.objects.create(email="test@example.com")

        # Create a one-click order for testing
        self.one_click_order = OneClickOrder.objects.create(
            product=self.product, name="Test User", phone="123456789"
        )

        # Create a product attribute for testing
        self.product_attribute = ProductAttribute.objects.create(
            product=self.product, key="Test Key", value="Test Value"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.slug, "test-category")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.category.name, "Test Category")

    def test_blog_creation(self):
        self.assertEqual(self.blog.title, "Test Blog")
        self.assertEqual(self.blog.slug, "test-blog")

    def test_contact_creation(self):
        self.assertEqual(self.contact.adress, "Test Address")
        self.assertEqual(self.contact.phone, "123456789")

    def test_contact_mail_creation(self):
        self.assertEqual(self.contact_mail.email, "test@example.com")
        self.assertEqual(self.contact_mail.message, "Test Message")

    def test_setting_creation(self):
        self.assertEqual(self.setting.adress, "Test Address")
        self.assertEqual(self.setting.blog_title, "Test Blog Title")

    def test_subscriber_creation(self):
        self.assertEqual(self.subscriber.email, "test@example.com")

    def test_one_click_order_creation(self):
        self.assertEqual(self.one_click_order.name, "Test User")
        self.assertEqual(self.one_click_order.phone, "123456789")

    def test_product_attribute_creation(self):
        self.assertEqual(self.product_attribute.key, "Test Key")
        self.assertEqual(self.product_attribute.value, "Test Value")


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a category for testing
        self.category = Category.objects.create(name="Test Category", slug="test-category")

        # Create a product for testing
        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product",
            price=100.0,
            category=self.category,
            image=SimpleUploadedFile(
                "test_image.jpg", b"file_content", content_type="image/jpeg"
            ),
            image2=SimpleUploadedFile(
                "test_image2.jpg", b"file_content", content_type="image/jpeg"
            ),
            image3=SimpleUploadedFile(
                "test_image3.jpg", b"file_content", content_type="image/jpeg"
            ),
            image_min=SimpleUploadedFile(
                "test_image_min.jpg", b"file_content", content_type="image/jpeg"
            ),
        )

        # Create a blog for testing
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            description="Test Description",
            image=SimpleUploadedFile(
                "test_blog_image.jpg", b"file_content", content_type="image/jpeg"
            ),
        )

        # Create a contact for testing
        self.contact = Contact.objects.create(
            adress="Test Address", phone="123456789", mail="test@example.com"
        )

        # Create a setting for testing
        self.setting = Setting.objects.create(
            adress="Test Address",
            phone="123456789",
            logo=SimpleUploadedFile(
                "test_logo.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo1=SimpleUploadedFile(
                "test_bg1.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo2=SimpleUploadedFile(
                "test_bg2.jpg", b"file_content", content_type="image/jpeg"
            ),
            background_photo3=SimpleUploadedFile(
                "test_bg3.jpg", b"file_content", content_type="image/jpeg"
            ),
            blog_title="Test Blog Title",
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_view(self):
        response = self.client.get(reverse("product"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_single_view(self):
        response = self.client.get(
            reverse("product_single", kwargs={"product_slug": self.product.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_blog_view(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")

    def test_blog_details_view(self):
        print(f"Blog Slug: {self.blog.slug}")  # Debugging: Print the slug
        response = self.client.get(
            reverse("blog-detail", kwargs={"blog_slug": self.blog.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Address")

    def test_search_view(self):
        response = self.client.post(reverse("search"), {"search": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertContains(response, "Test Blog")

    def test_one_click_order_view(self):
        response = self.client.post(
            reverse("one_click_order", kwargs={"product_id": self.product.id}),
            {"name": "Test User", "phone": "123456789"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sifarişiniz uğurla göndərildi!")


class FormTests(TestCase):
    def test_one_click_order_form(self):
        form_data = {"name": "Test User", "phone": "123456789"}
        form = OneClickOrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form(self):
        form_data = {"email": "test@example.com", "message": "Test Message"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())