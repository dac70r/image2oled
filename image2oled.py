
import imageio
import numpy as np

# declaring variables

row = 0;
column = 0;
index = 0;
sum = 0; 

a = 0;
b = 0;
c = 0;


im = imageio.imread('too_loud.png') #read image, convert to data and store in array
print(im.shape) #shows the dimensions of the read image

# print(64*96)
# print(im[0][0][0],bin(im[0][0][0]))
# print(im[0][0][1],bin(im[0][0][1]))
# print(im[0][0][2],bin(im[0][0][2]))



# print(a,b,c)
# print(bin(a),bin(b),bin(c))

print(sum,":",bin(im[0][0][0]).replace("0b", "pixel_data = 16'b"),";")

for column in range (64):
   for row in range (96):
        a = int(im[column][row][0]/255*31)
        b = int(im[column][row][1]/255*63)
        c = int(im[column][row][2]/255*31)
        print(sum," :pixel_data = 16'b"+bin(a).replace("0b","").zfill(5)+"_"+bin(b).replace("0b","").zfill(6)+"_"+bin(c).replace("0b","").zfill(5)+";")

        sum = sum + 1



