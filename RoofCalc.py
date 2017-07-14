import math

def areaOfCone(radius, height):
    # calculate the area of a conical roof
    length= math.sqrt((height**2 + radius**2))
    area = math.pi * radius * length
    return area;

def areaOfPyramid4(length, width, height):
    # calculate the area of a 4-sided pyramidal roof
    area = (length * math.sqrt(((width/2)**2)+height**2)) + (width * math.sqrt(((length/2)**2)+height**2))
    return area;

def areaOfPyramid3(side, height):
    # calculate the area of a 3-sided pyramidal roof
    area = 3 * side * height / 2
    return area;

def areaOfGableRoof(length, width, slope):
    # calculate the area of a 2-sided roof
    slant = (1 / math.cos(math.radians(slope))) * (width/2)
    #height = (1 / math.sin(math.radians(slope))) * (width/2)
    area = (length * slant * 2)
    return area;

def areaOfHipRoof(length, width, slope):
    # calculate the area of a 4-sided roof with equal slopes
    slant = (1 / math.cos(math.radians(slope))) * (width/2)
    #height = (1 / math.sin(math.radians(slope))) * (width/2)
    area = (length * slant * 2)
    return area;

def areaOfHipRoof2(length, width, slopeL, slopeW):
    # calculate the area of a 4-sided roof with two different slopes
    slant = (1 / math.cos(math.radians(slope))) * (width/2)
    height = (1 / math.sin(math.radians(slope))) * (width/2)
    area = (length * slant * 2)
    return area;

def degToPercent(deg):
    # takes degrees of slope, returns percent slope
    rad = math.radians(deg)
    percent = math.tan(rad)*100
    return percent;

def percentToDeg(per):
    # takes percent slope, returns degree of slope
    deg = math.degrees(math.atan(per/100))
    return deg;

