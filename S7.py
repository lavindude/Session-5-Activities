'''
Problem 1: Combine 2 lists to make a dictionary, make it as dynamic as possible
i.e. : Make it so the program would work if you added more values to the lists.
'''

word_numbers = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty']
nums = [10, 20, 30, 40, 50]

combined = dict()
counter = 0
for i in range(0, len(word_numbers)):
    combined[word_numbers[i]] = nums[i]

print(combined)


''' 
Problem 2: List of dictionaries, find the shortest state name. If there are multiple names with 
           the same length, just pick one of them. Just like the last problem, try to make it
           dynamic so any number of states would work.
'''

states = [
    {
        "name": "Alabama",
        "abbreviation": "AL"
    },
    {
        "name": "Alaska",
        "abbreviation": "AK"
    },
    {
        "name": "American Samoa",
        "abbreviation": "AS"
    },
    {
        "name": "Arizona",
        "abbreviation": "AZ"
    },
    {
        "name": "Arkansas",
        "abbreviation": "AR"
    },
    {
        "name": "California",
        "abbreviation": "CA"
    }
]

shortest_len = len(states[0]['name'])
shortest_word = ''
for item in states:
    if len(item['name']) < shortest_len:
        shortest_len = len(item['name'])
        shortest_word = item['name']

print(shortest_word, 'is the shortest state name with', shortest_len, 'letters.')
