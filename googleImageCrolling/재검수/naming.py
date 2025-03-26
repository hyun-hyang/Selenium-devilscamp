import os
import re

# 현재 작업 디렉토리의 '지민' 폴더 경로
folder_path = os.path.join(os.getcwd(), '지민')

# '지민' 폴더 내의 폴더 목록 가져오기
folder_list = os.listdir(folder_path)

# '오전' 뒤의 모든 내용을 제거하는 함수
def remove_time_info(folder_name):
    print(f'처리 중인 폴더명: "{folder_name}"')  # 추가 디버깅 출력
    # '오전'이 포함된 경우, 그 뒤의 내용을 제거
    new_name = re.sub(r'오전.*$', '', folder_name).strip()
    print(f'원본: "{folder_name}" -> 수정: "{new_name}"')  # 디버깅 출력
    return new_name

# 각 폴더 이름에 대해 수정
for folder_name in folder_list:
    # 폴더명을 test_string으로 설정
    test_string = f"{folder_name}"
    print(f'원본 폴더명: "{test_string}"')

    # '오전' 뒤의 모든 내용을 제거
    new_name = remove_time_info(test_string)

    # 폴더의 전체 경로 생성
    old_folder_path = os.path.join(folder_path, folder_name)
    new_folder_path = os.path.join(folder_path, new_name)

    # 디버깅 출력을 추가
    print(f'원본 경로: {old_folder_path}')
    print(f'수정된 경로: {new_folder_path}')

    # 이름이 변경될 경우에만 변경
    if old_folder_path != new_folder_path and new_name:  # new_name이 비어 있지 않은지 확인
        try:
            os.rename(old_folder_path, new_folder_path)
            print(f'원본: {folder_name} -> 수정된: {new_name}')
        except Exception as e:
            print(f'변경 실패: {folder_name} -> {e}')
    else:
        print(f'변경 없음: {folder_name}')

# 테스트 문자열
test_string = '빈호아 푸옌 해변((Vinh Hoa Phu Yen Beach) 오전 10.09.30'

# '오전' 뒤의 모든 내용을 제거
result = re.sub(r'오전.*$', '', test_string).strip()
print(f'테스트 문자열 수정 결과: "{result}"')
