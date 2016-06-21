import numpy as np
import colorsys

def get_colors(num_colors):

    HSVcolors = np.array([np.linspace(0, 1, num_colors),
                  #np.random.uniform(low=0.3, high=0.7, size=(num_colors,)),
                  #np.random.uniform(low=0.55, high=0.95, size=(num_colors,))])
                  np.linspace(0.3, 0.7, num_colors),
                  np.linspace(0.55, 0.95, num_colors)])

    HSVcolors = HSVcolors.transpose()
    #np.random.shuffle(HSVcolors)

    RGBcolors = [colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]) for hsv in HSVcolors]
    return RGBcolors

#import matplotlib.colorbar as cb
#import matplotlib.pyplot as plt
#from matplotlib.colors import LinearSegmentedColormap
#n=20
#fig, ax = plt.subplots(figsize=(15, 1))
#cb.ColorbarBase(ax, cmap=LinearSegmentedColormap.from_list('newcm', get_colors(n), N=n), spacing='proportional', ticks=None, format='%1i', orientation=u'horizontal')
#plt.axis('off')
#plt.show()

