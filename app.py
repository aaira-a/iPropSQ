from flask import Flask, render_template
import requests
app = Flask(__name__)


myparams = {'client_id': 'MT3VHUDOIPPIF00TPOEMOUOV550MISJG21TM0U2RUZZP42XD',
            'client_secret': 'FZI4HLHMZ1U0IKFSHESG2BLAFMOPSU1T2XUMDIAKCWV0FO3C',
            'v': '20141101',
            }
venue_id = '4b058805f964a520fbac22e3'


@app.route('/')
def index():
    text_to_render = 'iPropSQ'
    return render_template('index.html', text_tag=text_to_render)


if __name__ == '__main__':
    app.run(debug=True)