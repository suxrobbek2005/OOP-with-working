from colorama import Style, Fore

class Phone:

    def __init__(self, name, brand, volume, price):

        self.name = name
        self.brand = brand
        self.volume = int(volume)
        self.price = float(price)

save_data = []

length = int(input(f"{Fore.LIGHTMAGENTA_EX}, Nechta telifoni malumot kiritmoqchisiz {Fore.RESET}"))

for i in range(length):

    print(f"{Style.BRIGHT}, {Fore.LIGHTBLUE_EX} ,{i + 1} - Telifon malumotlarni kiriting {Style.RESET_ALL}")

    name = input(f"{Fore.BLUE},Telifon nomini kiriting {Fore.RESET} ")
    brand = input(f"{Fore.BLUE},Telifon brendini kiriting {Fore.RESET} ")
    volume = int(input(f"{Fore.BLUE}, Telifon Xotirasini kiriting {Fore.RESET} "))
    price = float(input(f"{Fore.BLUE}, Telifon narxini kiriting {Fore.RESET} "))
    
    print(f"{Style.BRIGHT}, {Fore.LIGHTYELLOW_EX}, Nomi: {name}, Brendi: {brand}, Ram: {volume}, Narxi: {price}, {Style.RESET_ALL}")    

if volume == -1 and name == '-1' and brand == '-1' and price == float(-1):
    print(f"{Fore.LIGHTWHITE_EX}, Dasturimizda biror bir muomoga o'chragan bulsangiz izohda yozib ketishing mumkin {Fore.RESET}")
    exit()


