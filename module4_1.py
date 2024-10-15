from fake_math import divide as fk_div
from true_math import divide as tr_div


print('result1 = ', fk_div(55, 5))
print('result2 = ', fk_div(55, 0))
print('result3 = ', tr_div(77, 7))
print('result4 = ', tr_div(77, 0))