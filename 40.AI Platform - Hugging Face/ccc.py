import torch
from transformers import DetrFeatureExtractor, DetrModel
from PIL import Image
import requests

# モデルと特徴抽出器の読み込み
model_name = 'facebook/detr-resnet-50'
model = DetrModel.from_pretrained(model_name)
feature_extractor = DetrFeatureExtractor.from_pretrained(model_name)

# 画像の読み込み
url = "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce"
image = Image.open(requests.get(url, stream=True).raw)

# 画像の前処理
inputs = feature_extractor(images=image, return_tensors="pt")

# 推論の実行
with torch.no_grad():
  outputs = model(**inputs)

# 特徴量の抽出
features = outputs.last_hidden_state

# 特徴量の表示
print("特徴量の形状:", features.shape)
print("特徴量:", features)
