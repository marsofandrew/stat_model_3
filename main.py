import tests as ts
import sys

values_count = 10 ** 4

if len(sys.argv) == 1:
	print("[Error] Enter some argument or type 'help' as an argement to see all availible distributions")
elif len(sys.argv) >= 3:
	print("[Error] Two or more arguments are not allowed! Type 'help' to see some arguments")
else:
	if sys.argv[1] == "help":
		print(" Choose your distribution as an argument to get results")
		print(" of work all availible methods which implement it. Availible now:")
		print("\n *Continious distributions: uniform, normal, exponential, chisquare,")
		print(" 			  student")
	
	elif sys.argv[1] == "uniform":
		a, b =  1., 100.
		ts.testUniform(a, b, values_count)

	elif sys.argv[1] == "normal":
		mu, sigma, N = 0, 1, 12
		ts.testNormal(mu, sigma, N, values_count)

	elif sys.argv[1] == "exponential":
		betta = 1
		ts.testExponential(betta, values_count)

	elif sys.argv[1] == "chisquare":
		N = 10
		ts.testChisquare(N, values_count)

	elif sys.argv[1] == "student":
		N = 10
		ts.testStudent(N, values_count)	

	else:
		print("Unknown distribution! Type 'help' to see all availible distributions")
