# name of the character.
define girlAssistant = Character("水月宫待女",image="girlAssistant")

#side image definition
image side girlAssistant=Image("scene_7/girl_assistant_side_image.png")

#character image definition

#background img def
image bg WaterMoonPalace="scene_7/WaterMoonPalace.png"
image protagonist sitting=Image("scene_7/protagonist_sitting.png")
image girlAssistant DownRight=Image("scene_7/girl_assistant_downRight.png")
image girlAssistant UpLeft=Image("scene_7/girl_assistant_upLeft.png")
image protagonist FaceLeft=Image("scene_7/protagonist_face_left.png")
image shadow=Image("scene_7/shadow.png")
image protagonist moveUpLeft:
  "scene_7/protagonist_up_left2.png"
  pause 0.2
  "scene_7/protagonist_up_left3.png"
  pause 0.2
  "scene_7/protagonist_up_left4.png"
  pause 0.2
  "scene_7/protagonist_up_left5.png"
  pause 0.2
  "scene_7/protagonist_up_left6.png"
  pause 0.2
  "scene_7/protagonist_up_left7.png"
  pause 0.2
  "scene_7/protagonist_up_left8.png"
  pause 0.2
  "scene_7/protagonist_up_left1.png"
  pause 0.2  
  repeat  #1.6s

label scene_7:

    show bg WaterMoonPalace with dissolve:
       xanchor 0.396
       yanchor 0.362
       xpos 0 ypos 0
       zoom 1
    show protagonist sitting:
       xpos 0.5 ypos 0.46
       xanchor 0 yanchor 0
    show girlAssistant DownRight:
       xpos 0.35 ypos 0.5
    protagonist "哎呀，头好沉，这是哪儿？"
    show protagonist FaceLeft:
      xpos 0.466 ypos 0.465
    girlAssistant "你醒了，海上风浪那么大，要不是灵儿公主相救，你早就被淹死了。"
    protagonist "灵儿公主？我现在在哪，我只记得和水生叔一起出海，船被海浪打翻了..."
    girlAssistant "这里是水月宫，我是灵儿公主的侍女阿香。"
    $ girlAssistant.name="阿香"
    protagonist surprised "那我岂不是在海底？"
    girlAssistant "不是，这里是仙灵岛，一座逐海而漂的仙岛，平常人是不容易到这岛上来的。"
    protagonist "仙岛？嗨，真有这回事，阿香，现在我可否去见一见你们的灵儿公主，只因村里的丁大伯染了重病，我是特地来仙岛求药的秀才李逍遥。"
    girlAssistant "灵儿公主现在有事，请你在这里静候一会。"
    protagonist "丁大伯的病可等不了，公主在哪，我现在去见她。"
    show shadow:#transient ui disappears after a say statement
      xoffset 70 yoffset 31
    show protagonist moveUpLeft behind shadow:
      linear 3.2 xpos 0.232 ypos 0.256
    pause 3.2
    show girlAssistant UpLeft
    girlAssistant "李公子，且慢，水月宫乃清修之地，不允许外人私自探访..."
    show protagonist moveUpRight behind shadow:
      linear 3.2 xpos 0.365 ypos 0.068
    pause 3.2
    hide protagonist
    girlAssistant "哎呀，灵儿公主吩咐过我的，这秀才怎么跑得这么快...坏了，要是他不小心撞进了桃林里的温泉..."
    pause
    return
