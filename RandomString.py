from itertools import groupby    

class InvalidCountException(Exception):
	"""
	Custom Exception that raises exception in the case as follows
	a_count = 10
	b_count = 2

	Sequence might appear with more than three consequetive characters
	"""
	def __init__(self, message):
		super().__init__(message)

def sequence_generator(a_count,b_count):
	"""
	generates the sequence as per the count specified

	@param expr : count of 'a' and 'b'
	@type expr : integer 

	returns : sequence of characters
	@type : string

	@raises : L{InvalidCountException}
	"""
	resultant_string = []

	if(a_count == b_count):
		"""
		Will generate the sequence if count of 'a' and 'b ' are equal
		"""
		while(a_count > 0 or b_count >0):
			resultant_string.append('a')
			resultant_string.append('b')
			a_count = a_count - 1
			b_count = b_count - 1

	else:
		"""
		max_var = contains the variable(a_count/b_count) who has maximum count
		min_var = contains the variable(a_count/b_count) who has minimum count
		"""
		max_var = max(a_count,b_count) 
		min_var = min(a_count,b_count)
		
		c = 'a' if (max_var == a_count) else 'b'  # 'c' contains that character ('a'/'b') which has maximum count
		d = 'a' if (min_var == a_count) else 'b'  # 'd' contains that character ('a'/'b') which has minimum count

		while(max_var>0 or min_var>0):
			if(max_var < 2):
				if (max_var > 0): 
					resultant_string.append(c)
				max_var = max_var - 1
			else:
				for i in range(2):
					if (max_var > 0):
						resultant_string.append(c)
					max_var = max_var - 1
				if (min_var > 0):
					resultant_string.append(d)
				min_var = min_var - 1

	possibility = count_check(resultant_string) # resultant string passed to check for more than 3 consequetive characters
	if(possibility):
		return(''.join(resultant_string))   #coverting list elements into string
	else:
		raise InvalidCountException("The squence can't be generated. Please give the correct count") #if possibility if false exception raised

def count_check(res_str):
	"""
	checks if sequence contains more than three consecutive characters, and helps in raising exception
	for example 
	a_count = 8
	b_count = 2
	sequence generated  - 'aabaabaaaa' 

	@param expr : resultant sequence 
	@type expr : string 

	returns : true/false based on the count. true -if count doesnt exceeds 3 , otherwise false
	@type : boolean
	"""
	count_list = [[k, len(list(g))] for k, g in groupby(res_str)] #generates list of consecutive characters along with its count
	for i in range(len(count_list)):
		flag = True
		if (count_list[i][1] > 3):   
			flag = False
			break
	return flag

def main():
	"""
	Asking for input counts and returning the sequence
	"""
	a_count = int(input("enter count for a "))
	b_count = int(input("enter count for b "))

	resultant_sequence = sequence_generator(a_count,b_count)

	print(resultant_sequence)


if __name__ == '__main__':
	main()

