from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/rstatsp1w1')
def rstats():
    return render_template("rstatsp1w1.html")

@app.route('/rstatsp1w2')
def rstatsp1w2():
    return render_template("rstatsp1w2.html")

@app.route('/rstatsp1w3')
def rstatsp1w3():
    return render_template("rstatsp1w3.html")

@app.route('/rstatsp1w4')
def rstatsp1w4():
    return render_template("rstatsp1w4.html")

@app.route('/rstatsp1w5')
def rstatsp1w5():
    return render_template("rstatsp1w5.html")

@app.route('/rstatsp1w6')
def rstatsp1w6():
    return render_template("rstatsp1w6.html")

@app.route('/rstatsp2w1')
def rstatsp2w1():
    return render_template("rstatsp2w1.html")

@app.route('/rstatsp2w2')
def rstatsp2w2():
    return render_template("rstatsp2w2.html")

@app.route('/rstatsp2w3')
def rstatsp2w3():
    return render_template("rstatsp2w3.html")

@app.route('/rstatsp2w4')
def rstatsp2w4():
    return render_template("rstatsp2w4.html")


if __name__ == "__main__":
    app.run(debug=True)
