sub1 = int(input("Enter your marks\n"))
sub2 = int(input("Enter your marks\n"))
sub3 = int(input("Enter your marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
if(sub1+sub2+sub3)/3<40:
    print("You are Fail due to total marks less than 40")
else:
    print("Congratulation!You are passed")  

    #if --her if satisfy kiya to her if print hoga qk her if executehoga ni to else hoga(ye bhi ye bhi)
    #elif--jo satisfy kiya wha ruk jayega agr koi ni kiya to else execute hoga