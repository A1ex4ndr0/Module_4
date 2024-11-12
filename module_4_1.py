from fake_math import divide as fake_div
from true_math import divide as true_div

res1 = fake_div(125, 25)
res2 = fake_div(70, 0)
res3 = true_div(126, 24)
res4 = true_div(71, 0)

print(res1)
print(res2)
print(res3)
print(res4)