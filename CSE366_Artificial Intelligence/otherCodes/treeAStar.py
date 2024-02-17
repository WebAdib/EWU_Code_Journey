from collections import deque

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is heuristic function which is having values for all nodes
    def h(self, n):
        H = {
            'A': 14,
            'B': 12,
            'C': 11,
            'D': 6,
            'E': 4,
            'F': 11,
            'Z': 0
        }

        return H[n]

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected

        open_lst = set([start])
        closed_lst = set([])

        # poo(shortest distance) has present distances from start to all other nodes
        # the default value is +infinity

        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes

        par = {}
        par[start] = start
##        print(open_lst) #open list a sudhu A ache
##        print(closed_lst) #A er sob node travers kori nai tai ata empty
##        print(poo) # A theka A te jawar shortest distance 0

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                print("open list : "+ str(open_lst))
                print("Close list : "+ str(closed_lst))
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    print("lesser value : "+str(poo[v] + self.h(v))) #2nd time 4 + 12
                    print("Current Root : "+ str(v))
                    print("Distance to reach this Root : "+ str(poo[v]))
                    print("Heuristic value of this Root : "+ str(self.h(v)))
                    print("Currently in list, n : "+ str(n))
                    print("Higher value : "+str())
                    n = v;
                    print("Newly added in list to traverse : "+ str(n))
                    print(".................................")
            print("******************************************************")


            if n == None:
                print('Path does not exist!') #not work for this input
                return None

            # if the current node is the stop
            # then we start again from start

            if n == stop:
                reconst_path = []
                print("--------------------------------------------------")

                while par[n] != n: #E != Z

                    print("Perent of "+ str(n) + " : "+str(par[n]))
                    reconst_path.append(n)
                    print("path : "+ str(reconst_path))
                    n = par[n]

                reconst_path.append(start)
                print("Adding root to path : "+ str(reconst_path))

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                print("--------------------------------------------------")
                return reconst_path


            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    print("neighbor of "+str(n)+" : "+ str(m))
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                    print("actual distance from "+n+" to "+m+" is : "+str(weight))
                    print("Total distance from source : "+str(poo[m]))
                    print("++++++++++++++++++++++++++++++++++++++++++++++")

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                    print("neighbor of "+str(n)+" : "+ str(m))
                    print("Previous distance to reach "+str(m)+" : "+ str(poo[m]))
                    print("Distance to reach "+str(n)+" : "+ str(poo[n]))
                    print("actual distance from "+n+" to "+m+" is : "+str(weight))
                    print("Estemated New distance to reach "+str(m)+" : "+ str(poo[n]+weight))
                    if poo[m] > poo[n] + weight:
                        print("-_-_-_-_-_-_-_-_{}_-_-_-_-_-_-_-_-_-_-_")
                        print("neighbor of "+str(n)+" : "+ str(m))
                        print("Previous distance to reach "+str(m)+" : "+ str(poo[m]))
                        print("Distance to reach "+str(n)+" : "+ str(poo[n]))
                        print("actual distance from "+n+" to "+m+" is : "+str(weight))
                        poo[m] = poo[n] + weight
                        par[m] = n
                        print("Actual New distance to reach "+str(m)+" : "+ str(poo[m]))
                        print("-_-_-_-_-_-_-_-_{}_-_-_-_-_-_-_-_-_-_-_")

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
                            print("====================================")

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
            print("||||||||||||||||||||||||||||||")

        print('Path does not exist!')
        return None

adjac_lis = {
    'A': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'E': [('Z',5)],
    'F': [('Z',16)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'Z')




##from collections import deque
##
##class Graph:
##    def __init__(self, adjac_lis):
##        self.adjac_lis = adjac_lis
##
##    def get_neighbors(self, v):
##        return self.adjac_lis[v]
##
##    # This is heuristic function which is having equal values for all nodes
##    def h(self, n):
##        H = {
##            'A': 14,
##            'B': 12,
##            'C': 11,
##            'D': 6,
##            'E': 4,
##            'F': 11,
##            'Z': 0
##        }
##
##        return H[n]
##
##    def a_star_algorithm(self, start, stop):
##        open_lst = set([start])
##        closed_lst = set([])
##
##        poo = {}
##        poo[start] = 0
##
##        par = {}
##        par[start] = start
##
##        while len(open_lst) > 0:
##            n = None
##
##            for v in open_lst:
##                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
##                    n = v;
##
##            if n == None:
##                print('Path does not exist!')
##                return None
##
##            if n == stop:
##                reconst_path = []
##
##                while par[n] != n:
##                    reconst_path.append(n)
##                    n = par[n]
##
##                reconst_path.append(start)
##
##                reconst_path.reverse()
##
##                print('Path found: {}'.format(reconst_path))
##                return reconst_path
##
##            for (m, weight) in self.get_neighbors(n):
##
##                if m not in open_lst and m not in closed_lst:
##                    open_lst.add(m)
##                    par[m] = n
##                    poo[m] = poo[n] + weight
##
##                else:
##                    if poo[m] > poo[n] + weight:
##                        poo[m] = poo[n] + weight
##                        par[m] = n
##
##                        if m in closed_lst:
##                            closed_lst.remove(m)
##                            open_lst.add(m)
##
##            open_lst.remove(n)
##            closed_lst.add(n)
##
##        print('Path does not exist!')
##        return None
##
##adjac_lis = {
##    'A': [('B', 4), ('C', 3)],
##    'B': [('F', 5), ('E', 12)],
##    'C': [('D', 7), ('E', 10)],
##    'D': [('E', 2)],
##    'E': [('Z',5)],
##    'F': [('Z',16)]
##}
##graph1 = Graph(adjac_lis)
##graph1.a_star_algorithm('A', 'Z')
