class Building:
    year = None
    city = None
#"Pupils:", self.pupils

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupils)


class House (Building):
    pass

class Shop (Building):
    pass

school = School(150, 2000, "Smila.")
school.get_info()
house = Building(1995, "Smila.")
shop = Building(1980, "Smila.")

# просто коментар

print("ttnhth")