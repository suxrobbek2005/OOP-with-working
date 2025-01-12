from colorama import Style, Fore


class Move:

    def __init__(self, name, duration, reyting, year):

        self.name = name
        self.duration = float(duration)
        self.reyting = float(reyting)
        self.year = year
    
    def duration_film(self):

        if self.duration >= 1.50:
            self.reyting -= 0.5

moves = [
    Move(name="The social network", duration=2, reyting=7.7, year='2010'),
    Move(name="Steve Jobs", duration=2.2, reyting=7.8, year='2015'),
    Move(name="Ex Machina", duration=1.48, reyting=6.3, year='2014'),
    Move(name="Hackers",duration=1.55, reyting=8.0, year='1995'),
    Move(name="The Imitation Game", duration=1.54, reyting=8.2, year='2014'),
    Move(name="Tron: Legacy", duration=2.5, reyting=6.8, year='2010')
]          

for movess in moves:
    movess.duration_film()
    
for movess in moves:
    print(f"{Style.NORMAL}, {Fore.RED}, Kino nomi: {movess.name}, Davomiyligi: {movess.duration}, Yili: {movess.year}, {Style.RESET_ALL}")



            
        

