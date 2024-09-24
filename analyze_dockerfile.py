from dockerfile_parse import DockerfileParser

def analyze_dockerfile(file_path):
    parser = DockerfileParser()
    with open(file_path, 'r', encoding='utf-8') as f:
        parser.content = f.read()

    issues = []

    # 1. 베이스 이미지 확인 
    base_image = parser.baseimage
    if base_image.startswith("ubuntu") or base_image.startswith("debian"):
        issues.append(f"큰 베이스 이미지 사용 ({base_image}). Alpine 또는 Distroless 이미지를 추천합니다.")
    
    # 2. RUN 명령어 개수 확인
    run_commands = [inst for inst in parser.structure if inst['instruction'] == 'RUN']
    if len(run_commands) > 1:
        issues.append(f"{len(run_commands)}개의 RUN 명령어가 발견되었습니다. RUN 명령어를 결합해 레이어 수를 줄여보세요.")
    
    # 3. .dockerignore 파일의 필요성 확인
    if not any(inst['instruction'] == 'COPY' and '.' in inst['content'] for inst in parser.structure):
        issues.append("불필요한 파일이 포함될 가능성이 있습니다. .dockerignore 파일을 사용해 필수 파일만 포함하세요.")
    
    # 4. 멀티 스테이지 빌드
    if not any("AS" in inst['content'] for inst in parser.structure):
        issues.append("멀티 스테이지 빌드가 사용되지 않았습니다. 빌드 단계와 최종 이미지를 분리하여 최종 이미지 크기를 줄이세요.")
    
    # 5. 환경 변수 경고
    env_instructions = [inst for inst in parser.structure if inst['instruction'] == 'ENV']
    for inst in env_instructions:
        if "PASSWORD" in inst['content'] or "SECRET" in inst['content'] or "API_KEY" in inst['content']:
            issues.append("ENV에 민감한 정보(API 키, 비밀번호 등)가 포함되었을 수도 있습니다. 환경 변수나 .env 파일을 통해 민감한 정보를 관리하세요.")

    return issues



dockerfile_path = "./Dockerfile"  # 분석할 Dockerfile 경로 설정
issues_found = analyze_dockerfile(dockerfile_path)

if issues_found:
    print("🐳 Dockerfile 최적화 필요 사항:")
    for issue in issues_found:
        print(f"❗{issue}")
else:
    print("✅ Dockerfile이 최적화되었습니다.")
