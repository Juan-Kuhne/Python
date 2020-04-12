from random import choices

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passw = ""

l = choices(s, k=8)
for i in range(0, 8):
    passw += l[i]
print(passw)
