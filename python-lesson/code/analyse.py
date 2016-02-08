def analyse(datafile):
    '''Plots, as a function of time, the mean, minimum, and maximum inflammation
    values across all patients for data contained in a file named datafile.
    
    datafile - this should be a string specifying the name of the file
               containing the inflammation data. The data is expected 
               to be in comma separated format, with each row corresponding
               to a different patient and successive columns to 
               inflammation values on successive days'''

    import numpy
    data = numpy.loadtxt(datafile, delimiter=',')
    from matplotlib import pyplot as plt

    plt.figure(figsize=(10.0, 3.0))

    plt.suptitle(datafile)    
    
    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))

    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))

    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))

    plt.tight_layout()

    plt.show(block=False)



