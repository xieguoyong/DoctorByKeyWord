# import json
#
# str_list = "[11.23,23.34,' ' ]"
# list_list = json.loads(str_list)
# print(type(list_list))
# print

import ast

str_list = "['',739591]"
list_list = ast.literal_eval(str_list)
print(type(list_list))
print(list_list)