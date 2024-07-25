#bonus 1 :
height: float = float(input("what is your height?"));
year_of_birth: int= int(input("what is your year of birth?"));
fname = input(("what is your first name?"));
lname = input(("what is your last name?"));

height_1: float = float(input("what is your height?"));
year_of_birth_1: int= int(input("what is your year of birth?"));
fname_1 = input(("what is your first name?"));
lname_1 = input(("what is your last name?"));

print(f"{height:.2f}, {year_of_birth:<4}, {fname:<10}, {lname:<10}");
print(f"{height_1:.2f}, {year_of_birth_1:<4}, {fname_1:<10}, {lname_1:<10}");

#bonus 2 :
slices_num: int = int(input("how many slices there is?"));
if slices_num % 4 == 0:
    print(f"each one of the friends got {slices_num // 4}, and nothing left ");
else:
    print(f"each one of the friends got {slices_num // 4}, and {slices_num % 4} left");

friends: int = int(input("how many friends came to Dani?"));
slices: int = int(input("how many slices there is?"));
if friends % slices:
    print(f"each one of the friends got {friends // slices}, and nothing left");
else:
    print(f" each one of the friends got {slices // friends}, and {slices % friends} left");

