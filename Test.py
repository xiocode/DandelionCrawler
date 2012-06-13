'''
Created on 2012-6-4

@author: windows
'''
import time

startTime = time.time()
result = 0
for i in xrange(1000000):
    result = i + i - i * i / (i + 1);
endTime = time.time()
print result
print (endTime - startTime)