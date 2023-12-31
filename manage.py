from flask import Flask, render_template
from scr.views import  view_datatable

import os

template_dir = os.path.abspath('scr/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def principal():
    return render_template("index.html")


if __name__ == '__main__':
    app.register_blueprint(view_datatable.main,url_prefix='/')
    app.run(debug=True)
