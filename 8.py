# Maping the number to a day of the week
    
num = int(input("Enter a number between 1 and 7: "))

if num >= 1 and num <= 7:
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    day = days[num]
    
    # Result
    print("The day corresponding to", num, "is", day)
else:
    # Error message
    print("Invalid number entered. Please enter a number between 1 and 7.")