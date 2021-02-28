from flask import Flask, render_template, request, flash
import time
from searcher import search
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/search")
def searchResult():
    query = request.args.get('query')
    urls = [''] * 5
    searchEni = search("./indexFile/10176TokenDocId.txt", "./indexFile/tf_idfMerge.txt")
    if query != None and query!= "":
        start = time.time()
        try:
            urls = searchEni.start(query)
        except:
            urls = [''] * 5
        searchTime = time.time() - start
        flash(f"Searching completed in {round(searchTime, 5)} seconds.")

    query = "Enter here" if query == None else query
    print(urls)
    return render_template("searchResult.html", one=urls[0], two=urls[1], three=urls[2],
        four=urls[3],five=urls[4], query=query)

if __name__=="__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=2021,host="127.0.0.1",debug=True)
