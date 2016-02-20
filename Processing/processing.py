import collections
from Ranking import models

def card_rank(input_json):
    '''
    Takes the input json data and turns into readable data for averaging function

    :param input_json: the input json from when the cards are sorted
    :return: a dictionary of mats mapped to each cards mapped to list of rankings
    '''

    #Initialize output variables
    mat_data = {}

    #Initialize all of the mat dictionaries
    for idx in range(input_json['submissions']):
        # print 'user: ', user
        # mat_dict = input_json[user]

        # for card_val in submission:
            # print 'Mat: ', mat
        mat_data[idx] = collections.defaultdict(list)

    #Reorganize data into output dictionary
    for idx in range(input_json['submissions']):
        # print 'user: ', user
        # mat_dict = input_json[user]
        #
        # for mat in mat_dict.keys():
        #     print 'Mat: ', mat
        #     card_dict = mat_dict[mat]
        submission = input_json['submissions'][idx]
            #collect ranks for each card
        for card_val in submission:
            for card in card_val.keys():
                mat_data[idx][card].append(card_val[card])

    return mat_data

#Testing
input_json = {"themes": ["Robotics", "Sewing", "Commercial Kitchen", "Place to make new products", "Woodworking",
                         "Focus on future tools", "Inter-age activities", "tools", "Quite Classroom", "Machinery",
                         "Metalworking", "Different short classes", "Art Space", "Focus on youth", "Shared knowledge",
                         "Electronics", "Skilled tutors", "Computer Skills", "Jewelery making"],
              "submissions": [[{"Robotics": 4}, {"Sewing": 5}, {"Commercial Kitchen": 1}, {"Place to make new products": 4},
                               {"Woodworking": 2}, {"Focus on future tools": 3}, {"Inter-age activities": 4}, {"tools": 3},
                               {"Quite Classroom": 5}, {"Machinery": 3}, {"Metalworking": 3}, {"Different short classes": 3}, {"Art Space": 2}, {"Focus on youth": 2}, {"Shared knowledge": 1}, {"Electronics": 2}, {"Skilled tutors": 4}, {"Computer Skills": 3}, {"Jewelery making": 3}], [{"Robotics": 2}, {"Sewing": 2}, {"Commercial Kitchen": 3}, {"Place to make new products": 1}, {"Woodworking": 1}, {"Focus on future tools": 2}, {"Inter-age activities": 4}, {"tools": 3}, {"Quite Classroom": 4}, {"Machinery": 4}, {"Metalworking": 3}, {"Different short classes": 3}, {"Art Space": 3}, {"Focus on youth": 3}, {"Shared knowledge": 5}, {"Electronics": 4}, {"Skilled tutors": 2}, {"Computer Skills": 5}, {"Jewelery making": 3}], [{"Robotics": 4}, {"Sewing": 2}, {"Commercial Kitchen": 3}, {"Place to make new products": 3}, {"Woodworking": 4}, {"Focus on future tools": 3}, {"Inter-age activities": 5}, {"tools": 4}, {"Quite Classroom": 2}, {"Machinery": 3}, {"Metalworking": 1}, {"Different short classes": 3}, {"Art Space": 5}, {"Focus on youth": 2}, {"Shared knowledge": 3}, {"Electronics": 2}, {"Skilled tutors": 3}, {"Computer Skills": 1}, {"Jewelery making": 4}], [{"Robotics": 5}, {"Sewing": 2}, {"Commercial Kitchen": 4}, {"Place to make new products": 3}, {"Woodworking": 2}, {"Focus on future tools": 3}, {"Inter-age activities": 3}, {"tools": 4}, {"Quite Classroom": 2}, {"Machinery": 3}, {"Metalworking":4}, {"Different short classes": 3}, {"Art Space": 4}, {"Focus on youth": 3}, {"Shared knowledge": 5}, {"Electronics": 2}, {"Skilled tutors": 1}, {"Computer Skills": 1}, {"Jewelery making": 3}], [{"Robotics": 2}, {"Sewing": 3}, {"Commercial Kitchen": 4}, {"Place to make new products": 3}, {"Woodworking": 3}, {"Focus on future tools": 4}, {"Inter-age activities": 5}, {"tools": 2}, {"Quite Classroom": 3}, {"Machinery": 4}, {"Metalworking": 1}, {"Different short classes": 1}, {"Art Space": 2}, {"Focus on youth": 4}, {"Shared knowledge": 3}, {"Electronics": 5}, {"Skilled tutors": 3}, {"Computer Skills": 2}, {"Jewelery making": 3}], [{"Robotics": 3}, {"Sewing": 4}, {"Commercial Kitchen": 4}, {"Place to make new products": 3}, {"Woodworking": 4}, {"Focus on future tools": 5}, {"Inter-age activities": 2}, {"tools": 3}, {"Quite Classroom": 2}, {"Machinery": 3}, {"Metalworking": 2}, {"Different short classes": 1}, {"Art Space": 3}, {"Focus on youth": 2}, {"Shared knowledge": 3}, {"Electronics": 1}, {"Skilled tutors": 4}, {"Computer Skills": 5}, {"Jewelery making": 3}], [{"Robotics": 3}, {"Sewing": 1}, {"Commercial Kitchen": 3}, {"Place to make new products": 3}, {"Woodworking": 4}, {"Focus on future tools": 4}, {"Inter-age activities": 2}, {"tools": 5}, {"Quite Classroom": 4}, {"Machinery": 4}, {"Metalworking": 3}, {"Different short classes": 2}, {"Art Space": 2}, {"Focus on youth": 1}, {"Shared knowledge": 2}, {"Electronics": 5}, {"Skilled tutors": 3}, {"Computer Skills": 3}, {"Jewelery making":3}], [{"Robotics": 3}, {"Sewing": 2}, {"Commercial Kitchen": 3}, {"Place to make new products": 5}, {"Woodworking": 2}, {"Focus on future tools": 4}, {"Inter-age activities": 1}, {"tools": 4}, {"Quite Classroom": 3}, {"Machinery": 1}, {"Metalworking": 5}, {"Different short classes": 3}, {"Art Space": 4}, {"Focus on youth": 3}, {"Shared knowledge": 2}, {"Electronics": 2}, {"Skilled tutors": 3}, {"Computer Skills": 3}, {"Jewelerymaking": 4}], [{"Robotics": 4}, {"Sewing": 3}, {"Commercial Kitchen": 3}, {"Place to make new products": 3}, {"Woodworking": 3}, {"Focus on future tools": 5}, {"Inter-age activities": 4}, {"tools": 2}, {"Quite Classroom": 3}, {"Machinery": 4}, {"Metalworking": 1}, {"Different short classes": 2}, {"Art Space": 3}, {"Focus on youth": 1}, {"Shared knowledge": 3}, {"Electronics": 4}, {"Skilled tutors": 2}, {"Computer Skills": 2}, {"Jewelery making": 5}], [{"Robotics": 2}, {"Sewing": 3}, {"Commercial Kitchen": 3}, {"Place to make new products": 5}, {"Woodworking": 2}, {"Focus on future tools": 5}, {"Inter-age activities": 3}, {"tools": 4}, {"Quite Classroom": 4}, {"Machinery": 3}, {"Metalworking": 4}, {"Different short classes": 3}, {"Art Space": 2}, {"Focus on youth": 3}, {"Shared knowledge": 1}, {"Electronics": 3}, {"Skilled tutors": 4}, {"Computer Skills": 2}, {"Jewelery making": 1}]], "description": "Let us make things together", "title": "Maker Space"}



print card_rank(input_json)



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
    mat_to_card_ranking = collections.defaultdict(list)

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

# def process_data():
#     mats = gather_mats()
#     card_ranks = card_rank(mats)
#     avg_ranks = sort_data(card_ranks)
#     return avg_ranks
