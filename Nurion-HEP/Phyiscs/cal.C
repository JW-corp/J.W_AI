double GetPvalue(double nbkg, int nsigNbkg){

  double integral = 1.; 
  for(int i = 0; i < nsigNbkg; i++){
    integral -= TMath::Poisson(i,nbkg);
  }
  return integral;
} 


void cal(){


//double N_exptect_bgr =237941.4286139921;
//double N_exptect_sig =398681.31486866204;

//('numsig :', 539.115067715226)
//('num bkg: ', 2391.2241738127964)


//('# of Signal_region ', 2762.7768673102973)
//('# of BKG_region ', 633859.9666153438)


//('numsig :', 539.115067715226)
//('num bkg: ', 2391.2241738127964)



double N_exptect_bgr = 2391.2241738127964 ;
double N_exptect_sig = 539.115067715226 ;


double pvalue_expected       = GetPvalue(N_exptect_bgr,N_exptect_bgr + N_exptect_sig);
double significance_expected = ROOT::Math::gaussian_quantile_c(pvalue_expected,1);


double estimated = N_exptect_sig / sqrt(N_exptect_bgr+N_exptect_sig);

cout << "P-value: "<< pvalue_expected << endl;
cout << "calculated sigma : "<< significance_expected <<endl;
cout << "Rough calculated sigma : "<<estimated << endl;

}
