# Hunter Leise
# CSCI-3202 Problem Set 3
# Problem 3.2

from math import log2

x = 27

set1_yes = x
set1_no = 50

set2_yes = x
set2_no = 50

set3_yes = (100 - 2 * x)
set3_no = 0

set1_total = set1_yes + set1_no
set2_total = set2_yes + set2_no
set3_total = set3_yes + set3_no

set1_weight = set1_total / (set1_total + set2_total + set3_total)
set2_weight = set2_total / (set1_total + set2_total + set3_total)
set3_weight = set3_total / (set1_total + set2_total + set3_total)

pa = set1_yes / set1_total  # P(set 1 yes)
pb = set1_no / set1_total  # P(set 1 no)
pc = set2_yes / set2_total  # P(set 2 yes
pd = set2_no / set2_total  # P(set 2 no)
pe = set3_yes / set3_total  # P(set 3 yes)
pf = set3_yes / set3_total  # P(set 3 no)

set1_entropy = set1_weight * ((-pa * log2(pa)) + (-pb * log2(pb)))
set2_entropy = set2_weight * ((-pc * log2(pc)) + (-pd * log2(pd)))
set3_entropy = set3_weight * ((-pe * log2(pe)) + (-pf * log2(pf)))

entropy = set1_entropy + set2_entropy + set3_entropy
print(entropy)
