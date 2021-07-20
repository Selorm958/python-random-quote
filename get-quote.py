def prim():
   #print("Keep it logically awesome with Love.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])

if __name__== "__main__":
  prim()
