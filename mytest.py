# import json
#
# str_list = "[11.23,23.34,' ' ]"
# list_list = json.loads(str_list)
# print(type(list_list))
# print

import ast

str_list = "[15221739591,739591,'15:00','15:30']"
list_list = ast.literal_eval(str_list)
print(type(list_list))
print(list_list)