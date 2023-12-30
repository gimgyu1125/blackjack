
import pygame #외부모듈이나 패키기를 가져옴
import random
import time

WIDTH, HEIGHT = 900, 900#카드x,y좌표설정

#색깔코드
BlACK = (0,0,0)
WHITE = (255,255,255)
GREEN = "#1F5C23"
YELLOW = ("#FFEB3B")
Pcard_sum=0
#Num=0



pygame.init()#라이브러리 초기화
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # 화면위치설정
pygame.display.set_caption("BLACKJACK")#게임이름 설정
myFont = pygame.font.SysFont(None, 30)#pygame 폰트 호출
img=pygame.image.load("20230804_232701.png")
img=pygame.transform.scale(img,(300,300))
game_text1 = myFont.render("PLAYER", True, WHITE)#폰트 변수생성 이떄 Ture는 사용여부를 묻는것
game_text2 = myFont.render("DEALER", True, WHITE)
start_taxt1= myFont.render("press any key to start", True, WHITE)
start_text2 = myFont.render("ESC : Quit",True,WHITE)
start_text3= myFont.render("Welcome to blackjack",True,YELLOW)
pscore_text = myFont.render(f"player : {Pcard_sum}",True,WHITE)
player_lose = myFont.render("LOSE! Press ESC",True,YELLOW)
player_win= myFont.render("WIN! Press ESC",True,YELLOW)
game_draw = myFont.render("DRAW",True,YELLOW)
Enter = myFont.render("Press Enter Key!",True,YELLOW)


result = 0 # 1 : player win 2: player lose

image_file = [                             #카드리스트 생성(조커제외)
    'ace_of_diamonds.png',
    '2_of_diamonds.png',
    '3_of_diamonds.png',
    '4_of_diamonds.png',
    '5_of_diamonds.png',
    '6_of_diamonds.png',
    '7_of_diamonds.png',
    '8_of_diamonds.png',
    '9_of_diamonds.png',
    '10_of_diamonds.png',
    'ace_of_clubs.png',
    '2_of_clubs.png',
    '3_of_clubs.png',
    '4_of_clubs.png',
    '5_of_clubs.png',
    '6_of_clubs.png',
    '7_of_clubs.png',
    '8_of_clubs.png',
    '9_of_clubs.png',
    '10_of_clubs.png',
    'ace_of_spades.png',
    '2_of_spades.png',
    '3_of_spades.png',
    '4_of_spades.png',
    '5_of_spades.png',
    '6_of_spades.png',
    '7_of_spades.png',
    '8_of_spades.png',
    '9_of_spades.png',
    '10_of_spades.png',
    'ace_of_hearts.png',
    '2_of_hearts.png',
    '3_of_hearts.png',
    '4_of_hearts.png',
    '5_of_hearts.png',
    '6_of_hearts.png',
    '7_of_hearts.png',
    '8_of_hearts.png',
    '9_of_hearts.png',
    '10_of_hearts.png',
    'jack_of_clubs2.png',
    'jack_of_diamonds2.png',
    'jack_of_hearts2.png',
    'jack_of_spades2.png',
    'king_of_clubs2.png',
    'king_of_diamonds2.png',
    'king_of_hearts2.png',
    'king_of_spades2.png',
    'queen_of_clubs2.png',
    'queen_of_diamonds2.png',
    'queen_of_hearts2.png',
    'queen_of_spades2.png',
]

hidden_image_file = ''   #뒤집힌카드

Pcard_images = []#플레이어 카드 리스트 생성
Pcard_sum = 0 #처음 플레이어카드 초기값

Dcard_images = []#딜러 카드리스트 생성
Dcard_sum = 0#딜러카드 합

standOff = True
ending = 0

def cardToNum(card_path:str):#카드 숫자 설정 함수
    if card_path[0]=='a':         #image_file 리스트의 변수의 0번째 자리가 a라면 에이스카드 이므로 1로 정함
        return 1
    elif card_path[0]=='j'or card_path[0]=='k'or card_path[0]=='q':  #j,k,q라면 10처리
        return 10
    else:
        if card_path[0:2]=="10": #문자열 "10"이라면 정수형으로 변환하여 반환
            return int(card_path[0:2]) # 0번째 문자부터 2번째 문자까지를 확인하여 카드의 숫자를 추출
        return int(card_path[0]) #그렇지 않다면 0번째 문자를 정수형으로 변환하여 반환

def point_sum(pord): # pord = "p" or "d"  #플레이어 혹은 딜러의 점수를 합해주는 함수
    answer = 0                    #점수저장하는 변수
    if pord == "p":               #.p라면 카드를받음
        lst = Pcard_images
    else :                        #D라면 카드를받음
        lst = Dcard_images
    for i in lst:               #리스트 속 카드의 숫자를 총합
        answer += cardToNum(i) #,각 카드 이미지에 대해 cardToNum 함수를 호출하여 카드의 숫자를 가져옴
    return answer



def start(): # intro
    screen.blit(start_taxt1, (WIDTH/2-170, HEIGHT/ 2-50)) #start_taxt1을 가로/2-170,높이/2-50만큼 설정
    screen.blit(start_text2, (WIDTH / 2-170, HEIGHT / 2))
    screen.blit(start_text3,(WIDTH/2-130, HEIGHT /2-90))
    screen.blit(img,(WIDTH/2-170,10))
    pygame.image.load(image_file[0])
    pygame.display.flip() #화면 업데이트
    running = True


    while 1: #계속진행
        for event in pygame.event.get(): #이벤트 처리 루프생성
            if event.type == pygame.KEYDOWN: #지금 처리중인 이벤트가 키를 눌렀을떄인지 확인
                if event.key == pygame.K_ESCAPE: #누른키가 esc인지확인
                    return 0 #맞다면 루프종료
                else:
                    return 1#아니면 계속진행
            if event.type == pygame.QUIT: #종료버튼(윈도우 키 혹은 X버튼)눌렀을떄
                return 0 #루프종료

#def end():# 게임 마무리함수
    #pass#아직 정하지 않아서 pass처리
def draw_card(x, y, image_path): #카드 뽑아주고 스크린에 올려주는 함수
    picture = pygame.image.load(image_path) # image_path를 이용해 이미지를 picture에 로드함
    picture = pygame.transform.scale(picture, (picture.get_size()[0] / 4, picture.get_size()[1] / 4))#카드크기정해줌
    screen.blit(picture, (x, y))#카드위치설정

def hit(): # 히트라는 버튼 눌렀을때 함수설정
    global Pcard_sum #플레이어카드값 전역변수에 접근
    i = 0# 루프를하기위한 변수생성

    while i < 1:
        ri = random.randint(0, len(image_file) - 1) #새카드 뽑아주는 변수생성
        if not image_file[ri]: #해당이미지가 사용됬다면
            i -= 1 #감소시켜 다시뽑음
        else:
            Pcard_images.append(image_file[ri]) #플레이어 카드이미지 리스트에 뽑힌카드이미지 넣기
            p_x_positions.append(p_x_positions[-1]+50) #뽑힌카드 x좌표설정
            draw_card(p_x_positions[-1],p_y_position, Pcard_images[-1]) #카드띄움
            Pcard_sum += cardToNum(Pcard_images[-1]) #뽑힌 카드의 숫자를 플레이어카드값에 더함
            image_file[image_file.index(Pcard_images[-1])] = None #사용했다고 처리
            break #끝나면 멈추기
        print(Pcard_images)
        i += 1 #무한반복 끄기
    print(Pcard_sum) #확인을위한 값 프린트
    pscore_text = myFont.render(f"player : {Pcard_sum}", True, BlACK) #카드총합 을 띄우는 폰트
    pygame.draw.rect(screen, WHITE, (750, 455, 110, 30))
    screen.blit(pscore_text, (WIDTH / 1.2, 455)) #띄우기



def standon():
    global Dcard_sum,ending
    pygame.draw.rect(screen, GREEN,(d_x_positions[1],d_y_position, 180,230))
    draw_card(d_x_positions[-1],d_y_position,hidden_image_file)
    Dcard_sum += cardToNum(hidden_image_file)
    pygame.draw.rect(screen, WHITE, (750, 20, 110, 30))
    dscore_text = myFont.render(f"dealer : {Dcard_sum}", True, BlACK)
    screen.blit(dscore_text, (WIDTH / 1.2, 20))
    pygame.display.flip()
    pygame.time.delay(1000)
    # 히든카드 오픈 + 화면에 이쁘게 출력

    while True:
        if Dcard_sum >= 17:
            break
        i = 0
        randomInt = random.randint(0, len(image_file) - 1)
        while i < 1:
            if not image_file[randomInt]:
                i -= 1
                randomInt = random.randint(0, len(image_file) - 1)
            else:
                Dcard_images.append(image_file[randomInt])
                d_x_positions.append(d_x_positions[-1] + 50)
                draw_card(d_x_positions[-1], d_y_position, Dcard_images[-1])
                image_file[image_file.index(Dcard_images[-1])] = None
                Dcard_sum+=cardToNum(Dcard_images[-1])
            i += 1
        pygame.draw.rect(screen, WHITE, (750, 20, 110, 30))
        dscore_text = myFont.render(f"dealer : {Dcard_sum}", True, BlACK)
        screen.blit(dscore_text, (WIDTH / 1.2, 20))
        pygame.display.flip()
        pygame.time.delay(1000)
    ending = 1

if start(): #게임시작했을때
    running = True #시스템 돌아가도록 설정
    screen.fill(GREEN) #바탕화면은 초록색
    pygame.draw.line(screen, BlACK,(0,HEIGHT/2), (WIDTH,HEIGHT/2), 5) #딜러와 플레이어 구분을 위한 검은 줄 중간에 넣기
    pygame.draw.rect(screen, WHITE,(45, 500, 70, 40)) #player hit x : 45 ~ 115 , y : 50 ~ 90 #히트 버튼 박스만들기
    pygame.draw.rect(screen,WHITE,(45,560,74,40))#스탠드 박스
    hit_text = myFont.render("HIT",True,BlACK) #히트 글자 생성
    stand_text = myFont.render("STAND",True,BlACK)#스탠드 글자 생성
    screen.blit(hit_text,(63.5,510)) #띄우기
    screen.blit(stand_text,(49,570))
    #player start
    screen.blit(game_text1, (WIDTH/102,HEIGHT/1.987))#플레이어 글자 띄우기
    screen.blit(game_text2, (WIDTH/102,HEIGHT/100))#딜러 글자 띄우기




    random_card_indexes = random.sample(range(len(image_file)), 2) # 2개의 랜덤 카드 인덱스 선택 .......?,두 개의 매개변수받음,2는 샘플 개수로, 즉 몇 개의 랜덤한 요소를 선택할지를 나타냄
    p_x_positions = [WIDTH/2-60, WIDTH/2-10]  # 카드의 x 좌표
    p_y_position = 500  # 모든 카드는 y 좌표 50에 위치
    i = 0 #루프를 위한 변수생성
    while i < 2:
        if not image_file[random_card_indexes[i]]: #한번더쓴건지확인
            i -= 1#맞다면 다시 뽑게함
        else:
            Pcard_images.append(image_file[random_card_indexes[i]])#아니다면 플레이어 이미지 리스트에 넣고
            draw_card(p_x_positions[i],p_y_position, Pcard_images[i])#카드위치정하고 띄우고
            image_file[image_file.index(Pcard_images[-1])] = None#썻다고 알리기
        i += 1# 무한루프방지


    d_x_positions = [WIDTH / 2 - 60, WIDTH / 2 - 10]  # 카드의 x 좌표 # step 50 d_x_postions.append(d_x_positions[-1]+50)
    d_y_position = 200  # 모든 카드는 y 좌표 50에 위치
    i = 0 #플에이어와 같은 방법으로 진행
    randomInt = random.randint(0, len(image_file) - 1)
    while i < 1:
        if not image_file[randomInt]:
            i -= 1
            randomInt = random.randint(0, len(image_file) - 1)
        else:
            Dcard_images.append(image_file[randomInt])
            draw_card(d_x_positions[0], d_y_position, Dcard_images[i])
            image_file[image_file.index(Dcard_images[-1])] = None
        i += 1
    randomInt = random.randint(0, len(image_file) - 1)
    i = 0  # 플에이어와 같은 방법으로 진행
    while i < 1:
        if not image_file[randomInt]:
            i -= 1
            randomInt = random.randint(0, len(image_file) - 1)
        else:
            hidden_image_file = image_file[randomInt]
            image_file[image_file.index(hidden_image_file)] = None
        i += 1
    Pcard_sum += point_sum("p")#포인트합계 함수 호출해서 플레이어 합계냄
    Dcard_sum += point_sum("d")#딜러카드 점수함계
    draw_card(d_x_positions[1], d_y_position, 'pngwing.com.png')#히든카드나타내기
    pygame.display.flip()#화면 업데이트
    print(Pcard_sum)#확인을위한 플레이어 카드 총합계산 없어도됨
    print(Dcard_sum)
    print(cardToNum(hidden_image_file))

    while running: # 이게 끝나면 게임 종료
        if not ending:
            pygame.draw.rect(screen, WHITE, (750, 455, 110, 30))#점수가 계속 겹쳐나와서 원래점수가릴 초록사각형만듬 #계속 덧칠해서 전에점수가릴계획
            pscore_text = myFont.render(f"player : {Pcard_sum}",True,BlACK) #흰색말고 검은색으로 정함
            screen.blit(pscore_text, (WIDTH / 1.2, 455))#위치정하고 나타내기
            pygame.draw.rect(screen, WHITE, (750, 20, 110, 30))
            dscore_text = myFont.render(f"dealer : {Dcard_sum}", True, BlACK)
            screen.blit(dscore_text, (WIDTH / 1.2, 20))
            pygame.display.flip()#업데이트
        for event in pygame.event.get(): # 키보드, 마우스 입력 판단.#start함수랑 같은 역할을 함 이건 게임하고있을때
            if event.type == pygame.QUIT:
                running = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:# 마우슬 클릭했을때 이벤트 확인
                if event.pos[0] >= 45 and event.pos[0] <= 115 and event.pos[1] >= 500 and event.pos[1] <= 540 and standOff: #버튼누룰수있는 범위설정
                    hit()#히트함수 호출
                if event.pos[0] >= 42 and event.pos[0] <= 118 and event.pos[1] >= 555 and event.pos[1] <= 630 and standOff: #스탠드 버튼 범위
                    pygame.draw.rect(screen, GREEN,(45, 500, 70, 40))
                    pygame.draw.rect(screen, GREEN, (45,560,74,40))
                    standOff = False #스탠드 눌렀을때 더이상 히트 작동X
                    print("stand")
                    standon()
                    pygame.display.flip()
        if Pcard_sum >21: #Dcard_sum-21<Dcard_sum-21:#플레이어 카드합이 21넘으면 멈추기
            ending = 1
            result = 2
            running = 0
        elif Dcard_sum>21: #Pcard_sum-21>Dcard_sum-21
            ending = 1
            result = 1
            running = 0
        elif ending :
            if Dcard_sum > Pcard_sum :
                result = 2
            elif Dcard_sum < Pcard_sum :
                result = 1
            else :
                result = 3
            ending = 1
            running = 0
        pygame.display.flip() #화면업데이트

if ending :
    running = 1
    screen.blit(Enter, (WIDTH / 2.5, HEIGHT / 2))
    while running :
        for event in pygame.event.get():  # esc 눌럿을때 running을 멈춤
            if event.type == pygame.QUIT:
                running = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
                elif event.key == pygame.K_RETURN:
                    screen.fill(BlACK)
                    if result == 1:
                        screen.blit(player_win, (WIDTH / 2.5, HEIGHT / 2))
                    elif result == 2:
                        screen.blit(player_lose, (WIDTH / 2.5, HEIGHT / 2))
                    elif result == 3:
                        screen.blit(game_draw,(WIDTH / 2.5, HEIGHT / 2))
        pygame.display.flip()
pygame.quit()
