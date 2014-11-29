# coding:utf-8

import string

# str1="""
#       dia 周末
#       eee
# 
# ghr \""""


# print str1
# 
# def sumAdd(x,y):
#     return x+y
# print sum.__doc__

class Foo(object):
    """演示"""
    pass

print  r"\nwinxt\rdd"

str1 = "hello world"
str2 = u"hello python"

print str1
print str2.encode("utf-8")

print "-------------cut------------------"

str3 = "hellopython"
print str3[2:5:2]
print str3[2:9:3]
print str3[2:]
print str3[2:9]
print "-----------------"
print str3[-4:-1]
print str3[-4:]

str4 = "hello"
str5 = "python"
print str4 + str5

print str4 * 4

print "--------------in------------------"
str5 = "  fhdisajfida  fdjsiahd   "
print "d" in str5

print "-----------split---------------"
stringList = str5.split()
print stringList

print "*".join(stringList)
print len(str5)
print len(str5.strip())
print "-----------------l---------------"
print str5.lstrip()
print str5.rstrip()
print "-----------------s---------------"

print "--------------find--------------------"
print str5.find("hd")

print "--------------find double------------------"
str6="abcdeabcd"
print str6.find("abc")

print"----------"
help(string)

print '%d %3.2f %s' % (1, 2.3, ['one', 'two', 'three'])
print "%6.2f" % 6719909032.789002

print "%(name)s:%(score)6.1f" % {'score':9.5, 'name':'newSin'}

unicodeString = u"hello unicode"
print unicodeString


print "--------------ord-----------------"
print ord("a")
print ord("z")
print ord("A")
print ord("Z")
print ord("X")
print ord("K")


print '杭州先临三维科技股份有限公司'.endswith('有限公司')