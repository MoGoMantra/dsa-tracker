# How many Different Binary Trees can be generated through N nodes == catalan(n)
# For labeled nodes == unlabeled num * n!
# With max height => height = n-1 => num = 1X2X2X.....h-times = 2^h => 2^(n-1)
# if node values repeat itself by k1,k2,.. times 
# then number of poss unique binary tress are => catalan(n) * n! // ( k1! * k2! ....)



def catalan(n):
    """
    TC = O(2^n)
    """
    res = 0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
    return res

def bin_coff(n,k):
    res = 1
    if k>n-k:
        k = n-k
    for i in range(k):
        res*=(n-i)
        res//=(i+1)
    return res

def catlan2(n):
    """
    TC = O(n)
    """
    return (bin_coff(2*n,n)//(n+1))

def catlan3(n):
    """
    TC = O(n)
    """
    res = 1
    for i in range(2,n+1):
        res = (res*(4*n-2))//(n+1)
    return res

def catlan4(n):
    if n==1 or n==0:
        return 1
    return ((catlan4(n-1)*(4*n-2))//(n+1))

def factorial(n):
    fact = 1
    for i in range(n):
        fact*=(i+1)
    return fact

def fact_rec(n):
    if n == 0 or n ==1:
        return 1
    return n*fact_rec(n-1)

def label_nodes(n):
    res = catlan4(n) * factorial(n)
    return res

def lab_nodes(n):
    
    def nPk(n,k):
        res = 1
        for i in range(k):
            res*=(n-i)
        return res
    
    return (nPk(2*n,n)//(n+1))

def max_height_trees(n):
    return 2**(n-1)

def repitition_index(*repitn_values):
    res = 1
    for x in repitn_values:
        res*=factorial(x)
    return res


if __name__ == "__main__":
    n = 10
    print(f"Number of possible unlabelled unique binary trees with {n} nodes are {catlan2(n)}")
    print(f"Number of possible unique laelled binary trees with {n} nodes are {lab_nodes(n)}")
    print(f"Number of possible unique unlabelled binary trees with maximum height with {n} nodes are {max_height_trees(n)}")
    print(f"Number of possible unique labelled binary trees with maximum height with {n} nodes are {max_height_trees(n)*factorial(n)}")
    # node values repeating
    k1 = 2 # node value x repeating 2 times 
    k2 = 3 # node value y repeating 3 times
    k3 = 4 # node value z repeating 4 times
    # total num nodes > = k1+k2+k3+.....
    num_nodes_label = lab_nodes(n) // repitition_index(k1,k2,k3)
    num_nodes_max_height_label = (max_height_trees(n)*factorial(n)) // repitition_index(k1,k2,k3)

    print(f"Number of possible unique laelled binary trees with {n} nodes with repititions {k1},{k2},{k3} {num_nodes_label}")
    print(f"Number of possible unique labelled binary trees with maximum height with {n} nodes  with repititions {k1},{k2},{k3} are {num_nodes_max_height_label}")
