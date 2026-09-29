import json
from app.customer import Customer
from app.pricing import final_price
from app.checkout import checkout_total
from app.shipping import shipping_fee

def main():
    scenarios = [
        ("regular_1000", Customer("r1", "regular"), 1000),
        ("premium_1000", Customer("p1", "premium"), 1000),
        ("premium_500", Customer("p2", "premium"), 500),
        ("regular_500", Customer("r2", "regular"), 500),
    ]

    results = {}
    for name, customer, subtotal in scenarios:
        results[name] = {
            "final_price": final_price(customer, subtotal),
            "shipping_fee": shipping_fee(customer, subtotal),
            "checkout_total": checkout_total(customer, subtotal),
        }

    print(json.dumps(results, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
