import json
import collections

def card_rank(input_json):

    card_ranks = collections.defaultdict(list)
    for user in input_json.keys():
        mat_dict = input_json[user]
        for mat in mat_dict.keys():
            card_dict = mat_dict[mat]
            for card in card_dict.keys():
                card_ranks[card].append(card_dict[card])

