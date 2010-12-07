#!/usr/bin/python

def calc_tax(inc, dep): #A
    path = [1]
    decisions = []
    bracket = 0
    if (0 < inc <= 20000): #B
        path.append(2)
        decisions.append('B')
        bracket = 1
    elif (20000 < inc <= 30000): #C
        path += [3,4]
        decisions += ['B', 'C']
        bracket = 2
    elif (30000 < inc <= 40000): #D
        path += [3,5,6]
        decisions += ['B', 'C', 'D']
        bracket = 3
    elif (40000 < inc <= 50000): #E
        path += [3,5,7,8]
        decisions += ['B', 'C', 'D', 'E']
        bracket = 4
    elif (50000 < inc <= 90000): #F
        path += [3,5,7,9,10]
        decisions += ['B', 'C', 'D', 'E', 'F']
        bracket = 5
    else: 
        path += [3,5,7,9,11]
        decisions += ['B', 'C', 'D', 'E', 'F']
        bracket = 6

    def switch(x): #G
        decisions.append('G')
        if x == 1:
            path.append(13)
            tax = inc * .04 #H
        elif x == 2:
            path.append(14)
            tax = inc * .05 #I
        elif x == 3:
            path.append(15)
            tax = inc * .06 #J
        elif x == 4:
            path.append(16)
            tax = inc * .07 #K
        elif x == 5:
            path.append(17)
            tax = inc * .10 #L
        elif x == 6:
            path.append(18)
            tax = inc * .13 #M
        else: #N
            path.append(19)
            print "something is wrong with the income bracket computation" #O
        return tax
    
    path.append(12)    
    tax = switch(bracket)

    path.append(20)
    if (dep == 1): #O
        path.append(21)
        decisions.append('O')
        tax = tax - (.1 * tax)
    elif (2 <= dep <= 3): #P
        path += [22,23]
        decisions += ['O', 'P']
        tax = tax - (.25 * tax)
    elif (3 < dep): #Q
        path += [22,24,25]
        decisions += ['O', 'P', 'Q']
        tax = tax - (.4 * tax)
    else:
        decisions += ['O', 'P', 'Q']
        path += [22,24,26]
        tax = tax

    path.append(27)
    print "income = {0} dependent = {1} tax = {2}".format(inc, dep, tax) #R

    return (inc, dep, path, decisions)
        
def do_test(test_cases):
    decisions_hit = {
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'P': 0,
        'Q': 0,
        }
    edges_hit = dict.fromkeys(range(1,28), 0)

    for case in test_cases:
        result = calc_tax(case[0], case[1])
        edges = result[2]
        decisions = result[3]
        print "inc: {0}, dep: {1}, edges: {2}, decisions: {3}".format(result[0], result[1], result[2], result[3])
        for x in edges:
            if x in edges_hit:
                edges_hit[x] += 1

        for x in decisions:
            if x in decisions_hit:
                decisions_hit[x] += 1

    
                
    print 'Number of test cases: ', len(test_cases)

    missed_edges = edges_hit.values().count(0)
    print "{0} of {1} edges hit ({2:.1%})".format(
        len(edges_hit) - missed_edges,
        len(edges_hit),
        float( (len(edges_hit) - missed_edges) ) / float( len(edges_hit) ))
    print "{0} edges hit, {1} unique edges hit. {2:.1%} efficiency".format(
        sum(edges_hit.values()),
        len(edges_hit) - missed_edges,
        float( (len(edges_hit) - missed_edges) ) / float( sum(edges_hit.values()) ))
    edges_missed = []
    for x in edges_hit.iteritems():
        if x[1] == 0:
            edges_missed.append(x[0])
    print "Edges missed: ", edges_missed

    missed_decisions = decisions_hit.values().count(0)
    print "{0} of {1} decisions hit ({2:.1%})".format(
        len(decisions_hit) - missed_decisions,
        len(decisions_hit),
        float( (len(decisions_hit) - missed_decisions) ) / float( len(decisions_hit) ))
    print "{0} decisions hit, {1} unique decisions hit. {2:.1%} efficiency".format(
        sum(decisions_hit.values()),
        len(decisions_hit) - missed_decisions,
        float( (len(decisions_hit) - missed_decisions) ) / float( sum(decisions_hit.values()) ))
    decisions_missed = []
    for x in decisions_hit.iteritems():
        if x[1] == 0:
            decisions_missed.append(x[0])
    print "Decisions missed: ", decisions_missed
    
    
    
        

if __name__ == "__main__":
    print calc_tax(20000, 1)

    test_cases = [(20000, 1),
                  (30000, 0)]
    do_test(test_cases)
