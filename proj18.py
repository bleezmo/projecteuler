triangle_input = "75\
:95 64\
:17 47 82\
:18 35 87 10\
:20 04 82 47 65\
:19 01 23 75 03 34\
:88 02 77 73 07 63 67\
:99 65 04 28 06 16 70 92\
:41 41 26 56 83 40 80 70 33\
:41 48 72 33 47 32 37 16 94 29\
:53 71 44 65 25 43 91 52 97 51 14\
:70 11 33 28 77 73 17 78 39 68 17 57\
:91 71 52 38 17 14 91 43 58 50 27 29 48\
:63 66 04 68 89 53 67 30 73 16 69 87 40 31\
:04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

class TrianglePos:
	def __init__(self,row_index,offset,value):
		self.row = row_index
		self.offset = offset
		self.value = value
class TriangleRow:
	def __init__(self,row,row_index):
		self.row = []
		count = 0
		while count < len(row):
			self.row = self.row + [TrianglePos(row_index,count,int(row[count]))]
			count+=1
	def getValue(self,offset):
		return self.row[offset].value
class Triangle:
	def __init__(self,triangle):
		rows = triangle.split(":")
		self.rows = []
		count = 0
		while count < len(rows):
			self.rows = self.rows + [TriangleRow(rows[count].split(" "),count)]
			count+=1
def getSummedParents(sums,node):
	summed = []
	for sumnode in sums:
		if(sumnode.row == (node.row-1)):
			if(sumnode.offset == node.offset or sumnode.offset == (node.offset-1)):
				summed = summed + [sumnode]
	return summed


def main():
	triangle = Triangle(triangle_input)
	sums = []
	rowcounter = 0
	for rowobj in triangle.rows:
		for node in rowobj.row:
			summed = getSummedParents(sums,node)
			if(len(summed) == 0):
				sums = sums + [node]
			else:
				result = 0
				for sumnode in summed:
					sums = sums + [TrianglePos(node.row,node.offset,sumnode.value+node.value)]
		sums = list(filter(lambda x: x.row > (rowcounter-1),sums))
		rowcounter+=1
	largest = sums[0]
	for sumnode in sums:
		if(largest.value < sumnode.value):
			largest = sumnode
	print("max is:",largest.value)
main()