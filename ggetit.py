#!/Users/ptw/anaconda3/bin/python
import os
import time
for id in range(100000000):
	syscmd = '/usr/local/bin/wget https://www.opensecrets.org/orgs/totals.php\?id\=D{:09d} -w1'.format(id)
	print(syscmd)
	os.system(syscmd)
	time.sleep(0.25)
