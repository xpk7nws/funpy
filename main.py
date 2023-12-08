def get_bakery_file():
    sales_data_file = open('Bakery.csv', 'r')
    sales_list = []
    for singleSale in sales_data_file:
        sales_list.append(singleSale)
    sales_data_file.close()
    print("lines in file=" + str(len(sales_list)))


if __name__ == '__main__':
    get_bakery_file()
