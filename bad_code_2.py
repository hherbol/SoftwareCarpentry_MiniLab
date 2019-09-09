if __name__ == "__main__":
    # For your own health, I'm cutting you off to a max of 4 beers.
    max_n = 4
    for i in range(max_n, -1, -1):
    	if i > 2:
        	print("%d bottles of beer on the wall, %d bottles of beer.  Take one down, pass it around, %d bottles of beer on the wall." % (i, i, i-1))
        elif i == 2:
        	print("%d bottles of beer on the wall, %d bottles of beer.  Take one down, pass it around, %d bottle of beer on the wall." % (i, i, i-1))
        elif i == 1:
        	print("%d bottle of beer on the wall, %d bottle of beer.  Take it down, pass it around, %d bottles of beer on the wall." %(i,i,i-1))
        elif i == 0:
        	print("No bottles of beer on the wall, no bottles of beer.  Go to the store, buy some more. %d bottles of beer on the wall." % (max_n))
        else:
        	break
        	