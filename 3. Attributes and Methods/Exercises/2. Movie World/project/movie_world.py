class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f'{customer.__repr__()}\n'
        for dvd in self.dvds:
            result += f'{dvd.__repr__()}\n'
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def find_customer(id, customers):
        for customer in customers:
            if customer.id == id:
                return customer

    @staticmethod
    def find_dvd(id, dvds):
        for dvd in dvds:
            if dvd.id == id:
                return dvd

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: object):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer(customer_id, self.customers)
        dvd = self.find_dvd(dvd_id, self.dvds)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return f"DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer(customer_id, self.customers)
        dvd = self.find_dvd(dvd_id, self.dvds)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"


