from colorama import Fore, Style


class Vaqt:

    def __init__(self, soat, minut, sekund):
        self.soat = soat
        self.minut = minut
        self.sekund = sekund

    def __str__(self):

        return f"{self.soat:02d}:{self.minut:02d}:{self.sekund:02d}"


class Hour:

    def __init__(self, vaqt):

        self.vaqt = vaqt

    def oshir(self):

        self.vaqt.soat += 1

        if self.vaqt.soat == 24:

            self.vaqt.soat = 0


class Minut:

    def __init__(self, vaqt):

        self.vaqt = vaqt

    def oshir(self):

        self.vaqt.minut += 5

        if self.vaqt.minut >= 60:

            self.vaqt.minut -= 60
            Hour(self.vaqt).oshir()


class Sekund:

    def __init__(self, vaqt):

        self.vaqt = vaqt

    def oshir(self):

        self.vaqt.sekund += 5

        if self.vaqt.sekund >= 60:

            self.vaqt.sekund -= 60
            Minut(self.vaqt).oshir()


soat = int(input(Fore.GREEN + "Soatni kiriting: " + Style.RESET_ALL))
minut = int(input(Fore.GREEN + "Minutni kiriting: " + Style.RESET_ALL))
sekund = int(input(Fore.GREEN + "Sekundni kiriting: " + Style.RESET_ALL))


vaqt = Vaqt(soat, minut, sekund)


sekund_class = Sekund(vaqt)
sekund_class.oshir()

minut_class = Minut(vaqt)
minut_class.oshir()

hour_class = Hour(vaqt)
hour_class.oshir()


print(Fore.CYAN + f"\nYangi vaqt: {vaqt}" + Style.RESET_ALL)
