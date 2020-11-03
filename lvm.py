from pyfiglet import Figlet
import os
f = Figlet(font='slant')
print (f.renderText('to create lvm'))
i=0
e=[]
remove_content = ["'", "[", "]",","]
while True:


    s=i=1+i


    
    a=input("Please insert the disk name or q to exit\n")
    print(s)
    if (a=='q'):
        break;
    else:
        e.append(a)

n=input("Enter volume name\n")

my_str = repr(e)

for content in remove_content:
    my_str = my_str.replace(content, '')


vg=("vgcreate  {1} {0}".format(my_str,n))
os.system(vg)
a=input("lv name you want to give\n")
b=input("size\n")
lv=("lvcreate --name {0} --size {1} {2}".format(a,b,n))
os.system(lv)
