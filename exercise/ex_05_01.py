sum = 0;
count = 0;
while True:
    inputNum = input("Enter a number: ")

    if inputNum == "done":
        break;
    try:
        num = int(inputNum)
    except:
        print("Invalid input")
        continue

    sum = sum + num
    count += 1

print("aver is", sum/count)
