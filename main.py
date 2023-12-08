def print_hi(name):
    print(f'Hi, {name}')


def get_bakery_file():
    sales_data_file = open('Bakery.csv', 'r')
    sales_list = []
    for singleSale in sales_data_file:
        sales_list.append(singleSale)
    sales_data_file.close()


if __name__ == '__main__':
    get_bakery_file()
