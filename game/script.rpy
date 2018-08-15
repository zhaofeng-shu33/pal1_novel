# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define protagonist = Character("李逍遥",image="protagonist")
define aunt = Character("婶婶",image="aunt")
image side protagonist = Image("protagonist_left.png")
image side aunt =Image("aunt_left_happy.png")
image aunt normal = Image("aunt_normal.png")
image protagonist = Image("protagonist_normal.png")
image bg protagonistRoom = "scene_1/protagonist_room.png"
#define le = Character("赵灵儿")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # jump scene_2
    scene bg protagonistRoom with fade:
      xcenter 320
      ycenter 240
      zoom 2.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    show protagonist:
       xalign 0.3 yalign 0.3
    protagonist "哇哇！作恶多端的罗煞鬼婆"

    protagonist "既然落在你的手里,要杀要剐不用多说"
    show aunt normal:
       xalign 0.07 yalign 0.6
    aunt "李逍遥！你皮痒啊？ 敢说老娘是什么鬼婆！"
    protagonist "哎呦～疼啊！ "
    aunt "又在作白日梦了！ 你也老大不小了，整天疯疯癫癫地，也不学学做正经事！"
    protagonist " 婶婶～　 你不要每次叫人起床都拿锅 呀、铲呀，乱敲一通的，会 吓死人哪！  咱们这木床又不牢靠，万一我 给摔死了，咱们李家就绝后啦"
    aunt "不这样叫得醒你吗？好歹你也 跟林师傅学过几个月的木工， 床不牢自己动手修一修不就好了？  就只会削些木刀木剑的，书也不好好读，整天没个定性， 有哪家姑娘愿意嫁给你喔．．"
    protagonist "那我爹怎么会娶到我娘？ "
    aunt "啧！你娘也是跟你爹一个样儿 嫁到咱们李家来，也不做针线 女红，就只会跟着你爹疯．． "
    protagonist "嘿．．大家都说～他们是江湖上人人羡慕的鸳鸯侠侣呢！ "
    aunt "是哦～侠侣？说要去行侠仗义 丢下你这惹祸精，一去无回 还不是我这老太婆省吃俭用的 开了这么一家小小的客栈，才 把你拉拔到这么大，结果养出这么一个懒鬼！"
    protagonist "谁说我是懒鬼啦？ 店里的活我也没少干，圣贤书也没少读，只不过我年纪还小，我将来可是要成为张仪苏秦他们那种佩六国相印周游天下的英雄呢！"
    aunt "少跟老娘鬼扯淡！ 你呀～游手好闲是出了名的 要不是这回我忙不过来，才不指望你这懒鬼来帮忙呢！"
    protagonist "一大早就有客人上门啦？ "
    aunt "是啊．．还不快过来帮忙！"
    hide aunt
    protagonist "真没意思．．一大清早就要人家做这个又做那个的．． "
    aunt "逍遥！还窝在房里干啥？快出来帮忙招呼客人! "
    protagonist "喔！　．．我马上就去"
    
    jump scene_2
    return
