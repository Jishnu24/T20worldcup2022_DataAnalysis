import csv
import psycopg2
from psycopg2.extras import execute_values

projects =[]
csv_filename = 't20-world-cup-22.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        projects.append(row)

#print(projects)
conn = psycopg2.connect(
    database="WorldCup", user='postgres',
    password='root', port='5432'
)
cursor = conn.cursor()
columns = projects[0].keys()
query = "INSERT INTO wordcup_data ({}) VALUES %s".format(','.join(columns))

# convert projects values to list of lists
values = [[value for value in project.values()] for project in projects]

execute_values(cursor, query, values)
conn.commit()