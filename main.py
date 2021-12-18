import json
import os
from pprint import pprint

from cook_book import Cook_book
from recept import Receipt

path = os.path.join(os.getcwd(), 'recipes.txt')


def main():
    cook_book = Cook_book()
    with open(path) as file:
        for dish in file:
            receipt = Receipt(dish.strip())
            cook_book.add_recept(receipt)
            count_dishes = int(file.readline().strip())
            for item in range(count_dishes):
                ingridient_name, count_ingridient, unit_of_measure = file.readline().split('|')
                receipt.add_ingridient(ingridient_name, count_ingridient, unit_of_measure)
            file.readline()
    print(cook_book)
    pprint(cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




if __name__ == "__main__":
    main()