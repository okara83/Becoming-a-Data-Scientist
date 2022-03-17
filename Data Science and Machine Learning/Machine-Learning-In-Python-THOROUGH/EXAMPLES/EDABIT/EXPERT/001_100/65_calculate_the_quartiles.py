"""
Calculate the Quartiles
In statistic a quartile is a type of quantile, more specifically is any of the three values (q1, q2 or q3) that divide the items of a sorted frequency distribution (that starts at q0 with the lowest value and ends at q4 with the highest value) into four classes with each containing one fourth of the total population.

There are three main methods used for calculate the quartiles of a dataset: Tukey (abbr. T), Moore & McCabe (abbr. MM) and Mendenhall & Sincich (abbr. MS). (see Resources tab for more informations about quartiles and other calculation methods).

As already said, in a dataset q0 is the lowest value and q4 is the highest value.
All methods share one common statement: q2 is equal to the median of the set.
Using T or MM you split the dataset in two parts:

If dataset has an odd population T includes the median appending it at the end of the lower half and at the beginning of the upper half, while MM excludes the median from both parts.
If dataset has an even population is splitted in two equal parts by both methods.
With the dataset split in two q1 is equal to the median of the lower half and q3 is equal to the median of the upper half.
Using MS you don't split the dataset:

q1 is equal to the nth term of the dataset with n equal to (population length + 1) / 4, rounded to the nearest integer, unless the decimal part is equal to 0.5, in that case it should be rounded up to the nearest integer.
q3 is equal to the nth term of the dataset with n equal to 3 * (population length + 1) / 4 rounded to the nearest integer, unless the decimal part is equal to 0.5, in that case it should be rounded down to the nearest integer.
Given a list of values and a string with one of the three possible methods ("T", "MM" or "MS") return a list in the form [q0, q1, q2, q3, q4].

Examples
get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "T") ➞ [1, 3.5, 6, 8.5, 11]
# T includes the median (q2 = 6) in lower half (1 to 6, q1 = mean of 3+4)
# and in upper half (6 to 11, q3 = mean of 8+9).

get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "MM") ➞ [1, 3, 6, 9, 11]
# MM excludes the median in lower half (1 to 5, q1 = 3) and in upper
# half (7 to 11, q3 = 9).

get_quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9] ➞ [1, 3, 5, 7, 9]
# With MS q1 = population + 1 = 11 / 4 = 2.75 rounded up to 3 = third
# number of dataset, and q2 = population + 1 = 11 * 3 = 33 / 4 = 8.25
# rounded down to 8 = eighth number of dataset.
Notes
Try this challenge if you need to get familiar with medians.
The dataset has to be sorted in ascending order.
Values can be either positive or negative integers.
All given lists are valid, no exceptions to handle.
Test.assert_equals(get_quartiles([4, 1, 7, 8, 3, 6, 5, 2], "T"), [1, 2.5, 4.5, 6.5, 8])
Test.assert_equals(get_quartiles([4, 1, 7, 8, 3, 6, 5, 2], "MS"), [1, 2, 4.5, 7, 8])
Test.assert_equals(get_quartiles([2, 6, 1, 8, 5, 9, 7, 4, 3], "MM"), [1, 2.5, 5, 7.5, 9])
Test.assert_equals(get_quartiles([2, 6, 1, 8, 5, 9, 7, 4, 3], "MS"), [1, 3, 5, 7, 9])
Test.assert_equals(get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "T"), [1, 3, 5.5, 8, 10])
Test.assert_equals(get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "MM"), [1, 3, 5.5, 8, 10])
Test.assert_equals(get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "MS"), [1, 3, 5.5, 8, 10])
Test.assert_equals(get_quartiles([3, 9, 11, 2, 4, 1, 8, 6, 10, 5, 7], "T"), [1, 3.5, 6, 8.5, 11])
Test.assert_equals(get_quartiles([3, 9, 11, 2, 4, 1, 8, 6, 10, 5, 7], "MM"), [1, 3, 6, 9, 11])
Test.assert_equals(get_quartiles([41, 33, 10, 26, 52, 77, 20, 39, 33, 33], "T"), [10, 26, 33, 41, 77])
Test.assert_equals(get_quartiles([-4, -25, -33, 12, 37, 12], "MM"), [-33, -25, 4, 12, 37])
Test.assert_equals(get_quartiles([-121, 8, -3, 12, 412, -66], "MS"), [-121, -66, 2.5, 12, 412])
"""
def get_quartiles(lst, method):
    
    a=sorted(lst)
    q0, q4 = a[0], a[-1]
    if len(a)%2==1: q2 = a[(len(a)-1)//2]
    else: q2 = (a[len(a)//2] + a[(len(a)//2)-1])/2

    if method == "T":
        if len(a)%2==1:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2-1:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2            
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2                 
        else:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2 
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2        

    elif method == "MM":
        if len(a)%2==1:
            b1 = a[:(len(a)-1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2            
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2                 
        else:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2 
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2  
                    
    elif method == "MS":
        if ((len(a)+1)/4)-((len(a)+1)//4) < 0.5:
            q1 = a[int((len(a)+1)//4)-1]
            q3 = a[3*(len(a)+1)//4]
        else: # ((len(a)+1)/4)-((len(a)+1)/4) < 0.5:
            q1 = a[int((len(a)+1)//4)]
            q3 = a[3*(len(a)+1)//4-1]
                                        
    return ([q0,q1,q2,q3,q4])

            
            
#get_quartiles([4, 1, 7, 8, 3, 6, 5, 2], "T") #, [1, 2.5, 4.5, 6.5, 8])
#get_quartiles([4, 1, 7, 8, 3, 6, 5, 2], "MS") #, [1, 2, 4.5, 7, 8])
#get_quartiles([2, 6, 1, 8, 5, 9, 7, 4, 3], "MM") #, [1, 2.5, 5, 7.5, 9])
#get_quartiles([2, 6, 1, 8, 5, 9, 7, 4, 3], "MS") #, [1, 3, 5, 7, 9])
#get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "T") #, [1, 3, 5.5, 8, 10])
#get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "MM") #, [1, 3, 5.5, 8, 10])
#get_quartiles([10, 3, 1, 8, 6, 4, 7, 5, 2, 9], "MS") #, [1, 3, 5.5, 8, 10])
get_quartiles([3, 9, 11, 2, 4, 1, 8, 6, 10, 5, 7], "T") #, [1, 3.5, 6, 8.5, 11])
#get_quartiles([3, 9, 11, 2, 4, 1, 8, 6, 10, 5, 7], "MM") #, [1, 3, 6, 9, 11])
#get_quartiles([41, 33, 10, 26, 52, 77, 20, 39, 33, 33], "T") #, [10, 26, 33, 41, 77])
#get_quartiles([-4, -25, -33, 12, 37, 12], "MM") #, [-33, -25, 4, 12, 37])
#get_quartiles([-121, 8, -3, 12, 412, -66], "MS") , [-121, -66, 2.5, 12, 412])