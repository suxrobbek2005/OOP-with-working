from colorama import Fore, Style


class Restaurant:

    def __init__(self, name):

        self.name = name
        self.menu = {}

    def add_menu_item(self, dish, price):
        """Menyuga ovqat va narx qo'shish."""

        self.menu[dish] = price

    def show_menu(self):
        """Menyuni ko'rsatish."""

        print(f"{Fore.LIGHTBLUE_EX}--- {self.name} Menyu ---{Style.RESET_ALL}")

        for dish, price in self.menu.items():

            print(f"{Fore.YELLOW}{dish}: {Fore.GREEN}${price}{Style.RESET_ALL}")
        

class FastFood(Restaurant):

    def __init__(self, name):

        super().__init__(name)

    def show_menu(self):
        """FastFood menyusini ko'rsatish."""

        print(f"{Fore.LIGHTCYAN_EX}=== Tez ovqatlanish restorani: {self.name} ==={Style.RESET_ALL}")
        super().show_menu()


class FineDining(Restaurant):

    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        """FineDining menyusini ko'rsatish."""

        print(f"{Fore.LIGHTMAGENTA_EX}=== Yuqori darajadagi restoran: {self.name} ==={Style.RESET_ALL}")
        super().show_menu()


if __name__ == "__main__":

    fast_food = FastFood("KFC")
    fast_food.add_menu_item("Burger", 5.99)
    fast_food.add_menu_item("Chicken", 4.99)
    fast_food.add_menu_item("Fries", 2.49)

    
    fine_dining = FineDining("Lue burger")
    fine_dining.add_menu_item("Steak", 25.99)
    fine_dining.add_menu_item("Burger&go", 39.99)
    fine_dining.add_menu_item("Lavash", 29.99)


    fast_food.show_menu()
    fine_dining.show_menu()
