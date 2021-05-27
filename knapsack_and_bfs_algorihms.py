import numpy as np
def SELECT_TOURIST(g,p,r_array,n_array):
    results = np.array(np.zeros((p+1,g+1),dtype=np.int32))
    for i in range(1,g+1):
        for j in range(1,p+1):
            
            results[j][i] = results[j][i-1]
            if n_array[i-1]<=j:
                
                val = results[j-n_array[i-1]][i-1]+r_array[i-1]
                if results[j][i] < val:
                   results[j][i] = val
    maxGroups = []
    j = p
    for i in range(g,0,-1):
        weight = n_array[i-1]
        value = r_array[i-1]
        if results[j][i] == results[j-weight][i-1]+value:
            j = j-weight
            maxGroups.append(i)
    return results[p][g],maxGroups



def MIN_BRIDGES(graph,n):
    visited = [False for i in range(n)]
    queue = []
    count = 0 #number of cities
    for i in range(n):
        if not visited[i]:
            count += 1
            queue.append(str(i+1))
            while queue:
                key = queue.pop(0)
                for neighbour in graph[key]:
                    if not visited[int(neighbour)-1]: 
                        visited[int(neighbour)-1] = True
                        queue.append(neighbour)
    return count-1 #minimum number of bridges

def main():
    
    g = 5
    p = 40
    r_array = [2000,400,1200,800,2200]
    n_array = [24,16,32,8,26]
    
    print("First sample of first algorithm: ")
    print(SELECT_TOURIST(g, p, r_array, n_array))
    print()
    
    
    g = 7
    p = 90
    r_array = [500,1200,800,100,1100,60,900]
    n_array = [40,80,50,30,60,15,25]
    print("Second sample of first algorithm: ")
    print(SELECT_TOURIST(g, p, r_array, n_array))
    
    num_graph = {
        "1":["2","3"],
        "2":["1"],
        "3":["1","4"],
        "4":["3","6"],
        "5":["6"],
        "6":["4","5"],
        "7":["9"],
        "8":["9"],
        "9":["7","8"],
        "10":["12"],
        "11":["12","13"],
        "12":["10","11"],
        "13":["11"],
        "14":["15"],
        "15":["14"],}
    print()
    print("Min number of bridges is",MIN_BRIDGES(num_graph, 15))

main()