import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = "fonts/NanumSquareL.otf"  # 폰트 경로
fontprop = fm.FontProperties(fname=font_path)

# 데이터 로드
DATA_PATH = "data"  # 실제 데이터 경로로 변경하세요
df_card_1 = pd.read_csv(f"{DATA_PATH}/TOTAL_BC1_MM_CCND_CUST_CRTR_CCND_CSPT_SGG_MG.csv", encoding='cp949')
df_card_2 = pd.read_csv(f"{DATA_PATH}/TOTAL_BC1_MM_CCND_CUST_CRTR_CCND_EXCL_LC_CSPT_SGG_MG.csv", encoding='cp949')
df_card_3 = pd.read_csv(f"{DATA_PATH}/TOTAL_BC1_MM_CCND_EXCL_RSDT_CRTR_CCND_CSPT_SGG_MG.csv", encoding='cp949')
df_card_4 = pd.read_csv(f"{DATA_PATH}/TOTAL_BC1_MM_LC_CRTR_TOBIZ_SLS_SZ_MG.csv", encoding='cp949')

# Streamlit 레이아웃 구성
st.title("기타 참고자료")

# 시군구별 전체이용건수 시각화
st.subheader("시군구별 전체이용건수")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_card_1['시군구명'], df_card_1['전체이용건수'], color='skyblue')
ax.set_xlabel('시군구명', fontproperties=fontprop)
ax.set_ylabel('전체이용건수', fontproperties=fontprop)
ax.set_title('시군구별 전체이용건수', fontproperties=fontprop)
ax.set_xticklabels(df_card_1['시군구명'], rotation=45, ha='right', fontproperties=fontprop)
st.pyplot(fig)

# 시군구별 전체이용금액 시각화
st.subheader("시군구별 전체이용금액")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_card_1['시군구명'], df_card_1['전체이용금액'], color='orange')
ax.set_xlabel('시군구명', fontproperties=fontprop)
ax.set_ylabel('전체이용금액', fontproperties=fontprop)
ax.set_title('시군구별 전체이용금액', fontproperties=fontprop)
ax.set_xticklabels(df_card_1['시군구명'], rotation=45, ha='right', fontproperties=fontprop)
st.pyplot(fig)

# 천안시 동남구 연도별 시각화
region_name = '천안시 동남구'
df_region = df_card_1[df_card_1['시군구명'] == region_name]
df_region['기준연월'] = df_region['기준연월'].astype(str)
df_region['년도'] = df_region['기준연월'].str[:4]

st.subheader(f"{region_name} 연도별 이용건수 및 이용금액")
years = ['2019', '2020', '2021', '2022', '2023']

for year in years:
    st.markdown(f"**{year}년**")
    df_year = df_region[df_region['년도'] == year]
    x = np.arange(len(df_year['기준연월']))

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 첫 번째 y축 (이용건수) 막대 그래프
    color = 'tab:blue'
    ax1.set_xlabel('기준연월', fontproperties=fontprop)
    ax1.set_ylabel('전체이용건수', color=color, fontproperties=fontprop)
    ax1.bar(x - 0.2, df_year['전체이용건수'], width=0.4, color=color, label='전체이용건수')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(x)
    ax1.set_xticklabels(df_year['기준연월'], fontproperties=fontprop)

    # 두 번째 y축 (이용금액) 막대 그래프
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('전체이용금액', color=color, fontproperties=fontprop)
    ax2.bar(x + 0.2, df_year['전체이용금액'], width=0.4, color=color, label='전체이용금액')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    st.pyplot(fig)

# 천안시 서북구 연도별 시각화
region_name = '천안시 서북구'
df_region = df_card_1[df_card_1['시군구명'] == region_name]
df_region['기준연월'] = df_region['기준연월'].astype(str)
df_region['년도'] = df_region['기준연월'].str[:4]

st.subheader(f"{region_name} 연도별 이용건수 및 이용금액")
for year in years:
    st.markdown(f"**{year}년**")
    df_year = df_region[df_region['년도'] == year]
    x = np.arange(len(df_year['기준연월']))

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 첫 번째 y축 (이용건수) 막대 그래프
    color = 'tab:blue'
    ax1.set_xlabel('기준연월', fontproperties=fontprop)
    ax1.set_ylabel('전체이용건수', color=color, fontproperties=fontprop)
    ax1.bar(x - 0.2, df_year['전체이용건수'], width=0.4, color=color, label='전체이용건수')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(x)
    ax1.set_xticklabels(df_year['기준연월'], fontproperties=fontprop)

    # 두 번째 y축 (이용금액) 막대 그래프
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('전체이용금액', color=color, fontproperties=fontprop)
    ax2.bar(x + 0.2, df_year['전체이용금액'], width=0.4, color=color, label='전체이용금액')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    st.pyplot(fig)
