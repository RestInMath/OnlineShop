#add getters and setters
class Product():
    id_counter = 0

    def __init__(self, name, description, parameters):
        Product.id_counter += 1
        self.id = Product.id_counter

        self.name = name
        self.description = description
        self.parameters = parameters

    @classmethod
    def update_id_counter(self, new_value):
        Product.id_counter = new_value