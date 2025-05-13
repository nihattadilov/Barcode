import os

print("🔄 Running migrate...")
os.system("python manage.py migrate")

print("✅ Loading data.json...")
os.system("python manage.py loaddata data.json")
