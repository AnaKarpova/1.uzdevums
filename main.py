text = input("Ievadiet tekstu: ")
def countWords(text):
  summa = 0
  sar1 = text.split()
  for word in sar1:
    if len(word)>1:
      summa += 1
  print("Tekstā ir", summa , "vārdi")
  return summa
countWords(text)