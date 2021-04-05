import random
import string
import os


class Tools(object):

    @staticmethod
    def check_dir(dirname):
        """
        检测目录是否存在，不存在则创建
        :param dirname:
        :return:
        """
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return dirname

    @staticmethod
    def create_name():
        name = ''
        for i in range(15):
            s = string.ascii_letters
            r = random.choice(s)
            name += r
        return name

    @staticmethod
    def construct_params(json_parm):
        params = ['image_dir', 'det_model_dir', 'rec_model_dir', 'det_db_task_id', 'vis_font_path']
        basic_args = []
        for param in params:
            if json_parm.get(param):
                basic_args.append(f"--{param}")
                basic_args.append(str(json_parm[param]))
        bool_params = ['is_debug']
        for param in bool_params:
            if json_parm.get(param):
                basic_args.append(f"-{param}")
        return basic_args
