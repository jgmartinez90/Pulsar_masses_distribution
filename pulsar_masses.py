import numpy as np

try:
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt
    import matplotlib.colors

    from matplotlib import cm, rcParams
    from matplotlib.ticker import NullFormatter

except:
    raise ImportError 
    matplotlib = False


def readfile(file='pulsar_masses.txt'):
    masses = np.genfromtxt(file,dtype=[("ID",np.int),("type",np.int),("Name","|S256"),("Mass",np.float),("uerr",np.float),("lerr",np.float),("ref","|S256")],delimiter="")
    return masses

def prepare_frame():
    nullfmt   = NullFormatter()
#    plt.figure()
    plt.figure(figsize=(9.,13.944))
    plt.rcParams["savefig.dpi"] = 400
    rcParams['font.size'] = 18

    fig = plt.axes()
    fig.yaxis.set_major_formatter(nullfmt)

    return fig


def plot_masses(mass_table):

    fig = prepare_frame()
    markers = ["o","1","2","3","s","p","8"]
    colors = ['r','b','g','c','m','k','y']

    masses = readfile()
    typ = masses["type"]


    for i in range(masses['Mass'].shape[0]):
       fig.errorbar(masses['Mass'][i],
                    i+0.1, 
                    xerr=np.array(-masses['lerr'][i],masses['uerr'][i]),
                    color=colors[masses["type"][i]],marker='D')
    for i in range(masses['Mass'].shape[0]):
        fig.text(0.1,i, masses["Name"][i])




    fig.axis([0.0,2.2,-0.3,masses['Mass'].shape[0] + 0.2],size='xx-large',weight='light')
    fig.set_xlabel('Mass (Solar Mass)',size='large',weight='light')

    fig.yaxis.set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['left'].set_visible(False)
    fig.spines['bottom'].set_linewidth (2.0)
    fig.spines['top'].set_linewidth (1.0) #2.0
    fig.xaxis.set_tick_params(width=3.0,length=5)
    plt.savefig('/homes/joey/programs/pulsar_masses/ns_masses.pdf',format='pdf')

plot_masses('pulsar_masses.txt')
plt.savefig('/homes/joey/Scripts/pulsar_masses/masses.eps')
plt.show()
