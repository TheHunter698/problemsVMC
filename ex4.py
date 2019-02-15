#To know if they form a new rectangle inside of both we have to calculate
#If any vector has an intersection, means that both have a common point

#Test rectangles
rectangle1 = dict(
    xLeft = 1,
    yBottom = 1,
    
    width = 3,
    height = 2,
)

rectangle2 = dict(
    xLeft = 3,
    yBottom = 2,

    width = 2,
    height = 3,
)

def calculate_area(r1, r2):
    totalArea = (r1[height] * r1[width]) + (r2[height] * r2[width])
    
    #Calculating differences in x and y 
    dx = (r1.xLeft + r1.width, r2.xLeft + r2.width) - (r1.xLeft, r2.xLeft)
    dy = (r1.yBottom + r1.height, r2.yBottom + r2.height) - (r1.yBottom, r2.yBottom)
    
    #Calculating the area of that difference which will result in the area of the intersection
    intersectionArea = dx*dy

    totalArea = totalArea - intersectionArea
    print('Total Area is ' + totalArea + ' !')
    return totalArea

calculate_area(rectangle1, rectangle2)

