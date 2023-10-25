print("How many Days,  left if you live until 90 year old")
print("---------------------------------------------------------------")
cur_age=input("How old are you? ")
year_more=0
if cur_age.isdigit():
    print("your current age is ",cur_age)
    year_more=90-int(cur_age)
    
    days_more=365*year_more
    
    
    
else:
    print("Entered value is not number")