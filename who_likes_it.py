# You probably know the "like" system from Facebook
#  and other pages. People can "like" blog posts,
#   pictures or other items. We want to create the
#    text that should be displayed next to such an item.

# Implement the function which takes an array containing
#  the names of people that like an item. It must return
#   the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Note: For 4 or more names, the number in "and 2 others" simply increases.

# def likes(l):
#     n= len(l)
#     if n == 0:
#        return 'no one likes this'
#     elif n == 1:
#         return f'{l[0]} likes this'
#     elif n == 2:
#         return f'{l[0]} and {l[1]} like this'
#     elif n == 3:
#         return f'{l[0]}, {l[1]} and {l[3]} like this'
#     else:
#         return f'{l[0]}, {l[1]} and {n - 2} others like this'

# Codewars
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

names = ["Alex", "Jacob"]
n = len(names)
print('{}, {} and {others} others like this'.format(*names[:3], others=n-2))