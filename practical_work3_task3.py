s = str(input("Input any sentense: "))

words = s.split()

result = ""

for i in words:

    if words.count(i) == 1:

        result += i + " "

print(result)