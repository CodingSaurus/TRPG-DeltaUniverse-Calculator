import random

#아스트랄 이름 입력
astral = int(input("캐릭터 명수 입력 : "))
astral_name = []

for count in range(1, astral+1) :
    print(count,"번째 캐릭터 이름을 입력받습니다.") #3명보다 많아야 함. 적을 경우 오류.
    name = input("입력 : ")
    astral_name.append(name)
print("참전 캐릭터 목록 : ", astral_name) 


boss_targetEnd = 4 #보스 타겟팅 끝 숫자
boss_skillOnOff = False
battleround = 1 #라운드

boss_name = "대적점 화산의 에너미" #지우고 이름 넣어도 됨
boss_hp = 100000 #지우고 체력 숫자 넣어도 됨
boss_dmg_one = [4000, 4500, 5000] #지우고 숫자 넣어도 됨
boss_dmg_con = [2000, 2500, 3000]  #지우고 숫자 넣어도 됨
boss_dmg_all = [1000, 1200, 1400] #지우고 숫자 넣어도 됨


while boss_hp > 0 :

    boss_target = random.randint(1, boss_targetEnd) #보스가 서있는 자리
    boss_atkType = random.randint(1, 6) #보스 공격유형 개수
    
    boss_atkTarget = random.sample(astral_name, 3)
    
    boss_dmgType = random.randint(0, 2) #보스 공격데미지
    boss_dmgType_skill = random.randint(0,4) #보스 1스킬 공격 추가 데미지
    boss_atk = "" #단일/광역/조건부 들어갈 자리


    if boss_atkType >= 5 :
        boss_atk = "광역"

    elif boss_atkType >= 3:
        boss_atk = "단일"

    else :
        boss_atk = "일부"


    #이하 출력되는 부분! 건들지 말 것!
    
    print()
    print("[", battleround, "라운드를 시작합니다. ]" )

    #단일공격 패턴
    if boss_atk == "단일" :

        print()

        if boss_atkType == 3 :
            boss_atk = input("에너미의 공격 대상 선택 후 입력 (ex. 단일 공격 > 캐릭터이름) :")
            print()
            print("거칠게 마모된 부리가 날카로운 소리를 내며 부딪힙니다. 암빛 불꽃이"
            "아른거리는가 싶더니 어느새 (해당 캐릭터 or 최전방에 서있는..등) 의 눈앞에 서서 빠른 속도로 부리를"
            "내려꽂습니다.")

            #단일3 헤더
            print()
            print("[", battleround, "라운드 결과 ]")
            print()
            print(boss_name, ":", boss_atk, "/ 타겟팅 위치[ ★ :", boss_target, "]")

            print("> 인당 대미지 -", boss_dmg_one[boss_dmgType], "HP.")
            

        if boss_atkType == 4 :
            print("협곡의 가장자리를 움켜쥐고있던 발톱이 떨어집니다. 후두둑, 돌이 굴러내리고 스산한 한기를 지닌"
            "그것은 길게 뻗어져", boss_atkTarget[0], "(의 신체부위)를 거칠게 베어냅니다. 벌어진 상흔 사이로 살아있는 영이라면 가질"
            "수 없는 냉기가 파고듭니다.")

            #단일4 헤더
            print()
            print("[", battleround, "라운드 결과 ]")
            print()
            print(boss_name, ":", boss_atk, "공격 >", boss_atkTarget[0], "/ 타겟팅 위치[ ★ :", boss_target, "]")

            print("> 인당 대미지 -", boss_dmg_one[boss_dmgType], "HP.")
        


    #일부 공격 패턴
    if boss_atk == "일부" :

        print()
       
        if boss_atkType == 1 : 
            print("길게 늘어뜨려진 꼬리가 크게 반원을 그리며 휘둘러집니다. 인위적으로 생성된 소용돌이에 의해 협곡 "
            "위에 흩어져있던 어두운 불꽃을 품은 날개깃이 허공에 드리우고, 곧 몇몇 캐릭터 ("
            , boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2],") 을 향해 격추됩니다.")
            
        if boss_atkType == 2 :
            print("바람이 이는 소리와 함께 캐릭터들의 머리위로 거대한 날개가 장막마냥 "
            "드리웁니다. 별빛마저 허락하지 않는 완전한 어둠은 곁에 서있던 동료마저 식별하지 못하게 만듭니다. 그때, ",
            boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2], "와 몇 발자국 떨어진 거리에서 작은 불꽃이 피어오릅니다.")

        print()
        print("[", battleround, "라운드 결과 ]")
        print()
        print(boss_name, ":", boss_atk, "공격 >", boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2], "/ 타겟팅 위치[ ★ :", boss_target, "]")

        print("> 인당 대미지 -", boss_dmg_con[boss_dmgType], "HP.")
        
            



    #광역 공격 패턴
    if boss_atk == "광역" :

        print()
       
        if boss_atkType == 5 : #특수스킬
            print("거대한 에너미가 고개를 치켜들고 폭풍과도 같은 울음소리를 냅니다. 협곡 안의 검은 용암이 "
            "부글부글 끓다가 화염과 함께 온 사방으로 흘러내리며 터져나갑니다. 하늘로 치솟아 올라간 화산탄들이 일제히 "
            "캐릭터들의 주변으로 쏟아져 내립니다. 모두가 정신 없는 가운데" , boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2],
            "의 앞으로 돌덩이들이 쾅쾅 내리꽂히며 움직임이 저지됩니다.")
            boss_skillOnOff == True

        if boss_atkType == 6 : #특수스킬
            print("두 쌍의 불꽃 날개가 펄럭이며 강한 바람을 사방으로 뻗어냅니다. 흐름에 따라 출렁이던 "
            "먼지구덩이가 서로간의 인력을 이기지 못하고 무너져내립니다. 그 틈 사이로 뿜어 올라온 용암이 기둥을 이루며 "
            "사방으로 뿜어져 나갑니다. 주위의 모든 빛들이 휘말리듯 일제히 그 곳을 향합니다."
            , boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2], "의 영도 그 곳에 잠시 이끌려 "
            "형체를 움직일 수 없음이 느껴집니다.")
            boss_skillOnOff == True


        #헤더
        print()
        print("[", battleround, "라운드 결과 ]")
        print()
        print(boss_name, ":", boss_atk, "공격 / 타겟팅 위치[ ★ :", boss_target, "]")

        print("> 인당 대미지 -", boss_dmg_all[boss_dmgType], "HP.")





    #데미지 정산
    print()
    print("( * 이 곳에는 캐릭터들의 공격 상황을 직접 입력해줘야 함 )")
    print()
    astral_atk = int(input("* 캐릭터들이 넣은 총 데미지는? : "))
    print()

    print("( * 이 곳에는 캐릭터들의 피해 상황을 직접 입력해줘야 함 )")
    if boss_skillOnOff == True :
        print("> 현재 적용중인 버프/디버프 :" , "행동불가(적>", boss_atkTarget[0], ",", boss_atkTarget[1], ",",boss_atkTarget[2], ")")
    else :
        print("> 현재 적용중인 버프/디버프 : (있으면 적기)")
        
    boss_hp = boss_hp - astral_atk
    
    print(">", boss_name, "에게 총", astral_atk, "대미지 격추")
    print("( * 보스의 남은 체력 : ", boss_hp, ")" )
    print()
    print()

    
    battleround += 1
    boss_skillOnOff = False
    

print("레이드 페이즈를 종료합니다.")


#2022.04.21. <계획> 수정 할 거
#0. 코드 조각내서 함수로 만들어주기
#1. GUI 제작.
#2. GUI 제작하면 전라운드 결과가 날아가니까 전라운드 결과를 String 변환해서 배열에 저장.
#3. 캐릭터 정보 선입력해서 저장. Google 시트랑 연동해도?
#4. 3-구글시트 연동이 성공했을 경우 공격기믹에 관한 내용들 또한 Google시트로 옮겨도 됨.


