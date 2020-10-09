# Level 4
## First challenge
This problem was very, very interesting. I think it illustrate really well what Foobar was about (at least for me). 
It's not about knowing everything and going forward with that, as others have already said it's more like encountering a new, unknown issue, and learning how to solve it. 
When I first read the problem statement, I had no idea what to make of it. 
To sum it up they were describing how you had a few rooms on a floor, with entrances, escape pods and intermediary rooms. 
And you had to figure out how many rabbits (or people, but in this case it was about rabbits escaping a spaceship, yes really) could reach the escape pods every "turn". 
I had no idea how I was supposed to go with that, what time we had, etc. 
So I started writing all that stuf on a whiteboard, and after researching infos for a few hours, I realized the data they gave me was an Adjacency Matrix, 
and we were talking about Graph Theory (which I knew very little about).  
  
With that in mind I started to orient my researchs by typing stuff like "maximum traffic on a graph" and quickly found out about the Maximum Flow problem. 
To solve this I found out I could use the [Ford-Fulkerson Algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm). 
Basically what you end up doing is creating another equivalent graph, a "flow graph" by taking every possible route from each entrance to each exit, using the maximum flow you can every time. 
So if for the first route you pass 3 edges, with maximum flow values of 19, 12 and 16 for example, you'd add a flow of 12 on this path on the flow graph, because it is the maximum value you can reach on this route (the value of the lowest edge). 
If you do that until you've explored every possibilities, you end up with one solution for the maximum flow, and you just have to sum up either the values of all the edges going to each exit or going out of each entrance.  
  
This was really satisfying to solve because it was the first "hard" (to me) problem that I knew nothing about. 
By hard problem I mean a known issue which is complicated enough to have theorems and algorithms that are commonly used to solve this particular issue. 
I really enjoyed that one.  

## Second challenge
This was by far the hardest challenge that I solved. I didn't clear the fifth level yet, and I don't know if I will because I might lack the time and ability to do so. 
But apart from that this problem was really hard. For this challenge your are placed in a room which size you are given. 
You get your position on a lattice in the room, and a target position. 
You are then given a weapon with an associated range d and are told that the projectiles bounce on walls until the maximum range is reached or they hit the target (or yourself). 
If you hit a corner, the projectile just bounce back the direction it came (essentially ending up hitting you if the range is long enough).
The goal is to find out in how many different directions you can shoot in order to hit the target.  
  
The key to this problem is realizing that you can represent bounces by drawing a reflexion of the room your in. 
I'll try to illustrate, given this room if you try to shoot the wall at the bottom :  
```
+---------+
|         |
|  P   T  |
|   \ /   |
+----v----+
```
You can hit the target. If you want, you can calculate the bounce to check wether you hit or not, here you can do so because it's a very simple trajectory. 
But if you have a very big range you might also be able to touch the target after hitting the top and bottom wall dozens of times bouncing back and forth, and this takes much longer to calculate. 
So instead the idea is to imagine the walls are mirrors, and draw the reflections relative to them :  
```
+---------+
|         |
|  P   T  |
|   \     |
+----\----+
|     \   |
|  P   T  |
|         |
+---------+
```
By doing so you only have two things to worry about : distance, and angle, which are part of a polar coordinate system as long as you bring the origin back to you. 
You don't really have to worry about corners, because hitting one will always mean that you'll end up hitting yourself, so you can just check wether you hit one of your reflections or not. 
What I did was generating two lists : the list of the target and its reflections, and the list of my reflections. 
from there I loop only once through all the targets and check if I'm in range, and if it is and I don't already hit a target or myself using that direction, I add one to the count. 
eventually I ended up taking a few particular cases to speed up the process, like "is the target on the same x or y axis as me ?", and that was it. 

