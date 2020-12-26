import csv, json

class LeetCode:
	def __init__(self):
		self.projectSource = "/home/kaushik/Desktop/Code/03_Git_Projects/Organizing_Leetcode/"

	def createProbSet(self, path):
		# Convert the csv file to JSON. 
		# This JSON file will be used as a reference when the topics will be loaded to create a new JSON. 
		with open(path) as page:
			read = csv.reader(page, delimiter=',')
			data = {}
			for row in read:
				rank = row[0]
				key  = row[1]
				name = row[2]
				name = name.replace("    ", "")

				diff = row[4]
				data[key] = [rank, name, diff]

			with open(self.projectSource + 'problemSet.json','w') as json_out:
				json.dump(data, json_out, indent=4)
			json_out.close()
		page.close()

	def createTopicSet(self, path):
		# Parse the CSV file for string that have topics.
		# After passing these strings to buildTopics functions, create a new dictionary to store the question 
		# by its rank and company in new JSON format. 
		with open(path) as page:
			read = csv.reader(page, delimiter=',')
			data = {}
			for row in read:
				rank = row[0]
				key  = row[1]
				topics = self.buildTopics(row[3])

				if key in data:
					data[key][1].append(rank)
				else:
					data[key] = [topics,[rank]]

			with open(self.projectSource + 'topicSet.json','w') as json_out:
				json.dump(data, json_out, indent=4)
			json_out.close()
		page.close()


	def buildTopics(self, string):
		# Iterate through the string and check if sub-string exists in topics set. 
		# If sub-string is a topic in set, append to output array. 
		# Return output array once entire string is iterted. 
		topics = ('Array','Hash Table','Linked List','Math','Two Pointers','String','Binary Search','Divide and Conquer','Dynamic Programming','Backtracking','Stack','Heap','Greedy','Sort','Bit Manipulation','Tree','Depth-First Search','Breadth-Frist Search','Union Find', 'Graph','Design','Topological Sort','Trie','Binary Indexed Tree','Recursion','Brainteaser','Memoization','Queue','Minimax','Reservoir Sampling','Ordered Map','Geometry','Random','Rejection Sampling','Sliding Window','Line Sweep','Rolling Hash','Suffix Array','Dequeue','OOP')
		output = []
		i = j = 0
		while j <= len(string):
			if string[i:j+1] in topics:
				output.append(string[i:j+1])
				i = j + 1
			j += 1
		return output

	def output(self):
		# Load the two json files. 
		# Iterate through the problem set and create a new CSV file will all the topics listed for each problem.
		with open(self.projectSource + 'problemSet.json') as f_1:
			problemSet = json.load(f_1)
		f_1.close()
		with open(self.projectSource + 'topicSet.json') as f_2:
			topicSet = json.load(f_2)
		f_2.close()

		with open(self.projectSource + 'FinalProblemSet.csv','w') as final:
			fileWriter = csv.writer(final, delimiter=',')

			for key in problemSet:
				rank, name, diff = problemSet[key]
				topicString = ""
				companyString = ""

				# Get topic information.
				if key in topicSet:
					temp = topicSet[key]
					for topic in temp[0]:
						topicString += topic + ", "
					for company in temp[1]:
						companyString += company + ", "

				fileWriter.writerow([rank, key, name, topicString, companyString, diff])
			final.close()




x = LeetCode()
# x.createProbSet("/home/kaushik/Desktop/Code/03_Git_Projects/Organizing_Leetcode/Problems.csv")
# x.createTopicSet("/home/kaushik/Desktop/Code/03_Git_Projects/Organizing_Leetcode/Topics.csv")
x.output()