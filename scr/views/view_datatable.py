from flask import Blueprint, render_template
from scr.models.ejemplo1 import ejemplo1
from scr.models.ejemplo2 import ejemplo2

main = Blueprint('datatable_bp', __name__)


@main.route('/ejemplo1')
def get_items():
    Items = ejemplo1.get_items()
    print(Items)
    return render_template('/ejemplo1.html', Items=Items)


@main.route('/ejemplo2')
def get_customerranking():
    customerranking = ejemplo2.get_customerranking()

    return render_template('/ejemplo2.html', customerranking=customerranking)
