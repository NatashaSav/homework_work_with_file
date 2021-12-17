class Receipt:
    def __init__(self, name):
        self.ingridients = []
        self.name = name

    def add_ingridient(self, name, quantity, measure):
        self.ingridients.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})

    def __str__(self):
        recept_format = '{}: [\n'.format(self.name)
        for item in self.ingridients:
            recept_format += "\t\t{},\n".format(item.__str__())
        recept_format += '\t\t]'
        return recept_format


