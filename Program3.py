def areaRectangle(length,breadth = 1):
    '''
    Objective: To compute the area of Rectangle
    Input Parameters: length,breadth - numeric value
    Return Value: area - numeric value
    '''
    area = length * breadth
    return area
def main():
    '''
    Objective: To compute the area of rectangle based on user input
    Input Parameter: None
    Return Value: None
    '''
    print('Enter the following values for rectangle:')
    lengthRect = int(input('Length: integer value:'))
    breadthRect =int(input('Breadth : integer value:'))
    areaRect = areaRectangle(lengthRect, breadthRect)
    print('Area of rectangle is',areaRect)

if __name__ == '__main__':
    main()
