"""
ASCII Charts (Part 2: Bar Chart)
Given a dictionary containing quarterly sales values for a year, return a string representing a bar chart of the sales by quarter.

Quarter names (Q1, Q2, Q3, Q4) should appear on the left.
Quarters should be sorted in descending order by value.
Quarters with the same value should be shown in their yearly order (Q1 -> Q4).
Bars should begin with a "|".
Repeat the character "#" to fill the bar, with each character having a value of 50.
A single space comes after the bar, then the sales for that quarter.
If the value is 0, there should be no space after "|".
Use the newline character ("\n") to separate each bar in the chart.
Example #1
bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})
➞ "Q1|###### 300\nQ4|##### 250\nQ2|### 150\nQ3|0"
When printed:

Q1|###### 300
Q4|##### 250
Q2|### 150
Q3|0
Example #2
bar_chart({"Q4": 500, "Q3": 100, "Q2": 100, "Q1": 150})
➞ "Q4|########## 500\nQ1|### 150\nQ2|## 100\nQ3|## 100"
When printed:

Q4|########## 500
Q1|### 150
Q2|## 100
Q3|## 100
"""
def bar_chart(results):

    a = list(sorted(sorted(results), key =results.get, reverse=True))
    b = list(sorted(results.values(), reverse=True))    
    c= []
    for i in range(len(a)):
        if b[i] == 0:
            c.append(a[i]+"|"+"#"*(int(b[i]/50))+ str(b[i]))
        else:    
            c.append(a[i]+"|"+"#"*(int(b[i]/50))+" "+ str(b[i]))
    return ("\n".join(c))

bar_chart({'Q4': 0, 'Q3': 100, 'Q2': 0, 'Q1': 600})

#bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})