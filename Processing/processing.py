<<<<<<< HEAD
import json
import collections

def card_rank(input_json):
    '''
    Takes the input json data and turns into readable data for averaging function

    :param input_json: the input json from when the cards are sorted
    :return: a dictionary of mats mapped to each cards mapped to list of rankings
    '''

    #Initialize output variables
    mat_data = {}

    #Initialize all of the mat dictionaries
    for user in input_json.keys():
        print 'user: ', user
        mat_dict = input_json[user]

        for mat in mat_dict.keys():
            # print 'Mat: ', mat
            mat_data[mat] = collections.defaultdict(list)

    #Reorganize data into output dictionary
    for user in input_json.keys()
        print 'user: ', user
        mat_dict = input_json[user]

        for mat in mat_dict.keys():
            print 'Mat: ', mat
            card_dict = mat_dict[mat]

            #collect ranks for each card
            for card in card_dict.keys():
                mat_data[mat][card].append(card_dict[card])

    return mat_data

#Testing
input_json = {'user1': {'mat1': {'card1': 1, 'card2': 2}, 'mat2': {'card4': 4, 'card5': 5}},
              'user2': {'mat1': {'card1': 3, 'card2': 2}, 'mat2': {'card4': 3, 'card5': 4}},
              'user3': {'mat1': {'card1': 2, 'card2': 3}, 'mat2': {'card4': 5, 'card5': 3}}}

print card_rank(input_json)



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

