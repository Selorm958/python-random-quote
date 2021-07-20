def prim():
   #print("Keep it logically awesome with Love.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[4])
  print(quotes[2])

if __name__== "__main__":
  prim()
