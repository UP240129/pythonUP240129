A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Exercise 1 (Level 2)

C = A|B # C=A.union(B)
print(C)

#Exercise 2 (Level 2)
print(A.intersection(B))

#Exercise 3 (Level 2)
print(A.issubset(B))

#Exercise 4 (Level 2)

print(A.isdisjoint(B))

#Exercise 5 (Level 2)

D = B|A

print(C==D)

#Exercise 6 (Level 2)
print(A.symmetric_difference(B))

#Exercise 7 (Level 2)

del A
del B

