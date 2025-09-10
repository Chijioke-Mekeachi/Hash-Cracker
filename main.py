# Cracking hash are impossible with the basic computer 
# But the idea here is simple
# you will give the progem a list of text
# The text will be converted to the hashing algorithm perdicted by the program
# then compare each word the see the matching word 
# !!!!!!!!!!!!!!!!!!!Programming is fun !!!!!!!!!!!!!!!!!!

# Author : Chijioke Mekeachi
# Date: 17-1-2025
# Still building don't ask Why

import hashlib
g = 0
def conv(word, hash_type):
  match(hash_type):
  # Statement to deside which hashing algorithm to use
    case 1:
      #MD5
      hash_value = hashlib.md5(
        word.encode()
      ).hexdigest()
      
    case 2:
      #sha1
      hash_value = hashlib.sha1(
        word.encode()
      ).hexdigest()
      
    case 3:
      #sha224
      hash_value = hashlib.sha224(
        word.encode()
      ).hexdigest()
     
    case 4:
      hash_value = hashlib.sha256(
        word.encode()
      ).hexdigest()
      
    case 5:
      hash_value = hashlib.sha384(
        word.encode()
      ).hexdigest()
    case 6:
      hash_value = hashlib.sha512(
        word.encode()
      ).hexdigest()
    case _:
      raise IndexError ("No Hash of such lenght")
  return hash_value

#Main function
def main():
  print("##########################")
  print("       Hash Cracker")
  print("# Author: Chijioke Mekeachi")
  print("# This Program was not build for\n# hacking bank so don't bother")
  print("# Almost forgot keep the wordlist \n# file in same place with this program file")
  print("##########################\n\n")

  hashed_word = str(input("Enter Hash ? "))
  hash_Lenght = hashed_word.len()

  word_list = str(input("Enter WordList Path ? "))
      
  if hash_Lenght == 32:
    hash_type = 1
  elif hash_Lenght == 40:
    hash_type = 2
  elif hash_Lenght == 56:
    hash_type = 3
  elif hash_Lenght == 64:
    hash_type = 4
  elif hash_Lenght == 96:
    hash_type = 5
  elif hash_Lenght == 128:
    hash_type = 6
  else:
    raise ("Exceeded Limit")

  # Cracking hash are impossible with the basic computer 
# But the idea here is simple
# you will give the progem a list of text
# The text will be converted to the hashing algorithm perdicted by the program
# then compare each word the see the matching word 
# !!!!!!!!!!!!!!!!!!!Programming is fun !!!!!!!!!!!!!!!!!!

# Author : Chijioke Mekeachi
# Date: 17-1-2025
# Still building don't ask Why

import hashlib
def lenght(text):
  # script is limited to test with 1024*1024 characters
  try:
    for x in range(1024*1024):
      text[x]
  except IndexError:
    return x

def conv(word, hash_type):
  match(hash_type):
  # Statement to deside which hashing algorithm to use
    case 1:
      #MD5
      hash_value = hashlib.md5(
        word.encode()
      ).hexdigest()
      
    case 2:
      #sha1
      hash_value = hashlib.sha1(
        word.encode()
      ).hexdigest()
      
    case 3:
      #sha224
      hash_value = hashlib.sha224(
        word.encode()
      ).hexdigest()
     
    case 4:
      hash_value = hashlib.sha256(
        word.encode()
      ).hexdigest()
      
    case 5:
      hash_value = hashlib.sha384(
        word.encode()
      ).hexdigest()
    case 6:
      hash_value = hashlib.sha512(
        word.encode()
      ).hexdigest()
    case _:
      raise IndexError ("No Hash of such lenght")
  return hash_value

#Main function
def main():
  g = 0
  print("##########################")
  print("       Hash Cracker")
  print("# Author: Chijioke Mekeachi")
  print("# This Program was not build for\n# hacking bank so don't bother")
  print("# Almost forgot keep the wordlist \n# file in same place with this program file")
  print("##########################\n\n")

  hashed_word = input("Enter Hash ? ")
  hash_Lenght = lenght(hashed_word)

  try:
      word_list = str(input("Enter WordList Path ? "))
  except FileNotFoundError:
      raise FileNotFoundError("Fine does not exist")
      
  if hash_Lenght == 32:
    hash_type = 1
    print("Using md5")
  elif hash_Lenght == 40:
    hash_type = 2
    print("Using sha224")
  elif hash_Lenght == 56:
    hash_type = 3
    print("Using sha256")
  elif hash_Lenght == 64:
    hash_type = 4
    print("Using sha384")
  elif hash_Lenght == 96:
    hash_type = 5
    print("Using sha512")
  elif hash_Lenght == 128:
    hash_type = 6
  else:
    raise IndexError("Exceeded Limit or Below Range")

  with open(word_list,"r") as WordListText:
    for line in WordListText:
      single_text = line.strip()
      hashed_text = conv(single_text, hash_type)
      if hashed_text == hashed_word:
        print(f"Hash Cracked \n#### Password : {single_text}")
        g = 0
      else:
        g=1
      
  
  
if 1 == 1:
    main()
    if g !=0:
      print("Can't Crack this hash")
  
  
    
