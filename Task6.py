import math

# Program 1
# friends_list = ["Dharmi", "Tanvi", "Priyanshi", "Khushi", "Dhruti"]
# friends_tuple = []
#
# for i in friends_list:
#     friends_tuple.append((i, len(i)))
#
# print(friends_tuple)

# Program 2
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total_exp = sum(your_expenses.values())
partner_total_exp = sum(partner_expenses.values())

print(f"You spent: {your_total_exp}")
print(f"Your partner spent: {partner_total_exp}")

if your_total_exp > partner_total_exp:
    print("You spent more money than your partner")
else:
    print("Your partner spent more money than you")

diff = 0
max_diff_category = None
for category in your_expenses.keys():
    diff1 = math.fabs(partner_expenses.get(category) - your_expenses.get(category))
    if diff < diff1:
        diff = diff1
        max_diff_category = category


print(f"Difference: {int(diff)}")
print(f"Category: {max_diff_category}")

