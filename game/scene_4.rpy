# name of the character.
define daughterPretty = Character("白苗头领",image="daughterPretty")
define minority_white_soldier_1=Character("白苗喽啰甲")
define minority_white_soldier_2=Character("白苗喽啰乙")

#side image definition
image side daughterPretty=Image("scene_4/minority_white_captain_daughter_left.png")

#character image definition
image daughterPretty normal=Image("scene_4/minority_white_captain_daughter.png")
image minorityWhiteSoldierOne normal=Image("scene_4/minority_white_soldier_one.png")
image minorityWhiteSoldierOne right=Image("scene_4/minority_white_soldier_one_right.png")
image minorityWhiteSoldierTwo normal=Image("scene_4/minority_white_soldier_two.png")
image minorityWhiteSoldierOne angry=Image("scene_4/minority_white_soldier_one_angry.png")
image protagonist beaten=Image("scene_4/protagonist_beaten.png")
image daughterPretty battle=Image("scene_4/minority_white_captain_battle.png")
#background img def
image bg outsideInn = "scene_4/outside_inn.png"
image bg roomLeft = "scene_4/roomLeft.png"

label scene_4:

    show bg outsideInn with dissolve:
        xalign 0.5 yalign 0.3
    show protagonist:
       xalign 0.62 yalign 0.45
    show daughterPretty normal:
       xalign 0.4 yalign 0.5
    show minorityWhiteSoldierTwo normal:
       xalign 0.27 yalign 0.4
    show minorityWhiteSoldierOne right:
       xalign 0.35 yalign 0.5
    minority_white_soldier_1 "首长，这么有一家客栈"   
    show minorityWhiteSoldierOne normal
    daughterPretty "喂，那个少年，请问你家客栈的客人，还是店里的伙计？"
    protagonist "这...你们不是本地人吧？"
    show minorityWhiteSoldierOne angry
    minority_white_soldier_1 "首长问你话呢，你怎么这么没礼貌！"
    protagonist "果然是蛮夷之人，不速之客！"
    daughterPretty "敢拿我们的身份取笑，蛮夷怎么了，就只有你们中原人天生高贵吗！白楼，给我好好教训一下这个臭小子！"
    $ minority_white_soldier_1.name="白楼"
    protagonist "你敢？"
    $ renpy.play('scene_4/punch.wav')
    with hpunch
    show protagonist beaten
    protagonist "还真打啊？"
    daughterPretty "你嘴上虽硬，看来还是弱不经风的样子，我们一路上见到很多你这种书呆子，难怪你们大半个江山都让金人给掠去了。"
    show protagonist
    show minorityWhiteSoldierOne normal
    protagonist "话不能这样说，故国虽落敌手，但故国的老百姓无心系王师北定中原之日。"
    daughterPretty "靠你这种人只怕你们故国的老百姓是看不到这一天了。"
    protagonist "遗民泪尽胡尘里，在下武艺不精，实在惭愧。"
    show daughterPretty battle:
       xalign 0.62 yalign 0.45  
    show protagonist beaten
    daughterPretty "不许说我们是胡人，一点都不知道考虑其他民族的感受！"
    show protagonist
    show daughterPretty normal:
       xalign 0.4 yalign 0.5    
    protagonist "不敢了，小店今日无客，三位是要寻个歇脚处吗？"
    minority_white_soldier_1 "你早说不就好了，白挨了两顿揍。"
    show bg roomLeft with fade
    show minorityWhiteSoldierTwo normal:
       xalign 0.3 yalign 0.4
    
    protagonist "这间房早上刚打扫过，女少主你看怎么样？"    
    daughterPretty "谁是你女少主，你又不是我们苗人的俘虏。哎呀，说真的，其实当汉人俘虏有什么可耻的，还能帮助我们多干些兴邦利民的事儿，都是你们那些教条的观念害死人。"
    protagonist "随你们怎么说，反正在我们的青史中，苏武者荣，李陵者耻。"
    daughterPretty "算了，没空跟你这种人争辩，这间客栈我们包下了，除了老板和伙计，其他不相干的人你们不要再接持了。"
    protagonist "怎么又是这样说，凭什么那么霸道？"
    show minorityWhiteSoldierOne angry       
    protagonist "没..当然没问题。"
    hide minorityWhiteSoldierOne
    hide minorityWhiteSoldierTwo
    hide daughterPretty
    show bg YuHangInn with fade:
        xalign 0.7
        yalign 0.1
    show protagonist:
       xalign 0.42 yalign 0.32
    protagonist "哎呀，早知道就留下黑苗那一帮了，差点又挨第三顿揍，还没了小费。"
    protagonist "还是先去市场吧!"
    pause
    jump scene_5