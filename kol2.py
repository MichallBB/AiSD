from typing import List

class Tab_ros_s:
    dane: List[float]
    zajetosc: int
    pojemnosc: int
    przyrost: int

    def __init__(self, przyrost):
        self.dane = []
        self.zajetosc = 0
        self.pojemnosc = 0
        self.przyrost = przyrost

    def ustal(self, idx: int, wartosc: float):
        assert idx >= 0, "Idx must be >= 0"
        while self.pojemnosc < idx+1:
            self.pojemnosc += self.przyrost
        temp = [0] * self.pojemnosc
        i = 0
        for x in self.dane:
            temp[i] = x
            i += 1
        temp[idx] = wartosc
        self.dane = temp

        i = -1
        temp = 0
        while True:
            if self.dane[i] != 0:
                temp = -i - 1
                break
            i = i - 1
        self.zajetosc = self.pojemnosc - temp

    def pobierz(self, idx: int) -> float:
        if idx + 1 > self.zajetosc:
            return 0
        return self.dane[idx]

    def usun_el(self, idx: int):
        i = idx
        while True:
            if i == self.pojemnosc-1:
                self.dane[i] = 0
                break
            self.dane[i] = self.dane[i+1]
            i += 1
        self.zajetosc -= 1

    def uprosc(self):
        #przechodzenie od konca
        i = -1
        temp = 0
        while True:
            if self.dane[i] != 0:
                temp = -i - 1
                break
            i = i - 1
        self.zajetosc = self.pojemnosc - temp

        # zrobienie tablicy z samych danych
        temp = [0]*self.zajetosc
        for x in range(self.zajetosc):
            temp[x] = self.dane[x]
        self.dane = temp

        #jesli zajetosc jest mniejsza od przyrostu
        roznica = self.przyrost - self.zajetosc
        if roznica > 0:
            self.dane += [0]*roznica

        self.pojemnosc = len(self.dane)

        # dodanie jesli pojemnosc nie jest wielokrotnoscia przyrostu
        while (self.pojemnosc % self.przyrost) != 0:
            self.pojemnosc += 1
        roznica = self.pojemnosc - len(self.dane)
        self.dane += [0] * roznica

    def __str__(self):
        text = ''
        for x in range(self.zajetosc):
             text += str(self.dane[x]) + '; '
        return text



x = Tab_ros_s(4)
x.ustal(0,7)
x.ustal(1,5)
x.ustal(2, 3)
x.ustal(4,4)
x.ustal(5,1)
x.usun_el(1)
x.uprosc()

x.dane = [7,3,0,0,0,0,0,0,0]
x.zajetosc = 5
x.pojemnosc = 9
x.przyrost = 3
print(x)

