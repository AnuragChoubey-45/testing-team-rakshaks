from app.inventory import can_fulfill, remaining_stock

def test_exact_inventory_can_be_fulfilled():
    assert can_fulfill(5, 5) is True

def test_remaining_stock_never_negative():
    assert remaining_stock(3, 5) == 0
