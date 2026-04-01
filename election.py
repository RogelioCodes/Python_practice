
"""
Given an array of names of candidates in an election. A candidate’s name in the array represents a vote cast on the candidate. 
Print the name of candidates who received the maximum vote. If there is a tie, print a lexicographically smaller name.
"""
def findWinner(votes):
    count = {}
    maxV = 0
    res = ""
    for name in votes:
        count[name] = 1 + count.get(name, 0)
      
        if count[name] > maxV:
            maxV = count[name]
            res = name
        elif count[name] == maxV:
            res = min(res, name)

    print(f"count: {count}")
    print(f"maxV: {maxV}")
    print(f"res: {res}")

votes = [ "john", "johnny", "jackie", "johnny",
        "john", "jackie", "jamie",  "jamie",
        "john", "johnny", "jackie", "jackie", "jackie", "jackie", "jamie",  "johnny",
        "john" ]
 
findWinner(votes)