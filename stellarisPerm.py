#exec(open("stellarisPerm.py").read())

import itertools

BLANK_PLACEHOLDER = "EMPTY"
ETHICS = ['Xenophobe', 'Xenophile', 'Spiritualist', 'Materialist', 'Egalitarian', 'Authoritarian', 'Militarist', 'Pacifist']

def generate_permutation():
	all_entry_permutation = list(itertools.permutations(ETHICS))
	snipped_permutations = [combination[:3] for combination in all_entry_permutation]
	return [list(entry) for entry in snipped_permutations]

def fanatic_count_in_ethics_combination(combination):
	fanatic_ethics_count = 0
	for fanatic_ethic in FANATIC_ETHICS:
		fanatic_ethics_count += fanatic_ethic in combination
	return fanatic_ethics_count

def ethics_contradict(ethics):
	return (('Xenophobe' in ethics and 'Xenophile' in ethics) 
		or ('Spiritualist' in ethics and 'Materialist' in ethics) 
		or ('Egalitarian' in ethics and 'Authoritarian' in ethics) 
		or ('Militarist' in ethics and 'Pacifist' in ethics))

def remove_duplicates(permutations):
	perms_sorted_interior = [sorted(entry) for entry in permutations]
	duplicate_sorted_remove = list(perms_sorted_interior for perms_sorted_interior,_ in itertools.groupby(perms_sorted_interior))
	contradicting_ethics_removed = [entry for entry in duplicate_sorted_remove if not ethics_contradict(entry)]
	for entry in contradicting_ethics_removed:
		if BLANK_PLACEHOLDER in entry:
			entry = entry.remove(BLANK_PLACEHOLDER)
	return contradicting_ethics_removed

combinations = remove_duplicates(generate_permutation())
f = open("combinations.txt", "w")
for ethics in combinations:
	for ethic in ethics:
		f.write(ethic + "\t")
	f.write("\n")
f.close()