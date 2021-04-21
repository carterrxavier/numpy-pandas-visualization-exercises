import pandas as pd 
import matplotlib as mlt


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#part 1

#1 determine the number of elements of fruits
fruits.size

#2 output only the index from fruits
fruits.index

#3 output only the values from fruits
fruits.values

#4 confirm the datatype of the values in fruits
fruits.dtype

#5 output only the first 5 values from fruits, output the last 3,output 2 random
fruits.head(5)
fruits.tail(3)
fruits.sample(2)


#6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()


#7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

#8 Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

# 9 Determine the string value that occurs most frequently in fruits.
fruits.value_counts().head(1)

# 10  Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n=1 , keep  = 'all')

#part 2 

#1 Capitalize all the string values in fruits.
fruits.str.capitalize()

#2 Count the letter "a" in all the string values (use string vectorization).
fruits[fruits.str.lower().str.count((r'[a]'))]


#3 Output the number of vowels in each and every string value.
print(fruits[fruits.str.lower().str.count((r'[aeiou]'))]

#4 Write the code to get the longest string value from fruits.
variable = fruits.str.len().max() == fruits.str.len()


#5 Write the code to get the string values with 5 or more letters in the name.
arg = fruits.str.len() >= 5


#6 Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
def count_os(word):
    word_lower = word.lower()
    if word_lower.count('o') >= 2:
        return True
    else:
        return False

fruits[fruits.apply(count_os)]


#7 Write the code to get only the string values containing the substring "berry".
arg = fruits.str.lower().str.contains('berry')
fruits[arg]

#8 Write the code to get only the string values containing the substring "apple".
arg = fruits.str.lower().str.contains('apple')
fruits[arg]

#9 Which string value contains the most vowels?
fruits[max(fruits.str.lower().str.count((r'[aeiou]')))]


letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))


#part 3 

#1 Which letter occurs the most frequently in the letters Series?
letters.value_counts().nlargest(n=1, keep='all')


#2 Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1, keep='all')

#3 How many vowels are in the Series?
all_vowels = letters.str.lower().str.count(r'[aeiou]')
sum(all_vowels)

#4 How many consonants are in the Series?
sum(letters.str.lower().str.count(r'[a-z]') - all_vowels)

#5 Create a Series that has all of the same letters but uppercased.
letters_up = letters.str.capitalize()

#6 in jupyter notebook 
# 
# Create a bar plot of the frequencies of the 6 most commonly occuring letters.
arg = letters.value_counts().nlargest(n=6, keep='first').plot.bar(rot=0).
print(arg)





#rest found in jupyter notebook









