class Customer:
    def __init__(self, customer_id: str, tier: str):
        self.customer_id = customer_id
        self.tier = tier

    @property
    def is_premium(self) -> bool:
        return self.tier == "premium"
