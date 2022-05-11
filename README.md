# Acachu

<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/acachu.png?raw=true' height='400' width='400'>

<br>

## 1. 조원 소개
- 조우석(조장), 김규혁, 김동현, 윤지혜, 이성주, 이은성

<br>

## 2. 📢 서비스 소개
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/serviceflow.png?raw=true'>

<br>

## 3. :link: 선정 배경
 > - 코로나로 인한 개인 카페 폐업률 상승과 상권 경쟁 심화
 > - 대형 프랜차이즈 카페보다 개인 운영 카페에 대한 수요 증가
<!-- <img src='C:\Users\User\Desktop\최종 프로젝트\Acachu\readmeImage\bg1.png?raw=true'>
<img src='C:\Users\User\Desktop\최종 프로젝트\Acachu\readmeImage\bg2.png?raw=true'> -->
<!-- <img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/background.PNG?raw=true' height='400'> -->

<br>

## 4. 💾 ERD
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/erd.png?raw=true'>

<br>

## 5. :fire: 기대 효과
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/effect.png?raw=true' height='350'>

<br>

## 6. 📸 UI/UX
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/main_ui.PNG?raw=true' height='442'>

<br>

## 7. 🔎 사용자 기능
<!-- <img src='C:\Users\User\Desktop\최종 프로젝트\Acachu\readmeImage\utils.png?raw=true'> -->

### 7.1 게스트(비로그인)
- 추천 기능

### 7.2 일반 사용자
- 댓글 기능
- 북마크 기능
- 추천 기능
- 프로필 관리
 
### 7.3 업주
- 댓글 기능
- 북마크 기능
- 추천 기능
- 프로필 관리
- 업장관리 페이지

### 💻 AI 기능
- 🎞 이미지 분류 기능
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/image_classification.PNG?raw=true'>

- 📃 카테고리 분류 기능
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/review_classification.PNG?raw=true' width='923'>


## 8. 💽 사용법
- 모델 파일 : https://drive.google.com/file/d/1zxllSLgHfCMIFafWk3bUIBBvoi49ucMi/view?usp=sharing

1. acahcu repository를 클론 한 뒤 프로젝트 폴더 내에 acachu.zip을 여기에 풀기로 풀어주세요
2. settings.py 파일을 프로젝트폴더 안 config 폴더에 넣어주세요
3. redis 설치파일로 redis를 설치하세요(https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504,  Redis-x64-3.0.504.msi)
4. requirements.txt 를 이용해 아나콘다 가상환경을 설정해주세요
5. 프로젝트 폴더에서 아나콘다 프롬프트로 python manage.py runserver 명령을 통해 장고 서버를 실행해주세요
6. 아나콘다 프롬프트를 하나 더 실행해서 프로젝트 폴더 내로 이동 후 celery -A config worker -l info -P eventlet 명령을 입력해주세요

<br>

