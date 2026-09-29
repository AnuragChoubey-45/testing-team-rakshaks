from app.customer import Customer
from app.auth import can_access_admin, can_view_reports

def test_only_admin_can_access_admin():
    assert can_access_admin(Customer("a1", "admin")) is True
    assert can_access_admin(Customer("p1", "premium")) is False

def test_premium_can_view_reports():
    assert can_view_reports(Customer("p1", "premium")) is True
    assert can_view_reports(Customer("r1", "regular")) is False
