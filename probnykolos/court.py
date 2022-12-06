from datetime import datetime


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(
        self,
        width: float = 68,
        length: float = 150,
        address: str = "",
        year_built: int = 0,
    ) -> None:
        if length >= 90 and length <= 120 and width >= 45 and width <= 90:
            self.__width = width
            self.__length = length
        else:
            self.__width = 68
            self.__length = 150
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if value >= 45 and value <= 90:
            self.__width = value
        else:
            self.__width = 68

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value) -> None:
        if value >= 90 and value <= 120:
            self.__length = value
        else:
            self.__length = 150

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value) -> None:
        self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.setter
    def year_built(self, value) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.length * self.width

    @staticmethod
    def validate(other: "Court") -> None:
        if other.year_built <= datetime.now().year and other.year_built > 0:
            pass
        else:
            other.year_built = datetime.now().year

    def __repr__(self) -> str:
        return (
            f"Boisko wybudowane w roku {self.__year_built}, "
            f"o długości {self.__length} metrów i szerokości "
            f"{self.__width} metrów.\nPole powierzchni: "
            f"{self.area()} mkw.\nAdres: {self.__address}\n"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Court):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Court):
            return NotImplemented
        return self.area() != other.area()
