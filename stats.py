def get_nums_words(contents):
  word_count = len(contents.split())
  return word_count
def get_characters_count(contents):
  char_dict = {}
  lower_case = contents.lower()
  for char in lower_case:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

def sort_on(items):
  return items["num"]

def sort_characters_count(char_dict):
  #first we go through the original list and update the keys
  list = []
  for k in char_dict:
    new_dict = {}
    new_dict["char"] = k
    new_dict["num"] = char_dict[k]
    list.append(new_dict)
  list.sort(reverse=True, key=sort_on)
  return list
