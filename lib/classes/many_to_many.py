class Coffee:

    def __init__(self, name):
        self.name = name

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, "_name"):
            self._name = name 
        
    def orders(self):
        coffee_orders = [order for order in Order.all if order.coffee == self]
        return coffee_orders
    
    def customers(self):
        customer_set = {order.customer for order in Order.all if order.coffee == self}
        customer_list = list(customer_set)
        return customer_list
    
    def num_orders(self):
        orders = [order for order in Order.all if order.coffee == self]
        count = len(orders)
        return count
    
    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee == self]
        average = sum(prices) / len(prices) 
        return average

class Customer:

    def __init__(self, name):
        self.name = name

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        orders = [orders for orders in Order.all if orders.customer == self]
        return orders
    
    def coffees(self):
        coffee_set = {order.coffee for order in Order.all if order.customer == self}
        coffee_list = list(coffee_set)
        return coffee_list
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "_price"):
            self._price = price
            return self._price
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
            return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
            return self._coffee
    
