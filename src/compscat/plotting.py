import matplotlib.pyplot as plt
import uproot


class PlotData:
	
    def __init__(self):
    	self.filename=filename    
    def plot(data, key):
        plt.hist(data, bins=100, color=None)
        label = key.replace("_", " ")
        plt.xlabel(label + " [keV]")
        plt.ylabel("Counts")
        plt.show()
        plt.savefig(key + ".png")

    def file(self.filename='MC_compton.root'):
        if 'root' not in filename:
            raise Exception("Input must be a ROOT file")
        file = uproot.open(self.filename)
        tree = file["events"]
        branches = tree.arrays()
        for key in tree.keys():
            PlotData().plot(branches[key], key)
        return 0
