def merge_the_tools(string, k):
    splitted_k_string=[]
    for i in range(0,len(string),k):
        sub_string=string[i:i+k]
        unique_sub_string=[]
        for sub_string_item in sub_string:
            if( not(sub_string_item in unique_sub_string)):
                unique_sub_string.append(sub_string_item)
        splitted_k_string.append(unique_sub_string)
    for letters in splitted_k_string:
        print(''.join(letters))



string, k = input(), int(input())
merge_the_tools(string, k)