def isEven(n):
  if num % 2 == 0:
      return True
  return False

num = int(input("Enter the Number: "))
print("The number is " + "EVEN" if isEven(num) else "ODD")
