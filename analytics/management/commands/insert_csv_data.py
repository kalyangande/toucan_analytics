# Taking very less time comparing with others code

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




# # # import csv
# # # from django.core.management.base import BaseCommand
# # # from django.db import connection

# # # class Command(BaseCommand):
# # #     help = 'Insert data from CSV into the default database'

# # #     def add_arguments(self, parser):
# # #         parser.add_argument('csv_file', type=str, help='Data/data_for_database.csv')

# # #     def handle(self, *args, **options):
# # #         csv_file = options['csv_file']

# # #         with open(csv_file, 'r') as file:
# # #             reader = csv.reader(file)
# # #             next(reader)  # Skip header row

# # #             with connection.cursor() as cursor:
# # #                 for row in reader:
# # #                     query = f"INSERT INTO analytics_customerdata (customer_Id, category, mode_of_payments,amount_spent,date) VALUES ('{row[1]}', '{row[2]}', '{row[3]}','{row[4]}', '{row[5]}')"
# # #                     cursor.execute(query)

# import csv
# from django.core.management.base import BaseCommand
# from django.db import connection

# class Command(BaseCommand):
#     help = 'Insert data from CSV into the default database'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Data/data_for_database.csv')

#     def handle(self, *args, **options):
#         csv_file = options['csv_file']

#         rows = []
#         with open(csv_file, 'r') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip header row

#             for row in reader:
#                 rows.append((row[1], row[2], row[3], row[4], row[5],))

#         query = "INSERT INTO analytics_customerdata (customer_Id, category, mode_of_payments, amount_spent, date) VALUES (%s, %s, %s, %s, %s)"

#         with connection.cursor() as cursor:
#             cursor.executemany(query, rows)




# # import csv
# # from django.core.management.base import BaseCommand
# # from django.db import connection

# # class Command(BaseCommand):
# #     help = 'Insert data from CSV into the default database'

# #     def add_arguments(self, parser):
# #         parser.add_argument('csv_file', type=str, help='Data/data_for_database.csv')
# #         parser.add_argument('batch_size', type=int, help='1000')

# #     def handle(self, *args, **options):
# #         csv_file = options['csv_file']
# #         batch_size = options['batch_size']

# #         with open(csv_file, 'r') as file:
# #             reader = csv.reader(file)
# #             next(reader)  # Skip header row

# #             rows = []
# #             total_rows = 0

# #             with connection.cursor() as cursor:
# #                 for row in reader:
# #                     rows.append((row[0], row[1], row[2]))
# #                     total_rows += 1

# #                     if len(rows) == batch_size:
# #                         self.insert_batch(cursor, rows)
# #                         rows = []

# #                 if rows:
# #                     self.insert_batch(cursor, rows)

# #         self.stdout.write(self.style.SUCCESS(f"Data insertion completed. Total rows: {total_rows}"))

# #     def insert_batch(self, cursor, rows):
# #         query = "INSERT INTO your_table (field1, field2, field3) VALUES (%s, %s, %s)"
# #         cursor.executemany(query, rows)
# #         connection.commit()



