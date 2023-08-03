class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		integer = 0
		symbols={"I":1,"II": 2, "III":3 ,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		#first case:
		if s in symbols.keys():
			integer = symbols[s]
			return integer
		#second case (subtractions):
		symbols_b={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
		if s in symbols_b.keys():
			integer = symbols_b[s]
			return integer
		#third case
		symbols.update(symbols_b)


s=Solution()
print(s.romanToInt("XCIX"))
