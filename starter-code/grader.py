# add your logic here by implementing the requirements
# described in the lab sheet.
# replace pass with your implementation.
def doGrading(answers, responses,studentID):
	# add your implementation here to iterate through
	# answers and responses array to compute the grading details. 
	pass
	
# test the implementation of the above defined method. 
answers = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
responses = [['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
studentID = int(input("Enter a student ID:"))
if (studentID < 0 or studentID > len(responses)-1):
	print(f"Please provide a student id number between 0 and {len(responses)-1}")
else:
	doGrading(answers,responses,studentID)