import h5py


RPV_list = ["RPV/RPV_0.h5","RPV/RPV_1.h5","RPV/RPV_10.h5"]

QCD_list = ["QCD_HT1000/QCD_HT1000_8.h5", "QCD_HT1500/QCD_HT1500_8.h5","QCD_HT2000/QCD_HT2000_16.h5"]






for f in QCD_list:
	dat = h5py.File(f,'r')
	print(dat['all_events']['weights'].shape)
