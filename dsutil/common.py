import findspark
import pyspark
import os
from matplotlib.font_manager import FontProperties

def create_spark():
    findspark.init()
    sc = pyspark.SparkContext()
    return sc

def get_zhfont():
    path = os.path.realpath(__file__)
    par_path = os.path.dirname(path)
    
    # zhfont1 = matplotlib.font_manager.FontProperties(fname=par_path + '/SimHei.ttf') 
    zhfont1 = FontProperties(fname=par_path + '/SimHei.ttf') 
    return zhfont1
