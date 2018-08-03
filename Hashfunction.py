import os
class hashmap:
  def hash(self):
    listoffiles=[]
    f1=open("hashfile.txt","w+")
    for dirpath, dirs, files in os.walk("."):
        for file in files:
    	   listoffiles.append(dirpath+"/" +file)
    print(listoffiles)
    for i in range(0,len(listoffiles)):
     f=open(listoffiles[i],'rb')
     list=[0]*32
     result=[]
     while True:
       list2=[]
       buf=f.read(1)
       if buf:
          for x in range(0,4):
             x1=list[0]
             list.remove(list[0])
             list.insert(31,x1)
          c=buf
          x = ord(buf)
          t = bin(x)
          t1=str(t)
          for u in range(2,len(t1)):
             list2.append(int(t1[u]))
          while(len(list2)<8):
             list2.insert(0,0)
          for v in range(0,8):
              list[v+23]=list[v+23]^list2[v]
       else:
          for v1 in range(0,len(list)):
              list[v1]=str(list[v1])
          hash=''.join(list)
          f1.write(listoffiles[i]+"="+hash + '\n')
          break
def main():
   x=hashmap()
   x.hash()
if __name__=='__main__':main()
