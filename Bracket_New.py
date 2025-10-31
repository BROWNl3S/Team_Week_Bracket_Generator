import math as m

def generator(team_sizes):

    teams=[]
    for team, size in enumerate(team_sizes):
        teams.extend(names[team] for _ in range(size))

    if len(teams) == 0:
        return([],[])

    R1=[]
    
    split(teams,R1)

    return(R1)

def split(teams,R1,index=0,depth=0):
    if len(teams)==0:
        return
    if len(teams)==1:
        R1.extend([[teams[0],'Bye'],depth])
        return
    if len(teams)==2:
        R1.extend([teams,depth])
        return
    
    total = len(teams)
    half1_size = total//2

    team_counts = {}
    for t in teams:
        team_counts[t] = team_counts.get(t, 0) + 1

    h1 = []
    h2 = []

    # Distribute each team, ensuring we hit the target half size
    for team_num in sorted(team_counts.keys(),key=lambda x:x[1]):
        count = team_counts[team_num]
        
        remaining_h1 = half1_size - len(h1)
        remaining_h2 = total - half1_size - len(h2)
        
        # Try to split evenly, but respect remaining space
        ideal_to_h1 = (count + ((team_num.lower()[0].encode()[0] + index) % 2)) // 2
    
        
        # Clamp to available space
        to_h1 = min(ideal_to_h1, remaining_h1)
        to_h1 = max(to_h1, count - remaining_h2)
        
        h1.extend([team_num] * to_h1)
        h2.extend([team_num] * (count - to_h1))

    split(h1,R1,index+1,depth+1)
    split(h2,R1,index+2,depth+1)


team_sizes=[]
names=['Vampires','Witches','Zombies','Teamless']

team_sizes.append(int(input('How many Vampires are there?:')))
team_sizes.append(int(input('How many Witches are there?:')))
team_sizes.append(int(input('How many Zombies are there?:')))
team_sizes.append(int(input('How many Teamless are there?:')))


round1 = generator(team_sizes)
round1_size = len(round1)//2

bracket_size = m.floor(m.log2(sum(team_sizes)))

TR1=[]
for e, match in enumerate(round1):

    if e%2==1:
        if match==bracket_size:
            TR1.extend(round1[e-1])
        else:
            TR1.extend([round1[e-1][0],'bye'])
            TR1.extend([round1[e-1][1],'bye'])

TR1_size = len(TR1)//2

print('')
print('Bracket')
for i in range (TR1_size):
    print(f'Match{i+1}: {TR1[2*i]} vs {TR1[2*i+1]}')

print('')
input('Press Enter to close')
