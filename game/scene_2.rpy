# The script of the game goes in this file.

# name of the character.
define minorityBlackCaptain = Character("黑苗头领",image="minorityBlackCaptain")
define minority_black_soldier_1 = Character("黑苗喽啰甲")
define minority_black_soldier_2 = Character("黑苗喽啰乙")

#side image definition
image side minorityBlackCaptain=Image("minority_black_captain_left_normal.png")

#character image definition
image minorityBlackSoldierOne normal=Image("minority_black_soldier_one.png")
image minorityBlackSoldierOne angry=Image("minority_black_soldier_one_angry.png")
image minorityBlackSoldierTwo normal=Image("minority_black_soldier_two.png")
image minorityBlackSoldierTwo angry=Image("minority_black_soldier_two_angry.png")
image minorityBlackCaptain normal=Image("minority_black_captain_normal.png")
#background image definition
image bg YuHangInn = "inn.png"

#scene starting point
label scene_2:


    show bg YuHangInn with fade:
        xalign 0.7
        yalign 0.1
    show protagonist:
       xalign 0.8 yalign 0.55
    show minorityBlackCaptain normal:
       xalign 0.4 yalign 0.3
    show minorityBlackSoldierTwo normal:
       xalign 0.3 yalign 0.25
    show minorityBlackSoldierOne normal:
       xalign 0.25 yalign 0.23
    show aunt normal:
       xalign 0.5 yalign 0.4
    aunt "搞什么～慢吞吞的"
    protagonist "君子待客，必先正衣冠，故迟也。"
    aunt "少废话了，这时候倒显得你文质彬彬了。"
    aunt "各位客官．．里边儿请．．  逍遥！帮我招呼客官们歇歇腿,我到厨房准备酒菜．．"
    hide aunt
    minorityBlackCaptain "小二，这间客栈我们包下了，除了老板和伙计，其他不相干的人你们不要再接持了。" 
    protagonist "小店今天没别的客人，只是你们三位...你们三位未必能住满这间客栈吧?"  
    minorityBlackCaptain "这些银子你拿去，往后这几天只要你乖乖听我们的话办事，赏银不会少你的。"
    protagonist "大爷，我不是这个意思，承蒙各位照顾小店生意，若是打赏则使得，若是收买在下干些不可告人的勾当，我李逍遥决不答应。"
    show minorityBlackSoldierTwo angry
    minority_black_soldier_2 "你怎么跟我们头讲话的，小心我一不高兴剁了你这小子。"
    minorityBlackCaptain "不要吓唬人家，黑罗！把刀收起来！"
    show minorityBlackSoldierTwo normal
    protagonist "君子动口不动手，大爷，你得好好管教一下你的下属，这里可是讲王法的地方。"
    minority_black_soldier_1 "王法？杀人越货，可算犯王法？"
    protagonist "岂止犯法，当不待教而诛之！"
    minority_black_soldier_1 "住口，我们不是中原人，自然轮不到你们这里的王法管，我们眼里只有头领，唯头领之命是从。"
    protagonist "头领者，皆篡弑之徒也，从其命，故夷狄之国常乱而不治也！"
    show minorityBlackSoldierOne angry
    minorityBlackCaptain "小伙子，我们不是要干什么勾当，只是怕店里来了其他人太吵，想图个清净，如果你们店执意不能满足的话，我们就去村东头的另一家客栈了。"
    show minorityBlackSoldierOne normal
    $ minority_black_soldier_2.name="黑罗"
    protagonist "本店地方狭小潮湿，不宜胡人居住，大爷请便！"
    minority_black_soldier_2 "头儿，他竟敢如此瞧不起我们，给他点颜色看看！"
    minorityBlackCaptain "我们有更要紧的事，不要图一时痛快惹上麻烦。小伙子，既然你们店不留我们，那好，黑罗，黑鼓，我们走。"
    $ minority_black_soldier_1.name="黑鼓"
    hide minorityBlackCaptain
    minority_black_soldier_1 "送上门的生意都不做！"
    hide minorityBlackSoldierOne
    show minorityBlackSoldierTwo angry
    minority_black_soldier_2 "下次再让我碰到你..."
    hide minorityBlackSoldierTwo
    protagonist "这一伙人行迹可疑，多亏我把他们赶走了。"    
    protagonist "哎呀，婶婶那边可如何交待！"    
    jump scene_3
