# coding:utf-8
p = True
q = False

title = "p          q        p and q   p or q"
  
length = len(title)
 
print title
print length * "-"
  
for p in [True, False]:
    for q in [True , False]:
        print "%-9s %-9s %-9s %-9s" % (p, q, (p and q), (p or q))
     
