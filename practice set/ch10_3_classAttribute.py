class Sample:
    a="Harry"

obj=Sample()
obj.a="Vicky"
# Sample.a="Vicky"          #class k ander jo hai wo wahi hoga jo obj k refrance value add hoga wo obj k liye hai
                        #isliye jb hum direct sample.a krk value denge tb value class ko hoga
print(Sample.a)
print(obj.a)