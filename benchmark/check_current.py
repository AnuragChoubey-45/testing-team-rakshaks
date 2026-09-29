from app.customer import Customer
from app.pricing import final_price

print("premium_1000_final_price =", final_price(Customer("p1", "premium"), 1000))
