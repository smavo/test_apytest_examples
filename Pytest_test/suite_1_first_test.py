import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.fixture()
def my_Setup():
    print("==========")
    print(">>>>>>>> MY SEYTUP <<<<<<<<<")

    return {"id": 18, 'name': 'smavodev'}


@pytest.mark.smoke
@pytest.mark.all
def test_checkout_gest(my_Setup):
    print("Checkout as guest")
    print("class: 11111")
    print("Name: {}".format(my_Setup.get('name')))


@pytest.mark.regression
def test_checkout_with_existing_user(my_Setup):
    print("Checkout with existing user")
    print("Class: 2222222")
    print("Name: {}".format(my_Setup.get('name')))