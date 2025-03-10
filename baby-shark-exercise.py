"""Baby Shark!
Examine the lyrics of the famous song “Baby Shark” if you haven’t heard it - you REALLY need to.
	1.	Identify patterns and repetitions (if there are any)
	2.	Use loops and functions to minimize the number of such repetitions

chorus repeat 5 times.
melody repeats 3 times, then one final 'x shark'

baby, mommy, daddy, grandma, grandpa
"""

chorus = range(5)
lines = range(4)

for repeat in chorus:
    def change_shark(repeat):
        if repeat == 0:
            return "Baby"
        if repeat == 1:
            return "Mommy"
        if repeat == 2:
            return "Daddy"
        if repeat == 3:
            return "Grandma"
        if repeat == 4:
            return "Grandpa"

    def shark_lines(shark):
        return f"{shark} Shark, doo-doo, doo-doo, doo-doo"

    shark = change_shark(repeat)
    for line in lines:
        print(shark_lines(shark)) if line < 3 else print(f"{shark} Shark")
