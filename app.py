import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask
import csv
from config import conn
import psycopg2
from psycopg2.extras import execute_values


app = Flask(__name__)


@app.route("/match_Won_By_1st_Batting_or_2nd", methods=['GET'])
def match_Won_By_1st_Batting_or_2nd():
    cur = conn.cursor()


    cur.execute("SELECT * FROM wordcup_data")
    Data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]

    # Store the column names in a list
    columns = column_names

    df = pd.DataFrame(Data, columns=columns)
    # print(df)

    df["Match Won By 1st Batting or 2nd"] = ''

    d1 = pd.DataFrame()
    d1['Whether Team Won by winning Toss'] = np.where(
    (df['toss_winner'] == df['winner']), 'Yes', 'No')
    # print(d1)

    col = 'Whether Team Won by winning Toss'
    count = d1.groupby(col).size()
    # print(type(count))
    d2 = pd.DataFrame(count)


    plot = d2.plot.pie(y=0, figsize=(5, 5), autopct='%1.1f%%')
    plt.title("Pie Chart to show whether team won by winning toss or not")
    plt.show()

    cur.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)

