from itertools import permutations
s=input("enter:")
words=["".join(p) for p in permutations(s)]
print(words)

