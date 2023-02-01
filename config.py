import psycopg2
from psycopg2.extras import execute_values




conn = psycopg2.connect(
    database="WorldCup", user='postgres',
    password='root', port='5432'
)