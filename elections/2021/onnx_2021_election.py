global candidates

candidates = ["Brandon Allgood (Valo Heath)", "Prasanth Pulavarthi (Microsoft)", "Alexandre Eichenberger (IBM)", "Rajeev Nalawdi (Intel)", "Sonal Agrawal (Binary Fountain)", "Wenming Ye (AWS)", "Mayank Kaushik (NVIDIA)"]

# ballots
microsoft = [[8,	1,	3,	2,	8,	8,	8], [8,	1,	8,	8,	8,	8,	8], 	[7,	1,	2,	3,	6,	4,	5], [7,	1,	2,	5,	6,	4,	3], [6,	5,	5,	5,	7,	5,	5], [6,	1,	5,	4,	7,	3,	2], [2,	1,	2,	2,	3,	2,	2], [6,	1,	4,	2,	7,	5,	3]]

ibm = [[7,	2,	1,	5,	7,	5,	5], [7,	1,	2,	3,	6,	5,	4], [7,	7,	1,	7,	7,	7,	7], [7,	1,	2,	3,	7,	5,	4], [7,	2,	1,	3,	7,	4,	4], [2,	3,	1,	6,	5,	7,	4]]

nvidia = [[6,	2,	3,	5,	7,	4,	1],[3,	2,	3,	3,	3,	3,	1]]

unknown = [	[3,	1,	4,	7,	2,	5,	6], [8,	1,	8,	8,	8,	1,	8]]

facebook = [[7,	1,	2,	2,	7,	2,	2]]

mit  = [[8,	8,	1,	8,	8,	8,	8]]

amazon = 	[[4,	2,	3,	4,	4,	1,	4]]

pinduoduo  = [	[5,	7,	5,	5,	5,	6,	5]]

walgreens  =[	[4,	1,	2,	3,	6,	7,	5]]

ballots = microsoft + ibm + nvidia + unknown + facebook + mit + amazon + pinduoduo + walgreens

ballots_minus_unknown = microsoft + ibm + nvidia + facebook + mit + amazon + pinduoduo + walgreens

microsoft1=[[6,1,3,2,7,5,4]]

ibm1=[[6, 2, 1, 3, 7, 5, 4]]

nvidia1=[[6,2,3,5,7,4,1]]

unknown1=[[4, 1, 5, 7, 3, 2, 6]]

ballots_one_vote= microsoft1 + ibm1 + nvidia1 + unknown1 +  facebook + mit + amazon + pinduoduo + walgreens

ballots_one_vote_minus_unknown = microsoft1 + ibm1 + nvidia1 +  facebook + mit + amazon + pinduoduo + walgreens

# rank order
def result(ballots):
    m = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    for i in ballots:
        for j in range(7):
            for k in range(7):
                if i[k]>i[j]:
                    m[k][j]=m[k][j]+1
    for i in range(7):
        print(m[i])
    total = [0,0,0,0,0,0,0]
    for i in m:
        for j in range(7):
            total[j]=total[j]+i[j]
    print("Totals =",total)
    rank = sorted(zip(candidates,total),key=lambda record: record[1])
    for i in rank[::-1]:
        print(i[0])
    

# cases
print(" ")
print("All 23 voters")
result(ballots)
print(" ")
print("Just the 21 known voters")
result(ballots_minus_unknown)
print("Calculate Microsoft's one vote")
result(microsoft)
print("Microsoft one vote = ", microsoft1)
print(" ")
print("Calculation IBM's one vote")
result(ibm)
print("IBM one vote = ", ibm1)
print(" ")
print("Calculate NVIDIA's one vote")
result(nvidia)
print("NVIDIA one vote = ", nvidia1)
print(" ")
print("Calculate unknown's one vote")
result(unknown)
print("Unknown one vote = ", unknown1)
print(" ")
print("All 9 orgs reduced to one vote each")
result(ballots_one_vote)
print(" ")
print("Just the 8 orgs reduced to one vote each, throwing out unknown")
result(ballots_one_vote_minus_unknown)


"""
issues:
tighten up code
hardwired for 7 candidates
no opinion = 8, which is worse than last place
does not handle ties well
should read ballots from spreadsheet input file
"""


