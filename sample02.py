raw_record = '                Apple,Banana,Melon,Grape     '
clean_record = raw_record.strip()
updated_record = clean_record.replace('Melon', 'Orange')
fruit_list = clean_record.split(',')
final_record = '->'.join(fruit_list)
slen = len(final_record)

print(clean_record)
print(updated_record)
print(fruit_list)
print(final_record)

print(slen)

