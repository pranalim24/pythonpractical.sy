#**************************************************
# CUSTOMER FEEDBACK FORMATTER
#**************************************************

raw_name=input("Enter Customer Name:")
raw_feedback=input("Enter feedback message:")
rating=input("Enter rating(1 to 5):")

clean_name=raw_name.strip()               #remove unwanted space from start and end
clean_feedback= raw_feedback.strip()

formatted_name= clean_name.title()          #capitalizes the first letter of each word

formatted_feedback= clean_feedback.capitalize()      #makes only the very first letter of the message in uppercase

formatted_feedback= formatted_feedback.replace("u","you").replace("r","are")           #replace specific words or character(abbreviation)

exclamation_count= formatted_feedback.count("!")    #count occurrence of specific character
while True:  
 if (rating >=1 and rating <=5):
    if int(rating)>=4:
     category="POSITIVE".upper()

    else:
     category="NEEDS REVIEW".upper()

 else:
    rating= int(input("Invalid rating provided. Enter rating (1 to 5):"))


print("\n" + "+"*45)
#^45 centers the text within a 45 character wide block
print(f"{"PROFESSIONAL FEEDBACK REPORT":^45}")
print("="*45)

#f-string variable interpolation
print(f"Customer Name:   {raw_name}")
print(f"Rating:      {rating}/ 5 stars")
print(f"Category:    [{category}]")
print(f"ExcitmentL:    {exclamation_count} exclamation mark(s)")
print("."*45)
print("Formatted Message:\t")
print(f'"{formatted_feedback}"')
print("-" * 45)