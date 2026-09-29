def can_fulfill(requested: int, available: int) -> bool:
    return requested <= available

def remaining_stock(available: int, sold: int) -> int:
    return max(0, available - sold)
