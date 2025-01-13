from colorama import Style, Fore

class Car:

    def __init__(self):

        self.cars = []

    def enter_data(self,):

        length = int(input(f"{Style.BRIGHT}, {Fore.YELLOW}, Nechta avtomabil haqida ma'lumot kiritmoqchisiz {Style.RESET_ALL}"))

        for car in range(length):

            print(f"\n{Fore.GREEN}, {car + 1}, - Avtomabil haqida malumot kiriting  ")

            self.car_brand = input(f"{Style.DIM}, {Fore.LIGHTBLUE_EX}, Avtomabil brendini kiritining {Style.RESET_ALL} ")
            self.model = input(f"{Style.DIM}, {Fore.LIGHTBLUE_EX}, Avtomabil modelini kiritining {Style.RESET_ALL} ")
            self. manafacture_year = int(input(f"{Style.DIM}, {Fore.LIGHTBLUE_EX}, Avtomabil yilini kiritining {Style.RESET_ALL} "))
            self. price =  str(input(f"{Style.DIM}, {Fore.LIGHTBLUE_EX}, Avtomabil narxini kiritining {Style.RESET_ALL} "))

            self.cars.append({

                "car_brand": self.car_brand,
                "model": self.model,
                "manafacture_year": self.manafacture_year,
                "price": self.price

            })
    
    def console(self):

        for i in self.cars:

            if i["manafacture_year"] < 2010:

                print(f"{Style.NORMAL}, {Fore.LIGHTBLACK_EX}, Avtomabil brendi: {self.car_brand}, Modeli: {self.model}, Yili: {self.manafacture_year} Narxi: {self.price}, {Style.RESET_ALL}")

car = Car()
car.enter_data()
car.console()