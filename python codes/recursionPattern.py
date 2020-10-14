#!/usr/bin/env python3
def pattern(n):
	if(n>1):
		pattern(n-1)
	print(" *"*n)
n=int(input("Enter pattern number: "))
pattern(n)
