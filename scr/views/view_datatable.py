from flask import Blueprint, render_template
from scr.models.ejemplo1 import ejemplo1
from scr.models.ejemplo2 import ejemplo2
from scr.models.ejemplo3 import ejemplo3
from scr.models.ejemplo4 import ejemplo4
from scr.models.ejemplo5 import ejemplo5
from scr.models.ejemplo6 import ejemplo6

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

@main.route('/ejemplo3')
def get_productbrands():
    productbrands = ejemplo3.get_productbrands()

    return render_template('/ejemplo3.html', productbrands=productbrands)

@main.route('/ejemplo4')
def get_productsDataSource():
    productsDS= ejemplo4.get_productsDataSource()

    return render_template('/ejemplo4.html', productsDS=productsDS)

@main.route('/ejemplo5')
def get_printingProductList():
    printingProductList= ejemplo5.get_printingProductList()

    return render_template('/ejemplo5.html', printingProductList=printingProductList)

@main.route('/ejemplo6')
def get_exportProductList():
    exportProductList= ejemplo6.get_exportProductList()

    return render_template('/ejemplo6.html', exportProductList=exportProductList)