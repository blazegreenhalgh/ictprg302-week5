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
sharks = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa"]

def change_shark(chorus_number):
    return sharks[chorus_number]

def shark_lines(shark):
    return f"{shark} Shark, doo-doo, doo-doo, doo-doo"

for repeat in chorus:
    shark = change_shark(repeat)
    for line in lines:
        print(shark_lines(shark)) if line < 3 else print(f"{shark} Shark")

