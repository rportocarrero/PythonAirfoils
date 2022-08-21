# this function takes a set of points representing a wing half and calculates it's surface area and aspect ratio

def wingArea(points):
    """
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]
    p4 = points[3]
    
    a1 = p3[0] * (p2[1] + p3[1])/2
    a2 = p4[0] * (p4[1])/2
    
    return a1 - a2
    
    """
    # find area
    area = 0
        
    previous_x = 0
    previous_y = 0
    
    points.append([0,0]) # to close the polygon
    
    for point in points:
        x = point[0]
        y = point[1]
        
        b = abs(x - previous_x)  # x should never be negative
        h = (y + previous_y)/2
        
        if x < previous_x:
            area -= b*h
        else:
            area += b*h
        
        previous_x = x
        previous_y = y

    return area
