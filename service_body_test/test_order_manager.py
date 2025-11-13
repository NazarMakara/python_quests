import pytest
from service_body_test import Order

@pytest.fixture
def items():
    return [
        {'name': 'A', 'price': 1200.00, 'quantity': 1},
        {'name': 'B', 'price': 25.50, 'quantity': 2},
        {'name': 'C', 'price': 75.00, 'quantity': 3}
    ]

@pytest.fixture
def ord_1(items):
    return Order(id=1, items=items)

@pytest.fixture
def ord_0():
    return Order(id=2, items=[])

def test_total_1(ord_1):
    assert ord_1.total() == 1476.00

def test_total_0(ord_0):
    assert ord_0.total() == 0

def test_total_max():
    items = [{'name': 'P', 'price': 0.5, 'quantity': 10000}]
    o = Order(id=3, items=items)
    assert o.total() == 5000.0

def test_exp_1(ord_1):
    exp = {'name': 'A', 'price': 1200.00, 'quantity': 1}
    assert ord_1.most_expensive() == exp

def test_exp_tie():
    items = [{'name': 'A', 'price': 20.0, 'quantity': 1},{'name': 'B', 'price': 20.0, 'quantity': 1}]
    o = Order(id=4, items=items)
    assert o.most_expensive() == {'name': 'A', 'price': 20.0, 'quantity': 1}

def test_disc_10(ord_1):
    ord_1.apply_discount(10)
    assert ord_1.items[0]['price'] == pytest.approx(1080.0)
    assert ord_1.items[1]['price'] == pytest.approx(22.95)

def test_disc_0(ord_1):
    p = [item['price'] for item in ord_1.items]
    ord_1.apply_discount(0)
    assert [item['price'] for item in ord_1.items] == p

def test_disc_100(ord_1):
    ord_1.apply_discount(100)
    for item in ord_1.items:
        assert item['price'] == 0.0

def test_disc_neg(ord_1):
    with pytest.raises(ValueError):
        ord_1.apply_discount(-1)

def test_disc_high(ord_1):
    with pytest.raises(ValueError):
        ord_1.apply_discount(101)

def test_disc_all_prices():
    items = [{'name': 'A', 'price': 100.0, 'quantity': 1}]
    o = Order(id=6, items=items)
    o.apply_discount(20)
    assert o.items[0]['price'] == pytest.approx(80.0)

def test_repr_1(ord_1):
    assert repr(ord_1) == "<Order 1: 3 items>"

def test_repr_0(ord_0):
    assert repr(ord_0) == "<Order 2: 0 items>"