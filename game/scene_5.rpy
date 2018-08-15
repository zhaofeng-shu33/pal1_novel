# name of the character.
define novelFlowerSister = Character("丁秀兰",image="novelFlowerSister")#妹
define novelFlower = Character("丁香兰",image="novelFlower")#姐
define sailer=Character("水生叔",image="sailer")
define smallTiger=Character("王小虎",image="smallTiger")
define washingMother=Character("来福婶")
define child=Character("孩童")
define oldSailer=Character("老水手")
define fish_seller=Character("卖鱼小哥")
#side image definition
image side novelFlowerSister=Image("scene_5/novelFlowerSister_left.png")
image side novelFlower=Image("scene_5/novelFlower_left.png")
image side sailer=Image("scene_5/sailer_left.png")
image side smallTiger=Image("scene_5/smallTiger_left.png")

#character image definition
image oldSailer normal=Image("scene_5/sailer_old.png")
image oldSailer upLeft=Image("scene_5/sailer_old_face_upLeft.png")
image childrenYuHang jumping:
  "scene_5/child1.png"
  pause 0.5
  "scene_5/child2.png"
  pause 0.5
  "scene_5/child3.png"
  pause 0.5
  "scene_5/child4.png"
  pause 0.5
  repeat
image protagonist moveUpRight:
  "scene_5/protagonist_up_right2.png"
  pause 0.2
  "scene_5/protagonist_up_right3.png"
  pause 0.2
  "scene_5/protagonist_up_right4.png"
  pause 0.2
  "scene_5/protagonist_up_right5.png"
  pause 0.2
  "scene_5/protagonist_up_right6.png"
  pause 0.2
  "scene_5/protagonist_up_right7.png"
  pause 0.2
  "scene_5/protagonist_up_right8.png"
  pause 0.2
  "scene_5/protagonist_up_right1.png"
  pause 0.2  
  repeat  #1.6s
image protagonist UpRight=Image("scene_5/protagonist_up_right1.png")
image protagonist moveDownRight:
  "scene_5/protagonist_down_right2.png"
  pause 0.2
  "scene_5/protagonist_down_right3.png"
  pause 0.2
  "scene_5/protagonist_down_right4.png"
  pause 0.2
  "scene_5/protagonist_down_right5.png"
  pause 0.2
  "scene_5/protagonist_down_right6.png"
  pause 0.2
  "scene_5/protagonist_down_right7.png"
  pause 0.2
  "scene_5/protagonist_down_right8.png"
  pause 0.2
  "scene_5/protagonist_down_right1.png"
  pause 0.2  
  repeat  
image protagonist DownRight=Image("scene_5/protagonist_down_right1.png")
image novelFlowerSister moveLeft:
  "scene_5/novelFlowerSister_left1.png"
  pause 0.5
  "scene_5/novelFlowerSister_left2.png"
  pause 0.5
  "scene_5/novelFlowerSister_left3.png"
  pause 0.5
  "scene_5/novelFlowerSister_left2.png"
  pause 0.5
  repeat 5
image novelFlowerSister moveRight:
  "scene_5/novelFlowerSister_right1.png"
  pause 0.5
  "scene_5/novelFlowerSister_right2.png"
  pause 0.5
  "scene_5/novelFlowerSister_right3.png"
  pause 0.5
  "scene_5/novelFlowerSister_right2.png"
  pause 0.5
  repeat 5

image washingMother animated:
   "scene_5/washing1.png"
   pause 1.0
   "scene_5/washing2.png"
   pause 1.0
   repeat
image sailer normal=Image("scene_5/sailer_normal.png")
image sailer upLeft=Image("scene_5/sailer_face_upLeft.png")
image smallTiger normal=Image("scene_5/smallTiger_normal.png")
image novelFlower normal=Image("scene_5/novelFlower.png")

#background img def
image bg market="scene_5/market.png"

label scene_5:

    show bg outsideInn with dissolve:
        xalign 0.5 yalign 0.4
    #adjust the washingMother position    
    show washingMother animated:
       xalign 0.15 yalign 0.45
    show protagonist:
       xalign 0.25 yalign 0.35
    washingMother "嗨～小李子！你婶婶还在店里头忙啊？怎么没见她来这洗衣服．．"
    protagonist "是啊．．今天一大早就来了一伙人要住店"
    washingMother "就是那伙黑衣服的人吗，我看他们不像是好人，说不定半夜里把你们店给..."
    protagonist "嗨，他们让我三两句话给吓跑了！"
    washingMother "是吗？那他们不会跑去老李家开的店吧，咱们这小地方，可真没过几天太平日子，几年前金兵南下，到地儿抢了不少东西走，这次不会是他们的卧底吧？"
    show novelFlowerSister moveLeft:
        xalign 0.72 yalign 0.95
        linear 10 xalign 0.30 yalign 0.40
    pause
    protagonist "秀兰妹子今天这么早就在帮丁伯伯挑水浇菜呀"
    novelFlowerSister "李大哥今天怎么也起的这么早啊,看来知道用功读书了，咱们镇马上要出一位进士了。"
    protagonist "我一惯早起，正所谓三更灯火..."
    washingMother "小李子，你说你天天读书，XXX怎么考了好几回也过不了呢？"#research on 南宋科举制 here
    protagonist "我朝名相苏洵不是二十七岁才举进士的吗？"
    novelFlowerSister "是啊，李大哥还年轻，早晚要出人头地的。对了，李大哥，我有件东西要送给你，等会你能不能去我家来拿？"
    protagonist "正好婶婶叫我去你家办点事，我一会过去。"
    show novelFlowerSister moveRight:        
        linear 10 xalign 0.72 yalign 0.95
    pause
    hide novelFlowerSister
    hide washingMother
    show bg outsideInn with dissolve:
        xalign 0.8 yalign 0.7
    show smallTiger normal at truecenter
    smallTiger "逍遥哥哥！你今天再带我去树林里去找鸟窝，好不好吗?"
    protagonist "小虎子，店里有事，大哥哥要忙啊，今天不能带你去啰．．"
    smallTiger "上次你也说有事，结果看见你和邻村的张四他们在斗蛐蛐..."
    protagonist "小虎子，不要乱说，让村里人听到了对我名声不利。好好好，明天，明天我带你去成不？"
    smallTiger "可当真？"
    protagonist "君子言而有信。"
    hide smallTiger    
label scene_5_children:
    show bg outsideInn with dissolve:
        xalign 0.7 yalign 0.9
    show childrenYuHang jumping at truecenter
    show protagonist:
       xalign 0.45 yalign 0.35
    child "{b}小李子 志气高{/b} \n{b}想学剑仙登云霄{/b} \n{b}日上三竿不觉醒{/b} \n{b}天天梦里乐陶陶{/b}"
    protagonist "你们三个小鬼竟敢编歌来笑我！"
    child "呵呵！这是我哥教我的,全村的孩童都会唱呢！"
    protagonist "看来我的败名已经家喻户晓了，一定是那小虎子干的，看我明天不找他算账。"
    child "吕洞宾，乘风飘        肩背龙剑斩群妖 \n悲心救苦传妙道        至今万古姓名标\n韩湘子，品玉箫        志学修行家室抛 \n雪拥蓝关难行马        曾度文公上九霄"
    protagonist "这是八仙歌吧。想当年韩愈的侄儿也成了神仙，还为自己的伯父料理后事，"#comment on 八仙歌 here
    child "曹国舅，爱逍遥        不恋荣华卸锦袍 \n世上万般修行好        手执云阳仙板敲 \n李铁拐，相咆哮        黑脸浓眉腿又跷 \n虔心修炼长生法        挂拐登云蔼蔼飘"
    protagonist "连皇亲国戚也修了道，是惧潜在的灾祸吗？"#comment on 八仙歌 here
    child "汉钟离，性儿矫        识透人情事态枭 \n终南山上修妙道        列位仙班道行高 \n何仙姑，容貌娇        懒伴红尘愿寂寥 \n苦志真修千百载        也归仙界乐逍遥"    
    protagonist "汉钟离是汉朝的大将，怎么也成了真人？"#comment on 八仙歌 here
    child "蓝采和，年纪小        最爱修行却富饶 \n名山修炼成真果        使执棕篮驾海潮 \n张果老，年纪高        须发苍苍两鬓萧 \n倒骑驴子呵呵笑        竟把繁华世界抛"    
    protagonist "张果老深得唐玄宗宠信，然未见其道之可兴国也。算了，我还有正事呢，得赶紧去集市。"#comment on 八仙歌 here
    hide childrenYuHang
label scene_5_market:
    show bg market with dissolve:#position of the screen
       xanchor 0.263
       yanchor 0.289
       xpos 0 ypos 0
       zoom 1
    show oldSailer normal:
       xpos 0.83 ypos 0.22
    show sailer normal:
       xpos 0.90 ypos 0.36
    show protagonist:
       xpos 0.279 ypos 0.263
       xalign 0 yalign 0
    protagonist "你们这有新鲜的鱼吗？"
    fish_seller "这两天风浪太大了些，船家们都捕不到鱼货,你要是不嫌的话，这些之前捕到的可以贱卖给你。"
    protagonist "婶婶要我买新鲜的，那算了，我去问问打渔的船家吧。"
    show protagonist moveUpRight:
       linear 4.8 xpos 0.606 ypos 0.087
    pause 4.8
    show protagonist moveDownRight:
       linear 3.2 xpos 0.754 ypos 0.212
    pause 3.2
    show protagonist DownRight
    protagonist "水生叔，你们这打到新鲜的鱼没？"
    show sailer upLeft
    sailer "小李子，实不相瞒，这两天风浪太大了,勉强出海打渔，结果一条鱼也没打到，真是晦气！"
    protagonist "咱们镇自从几年前兵乱以来不是一直风调雨顺吗，怎么最近风浪..."
    show oldSailer upLeft
    oldSailer "小李子，我听算命先生讲啊，这大风浪往往预示着大灾殃，不知谁家又要倒霉喽。"
    protagonist "是啊，从来人间之事，天必应之，只是不知这风浪因何而起，看来我明天得去山神庙烧几柱香给自家祈福呢。"
    oldSailer "昨日我冒险出海时看到东边的岛上有一位巫婆在兴风作浪，怕这风浪是和这有关。"
    sailer "大伯，你准是花眼了，我下海也有几年了，怎么从来没看见过东边有什么岛。"
    protagonist "天下哪有什么鬼怪之事，都是心里有鬼闹腾的。"
    oldSailer "嗨！小虎子不是也讲他去过什么仙岛，还见到了菩萨娘娘，求得了仙丹，治好了父亲的病不是。"
    sailer "小虎子的话你也信，明明是镇上的洪大夫给治好的，不知那小屁孩哪天做梦梦到菩萨娘娘还差不多。小李子，听你刚才这么说，既然你不信鬼神，干嘛还成天想着学道成仙？"
    protagonist "这都是以讹传讹，我只是平日里读什么佛啊，老啊，方术之类的闲书解闷，我婶婶又是个大嘴巴，和镇上的人聊着聊着肯定会数落起我这些不务正业的事来。"
    sailer "也不怪李大婶说你，你年纪也不小了，又是镇上比较有学问的，得赶快想着谋个一官半职，哪能成天带着一群小孩疯呢？"
    protagonist "水生叔，我用功的时候都找清净之地，别人见不到。算了，既然买不到鱼，我还是去丁家讨账吧。"
    protagonist "刚才丁秀兰说有东西要送我，不知是怎的。秀兰这妮子，没事总找我搭讪，我可是宋玉一流的人物，东家之女登墙窥宋玉三年他都不动心，不动心必有道哉！"
    hide sailer
    hide oldSailer
    jump scene_6
    return