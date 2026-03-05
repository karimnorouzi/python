global_state = 0
def impure_function(x):
	global global_state
	global_state += x
	return global_state


impure_function(5)
print(global_state)  # Output: 5
