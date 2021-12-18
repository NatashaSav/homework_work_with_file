class Cook_book:
    def __init__(self):
        self.recept_list = []

    def add_recept(self, recept):
        self.recept_list.append(recept)

    def get_shop_list_by_dishes(self, recept_list, person_count):
        ingridients = dict()
        for dish in self.recept_list:
            if dish.name not in recept_list:
                continue
            for ingridient in dish.ingridients:
                ingridients[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] * person_count}
        return ingridients

    def __str__(self):
        cook_book_format = "cook_book = {\n\t"
        for receipt in self.recept_list:
            cook_book_format += '{},\n\t'.format(receipt)
        cook_book_format += '}'
        return cook_book_format