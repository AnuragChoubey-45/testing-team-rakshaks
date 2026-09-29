from .customer import Customer
from .pricing import final_price
from .shipping import shipping_fee

def checkout_total(customer: Customer, subtotal: float) -> float:
    return round(final_price(customer, subtotal) + shipping_fee(customer, subtotal), 2)
