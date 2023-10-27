# tutorial_wlcosmology

Tutorial for KIPAC on cosmological inference with 3x2pt. 

Instructions to run a full chain on sherlock:

1. Connect to sherlock. I recommend working in $SCRATCH or in your space in $OAK.

2. Install cosmosis environment and get cosmosis-standard-library by running the following commands:
> sh_dev
(the following takes a while so we request an interactive node)
We follow the instructions from here https://cosmosis.readthedocs.io/en/latest/intro/installation.html#conda-forge-from-scratch because the conda install does not work (it used to, at least until this summer - strange!)
> wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
> chmod +x Miniforge3.sh
> ./Miniforge3.sh -b -p ./env_cosmosis
> source ./env_cosmosis/bin/activate
> conda install -y cosmosis cosmosis-build-standard-library
> source cosmosis-configure
> cosmosis-build-standard-library main

3. Clone this github repository:
> git clone git@github.com:aferte/tutorial_wlcosmology.git

4. Edit the job submission script:
> cd tutorial_wlcosmogy/ini_inference
> emacs -nw lssty10_32pt_run.sh
Edit the file to set the cosmosis environment,
Save and exit the file.
You can give your stanford email address in the header of the sh file to receive notifications about your job, they get to your stanford inbox but not forwarded to your SLAC inbox :(

5. Submit the chain by running (exit sh_dev if you are still on the interactive node):
> sbatch lssty10_32pt_run.sh

This will write the chain in chain_lssty10_32pt_srd_nautilus.txt in tutorial_wlcosmogy/ini_inference.
To get contour plots, use tutorial_wlcosmogy/script_plot/plot_chain.py !!You need to edit line 134 to point to the correct chain's path!!

Happy chain running!

 
