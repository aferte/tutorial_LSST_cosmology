import numpy as np
import matplotlib.pyplot as plt
from getdist import plots, MCSamples
import getdist
from matplotlib import colors as mcolors
css_colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

###################
###CHAIN READING###
###################
#methods for chain loading
def get_name_param(chain_filename):
    with open(chain_filename) as f:
        first_line = f.readline().split('\t')
    first_line[0] = first_line[0][1:]
    #remove the 3 last names which are chain properties
    return first_line[:-3]

def get_chain_samples(chain_filename,dict_labels,main_chain_label,**kwargs):
    '''
    chain_filename: string of chain path
    dict_labels: dict of labels
    chain_label: string to label the chain
    '''
    #get parameters name and associated labels
    param_name = get_name_param(chain_filename)
    chain_label = []
    for ii in param_name:
        chain_label.append(dict_labels[ii])
    #read the chain and get samples
    chain = np.loadtxt(chain_filename)
    samples = MCSamples(samples=chain[:,:-3],names=param_name,\
    labels=chain_label,weights=np.exp(chain[:,-3]),\
        settings={'smooth_scale_1D':4},label=main_chain_label,**kwargs)
    return samples


#parameter labels
dict_labels = {\
                   'cosmological_parameters--omega_m':r'\Omega_{\rm m}',\
                   'cosmological_parameters--w':r'$w_0$',\
                   'cosmological_parameters--wa':r'$w_a$',\
                   'cosmological_parameters--wp':r'$w_{\rm p}$',\
                   'a_pivot':r'$a_{\rm p}$',\
                   'z_pivot':r'$z_{\rm p}$',\
                   'cosmological_parameters--omega_k':r'$\Omega_k$',\
                   'cosmological_parameters--omega_c':r'$\Omega_{\rm c}$',\
                   'COSMOLOGICAL_PARAMETERS--SIGMA_8':r'\sigma_8',\
                   'cosmological_parameters--sigma_8':r'\sigma_8',\
                   'S8':r'$S_8$',\
                   'cosmological_parameters--h0':r'h_0',\
                   'cosmological_parameters--omega_b':r'\Omega_b',\
                   'cosmological_parameters--n_s':r'n_s',\
                   'cosmological_parameters--a_s':r'A_s',\
                   'cosmological_parameters--mnu':r'm_{\nu}',\
                   'cosmological_parameters--ommh2':r'$\Omega_{\rm m}h^2$',\
                   'cosmological_parameters--ombh2':r'$\Omega_{\rm b}h^2$',\
                   'cosmological_parameters--omch2':r'$\Omega_{\rm c}h^2$',\
                   'cosmological_parameters--alens':r'$A_{\rm L}$',\
                   'cosmological_parameters--r':r'r',\
                   'summnu':r'$\sum m_{\nu}\,[{\rm eV}]$',\
                   'supernova_params--m':r'$M_{\rm SN}$',\
                    'halo_model_parameters--logt_agn':r"T_{\rm AGN}",\
                   'bin_bias--b1':r'$b_1$',\
                   'bin_bias--b2':r'$b_2$',\
                   'bin_bias--b3':r'$b_3$',\
                   'bin_bias--b4':r'$b_4$',\
                   'bin_bias--b5':r'$b_5$',\
                   'bin_bias--b6':r'$b_6$',\
                   'bin_bias--b7':r'$b_7$',\
                   'bin_bias--b8':r'$b_8$',\
                   'bin_bias--b9':r'$b_9$',\
                   'bin_bias--b10':r'$b_{10}$',\
                   'bias_lens--b1':r'$b_1$',\
                   'bias_lens--b2':r'$b_2$',\
                   'bias_lens--b3':r'$b_3$',\
                   'bias_lens--b4':r'$b_4$',\
                   'bias_lens--b5':r'$b_5$',\
                   'bias_lens--b1wt_bin1':r'$b_1$',\
                   'bias_lens--b1wt_bin2':r'$b_2$',\
                   'bias_lens--b1wt_bin3':r'$b_3$',\
                   'bias_lens--b1wt_bin4':r'$b_4$',\
                   'bias_lens--b1wt_bin5':r'$b_5$',\
                   'bias_lens--rmean_bin':r'$X_{\rm lens}$',\
                   'shear_calibration_parameters--m1':R'$m_1$',\
                   'shear_calibration_parameters--m2':r'$m_2$',\
                   'shear_calibration_parameters--m3':r'$m_3$',\
                   'shear_calibration_parameters--m4':r'$m_4$',\
                   'shear_calibration_parameters--m5':r'$m_5$',\
                   'intrinsic_alignment_parameters--a':r'A_{ IA}',\
                   'intrinsic_alignment_parameters--a1':r'a_1',\
                   'intrinsic_alignment_parameters--a2':r'a_2',\
                   'intrinsic_alignment_parameters--alpha':r'\alpha_{IA}',\
                   'intrinsic_alignment_parameters--alpha1':r'\alpha_{1}',\
                   'intrinsic_alignment_parameters--alpha2':r'\alpha_{2}',\
                   'intrinsic_alignment_parameters--bias_ta':r'b_{TA}',\
                   'photoz_source_errors--bias_1':r'$\Delta z_{s}^1$',\
                   'photoz_source_errors--bias_2':r'$\Delta z_{s}^2$',\
                   'photoz_source_errors--bias_3':r'$\Delta z_{s}^3$',\
                   'photoz_source_errors--bias_4':r'$\Delta z_{s}^4$',\
                   'photoz_source_errors--bias_5':r'$\Delta z_{s}^5$',\
                   'lens_photoz_errors--bias_1':r'$\Delta z_{l}^1$',\
                   'lens_photoz_errors--bias_2':r'$\Delta z_{l}^2$',\
                   'lens_photoz_errors--bias_3':r'$\Delta z_{l}^3$',\
                   'lens_photoz_errors--bias_4':r'$\Delta z_{l}^4$',\
                   'lens_photoz_errors--bias_5':r'$\Delta z_{l}^5$',\
                   'wl_photoz_errors--bias_1':r'$\Delta z_{s}^1$',\
                   'wl_photoz_errors--bias_2':r'$\Delta z_{s}^2$',\
                   'wl_photoz_errors--bias_3':r'$\Delta z_{s}^3$',\
                   'wl_photoz_errors--bias_4':r'$\Delta z_{s}^4$',\
                   'wl_photoz_errors--bias_5':r'$\Delta z_{s}^5$',\
                   'photoz_lens_errors--bias_1':r'\Delta z_{l}^1',\
                   'photoz_lens_errors--bias_2':r'\Delta z_{l}^2',\
                   'photoz_lens_errors--bias_3':r'\Delta z_{l}^3',\
                   'photoz_lens_errors--bias_4':r'\Delta z_{l}^4',\
                   'photoz_lens_errors--bias_5':r'\Delta z_{l}^5',\
                   'photoz_lens_errors--bias_6':r'\Delta z_{l}^6',\
                   'photoz_lens_errors--bias_7':r'\Delta z_{l}^7',\
                   'photoz_lens_errors--bias_8':r'\Delta z_{l}^8',\
                   'photoz_lens_errors--bias_9':r'\Delta z_{l}^9',\
                   'photoz_lens_errors--bias_10':r'\Delta z_{l}^{10}',\
                   'lens_photoz_errors--width_1':r'$W_{l}^1$',\
                   'lens_photoz_errors--width_2':r'$W_{l}^2$',\
                   'lens_photoz_errors--width_3':r'$W_{l}^3$',\
                   'lens_photoz_errors--width_4':r'$W_{l}^4$',\
                   'lens_photoz_errors--width_5':r'$W_{l}^5$',\
                   'cosmological_parameters--tau':r'\tau',\
                   'planck--a_planck':r'A_{ planck}',\
                   'cosmological_parameters--yhe':r'$Y_{\rm He}$',
                   'DATA_VECTOR--2PT_CHI2':r'\Delta \Chi^2',
}

#load the chain
chain_lsst   = '../chains/chain_lssty10_32pt_srd.txt'
samples_lsst = get_chain_samples(chain_lsst,dict_labels,'LSST Y10')


####FIDUCIAL####
plt.clf()
g= plots.getSubplotPlotter(width_inch=8.)
g.settings.scaling=False
g.settings.tight_layout=False
g.settings.rc_sizes(axes_fontsize=15,lab_fontsize=15)
#g.settings.lw_contour=2.5
g.settings.norm_1d_density = False
g.plot_2d([samples_lsst],
                ['cosmological_parameters--omega_m','COSMOLOGICAL_PARAMETERS--SIGMA_8'],
                colors=[css_colors['indianred']],\
                contour_lws = [8],\
                alphas=[0.8],
                filled=[True],\
               # lims=[.945,0.98,3e-4,0.5]
        )

g.settings.lab_fontsize = 15
g.settings.axes_fontsize = 15
g.add_legend(['LSST Y10 3x2pt'],colored_text=True,legend_loc='upper left',\
                fontsize=18)
plt.savefig('lssty10_cosmo.pdf')
