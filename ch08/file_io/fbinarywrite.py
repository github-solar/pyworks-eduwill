#바이너리 파일 - 텍스트가 아닌 파일. 음성, 화상, 이미지등등

#바이너리 파일 생성 출력은 이미지 파일로 실습해야 한다.

with open('data.bin', 'wb') as f:
    text = '날씨가 덮다'
    f.write(text.encode())


with open('data.bin', 'rb') as f:
    data = f.read()
    text = data.decode()
    print(text)
