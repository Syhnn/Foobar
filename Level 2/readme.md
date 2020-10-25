# Level 2

## First challenge
In this problem, we wanted to figure out the parent of a node given only the height of a perfect binary tree and knowing how to numerate the nodes.  
To numerate the nodes, you'd basically go through the tree by always checking the left child first. So for a tree of height 3 you'd have :  
```
   7
 3   6
1 2 4 5
```
So given the node number 3, you'd want to return 7. For the root, you'd return -1.  
At first I didn't have many ideas so I just implemented the tree, and read it to get the answer. But it was a bit inefficient. I think those exercises aren't just easy/medium difficulty but also allow to see if we can find better solutions.  
With that in mind I tried to see if there was any logic in the answer, and sure enough there was. If you list the answers the same way you list the nodes, in an array as it is passed in parameter :  
```
height = 3
nodes = [1, 2, 3, 4, 5, 6, 7]
answers = [3, 3, 7, 6, 6, 7, -1]
```
You can kind of start seeing the logic if you increase the height :  
```
height = 4
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
answers = [3, 3, 7, 6, 6, 7, 15, 10, 10, 14, 13, 13, 14, 15, -1]
```
When you increase the height you simply add another identic tree next to the first one and a new root node at the top to merge both tree. To numerate the new tree you'd just have to keep the same values but increase them by the number of nodes in the initial tree.  
```
    new_root                     15
   7       7                 7        14 
 3   6   3   6             3   6   10   13
1 2 4 5 1 2 4 5    -->    1 2 4 5 8 9 11 12
```
So in order to get the list of result for the next height, you take the previous one, and append 3 things : 2^h - 1, the previous list + 2^h-1 - 1, 2^h - 1. Because increasing the height doesn't change the beginning of the list, you can iterate while following this logic and just add -1 at the end :  
```
height = 2
answers = [3, 3] # and -1
-> [3, 3, 7, 6, 6, 7] -> [3, 3, 7, 6, 6, 7, 15, 10, 10, 14, 13, 13, 14, 15] -> and so on... then add -1 at the end.
```
By doing that I don't even need to implement a tree, which was taking a lot of time before sending back an answer.  

## Second challenge
For this challenge the idea was to assign a value to a set of coordinate (this isn't exactly how it was presented but that's how I understood it afterwards).  
```
4 | 7
3 | 4 8
2 | 2 5 9
1 | 1 3 6 10
y +---------
  x 1 2 3 4 
```
I think I missed the point when I did this one on Foobar. This is a very easy question. When I sent my answer I just wanted to see the level 3, so I quickly calculated the answer using for loops and submited it.  
But I think that was a mistake, even when the question is easy you should probably think about it to check if there isn't a way of simplifying it.  
here I figured I had to sum all integers up to x, then continue up to y but starting from x. What I forgot about was this formula :
```
sum(1, n) = n * (n - 1) / 2
```
With this I realised I could just calculate the sum of integers from 1 to x+y, add x, and that's it.
