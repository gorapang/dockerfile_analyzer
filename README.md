# Dockerfile Analyzer 🐳

**Dockerfile Analyzer**는 주어진 Dockerfile을 분석하여 최적화 포인트를 찾아내고, 이를 기반으로 최적화 권장 사항을 제시하는 도구입니다. Dockerfile 내의 불필요한 명령어, 비효율적인 사용 방식, 보안 위험 요소를 감지하여 사용자가 최적화된 Dockerfile을 작성할 수 있도록 도와줍니다.

<br>

## 기능 ✨
1. **베이스 이미지 분석**: 큰 이미지를 사용하는 경우 경고하고, alpine 등 경량 이미지 사용을 권장
2. **RUN 명령어 최적화**: 여러 개의 `RUN` 명령어가 있을 경우 이를 결합해 레이어 수를 줄이는 것을 추천
3. **.dockerignore 파일 필요성 경고**: `COPY` 명령어로 인해 불필요한 파일이 포함될 가능성을 경고하고 `.dockerignore` 사용 권장
4. **멀티 스테이지 빌드 확인**: 멀티 스테이지 빌드를 사용하지 않은 경우 권장
5. **환경 변수 민감 정보 경고**: `PASSWORD`, `SECRET`, `API_KEY`와 같은 민감한 정보가 포함된 경우 경고

<br>

## 사용 방법 🚀


### 1. Python으로 실행

**실행환경**: 
- 🐍 Python 3.12.4

```bash
pip install -r requirements.txt
python analyze_dockerfile.py
분석할 Dockerfile의 경로를 입력하세요: /path/to/Dockerfile
```
`/path/to/Dockerfile`에 실제 경로를 넣어주세요.

### 2. Docker로 실행

**실행환경**: 
- 🐧 Ubuntu 22.04
- 🐋 Docker version 27.3.1, build ce12230

```
docker run -v /path/to/your/local/Dockerfile:/app/Dockerfile -it jeongju/dockerfile-checker:5.0
```
`/path/to/your/local/Dockerfile`에 실제 경로를 넣어주세요.

`/app/Dockerfile`은 수정하지 마세요!

<br>

## 프로그램 출력 예시

예시: 최적화가 필요한 Dockerfile
```
🐳 Dockerfile 최적화 필요 사항:
❗ 큰 베이스 이미지 사용 (ubuntu:20.04). Alpine 또는 Distroless 이미지를 추천합니다.
❗ 4개의 RUN 명령어가 발견되었습니다. RUN 명령어를 결합해 레이어 수를 줄여보세요.
❗ 불필요한 파일이 포함될 가능성이 있습니다. .dockerignore 파일을 사용해 필수 파일만 포함하세요.
❗ 멀티 스테이지 빌드가 사용되지 않았습니다. 빌드 단계와 최종 이미지를 분리하여 최종 이미지 크기를 줄이세요.
❗ ENV에 민감한 정보(API 키, 비밀번호 등)가 포함되었을 수도 있습니다. 환경 변수나 .env 파일을 통해 민감한 정보를 관리하세요.
```

<br>

예시: 최적화된 Dockerfile
```
✅ Dockerfile이 최적화되었습니다.
```
