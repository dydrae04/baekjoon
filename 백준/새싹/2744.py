eng=input()
answer=""
for i in eng:
    if i in "ABCEDFGHIJFKLMNOPQRSTUVWEYZ":
        i=i.lower()
        answer+=i
    else:
        i=i.upper()
        answer+=i
print(answer)