from .customer import Customer

FREE_SHIPPING_THRESHOLD = 1000.0
PREMIUM_FREE_SHIPPING_THRESHOLD = 500.0

def shipping_fee(customer: Customer, subtotal: float) -> float:
    if customer.is_premium and subtotal >= PREMIUM_FREE_SHIPPING_THRESHOLD:
        return 0.0
    if subtotal >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return 79.0
