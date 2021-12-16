d1={1:200,2:20,3:100}
d2={2:40,4:70}
print("d1=",d1)
print("d2=",d2)
for key in d2:
    if key in d1:
        d2[key]=d2[key]+d1[key]
else:
    pass
d1.update(d2)
print("merged=",d1)
