from colorama import Style, Fore, Back
import employe 

employer1 = employe.Employee("Sherbek", 1234455)
employer2 = employe.Employee("Azizbek", 345673)
employer3 = employe.Employee("Olimjon", 987654)
employer4 = employe.Employee("Suxrobbek", 678934)
employer5 = employe.Employee("Mehriddin", 3567635)


print(f"{Style.NORMAL}, {Back.YELLOW}, {Fore.GREEN},Xodim ismi: {employer1.name}, Oylik maosh: {employer1.salary}, {Style.RESET_ALL}")
print(f"{Style.NORMAL}, {Back.YELLOW}, {Fore.GREEN},Xodim ismi: {employer2.name}, Oylik maosh: {employer2.salary}, {Style.RESET_ALL}")
print(f"{Style.NORMAL}, {Back.YELLOW}, {Fore.GREEN},Xodim ismi: {employer3.name}, Oylik maosh: {employer3.salary}, {Style.RESET_ALL}")
print(f"{Style.NORMAL}, {Back.YELLOW}, {Fore.GREEN},Xodim ismi: {employer4.name}, Oylik maosh: {employer4.salary}, {Style.RESET_ALL}")
print(f"{Style.NORMAL}, {Back.YELLOW}, {Fore.GREEN},Xodim ismi: {employer5.name}, Oylik maosh: {employer5.salary}, {Style.RESET_ALL}")