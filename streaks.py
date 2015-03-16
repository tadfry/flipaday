# streaks.py by Tad Fry @tadfry
# Reads flips.csv to count the streaks of Heads and Tails.
# Download the current flips.csv file and put in the same location as streaks.py: http://tadfry.com/flipaday/flips.csv

# Import the CSV module:
import csv

# We need to track the previous flip while we iterate over the flip results.
# A Heads or Tails result will be stored here, but set it to None for now:
previous_flip = None

# We need a counter to track the current streak:
counter = 1

# We will store the streaks for Heads and Tails in their own lists:
heads_streaks = []
tails_streaks = []

# Open flips.csv:
with open('flips.csv', 'rb') as file:
	# Set the reader object:
	reader = csv.reader(file)

	# Read each row of flips.csv to figure out the streaks:
	for row in reader:
		# The flip is the second column of the row: row[1]
		# Store it in flip for readability:
		flip = row[1]

		# If flip is the same as previous_flip, then increment the counter:
		if flip == previous_flip:
			counter += 1
		# If flip is not the same as previous_flip,
		# then we need to see if a streak occurred.
		else:
			# If counter is greater than 1, then a streak occurred:
			if counter > 1:
				# If previous_flip is Heads, then a Heads streak has ended.
				# We save the streak counter in the heads_streaks list:
				if previous_flip == 'Heads':
					heads_streaks.append(counter)
				# If previous_flip is Tails, then a Tails streak has ended.
				# We save the streak counter in the tails_streaks list:
				if previous_flip == 'Tails':
					tails_streaks.append(counter)

			# Since the flip is not the same as the previous_flip, we need to set the counter to 1:
			counter = 1

		# Store the flip in previous_flip so we can compare it to the flip in the next row:
		previous_flip = flip

# Sort the streaks in ascending order:
# Not needed, but nice if you want to print them out.
heads_streaks.sort()
tails_streaks.sort()

# Make dictionaries to store the streaks and how many times they occurred:
# The keys will be the streak count, and the values will be the number of times the streak occurred.
heads_streaks_totals = {}
tails_streaks_totals = {}

# For each streak in heads_streaks:
for streak in heads_streaks:
	# If the streak is in heads_streaks_totals, then increment the number of times it occurred:
	if streak in heads_streaks_totals:
		heads_streaks_totals[streak] += 1
	# If the streak is not in heads_streaks_totals, then begin tracking it by setting it to 1:
	else:
		heads_streaks_totals[streak] = 1

# For each streak in tails_streaks:
for streak in tails_streaks:
	# If the streak is in tails_streaks_totals, then increment the number of times it occurred:
	if streak in tails_streaks_totals:
		tails_streaks_totals[streak] += 1
	# If the streak is not in tails_streaks_totals, then begin tracking it by setting it to 1:
	else:
		tails_streaks_totals[streak] = 1

# Print the streaks!
print 'Heads Streaks:'

# For each heads_streaks_totals, print the streak count (key) with the number of times it occurred (value):
for key, value in heads_streaks_totals.iteritems():
	print '{0}-flip {1} time{2}'.format(key, value, 's' if value > 1 else '')

# Print the total streaks that occurred for Heads:
print 'Total Heads Streaks: {0}'.format(len(heads_streaks))

print ''

print 'Tails Streaks:'

# For each tails_streaks_totals, print the streak count (key) with the number of times it occurred (value):
for key, value in tails_streaks_totals.iteritems():
	print '{0}-flip {1} time{2}'.format(key, value, 's' if value > 1 else '')

# Print the total streaks that occurred for Tails:
print 'Total Tails Streaks: {0}'.format(len(tails_streaks))