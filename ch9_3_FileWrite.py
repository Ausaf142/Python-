f =open("Writting.txt","wt")#--->text file k liye rt likhte ye by default rhta hai so no need
#but for binary hume likhna hoga "rb","wb"....
#write function mein override kr deta hai pure file ko like jo ek bar likho whi likha jayega
#isliye one by one ek hi file mein likhne k liye apkp append use krna hoga
f.write(" i am learning python")
f.write(" he am learning python")
f.write(" iy am learning python")
f.close()