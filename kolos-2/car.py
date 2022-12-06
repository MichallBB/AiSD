from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022, price: float = 0, colour: str = None,
                 extra_seats: int = 0):
        super().__init__(reg, model, prod_year)
        self.__colour = colour
        if price < 0:
            self.__price = 0
        else:
            self.__price = price
        if extra_seats < 0:
            self.__extra_seats = 0
        else:
            self.__extra_seats = extra_seats

    @property
    def colour(self) -> str:
        return self.__colour

    @colour.setter
    def colour(self, wart: str) -> None:
        self.__colour = wart

    @property
    def extra_seats(self) -> int:
        return self.__extra_seats

    @extra_seats.setter
    def extra_seats(self, wart: int) -> None:
        if wart < 0:
            print('Extra_seats nie spełnia warunkow')
        else:
            self.__price = wart

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, wart: float) -> None:
        if wart < 0:
            print('Price nie spelnia warunkow')
        else:
            self.__price = wart

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.__prod_year}! Ma kolor {self.__colour}'

    def __eq__(self,other):
        if self.__colour == other and self.__model == other:
            return True

    def __ne__(self, other):
        if self.__colour != other and self.__model == other:
            return False

    def __repr__(self):
        if self.reg is None and self.colour is None:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n' \
                   f'Cena: {self.__price}\n' \
                   f'Dodatkowe siedzeinia: {self.__extra_seats}\n '
        if self.reg is None:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n' \
                   f'Cena: {self.__price}\n' \
                   f'Kolor: {self.__colour}\n' \
                   f'Dodatkowe siedzeinia: {self.__extra_seats}\n '
        if self.colour is None:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n' \
                   f'Rejestracja: {self.__reg}\n' \
                   f'Cena: {self.__price}\n' \
                   f'Dodatkowe siedzeinia: {self.__extra_seats}\n '
        else:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n' \
                   f'Rejestracja: {self.__reg}\n' \
                   f'Cena: {self.__price}\n' \
                   f'Kolor: {self.__colour}\n' \
                   f'Dodatkowe siedzeinia: {self.__extra_seats}\n '

