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
