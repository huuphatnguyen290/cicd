# test_spending_tracker_pytest.py

import pytest
from spending_tracker import calculate_total, calculate_average, get_top_category, add_expense


@pytest.fixture
def expenses():
    return [
        {"desc": "Lunch", "amount": 12.50, "category": "Food"},
        {"desc": "Bus fare", "amount": 3.00, "category": "Transport"},
        {"desc": "Dinner", "amount": 20.00, "category": "Food"},
    ]


# --- calculate_total ---

def test_calculate_total(expenses):
    assert calculate_total(expenses) == pytest.approx(35.50, abs=1)


def test_calculate_total_empty():
    assert calculate_total([]) == 0


# --- calculate_average ---

def test_calculate_average(expenses):
    assert calculate_average(expenses) == pytest.approx(11.83, abs=0.01)

def test_calculate_average_empty():
    assert calculate_average([]) == 0


# --- get_top_category ---

def test_get_top_category(expenses):
    assert get_top_category(expenses) == "Food"

def test_get_top_category_empty():
    assert get_top_category([]) is None


# --- add_expense ---

def test_add_expense_valid(expenses):
    add_expense(expenses, "Coffee", 5.00, "Food")
    assert len(expenses) == 4

def test_add_expense_invalid_amount(expenses):
    with pytest.raises(ValueError):
        add_expense(expenses, "Coffee", -5.00, "Food")

def test_add_expense_empty_desc(expenses):
    with pytest.raises(ValueError):
        add_expense(expenses, "", 5.00, "Food")