import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
def test_checkout_gest():
    print("Checkout as guest")
    print("class: 11111")


@pytest.mark.regression
def test_checkout_with_existing_user():
    print("Checkout with existing user")
    print("Class: 2222222")
