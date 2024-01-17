
def get_probability(n, m):
    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    Dynamic Programing Tabulation
    """
    
    if n < m or n < 0 or m < 0:
        print("Incorrect inputs")
        return

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(m-1,-1,-1):
            dp[i][j] = dp[i-1][0] + dp[i-1][j+1]

    valid_way = dp[n][0]  
    way_to_miss_last_day = dp[n-1][1]  
    
    for i in dp:
        print(i, "\n")
        
    return f"{way_to_miss_last_day}/{valid_way}"

n = 5 # number of days
m = 4 # number of classes you are not allowed to miss or more consecutive days.
print(get_probability(5,4))
