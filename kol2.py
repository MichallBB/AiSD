from typing import List

class Tab_ros_s:
    dane: List[float]
    zajetosc: int
    pojemnosc: int
    przyrost: int

    def __init__ (self, zajetosc = 0, pojemnosc = 0, dane = [], przyrost = ...):
#   def __init__(self, przyrost):
        self.dane = dane
        self.zajetosc = zajetosc
        self.pojemnosc = pojemnosc
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

        while True:
            if self.dane[i] != 0:
                temp = -i - 1
                break
            i = i - 1
        self.zajetosc = self.pojemnosc - temp

    def pobierz(self, idx: int) -> float:
        if idx > self.zajetosc:
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

        self.pojemnosc = len(self.dane)
        # dodanie 0 jesli pojemnosc nie jest wielokrotnoscia przyrostu
        while (self.pojemnosc % self.przyrost) != 0:
            self.pojemnosc += 1
        roznica = self.pojemnosc - len(self.dane)
        self.dane += [0] * roznica

    def sortuj(self):
        n = len(self.dane)
        while n > 1:
            for l in range(0, n - 1):
                if self.dane[l] > self.dane[l + 1]:
                    self.dane[l], self.dane[l + 1] = self.dane[l + 1], self.dane[l]
            n -= 1


        #zajetosc
        i = -1
        while True:
            if self.dane[i] != 0:
                temp = -i - 1
                break
            i = i - 1
        self.zajetosc = self.pojemnosc - temp

    def print(self):
        text = self.dane[0:self.zajetosc]
        print(*text, sep=";")



x = Tab_ros_s(przyrost=4)
x.ustal(0,7)
x.ustal(1,5)
x.ustal(2, 3)
x.ustal(4,4)
x.usun_el(1)
print(x.pobierz(3))
x.uprosc()

x.dane = [7,3,0,0,0,0,0,0,0]
x.zajetosc = 5
x.pojemnosc = 9
x.przyrost = 3
#x.uprosc()
x.sortuj()
x.print()

