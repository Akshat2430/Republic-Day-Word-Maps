# Getting speech from JSON and saving as TXT file
Speeches = pd.read_json("/kaggle/input/mann-ki-baat/mann_ki_baat.json")
pf = Speeches['allText']
np.savetxt(r'./np3.txt', pf.values, fmt='%s', newline='\n'*2)
