import itertools
import mpmath
def perm_comb(items, k):
    n = len(items)
    permute_all = list(itertools.permutations(items))
    permute_k = list(itertools.permutations(items, k))
    permute_repeat = [i for i in itertools.product(items, repeat = k)]
    choose_k = list(itertools.combinations(items, k))
    print("Permutations of this set:\n")
    print(permute_all,"\n")
    print("Number of such permutations:", len(permute_all), "\n\n")
    print("Permutations obtained on choosing %i elements at a time:\n" %k)
    print(permute_k,"\n")
    print("Number of such permutations:", len(permute_k), "\n\n")
    print("Permutations of %i elements with repetitions allowed:\n" %k)
    print(permute_repeat,"\n")
    print("Number of such permutations:", len(permute_repeat),"\n\n")
    print("Combinations obtained on choosing %i elements at a time:\n" %k)
    print(choose_k,"\n")
    print("Number of such permutations:", len(choose_k), "\n\n\n")
    print("n! = ", int(mpmath.factorial(n)),"\n")
    print("n!/k! = ", int(mpmath.ff(n,k)), "\n")
    print("n^k = ", n**k, "\n")
    print("n choose k = ", int(mpmath.binomial(n,k)), "\n")
