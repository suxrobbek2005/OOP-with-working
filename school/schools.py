from colorama import Style, Fore

class School:
    
    def __init__(self):

        self.school = []  # Talabalar ro'yxati

    def add_student(self):

        student_name = input(f"{Fore.LIGHTGREEN_EX} Talabaning ismini kiriting: {Fore.RESET}")
        student_Lname = input(f"{Fore.LIGHTGREEN_EX} Talabaning familyasini kiriting: {Fore.RESET}")

        try:

            student_phone = int(input(f"{Fore.LIGHTGREEN_EX} Talabaning raqamini kiriting: {Fore.RESET}"))

        except ValueError:

            print(f"{Fore.RED} Noto‘g‘ri raqam kiritildi! {Fore.RESET}")
            return

        self.school.append({
            "student_name": student_name,
            "student_Lname": student_Lname,
            "student_phone": student_phone
        })

        print(f"{Style.DIM} {Fore.LIGHTRED_EX} {student_name} muvaffaqiyatli qo'shildi! {Style.RESET_ALL}")

    def delete_student(self):

        dell = input(f"{Fore.LIGHTGREEN_EX} O'quvchining ismini kiriting: {Fore.RESET}")

        for student in self.school:

            if student["student_name"] == dell:

                self.school.remove(student)
                print(f"{Style.NORMAL} {Fore.YELLOW} Talaba muvaffaqiyatli o'chirildi {Style.RESET_ALL}")
                return
            
        print(f"{Style.DIM} {Fore.RED} Talaba topilmadi {Style.RESET_ALL}")

pupil = School()
pupil.add_student()
pupil.delete_student()


            
        

            

        
        
        



