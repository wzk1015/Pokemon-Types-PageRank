regular = [('Steel', 0.0454),
 ('Ghost', 0.0508),
 ('Fairy', 0.052),
 ('Poison', 0.0525),
 ('Electric', 0.0528),
 ('Fire', 0.0537),
 ('Normal', 0.0542),
 ('Water', 0.0549),
 ('Flying', 0.0553),
 ('Dark', 0.0563),
 ('Dragon', 0.0565),
 ('Ground', 0.0569),
 ('Bug', 0.0573),
 ('Fighting', 0.0575),
 ('Psychic', 0.0591),
 ('Rock', 0.0611),
 ('Grass', 0.0616),
 ('Ice', 0.062)]

attack = [('Ground', 0.0632),
 ('Fire', 0.0606),
 ('Rock', 0.0605),
 ('Ice', 0.0602),
 ('Water', 0.06),
 ('Fighting', 0.0582),
 ('Fairy', 0.0575),
 ('Flying', 0.0573),
 ('Steel', 0.0573),
 ('Dark', 0.057),
 ('Psychic', 0.0554),
 ('Grass', 0.0549),
 ('Electric', 0.0545),
 ('Ghost', 0.0526),
 ('Poison', 0.052),
 ('Bug', 0.0518),
 ('Dragon', 0.05),
 ('Normal', 0.0484)]

defense = [('Steel', 0.0467),
 ('Ghost', 0.0485),
 ('Fairy', 0.0525),
 ('Normal', 0.0537),
 ('Poison', 0.0538),
 ('Dragon', 0.0538),
 ('Electric', 0.0542),
 ('Fire', 0.0554),
 ('Flying', 0.0558),
 ('Water', 0.0564),
 ('Bug', 0.0574),
 ('Ground', 0.0575),
 ('Fighting', 0.058),
 ('Dark', 0.058),
 ('Psychic', 0.0606),
 ('Rock', 0.0618),
 ('Grass', 0.0634),
 ('Ice', 0.0638)]

inverse = [('Ice', 0.0471),
 ('Psychic', 0.0511),
 ('Normal', 0.0516),
 ('Bug', 0.053),
 ('Fighting', 0.0532),
 ('Rock', 0.0535),
 ('Grass', 0.0538),
 ('Ground', 0.0539),
 ('Dark', 0.0539),
 ('Flying', 0.0553),
 ('Dragon', 0.056),
 ('Ghost', 0.0561),
 ('Fairy', 0.0563),
 ('Electric', 0.0566),
 ('Water', 0.0581),
 ('Poison', 0.0585),
 ('Fire', 0.0603),
 ('Steel', 0.0716)]

attack_defense_avg = {attack[i][0]: attack[i][1] + defense[i][1] for i in range(18)}
print("average score of attack and defense:", sorted(attack_defense_avg.items(), key=lambda x:x[1]), "\n")

rank_avg = {}
for i in range(18):
    name = attack[i][0]
    for j in range(18):
        if defense[j][0] == name:
            break
    # print(name, i, j)
    rank_avg[name] = (i + j) / 2
print("average rank of attack and defense:", sorted(rank_avg.items(), key=lambda x:x[1]))