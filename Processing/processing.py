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


