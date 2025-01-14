from colorama import Style, Fore


class Student:


    def __init__(self):

        self.student = []  
        self.count = 0    

    def enter_student(self):
        """Talabalarni ro'yxatga olish."""

        length = int(input(f"{Fore.LIGHTBLUE_EX}Nechta talabani ro'yxatga olmoqchisiz? {Fore.RESET}"))

        for i in range(length):

            print(f"{Style.DIM}{Fore.LIGHTYELLOW_EX}{i + 1} - O'quvchini ma'lumotlarini to'ldiring{Style.RESET_ALL}")

            name = input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Talabaning ismini kiriting: {Style.RESET_ALL}").title()
            age = int(input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Talabaning yoshini kiriting: {Style.RESET_ALL}"))
            grades = int(input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Talabaning bahosini kiriting: {Style.RESET_ALL}"))

            self.student.append({

                "name": name,
                "age": age,
                "grades": grades

            })

            self.count += 1

            print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{name} Talabaning ma'lumotlari saqlandi!{Style.RESET_ALL}\n")

    def take_out(self):
        """Barcha talabalar ma'lumotlarini ko'rsatish."""

        print(f"{Fore.LIGHTBLUE_EX}== Talabalar ro'yxati =={Style.RESET_ALL}")

        for student in self.student:

            print(f"{Style.NORMAL}{Fore.LIGHTYELLOW_EX}Talabaning ismi: {student['name']}, Yoshi: {student['age']}, "
                  f"Bahosi: {student['grades']}{Style.RESET_ALL}")

    def get_average(self):
        """O'rtacha bahoni hisoblash."""

        if self.count == 0:

            print(f"{Fore.RED}Talabalar ro'yxati bo'sh!{Style.RESET_ALL}")

            return

        total = sum(student["grades"] for student in self.student)
        average = total / self.count
        
        print(f"{Fore.LIGHTBLUE_EX}Umumiy {self.count} talabaning o'rtacha bahosi: {round(average)}{Style.RESET_ALL}")


students = Student()
students.enter_student()  
students.take_out()      
students.get_average()    
