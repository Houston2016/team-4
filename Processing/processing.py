from collections import defaultdict
def sort_data(data):
    """
    Sorts the data so that it can be visualized

    Arguments:
    data -- the data in the form of a dictionary mapping
    mat id's to a dictionary which maps card names to their
    respective ranks from different users

    Returns:
    a dictionary mapping mat ids to a list of tuples containing
    the card name and average rank in descending order
    """
    mat_to_card_ranking = defaultdict(list)
    for mat_id, mat in data.items():
        for card, ranks in mat.items():
            average_rank = float(sum(ranks))/len(ranks)
            mat_to_card_ranking[mat_id].append((card, average_rank))
    # Sorts the mat in descending order
    for mat_id, mat in mat_to_card_ranking.items():
        mat.sort(key=lambda tup: tup[1],reverse=True)
    return mat_to_card_ranking

test = {"123123": {"1": [1,2,3,4], "2":[5,5,5,5], "3":[1,1,1,2]}}
print sort_data(test)