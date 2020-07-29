def calc_average(scores):
	return sum(scores) / 5

def determine_grade(score):
	if 90 <= score <= 100:
		result = "A"
	elif 80 <= score <= 89:
		result = "B"
	elif 70 <= score <= 79:
		result = "C"
	elif 60 <= score <= 69:
		result = "D"
	else:
		result = "F"

	return result
scores = []

for _ in range(5):
	score = int(input("Please enter five test scores: "))
	print("Letter Grade is:", determine_grade(score))	
	scores.append(score)
avg = calc_average(scores)
print("Average test scores:", avg, "Letter Grade is:", determine_grade(avg))

