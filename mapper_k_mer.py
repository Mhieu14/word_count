
# import sys because we need to read and write data to STDIN and STDOUT
import sys

_K = 9
# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	length = len(line)
	count = 0
	while count + _K < length:
		print('%s\t%s'%(line[count : count + _K], 1))
		count = count + 1
