import os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# 전역 폰트 경로 설정
font_path = None

def setup_fonts():
    global font_path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_dir, 'fonts', 'NanumSquareL.otf')
    
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
    plt.rcParams['axes.unicode_minus'] = False
