from colorama import Fore, Style, Back
import student


names1 = student.Student('Sherbek', 'Nizmiddinov', '1', 65)
names2 = student.Student('Olimjon', 'Murtazoyev', '2',  80)
names3 = student.Student('Abdurasul', 'Salimov', '5', 98)
names4 = student.Student('Suxrobbek', 'Yaxshiboyev', '2', 90)
names5 = student.Student('Asror', 'Qurbonazarov', '1', 89)

print(f"{Style.DIM}, {Fore.BLUE}, {Back.CYAN} {names1.name}, {names1.last_name}, Kursi: {names1.course}, O'rtacha baxosi: {names1.grade}, {Style.RESET_ALL}")
print(f"{Style.DIM}, {Fore.BLUE}, {Back.CYAN} {names2.name}, {names2.last_name}, Kursi: {names2.course}, O'rtacha baxosi: {names2.grade}, {Style.RESET_ALL}")
print(f"{Style.DIM}, {Fore.BLUE}, {Back.CYAN} {names3.name}, {names3.last_name}, Kursi: {names3.course}, O'rtacha baxosi: {names3.grade}, {Style.RESET_ALL}")
print(f"{Style.DIM}, {Fore.BLUE}, {Back.CYAN} {names4.name}, {names4.last_name}, Kursi: {names4.course}, O'rtacha baxosi: {names4.grade}, {Style.RESET_ALL}")
print(f"{Style.DIM}, {Fore.BLUE}, {Back.CYAN} {names5.name}, {names5.last_name}, Kursi: {names5.course}, O'rtacha baxosi: {names5.grade}, {Style.RESET_ALL}")