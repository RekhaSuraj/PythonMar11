# Nested dictionary
#
# nd = {key:{key:value},
#       key:{key:value},
#       key:{key:value}
#     }

nd1 = {1:{2:'cat'},
       2:{3:'dog',4:'Cow'},
       3:{5:'Sheep',6:'Goat'}

}

print(nd1[2].keys())
# dict_keys([3, 4])

print(nd1[2][3])
# dog

print(nd1.keys())
# dict_keys([1, 2, 3])

print(nd1[1].keys())
# dict_keys([2])

print(nd1[1].items())
# dict_items([(2, 'cat')])

print(nd1[3])
# {5: 'Sheep', 6: 'Goat'}
print(nd1[3].items())
# dict_items([(5, 'Sheep'), (6, 'Goat')])

print(nd1[3][6])
# Goat




