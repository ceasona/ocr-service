# ocr-service

### 命令方式启动服务

- 安装

  ```
  pip install -r requirements.txt -i "https://pypi.douban.com/simple/"
  ```

- 启动

  ```
  python manage.py runserver
  ```

  conf/ocr_service.yaml 为配置文件路径



### 镜像方式启动

- 构建镜像

  ```
  docker build -f ocr-service/Dockerfile . -t ceasona250/ocr-service:v1
  ```

- 启动

  ```
  docker run -d -it --net=host --name "ocr_srv" ceasona250/ocr-service:v1
  ```

- 停止&删除

  ```
  docker stop ocr_srv && docker rm ocr_srv
  ```



命令行方式识别图片：

```
python tools/infer/predict_system.py --image_dir="./test/demo.jpg" --det_model_dir="./mypaddle/inference/ch_ppocr_mobile_v1.1_det_infer/"  --rec_model_dir="./mypaddle/inference/ch_ppocr_mobile_v1.1_rec_infer/"  --vis_font_path="./static/website/fonts/simfang.ttf"
```



### 参考：

1. PaddleOCR  https://github.com/PaddlePaddle/PaddleOCR/tree/develop

