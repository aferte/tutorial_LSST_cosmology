import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from astropy.io import fits
from matplotlib import colors as mcolors
css_colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

basedir = os.getenv('REPO_PATH')

#get theory
ell = np.loadtxt(basedir+'/ini_inference/lssty10_32pt_test/shear_cl/ell.txt')
cell = np.loadtxt(basedir+'/ini_inference/lssty10_32pt_test/shear_cl/bin_2_2.txt')

#get data
lsst = fits.open(basedir+'/data_vector/lssty10_srd_32pt_simulation.fits')
select_bin1 = lsst['shear_cl'].data['bin1'] == 2
select_bin2 = lsst['shear_cl'].data['bin2'] == 2
ell_data = lsst['shear_cl'].data['ANG'][select_bin1 & select_bin2]
cl_data = lsst['shear_cl'].data['VALUE'][select_bin1 & select_bin2]
cl_error_data = np.diag(lsst['COVMAT'].data)[15*5:15*6]

#make plot
plt.clf()
plt.tight_layout()

plt.plot(ell,cell*ell*1e7,color=css_colors['indianred'])
plt.errorbar(ell_data, cl_data*ell_data*1e7,yerr=ell_data*np.sqrt(cl_error_data)*1e7,fmt='o',ls='none',\
    markersize=3.,color=css_colors['teal'],label='LSST Y10')

plt.tick_params(labelsize=15)
plt.xscale('log')
plt.ylabel(r'$10^{7}\ell C_{\ell}^{\kappa \kappa, 22}$',fontsize=15)
plt.xlabel(r'$\ell$',fontsize=15)
plt.legend(frameon=False,prop={'size': 13})
plt.xlim(20,3000)
plt.savefig('cell_bin22.pdf',format="pdf", bbox_inches="tight")
#plt.show()
