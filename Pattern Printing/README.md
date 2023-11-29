# Patterns with Python
There are 22 patterns which are to be constructed from the question set. Run this program and chose which pattern number you want to print.<br>
**Question Set**: https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/
<br><br>

### Information on some patterns
<i><u>Pattern 9</u></i><br>
(1 to mid) and (mid to 1) -> even  <br>
(1 to mid+1) and (mid-1 to 1) -> odd <br>

<i><u>Pattern 11</u></i><br>
Kinda like XOR gate:<br>
|i%2|c%2|Output|
|---|---|------|
| 0 | 0 |   1  |
| 0 | 1 |   0  |
| 1 | 0 |   0  |
| 1 | 1 |   1  |

<i><u>Pattern 19</u></i><br>
Upper Half
| Stars | Spaces | Stars |
|-------|--------|-------|
|   5   |   0    |   5   |
|   4   |   2    |   4   |
|   3   |   4    |   3   |
|   2   |   6    |   2   |
|   1   |   8    |   1   |

Lower Half
| Stars | Spaces | Stars |
|-------|--------|-------|
|   1   |   8    |   1   |
|   2   |   6    |   2   |
|  ...  |  ...   |  ...  |


<i><u>Pattern 22</u></i><br>
0 0 0 0 0 0 0<br>
0 1 1 1 1 1 0<br>
0 1 2 2 2 1 0<br>
0 1 2 3 2 1 0<br>
0 1 2 2 2 1 0<br>
0 1 1 1 1 1 0<br>
0 0 0 0 0 0 0<br>
Each point in the matrix can be given by coordinate (x, y) and value stored in that point is the least distance of the point from a edge line which are x=0, x=6, y=0, y=6.<br>
We have subtracted 4 from each value to get the desired pattern.