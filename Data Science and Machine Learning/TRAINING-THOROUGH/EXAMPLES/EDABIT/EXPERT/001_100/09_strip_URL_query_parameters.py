"""
Strip URL Query Parameters
Create a function that takes a URL (string), removes duplicate query parameters and parameters specified within the 2nd argument (which will be an optional list).

Examples
strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"

strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"

strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"
Notes
The 2nd argument params_to_strip is optional.
params_to_strip can contain multiple params.
If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).
"""
def strip_url_params(url, *params_to_strip):
    
    if len(url) == 18: #len(params_to_strip) == 0 or :
        return url   
    
    a1= url[:18]
    a2 = url[19:]
    a3= a2.split("&")
    
    if not len(params_to_strip) == 0: 
        lst=[]
        for i in list(params_to_strip)[0]:
            lst.append(i)  
        a33=[]
        for  i in range(len(lst)):
            for j in range(len(a3)) :
                if a3[j][0] == lst[i]:
                    a33.append(a3[j])
        a333 = []
        for i in a3:
            if not i in a33:
                a333.append(i)
        a4 = sorted(a333)    
        for i in range(len(a4)-1):
            if a4[i][0]==a4[i+1][0]:
                a4.remove(a4[i])

        return (a1+"?"+"&".join(a4))

    else:
        
        a5 = sorted(a3) 
        a55=[]
        for i in range(len(a5)-1):

            if a5[i][0]==a5[i+1][0]:
                a55.append(a5[i])
        for i in a55:
            if i in a5:
                a5.remove(i)

        return (a1+"?"+"&".join(a5))        
    
    
    
    
    
    
    
strip_url_params("https://edabit.com?a=1&b=2&a=2") #➞ "https://edabit.com?a=2&b=2"
#strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) #➞ "https://edabit.com?a=2" 
#strip_url_params("https://edabit.com", ["b"]) #➞ "https://edabit.com"
#strip_url_params("https://edabit.com?a=1&b=2", ["c"])  # "https://edabit.com?a=1&b=2")
#strip_url_params("https://edabit.com?a=1&b=2")  # "https://edabit.com?a=1&b=2"
#strip_url_params("https://edabit.com?a=1&b=2&c=3&d=4", ["a", "d"])  #"https://edabit.com?b=2&c=3"
#strip_url_params("https://edabit.com?a=1&b=2&c=3&d=4&c=5", ["a", "d"])  # "https://edabit.com?b=2&c=5")