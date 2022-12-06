from court import Court


class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(
        self,
        width: float = 68,
        length: float = 150,
        address: str = "",
        year_built: int = 0,
        name: str = "",
        common_name: str = "",
        capacity: int = 0,
    ) -> None:
        super().__init__(width, length, address, year_built)
        self.__name = name
        self.__common_name = common_name
        if capacity < 0:
            self.__capacity = 0
        else:
            self.__capacity = capacity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def common_name(self) -> str:
        return self.__common_name

    @common_name.setter
    def common_name(self, value: str) -> None:
        self.__common_name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value < 0:
            self.__capacity = 0
        else:
            self.__capacity = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.area() == other.area() and self.capacity == other.capacity

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.area() != other.area() or self.capacity != other.capacity

    def __repr__(self) -> str:
        rep = (
            f"Boisko wybudowane w roku {self.year_built}, o długości "
            f"{self.length} metrów i szerokości {self.width} metrów.\n"
            f"Pole powierzchni: {self.area()} mkw.\n"
            f"Adres: {self.address}.\nNazwa: {self.name}.\n"
            f"Nazwa zwyczajowa: {self.common_name}.\n"
            f"Pojemność stadionu: {self.capacity} osób.\n"
        )
        rep2 = (
            f"Boisko wybudowane w roku {self.year_built}, o długości "
            f"{self.length} metrów i szerokości {self.width} metrów.\n"
            f"Pole powierzchni: {self.area()} mkw.\n"
            f"Adres: {self.address}.\nNazwa: {self.name}.\n"
            f"Pojemność stadionu: {self.capacity} osób.\n"
        )
        if self.common_name:
            return rep
        return rep2
