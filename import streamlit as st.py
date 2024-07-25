import streamlit as st
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Anthropic API 키 설정
anthropic = Anthropic(api_key='your_api_key_here')

# 페이지 제목 설정
st.title("회사 업무 교육 웹사이트")

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:")

# 제출 버튼
if st.button("제출"):
    # Claude API에 질문 전송
    response = anthropic.completions.create(
        prompt=f"{HUMAN_PROMPT} {user_input}{AI_PROMPT}",
        model="claude-2.1",
        max_tokens_to_sample=300
    )
    
    # 응답 표시
    st.write("Claude의 응답:")
    st.write(response.completion)

# 파일 업로더 추가
uploaded_file = st.file_uploader("교육 자료를 업로드하세요 (TXT 파일)", type="txt")

if uploaded_file is not None:
    # 파일 내용 읽기
    file_contents = uploaded_file.read().decode("utf-8")
    st.write("파일 내용:")
    st.write(file_contents)

    # 여기에 파일 내용을 Claude API에 전송하는 코드를 추가할 수 있습니다
    # 예: 파일 내용을 Claude의 컨텍스트로 사용