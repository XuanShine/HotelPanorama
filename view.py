from flask import Flask, render_template, send_from_directory
from flask import redirect, request, flash
from os import path

from werkzeug.utils import secure_filename
import yaml
from datetime import date
import pdb
from adjust_prices import list_number_room_booked

# app = Flask(__name__)

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
        ))


app = CustomFlask(__name__)


@app.route("/")
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route("/chambre.html")
def room():
    return render_template('chambre.html')


@app.route("/equipement.html")
def equipement():
    return render_template('equipement.html')


@app.route("/map.html")
def map():
    return render_template('map.html')


@app.route("/savoir.html")
def savoir():
    return render_template('savoir.html')


@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route('/prix/<int:year>-<int:month>-<int:day>/<type_room>')
def price(year, month, day, type_room):
    with open('price.yaml', 'r') as f_in:
        price = (yaml.load(f_in.read())[date(year, month, day)]
                                       [type_room.replace('_', ' ')])
    return str(price)


@app.route('/prix')
def price_main():
    return render_template('price.html')


@app.route('/ajuster_prix', methods=['GET', 'POST'])
def adjust_prices():
    if request.method == 'POST':
        # check if the post request has the file part
        # pdb.set_trace()
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(path.join('tmp', filename))
            text = yaml.dump(list_number_room_booked(
                                path.join('tmp', filename)),
                                default_flow_style=False)
            return str(text).replace('\n', '<br>')
    return render_template('adjust_price.html')


@app.route('/css/<path:path_file>')
def send_css(path_file):
    return send_from_directory('static', path.join('css', path_file))


@app.route('/js/<path:path_file>')
def send_js(path_file):
    return send_from_directory('static', path.join('js', path_file))


@app.route('/photo/<path:path_file>')
def send_photo(path_file):
    return send_from_directory('static', path.join('photo', path_file))


@app.route('/img/<path:path_file>')
def send_img(path_file):
    return send_from_directory('static', path.join('img', path_file))


@app.route('/color/<path:path_file>')
def send_color(path_file):
    return send_from_directory('static', path.join('color', path_file))


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
