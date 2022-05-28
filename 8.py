# a = 5
# b = 7
# c = 9
# a,b,c = 5,7,8
#import random
#l = [random.randint(-10,10) for i in range(10)]
# for i in range(10):
#     l.append(random.randint(-10,10))
#print(l)

# import  colorama
class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house can not built!"
def check_material(amount_of_material, limit):
    if amount_of_material > limit:
        return "enough material"
    else:
        raise BuildingError(amount_of_material)
Check_Material(int(input()), 300)
a = int(input())
f = open("8.txt")
try:
    f.write("Some text")
    print(10/a)
    print("sucssesful")
except ZeroDivisionError:
    print(Fore.RED + 'It is not possible to divide by 0')
except TypeError:
    print(Fore.RED + 'It is not possible to divide by "str"')
except NameError:
    print(Fore.YELLOW + 'You are accessing an object that does not exist')
except:
    print(Fore.RED + 'Some Error')
else:
    print(Fore.GREEN + 'Nothing went wrong')
finally:
    f.close()
    print(Fore.GREEN + 'The "try except" is finished')
input()