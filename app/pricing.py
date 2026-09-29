from .customer import Customer

PREMIUM_DISCOUNT = 0.20
REGULAR_DISCOUNT = 0.05

def discount_rate(customer: Customer) -> float:
    if customer.is_premium:
        return PREMIUM_DISCOUNT
    return REGULAR_DISCOUNT

def final_price(customer: Customer, subtotal: float) -> float:
    discount = subtotal * discount_rate(customer)
    return round(subtotal - discount, 2)
