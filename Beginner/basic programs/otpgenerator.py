# import library
import math, random, string
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = string.digits
    OTP = ""
 
   # length of password can be chaged
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
 
# Driver code
if __name__ == "__main__" :
     
    print("OTP of 4 digits:", generateOTP())