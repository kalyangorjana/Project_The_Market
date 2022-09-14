from flask import Flask, render_template
from flask import request, url_for, redirect
import Database as db

# here flask is a module and Flask is the class of that module which is used to create a app.
# render_template is a built-in function of flask module which is used to access the html files of template dir
app = Flask(__name__)

db.create_table()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/contactus")
def contactus():
    return render_template('contactus.html')


@app.route("/plist")
def plist():
    productlist = db.getall()
    return render_template("productlist.html", productlist=productlist)


@app.route("/addproduct", methods=['GET', 'POST'])
def addproduct():
    if request.method == 'GET':
        return render_template("productform.html")
    elif request.method == 'POST':
        # Here we fetch data from form
        pname = request.form['productName']
        pprice = request.form['productPrice']
        pdes = request.form['productDescription']
        # Here we insert data into database
        db.insert(pname, pprice, pdes)
        # After insert we redirect our request to plist function
        return redirect(url_for('plist'))


@app.route("/deleteproduct/<int:id>", methods=['POST', 'GET'])
# /<int:id> = To take inputs
# GET = By default and Not secured Request
# POST = Most Secured Request
def deleteproduct(id):
    if request.method == 'GET':
        # Herewe fetch product from database using id
        product = db.getproductbyid(id)
        # here we pass that product to form in tuple format
        return render_template('confirm.html', product=product)
    elif request.method == 'POST':
        db.delete(id)
        return redirect(url_for('plist'))


@app.route("/updateproduct/<int:id>", methods=['GET', 'POST'])
def updateproduct(id):
    if request.method == 'GET':
        product = db.getproductbyid(id)
        return render_template('updateproductform.html', product=product)
    elif request.method == 'POST':
        # Here we fetch the data from form
        pid = request.form['productId']
        pname = request.form['productName']
        pprice = request.form['productPrice']
        pdes = request.form['productDescription']
        db.update(pid, pname, pprice, pdes)
        return redirect(url_for('plist'))


if __name__ == '__main__':
    app.run(debug=True)
