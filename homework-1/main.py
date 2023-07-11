"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

# файлы с данными
file_name1 = '../homework-1/north_data/customers_data.csv'
file_name2 = '../homework-1/north_data/employees_data.csv'
file_name3 = '../homework-1/north_data/orders_data.csv'
# подключаемся к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="080374"
)
try:
    with conn:
        # используем контекстный менеджер объекта cursor для выполнения
        # запросов
        with conn.cursor() as cur:
            # Заполняем таблицу customers_data из customers_data.csv
            with open(file_name1) as csvfile:
                readers = csv.DictReader(csvfile)
                for reader in readers:
                    cur.execute("INSERT INTO customers_data VALUES (%s, %s, "
                                "%s)",
                                (reader['customer_id'], reader['company_name'],
                                 reader['contact_name']))
            # Заполняем таблицу employees_data из employees_data.csv
            with open(file_name2) as csvfile:
                readers = csv.DictReader(csvfile)
                for reader in readers:
                    cur.execute("INSERT INTO employees_data VALUES (%s, %s, "
                                "%s, %s, %s, %s)",
                                (reader['employee_id'], reader["first_name"],
                                 reader['last_name'], reader['title'], reader[
                                     'birth_date'], reader['notes']))
            # Заполняем таблицу orders_data из orders_data.csv
            with open(file_name3) as csvfile:
                readers = csv.DictReader(csvfile)
                for reader in readers:
                    cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, "
                                "%s, %s)",
                                (reader['order_id'], reader['customer_id'],
                                 reader['employee_id'], reader[
                                     'order_date'], reader['ship_city']))
finally:
    conn.close()


