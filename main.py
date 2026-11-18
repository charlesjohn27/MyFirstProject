print("task 1!")
print("==========================")
Student_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
gpa = float(input("Gpa: "))
is_enrolled = True

a = 3
b = 7
a, b = b, a

print (Student_name, age , gpa , is_enrolled)
print(a,b)
print("===========================")
print("task 2!")
print("===========================")
def greet(name):
    return f"Hello,{name}!"

def clean(text):
    return text.strip().title()

def shout(text):
    return text.upper() + "!"

def dialogue(speaker,line):
    return f'{speaker} says:"{line}"'

def initials(full_name):
    words = full_name.split()
    result = ""

    for word in words:
        result += word[0].upper()
    return result


print(greet(input("Enter Your Name : ")))
print(clean(" charles "))
print(shout(input("Shout : ")))
print(dialogue("Cj", "Gwapo!"))
print(initials(input("Initials: ")))