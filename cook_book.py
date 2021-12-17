class Cook_book:
    def __init__(self):
        self.recept_list = []

    def add_recept(self, recept):
        self.recept_list.append(recept)

    def __str__(self):
        cook_book_format = "cook_book = {\n\t"
        for receipt in self.recept_list:
            cook_book_format += '{},\n\t'.format(receipt)
        cook_book_format += '}'
        return cook_book_format