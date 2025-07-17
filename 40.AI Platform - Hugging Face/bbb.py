import torch
from transformers import DetrImageProcessor, DetrForSegmentation
from PIL import Image, ImageDraw, ImageFont
import requests

# モデルと特徴抽出器の読み込み
model_name = 'facebook/detr-resnet-50-panoptic'
model = DetrForSegmentation.from_pretrained(model_name)
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
processed_outputs = feature_extractor.post_process_panoptic_segmentation(outputs, target_sizes=[image.size[::-1]])[0]

# セグメンテーション結果の取得
segments_info = processed_outputs["segments_info"]
segmentation = processed_outputs["segmentation"].numpy()

# セグメンテーション結果を画像に描画
draw = ImageDraw.Draw(image)
unique_labels = np.unique(segmentation)

for segment in segments_info:
  if segment['score'] > 0.85:  # スコアが0.85以上のセグメントのみ表示
    mask = segmentation == segment['id']
    bbox = np.array(np.nonzero(mask))
    ymin, xmin = bbox.min(axis=1)
    ymax, xmax = bbox.max(axis=1)
    draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
    draw.text((xmin, ymin), f"{model.config.id2label[segment['label_id']]}: {segment['score']:.2f}", fill="red")

# 結果の表示
image.show()
