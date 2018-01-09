import matplotlib.pyplot as plt
from keras.models import Sequential
import os


#check if dir exists, create if not already.
def makeNewDir(newDirPath):
    if not os.path.exists(newDirPath):
        print("directory ", newDirPath, " did not exist, creating:")
        os.mkdir(newDirPath)
    else:
        print("directory ", newDirPath, "already existed. filecount = ", len(dirFileList(newDirPath)))

def dirFileList(dir_path):
    return [name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))]



def showLayersInfo(model):
    print ("Number of layers : ", len(model.layers))
    count = 0
    for layer in model.layers:
        print (count, type(layer), ", trainable:", layer.trainable)
        print ("input:", layer.input_shape, ", output:",layer.output_shape, ", len(weights)", len(layer.get_weights()), "\n")
        count +=1


def plot_history(history):
    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validate'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validate'], loc='upper left')
    plt.show()


def listDirsFileCount(directory):
    directory = sorted(directory)
    for dir_ in directory:
        print (dir_, len(dirFileList(dir_)))
