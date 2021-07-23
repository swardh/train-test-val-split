import errno
import os
import shutil

#PATH TO MAIN FOLDER
base = '/path/to'


def createTTVdirs(path):

 #   print(f'createdir path {path}')

    try:
        train = path + '/train'
        test = path + '/test'
        val = path + '/val'

        os.mkdir(train)
        os.mkdir(test)
        os.mkdir(val)

    except OSError as exc:

        if exc.errno != errno.EEXIST:
            raise

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

def mainrun(base, sizetrain, sizetest, sizeval):

    for root, sub, _ in (os.walk(base)):
        #GET FOLDERNAME OF EACH CLASS (DONE IN ITS OWN FUNCTION TO AVOID GETTING THE NEWLY CREATED 'TRAIN, TEST, VAL' FOLDERS ADDED TO THE LIST)
            classdir = getdirs(root, sub)

        #CREATE TRAIN, TEST & VAL FOLDERS IN EACH CLASS FOLDER
            for path in classdir:
                createTTVdirs(path)

        #GET TRAIN, TEST & VAL - SIZE. AS IN NUMBER OF FILES TO MOVE
                trainsize, testsize, valsize = split(os.listdir(path), sizetrain, sizetest, sizeval)

        #GET TRAIN, TEST, VAL - SET. LISTS OF ALL FILENAMES
                trainset, testset, valset = createTTVSets(path, trainsize, testsize)

        #MOVE THE FILES TO TRAIN, TEST & VAL FOLDERS
                train = path + '/train/'
                test = path + '/test/'
                val = path + '/val/'

                #TRAIN
                for file in trainset:
                    movefrom = path + '/' + file
                    moveto = train
                    if os.path.isfile(movefrom):
                        shutil.move(movefrom, moveto)
                #TEST
                for file in testset:
                    movefrom = path + '/' + file
                    moveto = test
                    if os.path.isfile(movefrom):
                        shutil.move(movefrom, moveto)
                #VAL
                for file in valset:
                    movefrom = path + '/' + file
                    moveto = val
                    if os.path.isfile(movefrom):
                        shutil.move(movefrom, moveto)

            break

mainrun(base, 0.8, 0.1, 0.1)