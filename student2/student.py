from colorama import Fore, Style

class Student:

    def __init__(self):

        self.student = []
        self.count = 0

    def enter_data_student(self):

        length = int(input(f"{Style.NORMAL},{Fore.LIGHTBLUE_EX}Nechta talabaning ruyxatini kiritmoqchisiz {Style.RESET_ALL}"))

        for i in range(length):

            print(f"{Style.BRIGHT},{Fore.LIGHTRED_EX},{i + 1} - Talabaning malumotlarini kiritinig {Style.RESET_ALL}")

            student_name = input(f"{Style.DIM},{Fore.LIGHTYELLOW_EX},Talabaning ismini kirining {Style.RESET_ALL} ")
            student_course = (input(f"{Style.DIM},{Fore.LIGHTYELLOW_EX},Talabaning kursi kirining {Style.RESET_ALL} "))
            student_avarge = int(input(f"{Style.DIM},{Fore.LIGHTYELLOW_EX},Talabaning baxosini kirining {Style.RESET_ALL} "))
            student_scholarship = int(input(f"{Style.DIM},{Fore.LIGHTYELLOW_EX},Talabaning stipendiyasini kirining {Style.RESET_ALL} "))

            self.student.append({

                "student_name": student_name,
                "student_course": student_course,
                "student_avarge": student_avarge,
                "student_scholarship": student_scholarship

            })

            print(f"{Fore.LIGHTRED_EX},{student_name}, Talabar ruyxatiga kiritildi{Fore.RESET}\n")

    def take_out_console(self):

        print(f"{Style.DIM},{Fore.YELLOW},== Talabarning ruyxati == {Style.RESET_ALL}\n")

        for i in self.student:

            print(f"{Style.DIM},{Fore.MAGENTA},Talabaning ismi: {self.student['student_name']}, Kursi: {self.student['student_course']},"
                f"Baxosi: {self.student['student_avarge']}, Stipendiyasi: {self.student['student_scholarshio']}, {Style.RESET_ALL}")
            
    def max_scholarship_grade(self):

        print(f"{Fore.LIGHTBLUE_EX},== Yo'qori stipindiya oluvchi talabalar ruyxati == {Fore.RESET}")

        for i in self.student:

            if i['student_avarge'] > 1_000_000 and i['student_scholarship'] > 80:

                print(f"{Style.DIM},{Fore.LIGHTGREEN_EX},1 mln dan yuqori stipindiya oluvchilar {self.i['student_scholarship']}",
                      f"80 balldan yo'qori olgan talabalar {self.i['student_avarge']},{Style.RESET_ALL}")

students = Student()
students.enter_data_student()
students.max_scholarship_grade()
   





