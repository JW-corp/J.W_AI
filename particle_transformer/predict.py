import uproot
import awkward as ak
import numpy as np

infile = "training/TopLandscape/ParT/20230518-115034_example_ParticleTransformer_ranger_lr0.001_batch512/predict_output/pred.root"
tree = uproot.open(infile+":Events")

top_score = tree["jet_isTop"].array().to_numpy()
qcd_score = tree["jet_isQCD"].array().to_numpy()


top_score = top_score.astype(int)
qcd_score = qcd_score.astype(int)

print(qcd_score)
print(np.sum(qcd_score)/len(qcd_score))

import matplotlib.pyplot as plt

plt.hist(qcd_score,histtype='step',color='r',label='qcd')
plt.hist(top_score,histtype='step',color='b',label='top')
plt.legend(loc='upper right')
plt.savefig('score.png')
plt.close()


