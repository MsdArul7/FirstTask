#cod
from collections import Counter
def mineoperation(N,String):
    freq = Counter(String)
    operations = []
    result = 0
    for char,count in freq.items():
        if count % 2 != 0:
            operations.append(f"{char} {N}")
            result += 1
            N = N
    print(result)
    for operation in operations:
        print(operation)
N = int(input())
String = input()
mineoperation(N, String)

#Print a single integer: the number of words in the sentence that start with a vowel.
from collections import Counter