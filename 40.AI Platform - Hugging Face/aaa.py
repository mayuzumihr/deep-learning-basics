import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image, ImageDraw
import requests

# モデルと特徴抽出器の読み込み
model_name = 'facebook/detr-resnet-50'
model = DetrForObjectDetection.from_pretrained(model_name)
feature_extractor = DetrImageProcessor.from_pretrained(model_name)

# 画像の読み込み
url = "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce"
image = Image.open(requests.get(url, stream=True).raw)

# 画像の前処理
inputs = feature_extractor(images=image, return_tensors="pt")

# 推論の実行
with torch.no_grad():
  outputs = model(**inputs)

# 推論結果の処理
target_sizes = torch.tensor([image.size[::-1]])
results = feature_extractor.post_process_object_detection(outputs, target_sizes=target_sizes)[0]

# 検出結果を画像に描画
draw = ImageDraw.Draw(image)
for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
  if score > 0.9:  # 確信度が0.9以上の検出結果のみ表示
    box = [round(i, 2) for i in box.tolist()]
    draw.rectangle(box, outline="red", width=3)
    draw.text((box[0], box[1]), f"{model.config.id2label[label.item()]}: {round(score.item(), 3)}", fill="red")

# 結果の表示
image.show()
