# facenet_mask
#model ※ファイルの配置は，facenet_mask/facenet_model, facenet_mask/mask_detect/mask_detector.model
https://drive.google.com/drive/folders/1rmUHukt40TcTBX8U2G-avaoWtjP2v2Gm?usp=sharing


#環境構築
pip install -r requirements.txt

#マスクあり・なし判別用のモデル作成(/mask_detect/train_mask_detector.py)
python train_mask_detector.py

#顔の登録(/facenet/register.sh)
bash register.sh

#カメラを用いて顔識別(./camera.sh)
bash camera.sh
