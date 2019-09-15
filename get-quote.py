import random
def primary():
  #print("Keep it logically awesome.")
  
  f = open("quotes.txt","a")
  wrt = input("Enter any novel quote:")
  f.write("\n" + wrt)
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  rnd = random.randint(0, last)
  print("Quotes:\n"+quotes[rnd],end="")
  rnd = random.randint(0, last)
  print(quotes[rnd],end="")

if __name__ == "__main__":
  primary()
