import hashlib

hash = input("[-] Enter MD5 hash : ")
wordlist = input("[-] Enter wordlist name : ")

try:
    pass_file = open(wordlist)
except:
    print("[*] ERROR: Could not open file")
    exit()
for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == hash:
        print("[+] Password found ")
        print("[+] Password: "+word)

print("Made By Mani")