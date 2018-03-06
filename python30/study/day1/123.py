name = input("name:").strip()
age = int(input("age:"))
job = input("job:")
# print("Information of []:"+ name +"\nName:[]"+ name +"\nAge:[]"+ age +"\nJob:[]"+ job)
# print("Information of %s:\nName:%a\nAge:%d\nJob:%s" %(name,name,age,job))
msg = '''Information of %a:
    Name:%s
    Age:%d
    Job:%s
''' %(name,name,age,job)
print(msg)