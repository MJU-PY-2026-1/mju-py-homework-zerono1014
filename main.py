# 파일이름 : 2차 과제 코드
# 작 성 자 : 김도영

user_name = str(input("투자자 이름을 입력하시오: "))
seed_money = float(input("총 시드머니(자산)를 입력하세요: "))
stock_list = []
m_cap_list = []
total_invested = 0.0

print(f'\n[안내] {user_name}님의 포트폴리오 등록을 시작합니다. (종료 시 '종료' 입력)')

for i in range(1, 11):
  name = input(f'\n{i}번째 종목명을 입력하세요: ')
  if name == '종료':
    if len(stock_list) < 2:
      print('최소 2개 이상의 종목을 입력해야 합니다.')
      continue
    break
  m_cap = float(input(f'{name}의 시가총액을 입력하세요(조 단위): '))
  if m_cap <= 0:
    print("시가총액은 0보다 커야 합니다. 다시 입력하세요.")
    continue
  stock_list.append(name)
  m_cap_list.append(m_cap)
  if m_cap >= 10:
    grade = "대형주"
    if m_cap >= 100:
      grade = "초대형주"
  elif m_cap >= 1 and m_cap < 10:
    grade = "중형주"
  else:
    grade = "소형주"
  print(f">> {name}은 {graede}로 판정되었습니다.")

total_count = len(stock_list)
max_cap = max(m_cap_list)
top_stock_idx = m_cap_list.index(max_cap)
top_stock_name = stock_list[top_stock_idx]

print("\n" + "="*50)
print(f"[{user_name}님의 최종 포트폴리오 분석]")
print(f'-등록 종목 수: {total_count}개')
print(f'가장 체급이 큰 종목: {top_stock_name} (시총 {max_cap}조)')

print("-"*50)

for stock in stock_list:
  print(f'보유종목:{stock}')


# 파일이름: 3차 과제 코드
#작성자: 김도영

user_name = ""
seed_money = 0.0
stock_names = []
stock_m_caps = []
stock_grades = []

def register_stock():
  """1번 메뉴: 신규 종목을 입력받아 전역 리스트에 저장하는 함수"""
  global seed_money, user_name
  if user_name =="":
    user_name = str(input("투자자 이름을 등록하세요:"))
    seed_money = float(input("총 시드머니(원)을 입력하세요:"))
  print("\n--- [1. 신규 종목 등록] ---")
  while True:
    name = input("등록할 종목명을 입력하세요 (이전 메뉴로 가려면 'q' 입력): "))
    if name.lower() == 'q':
      break
    m_cap = float(input(f"{name}의 시가총액을 입력하세요(조 단위):"))
    if m_cap <= 0:
      print("⚠️ 시가총액은 0보다 커야 합니다. 다시 입력하세요.")
      continue
    # 체급 판정 지역 변수 사용 #
    if m_cap >= 10:
      grade = "대형주"
    elif m_cap >= 1:
      grade = "중형주"
    else:
      grade = "소형주"
    stock_names.append(name)
    stock_m_caps.append(m_cap)
    stock_grades.append(grade)
    print(f">> {name}({grade})이(가) 포트폴리오에 추가되었습니다.")


def display_portfolio():
  print("\n--- [2. 전체 보유 종목 조회] ---")
  if len(stock_names) == 0:
    print("❌ 현재 등록된 종목이 없습니다. 1번 메뉴에서 먼저 등록해주세요.")
    return #함수 조기 종료#
  print(f"현재 총 {len(stock_names)}개의 종목을 보유 중입니다.")
  print("-" * 40)
  for i in range(len(stock_names)):
    print(f"[{i+1}] {stock_names[i]:<10} | 체급: {stock_grades[i]:<5} | 시총: {stock_m_caps[i]:>5}조 원")
  print("-" * 40)


def analyze_assets(caps_list):
  """3번 메뉴용 연산 함수: 매개변수를 받아 연산 후 결과를 반환 (필수 요건 3,4번)"""
  total_m_cap = 0.0
  for cap in caps_list:
    total_m_cap += cap
  return total_m_cap


while True:
  print("\n" + "="*50)
  print("[스마트 주식 포트폴리오 시스템 V2.0]")
  print("="*50)
  print("1. 신규 종목 및 시가총액 등록 (Input)")
  print("2. 전체 보유 종목 및 체급 조회 (Print)")
  print("3. 포트폴리오 자산 배분 현황 (Calc)")
  print("0. 프로그램 종료 (Exit)")
  print("="*50)
  choice = input("원하시는 메뉴 번호를 입력하세요:")
  if choice == "1:":
    register_stock()
  elif choice == "2":
    display_portfolio()
  elif choice == "3":
    print("\n --- [3. 포트폴리오 자산 배분 현황] ---")
    if not stock_names:
      print("❌ 분석할 데이터가 없습니다.")
      continue
      total_result = analyze_assets(stock_m_caps)
      print(f"● 투자자 성함: {user_name}")
      print(f"● 설정 시드머니: {seed_monet: ,.0f}원")
      print(f"● 보유 주식 시가총액 총합: {total_result:.1f}조 원")
    elif choice == "0":
      print("프로그램을 안전하게 종료합니다.")
      break
    else:
      print("⚠️ 잘못된 입력입니다.")








