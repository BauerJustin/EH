import hashlib

found = False
pass_hash = input("Enter md5 hash: ")

try:
    pass_file = open("passwords.txt", "r")
except:
    print("File not found")
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.md5(encoded_word.strip()).hexdigest()
    if digest == pass_hash:
        print("Password found:")
        print(word)
        found = True
        break

if not found:
    print("Password is not in the list")