# WORD RECOMMEND

## Folder structure
- data <br>
  -- data_19_9_2023.txt <br>
  -- tokenizer.picker <br>
  -- vietnamese-stopwords.txt <br>
  -- word_dict.txt <br>
- pretrain <br>
  -- word_recommendation.h5 <br>
- src <br>
  -- config.py <br>
  -- datsets.py <br>
  -- inference.py <br>
  -- model.py  <br>
  -- test.py  <br>
  -- train.py <br>
  -- train_model.ipynb <br>
  -- word_recommend_api.py <br>
-index.html <br>
-requirement.txt <br>


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


  
