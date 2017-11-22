

def main():
    name = int(input("Whats your name?"))
    age=int(input("How old are you?"))
    return name, age

def ageCategory():
    name, age=main()
    print(name)
    print(age)

ageCategory()
