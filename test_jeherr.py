from TensorMol import *
import time

#jeherr tests

# Takes two nearly identical crystal lattices and interpolates a core/shell structure, must be oriented identically and stoichiometric
if (0):
	a=MSet('cspbbr3_tess')
	#a.ReadGDB9Unpacked(path='/media/sdb2/jeherr/TensorMol/datasets/cspbbr3/pb_tess_6sc/')
	#a.Save()
	a.Load()
	mol1 = a.mols[0]
	mol2 = a.mols[1]
	mol2.RotateX()
	mol1.AlignAtoms(mol2)
	optimizer = Optimizer(None)
	optimizer.Interpolate_OptForce(mol1, mol2)
	mol1.WriteXYZfile(fpath='./results/cspbbr3_tess', fname='cspbbr3_6sc_pb_tess_goopt', mode='w')
	# mol2.WriteXYZfile(fpath='./results/cspbbr3_tess', fname='cspbbr3_6sc_ortho_rot', mode='w')

if (0):
	a=MSet('toluene_tmp')
	# a.ReadGDB9Unpacked(path='/media/sdb2/jeherr/TensorMol/datasets/benzene/', has_force=True)
	# a.Save()
	# a.WriteXYZ()
	a.Load()
	print "nmols:",len(a.mols)
	TreatedAtoms = a.AtomTypes()
	d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
	tset = TensorData(a,d)
	tset.BuildTrainMolwise("toluene_tmp",TreatedAtoms)
	tset = TensorData(None,None,"toluene_tmp_"+"GauSH",None,2000)
	manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms

if (0):
	a=MSet('OptMols')
	a.ReadXYZ("OptMols")
	test_mol=a.mols[0]
	b=MSet("test_mol")
	b.mols.append(test_mol)
	TreatedAtoms = b.AtomTypes()
	d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
	tset = TensorData(b,d)
	tset.BuildTrainMolwise("test_mol",TreatedAtoms)

if (0):
	a=MSet("md_set")
	#a.ReadGDB9Unpacked(path='/data/jeherr/TensorMol/datasets/md_datasets/md_set/', has_force=True)
	#a.Save()
	#a.WriteXYZ()
	a.Load()
	b=a.RotatedClone(3)
	b.WriteXYZ("md_set_rot")
	b.Save("md_set_rot")
	a.Load()
	print "nmols:",len(a.mols)
	b=MSet("md_set_rotated")
	b=a.RotatedClone(3)
	b.Save()
	print "nmols:",len(b.mols)
	TreatedAtoms = a.AtomTypes()
	d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
	tset = TensorData(a,d)
	tset.BuildTrainMolwise("md_set_rotated",TreatedAtoms)
	tset = TensorData(None,None,"md_set_rotated_"+"GauSH",None,2000)
	manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms
	optimizer = Optimizer(manager)
	optimizer.OptRealForce(test_mol)

if(0):
	a=MSet("benzene")
	a.Load()
	test_mol = a.mols[0]
	test_mol.coords = test_mol.coords - np.average(test_mol.coords, axis=0)
	test_mol.Distort()
	manager=TFManage("md_set_rotated_GauSH_fc_sqdiff",None,False)
	optimizer=Optimizer(manager)
	optimizer.OptRealForce(test_mol)

if(0):
	a=MSet("md_set")
	a.ReadXYZUnpacked(path='/data/jeherr/TensorMol/datasets/md_datasets/md_set/', has_force=True, center=True)
	a.Save()
	a.WriteXYZ()
	##a.Load()
	b=a.RotatedClone(5)
	b.WriteXYZ("md_set_rot")
	b.Save("md_set_rot")
	#b=MSet("md_set_rot")
	#b.Load()
	##print "nmols:",len(a.mols)
	print "nmols:",len(b.mols)
	TreatedAtoms = b.AtomTypes()
	d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
	tset = TensorData(b,d)
	tset.BuildTrainMolwise("md_set_rotated",TreatedAtoms)
	tset = TensorData(None,None,"md_set_rotated_"+"GauSH")
	manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms
	#optimizer = Optimizer(manager)
	#optimizer.OptRealForce(test_mol)

if(0):
	#a=MSet("OptMols")
	##a.ReadXYZ('OptMols')
	##a.Save()
	##a.WriteXYZ()
	#a.Load()
        #b=a.DistortAlongNormals(80, True, 0.7)
	#print "nmols:",len(b.mols)
	#c=b.RotatedClone(6)
	#c.WriteXYZ("OptMols_NEQ_rot")
	#c.Save("OptMols_NEQ_rot")
	##b=MSet("md_set_rot")
	##b.Load()
	###print "nmols:",len(a.mols)
	#print "nmols:",len(c.mols)
	#TreatedAtoms = c.AtomTypes()
	#d = Digester(TreatedAtoms, name_="GauSH",OType_ ="GoForce")
	#tset = TensorData(c,d)
	#tset.BuildTrainMolwise("OptMols_NEQ_rot",TreatedAtoms)
	tset = TensorData(None,None,"OptMols_NEQ_rot_"+"GauSH")
	manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms
	#optimizer = Optimizer(manager)
	#optimizer.OptRealForce(test_mol)

if(0):
	#a=MSet("md_OptMols_gdb9clean")
	#a.Save()
	#a.WriteXYZ()
	#print "nmols:",len(a.mols)
	#TreatedAtoms = a.AtomTypes()
	#d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
	#tset = TensorData(a,d)
	#tset.BuildTrainMolwise("md_OptMols_gdb9clean",TreatedAtoms)
	tset = TensorData(None,None,"md_OptMols_gdb9clean_"+"GauSH")
	manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms
	#optimizer = Optimizer(manager)
	#optimizer.OptRealForce(test_mol)

#a=MSet("benzene")
#a.Load()
#test_mol = a.mols[0]
#TreatedAtoms = a.AtomTypes()
#d = Digester(TreatedAtoms, name_="GauSH",OType_ ="Force")
#tset = TensorData(a,d)
#tset.BuildTrainMolwise("benzene_NEQ",TreatedAtoms)
tset = TensorData(None,None,"benzene_NEQ_"+"GauSH")
manager=TFManage("",tset,True,"fc_sqdiff") # True indicates train all atoms
#manager=TFManage("benzene_NEQ_GauSH_fc_sqdiff",None,False)
#optimizer = Optimizer(manager)
#optimizer.OptTFRealForce(test_mol)

#a=MSet("benzene")
#a.Load()
#test_mol = a.mols[0]
#test_mol.coords = test_mol.coords - np.average(test_mol.coords, axis=0)
#test_mol.Distort()
#manager=TFManage("md_set_rotated_GauSH_fc_sqdiff",None,False)
#optimizer=Optimizer(manager)
#optimizer.OptRealForce(test_mol)
