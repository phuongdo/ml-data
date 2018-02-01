# Benchmark


## Model 06 TestDate: 01/02/2018

Overall: (Positives: 88 imgs, Negatives :  164 imgs)

* TP: 49, FP: 39, FN : 20, TN : 42
* Sensitivity: TP/(TP+FN) = 	`41.18%`
* Specificity:  TN/(FP+ TN) = `84.00%`	
* Accuracy : `66.67%` 


See: https://www.medcalc.org/calc/diagnostic_test.php

DEBUG:

* test-pos: `https://github.com/phuongdo/ml-data/tree/master/hand-palm/test-pos`
```
URL	Label	Wrong
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_001.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_002.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_003.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_004.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_005.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_006.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_007.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_008.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_009.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_010.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_011.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_012.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_013.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_014.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_015.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_016.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_017.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_018.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_019.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_020.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_021.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_022.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_023.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_024.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_025.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_026.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_027.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_028.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_029.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_030.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_031.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_032.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_033.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_034.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_035.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_036.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_037.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_038.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_039.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_040.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_041.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_042.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_043.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_044.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_045.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_046.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_047.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_048.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_049.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_050.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_051.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_052.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_053.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_054.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_055.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_056.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_057.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_058.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_059.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_060.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_061.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_062.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_063.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_064.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_065.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_066.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_067.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_068.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_069.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_070.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_071.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_072.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_073.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_074.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_075.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_076.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_077.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_078.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_079.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_080.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_081.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_082.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_083.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_084.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_085.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_086.jpg	positive
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_087.jpg	negative	x
https://raw.githubusercontent.com/phuongdo/ml-data/master/hand-palm/test-pos/IMG_088.jpg	positive

* test-neg:`https://github.com/phuongdo/ml-data/tree/master/hand-palm/test-neg`

```
URL	Label	Wrong

```

* Sensitive cases:

```
URL	Label	Wrong

```


