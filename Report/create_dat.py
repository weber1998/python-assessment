class Create_dat:

    def write(self):

        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 20, 30, 40, 50]

        with open("sample.dat", "w") as file:
            for x, y in zip(x_data, y_data):
                file.write(f"{x}\t{y}\n")
