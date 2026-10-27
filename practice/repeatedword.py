def repeatedword(sentence):
  words = sentence.split()
  counts = {}
  for word in words:
      if word in counts:
        counts[word] += 1
      else:
        counts[word]=1
  print(counts)
  
repeatedword(input("Enter input:"))