#simple data structure 1 parent with two children
#add
child_one = {
    'value': 50,
    'children': []
}

child_two = {
    'value':39,
    'children': []
}

root_node = {
    'value': 20,
    'children':[
        child_one,
        child_two
    ]
}
print(root_node)
child = root_node.get('children')[0]
print(child)

