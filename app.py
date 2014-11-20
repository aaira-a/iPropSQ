from flask import Flask, render_template, request
from models import Category, categories

app = Flask(__name__)


@app.route('/')
def index():
    text_to_render = 'iPropSQ'
    return render_template('index.html', text_tag=text_to_render)


@app.route('/results', methods=['GET', 'POST'])
def show_results():
    if request.method == 'GET':
        category = Category('elementary_school')
        results = category.full_results('3.1175,101.6773', '1000', topfive=False)
        return render_template('results.html', category=category, venues=results, categories=categories.keys())
    else:
        category = Category('mall')
        latlong = request.form['lat'] + ',' + request.form['long']
        results = category.full_results(latlong, '1000', topfive=False)
        return render_template('results.html', category=category, venues=results, categories=categories.keys())


if __name__ == '__main__':
    app.run(debug=True)
