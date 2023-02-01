import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask
import csv
from config import conn
import psycopg2
from psycopg2.extras import execute_values


app = Flask(__name__)


def create_app():
    app=Flask(__name__)
    with app.app_context():
        @app.route('/won_after_winning_toss',methods=['GET'])
        def won_after_winning_toss():
        

            df["Match Won By 1st Batting or 2nd"]=''

            d1=pd.DataFrame()
            d1['Whether Team Won by winning Toss']=np.where((df['toss_winner'] == df['winner']),'Yes','No')
            # print(d1)

            col='Whether Team Won by winning Toss'
            count=d1.groupby(col).size()
            #print(type(count))
            d2=pd.DataFrame(count)
            plot=d2.plot.pie(y=0, figsize=(5,5),autopct='%1.1f%%')
            plt.title("Pie Chart to show whether team won by winning toss or not")
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            return Response(buf.getvalue(), mimetype='image/png')
        @app.route('/most_player_of_the_match',methods=['GET'])
        def most_player_of_the_match():
            # dt=df.dropna()
            sns.countplot(y='player_of_match',data=df)
            buf=io.BytesIO()
            plt.savefig(buf,format='png')
            buf.seek(0)
            return Response(buf.getvalue(),mimetype='image/png')
        @app.route('/won_1st_or_2nd_battings',methods=['GET'])
        def win_1st_or_2nd_battings():
            Data=df.dropna()

            d1=pd.DataFrame()
            d1['Whether Team Won by 1st Batting or 2nd']=np.where((Data['won_by'] == 'Runs'),'1st Batting','2nd Batting')


            col='Whether Team Won by 1st Batting or 2nd'
            count=d1.groupby(col).size()
            d2=pd.DataFrame(count)

            plot=d2.plot.pie(y=0, figsize=(5,5),autopct='%1.1f%%')
            plt.title("Pie Chart to show whether team won by 1st Batting or 2nd Batting")
            buf=io.BytesIO()
            plt.savefig(buf,format='png')
            buf.seek(0)
            return Response(buf.getvalue(),mimetype='image/png')
            # plt.show()
            # plt.savefig("D:\T20 World Cup\Plots/Fig.png")
        @app.route('/top_scorer', methods=['GET'])
        def top_scorer():
            
            # dt=df.dropna()
            sns.barplot(x='top_scorer',y='highest_score',data=df)
            plt.xticks(rotation = 'vertical')
            buf=io.BytesIO()
            plt.savefig(buf,format='png')
            buf.seek(0)
            return Response(buf.getvalue(),mimetype='image/png')
        @app.route('/total_score_in_each_venue',methods=['GET'])
        def total_score_in_each_venue():
            Data=df.dropna()
            
            plt.bar(Data["venue"], Data["first_inn_score"] + Data["second_inn_score"])
            plt.xlabel("Venue")
            plt.ylabel("Total Score")
            plt.title("Total Score in each Venue")
            plt.xticks(rotation=30)
            buf=io.BytesIO()    
            plt.savefig(buf,format="png")
            buf.seek(0)
            return Response(buf.getvalue(),mimetype='image/png')
        @app.route("/best_stadiums_to_bat_first_or_chase",methods=['GET'])
        def best_stadiums_to_bat_first_or_chase():
                pass
                
            
    return app

#sns.barplot(x='top_scorer',y='highest_score',data=df)
# plt.xticks(rotation = 'vertical')
# plt.show()
# sns.countplot(y='venue',data=df)
# plt.show()
# Close the cursor and connection
conn.close()
if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)