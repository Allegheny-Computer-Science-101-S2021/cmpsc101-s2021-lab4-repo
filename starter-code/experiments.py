import array, time, sys, random, numpy as np
# this method is used to generate a built in python array
def generateArray(cap):
	start_time = time.time()	
	arr = array.array('i',[])
	for num in range(0,cap):
		arr.append(num)
	end_time = time.time()
	print("array generate took this long to run: {}".format(round((end_time-start_time),5)))
	print("size of array:", sys.getsizeof(arr))
	return arr
# this method is used to generate a numpy array
def generateNPArray(cap):
	start_time = time.time()	
	np_arr = np.arange(1,cap+1)
	end_time = time.time()
	print("np array generate took this long to run: {}".format(round((end_time-start_time),5)))
	print("size of np array:", sys.getsizeof(arr))
	return np_arr
# this method is used to generate a list
def generateList(cap):
	start_time = time.time()	
	ls = []
	for num in range(0,cap):
		ls.append(num)
	end_time = time.time()
	print("list generate took this long to run: {}".format(round((end_time-start_time),5)))
	print("size of list:", sys.getsizeof(ls))
	return ls
# this method is used to process a built in array. 
# the process is simple, that is add 100 to each element in the array
def processArray(arr,cap):
	start_time = time.time()	
	for i in range(len(arr)):
		arr[i] = arr[i] + 100
	end_time = time.time()
	print("array process took this long to run: {}".format(round((end_time-start_time),5)))
# this method is used to process a np array. 
# the process is simple, that is add 100 to each element in the np array
def processNPArray(np_arr,cap):
	start_time = time.time()	
	mod_arr = np.array(np_arr)
	mod_arr = mod_arr+100
	end_time = time.time()
	print("np array process took this long to run: {}".format(round((end_time-start_time),5)))
# this method is used to process a list. 
# the process is simple, that is add 100 to each element in the list.
def processList(ls,cap):
	start_time = time.time()	
	for i in range(0,cap):
		ls[i] = ls[i]+100
	end_time = time.time()
	print("list process took this long to run: {}".format(round((end_time-start_time),5)))
# this method is used to remove elements from a built in python array (random)	
def removeArray(arr):
	start_time = time.time()	
	while(len(arr) != 0):
		rand = random.randint(0, len(arr)-1)
		arr.pop(rand)
	end_time = time.time()
	print("removing elements from an array took this long to run: {}".format(round((end_time-start_time),5)))

# this method is used to remove elements from a numpy array (random)

def removeNPArray(np_arr):
	start_time = time.time()	
	rm = random.sample(range(0, len(np_arr)), len(np_arr))
	np_arr = np.delete(np_arr,rm)
	end_time = time.time()
	print("removing elements from an np array took this long to run: {}".format(round((end_time-start_time),5)))
	
# this method is used to remove elements from a list (random)
def removeList(ls):
	start_time = time.time()	
	while(len(ls) != 0):
		rand = random.randint(0, len(ls)-1)
		ls.pop(rand)
	end_time = time.time()
	print("removing elements from a list took this long to run: {}".format(round((end_time-start_time),5)))
	
cap = 1000000
arr = generateArray(cap)
np_arr = generateNPArray(cap)
ls = generateList(cap)
processArray(arr,cap)
processNPArray(np_arr,cap)
processList(ls,cap)
removeArray(arr)
removeNPArray(np_arr)
removeList(ls)

