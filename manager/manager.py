from colorama import Fore, Style


class Manager:

    def __init__(self, name, position, hours_worked, salary):
        self.name = name
        self.position = position
        self.hours_worked = hours_worked
        self.salary = salary


employees = []

count = int(input(Fore.CYAN + "Nechta xodimning ma'lumotini kiritmoqchisiz? " + Style.RESET_ALL))

for i in range(count):

    print(Fore.YELLOW + f"\n{i+1}-xodimning ma'lumotlarini kiriting:" + Style.RESET_ALL)
    name = input(Fore.GREEN + "Xodim ismi: " + Style.RESET_ALL)
    position = input(Fore.GREEN + "Lavozimi: " + Style.RESET_ALL)
    hours_worked = int(input(Fore.GREEN + "Ishlagan vaqti (soat): " + Style.RESET_ALL))
    salary = int(input(Fore.GREEN + "Ish haqi (so'm): " + Style.RESET_ALL))
    
    employees.append(Manager(name, position, hours_worked, salary))

print(Fore.CYAN + "\nIsh vaqti 40 soatdan yuqori va lavozimi 'Rahbar' bolgan xodimlar:" + Style.RESET_ALL)
found = False

for employee in employees:

    if employee.hours_worked > 40 and employee.position.lower() == "rahbar":

        print(
            Fore.GREEN +
            f"Xodim ismi: {employee.name}, "
            f"Lavozimi: {employee.position}, "
            f"Ish vaqti: {employee.hours_worked} soat, "
            f"Ish haqi: {employee.salary} so'm" +
            Style.RESET_ALL
        )
        
        found = True

if not found:
    print(Fore.RED + "Bunday xodimlar topilmadi!" + Style.RESET_ALL)
