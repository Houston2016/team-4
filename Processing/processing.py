from collections import defaultdict
def sort_data(data):
    """

    :param data:
    :return:
    """
    mat_to_card_ranking = defaultdict(list)
    for mat in data.keys():
        for card, ranks in data[mat].items():
            average_rank = float(sum(ranks))/len(ranks)
            mat_to_card_ranking[mat].append((card, average_rank))
    return mat_to_card_ranking

test = {"123123": {"1": [1,2,3,4], "2":[5,5,5,5], "3":[1,1,1,2]}}
print sort_data(test)