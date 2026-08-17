"""
TEXT ANALYSER TOOL(Basic Version-No Function)
-------------------------------------------------------
Concept  Demonstrated: Strings,Indexing,Slicing,String Traversal

The User enters a paragraph , and the program analyzes it to count:
    - Total characters
    - Total words
    - Total vowels
    - Total spaces
    - Total consonants
    - Total digits
"""

print("=" * 45)
print(" TEXT ANALYSER TOOL ")
print("=" * 45)

paragraph= input("Enter a Paragraph:\n")

#------------Basic Info using len() and slicing--------------
total_length= len(paragraph)
print("\n---Basic Info---")
print("Total Characters(including spaces):" ,total_length)
print("First 10 Characters(slicing):", paragraph[0:10])
print("Last 10 Characters(slicing):" , paragraph[-10:])
print("Reversed paragraph(slicing):", paragraph[::-1])

#--------------Counter----------------
vowel_count=0
space_count=0
consonant_count=0
digit_count=0
other_count=0

vowels= "aeiouAEIOU"

#--------Traversal using indexing----------
for i in range(len(paragraph)):
    ch=paragraph[i]
    
    if ch==" ":
        space_count= space_count+1

    elif ch.isalpha():
        if ch in vowels:
            vowel_count= vowel_count +1

        else:
            consonant_count = consonant_count +1

    elif ch.isdigit():
        digit_count= digit_count+1

    else:
        other_count= other_count+1         #punctuation,symbols,etc.


        #---------Word Count----------

words=paragraph.split()        # split paragraph into a list of words
word_count= len(words) 

    #--------Display Results-----------

print("\n------Character Analysis------")   
print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)
print("Total Spaces:",space_count)
print("Total Digits:", digit_count) 
print("Total Characters:", other_count, "(punctuation/symbol)")

print("\n------Word Analysis------")
print("Total Words:", word_count)
print("First word:", words[0])
print("Last Word:", words[-1])

print("\n------Word List(Traversal)-----")
for i in range(len(words)):
    print(f"Word{i+1}: {words[i]}")

print()    

