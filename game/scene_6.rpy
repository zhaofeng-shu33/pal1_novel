# name of the character.
#define novelFlowerSister = Character("丁秀兰",image="novelFlowerSister")#妹
#define novelFlower = Character("丁香兰",image="novelFlower")#姐
#above character already defined

#side image definition
image side novelFlowerSister shy=Image("scene_6/novelFlowerSister_shy_left.png")
image side protagonist surprised=Image("scene_6/protagonist_surprised_left.png")
image side novelFlowerSister concerned=Image("scene_6/novelFlowerSister_concerned_left.png")
#image side novelFlower=Image("scene_5/novelFlowerSister_left.png")

#character image definition

image novelFlowerSister = Image("scene_6/novelFlowerSister_normal.png")
image novelFlowerFather lying=Image("scene_6/novelFlowrFather_lying.png")
image novelFlower DownRight=Image("scene_6/novelFlower_downRight.png")
image novelFlower UpLeft=Image("scene_6/novelFlower_upLeft.png")
image novelFlowerSister KnockDown=Image("scene_6/novelFlowerSister_KnockDown.png")
#background img def
image bg novelFlowerSisterHome="scene_6/flowerHome.png"

label scene_6:

    show bg novelFlowerSisterHome with fade:
       xanchor 0.093
       yanchor 0.015
       xpos 0 ypos 0
       zoom 1
    show novelFlower normal:
       xpos 0.476 ypos 0.427
    show novelFlowerSister:
       xpos 0.693 ypos 0.325
    show protagonist UpRight:
       xpos 0.355 ypos 0.72
       xanchor 0 yanchor 0
    show novelFlowerFather lying:
       xpos 0.881 ypos 0.468
    novelFlower "逍遥小弟，我们家里熬了一锅腊八粥，中午要不要请李大娘一起过来尝尝？"
    protagonist "香兰姐煮的点心是出了名的，不过我们店今天有客人，恐怕婶婶忙不过来。对了，秀兰呢，她刚才说有东西要给我。"
    novelFlower "哎，爹的病一天重似一天，秀兰每天清早去洪大夫那儿去抓药，她现在在里间照顾着爹呢。"
    show bg novelFlowerSisterHome with dissolve
    show protagonist DownRight:
       xpos 0.604 ypos 0.302
    show novelFlower DownRight:
       xpos 0.765 ypos 0.387
    novelFlowerSister "李大哥，你看．．这件是我亲手缝制的布靴，你穿看看合不合你的脚？"
    protagonist "哦！谢谢你,不过我还今天来还有一事，可能现在不方便讲..."
    novelFlowerSister shy "李家哥哥，你不会是..."
    show novelFlower UpLeft
    novelFlower "不会是来向秀兰提亲的吧!"
    protagonist surprised "误会了，实不相瞒，你们家之前借我们的钱一直没还，我特定过来提醒一下。"
    novelFlowerSister "人家还以为你是..."
    novelFlowerSister concerned "李大哥，要不是我爹的病，之前借的钱也不会脱到现在，只是现在我们家全靠我们姐妹俩的手艺撑着，娘又去世的早..."
    protagonist "丁大伯的病可有好转。"
    novelFlower "哎，洪大夫也回天无力了，逍遥小弟，你读书多见识广，可有什么起死回生之术。"
    protagonist "死生有命，皆天意使然，非人事可预之也。"
    novelFlowerSister "小虎子说东边有座仙岛，仙岛上有菩萨娘娘济世救人，或许能救我爹一命？"
    novelFlower "是啊，我也听说书的艺人讲过太真仙子的故事。"
    protagonist normal "是杨贵妃死后成仙的故事吧，但仙山仙岛，往往缥缈然寻..."
    novelFlowerSister "李大哥，虽然仙岛之事希望渺茫，但事到如今，宁可信其有..."
    show novelFlowerSister KnockDown
    protagonist surprised "秀兰妹，这是何意？"
    novelFlowerSister "李大哥，有一事相托，不知你可否答应？"
    protagonist normal "先起来再说，我知道你忧心丁伯伯的病情，可是..."
    protagonist "也罢，想我李逍遥好歹也是个男子汉，见义不为何以称勇，见死不救何以谈义。秀兰妹，香兰姐，我回去收拾一下东西，即刻动身去寻觅仙岛求药。"
    show novelFlowerSister normal
    novelFlowerSister shy "多谢李大哥，如果爹爹的病能治好，我情愿以身相许..."
    protagonist surprised "千万别这么说，邻居有急我帮忙也是应该的。"
    novelFlower "最近风浪太大，逍遥弟要不缓缓再动身？"
    protagonist normal "救人要紧，我福大命大，待会你们就不要去送了。能不能找到仙岛我心里没底，但八成还是能活着回来的。"
    hide protagonist
    novelFlowerSister "姐姐，李家哥哥虽与我们不是至亲，但我的心意，你知道，如今可怜见爹爹命在逡巡，济不济事权靠他来试一试了。若能求得仙药，治好爹爹，情愿倒陪家门，与英雄结婚姻，成秦晋。"
    hide novelFlower
    hide novelFlowerSister
    hide novelFlowerFather
    jump scene_7
    return