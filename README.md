# WORD RECOMMEND

## Introduction
Word recommendation system is a system that supports real-time text suggestions. When users use the "space" + "`", a series of suggested paragraphs will appear. The number of suggestions displayed and the number of suggested words are pre-set. word recommendation system will help users operate faster during the typing process



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
For training and testing, you should use ```git clone``` for 
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
#### Train
For training, you need to check the data path is set in ```config.py```. After training, you can check the model in the pretrain folder.
If you don't want to train on local. You can use ```train_model.ipynb``` to train on Google colab and download the training results saved as a ```.h5``` file.<br>
To training on local:
```
python train.py
```

#### Inference
To test the trained model, run the ```inference.py``` file. When running this file you can type your text , number of suggestions displayed and number of suggested words.
```
python inference.py
```

#### Application
To use web application, run word_recommend_api.py
```
python word_recommend_api.py
```
Get your local IP address from the active session, then update line 31 in the index.html file with this IP. Finally, open the index.html file in your browser to run web application.


  
