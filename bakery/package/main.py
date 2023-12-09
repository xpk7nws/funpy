def get_bakery_file():
    sales_data_file = open('Bakery.csv', 'r')
    sales_array = []
    for singleSale in sales_data_file:
        sales_array.append(singleSale)
    sales_data_file.close()
    return sales_array


def main():
    all_sales = get_bakery_file()
    print("lines in file=" + str(len(all_sales)))


if __name__ == '__main__':
    main()
