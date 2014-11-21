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
    elif request.method == 'POST':
        category = Category(request.form['category'])
        latlong = request.form['lat'] + ',' + request.form['long']
        radius = request.form['radius']
        results = category.full_results(latlong, radius, topfive=False)
        return render_template('results.html', category=category, venues=results, categories=categories.keys(), lat_=request.form['lat'], long_=request.form['long'], radius_=request.form['radius'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
