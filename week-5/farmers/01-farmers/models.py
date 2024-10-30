class Product:
  _idx = 1

  def __init__(self, name, type):
    self.id = Product._idx
    Product._idx += 1

    self.name = name
    self.type = type

  def __repr__(self):
    return f'<Product {self.name}>'


class Stock:
  _idx = 1

  def __init__(self, product_id, qty, price, expiry):
    self.id = Stock._idx
    Stock._idx += 1

    self.product_id = product_id
    self.qty = qty
    self.price = price
    self.expiry = expiry

  def __repr__(self):
    return f'<Stock {self.product_id}>'


products = {
    1: Product('milk', 'dairy'),
    2: Product('apple', 'fruit'),
    3: Product('honey', 'others')
}

stocks = {
    1: Stock(product_id=1, qty=3, price=40, expiry=2),
    2: Stock(product_id=2, qty=4, price=200, expiry=10),
    3: Stock(product_id=3, qty=5, price=500, expiry=1000)
}


def add_product(product):
  products[product.id] = product


def add_stock(stock):
  stocks[stock.id] = stock
