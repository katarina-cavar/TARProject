def title_print(title):
	no_equals = len(title) + 16
	print()
	print("="*no_equals)
	print("\t{}".format(str(title)))
	print("="*no_equals)
	print()

def line_print(title):
	no_equals = len(title)
	print()
	print("{}".format(str(title)))
	print("-"*no_equals)