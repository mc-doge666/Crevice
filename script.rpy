# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# define e = Character("艾琳")

define xl = Character("小林")
define worker = Character("工人")
define wendolin = Character("温多林")
define wrtrin = Character("维尔汀")
define linx = Character("林克斯")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    # scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。

    # e "您已创建一个新的 Ren'Py 游戏。"

    # e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    #############################################################################
    ####################################START####################################
    #############################################################################
    
    #scene 1
    xl "咦，好脏。"
    voice "audio/worker1_1_1.ogg"
    worker "啊？！什么人！"#1_1_1
    xl "这是哪里？"
    voice "audio/worker1_2_1.ogg"
    worker "外地人？奇怪了……"#1_2_1
    voice "audio/worker1_2_2.ogg"
    worker "最近怪事本来就多，你该不会是什么……"#1_2_2
    xl "是什么？"
    voice "audio/worker1_3_1.ogg"
    worker "你该不会是我的工友吧？最近那股力量出现的越来越频繁，很多人看见了朋友年轻时的样子。"#1_3_1
    xl "啊？我不是，我叫小林，来自乌泽镇。"
    voice "audio/worker1_4_1.ogg"
    worker "……？你是不是早晨起太早，还在做梦？这是是艾瑟兰小镇，哪有什么乌泽镇，我可从来没有听说过那个地方。"#1_4_1
    voice "audio/worker1_4_2.ogg"
    worker "是最近那股力量增强了吗？平常这样的现象只持续几秒钟。"#1_4_2
    xl "我真不是你的工友，我叫小林。"
    voice "audio/worker1_5_1.ogg"
    worker "或许你真不是，小林是吧，跟我来，我带你去见上头的人。"#1_5_1
    xl "好……好的。"


    #scene2
    wendolin "维尔汀小姐，您好。我是镇长的助理温多林欢迎来到艾瑟兰小镇。镇上最近有些不太平，就像我来信中提到的那样。"
    wrtrin "错乱的时间……混淆的记忆……这次的委托很有意思呢"
    linx "既来之则安之，来吧，去看看那个矿井"

    # 此处为游戏结尾。

    return

