secret = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(30):
    msg = ""
    for x in secret:
       letterIndex = (ord(x) - ord('A') + key) % 26
       msg += chr(ord('a') + letterIndex)
    print(key, msg)
