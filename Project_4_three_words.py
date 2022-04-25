first_word = str(input("Enter the first word: "))
second_word = str(input("Enter the second word: "))
third_word = str(input("Enter third word: "))

print("Lower case: " +
      first_word.lower() + ", " +
      second_word.lower() + ", " +
      third_word.lower())
print("Uppercase:  " +
      first_word.upper() + ", " +
      second_word.upper() + ", " +
      third_word.upper())
print("Only the first letter in Uppercase: " +
      first_word.capitalize() + ", " +
      second_word.capitalize() + ", " +
      third_word.capitalize())

first_word_count = input(str('{} need to be bought (pieces): '.format(first_word.capitalize())))
second_word_count = input(str('{} need to be bought (pieces): '.format(second_word.capitalize())))
third_word_count = input(str('{} need to be bought (pieces): '.format(third_word.capitalize())))

text = ('First you need to buy {5} pieces of {4}, '
        'then about {1} pieces of {0}. '
        'Finally, you can buy {3} {2}'.
        format(third_word.lower(), third_word_count,
               second_word.lower(), second_word_count,
               first_word_count, first_word.lower()))
print(text)
