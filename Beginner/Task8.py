class Avengers:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return (f"name: {self.name}\n"
                f"age: {self.age}\n"
                f"gender: {self.gender}\n"
                f"super_power: {self.super_power}\n"
                f"weapon: {self.weapon}\n")

    def is_leader(self):
        return(self.name == 'Captain America')


avenger1 = Avengers('Captain America', 30, 'Male', 'Super strength', 'Shield')
avenger2 = Avengers('Iron Man', 35, 'Male', 'Technology', 'Armors')
avenger3 = Avengers('Black Widow', 32, 'Female', 'Superhuman', 'Batons')
avenger4 = Avengers('Hulk', 40, 'Male', 'Unlimited strength', 'Mjölnir')
avenger5 = Avengers('Thor', 42, 'Male', 'Super Energy', 'Shield')
avenger6 = Avengers('Hawkeye', 38, 'Male', 'Fighting Skills', 'Bow and Arrows')

super_heroes = [avenger1, avenger2, avenger3, avenger4, avenger5, avenger6]

for hero in super_heroes:
    print(hero.get_info())
    if hero.is_leader():
        print(f"{hero.name} is a leader")
    print()