from colorama import Style, Back, Fore

class Market:

    def __init__(self):

        self.shops = []

    def enter_data(self):

        length = int(input(f"{Style.DIM}, {Fore.LIGHTGREEN_EX}, Nechta dukoni malumotini kiritmoqchisiz {Style.RESET_ALL}"))
        
        for i in range(length):

            print(f"{Style.DIM}, {Fore.LIGHTYELLOW_EX}, {i + 1} - Dukoni malumotini kiriting ")

            self.market_name = input(f"{Style.BRIGHT}, {Fore.LIGHTRED_EX}, Dukon nomini kiriting {Style.RESET_ALL}").title()
            self.location = input(f"{Style.BRIGHT}, {Fore.LIGHTRED_EX},Dukon manzilini kiriting {Style.RESET_ALL}").title()
            self.marketible_type = input(f"{Style.BRIGHT}, {Fore.LIGHTRED_EX},Dukon qanaqa turdaligini kiriting {Style.RESET_ALL}").title()
            self.time_work = float(input(f"{Style.BRIGHT}, {Fore.LIGHTRED_EX},Dukon ishlash vaqtini kiriting {Style.RESET_ALL}"))

            self.shops.append({

                "market_name": self.market_name,
                "location": self.location,
                "marketible_type": self.marketible_type,
                "time_work": self.time_work

            })

    def consule(self):

        for i in self.shops:

            if i["marketible_type"] == "elektironika".title():

                print(f"{Style.NORMAL}, {Fore.LIGHTBLACK_EX}, Dukon nomi: {self.market_name}, Manzili: {self.location}, Dukoninig tijorat turi: {self.marketible_type} Ish vaqti: {self.time_work}, {Style.RESET_ALL}")

            else:
                print(f"{Style.BRIGHT}, {Fore.LIGHTCYAN_EX}, Sizda xali birorta xam elektironikaga oid dukon kiritilmagan ")

market = Market()
market.enter_data()
market.consule()
        



