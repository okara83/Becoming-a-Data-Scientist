Bolded assignments are effectively *new* compared to previous years of the course. 

#### Assignment 1: Python/Jupyter Basics
- Q1: Markdown formatting, Jupyter shortcuts
- Q2: List manipulations, pass by reference, dictionary keys
- Q3: Falsy values, is vs ==
- Q4: FizzBuzz
- Q5: Fibonacci: Recursion vs DP
- Q6: List Comprehensions

#### Assignment 2: Sage Basics
- Q1: Distribution of Prime Numbers
- Q2: Diophantine Equations/Naive Diophantine Solver
- Q3: Taylor Series
- Q4: Integrating Area Under Ellipse
- Q5: **Compute your Grade in this Class**
    - Given scores for a student on assignments/quizzes/final project/participation, compute their final grade in this class

#### Assignment 3: Linear Algebra
- Q1: Numerical Instability 
    - **Be careful; I believe this same question in previous years has a syntax error due to NumPy componentwise multiplication quirks**; I don't think the instability really visually kicks in until the Hilbert matrix is at least 15x15 or so
- Q2: Image Compression via SVD
    - **I think you asked a question along these lines in a previous class but I don't know exactly when or where it was so this is "new take" on an old question**
- Q3: Gradient Fields
    - **There is a new part to this which gives a visual depiction of curl**
- Q4: Numerically confirm linear algebra theorems on some concrete examples
- Q5: **Conjecture and Proof: The Fibonacci Matrix**
    - Set up the 2x2 matrix $M$ which has the property that $M^n$ has nth Fibonacci number in top left; conjecture a formula and use this conjecture to prove Fibonacci identities.

#### Assignment 4: Combinatorics/Graph Theory
- Q1: Chicken Nugget Problem
- Q2: Travelling College Student Problem 
    - Various versions of this question have been asked; **be careful** and ensure that the computation can actually be carried out it **cannot** be carried out on the version I provided (50 cities to visit)
- Q3: Numerically Computing Thresholds in Random Graphs
- Q4: **Spectral Properties of Graphs**
    - Nicer in theory than practice; exercise as is does not work like I want it to due to computational costs for *exact* computation of things. Could be good with some additional care
- Q5: **Permutations**
    - Counting derangements
    - Counting longest increasing subsequences and approximating the Tracy-Widom distribution

#### Assignment 5: Basic Number Theory
- Q1: **Function Graphs mod N**
    - With a somewhat underlying theme of Pollard's Rho Algorithm
- Q2: Sophie Germain Primes
    - **New part on Cunningham Chains**
- Q3: **Quadratic Residues** (previously just part of the lecture; I booted this to an exercise)
    - Numerical verification of Quadratic Reciprocity and Cebotarev
- Q4: Artin's Conjecture on Primitive Roots
- Q5: **Selfridge's Conjecture**
    - Numerically verifying a conjectural primality test

#### Assignment 6: Cryptography, Basic Data Analysis (*without* Pandas)
- Q1: **Calculating the EPL Champion**
    - Given a text file of season results for English Premier League, compute the champion "by hand"
- Q2: **Reviewing some Cryptosystems**
    - A very tame exercise to make sure everyone was on the same page regarding RSA and DHM
- Q3: Attacks on RSA
- Q4: **Linear Regression and the Hawaiian Emperor Seamount Chain**
    - Bread and butter series of linear regression questions
- Q5: **Feature Engineering and Moore's Law**
    - Linear regression can model exponential growth if you just take logs

#### Assignment 7: Stats/Data Analysis (*with* Pandas)
- Q1: Basic Pandas Syntax
    - Written from scratch on a new dataset, so a **new take** 
- Q2: **Data Pipelines**
    - Impute missing values, ordinal encoding, interaction terms on made up data set
- Q3: **Bias Variance Tradeoff and Overengineering**
    - On a roughly quadratic bivariate data set, compare polynomial regression of degrees 1, 2, 12.
- Q4: **Hypothesis Testing**
    - Have NBA players gotten taller since 1995? Are NBA players taller than the average human?
- Q5: **Simpson's Paradox**
    - Two versions; I don't know if the paradox "clicked" for them, so maybe give better guidance
    
#### Assignment 8: Natural Language Processing
- Q1: **Stylometry: Dickens vs Wells**
    - Compare War of the Worlds to Tale of Two Cities and then guess the author of a third mystery text
- Q2: **Zipf's Law and the Scarlett Letter**
    - Exhibit the power rule that occurs when looking at the frequency that words are used in a text
- Q3: **SVM Classifiers**
    - This was underprepared; a better version of the question exists. The idea was to have them discover the linear decision boundary that comes from an SVM.
- Q4: **Fun with Word Vectors**
    - Exploring analogies, similar words, and autoantonyms with GloVe word vectors
- Q5: **Dark Magic with Word Vectors**
    - Romantic vs Depressing poetry can be linearly separated with fairly high accuracy (~80-85%) *just by looking at the average word in the poem.*
