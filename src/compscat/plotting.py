import matplotlib.pyplot as plt
import uproot


class PlotData:
	

    def plot(data, key):
        plt.hist(data, bins=40, color=None)
        label = key.replace("_", " ")
        plt.xlabel(label + " [keV]")
        plt.ylabel("Counts")
        plt.show()
        plt.savefig(key + ".png")

    def file(filename='MC_compton.root'):
        if 'root' not in filename:
            raise TypeError("Input must be a ROOT file")
        file = uproot.open(filename)
        tree = file["events"]
        branches = tree.arrays()
        for key in tree.keys():
            PlotData.plot(branches[key], key)

