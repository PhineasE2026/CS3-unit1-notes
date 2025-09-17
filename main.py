print("Gorb")

lucky_num = 37
my_name = "Car Sifflington"
cash = 5.50
is_raining = True
is_sunny = False

greeting = "Howdy, " + my_name
print(greeting)

greeting = 'Shalom yeled, Ani akshev\' barukh ata adonai'
print(greeting)

long_greeting = """
                Oh shmeep shmorp gleep atanadeep
                In western lands there stood a sheep
                Leaping round the evergreens
                Moschep alep gatanamep
                """

print(long_greeting)

# f-strings are FORMATTED strings (like templates)
f_string = f"Hello my name is {my_name} and i pay with {cash}"
print(f"Hello my name is {f_string} and i pay with {cash}")

f_string2 = "Hibiscus Tea"

def HibiscusTeaSimulation():
    #function body indented under the colon
    print("Hello Hisibsuvc Tea iam functional")
    print("Habisucs tea")
    print("hibisucs")

HibiscusTeaSimulation()

def multiply(x, y):
    return x * y

print(multiply(150230, 403201))

five_times_three = multiply(5, 3)
print(five_times_three)

one_hundred_seventy_five_billion_times_three_thousand_sixty_five_plus_seven_to_the_power_of_3 = (multiply(175000000000,3365) + (7 ** 3))

print(one_hundred_seventy_five_billion_times_three_thousand_sixty_five_plus_seven_to_the_power_of_3)

print(multiply(20, 6))

# *** LISTS ***
#ordered mutable sequences
empty_list = list() # constructor
another_empty_list = []

class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)
print(len(class_roster))

first_item = class_roster[0]
print(first_item)

#Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

lottery_nums = [13, 7, 89, 99, 44, 23, 4]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums)
lottery_nums.sort()
print(lottery_nums)
class_roster.sort(reverse=True)
print(class_roster)
class_roster.sort()

class_roster.append("Alex")
class_roster.insert(0, "Zoie")
class_roster.remove("Zoie")
class_roster.pop()
print(class_roster)

print(13 in lottery_nums)

# *** TUPLES ***
# sorted, immutable
# useful for "snapshot" of a row of data
student = ('Finny', 17, 'Computer Science', 4.0)
print(student)
# student[3] = 2.6

# *** SETS ***
# unsorted, stores other immutable types
# no duplicates allowed
songs = {'Stranger', '3005', '7', '3', 'Mutt', 'Freeze', '3005'}
print(songs)
# sets can be used to de-duplicate list items
colors = ['blue', 'pink', 'purple', 'blue', 'pink']
print(set(colors))

songs.add('Gypsy')
songs.add('Stranger')

print(songs)

# *** DICTIONARIES ***
# mutable, but the keys can only be immutable types, like strings
# { key: value } pairs. keys must be unique
# unordered
characters = { 'Aelin': 'Assassin queen',
              'Karate Kid': 'pupil',
              'Mr. Miyagi': 'sensei',
              'Phil Dunphy': 'dad',
              'Wall-E': 'trash robot',
              'Princess Peach': 'damsel in distress',
              'Dexter': 'serial killer'
              }

print(len(characters))
# dictionary with numerical keys, list values
grade_requirements = { 
    9: ['Bio'],
    10: ['Chem'],
    11: ['Physics', 'Math', 'English', 'PE'],
    12: ['Math', 'English', 'PE']
    }