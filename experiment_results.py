'''
GUERRA ADAMES Ariel
Script containing experimental results and graphic generation.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

#######################################
#####   0/1 Knapsack Results   ########
#######################################

#### 1.1 Bruteforce Results

### Our problem generator (Uniform distribution)
# Number of possible items
brute_no_items_pg = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]  # Number of possible items
# Execution time for corresponding number of items
brute_times_pg = [0.00003194, 0.0001730, 0.002457, 0.02183, 0.18702, 1.7720, 16.25510, 146.71864, 1313.96032, 11585.78009]

###  Dataset 1
# Number of possible items
no_items_db = [10, 20, 4, 4, 15, 10, 7, 23, 5, 20]
# Execution time for corresponding number of items
brute_times_db = [4.1298, 7724.5411, 0.10085, 0.09083, 206.9239, 4.8999, 0.39196, 69545.2837, 0.180006, 7659.6701]

#### 1.2 Meet me in the Middle (Bruteforce type)

### Our problem generator
# Number of possible items
MiM_no_items_pg = [3, 6, 9, 12, 15, 18, 21, 24, 27]  # Number of possible items
# Execution time for corresponding number of items
MiM_times_pg = [8.702278137207031e-05, 9.775161743164062e-05, 0.0003829002380371094, 0.002681732177734375, 0.017619848251342773, 0.20154309272766113, 2.4896278381347656, 23.694475173950195, 793.1278920173645, 7138.08431234223]

### Dataset provided
# Execution time for corresponding number of items
MiM_time_db = [0.50306, 897.95207, 0.110149, 0.12207, 16.375064, 0.579833, 0.16903, 8848.0949, 0.1578330, 852.91290]

# Accuracy results
MiM_accuracy_db = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
MiM_edit_db = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#####################
#### 1.3 Backtracking (Bruteforce type)
### Our problem generator (Uniform distribution)
# Number of possible items
Backt_no_items_pg = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]  # Number of possible items
# Execution time for corresponding number of items
Backt_times_pg = [2.193450927734375e-05, 3.409385681152344e-05, 0.00048, 0.00450205, 0.0241119, 0.113250, 0.960355, 6.423973, 27.751918, 243.25796]

### Dataset provided
# Execution time for corresponding number of items
Backt_time_db = [0.68402, 1299.7241, 0.04410, 0.041007, 23.05507, 0.61511, 0.17619, 5848.47831, 0.0629425, 1312.37483]

# Accuracy results
Backt_accuracy_db = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
Backt_edit_db = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#####################
#### 2. Branch and Bound

### Our problem generator  (Uniform distribution)
# Testing on our problem generator was not possible due to how the algorithm was designed. Ask thomas to fix it.

### Dataset provided
# Execution time for corresponding number of items
BaB_time_db = [0.06294, 0.36501, 0.02193, 0.02717, 0.1111, 0.08225, 0.03385, 0.28276, 0.02503, 0.22387]

# Accuracy results
BaB_accuracy_db = [85.08474, 81.34765, 94.2857, 100, 72.7545, 96.1538, 89.7196, 99.6723, 100, 91.4146]
BaB_edit_db = [4, 8, 2, 0, 4, 4, 4, 18, 1, 5]
BaB_edit_ratio = np.asarray(BaB_edit_db)/np.asarray(no_items_db)

#####################
#### 3. Greedy Approaches
#### 3.1 Value-oriented greedy

### Our problem generator
## Uniform distribution
GreedV_no_items_uni = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedV_time_uni = [1.0569095611572266, 5.084991455078125, 15.954971313476562, 32.34410285949707, 56.726694107055664, 88.61613273620605, 160.61973571777344, 171.48804664611816, 216.86506271362305, 283.0789089202881, 347.8739261627197]
GreedV_ave_acc_uni_20 = 0.9454

## Normal distribution
GreedV_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedV_time_nor = [1.6188621520996094, 3.0629634857177734, 10.144948959350586, 19.167184829711914, 33.960819244384766, 53.68185043334961, 79.23603057861328, 135.21814346313477, 164.13402557373047, 172.6078987121582, 204.85186576843262]
GreedV_ave_acc_nor_20 = 0.9201

## Inverse triangular distributions
GreedV_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedV_time_tri = [1.2938976287841797, 5.043983459472656, 16.051292419433594, 32.518863677978516, 56.66804313659668, 86.61317825317383, 127.06899642944336, 177.26898193359375, 216.15099906921387, 292.16527938842773, 349.0939140319824]
GreedV_ave_acc_tri_20 = 0.9387

### Dataset provided
# Execution time for corresponding number of items in miliseconds
GreedV_time_db = [0.47588, 0.69904, 0.3719, 0.32281, 0.61893, 0.53215, 0.59199, 0.985145, 0.62799, 0.696182]

# Accuracy results
GreedV_accuracy_db = [97.6271, 100, 80, 100, 99.1540, 82.69230, 100, 99.9795, 100, 100]
GreedV_edit_db = [4, 0, 3, 0, 0, 6, 1, 4, 1, 0]
GreedV_edit_ratio = np.asarray(GreedV_edit_db)/np.asarray(no_items_db)

#### 3.2 Weight-oriented greedy
### Our problem generator
## Uniform distribution
GreedW_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedW_time_uni = [1.8508434295654297, 4.904031753540039, 16.550064086914062, 33.41412544250488, 58.21490287780762, 90.01493453979492, 132.54094123840332, 172.4991798400879, 214.41221237182617, 302.45184898376465, 369.49706077575684]
GreedW_ave_acc_uni_20 = 0.9065

## Normal distribution
GreedW_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedW_time_nor = [0.8928775787353516, 2.768993377685547, 9.04703140258789, 18.082857131958008, 32.015085220336914, 47.08385467529297, 71.52891159057617, 100.72088241577148, 137.7096176147461, 167.76609420776367, 210.61396598815918]
GreedW_ave_acc_nor_20 = 0.9234

## Inverse triangular distributions
GreedW_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedW_time_tri = [1.3899803161621094, 4.883050918579102, 16.03102684020996, 36.03816032409668, 91.09306335449219, 94.9089527130127, 127.52985954284668, 178.9228916168213, 216.05920791625977, 293.06697845458984, 354.92491722106934]
GreedW_ave_acc_tri_20 = 0.94829

### Dataset provided
# Execution time for corresponding number of items
GreedW_time_db = [0.23698, 0.34189, 0.17619, 0.13780, 0.25701, 0.18310, 0.33783, 0.294923, 0.357866, 0.338077]

# Accuracy results
GreedW_accuracy_db = [72.5423, 92.6757, 100, 69.56521, 71.5073, 96.15384, 73.8317, 97.8191, 100 ,92.68292]
GreedW_edit_db = [4, 4, 0, 2, 7, 4, 4, 5, 1, 6]
GreedW_edit_ratio = np.asarray(GreedW_edit_db)/np.asarray(no_items_db)

#### 3.3 Fractional greedy

### Our problem generator
## Uniform distribution
GreedF_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedF_time_uni = [1.2907981872558594, 5.096912384033203, 16.519784927368164, 33.618927001953125, 62.107086181640625, 93.84393692016602, 140.7029628753662, 186.16032600402832, 243.04890632629395, 312.34192848205566, 364.2611503601074]
GreedF_ave_acc_uni_20 = 0.9770

## Normal distribution
GreedF_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedF_time_nor = [0.7991790771484375, 4.8160552978515625, 15.08784294128418, 30.122995376586914, 54.01873588562012, 87.32986450195312, 124.87387657165527, 158.13660621643066, 204.37097549438477, 265.6292915344238, 309.03005599975586]
GreedF_ave_acc_nor_20 = 0.9820

## Inverse triangular distributions
GreedF_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
GreedF_time_tri = [1.3201236724853516, 5.5999755859375, 18.082857131958008, 37.405967712402344, 65.19699096679688, 94.18487548828125, 140.01893997192383, 206.6650390625, 241.84799194335938, 295.6991195678711, 358.2031726837158]
GreedF_ave_acc_tri_20 = 0.9838

### Dataset provided
# Execution time for corresponding number of items
GreedF_time_db = [0.31876, 0.40984, 0.22292, 0.13899, 0.61488, 0.211, 0.17023, 0.34689, 0.275135, 0.4048347]

# Accuracy results
GreedF_accuracy_db = [100, 100, 100, 69.565217, 100, 100, 95.327102, 99.8566, 100, 99.41463]
GreedF_edit_db = [0, 0, 0, 2, 0, 0, 5, 4, 0, 2]
GreedF_edit_ratio = np.asarray(GreedF_edit_db)/np.asarray(no_items_db)

#####################
#### 4. Dynamic approaches
### 4.1 Dynamic

### Our problem generator
## Uniform distribution
Dynamic_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Dynamic_time_uni = [0.9739398956298828, 130.7070255279541, 523.129940032959, 1122.3375797271729, 1951.2560367584229, 2925.8217811584473, 4218.627214431763, 6076.565980911255, 12086.55595779419, 10173.686981201172, 12116.510391235352]
Dynamic_ave_acc_uni_20 = 100

## Normal distribution
Dynamic_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Dynamic_time_nor = [0.5741119384765625, 103.48916053771973, 374.49073791503906, 846.6942310333252, 1500.2422332763672, 2315.9189224243164, 3317.8000450134277, 4605.143785476685, 5934.11111831665, 7540.001153945923, 9469.321250915527]
Dynamic_ave_acc_nor_20 = 100

## Inverse triangular distributions
Dynamic_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Dynamic_time_tri = [1.9690990447998047, 20.69687843322754, 39.58773612976074, 58.09307098388672, 78.0479907989502, 127.81476974487305, 120.94473838806152, 158.45298767089844, 169.83389854431152, 191.36691093444824, 226.63307189941406]
Dynamic_ave_acc_tri_20 = 100

### Dataset provided
# Execution time for corresponding number of items
Dynamic_time_db = [1.89495, 12.43066, 0.23198, 0.13279, 3.674030, 0.4670619, 0.306129, 173.210859, 12.351989]

# Accuracy results
Dynamic_accuracy_db = [100, 100, 100, 100, 100, 100, 100, 100, 100]
Dynamic_edit_db = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Dynamic_edit_ratio = np.asarray(Dynamic_edit_db)/np.asarray(no_items_db)

### 4.2 Top Down

### Our problem generator.
## Uniform distribution
TopDown_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
TopDown_time_uni = [0.7381439208984375, 265.20299911499023, 1622.1928596496582, 2605.181932449341, 4022.2079753875732, 6363.40594291687, 7509.543895721436, 10690.110921859741, 16099.021911621094, 18273.747205734253, 22862.72621154785]
TopDown_ave_acc_uni_20 = 100

## Normal distribution
TopDown_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
TopDown_time_nor = [0.293731689453125, 225.36993026733398, 995.9707260131836, 1986.159086227417, 3155.8172702789307, 5039.412021636963, 7196.74015045166, 10637.749910354614, 12809.446811676025, 17643.080949783325, 22180.805206298828]
TopDown_ave_acc_nor_20 = 100

## Inverse triangular distributions
TopDown_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
TopDown_time_tri = [1.1599063873291016, 44.406890869140625, 80.59906959533691, 123.50893020629883, 162.4898910522461, 217.43106842041016, 288.28883171081543, 305.9840202331543, 342.82875061035156, 394.89197731018066, 434.049129486084]
TopDown_ave_acc_tri_20 = 100

### Dataset provided
# Execution time for corresponding number of items
TopDown_time_db = [0.94795, 11.9049, 0.126838, 0.09179, 3.23390, 0.470161, 0.20885, 33.64896, 0.420808, 12.1982097]

# Accuracy results
TopDown_accuracy_db = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
TopDown_edit_db = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TopDown_edit_ratio = np.asarray(TopDown_edit_db)/np.asarray(no_items_db)

#####################
#### 5. Fully polynomial
### Our problem generator
## Uniform distribution
Poly_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Poly_time_uni = [0.8540153503417969, 209.84792709350586, 785.7582569122314, 1704.8368453979492, 3078.2229900360107, 4659.898996353149, 6902.009010314941, 9319.336891174316, 12098.652124404907, 15028.721332550049, 20274.91593360901]
Poly_ave_acc_uni_20 = 1

## Normal distribution
Poly_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Poly_time_nor = [0.31495094299316406, 222.1357822418213, 912.482738494873, 1872.4868297576904, 3042.4559116363525, 5034.296035766602, 7432.201862335205, 9923.196077346802, 12412.155151367188, 15588.731050491333, 19344.161987304688]
Poly_ave_acc_nor_20 = 1

## Inverse triangular distributions
Poly_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Poly_time_tri = [1.127004623413086, 37.55974769592285, 74.31483268737793, 113.56616020202637, 152.53233909606934, 195.512056350708, 232.8779697418213, 275.39801597595215, 317.7070617675781, 354.62093353271484, 392.6558494567871]
Poly_ave_acc_tri_20 = 1

### Dataset provided
# Execution time for corresponding number of items
Poly_time_db = [1.14011, 13.91005, 0.20289, 0.250816, 3.31497, 1.03092, 0.34999, 23.00810, 0.266075, 14.7159, 0.149965]

# Accuracy results
Poly_accuracy_db = [100, 100, 100, 95.6521, 100, 100, 100, 99.89, 100, 100]
Poly_edit_db = [0, 0, 0, 2, 0, 0, 0, 5, 0, 0]
Poly_edit_ratio = np.asarray(Poly_edit_db)/np.asarray(no_items_db)

#####################
#### 6. Randomized
### Our problem generator
# Uniform distribution
Random_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Random_time_uni = [11.77668571472168, 79.18906211853027, 146.57115936279297, 239.9880886077881, 322.8869438171387, 378.2081604003906, 459.4743251800537, 547.5647449493408, 695.6562995910645, 1157.1221351623535, 831.1402797698975]
Random_ave_acc_uni_20 = 0.95

## Normal distribution
Random_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Random_time_nor = [10.392189025878906, 65.61803817749023, 119.32587623596191, 185.8229637145996, 251.3902187347412, 318.16911697387695, 381.34098052978516, 445.6350803375244, 509.78684425354004, 570.5859661102295, 631.8919658660889]
Random_acc_nor_20 = 0.9601

## Inverse triangular distributions
Random_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Random_time_tri = [11.22593879699707, 72.10206985473633, 128.98612022399902, 197.78108596801758, 267.0152187347412, 338.52624893188477, 406.6882133483887, 489.58301544189453, 552.2267818450928, 608.8330745697021, 668.6463356018066]
Random_ave_acc_tri_20 = 0.9573

### Dataset provided
# Execution time for corresponding number of items
Random_time_db = [110.5637, 210.5350, 66.3156, 53.431749, 139.0089, 112.4358, 96.46010, 207.8049, 72.17311, 200.6928920]

# Accuracy results
Random_accuracy_db = [99.66101, 100, 80, 95.6521, 99.15409, 100, 95.32710, 99.92833, 71.53846, 100]
Random_edit_db = [2, 0, 3, 2, 0, 4, 5, 5, 2, 0]
Random_edit_ratio = np.asarray(Random_edit_db)/np.asarray(no_items_db)

#####################
#### 7. Genetic
### Our problem generator
# Uniform distribution
Genetic_no_items = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Genetic_time_uni = [19.56915855407715, 19.72508430480957, 20.42388916015625, 20.584821701049805, 21.567821502685547, 21.672964096069336, 21.818161010742188, 21.552085876464844, 22.264957427978516, 23.82802963256836, 24.364233016967773]
Genetic_ave_acc_uni_20 = 85.19683

## Normal distribution
Genetic_no_items_nor = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Genetic_time_nor = [24.049997329711914, 31.89992904663086, 41.37110710144043, 51.346778869628906, 67.07096099853516, 75.75607299804688, 78.08399200439453, 87.34512329101562, 99.71475601196289, 102.61201858520508, 116.83797836303711]
Genetic_acc_nor_20 = 60.77161

## Inverse triangular distributions
Genetic_no_items_tri = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010]
Genetic_time_tri = [19.224882125854492, 19.017934799194336, 20.112276077270508, 20.442724227905273, 20.5078125, 21.090030670166016, 22.908926010131836, 24.85203742980957, 25.058984756469727, 26.356935501098633, 23.6051082611084]
Genetic_ave_acc_tri_20 = 90.49434

### Dataset provided
# Execution time for corresponding number of items
Genetic_time_db = [23.8730, 23.42605, 19.8421, 21.95501, 23.54311, 21.73185, 19.20604, 23.42391, 19.429206, 20.42078]

# Accuracy results
Genetic_accuracy_db = [99.322, 84.375, 100, 100, 71.7152, 96.15384, 86.91588, 99.35497, 100, 89.26829]
Genetic_edit_db = [3, 5, 0, 0, 6, 6, 3, 12, 0, 6]
Genetic_edit_ratio = np.asarray(Genetic_edit_db)/np.asarray(no_items_db)

dfacc = pd.DataFrame([BaB_accuracy_db, Random_accuracy_db, Genetic_accuracy_db, GreedV_accuracy_db, GreedW_accuracy_db, GreedF_accuracy_db, Poly_accuracy_db])
dftime = pd.DataFrame([BaB_time_db, Random_time_db, Genetic_time_db, GreedV_time_db, GreedW_time_db, GreedF_time_db, Poly_time_db])
dfedit = pd.DataFrame([BaB_edit_ratio, Random_edit_ratio, Genetic_edit_ratio, GreedV_edit_ratio, GreedW_edit_ratio, GreedF_edit_ratio, Poly_edit_ratio])
dftimebrute = pd.DataFrame([brute_times_db, Backt_time_db, MiM_time_db])

filepath = 'BruteTIme.xlsx'
dftimebrute.to_excel(filepath, index=False)

#######################################
###    Multiple Knapsacks Results   ###
#######################################

no_items_multi_db = [10, 6, 10]

### 2. Greedy Results

# 2.1 Value-wise greedy
# Execution time for corresponding number of items
multigreedyV_time_db = [0.194072, 0.22697, 0.194072]

# Accuracy results
multigreedyV_accuracy_db = [91.6184, 100, 91.7827]

# 2.1 Weight-wise greedy
# Execution time for corresponding number of items
multigreedyW_time_db = [0.063896, 0.05507, 0.113964]

# Accuracy results
multigreedyW_accuracy_db = [92.6174, 83.87096, 92.71743]

# 2.1 Fractional greedy
# Execution time for corresponding number of items
multigreedyF_time_db = [0.1080036, 0.0848770, 0.1349449]

# Accuracy results
multigreedyF_accuracy_db = [97.718, 86.2478, 92.7174]

#######################################
#########       PLOTS      ############
#######################################

font = {'size'   : 18}
plt.rc('font', **font)

##### Time performance
# Bruteforce approaches
plt.figure()
plt.title("Execution time of the Bruteforce approaches")
plt.semilogy(brute_no_items_pg, brute_times_pg, marker='o', linestyle='dashed', label='Brute force')
plt.semilogy(brute_no_items_pg, Backt_times_pg, marker='o', linestyle='dashed', label='Backtracking')
plt.semilogy(brute_no_items_pg, MiM_times_pg, marker='o', linestyle='dashed', label='Meet in the Middle')
plt.xlabel("Number of items in the sack")
plt.xticks(range(3, 33, 3))
plt.legend()
plt.ylabel("Execution time (seconds)")
plt.grid('minor')
plt.show()

# Time performances of non bruteforce algorithms
plt.figure()
plt.title("Execution time of algorithms, uniformly distributed data")
plt.semilogy(GreedV_no_items_uni, GreedV_time_uni, marker='o', linestyle='dashed', label='Value-Greedy')
plt.semilogy(GreedV_no_items_uni, GreedW_time_uni, marker='o', linestyle='dashed', label='Weight-Greedy')
plt.semilogy(GreedV_no_items_uni, GreedF_time_uni, marker='o', linestyle='dashed', label='Fractional-Greedy')
plt.semilogy(GreedV_no_items_uni, Dynamic_time_uni, marker='o', linestyle='dashed', label='Dynamic')
plt.semilogy(GreedV_no_items_uni, TopDown_time_uni, marker='o', linestyle='dashed', label='Top-Down')
plt.semilogy(GreedV_no_items_uni, Poly_time_uni, marker='o', linestyle='dashed', label='Polynomial')
plt.semilogy(GreedV_no_items_uni, Random_time_nor, marker='o', linestyle='dashed', label='Randomized')
plt.semilogy(GreedV_no_items_uni, Genetic_time_uni, marker='o', linestyle='dashed', label='Genetic')
plt.legend()
plt.xlabel("Number of items to be arranged")
plt.xticks(range(10, 1100, 100))
plt.ylabel("Execution time (miliseconds)")
plt.grid('minor')
plt.show()

# Time performances of genetic algorithms
Genetic_no_ind = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010, 1110, 1210, 1310, 1410, 1510, 1610, 1710, 1810, 1910, 2010]
Genetic_time_ind = [0.023940086364746094, 0.25715041160583496, 0.6044480800628662, 1.0253541469573975, 1.7067828178405762, 2.174448251724243, 3.0660758018493652, 3.587392807006836, 4.9399847984313965, 5.649533987045288, 6.658737897872925, 7.722131013870239, 9.170852184295654, 10.78105115890503, 11.947166919708252, 13.377212047576904, 15.054158926010132, 16.901196002960205, 18.76530694961548, 20.74959087371826, 23.233350038528442]
plt.figure()
plt.title("Execution time of the genetic algorithm")
plt.semilogy(Genetic_no_ind, Genetic_time_ind, marker='o', linestyle='dashed')
plt.xlabel("Number of individuals")
plt.xticks(range(10, 2100, 100), rotation = 45)
plt.ylabel("Execution time (miliseconds)")
plt.grid('minor')
plt.show()

# Accuracy of algorithms

nom3=['BaB','Randomized','Genetic','GreedV','GreedW','GreedF','Poly']
plt.figure()
plt.title("Average accuracy of the algoritms")
plt.boxplot([BaB_accuracy_db, Random_accuracy_db, Genetic_accuracy_db, GreedV_accuracy_db, GreedW_accuracy_db, GreedF_accuracy_db, Poly_accuracy_db], patch_artist=True)
plt.ylabel("Accuracy")
plt.xticks(range(1,8),nom3)
plt.xlabel("Algorithm")
plt.grid('minor')
plt.show()

plt.figure()
plt.title("Average edit distance ratio")
plt.boxplot([BaB_edit_ratio, Random_edit_ratio, Genetic_edit_ratio, GreedV_edit_ratio, GreedW_edit_ratio, GreedF_edit_ratio, Poly_edit_ratio], patch_artist=True)
plt.ylabel("Edit distance ratio")
plt.xticks(range(1,8),nom3)
plt.xlabel("Algorithm")
plt.grid('minor')
plt.show()

plt.figure()
plt.title("Average accuracy of the greedy algorithms")
plt.boxplot([multigreedyV_accuracy_db, multigreedyW_accuracy_db, multigreedyF_accuracy_db], patch_artist=True)
plt.ylabel("Accuracy")
plt.xticks(range(1,4),['Value-Greedy', 'Weight-Greedy', 'Fractional-Greedy'])
plt.xlabel("Algorithm")
plt.grid('minor')
plt.show()

