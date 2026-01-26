import math

ac = 2
ab = 7
bc = ab-ac

print(bc)
print(f"1a. fraction of ac : bc = {ac}/{bc}")

'''
ratio_ac = ac
ratio_bc = bc
real_ac = 24

k = real_ac / ratio_ac
real_bc = ratio_bc*k

print(real_bc)
print(f"1b. the length of BC = {real_bc}")
'''


def calculate_actual(ac1, bc1, ac2):
    k = ac2/ac1
    bc2 = bc1*k
    return  bc2

bc2 = calculate_actual(ac, bc, 24)
print(f"1b. the length of BC = {bc2}")
