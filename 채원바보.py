import streamlit as st

st.title("제목 : st.title()")
st.header("헤더 : st.header()")
st.subheader("서브헤더 : st.subheader()")
st.text("본문 텍스트 : st.text()")
st.markdown("## 마크다운 : st.markdown()")
st.caption("캡션(작고 흐린 글씨로 표현됨) : st.caption()")
# st.write(): 텍스트/마크다운/데이터/차트 등 거의 모든 것 출력
st.write("# 마크다운 H1 : st.write()")
st.write("### 마크다운 H3 : st.write()")
st.write("")  # 빈 줄 추가
# st.write(): 텍스트/마크다운/데이터/차트 등 거의 모든 것 출력
st.write("# 마크다운 H1 : st.write()")
st.write("### 마크다운 H3 : st.write()")
st.write("")  # 빈 줄 추가

# 색이 있는 텍스트
st.write(":red[빨간색 텍스트]")
st.write(":blue[파란색 텍스트]")

# 형식 있는 텍스트
st.code('print("Hello, World!")', language="python", line_numbers=True)

with st.echo():
    name = "Chunghun Ha"
    st.write("Hello, Streamlit!", name)

st.latex(r'\int_a^b f(x)dx')
st.divider()
st.write(
    """
### 마크다운 헤더3
- 마크다운 목록1. **굵게** 표시
- 마크다운 목록2. *기울임* 표시
  - 마크다운 목록2-1
  - 마크다운 목록2-2

### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 인용
> 인용문: "Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다."

### 마크다운 표
| 헤더1 | 헤더2 |
|---|---|
| 데이터1 | 데이터2 |
"""
)

st.code(
    """
def hello_world():
    print("Hello, World!")
""",
    language="python"
)
import streamlit as st

st.success("성공 메시지입니다")
st.info("정보 안내 메시지입니다")
st.warning("경고 메시지입니다")
st.error("에러 메시지입니다")
x = 5

if x > 0:
    st.success("x는 양수입니다")
else:
    st.error("x는 0 이하입니다")
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "이름": ["A", "B", "C"],
    "점수": [85, 90, 78],
    "합격여부": ["O", "O", "X"]
})
st.dataframe(df)
st.dataframe(df, use_container_width=True)
st.write("데이터 크기:", df.shape)
st.write("컬럼 목록:", df.columns.tolist())

st.line_chart(df["점수"])

st.subheader("부산 구별 ㎡당 전세보증금 지도")

html_path = r"busan_전세_㎡당_보증금.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=700, scrolling=True)

### :orange[다운로드 버튼: st.download_button()]

with open("busan_전세_㎡당_보증금.html", "r", encoding="utf-8") as file:
    html_data = file.read()

st.download_button(
    label="부산 전세 지도 HTML 다운로드",
    data=html_data,
    file_name="busan_전세_㎡당_보증금.html",
    mime="text/html"
)
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")

if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]}을 선택하였습니다.")

import streamlit as st

### :orange[체크박스]
check = st.checkbox('여기를 체크하세요')
if check:
    st.write('체크되었습니다.')

### :orange[라디오 버튼]
radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(radio + '가 선택되었습니다.')

### :orange[셀렉트 박스]
select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(select + '가 선택되었습니다.')

### :orange[멀티 셀렉트 박스]
multi = st.multiselect(
    '여러 개를 선택하세요',
    ['선택 1', '선택 2', '선택 3'],
    default=['선택 1']
)
st.write('선택한 값:', multi)

### :orange[슬라이더 (단일 값)]
slider_val = st.slider(
    '값을 선택하세요',
    min_value=0,
    max_value=100,
    value=50,
    step=5
)
st.write('선택한 값:', slider_val)

### :orange[슬라이더 (범위)]
range_val = st.slider(
    '범위를 선택하세요',
    min_value=0,
    max_value=100,
    value=(20, 80)
)
st.write('선택한 범위:', range_val)

### :orange[숫자 입력]
number = st.number_input(
    '숫자를 입력하세요',
    min_value=0,
    max_value=100,
    value=10,
    step=1
)
st.write('입력한 숫자:', number)

### :orange[텍스트 입력]
text = st.text_input('텍스트를 입력하세요')
st.write('입력한 텍스트:', text)

### :orange[날짜 입력]
date = st.date_input('날짜를 선택하세요')
st.write('선택한 날짜:', date)

### :orange[파일 업로더]
file = st.file_uploader('파일을 업로드하세요')
if file is not None:
    st.write('업로드한 파일명:', file.name)

### :orange[사이드바 - 셀렉트]
st.sidebar.header('사이드바')
side_select = st.sidebar.selectbox(
    '사이드바 선택',
    ['A', 'B', 'C']
)
st.write('사이드바 선택값:', side_select)

### :orange[사이드바 - 슬라이더]
side_slider = st.sidebar.slider(
    '사이드바 슬라이더',
    0, 100, 30
)
st.write('사이드바 슬라이더 값:', side_slider)
import streamlit as st

if st.button("풍선 띄우기"):
    st.balloons()
import streamlit as st

if st.button("눈 내리기"):
    st.snow()
import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("증가"):
    st.session_state.count += 1

st.write(st.session_state.count)
import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0
import streamlit as st

if "option" not in st.session_state:
    st.session_state.option = "A"

option = st.selectbox(
    "선택",
    ["A", "B", "C"],
    index=["A", "B", "C"].index(st.session_state.option)
)

st.session_state.option = option
st.write(option)

import streamlit as st
import time

@st.cache_data
def long_running_function(param1):
    time.sleep(5)
    return param1 * param1

start = time.time()

# 숫자 입력은 입력된 값을 반환
num_1 = st.number_input('입력한 숫자의 제곱을 계산합니다.')

st.write(
    f'num_1의 제곱은 {long_running_function(num_1)} 입니다. '
    f'계산시간은 {time.time() - start:.2f}초 소요'
)

st.write('🚀 :green[캐싱이 적용되면 동일 계산은 저장된 결과를 사용하여 빠르게 처리함]')

