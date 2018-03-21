num=int(input("enter the numbers"):
def separate_string(sentence):
    l = list(sentence)
    l2 = list()
    for letter in range(l):
        index = l.index(letter)
        if index % 2 != 0:
            l2.append(l[letter])
            l.remove(letter)
separate_string('2,4,6,8,10)
print("display the even numbers are replace with the odd numbers")
