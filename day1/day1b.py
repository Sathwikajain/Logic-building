# Program 2 to find the size of different data types
import sys
# Variables of different types
integer = 10
floating = 10.5
character = 'A'
double_num = 10.555555555  # Python float behaves like double

# Print sizes
print("Size of int:", sys.getsizeof(integer), "bytes")
print("Size of float:", sys.getsizeof(floating), "bytes")
print("Size of double:", sys.getsizeof(double_num), "bytes")
print("Size of char:", sys.getsizeof(character), "bytes")