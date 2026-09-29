from app.customer import Customer
from app.shipping import shipping_fee

def test_premium_gets_free_shipping_at_500():
    assert shipping_fee(Customer("p1", "premium"), 500) == 0.0

def test_regular_gets_free_shipping_at_1000():
    assert shipping_fee(Customer("r1", "regular"), 1000) == 0.0

def test_regular_pays_below_threshold():
    assert shipping_fee(Customer("r1", "regular"), 499) == 79.0
