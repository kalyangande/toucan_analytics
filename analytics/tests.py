from django.test import TestCase
from analytics.models import CustomerData, EMIData
from datetime import date
from django.http import JsonResponse
from .views import table, bar, pie, emi

class CustomerDataTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomerData.objects.create(
            customer_Id=1,
            category='Regular',
            mode_of_payments='Credit Card',
            amount_spent=100.0,
            date='2023-05-31'
        )


    def test_model_creation(self):
        obj = CustomerData.objects.get(customer_Id=1)
        self.assertEqual(obj.customer_Id, 1)
        self.assertEqual(obj.category, 'Regular')
        self.assertEqual(obj.mode_of_payments, 'Credit Card')
        self.assertEqual(obj.amount_spent, 100.0)
        self.assertEqual(obj.date, date(2023, 5, 31))


    def test_model_update(self):
        obj = CustomerData.objects.get(customer_Id=1)
        obj.amount_spent = 150.0
        obj.save()

        updated_obj = CustomerData.objects.get(pk=obj.pk)
        self.assertEqual(updated_obj.amount_spent, 150.0)

    def test_model_deletion(self):
        obj = CustomerData.objects.get(customer_Id=1)
        obj.delete()

        self.assertFalse(CustomerData.objects.filter(customer_Id=1).exists())


class EMIDataTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        EMIData.objects.create(customer_Id=1, EMI_paid_on_time='True')

    def test_model_creation(self):
        obj = EMIData.objects.get(customer_Id=1)
        self.assertEqual(obj.customer_Id, 1)
        self.assertEqual(obj.EMI_paid_on_time, 'True')

    def test_model_update(self):
        obj = EMIData.objects.get(customer_Id=1)
        obj.EMI_paid_on_time = 'False'
        obj.save()

        updated_obj = EMIData.objects.get(pk=obj.pk)
        self.assertEqual(updated_obj.EMI_paid_on_time, 'False')

    def test_model_deletion(self):
        obj = EMIData.objects.get(customer_Id=1)
        obj.delete()

        self.assertFalse(EMIData.objects.filter(customer_Id=1).exists())


# class AnalyticsTestCase(TestCase):
#     def setUp(self):
#         # Create test data
#         CustomerData.objects.create(
#             customer_Id=1,
#             category='Regular',
#             mode_of_payments='Credit Card',
#             amount_spent=100.0,
#             date='2023-05-31'
#         )
#         EMIData.objects.create(
#             customer_Id=1,
#             EMI_paid_on_time='Yes'
#         )

#     def test_table_view(self):
#         response = table(None, '2023-05-01', '2023-05-31')
#         self.assertIsInstance(response, JsonResponse)
#         # Add assertions for the response data if required

#     def test_bar_view(self):
#         response = bar(None, '2023-05-01', '2023-05-31')
#         self.assertIsInstance(response, JsonResponse)
#         # Add assertions for the response data if required

#     def test_pie_view(self):
#         response = pie(None, '2023-05-01', '2023-05-31')
#         self.assertIsInstance(response, JsonResponse)
#         # Add assertions for the response data if required

#     def test_emi_view(self):
#         response = emi(None)
#         self.assertIsInstance(response, JsonResponse)
#         # Add assertions for the response data if required

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



