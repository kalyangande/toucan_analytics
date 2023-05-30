import csv
from django.core.management import BaseCommand
from django.utils import timezone

from  analytics.models import CustomerData


class Command(BaseCommand):
    # help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("Data/data_for_database.csv", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["Data/data_for_database.csv"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data)
            products = []
            for row in data:
                customer_data= CustomerData(
                    customer_Id=row[1],
                    category=row[2],
                    mode_of_payments=row[3],
                    amount_spent=row[4],
                    date=row[5]
                )
                products.append(customer_data)
                if len(products) > 5000:
                    CustomerData.objects.bulk_create(products)
                    products = []
            if products:
                CustomerData.objects.bulk_create(products)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )