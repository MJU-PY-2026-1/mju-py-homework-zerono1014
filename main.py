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

# [과제 4차] 이중 리스트 및 파일 입출력 기반 포트폴리오 관리 시스템 V3.0

import os

# 1. 전역 변수 (이중 리스트 활용)
user_name = ""
seed_money = 0.0
# 데이터 구조: [ [종목명, 현재가, 보유주수, 시가총액, 체급], ... ]
portfolio_2d = [] 

def load_portfolio():
    global user_name, seed_money, portfolio_2d
    try:
        # 프로그램 시작 시 파일에서 데이터 불러오기
        with open("portfolio.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                user_name, seed_money_str = lines[0].strip().split(',')
                seed_money = float(seed_money_str)
                
                # 중첩된 데이터를 이중 리스트 형태로 복구
                for line in lines[1:]:
                    data = line.strip().split(',')
                    if len(data) == 5:
                        portfolio_2d.append([data[0], float(data[1]), float(data[2]), float(data[3]), data[4]])
        print(f"✨ [성공] {user_name}님의 저장된 포트폴리오를 불러왔습니다!")
    
    except FileNotFoundError:
        # 예외 처리 1: 파일이 없을 경우 비정상 종료 방지
        print("💡 [안내] 저장된 포트폴리오 파일이 없습니다. 새 자산 관리를 시작합니다.")

def register_stock():
    global user_name, seed_money
    
    if user_name == "":
        user_name = input("\n투자자 이름을 등록하세요: ")
        # 반복문(while)을 사용하여 올바른 숫자가 입력될 때까지 계속 질문
        while True:
            try:
                seed_money = float(input("총 시드머니(원)를 입력하세요: "))
                if seed_money <= 0:
                    print("⚠️ 시드머니는 0보다 커야 합니다.")
                    continue
                break # 성공적으로 입력받으면 루프 탈출
            except ValueError:
                print("❌ [입력 오류] 정확한 숫자(금액)를 입력해주세요!")

    print("\n--- [1. 신규 종목 등록] ---")
    while True:
        name = input("등록할 종목명을 입력하세요 (이전 메뉴는 'q'): ")
        if name.lower() == 'q':
            break
            
        try:
            # 예외 처리: 숫자 입력란에 문자가 들어올 경우 방어
            price = float(input(f"{name}의 현재가(원): "))
            shares = float(input(f"{name}의 보유 주수(주): "))
            m_cap = float(input(f"{name}의 시가총액(조 단위): "))
        except ValueError:
            print("❌ [입력 오류] 가격, 주수, 시가총액은 반드시 '숫자'로 입력해주세요!")
            continue

        # 체급 판정
        if m_cap >= 10:
            grade = "대형주"
        elif m_cap >= 1:
            grade = "중형주"
        else:
            grade = "소형주"

        # 새로운 항목을 이중 리스트에 누적[cite: 2]
        portfolio_2d.append([name, price, shares, m_cap, grade])
        print(f">> {name}({grade}) 데이터가 이중 리스트에 저장되었습니다.")

def display_portfolio():
    print("\n--- [2. 전체 보유 종목 조회] ---")
    if not portfolio_2d:
        print("❌ 등록된 종목이 없습니다.")
        return

    print(f"현재 총 {len(portfolio_2d)}개의 종목이 관리 중입니다.")
    print("-" * 75)
    # 중첩 for문을 대신하는 리스트 인덱싱 기반 이중 순회 및 표 포맷팅 출력
    for i in range(len(portfolio_2d)):
        name = portfolio_2d[i][0]
        price = portfolio_2d[i][1]
        shares = portfolio_2d[i][2]
        grade = portfolio_2d[i][4]
        invested = price * shares # 개별주 투자액 계산
        print(f"- {name:<10} | 체급: {grade:<4} | 현재가: {price:>8,.0f}원 | 보유: {shares:>6.2f}주 | 투자액: {invested:>10,.0f}원")
    print("-" * 75)

def analyze_assets():
    print("\n==================================================")
    print("🔍 현재 포트폴리오 자산 배분 실시간 진단")
    print("==================================================")
    if not portfolio_2d:
        print("❌ 분석할 데이터가 없습니다.")
        return
        
    total_invested = 0.0
    # for문을 통해 이중 리스트의 누적 연산 진행
    for stock in portfolio_2d:
        total_invested += stock[1] * stock[2]
        
    cash = seed_money - total_invested
    inv_ratio = (total_invested / seed_money) * 100
    cash_ratio = (cash / seed_money) * 100
    
    print(f" [총 자산 보유 현황]")
    print(f" • 총 시드머니 : {seed_money:,.0f} 원")
    print(f" • 주식 투자액 : {total_invested:,.0f} 원 ({inv_ratio:.1f}%)")
    print(f" • 잔여 현금   : {cash:,.0f} 원 ({cash_ratio:.1f}%)")
    print("==================================================")

def show_report():
    print("\n***************************************************************************")
    print(f" 📊 {user_name} 투자자님의 맞춤형 포트폴리오 리밸런싱 리포트")
    print("***************************************************************************")
    if not portfolio_2d:
        print("❌ 분석할 데이터가 없습니다.")
        return
        
    # 체급별 분류
    large = [row for row in portfolio_2d if row[4] == "대형주"]
    mid = [row for row in portfolio_2d if row[4] == "중형주"]
    small = [row for row in portfolio_2d if row[4] == "소형주"]
    
    # 보유 상황에 따른 목표 비율 분배 설정
    l, m, s = bool(large), bool(mid), bool(small)
    if l and m and s: weights = (60, 25, 15)
    elif l and m: weights = (70, 30, 0)
    elif l and s: weights = (80, 0, 20)
    elif m and s: weights = (60, 40, 0)
    elif l: weights = (100, 0, 0)
    elif m: weights = (0, 100, 0)
    elif s: weights = (0, 0, 100)
    else: weights = (0, 0, 0)

    print(f" [자산 배분 가이드] 위기 대응을 위한 [현금 20% 확보]를 최우선으로 권장합니다.")
    print(f" 주식에 투자되는 나머지 80% 자산 내에서 [{weights[0]}% : {weights[1]}% : {weights[2]}%] 비율을 제안합니다.")
    print("-" * 75)
    print(f" {'종목명':<10} | {'체급':<4} | {'현재 주수':>9} | {'권장 주수':>9} | {'행동 지침':<15}")
    print("-" * 75)
    
    total_invested = 0.0
    
    for row in portfolio_2d:
        name, price, current_shares, m_cap, grade = row
        total_invested += price * current_shares
        
        if grade == "대형주": p_weight = weights[0] / len(large)
        elif grade == "중형주": p_weight = weights[1] / len(mid)
        else: p_weight = weights[2] / len(small)
        
        # 총 시드머니의 80%만 주식 투자에 활용하도록 기준금액 설정
        stock_seed_money = seed_money * 0.8
        target_amount = stock_seed_money * (p_weight / 100)
        
        if price > 0:
            target_shares = target_amount / price
        else:
            target_shares = 0.0
            
        diff = target_shares - current_shares
        
        # 훈수(행동 지침) 판단 알고리즘
        if diff > 0:
            action = f"▶ {diff:>6.2f}주 추가 매수"
        elif diff < 0:
            action = f"▼ {abs(diff):>6.2f}주 부분 매도"
        else:
            action = "● 현재 비중 적정"
            
        print(f" {name:<10} | {grade:<4} | {current_shares:>8.2f}주 | {target_shares:>8.2f}주 | {action}")
        
    print("-" * 75)
    
    current_cash = seed_money - total_invested
    target_cash = seed_money * 0.2
    print(f" 💰 [현금 확보 지침] 현재 잔여 현금: {current_cash:,.0f}원 ➡️ 목표 보유 현금: {target_cash:,.0f}원")
    print("***************************************************************************")

def save_portfolio():
    # 이중 리스트를 파일에 쓰기 (Write 기능)
    with open("portfolio.txt", "w", encoding="utf-8") as f:
        f.write(f"{user_name},{seed_money}\n")
        for row in portfolio_2d:
            f.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")
    print("\n💾 [저장 완료] 포트폴리오 데이터가 'portfolio.txt'에 안전하게 저장되었습니다.")

# 메인 실행 로직: 함수 호출 위주의 간결한 구성
print("==================================================")
print(" ✨ 파이썬 기반 스마트 자산 배분 시스템 V3.0 ✨")
print("==================================================")
load_portfolio()

while True:
    print("\n1. 신규 종목 등록 (이중 리스트 저장)")
    print("2. 전체 종목 조회 (투자액 계산 출력)")
    print("3. 포트폴리오 자산 배분 진단")
    print("4. 최적 포트폴리오 리포트 (자산 리밸런싱)")
    print("0. 저장 및 프로그램 종료")
    
    choice = input("메뉴 번호를 입력하세요: ")
    
    if choice == "1":
        register_stock()
    elif choice == "2":
        display_portfolio()
    elif choice == "3":
        analyze_assets()
    elif choice == "4":
        show_report()
    elif choice == "0":
        save_portfolio()
        print("프로그램을 안전하게 종료합니다. 대박 나세요!")
        break
    else:
        print("⚠️ 잘못된 입력입니다. 다시 선택해주세요.")






