from colorama import Fore, Style


class Instrument:

    def __init__(self, name, price, manufacturer, type_):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.type_ = type_


instrument_list = []

count = int(input(Fore.CYAN + "Nechta musiqa asbobi kiritmoqchisiz? " + Style.RESET_ALL))

for i in range(count):

    print(Fore.YELLOW + f"\n{i+1}-musiqa asbobini kiritish:" + Style.RESET_ALL)

    name = input(Fore.GREEN + "Asbob nomi: " + Style.RESET_ALL)
    price = int(input(Fore.GREEN + "Narxi (so'm): " + Style.RESET_ALL))
    manufacturer = input(Fore.GREEN + "Ishlab chiqaruvchi: " + Style.RESET_ALL)
    type_ = input(Fore.GREEN + "Turi (masalan, klaviatura, struna): " + Style.RESET_ALL)

    instrument_list.append(Instrument(name, price, manufacturer, type_))

# Narxi 2 mln so‘mdan yuqori va turi klaviatura bo‘lgan musiqa asboblarini chiqarish
print(Fore.CYAN + "\nNarxi 2 mln so‘mdan yuqori va turi klaviatura bo‘lgan musiqa asboblari:" + Style.RESET_ALL)

found = False

for instrument in instrument_list:

    if instrument.price > 2000000 and instrument.type_.lower() == "klaviatura":

        print(
            Fore.GREEN +
            f"Asbob nomi: {instrument.name}, "
            f"Narxi: {instrument.price} so'm, "
            f"Ishlab chiqaruvchi: {instrument.manufacturer}, "
            f"Turi: {instrument.type_}" +
            Style.RESET_ALL
        )

        found = True

if not found:

    print(Fore.RED + "Bunday musiqa asboblari topilmadi!" + Style.RESET_ALL)
