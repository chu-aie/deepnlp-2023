# 기말 프로젝트 보고서
	Generative Agents (NPC 상호작용 프로그램)

	_Prepared by: 김도현_202021009_

# 초기 목표 설명
- llama2 활용

-  다중 AI NPC 상호작용 게임 프로그램의 개발을 목표

- 플레이어가 다양한 상호작용 가능한 AI NPC들을 통해 자연스럽고 현실적인 게임세계를 경험할 기회를 제공하는 것이 목적

# 해당 프로젝트 작동 내용
- Python 3.9.12.

- pip install -r requirements.txt

- api 설정
```python
# API Key 입력
openai_api_key = "___"

# 이름 입력
key_owner = "___"

# 경로 설정
maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# 디버그 출력
debug = True
```

- Environment 서버 실행
```
python manage.py runserver
```

- Simulation 서버 실행
```
python reverie.py
```

```
base_the_ville_isabella_maria_klaus
```
```
test-simulation
```

- 시뮬레이션 실행 및 저장
```
run <step-count>
```

- 작동 캡쳐 사진
<p align="center" width="100%">
<img src="project_cap.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

# 결론
	위 내용 및 해당 보고서 전부 불필요.
	
	프로젝트 기간 동안 예상치 못한 사건들로 인한 프로젝트 진행 실패
	
# LINK
- [Generative Agents](https://github.com/joonspk-research/generative_agents/tree/main)
