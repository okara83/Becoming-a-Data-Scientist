"""
https://edabit.com/challenge/MFFuPFnjT8ihniKtL

Parabolic Jumps
When a bug jumps to a height y, its position can be plotted as a quadratic function with x as the time, 
and y as the vertical distance traveled. 
For example, for a bug that jumps 9 cm up and is back on the ground after 6 seconds, its trajectory can be plotted as:

bug jump quadratic plot

Create a function that, given the max height of a vertical jump in cm and the current time in milliseconds, 
returns the current position of the bug rounded to two decimal places, and its direction ("up" or "down"). 
If the bug is already back on the ground, return 0 for the position and None for the direction.

Examples
bug_jump(9, 1000) ➞ [5, "up"]

bug_jump(9, 4000) ➞ [8, "down"]

bug_jump(9, 5500) ➞ [2.75, "down"]

bug_jump(9, 7000) ➞ [0, None]
Notes
Time and position both start at 0.
You only need to translate the parabola (you don't need to scale it).
"""
def bug_jump(height, time):
    t = time /1000
    
    # y = x**2 / 4 ,  https://www.futurelearn.com/courses/maths-linear-quadratic/0/steps/12114
    x = 2 * (height ** 0.5)
    
    if 0 < t < x/2:
        return [round((-t**2+t*x),2), "up"] 
    
    elif x/2 < t < x:
        return [round((-t**2+t*x),2), "down"]

    else:
        return [0, None]

bug_jump(9, 1000) #➞ [5, "up"]
#bug_jump(9, 4000) #➞ [8, "down"]
#bug_jump(9, 5500) #➞ [2.75, "down"]
#bug_jump(9, 7000) #➞ [0, None]