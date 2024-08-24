# Program 1
# height = float(input("Enter your height in meters :"))
# weight = int(input("Enter your weight in kgs :"))
#
# BMI = weight / (height * height)
#
# if BMI > 30:
#     print("Obesity")
# elif 25 <= BMI <= 29:
#     print("Overweight")
# elif 18.5 <= BMI < 25:
#     print("Normal")
# else:
#     print("Underweight")


# Program 2
# Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
# UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#
# countries = {
#     "Sydney": "Australia",
#     "Melbourne": "Australia",
#     "Brisbane": "Australia",
#     "Perth": "Australia",
#     "Dubai": "UAE",
#     "Abu Dhabi": "UAE",
#     "Sharjah": "UAE",
#     "Ajman": "UAE",
#     "Mumbai": "India",
#     "Bangalore": "India",
#     "Chennai": "India",
#     "Delhi": "India",
# }
#
# city = input("Enter a city name : ")
# country = countries.get(city)
#
# if country:
#     print(f"{city} is in {country}")
# else:
#     print("City is not in the list!")


# Program 3
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

countries = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India",
}
city1 = input("Enter city1:")
city2 = input("Enter city2:")

country1 = countries.get(city1)
country2 = countries.get(city2)

if country1 == country2:
    print(f"Both belong to {country1}")
else:
    print("They don't belong to the same country")