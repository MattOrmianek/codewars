"""
Given the lists with suppliers' production, consumers' demand, and the matrix of supplier-to-consumer transportation costs, calculate the minimum cost of the products transportation which satisfied all the demand.

Notes
Costs-matrix legend: costs[i][j] is the cost of transporting 1 unit of produce from suppliers[i] to consumers[j]

The produce is identical - multiple suppliers can be the source for one consumer, and multiple consumers can be the target of one supplier

The produce is not important - it can be anything and have any price, we're only interested in transporting it efficiently

Total supply will always equal total demand

Your solution should pass 12 cases with matrices of size 150x150 as a performance test (the reference solution itself takes ~8500 ms to do so)

For all tests, 0 <= costs[i][j] <= 100

In performance tests, 1 <= suppliers[i], consumers[j] <= 10000

Disabled modules are scipy and sklearn

Disabled built-in functions are open, exec, eval, globals, locals and exit

Example
Given these inputs:

suppliers = [10, 20, 20]

consumers = [5, 25, 10, 10]

costs =
    [2  5  3  0]
    [3  4  1  4]
    [2  6  5  2]
The shipments can be arranged the following way:

[            10]  | 10
[    10  10    ]  | 20
[ 5  15        ]  | 20
------------------+---
  5  25  10  10   |
By multiplying each element of this matrix by the corresponding element of the costs matrix, we get the result:

[             0]
[    40  10    ]  =>  0 + 40 + 10 + 10 + 90 = 150
[10  90        ]
"""

from collections.abc import Callable
import sys
import heapq



def minimum_transportation_price(suppl):
    sys.setrecursionlimit(1 << 25)

    N_suppliers = int(sys.stdin.readline())
    suppliers = list(map(int, sys.stdin.readline().split()))
    N_consumers = int(sys.stdin.readline())
    consumers = list(map(int, sys.stdin.readline().split()))
    N = N_suppliers + N_consumers + 2  # Including source (s) and sink (t)
    costs = []
    for _ in range(N_suppliers):
        costs.append(list(map(int, sys.stdin.readline().split())))

    s = 0
    t = N - 1
    graph = [[] for _ in range(N)]

    class Edge:
        def __init__(self, to, rev, capacity, cost):
            self.to = to
            self.rev = rev
            self.capacity = capacity
            self.cost = cost
            self.flow = 0

    INF = float('inf')

    # Add edge function
    def add_edge(frm, to, capacity, cost):
        forward = Edge(to, len(graph[to]), capacity, cost)
        backward = Edge(frm, len(graph[frm]), 0, -cost)
        graph[frm].append(forward)
        graph[to].append(backward)

    # Build the graph
    # From source to suppliers
    for i in range(N_suppliers):
        add_edge(s, 1 + i, suppliers[i], 0)

    # From suppliers to consumers
    for i in range(N_suppliers):
        for j in range(N_consumers):
            cost = costs[i][j]
            add_edge(1 + i, 1 + N_suppliers + j, float('inf'), cost)

    # From consumers to sink
    for j in range(N_consumers):
        add_edge(1 + N_suppliers + j, t, consumers[j], 0)

    # Min-cost Max-flow using SSP algorithm
    total_cost = 0
    potential = [0] * N  # For reducing edge costs

    while True:
        dist = [INF] * N
        dist[s] = 0
        hq = [(0, s)]
        prevnode = [None] * N
        prevedge = [None] * N
        while hq:
            d, u = heapq.heappop(hq)
            if dist[u] < d:
                continue
            for i, e in enumerate(graph[u]):
                if e.capacity > e.flow:
                    v = e.to
                    cost = e.cost + potential[u] - potential[v]
                    if dist[v] > dist[u] + cost:
                        dist[v] = dist[u] + cost
                        prevnode[v] = u
                        prevedge[v] = i
                        heapq.heappush(hq, (dist[v], v))
        if dist[t] == INF:
            break  # No more augmenting paths
        # Update potentials
        for i in range(N):
            if dist[i] < INF:
                potential[i] += dist[i]
        # Determine the amount by which we can augment the flow
        d = INF
        v = t
        while v != s:
            u = prevnode[v]
            e = graph[u][prevedge[v]]
            d = min(d, e.capacity - e.flow)
            v = u
        # Augment flow and update costs
        v = t
        while v != s:
            u = prevnode[v]
            e = graph[u][prevedge[v]]
            e.flow += d
            graph[v][e.rev].flow -= d
            total_cost += e.cost * d
            v = u

    print(int(total_cost))
    return int(total_cost)







#def minimum_transportation_price(suppliers, consumers, costs):
#    n = len(suppliers)
#    m = len(consumers)

#    # Make copies to preserve the original inputs
#    suppliers_copy = suppliers[:]
#    consumers_copy = consumers[:]

#    # Initialize result matrix
#    result = [[0 for _ in range(m)] for _ in range(n)]

#    # While there are supplies and demands to satisfy
#    while sum(suppliers_copy) > 0 and sum(consumers_copy) > 0:
#        # Calculate penalties for rows and columns
#        row_penalties = []
#        for i in range(n):
#            if suppliers_copy[i] == 0:
#                row_penalties.append(None)
#                continue
#            costs_row = [costs[i][j] for j in range(m) if consumers_copy[j] > 0]
#            if len(costs_row) >= 2:
#                sorted_costs = sorted(costs_row)
#                penalty = sorted_costs[1] - sorted_costs[0]
#            elif len(costs_row) == 1:
#                penalty = float('inf')  # Assign high penalty
#            else:
#                penalty = None
#            row_penalties.append(penalty)

#        col_penalties = []
#        for j in range(m):
#            if consumers_copy[j] == 0:
#                col_penalties.append(None)
#                continue
#            costs_col = [costs[i][j] for i in range(n) if suppliers_copy[i] > 0]
#            if len(costs_col) >= 2:
#                sorted_costs = sorted(costs_col)
#                penalty = sorted_costs[1] - sorted_costs[0]
#            elif len(costs_col) == 1:
#                penalty = float('inf')  # Assign high penalty
#            else:
#                penalty = None
#            col_penalties.append(penalty)

#        # Find the maximum penalty value
#        max_penalty_value = max([p for p in row_penalties + col_penalties if p is not None])

#        # Collect indices with maximum penalty
#        max_rows = [i for i, p in enumerate(row_penalties) if p == max_penalty_value]
#        max_cols = [j for j, p in enumerate(col_penalties) if p == max_penalty_value]

#        # For each candidate cell, find the minimal cost
#        min_cost = float('inf')
#        min_cell = (None, None)
#        for i in max_rows:
#            for j in range(m):
#                if consumers_copy[j] > 0 and costs[i][j] < min_cost:
#                    min_cost = costs[i][j]
#                    min_cell = (i, j)
#        for j in max_cols:
#            for i in range(n):
#                if suppliers_copy[i] > 0 and costs[i][j] < min_cost:
#                    min_cost = costs[i][j]
#                    min_cell = (i, j)

#        i, j = min_cell

#        # Allocate as much as possible
#        min_val = min(suppliers_copy[i], consumers_copy[j])
#        result[i][j] = min_val

#        # Update remaining supply and demand
#        suppliers_copy[i] -= min_val
#        consumers_copy[j] -= min_val

#    # Calculate total cost
#    total_cost = 0
#    for i in range(n):
#        for j in range(m):
#            total_cost += result[i][j] * costs[i][j]
#    print(result)
#    return total_cost


def test_function(f: Callable) -> None:
    # Test case 1
    suppliers = [10, 20, 20]
    consumers = [5, 25, 10, 10]
    costs = [
        [2, 5, 3, 0],
        [3, 4, 1, 4],
        [2, 6, 5, 2]
    ]
    assert f(suppliers, consumers, costs) == 150, "Test case 1 failed"

    # Test case 2
    suppliers = [8, 15, 21]
    consumers = [8, 36]
    costs = [
        [9, 16],
        [7, 13],
        [25, 1]
    ]
    assert f(suppliers, consumers, costs) == 288, "Test case 2 failed"

    suppliers = [13, 44, 27, 39, 17]
    consumers = [28, 12, 30, 17, 19, 34]
    costs = [
        [6, 6, 12, 8, 13, 13],
        [7, 20, 5, 16, 11, 16],
        [4, 6, 19, 0, 2, 18],
        [1, 16, 6, 11, 8, 11],
        [5, 6, 11, 1, 6, 14]
    ]
    assert f(suppliers, consumers, costs) == 759, "Test case 3 failed " +str(f(suppliers, consumers, costs))
    print("All tests passed")

if __name__ == "__main__":
    test_function(minimum_transportation_price)
