import sys
from stats import word_count, count_characters, sort_on, nested_dictionary

def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

   num_words = word_count()
   num_chars = count_characters()
   sorted_dicts = nested_dictionary(num_chars)

   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print(f'Found {num_words} total words')
   print("--------- Character Count -------")
   for dictionary in sorted_dicts:
      if dictionary["char"].isalpha() == True: 
         print(f'{dictionary["char"]}: {dictionary["num"]}')
   print("============= END ===============")

main()







