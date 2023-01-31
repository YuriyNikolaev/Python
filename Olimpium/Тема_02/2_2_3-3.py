# 2_2_3-3.py
# Дан символ. Определите, верно ли, что он является маленькой латинской буквой.

simb = 'а'
chk_smb = ord(simb)
print("chk_smb = ", chk_smb)
# символы с 97 по 122
if chk_smb in range(97, 123):
   print("yes")
else:
    print("no")