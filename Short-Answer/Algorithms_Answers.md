#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - it continues till the value of a is more than the product of n^3


b) O(n^2) - the for loop will go through the range of n, then the while loop will continue till j is more than n


c) O(n) - this will continue till the number of bunnies is 0

## Exercise II

I would find the length of the building then start at the middle floor. I'd drop an egg off the middle floor then, if it breaks, I'd move down a floor and try again. I would repeat going down a floor till the dropped egg no longer breaks.
The inverse of that is if I drop the egg from the middle floor and it doesn't break, then I move up a floor till the egg breaks, then I stop.
The runtime would be O(n) because I have to go down the length of a list whether up or down.
