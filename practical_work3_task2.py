s = str(input("Input any word: "))

result = ""

for i in s:

    if i.isalpha():

        result += i

print(result)