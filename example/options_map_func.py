from anytree import Node, RenderTree
from pickpack import pickpack

title = 'Please choose your favorite fruit: '
options = [
    { 'name': 'Apples', 'grow_on': 'trees' },
    { 'name': 'Oranges', 'grow_on': 'trees' },
    { 'name': 'Strawberries', 'grow_on': 'vines' },
    { 'name': 'Grapes', 'grow_on': 'vines' },
]



def get_description_for_display(option):
    # format the option data for display
    return Node('{0} (grow on {1})'.format(option.get('name'), option.get('grow_on')))

option, index = pickpack(options, title, indicator='=>', options_map_func=get_description_for_display)
print(option, index)
