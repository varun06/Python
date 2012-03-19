def squareRoot(n):
	initialGuess = n/2;
	finalGuess = (initialGuess + (n/initialGuess)/2)
	while(abs(finalGuess - initialGuess	> 0.0001)):
		initialGuess = finalGuess
		finalGuess = (initialGuess + (n/initialGuess)/2)
	while finalGuess*finalGuess > n:
	    finalGuess -= 1
	return finalGuess

print squareRoot(9)