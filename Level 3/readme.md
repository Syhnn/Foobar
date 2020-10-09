# Level 3
## First challenge
This is probably where most people start learning about problems they didn't know before. For this one I'd have to figure out a path in a grid using a pathfinding algorithm. The twist is that we were able to remove one wall of our choosing.  
  
For this I went with Breadth First Search which is a very simple way to do pathfinding. The idea is jut to check every node going from either the start or the end and process them one by one until we reach the opposite side. I hesitated to use more complex algorithms but I wanted to explore that more in details so I made another personnal project to do so [here](https://github.com/Syhnnn/Pathfinder).  
  
To handle the removal of the wall I simply listed all the wall positions and tried to remove them one by one. Because the grid was limited in size (20x20 max) we'd never have to run the code more than 361 times, and in that case the path would be "straight" to the end and only 39 nodes long. There may be a sweet spot between no walls and 361 walls where it takes a bit longer but with the grid capped like that going bruteforce isn't an issue.  

If I wanted to improve it to be able to run on much larger grids I'd try a few things like handling specific cases (if without touching anything the path is already the shortest it can be there's no need to think about a solution), or to try and detect when it is useless to remove a wall :  
When moving in a grid with no weight associated to its nodes, those two moves are equivalents :
```
+--+             +--+
|12| going right |1 | going down
| 3|  then down  |23| then right
+--+             +--+
```
So if you encounter a wall that is 2 nodes thick when trying to go from A to B, removing one is useless :
```
+------+  +------+  
|A     |  |A     |  
| #####|  | #####|  
| #####|  |  ####|  
|     B|  |     B|  
+------+  +------+  
```
Because it wont ever allow you to pass that wall if it blocks you. It would be beneficial in case diagonal moves where permitted because tou could litterally "cut corners" but that is not the case here. 
So you could try and detect such wall, and not even try to remove them if you know that's useless. For exemple if a wall is next to too many other walls (like 3 for example) removing them will be useless.  

## Second Challenge
For the second challenge you are given a number of bricks in input and you must determine how many different staircases you can build with those following a set of rules :  

- Every next step musty be strictly higher than the previous one
- You can build an incredibly high step next to a very low one as long as the first rule is respected
- A staircase is made of at least two steps

So if you have 3 bricks in input, there's only one solution :
```
#
##
21
```
But if you have 5, there's two way to do it :
```
#
#  #
#  ##
## ##
41 32
```
Both are valid starcases.  
  
To solve this I decided to use recursivity, which may not have been the smartest choice because it felt really slow to process. 
What I wanted to do was to take let's say the case where there was 2 steps, process every possibility, then go to the case where there are 3, and so on.  
After playing with it a bit I realized I was recalculating things I had already done before, so I decided to store the previous results in a hashtable to reuse them, and it work out fine.

## Third challenge
The last one I was a bit disappointed about. 
Not the challenge in itself, but rather the fact that I encountered the answer on the internet while searching for information. 
Basically at first I tried my usual approach for when I don't have many idea : 
I try to implement something first quickly in order to see which issue I encounter first. 
By doing so I get additionnal insight on problems that reveal their complexity only when you try to implement them. 
Here my first try was to brutally for loop my way to a solution. 
Which works really well but is also super slow, because you get O(n3) complexity. 
When I re-read the question I realized they put "lucky triples" in between double-quotes, so I figured maybe it was a known thing and researched more about it which got me to someone else's answer. 
So yeah a bit disappointed I didn't get to figure it out entirely myself but since I managed to clear the next level, I guess it's okay.
