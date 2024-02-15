def sum_csv (my_file):
    values = []
    for line in my_file:
        elements = line.split (',')
        if elements[0] != 'Date':
            elements[0]
            value = float(elements[1])
            values.append(value)
    return sum(values)

my_file = open('shampoo_sales.csv', 'r')
somma = sum_csv (my_file)
print(somma)