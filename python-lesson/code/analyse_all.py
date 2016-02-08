def analyse_all(filename_pattern):
    import glob
    from analyse import analyse
    datafiles = glob.glob(filename_pattern)
    for filename in datafiles:
        print filename
        analyse(filename)
        
