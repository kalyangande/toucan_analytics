from django.test import TestCase
from .models import CustomerData, EMIData

class ModelsTestCase(TestCase):
    def test_false_customer_data(self):
        # Creating a CustomerData object with invalid data types
        customer_data = CustomerData(customer_Id="abc", category=123, mode_of_payments=567, amount_spent="xyz", date="2021-09-01")
        self.assertFalse(customer_data.pk, "Invalid data types should not create a CustomerData object")

        # Creating a CustomerData object with empty required fields
        customer_data = CustomerData()
        self.assertFalse(customer_data.pk, "Empty required fields should not create a CustomerData object")

        # Creating a CustomerData object with a category exceeding the maximum allowed length
        customer_data = CustomerData(customer_Id=123, category="very_long_category_name_exceeding_maximum_length", mode_of_payments="Credit Card", amount_spent=100.0, date="2021-09-01")
        self.assertFalse(customer_data.pk, "Category exceeding the maximum length should not create a CustomerData object")

    def test_false_emi_data(self):
        # Creating an EMIData object with invalid data types
        emi_data = EMIData(customer_Id="abc", EMI_paid_on_time=123)
        self.assertFalse(emi_data.pk, "Invalid data types should not create an EMIData object")

        # Creating an EMIData object with empty required fields
        emi_data = EMIData()
        self.assertFalse(emi_data.pk, "Empty required fields should not create an EMIData object")

# Run the tests



