from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/k<int:page_num>")
def render_k_pages(page_num):
    if 1 <= page_num <= 12:
        return render_template(f"k{page_num}.html")

if __name__ == "__main__":
    app.run()