from django.shortcuts import render, get_object_or_404
from .models import Course
from django.shortcuts import redirect

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'shop/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'shop/course_detail.html', {'course': course})


def cart_view(request):
    cart = request.session.get('cart', {})
    course_ids = cart.keys()
    courses = Course.objects.filter(id__in=course_ids)

    cart_items = []
    total = 0  # ✅ مجموع قیمت‌ها

    for course in courses:
        quantity = cart[str(course.id)]
        total += course.price * quantity  # ✅ قیمت × تعداد
        cart_items.append({
            'course': course,
            'quantity': quantity
        })

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total  # ✅ ارسال به قالب
    })

def add_to_cart(request, course_id):
    cart = request.session.get('cart', {})

    # اگر قبلاً وجود داشته باشه، تعدادش رو افزایش بده
    if str(course_id) in cart:
        cart[str(course_id)] += 1
    else:
        cart[str(course_id)] = 1

    request.session['cart'] = cart  # ذخیره در سشن
    return redirect('shop:cart')  # بعد از افزودن، برو به صفحه سبد خرید

def remove_from_cart(request, course_id):
    cart = request.session.get('cart', {})
    course_id_str = str(course_id)

    if course_id_str in cart:
        del cart[course_id_str]
        request.session['cart'] = cart

    return redirect('shop:cart')