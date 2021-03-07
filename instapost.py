import datetime,time
from instapy_cli import client

n = datetime.datetime.today()
posts = []
caps = []
k = []
filex = 'instagram files'
import os
while True:
 for filename in os.listdir(filex):
    try:
     datetime.datetime.strptime(filename[:10], '%Y-%n-%d')
     with open("posts.txt") as pp:

        e = pp.readlines()
        for u in e:
          if u[:-1].split("",1)[0] not in k:
            k.append(u[:-1].split("",1)[0])


        if filename not in k:
         cap = input("caption for this post: ")
         with open("posts.txt", 'a') as fp:
          fp.writelines(filename)
          fp.writelines(" ")        
          fp.writelines(cap)        
          fp.writelines("\n")


    except:
      pass
                  
    with open("posts.txt") as pf:
     a  = pf.readlines()     
     for g in a:
      post,cap=g[:-1].split(" ",1)
      if post[:10] == str(n.date()):
        with client(username = username, password = password) as cl:
           cl.upload(post,caption = cap)