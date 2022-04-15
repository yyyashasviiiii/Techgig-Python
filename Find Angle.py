
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
  
import math
def main():

 # Write code here 
 a = int(input())
 b = int(input())
 c = math.sqrt(a**2 + b**2)
#  c = c/2.0
#  b = b/2.0
 angle = int(90 - round(math.degrees(math.atan(a/b))))
 print(angle)

main()
