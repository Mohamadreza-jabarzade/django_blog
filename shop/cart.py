# shop/cart.py
from .models import Course

def get_cart_data(session):
    cart = session.get('cart', {})
    cart_items = []
    total = 0

    for course_id, quantity in cart.items():
        try:
            course = Course.objects.get(id=course_id)
            cart_items.append({
                'course': course,
                'quantity': quantity,
            })
            total += course.price * quantity
        except Course.DoesNotExist:
            continue

    return cart_items, total
