from flask import Flask, render_template

app = Flask(__name__) #這裡的app是實體名稱  和app.py沒有關係

@app.route("/") #這裡的app是一個decorator (這邊三個app彼此都沒有關係)
def index():
    return render_template("index.html")

