def tobinary(n):
  bit =""

  while n>0:
    bit += str(n%2)
    n=n//2
  return bit[::-1] 


while True:
  g= input("Give me a sentence: ")
  g = list(g) 
  for x in range(len(g)):
    g[x] = tobinary(ord(g[x]))
  print(" ".join(g)) 