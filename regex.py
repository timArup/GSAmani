import re
import test 

es = "113 to 123 135 to 145 147 to 157 159 to 169 171 to 181 183 to 193 195 to 205 207 to 217 219 to 229 231 to 241 243 to 253 255 to 265 270 to 281"

def convert_to_2_list(to_string):

    to_list = to_string.split()

    updated = to_list.copy()
    updated_index = 0
    offset = 0
    for i,value in enumerate(to_list):
        updated_index = i + offset
        if value == 'to':
            del updated[updated_index]
            list_to_insert = list(range(int(to_list[i-1])+1,int(to_list[i+1])))
            list_to_insert.reverse()
            offset = offset + len(list_to_insert) - 1
            for inserted in list_to_insert:
                updated.insert(updated_index,inserted)
    
    updated = [int(item) for item in updated]
    return updated

updated = convert_to_2_list(es)

print(updated)

        

