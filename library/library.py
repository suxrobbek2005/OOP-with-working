from colorama import Fore, Style


class AdvancedLibrary:

    def __init__(self):

        self.books_list = []

    def AddBooks(self):
        """Bu funksiya kitob qo'shish vazifasini bajaradi""" 

        length = int(input(Fore.BLUE + "Nechta kitobning ma'lumotini kiritmoqchisiz? " + Style.RESET_ALL))

        for i in range(length):

            book_name = input(Fore.GREEN + "Kitob nomini kiriting: " + Style.RESET_ALL)
            book_author = input(Fore.GREEN + "Kitobning muallifini kiriting: " + Style.RESET_ALL)
            book_number = int(input(Fore.GREEN + "Kitobning raqamini kiriting: " + Style.RESET_ALL))
            due_book = int(input(Fore.GREEN + "Kitobning qaytarish muddatini kiriting (kun): " + Style.RESET_ALL))

            self.books_list.append({

                "book_name": book_name,
                "book_author": book_author,
                "book_number": book_number,
                "due_book": due_book

            })

            print(Fore.YELLOW + f"{book_name} muvaffaqiyatli qo'shildi!" + Style.RESET_ALL)

    def borrower(self):
        """Kitobdan qarzi borligini tekshirib beradi"""

        print(Fore.CYAN + "Kitoblardan qarzdorlar ro'yxati:" + Style.RESET_ALL)
        found = False

        for book in self.books_list:

            if book["due_book"] <= 0:

                print(Fore.RED + f"{book['book_name']} kitobdan qarzdorlik mavjud!" + Style.RESET_ALL)
                found = True

        if not found:

            print(Fore.GREEN + "Hech kim qarzdor emas!" + Style.RESET_ALL)

    def due_date(self):
        """Amal qilish muddatini tekshirib beradi va kitobni o'chiradi"""

        find_book = input(Fore.BLUE + "O'chirish uchun kitob nomini kiriting: " + Style.RESET_ALL)

        for book in self.books_list:

            if book['book_name'] == find_book:

                self.books_list.remove(book)
                print(Fore.YELLOW + f"{book['book_name']} muvaffaqiyatli o'chirildi!" + Style.RESET_ALL)
                return

        print(Fore.RED + "Bunday kitob topilmadi!" + Style.RESET_ALL)

    def TakeOutConsole(self):

        """Kiritilgan ma'lumotlarni terminalga chiqarish vazifasini bajaradi"""
        if not self.books_list:
            print(Fore.RED + "Hozircha hech qanday kitob kiritilmagan!" + Style.RESET_ALL)
            return

        print(Fore.CYAN + "Kutubxonadagi kitoblar ro'yxati:" + Style.RESET_ALL)

        for book in self.books_list:
            
            print(
                Fore.GREEN + f"Kitob nomi: {book['book_name']}, "
                f"Muallifi: {book['book_author']}, "
                f"Raqami: {book['book_number']}, "
                f"Qaytarish muddati: {book['due_book']} kun" + Style.RESET_ALL
            )


a = AdvancedLibrary()
a.AddBooks()
a.borrower()
a.due_date()
a.TakeOutConsole()
