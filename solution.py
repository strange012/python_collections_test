unique_names = lambda x, y: sorted(list(set(x + y)))

def group_by_owners(files):
    owners = dict()
    for key, value in files.items():
        if value not in owners.keys():
            owners[value] = []
        owners[value].append(key)
    return owners

class LeagueTable:
    
    def __init__(self, players):
        self.players = players
        self.table = dict.fromkeys(players, (0, 0))
    
    def record_result(self, name, score):
        self.table[name] = (self.table[name][0] + 1, self.table[name][1] + score)

    def player_rank(self, rank):
        return list(map(lambda x: x[0], sorted(sorted(self.table.items(), key=lambda x: x[1][0], reverse=False), key=lambda x: x[1][1], reverse=True)))[rank-1]

    def players_list(self):
        return sorted(sorted(self.table.items(), key=lambda x: x[1][0], reverse=False), key=lambda x: x[1][1], reverse=True)

def main():
    a = ['Ava', 'Emma', 'Olivia']
    b = ['Olivia', 'Sophia', 'Emma']
    print(unique_names(a, b))

    c = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    print(group_by_owners(c))

    table = LeagueTable(['Mike', 'Chris', 'Nick', 'Arnold', 'Alan', 'Penultimate guy','Last guy'])
    table.record_result('Mike', 2)
    table.record_result('Alan', 1)
    table.record_result('Alan', 4)
    table.record_result('Mike', 3)
    table.record_result('Nick', 8)
    table.record_result('Arnold', 5)
    table.record_result('Last guy', 5)
    table.record_result('Penultimate guy', 5)
    table.record_result('Chris', 5)
    table.record_result('Arnold', 1)
    for val in table.players_list():
        print(val) 

    print(table.player_rank(3))

if __name__ == "__main__":
    main()