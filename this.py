import os
name="x";
#past="y"
#future="z"
#path=raw_input("enter path")
path="/usr/share/backgrounds/"
tree=os.listdir(path)
#print (tree)
n=len(tree)
print (n)
dur="\n<static>\n<duration>17.0</duration>\n<file>"
#add="/media/sumant/C4D863BED863AD7C/Pictures/car/car_wallpaper_pack/Wallpaper_Cars"
fxml=open("this.xml","w+")
filetag="<background>\n<starttime>\n<year>2009</year>\n<month>08</month>\n<day>04</day>\n<hour>00</hour>\n<minute>00</minute>\n<second>00</second>\n</starttime>"
fxml.close();
fxml=open("this.xml","a+")
fxml.write(filetag);


for i in range(0,10):
		name=tree[i]
		future=tree[i+1]
		#print(name,future)
		print(len(name))
		if(len(name)):
			print ("you entered :" ,name)
			fxml.write(dur);
			fxml.write(path+name)
			fxml.write("</file>\n</static>\n<transition>\n<duration>5.0</duration>\n<from>")
			fxml.write(path+name+"</from>\n<to>")
			fxml.write(path+future+"</to>\n</transition>")
			i=i-1;

count = 0
for count in range(0,len(tree)):
    fxml.write(tree[count])
print ("Good bye!")
fxml.close();
