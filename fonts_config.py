import os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# 전역 폰트 경로 설정
font_path = None

def setup_fonts():
    global font_path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_dir, 'fonts', 'NanumSquareL.otf')
    
    print(f"폰트 경로: {font_path}")  # 경로 확인을 위해 추가
    
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"폰트 파일을 찾을 수 없습니다: {font_path}")
    
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
    plt.rcParams['axes.unicode_minus'] = False
