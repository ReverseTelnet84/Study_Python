# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Semin", "Seoul")

greet_with(location="Seoul", name="Semin")


# Love Calculator
# def calculate_love_score(name1, name2):
#
#     true_list = ["t", "r", "u", "e"]
#     love_list = ["l", "o", "v", "e"]
#
#     true_count = 0
#     love_count = 0
#
#     for name in name1:
#         if name in true_list:
#             true_count += 1
#         if name in love_list:
#             love_count += 1
#
#     for name in name2:
#         if name in true_list:
#             true_count += 1
#         if name in love_list:
#             love_count += 1
#
#     love_score = str(true_count) + str(love_count)
#     print(f"Love Score = {love_score}")
#
#
# calculate_love_score(name1="Brad Pitt".lower(), name2="Jennifer Aniston".lower())