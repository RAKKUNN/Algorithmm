# Algorithmm

**Algorithmm**은 알고리즘 문제 풀이를 구조적으로 관리하기 위한 저장소입니다.
프로그래밍 언어와 문제 플랫폼별로 풀이를 정리하며, 문제 디렉토리를 자동 생성하는 스크립트와 테스트 실행 스크립트를 포함하고 있습니다.
아래는 레포지토리 구조와 사용 방법에 대한 설명입니다.

---

## 📂 레포지토리 구조

* **`solutions/`** – 실제 문제 풀이 코드가 들어가는 곳

  * 언어별 하위 폴더 존재: `py`(Python), `cpp`(C++), `go`(Go)
  * 각 언어 폴더 안에 플랫폼별 폴더 존재: 예) `leet/` (LeetCode), `boj/` (백준)
  * 문제 디렉토리명: `<id>-<slug>` (예: `1-two-sum`)
  * 내부 파일:

    * `main.py|cpp|go` → 실제 풀이 코드
    * `README.md` → 문제 설명/풀이 메모
    * `cases.txt` → 테스트 케이스 모음

* **`templates/`** – 언어별 템플릿 코드가 저장된 폴더

  * `templates/py/main.py`, `templates/cpp/main.cpp`, `templates/go/main.go`
  * 메타데이터(문제 정보, 시간복잡도 등)와 최소 실행 코드가 포함
  * 새로운 문제 생성 시 `new.py` 스크립트가 이 템플릿을 복사해 사용

* **`scripts/`** – 자동화 도구

  * **`new.py`** : 새 문제 디렉토리 및 템플릿 코드 자동 생성
  * **`test.sh`** : `cases.txt` 기반 자동 테스트 실행

---

## ➕ 문제 추가 방법

`scripts/new.py` 스크립트를 실행하면 새로운 문제 폴더가 자동 생성됩니다.

**사용법:**

```bash
python scripts/new.py <platform> <id> "<title>" <url> \
  [--lang {python|cpp|go}] [--tags TAGS] [--time TIME] [--space SPACE] [--status STATUS] [--date YYYY-MM-DD]
```

**예시:**

```bash
python scripts/new.py leet 1 "Two Sum" https://leetcode.com/problems/two-sum --lang python --tags "array,hash-table"
```

**인자 설명:**

* `<platform>` : 플랫폼 코드 (예: `leet`, `boj`, `pgm`)
* `<id>` : 문제 번호 (예: `1`)
* `<title>` : 문제 제목 (`" "`로 감싸기)
* `<url>` : 문제 링크
* `--lang` : 언어 선택 (`python`, `cpp`, `go`, 기본은 Python)
* `--tags` : 문제 태그 (예: `"array,hash-table"`)
* `--time` / `--space` : 시간/공간 복잡도 (선택, 기본 `?`)
* `--status` : 상태 (`draft` / `solved`, 기본 `draft`)
* `--date` : 날짜 (기본값은 오늘 날짜)

실행하면 자동으로:

* `solutions/<lang>/<platform>/<id>-<slug>/` 디렉토리 생성
* 해당 언어 템플릿 기반 `main` 코드 파일 생성
* 빈 `README.md`, `cases.txt` 파일 생성

---

## 📝 테스트 케이스 작성 규칙 (`cases.txt`)

각 문제 디렉토리에는 **`cases.txt`** 파일이 있어야 합니다.
테스트 케이스는 아래 규칙에 따라 작성합니다:

* 입력을 그대로 작성 (여러 줄 가능)
* 구분자 `---` 를 입력/출력 사이에 작성
* 그 아래에 예상 출력 작성
* 여러 케이스는 **빈 줄**로 구분

**예시:**

```
2 3
---
5

4 5
---
9
```

* **테스트 케이스 1:** 입력 `2 3`, 출력 `5`
* **테스트 케이스 2:** 입력 `4 5`, 출력 `9`

---

## ▶ 테스트 실행 방법

풀이와 `cases.txt`를 준비했다면, `scripts/test.sh`로 자동 검증할 수 있습니다.

**사용법:**

```bash
./scripts/test.sh <lang> <platform> <problem_dir_name>
```

**예시:**

* Python : `./scripts/test.sh py leet 1-two-sum`
* C++    : `./scripts/test.sh cpp leet 1-two-sum`
* Go     : `./scripts/test.sh go leet 1-two-sum`

**동작 방식:**

* Python → `python main.py` 실행
* C++ → `g++ main.cpp` 컴파일 후 실행
* Go → `go build main.go` 빌드 후 실행
* `cases.txt`의 입력을 실행 결과와 비교 → PASS/FAIL 출력

실행 후 요약 결과:

```
Case 1: PASS
Case 2: FAIL
...
Passed: 3/4, Failed: 1/4
```

---

✅ 이 워크플로우(문제 추가 → 풀이 작성 → 케이스 작성 → 테스트 실행)를 따라가면, 효율적으로 알고리즘 문제 풀이를 관리하고 검증할 수 있습니다.

---