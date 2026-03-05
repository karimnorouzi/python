# Local
# Enclosing
# Global
# Builtins
# --- Global lookup works ---
def f():
	print(s)

s = "I love Paris in the summer!"
f()
# --- Local assignment creates local scope ---
def g():
	print(x)     # ERROR
#	x += 2       # x becomes local

x = 1
g()
