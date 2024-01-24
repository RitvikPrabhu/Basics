#Lookup table create with all unique symbols of integers to roman numerals, including the stipulations mentioned on Leetcode
intToRomDict = {
      1000: "M",
      900: "CM",
      500: "D",
      400: "CD",
      100: "C",
      90: "XC",
      50: "L",
      40: "XL",
      10: "X",
      9: "IX",
      5: "V",
      4: "IV",
      1: "I",
  }

#This function takes a number as the argument and converts it into a Roman numeral.
#We store the result as an empty string initially and make changes as the loop progresses.
# The loop goes through all the keys in the dictionary (Parsed as a list from highest to lowest). As long as the iterator numeral is less than or equal to the argument passed in, we will append the roman numeral representation of the iterator to the empty string, while simultaneosly subtracting the argument by the iterator. The final string is then returned by the function
#This code was written by Ritvik Prabhu and was written on VIM. 
def intToRoman(num):
	result = ''
	for i in sorted(intToRomDict.keys(), reverse=True):
		while i <= num:
			result += intToRomDict[i]
			num -= i
	return result

#Print statement to test out the output of the code.
print(intToRoman(1994)) 

