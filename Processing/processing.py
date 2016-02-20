from collections import defaultdict
def sort_data(data):
    """

    :param data:
    :return:
    """
    mat_to_card_ranking = defaultdict(list)
    for mat in data.keys():
        for card, ranks in mat.items():
            average_rank = float(sum(ranks))/len(ranks)
            mat_to_card_ranking[mat].append(card, average_rank)
    return mat_to_card_ranking

