from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/employees')
def employees():
    return render_template('employees.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
