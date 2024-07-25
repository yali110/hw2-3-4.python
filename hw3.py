##exercise 1
id: int = int(input(" enter id number"));
year_of_birth: int = int(input(" enter your year of birth"));
print(f"id: {id}, full name: {full_name}, height: {height}, year of birth: {year_of_birth}");

##exercise 2
grade: int = int(input("what is your grade?"));
if 0 <= grade <= 40 :
    print("try harder next time");
elif 41 <= grade <= 60:
    print("you are getting there, need some work");
elif 61 <= grade <= 80:
    print("pretty good");
elif 81 <= grade <= 95:
    print("awesome!!");
elif 96 <= grade <= 100 :
    print("excellent!! you are a star!!!");
elif 0 > grade > 100:
    print("illegal grade");

##exercise 3
volume: int = int(input("what is the volume level?"));
match volume :
    case 0:
        print("mute");
    case 1:
        print("very quiet");
    case 2:
        print("very quiet");
    case 3:
        print("quiet");
    case 4:
        print("moderately quiet");
    case 5:
        print("medium");
    case 6:
        print("moderately loud");
    case 7:
        print("loud");
    case 8:
        print("very loud");
    case 9:
        print("extremely loud ");
    case 10:
        print("extremely loud");
    case _:
        print("invalid volume level");

#exercise 4 :
number = int(input("enter number"));
if number % 7 == 0:
    print("seven boom");
else:
    print("not seven boom");

#exercise 5:
number_2 = int (input("enter number"));
if number_2 % 5 == 0:
    print("fizz");
if number_2 % 3 == 0:
    print("buzz");
if number_2 % 5 == 0 and number_2 % 3 == 0:
    print("fizz buzz");






