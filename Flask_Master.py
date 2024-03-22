from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/contacts/")
def contacts():
    developer_name = 'Макс Максбетов'
    adrec_name = 'Сигма бассейн 22'
    return render_template('contacts.html', name = developer_name, adrec = adrec_name)

# @app.route("/adrec/")
# def adrec():
#
#     return render_template('adrec.html', name1 = adrec_name)
#

@app.route("/slovar/")
def slovar():
    slovar0_name = 'sigma', 'sigma0'
    return render_template('slovar.html', sigma = slovar0_name)

if __name__ == "__main__":
    app.run(debug=True)
