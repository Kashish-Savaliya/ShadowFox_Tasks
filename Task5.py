# Program 1
# import random
#
# i = 0
# count_6 = 0
# count_1 = 0
# count = 0
# prev_no = None
#
# for i in range(20):
#     curr_no = random.randint(1, 6)
#     print(curr_no)
#
#     if prev_no == 6:
#         if prev_no == curr_no:
#             count += 1
#
#     if curr_no == 6:
#         count_6 += 1
#     elif curr_no == 1:
#         count_1 += 1
#
#     prev_no = curr_no
#
# print("Number of times 6 was rolled:", count_6)
# print("Number of times 1 was rolled:", count_1)
# print("Number of times you rolled two 6s in a row:", count)

# Program 2

for i in range(1, 101):
    if i % 10 == 0:
        ans = input("Are you tired ? : ")
        if ans == "yes" or ans == 'y':
            ans1 = input("Do you want to skip remaining sets ? :")
            if ans1 == "yes" or ans1 == 'y':
                print(f"You completed total of {i} jumping jacks")
                break
            elif ans1 == "no" or ans1 == 'n':
                print(f"{100 - i} jumping jacks are remaining")
                continue
        elif ans == "no" or ans == 'n':
            continue


if i == 100:
    print("Congratulations! You have completed your workout")
