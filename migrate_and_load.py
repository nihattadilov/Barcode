import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barcode.settings")
django.setup()

from django.contrib.auth import get_user_model

print("🔄 Running migrate...")
os.system("python manage.py migrate")

print("✅ Loading data.json...")
os.system("python manage.py loaddata data.json")

User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    print("✅ Creating superuser...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("ℹ️ Superuser already exists.")
