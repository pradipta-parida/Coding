""" Function best Practices """

''' 
Single-Responsibility Principle - A function should have one job/responsibility.
Other-wise functions are Hard to understand, Hard to maintain, Hard to reuse
'''

def calc_rect_area(length, width):
    area = length * width

calc_rect_area(13, 10)

print(area)
