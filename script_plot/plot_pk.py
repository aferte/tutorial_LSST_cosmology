import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from astropy.io import fits
from matplotlib import colors as mcolors
css_colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

basedir = os.getenv('REPO_PATH')

#get theory
k = np.loadtxt(basedir+'/ini_inference/lssty10_32pt_test/matter_power_nl/k_h.txt')
z = np.loadtxt(basedir+'/ini_inference/lssty10_32pt_test/matter_power_nl/z.txt')
pk = np.loadtxt(basedir+'/ini_inference/lssty10_32pt_test/matter_power_nl/p_k.txt')

#make plot
plt.clf()
plt.tight_layout()

plt.axvline(0.1,color=css_colors['silver'],ls='--')
plt.axvline(5.,color=css_colors['silver'],ls='--')

plt.plot(k,pk[0,:],color=css_colors['indianred'],label='z = 0')
plt.plot(k,pk[50,:],color=css_colors['salmon'],label='z = '+str(round(z[50],1)))
plt.plot(k,pk[-1,:],color=css_colors['coral'],label='z = '+str(round(z[-1],1)))

plt.tick_params(labelsize=15)
plt.xscale('log')
plt.yscale('log')
plt.ylabel(r'P(k,z)',fontsize=15)
plt.xlabel(r'$k$ (h/Mpc)',fontsize=15)
plt.legend(frameon=False,prop={'size': 13})
plt.savefig('pkz.pdf',format="pdf", bbox_inches="tight")