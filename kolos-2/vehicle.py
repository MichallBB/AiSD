class Vehicle:
    reg: str
    model: int
    prod_year: int

    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022):
        if model < 0:
            self.__model = 0
        else:
            self.__model = model
        if 1900 < prod_year > 2022:
            self.__prod_year = 2022
        else:
            self.__prod_year = prod_year
        self.__reg = reg

    @property
    def reg(self) -> str:
        return self.__reg

    @reg.setter
    def reg(self, wart: str) -> None:
        self.__reg = wart

    @property
    def model(self) -> int:
        return self.__model

    @model.setter
    def model(self, wart: int) -> None:
        if wart < 0:
            print('Model nie spelnia warunków')
        else:
            self.__model = wart

    @property
    def prod_year(self) -> int:
        return self.__prod_year

    @prod_year.setter
    def prod_year(self, wart: int) -> None:
        if 1900 < wart > 2022:
            print('Rok nie spelnia warunkow')
        else:
            self.__prod_year = wart

    @staticmethod
    def brake():
        print('Zatrzymuje sie')

    def drive(self) -> str:
        return f'Jade swietnym pojazem z roku {self.__prod_year}'

    def __eq__(self, other):
        if self.__model == other or self.__prod_year == other:
            return True

    def __ne__(self, other):
        if self.__model != other or self.__prod_year != other:
            return False

    def __str__(self):
        if self.__reg is None:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n'
        else:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\n' \
                   f'Model: {self.__model}\n' \
                   f'Rejestracja: {self.__reg}'
