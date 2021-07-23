import errno
import os
import shutil

#PATH TO MAIN FOLDER
base = '/Users/Retina/PycharmProjects/TrainTestVal/images/flowers/'


def createTTVdirs(path, classes):
    #   print(f'createdir path {path}')

    try:
        train = path + 'train'
        test = path + 'test'
        val = path + 'val'

        os.mkdir(train)
        for i in classes:
            c = train + '/' + i
            os.mkdir(c)

        os.mkdir(test)
        for i in classes:
            c = test + '/' + i
            os.mkdir(c)

        os.mkdir(val)
        for i in classes:
            c = val + '/' + i
            os.mkdir(c)


    except OSError as exc:

    #    if exc.errno != errno.EEXIST:
    #        raise

        pass

def createClassDirs(path, classes):

    try:

        train = path + '/train/'
        test = path + '/test/'
        val = path + '/val/'

        for i in classes:
            os.mkdir(train + i)

        for i in classes:
            os.mkdir(test + i)

        for i in classes:
            os.mkdir(val + i)

    except OSError as exc:

    #    if exc.errno != errno.EEXIST:
    #        raise

        pass

def split(dir, trainsize, testsize, valsize):

    train = len(dir) * trainsize
    test = len(dir) * testsize
    val = len(dir) * valsize

    return(int(train), int(test), int(val))


def createTTVSets(path, trainsize, testsize):

    classdir = os.listdir(path)

    trainset = classdir[:trainsize]
    testset = classdir[trainsize:trainsize + testsize]
    valset = classdir[trainsize + testsize:]

    return trainset, testset, valset

def getdirs(root, path):

    dirs = [root + i for i in path]

    return dirs

#------------------------------------------------------------------------------------------#


def cleanup(classname):

    try:
        os.rmdir(base + classname)
    except OSError as e:
        print("Error: %s : %s" % (base + classname, e.strerror))


def movefiles(classname, trainset, testset, valset, path, copy):
    # MOVE THE FILES TO TRAIN, TEST & VAL FOLDERS
    train = base + '/train/' + classname
    test = base + '/test/' + classname
    val = base + '/val/' + classname

    # TRAIN
    for file in trainset:
        movefrom = path + '/' + file
        moveto = train
        if os.path.isfile(movefrom):
            if copy == False:
                shutil.move(movefrom, moveto)
            else:
                shutil.copy(movefrom, moveto)
    # TEST
    for file in testset:
        movefrom = path + '/' + file
        moveto = test
        if os.path.isfile(movefrom):
            if copy == False:
                shutil.move(movefrom, moveto)
            else:
                shutil.copy(movefrom, moveto)
    # VAL
    for file in valset:
        movefrom = path + '/' + file
        moveto = val
        if os.path.isfile(movefrom):
            if copy == False:
                shutil.move(movefrom, moveto)
            else:
                shutil.copy(movefrom, moveto)


def getbase(classdir, sizetrain, sizetest, sizeval, deletefolders=True, copy=False):

    for path in classdir:

            if os.path.basename(os.path.normpath(path)) != 'train' or 'test' or 'val':

        #GET TRAIN, TEST & VAL - SIZE. AS IN NUMBER OF FILES TO MOVE
                trainsize, testsize, valsize = split(os.listdir(path), sizetrain, sizetest, sizeval)

        #GET TRAIN, TEST, VAL - SET. LISTS OF ALL FILENAMES
                trainset, testset, valset = createTTVSets(path, trainsize, testsize)

                classname = os.path.basename(os.path.normpath(path))


            #MOVE THE FILES

                movefiles(classname, trainset, testset, valset, path, copy)

                if deletefolders:
                    cleanup(classname)


def mainrun(base):

    for root, sub, _ in (os.walk(base)):
    #        print(f'root  {root}')
        #GET FOLDERNAME OF EACH CLASS (DONE IN ITS OWN FUNCTION TO AVOID GETTING THE NEWLY CREATED 'TRAIN, TEST, VAL' FOLDERS ADDED TO THE LIST)
            classdir = getdirs(root, sub)

        #CREATE TRAIN, TEST & VAL FOLDERS IN EACH CLASS FOLDER

            createTTVdirs(base, sub)

    #        createClassDirs(base, classdir)

            return classdir


#GET PATH TO EACH CLASS FOLDER
classdir = mainrun(base)

#DIVIDE INTO TRAIN, TEST, VAL AND MOVE TO NEW FOLDERS
#SET TRAINSIZE, TESTSIZE, VALSIZE, IF ORIGINAL FOLDERS SHOULD BE DELETED, AND IF THE FILES SHOULD BE COPIED OR MOVED
getbase(classdir, 0.7, 0.15, 0.15)
