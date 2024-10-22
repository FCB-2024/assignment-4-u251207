## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	def main(x):
    def count_divisors(n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count

    # Contar divisores de x
    divisores_x = count_divisors(x)

    # Verificar si algún número menor que x tiene más o iguales divisores
    for i in range(1, x):
        if count_divisors(i) >= divisores_x:
            print("not anti-prime")
            return

    print("anti-prime")

	c=0
	i=1

	while i <= x:
		if x % i == 0:
			c= c + 1
		i= i + 1
	l = x-1
	k = 0
	while l >= 1 and k< c:
		j=1
		k=0
		while j <= 1:
			if l % j == 0:
				k = k+1
			j = j+1
		l = l-1
	if k >= c:
		res="not anti-prime"
	else:
		res="anti-prime"
		


	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	x=int(sys.argv[1])
	print(main(x))
	

	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
