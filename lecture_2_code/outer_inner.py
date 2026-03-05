def outer():
	x = "outer variable"
	def inner():
		print(x)  # Accesses the outer variable
	inner()



outer()  # This will print "outer variable"
