#exercise 1:
a = 1
b = 1
if  a == b:
    print(" True")
else:
    print(" False")

#exercise 3:
temp: float = float(input("what is the temperature ?"));
print("hot" if temp > 30 else "normal");

#exercise 4:
print("numbers from 10 to 20:");
for i in range (10, 21):
    print(i, end=" ");
print()

print("numbers from 10 to 20 in steps of 2:");
for i in range (10, 21 , 2):
     print(i, end=" ");
print()

gap: int = int(input("what is the gap?"));
print(f"numbers in step of {gap}");
for i in range (10, 21 , gap):
    print(i, end=" ")
print()

tarting_point: int = int(input("what number do i start with?"));
ending_point: int = int(input("what number do i finish with? "));
gap_2: int= int(input("what is the gap?"));
for starting_point in range(starting_point, ending_point, gap_2):
    print(starting_point, end=" ")

#exercise 5:
total_iq_before: int = 0
students: int = 0
while True:
    iq = int(input("enter the iq before studies"));
    if 30 > iq or iq > 300:
        break
    total_iq_before += iq
    students += 1
if students > 0:
    avg = total_iq_before / students;
    print(f"the average iq of the students is: {avg:.2f}");

print("a year after python studies...");
total_iq_after : int = 0
students_after : int = 0
while True:
    iq_after = int(input("enter the iq after studies"));
    if 30 > iq_after or iq_after > 300:
        break
    total_iq_after += iq
    students_after += 1

if students_after > 0:
    avg_after = total_iq_after / students_after
    print(f"the average after python studies: {avg_after:.2f}");

diff = avg_after - avg
print(f"the average is bigger by {diff}");

#exercise 6:
str1 = input("enter your string1")
str2 = input("enter your string2")

while True :
    if str1 == str2:
        print(f"the strings are identical: {str1}");
    else :
        print(f"{str1} {str2}");
