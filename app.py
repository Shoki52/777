from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Данные для продуктов
products_data = {
    "bearings": [
        "Роликовые радиальные подшипники для железнодорожного транспорта",
        "Шариковые подшипники для промышленного оборудования",
        "Подшипники для сельскохозяйственной техники",
        "Подшипники для автомобильной промышленности",
        "Подшипники с угловым контактом для высокоскоростных приложений",
        "Подшипники для тяжелых условий эксплуатации",
    ],
    "asbestos": [
        "Профилированные листы (шифер)",
        "Плиты и трубы из асбестоцемента",
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        action = request.form.get('action')
        category = request.form.get('category')

        if action == 'add':
            new_item = request.form.get('new_item')
            if category and new_item:
                products_data[category].append(new_item)
        elif action == 'delete':
            item_to_delete = request.form.get('item_to_delete')
            if category and item_to_delete in products_data[category]:
                products_data[category].remove(item_to_delete)

        return redirect(url_for('products'))

    return render_template('products.html', products_data=products_data)

if __name__ == '__main__':
    app.run(debug=True)

