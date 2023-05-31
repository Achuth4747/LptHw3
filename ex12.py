from sys import argv

script,user_name=argv
prompt='>'
print("hai%s,i am the %s" %(user_name,script))
print("do you like me?%s"%(user_name))
likes = int(input(prompt))

print("whre do you live?%s"%(user_name))
lives=int(input(prompt))

print("""
so your nme is %s,you likes me%s""" %(likes,lives))