import sqlite3

conn = sqlite3.connect('spiderdb.sqlite')
cur = conn.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
# SELECT DISTINCT ignores duplicates
cur.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list()
for row in cur: 
    from_ids.append(row[0])

# Find the ids that receive page rank
# This is a filter of links with From-id pointing to To-id
to_ids = list()
links = list()
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
for row in cur:
    from_id = row[0]
    to_id = row[1]
    #Non interesting items
    if from_id == to_id: continue
    if from_id not in from_ids: continue
    #We don't want links that point to nowhere (not retrieved pages)
    if to_id not in from_ids: continue
    links.append(row)
    if to_id not in to_ids : to_ids.append(to_id)

# Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))
    row = cur.fetchone()
    prev_ranks[node] = row[0]

sval = input('How many iterations:')
many = 1
if (len(sval) > 0): many = int(sval)

# Sanity check
if len(prev_ranks) < 1 : 
    print("Nothing to page rank. Check data.")
    quit()

# Lets do 4_Page Rank in memory so it is really fast
for i in range(many):
    # print prev_ranks.items()[:5]
    next_ranks = dict();
    total = 0.0
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        # print node, old_rank

        #give_ids is a List of outbounding id of the Node that is sharing th goodness
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node: continue
           #  print '   ',from_id,to_id

            if to_id not in to_ids: continue
            give_ids.append(to_id)
        if (len(give_ids) < 1) : continue
        #Calculating how much we're giving in our outgoing link
        amount = old_rank / len(give_ids)
        # print node, old_rank,amount, give_ids

        #Giving fractional bits of our current goodness and accumulate it
        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank

    #Attributing an evaporative factor avoiding PageRank could be trapped in some dysfunctional shapes
    evap = (total - newtot) / len(next_ranks)

    # print newtot, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank

    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    # Tell us about the stability of the page rank
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff

    avediff = totdiff / len(prev_ranks)
    print(i+1, avediff)

    # rotate
    prev_ranks = next_ranks

# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in list(next_ranks.items()) :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()

