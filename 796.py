def strstr(s:str,goal:str):
    if len(s)!=len(goal):
        return False
    goal_s = s+s
    print(goal_s)
    return goal in goal_s

print()