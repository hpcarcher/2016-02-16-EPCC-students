def near(first, second):
    import numpy
    tolerance = 0.1*numpy.absolute(second)
    if numpy.absolute(first-second) <= tolerance: return True
    else: return False
    
    
    
