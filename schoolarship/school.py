from colorama import Fore, Style


class Student:

    def __init__(self, name, average_score, is_grant, stipend_amount):

        self.name = name
        self.average_score = average_score
        self.is_grant = is_grant  # True = Davlat granti, False = Kontrakt
        self.stipend_amount = stipend_amount


students = []

count = int(input(Fore.CYAN + "Nechta talaba ma'lumotini kiritmoqchisiz? " + Style.RESET_ALL))

for i in range(count):

    print(Fore.YELLOW + f"\n{i+1}-talabaning ma'lumotlarini kiriting:" + Style.RESET_ALL)
    name = input(Fore.GREEN + "Talaba ismi: " + Style.RESET_ALL)
    average_score = float(input(Fore.GREEN + "O'rtacha bahosi: " + Style.RESET_ALL))
    is_grant = input(Fore.GREEN + "Davlat granti asosida o'qiydimi? (ha/yo'q): " + Style.RESET_ALL).strip().lower() == "ha"
    stipend_amount = int(input(Fore.GREEN + "Stipendiya miqdori (so'm): " + Style.RESET_ALL))

    students.append(Student(name, average_score, is_grant, stipend_amount))


print(Fore.CYAN + "\nDavlat grantida o'qiydigan va o'rtacha bahosi 85 dan yuqori bo'lgan talabalar:" + Style.RESET_ALL)
found = False

for student in students:

    if student.is_grant and student.average_score > 85:

        print(
            Fore.GREEN +
            f"Talaba ismi: {student.name}, "
            f"O'rtacha bahosi: {student.average_score}, "
            f"Stipendiya miqdori: {student.stipend_amount} so'm" +
            Style.RESET_ALL
        )

        found = True

if not found:
    
    print(Fore.RED + "Bunday talabalar topilmadi!" + Style.RESET_ALL)
