def get_config(key):
    import numpy as np
    import commands
    if key=='tmpfiles':
        return '''complete.txt data_3lpmefe7.dat record_current_1.dat\
                          Input_tag_madgraph_*.txt'''
    if key=='cfg':
        pwd=commands.getoutput("pwd")
        cfg={'MicrOMEGAS_exe':'./micromegas/IDM/main',\
             'MadGraph_exe':'./MG5_aMC/bin/mg5_aMC',\
             'MadGraph_out_dir': "./Output_Madgraph_1",\
             'CheckMATE_exe': './CheckMATE/bin/CheckMATE',\
             'CheckMATE_out_dir': "%s/CheckMate_Analysis" %pwd}
        return cfg
    if key=='SM':
        return {'G_F': 1.166e-05, 'alpha_em': 0.0078125, 'm_e': 0.000511, \
                'm_mu': 0.1057, 'm_tau': 1.777, 'vev': 246.0, \
                'MW': 80.385, 'MZ': 91.1876, 'WH':4.21e-3}


    
        #test constants
    if key=='yuktest':
        return np.array([[  4.68956210e-07 +3.81993490e-06j,
                                1.38859126e-08 -4.92602010e-07j,
                                5.14669245e-07 +4.07459526e-08j],
                             [ -1.35834336e-06 -7.35968582e-06j,
                               -4.36558572e-06 -4.56875709e-07j,
                               -5.26964058e-06 +3.97752658e-07j],
                             [  6.00277570e-07 -5.16728840e-07j,
                                2.18323545e-06 -2.36196267e-06j,
                                1.40527437e-06 +3.01151766e-06j]])

    if key=='branchingtest':
        return  {'H+ -> ve,e+,~H0': 0, 'tr01 -> ve,~H0': 0.4833762,
                 'H+ -> vt,ta+,~H0': 0, 'tr01 -> vt~,~A0': 0,
                 'tr01 -> vm~,~A0': 0, 'tr01 -> e-,~H+': 0,
                 'tr01 -> vm,~H0': 0.007925269, 'tr01 -> ve,~A0': 0,
                 'tr01 -> vt,~A0': 0, 'A0 -> W+,~H-': 0, 'tr1- -> mu-,~A0': 0,
                 'tr01 -> e+,~H-': 0, 'tr01 -> ve~,~H0': 0.4833762, 'H+ -> W+,~A0': 0,
                 'H+ -> vm,mu+,~H0': 0, 'tr01 -> vm~,~H0': 0.007925269,
                 'tr01 -> vt~,~H0': 0.008698545, 'H+ -> c,d~,~H0': 0,
                 'H+ -> c,s~,~H0': 0, 'H+ -> u,d~,~H0': 0, 'tr1- -> ve~,~H-': 0,
                 'A0 -> a,~H0': 0, 'tr1- -> ta-,~A0': 0, 'tr01 -> ta+,~H-': 0,
                 'tr01 -> mu-,~H+': 0, 'tr01 -> ve~,~A0': 0, 'tr1- -> e-,~H0': 0.9667534,
                 'tr1- -> vt~,~H-': 0, 'tr1- -> vm~,~H-': 0, 'A0 -> Z,~H0': 0.9999999,
                 'tr01 -> vm,~A0': 0, 'H+ -> u,s~,~H0': 0, 'tr01 -> vt,~H0': 0.008698545,
                 'tr01 -> ta-,~H+': 0, 'tr1- -> ta-,~H0': 0.01739601, 'A0 -> W-,~H+': 0,
                 'tr1- -> e-,~A0': 0, 'H+ -> W+,~H0': 1.0, 'tr01 -> mu+,~H-': 0,
                 'tr1- -> mu-,~H0': 0.01585055}
    
    if key=='mitest':
        return {'widthA0': 109.0, 'NSI': 1.355e-12, 'widthtr01': 1.62e-11,\
                'PSI': 1.328e-12, 'widthtr1P': 1.61e-11, 'Xf': 23.8,\
                'sigmav': 1.84e-27, 'Omega': 0.118, 'widthHP': 111.0}


    
    if key=='checkmtest':
        return {'dCL_obs_mumu': 0.0, 'dS_stat_mumu': 0.0, 'dCL_exp_mumu': 0.0,\
                'dS_sys_elel': 0.0,'dB_elmu': 2.0, 'dB_elel': 2.2, 'dS_sys_elmu': 0.0,\
                'xsection_process': 0.0, 'r_exp': 0.0,'CL_obs_elmu': 1.0, 'B': 6.1,\
                'O_elel': 4.0, 'S_mumu': 0.0, 'CLs_exp': 1.0, 'CLs_obs': 1.0,\
                'CL_obs_elel': 1.0, 'dCLs_obs': 0.0, 'O_elmu': 5.0,\
                'SR': ' atlas_conf_2013_049 - SR_mT2_110_elel','dB': 2.2,\
                'S_elel': 0.0, 'S_elmu': 0.0, 'r_max': 0.0, 'dS_stat_elel': 0.0,\
                'dS_tot': 0.0,'dS_sys_mumu': 0.0, 'dS_stat_elmu': 0.0, 'r_obs': 0.0,\
                'dS_tot_mumu': 0.0, 'O_mumu': 4.0,'dCL_exp_elel': 0.0,\
                'dCL_exp_elmu': 0.0, 'xsectionerror_process': 0.0, 'B_mumu': 6.3,\
                'dCL_obs_elmu': 0.0, 'dCL_obs_elel': 0.0, 'dS_sys': 0.0,\
                'S95_exp': 6.699, 'dS_stat': 0.0,'O': 4.0, 'S': 0.0,\
                'CL_exp_elel': 1.0, 'S95_obs': 5.481, 'dCLs_exp': 0.0, 'dB_mumu': 2.4,\
                'CL_exp_elmu': 1.0, 'B_elmu': 4.4, 'B_elel': 6.1, 'CL_obs_mumu': 1.0,\
                'dS_tot_elmu': 0.0,'dS_tot_elel': 0.0, 'CL_exp_mumu': 1.0}

    if key=='madtest':
        return {'xsectionerror1': 0.001026, 'xsectionerror2': 0,\
                'xsection2': 0, 'xsection1': 0.144}
