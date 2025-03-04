from django.shortcuts import render
from core.models import Setting
from core.forms import SubscriberForm


def my_setting(request):
    setting_data = Setting.objects.last()
    subscriber_form = SubscriberForm()
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            subscriber_form = SubscriberForm()
    return {"setting_data": setting_data, "subscriber_form": subscriber_form}
