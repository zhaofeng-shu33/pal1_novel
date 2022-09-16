# name of the character.
define drunkard = Character("醉汉",image="drunkard")

#side image definition
image side drunkard=Image("scene_3/drunkard_left.png")

#character image definition
image drunkard normal=Image("scene_3/drunkard.png")
image drunkard lying =Image("scene_3/drunkard_lying.png")
image jade=Image("scene_3/jade.png")
image protagonist right=Image("scene_3/protagonist_right.png")
#background img def
image bg baseroom = "scene_3/baseroom.png"

label scene_3:

    show bg YuHangInn with dissolve:
        xalign 0.25 yalign 0.9
    show drunkard lying:
        xalign 0.1 yalign 0.5
    show protagonist:
        xalign 0.25 yalign 0.5
    "一名衣衫褴褛的醉汉躺在门口"
    pause
    protagonist "哎呀，大清早的怎么有个醉鬼躺在店门口？"
    drunkard "给我酒．．"
    protagonist "这位大伯，你快点走吧，不要妨碍我们做生意。"
    drunkard "客人不是已经走了吗？"
    protagonist "你刚才听见什么了？"
    drunkard "我刚才沉浸在满桌美酒的好梦里，被楼上一阵嚷嚷吵醒了，所以你要分我酒喝！"
    protagonist "没见到你这么赖皮的酒鬼，好吧，我昨天刚从集市上买了几坛清酒，你跟我到仓库来拿吧。你得保证，喝完就走人，而且下次不许再出现。"
    show drunkard normal
    drunkard "人生有酒则尽欢，小兄弟快带我去。"
    show bg baseroom with fade
    show protagonist:
      xalign 0.5 yalign 0.3
    show drunkard:
      xalign 0.8 yalign 0.2
    protagonist "哎呀，你怎么喝了这么多？...要是再来了客人我拿什么招待？"    
    drunkard "小伙子，你要是到我这个年纪就明白了。"
    protagonist "大伯可是有什么愁苦之情，不得通其志，故借酒以浇之？"    
    drunkard "说来话长喽..."
    protagonist "敢问一二曲折。"    
    drunkard "在下司徒钟，幼时拜入蜀山门下习武，后随师傅游历四方收妖，然一次奉命往大理拿妖之际，因凡心所动，遂自酿苦果..."
    $ drunkard.name="司徒钟"
    protagonist "看来神仙也难耐寂寞呵。"    
    drunkard "余与一凡间女子一夜风流，留一玉佩为念，后不归。十余年间将忘此事之际，值此一次往余杭镇捉妖，却于村外捡得此玉佩。"
    show jade at truecenter
    protagonist "于是十几年前的风流旧事便如在目前，让人痛心不己，虽然心上人近在咫尺之间，却如同远在天涯海角..."    
    hide jade
    drunkard "小兄弟你怎知我心意？"
    protagonist "这种故事书里看多了，你也不换个花样，好了，算我倒霉，遇上你这个假神仙，真醉鬼，白赚了我们家这么多酒喝。你现在喝够了赶紧走吧，我可没功夫听你这些陈词滥调。"
    drunkard "也罢，{b}凡人怎晓神仙事，刘晨阮肇非罔然。此情可待成追忆，酒醒时分事更哀。{/b}"
    drunkard "小兄弟，此番见面，也是我们有缘，只是我还有要事在身，不能久溺于凡情而坠，这玉佩就送你吧，我留着也只会徒增烦恼。"
    hide drunkard
    protagonist "你真是无情人偏说有情话，我看这也就是外边地摊上的仿制品，根本不够酒钱。" 
    aunt "逍遥，你去帮忙去市场上买几斤新鲜的鱼回来，顺便去丁家讨一下账。"
    protagonist "好嘞！"
    show protagonist right
    protagonist "这醉汉人呢?"    
    jump scene_4
