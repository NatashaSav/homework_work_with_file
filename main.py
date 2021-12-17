import os

from cook_book import Cook_book
from recept import Receipt

path = os.path.join(os.getcwd(), 'recipes.txt')


def main():
    cook_book = Cook_book()
    with open(path) as file:
        for shop in file:
            receipt = Receipt(shop.strip())
            cook_book.add_recept(receipt)
            count_dishes = int(file.readline().strip())
            for item in range(count_dishes):
                ingridient_name, count_ingridient, unit_of_measure = file.readline().split('|')
                receipt.add_ingridient(ingridient_name, count_ingridient, unit_of_measure)
            file.readline()

    print(cook_book)



if __name__ == "__main__":
    main()