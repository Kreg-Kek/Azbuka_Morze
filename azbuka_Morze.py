letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...',
         '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
alfavit = dict(zip(letters, morse))

s = input().upper()
for i in range(len(s)):
    if s[i] == ' ':
        print(' ', end=' ')
    if s[i] in alfavit.keys():
        print(alfavit[s[i]], end=' ')
