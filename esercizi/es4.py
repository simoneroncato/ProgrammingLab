class CSVfile():
    def __init__(self, name):
        self.name = name
        self.data_list = []
    def get_data(self):
        for line in self.name:
            line = line.strip()
            elements = line.split(',')
            if elements[0] != 'Date':
                self.data_list.append(float(elements[1]))
        return self.data_list


with open("shampoo_sales.csv", 'r') as my_file:
    file = CSVfile(my_file)
    print(file.get_max())

