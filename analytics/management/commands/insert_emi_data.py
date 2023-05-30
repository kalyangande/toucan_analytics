import csv
from django.core.management import BaseCommand
from django.utils import timezone

from  analytics.models import CustomerData,EMIData


class Command(BaseCommand):
    # help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("Data/Emi_data_for_DB.csv", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["Data/Emi_data_for_DB.csv"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data)
            products = []
            for row in data:
                customer_data= EMIData(
                    customer_Id=row[0],
                    EMI_paid_on_time=row[1]
                )
                products.append(customer_data)
                if len(products) > 5000:
                    EMIData.objects.bulk_create(products)
                    products = []
            if products:
                EMIData.objects.bulk_create(products)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )