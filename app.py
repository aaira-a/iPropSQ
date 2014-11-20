from flask import Flask, render_template
from models import Category

app = Flask(__name__)


@app.route('/')
def index():
    text_to_render = 'iPropSQ'
    return render_template('index.html', text_tag=text_to_render)


@app.route('/results')
def show_results():
    category = Category('college_university')
    results = category.full_results('3.1175,101.6773', '1000', topfive=False)
    return render_template('results.html', category=category, venues=results)


if __name__ == '__main__':
    app.run(debug=True)
