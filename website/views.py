import json
import subprocess
from django.shortcuts import render
from . import models
import os
from . import utils
from ocr.settings import BASE_DIR
from conf import config
from website.logger_mgr import LoggerMgr
__dir__ = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR, 'logs/ocr-service.log')
ocr_logger = LoggerMgr(filename=log_path)


# Create your views here.


def home(request):
    return render(request, 'website/home.html', )


def recognition(request):
    obj = request.FILES.get("file")
    name = utils.Tools.create_name() + os.path.splitext(str(obj))[1]
    ocr_logger.debug(f'upload {name}')
    utils.Tools.check_dir(os.path.join(BASE_DIR, "upload_data"))
    file_path = os.path.join("upload_data", name)
    f = open(file_path, 'wb')
    for i in obj.chunks():
        f.write(i)
    f.close()
    json_param = {
        "image_dir": file_path,
        "det_model_dir": "./mypaddle/inference/ch_ppocr_mobile_v1.1_det_infer/",
        "rec_model_dir": "./mypaddle/inference/ch_ppocr_mobile_v1.1_rec_infer/",
        "vis_font_path": os.path.join(BASE_DIR, 'static', 'website', 'fonts', 'simfang.ttf')
    }
    obj = models.Task.objects.create(input=json.dumps(json_param))
    json_param['det_db_task_id'] = obj.id
    basic_params = utils.Tools.construct_params(json_param)
    basic_args = [config.conf['python_env']['bin'], '-u', 'tools/infer/predict_system.py'] + basic_params
    ocr_logger.debug(basic_args)
    p = subprocess.Popen(basic_args, close_fds=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b""):
        try:
            try:
                msg = str(line, encoding="utf8").strip("\r").strip("\n")
            except:
                msg = str(line, encoding="gbk").strip("\r").strip("\n")
        except Exception as e:
            msg = str(e)
        ocr_logger.info(msg)
    return render(request, "website/home.html",
                  {"msg": models.Task.objects.get(id=obj.id).output, "image": f'website/inference_results/{name}'})
