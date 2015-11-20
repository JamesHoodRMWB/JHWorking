import re
regex = re.compile('th.s')
l = ['this', 'is', 'just', 'a', 'test']
matches = [string for string in l if re.match(regex, string)]

#print matches




li = ["#Date: 2015-03-24 14:01:34", "#Fields:",
      "date time s-ip cs-method cs-uri-stem cs-uri-querys-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken"]


import re
regex = re.compile('#.')
l = ['this', 'is', 'just', 'a', 'test']
matches2 = [string for string in li if re.match(regex, string)]

#print matches2

##############


#slist = ["walking in a winter wonderland", "more of the same", "#keep it coming", "#hashtage whatever", "not me", "date time", "end"]
#for s in slist:
#    print s
#    s.find(#)


str1 = "#this is string example....wow!!!";
str2 = "#";

print str1.find(str2)
print str1.find(str2)
print str1.find(str2)



