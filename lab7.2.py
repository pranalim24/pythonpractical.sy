paragraph=input("Enter Your Paragraph:")

words=paragraph.upper().split()
count =0

for word in words:
    if word== "python":
        count += 1

print("The Word 'python' appears",count, "times.")        