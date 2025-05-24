from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .forms import BuyerInfoForm
from shop.cart import get_cart_data
from django.core.mail import send_mail, EmailMessage
from django.utils.crypto import get_random_string
from .models import Purchase

def checkout(request):
    cart_items, total = get_cart_data(request.session)

    if request.method == 'POST':
        form = BuyerInfoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # ساخت کد پیگیری
            tracking_code = get_random_string(10).upper()

            # لینک دانلود (موقت)
            download_link = f'https://yourdomain.com/download/{tracking_code}/'

            # تولید محتوای HTML ایمیل با قالب
            html_message = render_to_string('payment/email_template.html', {
                'tracking_code': tracking_code,
                'download_link': download_link,
            })

            # ارسال ایمیل HTML
            email_msg = EmailMessage(
                subject='پرداخت موفق - لینک دانلود شما',
                body=html_message,
                from_email='info@10learn.ir',
                to=[email],
            )
            email_msg.content_subtype = 'html'  # بسیار مهم: تعیین نوع محتوا به HTML
            email_msg.send()

            # ذخیره کد پیگیری در سشن
            request.session['tracking_code'] = tracking_code

            Purchase.objects.create(
                tracking_code=tracking_code,
                email=email,
                phone=phone,
                product_name = cart_items[0]['course'].title

            )
            return redirect('payment:success')

    else:
        form = BuyerInfoForm()

    return render(request, 'payment/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'form': form
    })


@csrf_exempt
def confirm_payment(request):
    if request.method == 'POST':
        # اینجا باید اطلاعات سفارش ذخیره شه، درگاه پرداخت صدا زده شه و...
        request.session['cart'] = {}  # خالی کردن سبد
        return render(request, 'payment/success.html')

def success(request):
    tracking_code = request.session.get('tracking_code')

    if not tracking_code:
        # اگه کاربر مستقیم اومده اینجا، نه از مسیر پرداخت
        return render(request, 'payment/error.html', {
            'message': 'دسترسی غیرمجاز یا اطلاعات یافت نشد.'
        })

    return render(request, 'payment/success.html', {
        'tracking_code': tracking_code
    })