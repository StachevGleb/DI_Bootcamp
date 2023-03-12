# import datetime
# today_date = datetime.date.today()
# actual_datetime = datetime.datetime.now()
# my_birth = actual_datetime + datetime.timedelta(days=45, hours=10, minutes=29, milliseconds=46)
# print(my_birth)
#
# import os
# print(os.getcwd())
# os.makedirs(week, 5)

# import itertools
#
# my_list = [0, 0, 1, 2, 0]
#
# result = itertools.dropwhile(lambda x: x == 0, my_list)
#
# for elements in result:
#   print (elements)

import re

string = "at what time?"
match = re.sub("\s","!!!",string)
print (match)