from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

scroute = Blueprint('shopping_cart', __name__)

products = [
		{
			'name': 'Bag',
			'price': 50
		},

		{
			'name': 'Shoes',
			'price': 100
		},

		{
			'name': 'Socks',
			'price': 25
		}

	]

in_products = []
count = 0

@scroute.route('/')
def index():
	return render_template('default/shopping_cart.html', products=products, in_products=in_products, count=count)

@scroute.route('/', methods=['POST'])
def post_item():
	name = request.form['prodName']
	price = request.form['prodPrice']

	prod = {
		'name': name,
		'price': price
	}

	in_products.append(prod)

	return redirect(url_for('.index'))	