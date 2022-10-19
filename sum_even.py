#A four-digit integer is given. Find the sum of even digits in it.
var_int = 9876
x1 = (var_int // 1000 + 1) % 2 * (var_int // 1000)
x2 = (var_int % 1000 // 100 + 1) % 2 * (var_int % 1000 // 100)
x3 = (var_int % 1000 % 100 // 10 + 1) % 2 * (var_int % 1000 % 100 // 10)
x4 = (var_int % 10 + 1) % 2 * (var_int % 10)
sum_even = x1 + x2 + x3 + x4
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
