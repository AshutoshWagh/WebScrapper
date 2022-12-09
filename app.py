import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/back', methods=['GET'])  # route to display the home page
def back():
    return render_template("index.html")

@app.route('/review', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            url = "https://cdn.agenty.com/examples/csv/top-us-retailers-2011.txt"
            uClient = uReq(url)
            Page = uClient.read()
            uClient.close()

            page_html = bs(Page, "html.parser")
            t = str(page_html).split("\n")
            
            
            final = []
            my_dict = {}

            for s in t:
                final.append(s.split(","))
            print(final)

    
            finalFinal = []
            for l in final:
                mydict = {}
                mydict["Rank"] =  l[0]
                mydict["Retailer Name"] =  l[1]
                mydict["# Stores"] =  l[2]
                mydict["Revenue"] =  l[3]
                finalFinal.append(mydict)
            print(finalFinal)

            searchString = request.form['content'].replace("", "")
            
            my_df = pd.DataFrame(final)
            my_df.to_csv('my_csv2.csv', index=False, header=False, mode="w")
            return render_template('results.html', reviews=finalFinal, name=searchString)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=port) 
    # app.run(host='127.0.0.1', port=8001, debug=True)
