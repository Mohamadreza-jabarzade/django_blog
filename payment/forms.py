# payment/forms.py
from django import forms

class BuyerInfoForm(forms.Form):
    email = forms.EmailField(label='ایمیل', required=True)
    phone = forms.CharField(label='شماره موبایل', required=True, max_length=15)
