#  String Assignment

"""
String Assignment.
(This can be tricky so feel free to watch solution so we can do it together)
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days.
"""
days_until_birthday = int(input("How many days until your birthday?"))

weeks_until = days_until_birthday // 7
rem_days =  days_until_birthday % 7
print(f"There are approximately {weeks_until} weeks and {rem_days} days until your birthday.")