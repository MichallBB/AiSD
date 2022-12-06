from court import Court
from stadium import Stadium


def main():
    court_1 = Court(68, 150, "Słoneczna 10, 10-100 Olsztyn", 1999)
    print(court_1)
    court_2 = Court(500, 500, "Słoneczna 10, 10-100 Olsztyn", 1999)
    print(court_2)
    court_3 = Court(address="Słoneczna 10, 10-100 Olsztyn", year_built=1999)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    court_1.year_built = 2030
    print(court_1)
    Court.validate(court_1)
    print(court_1)
    print("------stadium------")
    stadium_1 = Stadium(
        year_built=1999,
        address="Słoneczna 10, 10-100 Olsztyn",
        name="Słoneczny stadion",
        common_name="Słoneczko",
        capacity=10000,
    )
    print(stadium_1)
    stadium_2 = Stadium(
        width=50,
        length=100,
        year_built=1999,
        address="Słoneczna 10, 10-100 Olsztyn",
        name="Słoneczny stadion",
        capacity=10000,
    )
    print(stadium_2)
    stadium_1.year_built = 2030
    print(stadium_1)
    Stadium.validate(stadium_1)
    print(stadium_1)
    print(stadium_1 == stadium_2)
    stadium_1.length, stadium_1.width = 100, 50
    print(stadium_1 == stadium_2)
    print(stadium_1 != stadium_2)
    stadium_1.capacity = 500
    print(stadium_1 == stadium_2)


if __name__ == "__main__":
    main()
