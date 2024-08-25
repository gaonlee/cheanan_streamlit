import streamlit as st
import pandas as pd

st.markdown("<hr style='border: 2px solid #0078D7;'>", unsafe_allow_html=True)

st.markdown("## 📍관광 선진 사례 (1)")

st.markdown("### 펫츠고 트래블")

st.markdown("""
- 반려동물 동반 전문 여행사. 반려동물 좌석이 제공되는 버스, 열차, 제주 전세기를 이용해 관광 명소를 반려동물과 함께 여행할 수 있는 상품 제공
- 천안에도 반려동물 친화시설 중심 관광 코스 개발 후 상품 운영 가능
""")

image_path = "images/관광 선진 사례_1.png"
st.image(image_path, use_column_width=True)

st.markdown("<hr style='border: 2px solid #0078D7;'>", unsafe_allow_html=True)

st.markdown("## 📍관광 선진 사례 (2) - 반려동물 관광친화도시")

st.markdown("""
반려동물 관광친화도시: 반려동물과 함께 여행하면서 자유롭게 숙박, 체험, 쇼핑 등 관광활동이 가능한 곳, 
선정된 지자체는 최대 4년간 연간 국비 2억 5천만 원을 지원 받음
""")

data = {
    "지역": ["충남 태안군", "울산 광역시", "경기 포천시", "전남 순천시"],
    "선정시기 및 주요 콘텐츠": [
        "- 2023 선정\n- 반려견 동반 전용 천리포 해수욕장 운영, 꽃지 해수욕장 도그 클래스(도가<Dog+Yoga> 등)",
        "- 2023 선정\n- 울산 크리스마스 댕댕트레인, 반려동물 동반 고래바다 여행선 등 체험프로그램 등",
        "- 2024 선정\n- 포천 아트밸리에 반려동물 웰컴 센터 조성, 한탄강 도그지오 투어링 등",
        "- 2024 선정\n- 순천만국가정원에서 진행하는 체험형 캠핑 '펫-캠핑 인더 플라워 월드' 등"
    ],
    "비고": ["천안과 같은 충청남도에서 채택된 사례", "", "", ""]
}

df = pd.DataFrame(data)
st.table(df)

st.caption("출처: 이해리 기자, '2024년 반려동물 친화관광도시'로 포천시와 순천시 선정 [헬스조선], 2024.03.05.; 한국관광공사, '2023 반려동물 친화관광도시에 울산광역시, 태안군 선정', 보도자료, 2023.04.04.")

st.markdown("<hr style='border: 2px solid #0078D7;'>", unsafe_allow_html=True)


image_path = "images/태안 성공 사례.png"
st.image(image_path, use_column_width=True)

st.markdown("""
## 📌태안의 성공 사례를 참고,

# <span style="color:red;">천안을 반려동물 관광도시로</span>
""", unsafe_allow_html=True)

st.markdown("""
- 태안은 '2023 반려동물 친화관광도시' 공모에 최종 선정돼 20억 원(국비·지방비)을 확보
- 한국관광공사가 발표한 '반려동물 동반여행 활성화방안 연구'를 보면,\n
  반려동물 동반여행은 연간 약 1조 3960억 원의 경제적 파급효과가 추정
- 이러한 태안의 선진 사례를 참고하여 천안도 유사한 방향으로 나아가고자 함
""")

st.markdown("""
<div style="
    background-color: #e1eff6; 
    padding: 10px; 
    border-radius: 10px; 
    display: flex;
    align-items: center;">
    <div style="color: #1c64a8; font-size: 2.5em; font-weight: bold; margin-right: 10px;">
        정책<br>제언
    </div>
    <div style="font-size: 1.3em; font-weight: bold;">
        - 기존 문화시설(식당, 펜션 등)을 반려동물 친화시설로 전환하는데 대한 지원이 필요<br>
        - 이를 통해 천안은 반려동물과 함께할 수 있는 도시로 발전할 수 있으며,<br>
        이는 곧 지역 경제 활성화로 이어질 것으로 예상됨
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #0078D7;'>", unsafe_allow_html=True)

st.markdown("## 참고")

st.markdown("### 1) 포천시 반려동물 친화 관광숙소 인증 업체 모집")

st.markdown("""
| 항목 | 세부내용 |
| --- | --- |
| **개요** | - 모집명: 2024 포천시 반려동물 친화관광숙소 인증 업체 모집<br> - 접수기간: 2024.07.29.(월) ~ 2024.08.28.(수)<br> - 모집대상: 포천시 내 반려동물 동반 가능한 숙박업체 대상 |
| **선정 혜택** | - 포천시 반려동물 친화관광숙소 인증 현판 수여<br> - OTA를 활용한 마케팅 쿠폰 비용 지원, 업체 홍보 콘텐츠, 홍보카드 제작 등 온/오프라인 마케팅 지원 |
""")

st.markdown("### 2) 울산 반려동물 동반 숙박시설 시설개선 지원 사업 모집 공고")

st.markdown("""
| 항목 | 세부내용 |
| --- | --- |
| **개요** | - 모집명: 2024년 반려동물 동반 숙박시설 시설개선 지원 모집<br> - 접수기간: 2024.05.16.(목) ~ 2024.06.05(수)<br> - 모집대상: 50객실 정도(울산 소재 영업 신고 된 숙박업소) |
| **선정 혜택** | - 일반 객실을 반려동물 동반가능 객실로 전환하는데 필요한 시설개선비 지원<br> - 반려동물 계단 개당 10만원, 반려동물 침대 개당 5만원 이하 |
""")

st.markdown("### 3) 대전 반려동물 친화(Pet-Friendly) 인증 제도")

st.markdown("""
| 항목 | 세부내용 |
| --- | --- |
| **개요** | - 모집명: 대전 반려동물 친화(Pet-Friendly) 인증 제도<br> - 접수기간: 2023.06.16(금) ~ 2023.07.03(월)<br> - 모집대상: 대전 내 반려동물 친화적이며 반려동물 동반이 가능한 장소(관광지, 음식점, 숙박, 공원, 교육시설) |
| **선정 혜택** | - 대전 Pet-Friendly 인증 시설 현판 수여<br> - 시설 홍보 콘텐츠 제작<br> - 대전 반려동물 브로슈어 활용 시설 홍보 |
""")

st.markdown("<hr style='border: 2px solid #0078D7;'>", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style='text-align: left;'>2024 반려동물 친화관광도시 선정<br>('23~'27 총 10개소)</h2>
    """, unsafe_allow_html=True
)

st.image('images/2024 반려동물 친화관광도시 선정.png', caption="출처: 한국관광공사, '2024년 한국관광공사 사업 설명회 자료 배포', 2024.01.30")

st.markdown(
    """
    <div style='background-color: #e0f2f1; padding: 10px; border-radius: 10px;'>
        <ul>
            <li>천안 거주 중인 반려가구를 위한 문화시설 및 서비스 확대</li>
            <li>내부 만족도 제고 뿐 아니라, 관광객 유입 효과 또한 누릴 수 있음</li>
            <li>최종적으로 반려동물 관광친화도시로 확장, 지역관광산업의 부흥을 기대함</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)