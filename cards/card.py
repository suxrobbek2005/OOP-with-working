from colorama import Style, Fore


class ShoppingCart:

    def __init__(self):

        self.cards_list = []
        self.count = 0

        print(f"\n{Style.DIM},{Fore.LIGHTBLUE_EX}Xizmat turlari:{Style.RESET_ALL}")

        print(f"\n,{Style.BRIGHT},{Fore.LIGHTGREEN_EX} --> Yangi mahsulot qo‘shish {Style.RESET_ALL}")
        print(f"{Style.BRIGHT},{Fore.LIGHTGREEN_EX} --> Maxsulotlarni kurish {Style.RESET_ALL}")
        print(f"{Style.BRIGHT},{Fore.LIGHTGREEN_EX} --> Mahsulot o'chirish {Style.RESET_ALL}")
        print(f"{Style.BRIGHT},{Fore.LIGHTGREEN_EX} --> Jami mahsulotlar narxini kurish {Style.RESET_ALL}")
        print(f"{Style.BRIGHT},{Fore.LIGHTGREEN_EX} --> Dasturdan chiqish {Style.RESET_ALL}")


    def add_item(self):

        length = int(input(f"{Style.BRIGHT},{Fore.LIGHTGREEN_EX}----> Nechta card malumotlarini kiritmoqchisiz {Style.RESET_ALL} "))

        for i in range(length):

            print(f"{Style.DIM},{Fore.LIGHTCYAN_EX},{i + 1}, - Cardni malumotlarini kiriting: {Style.RESET_ALL} ")
                
            card_who = input(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX},Card egasini nomini kiriting: {Style.RESET_ALL} ")
            card_number = input(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX},Card raqamanini kiriting: {Style.RESET_ALL} ")
            card_expirly = input(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX},Card mudatini kiriting: {Style.RESET_ALL} ")
            card_phoneNumber = input(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX},Cardga o'langan telifon raqamini kiriting: {Style.RESET_ALL} ")
            card_price = int(input(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX},Card narxini kiriting: {Style.RESET_ALL} "))

            self.cards_list.append({

                "card_who": card_who,
                "card_number": card_number,
                "card_expirly": card_expirly,
                "card_phoneNumber": card_phoneNumber,
                "card_price": card_price

            })

            self.count += 1
            print(f"{Fore.LIGHTYELLOW_EX},Card savatga qushildi {Fore.RESET}")
        
    def take_out_consol(self):

        if self.count > 0:

            for i in self.cards_list:
                 
             print(f"{Style.DIM}{Fore.YELLOW}Card egasi: {i['card_who']}, "
                f"16 talik codi: {i['card_number']}, "
                f"Cardning amal qilish muddati: {i['card_expirly']}, "
                f"Cardga o'langan raqam: {i['card_phoneNumber']}, "
                f"Card narxi: {i['card_price']} {Style.RESET_ALL}")

                        
        else:

            print(f"{Fore.LIGHTYELLOW_EX},Sizda birorta malumot qushilmagan{Fore.RESET}")

    def remove_item(self):

        dell = input(f"{Style.BRIGHT},{Fore.BLUE},Cardni egasini kiriting {Style.RESET_ALL}")

        for i in self.cards_list:

            if i['card_who'] == dell:

                self.cards_list.remove(i)
                print(f"{Fore.MAGENTA} Card muvaffaqiyalti o'chirildi {Fore.RESET}")

a1 = ShoppingCart()
a1.add_item()
a1.take_out_consol()
a1.remove_item()
