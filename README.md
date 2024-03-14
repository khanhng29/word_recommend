# WORD RECOMMEND

## Folder structure
- data <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- data_19_9_2023.txt <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- tokenizer.picker <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- vietnamese-stopwords.txt <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- word_dict.txt <br>
- pretrain <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- word_recommendation.h5 <br>
- src <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- config.py <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- datsets.py <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- inference.py <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- model.py  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- test.py  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- train.py <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- train_model.ipynb <br>
  &nbsp;&nbsp;&nbsp;&nbsp;-- word_recommend_api.py <br>
- index.html <br>
- requirement.txt <br>


## Installation
For training and testing, you should use ``` git clone``` for 
installing all necessary packages.
### For anaconda3:
```
conda create -y -n word_recommend python=3.11
conda activate word_recommend
git clone https://github.com/khanhng29/word_recommend.git
cd word_recommend
pip install -r requirement.txt
cd ./src
```
#### Training
```
python train.py
```

#### Inference 
```
python inference.py
```

#### Application
```
python word_recommend_api.py
```


  
