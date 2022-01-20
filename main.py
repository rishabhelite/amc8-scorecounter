ans = list(input("Copy and paste official answers: "))

# Get year.
while True:
    while True:
        try:
            yr = int(input("What year is this from? [>1985]: "))
            break
        except ValueError:
            print("NaN\n")

    if 1985 <= yr <= 2050:
        break
    print("Not a valid year.\n")

chs = ["", "A", "B", "C", "D", "E"]

# A = 1, B = 2, C = 3, D = 4, E = 5
# "1453232323311443153122144"


while True:

    # First get correct inputs.
    while True:
        try:
            mine = int(input("Enter answers [1-5 for A-E]\n--> "))
            mne2 = int(input("Enter answers again [1-5 for A-E]\n--> "))
            break

        except ValueError:
            print("NaN; try again.")

    # Then check if both are the same.
    if mine == mne2:
        mine, mne2 = list(str(mine)), list(str(mne2))
        break
    # Error message; if they are not identical.
    print("Sorry, your two inputs are not identical; try again.\n")


# Convert from 1-5 to A-E.
for n in range(25):
    mine[n] = chs[int(mine[n])]

score = 0
place = " "
for n in range(25):

    # Print out Question Number (example: `17) `)
    if n >= 9:
        print(f"{n + 1})", end=" ")
        place = ""
    else:
        print(f" {n + 1})", end=" ")

    # Print out checked answer.
    if mine[n] == ans[n]:
        score += 1
        print(f"|--| ✓ |--|   {mine[n]}    |-", end="")

    else:
        print(f"|--| X |--| {mine[n]} -> {ans[n]} |-", end="")

    print(f"-| https://aops.com/wiki/index.php/{yr}_AMC_8_Problems/Problem_{n + 1} {place}|-----")


print(f"\nYou got {score}/25 which is {score * 4}%.")
