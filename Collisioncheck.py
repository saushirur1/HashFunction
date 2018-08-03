class collision:
  def collision_check(self):
    list1=[]
    check={}
    flag=0
    f = open("hashfile.txt","r+")
    lines=f.readlines()
    for line in lines:
        print(line)
        line3=[]
        line3=line.strip().split("=")
        list1.append(line3[1])
    print(list1)
    for x in range(0,len(list1)):
        if(check.has_key(list1[x])):
            flag=1
            print("Collision")
        else:
           check[list1[x]]=1
    if(flag==0):
       print("No collision")
def main():
   x=collision()
   x.collision_check()
if __name__=='__main__':main()
