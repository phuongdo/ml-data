# Benchmark


## Model 01 TestDate: 22/01/2018

Overall: (Positives: 24 imgs, Negatives :  62 imgs)

* TP: 14, FP: 8, FN : 20, TN : 42
* Sensitivity: TP/(TP+FN) = 	`41.18%`
* Specificity:  TN/(FP+ TN) = `84.00%`	
* Accuracy : `66.67%` 


See: https://www.medcalc.org/calc/diagnostic_test.php

DEBUG:

* test-pos: `https://github.com/phuongdo/ml-data/tree/master/hand-palm/test-pos`
```
URL																							Label		Wrong
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_001.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_002.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_003.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_004.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_005.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_006.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_007.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_008.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_009.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_010.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_011.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_012.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_013.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_014.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_015.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_016.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_017.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_018.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_019.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_020.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_021.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_022.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_023.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_024.jpg	positive

* test-neg:`https://github.com/phuongdo/ml-data/tree/master/hand-palm/test-neg`

```
URL																							Label		Wrong
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_001.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_002.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_003.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_004.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_005.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_006.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_007.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_008.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_009.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_010.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_011.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_012.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_013.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_014.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_015.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_016.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_017.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_018.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_019.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_020.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_021.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_022.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_023.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_024.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_025.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_026.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_027.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_028.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_029.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_030.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_031.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_032.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_033.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_034.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_035.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_036.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_037.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_038.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_039.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_040.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_041.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_042.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_043.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_044.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_045.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_046.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_047.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_048.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_049.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_050.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_051.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_052.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_053.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_054.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_055.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_056.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_057.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_058.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_059.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_060.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_061.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-neg/IMG_062.jpg	negative
```

Sensitive cases:
```

URL																							Label		Wrong
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_001.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_002.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_003.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_004.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_005.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_006.jpg	positive	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_007.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_008.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_009.jpg	negative
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-sen/IMG_010.jpg	negative
```


