import sys
from stats import get_nums_words, get_characters_count, sort_characters_count

def get_book_text(filepath):
  with open(filepath) as f:
    contents = f.read()
  return contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_path = sys.argv[1]
  contents = get_book_text(book_path)
  num_words = get_nums_words(contents)
  char_dict = get_characters_count(contents)
  sorted_list = sort_characters_count(char_dict)
  print_report(book_path, num_words, sorted_list)
  
def print_report(book_path, num_words, chars_sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in chars_sorted_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")
  print("============= END ===============")
main()