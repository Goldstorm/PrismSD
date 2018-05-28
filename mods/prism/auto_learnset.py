## script to create learnsets for all pokemon ##
import re
import os.path

with open("pokemon_names.asm", 'rt') as myFile:
	pokemon_names_file = myFile.read()

# using REGEX to create list of pokemon names
pokemon_names_list = re.findall(r'\b[A-Z][A-Za-z0-9-]*\b',pokemon_names_file)
#for pokemon in pokemon_names_list:
#	print(pokemon)

# using REGEX to create list of lists of tmhm moves
with open("tmhmlearnsets.asm", 'rt') as myFile:
	tmhm_list = myFile.readlines() # creates list of tmhm moves for each line

"""
# remove tmhm from each line, and split the lines at each move
for tmhm_line in tmhm_file: 
	tmhm_line = tmhm_line.replace("tmhm", "")
	tmhm_line = re.findall(r'\w+', tmhm_line)
"""
for i in range(len(tmhm_list)):
	tmhm_list[i] = tmhm_list[i].replace("tmhm", "")
	tmhm_list[i] = re.findall(r'\w+', tmhm_list[i])


### trickier, create a list of egg moves for all pokenames and extract
### from egg_moves.asm if we have a name match

with open("egg_moves.asm", 'rt') as myFile:
	egg_moves_file = myFile.read()
	egg_moves_lines = myFile.readlines()

egg_move_list = [[] for i in range(len(pokemon_names_list))]

for i in range(len(pokemon_names_list)): 
	appendFlag = 0
	if re.search(pokemon_names_list[i], egg_moves_file):
		# found a match, add the moves!
		with open("egg_moves.asm", 'rt') as myFile:
			for line in myFile:
				if pokemon_names_list[i] in line:
					appendFlag = 1
				else:
					if appendFlag:
						if "$ff" in line: # not sure what $ff is in egg_moves.asm... placeholder? hex? spaghetti?
							break
						if "db" in line:
							egg_move = re.search(r'\w[A-Z_]+', line)
							if egg_move:
								egg_move_list[i].append(egg_move.group(0))
						else:
							break

#for i in range(len(pokemon_names_list)):
#	print(egg_move_list[i])


moveset_list = [[] for i in range(len(pokemon_names_list))]
# for loop for number of pokenames to read off movesets
for i in range(len(pokemon_names_list)):
	appendFlag = 0
	poke_moveset_file = "movesets/" + pokemon_names_list[i] + ".asm"
	if os.path.isfile(poke_moveset_file):
		with open(poke_moveset_file, 'rt') as myFile:
			for line in myFile:
				if re.search(r'\s0', line):
					appendFlag = appendFlag + 1
					if(appendFlag == 2):
						break
					else:
						continue
				else:
					if appendFlag:
						moveset = re.search(r'\w[A-Z_]+', line)
						if moveset:
							moveset_list[i].append(moveset.group(0))


# now we have everything we need for each pokemon: name, learnable tmhm, egg moves, and movesets via level up
# time to compile it all together!

"""
print(len(pokemon_names_list))
print(len(tmhm_list))
print(len(egg_move_list))
print(len(moveset_list))

"""

# format our lists to bring to lowercase and remove dashes/underscores

"""
f = open("learnsets.js", 'w+')
f.write("\'use strict\';\n")
f.write("exports.BattleLearnsets = {\n")
for i in range(len(pokemon_names_list)):
	pokemon_names_list[i] = re.sub(r'[-_]', '', pokemon_names_list[i])
	f.write("\t" + pokemon_names_list[i].lower() + ": {learnset: {\n")
	for line in tmhm_list[i]:
		line = re.sub(r'[-_]', '', line)
		line = line.lower()
		f.write("\t\t" + line + ": [\"4M\"],\n")
	for line in egg_move_list[i]:
		line = re.sub(r'[-_]', '', line)
		line = line.lower()
		f.write("\t\t" + line + ": [\"4M\"],\n")
	for line in moveset_list[i]:
		line = re.sub(r'[-_]', '', line)
		line = line.lower()
		f.write("\t\t" + line+ ": [\"4M\"],\n")
	f.write("\t}},\n")

f.write("};")

f.close()
"""



# it looks like we want alphabetized learnsets, so lets do that
learnset_list = [[] for i in range(len(pokemon_names_list))]
for i in range(len(pokemon_names_list)):
	learnset_list[i] = tmhm_list[i] + egg_move_list[i] + moveset_list[i]
	learnset_list[i] = list(set(learnset_list[i]))
	learnset_list[i].sort()
	for j in range(len(learnset_list[i])):
		learnset_list[i][j] = re.sub(r'[-_]', '', learnset_list[i][j])
		learnset_list[i][j] = learnset_list[i][j].lower()

# create the learnsets file with our created, combined list
f = open("learnsets_fluffyhusky.js", 'w+')
f.write("\'use strict\';\n\n")
f.write("exports.BattleLearnsets = {\n")
for i in range(len(pokemon_names_list)):
	pokemon_names_list[i] = re.sub(r'[-_]', '', pokemon_names_list[i])
	f.write("\t" + pokemon_names_list[i].lower() + ": {learnset: {\n")
	for line in learnset_list[i]:
		f.write("\t\t" + line + ": [\"4M\"],\n")
	f.write("\t}},\n")

f.write("};")

f.close()

# then remove egg and debug