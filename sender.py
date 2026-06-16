
import time
import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ========================================
# 1. 改成你自己的信息（必须改）
# ========================================
BOT_TOKEN = "8862803555:AAHGtuWOcQzkjpY7CLMYPSi50jryLCknsB0"
CHANNEL_ID = "-1003956197302"

# ========================================
# 2. 图片库（有图片ID就填进去，没有留空）
# ========================================
photo_ids = [
      "AgACAgEAAxkBAAMUajBsgv-3tZsS2coyJAJU3RoUvOAAAiQMaxvOOoFFN5zS1AMvSBYBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMVajBshvZNRVYYdwgjMD00OtSN9qcAAiUMaxvOOoFF0PUvtOhN0pQBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMWajBsiwABYQ59-5ckAZ1ec_SDauKuAAImDGsbzjqBRRCnNIzkcH5sAQADAgADeQADPAQ",
 "AgACAgEAAxkBAAMXajBskPjl_AkgZLqgDI3LQXQkGbIAAicMaxvOOoFF5_GdCAiAYRcBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMYajBslvMb35mXP-xKHvBiKx_uLMcAAigMaxvOOoFFSc4KI1hCmDcBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMZajBsmjmfwyGc31uNwnQE1_oXi-EAAikMaxvOOoFF5496Dbxv9dIBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMaajBsoeUrMzwuemUewKwnKCbRamgAAioMaxvOOoFF8PNrz76Qal8BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMbajBsrBuNOgwEwYY0m_vFEYXzLIAAAisMaxvOOoFFwdD8sLvCqi4BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMcajBstK6FAzXCl4GQMG4o8c3aVH0AAiwMaxvOOoFFw4ZSw3IB910BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMdajBsvcZDg3I4XEr74aO-fG1lRZAAAi0MaxvOOoFFliA6MjrMmqYBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMeajBswk0hRewrCoXMwUkVthlABwYAAi4MaxvOOoFFCjdW-WwIROcBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMfajBsyMxjrv4rqOhhLHtQiqIP93gAAi8MaxvOOoFFznJlSuUIqnMBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMgajBszX7McUTa6s_qW9dYoaF1V2EAAjAMaxvOOoFFD95WqAUtb8ABAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMhajBs0_hJ1jvcEUnqX9H_vgSyvf0AAjEMaxvOOoFFDIDIWtahN9sBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMiajBs2rc6P-YxDGDvBC8YA7UJoVcAAjIMaxvOOoFFxXf3U4XD6OwBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMjajBs3_KtamO9IQfAQdHKsNkqFbsAAjMMaxvOOoFFuBNsNYrl2lcBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMkajBs5RX-6o-JJy47_Oz3jjJKgIwAAjQMaxvOOoFF-TOCCdEOIwYBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMlajBs7oeGDlFHfttEi6Q0apPRnowAAjUMaxvOOoFFkkK9__ZSJ2UBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMmajBs9lECarDbk26sMmpFOIXq8ykAAjYMaxvOOoFF7UKU0JX65GEBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMnajBs_rVDL8gEdg5nJuoFUaMkxzkAAjcMaxvOOoFF4jE_4MfAibYBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMoajBtBBJ9PNsWJs2eB7E6Tptk5OQAAjgMaxvOOoFFleX5C3wQqg4BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMpajBtCkwVUCj_lrUuE7juLWgaxqQAAjkMaxvOOoFFezp18LI4K9kBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMpajBtCkwVUCj_lrUuE7juLWgaxqQAAjkMaxvOOoFFezp18LI4K9kBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMrajBtGWFdy4g8w2HV2coAAQWbiavmAAI6DGsbzjqBRfylmk5sDqpNAQADAgADeQADPAQ",
 "AgACAgEAAxkBAAMsajBtH68z3cNfpEgzg6mkARN_TnEAAjsMaxvOOoFFZ55bplZJwKoBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMtajBtJEjhn2WSD98yAU_iauI0FfAAAjwMaxvOOoFFcG84fbzEcYABAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMuajBtOS0u3Z05npvX89Yc-B41FZ0AAj0MaxvOOoFFhBtoxu2TQLQBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMvajBtQUdcl3lxJhOnidgV-XH1hWYAAj4MaxvOOoFFCzhxIGpWsVIBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMwajBtSN6zJ_B8764ygpcnYxx9QioAAj8MaxvOOoFFtjxvSGExXhABAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMxajBtU76vhW5BF-dBxEJS9flZ50cAAkAMaxvOOoFFzJeiXspzcXEBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMyajBtWQr5jjPfHzi_JrsFEKjFtZsAAkEMaxvOOoFFkwmTsrq0zysBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAMzajBtcUSRzdHscShFV2fFCmM2UnwAAkIMaxvOOoFFDDKCw_-ZqdIBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM0ajBtecTuLRN7yODtYhxaeboX82IAAkMMaxvOOoFFEZX5pQNZFTwBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM1ajBtjDoWWBNjj0RNe3xgoCHYhU0AAkQMaxvOOoFFzR9G4OsJlu8BAAMCAAN5AAM8BA",
"AgACAgEAAxkBAAM2ajBv2o1IcES7MlqiPz5mIMhBlMcAAkUMaxvOOoFF5D0n6CKDJ3UBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM3ajBv8l0i2SFiA9ybEQrAUunAeWcAAkYMaxvOOoFFHL-JjM8LfG4BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM4ajBv9_QtRWsNVmcsjiG6Jbqvvv8AAkcMaxvOOoFF5rKbAanjCJsBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM5ajBwAAFMNWLZRCxH1FlCC5p7KdBQAAJIDGsbzjqBRf_P3sWSQ-hxAQADAgADeQADPAQ",
 "AgACAgEAAxkBAAM6ajBxC2zkSlU-AuMjxQ-AtdquBxgAAkkMaxvOOoFFNouvFO5GNTsBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM7ajBxD-jjQtL5M7SYCUl5mKBdnrIAAkoMaxvOOoFF455ffHLhWJUBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM8ajBxFMKS8-pMs2h-m3jBVpCFJNAAAksMaxvOOoFFaQMNfEqLJNIBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM9ajBxGEaXksdjuQHsPpWfNE7k8IkAAkwMaxvOOoFFgbIb9teV4NMBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM-ajBxHbcMJhkKw4k_w0mrar0r98MAAk0MaxvOOoFF1x3vQgFEfWUBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAAM_ajBxIZcgsTOSD4pqg7GOqfUyIzcAAk4MaxvOOoFFU8KRr4wLGC8BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAANAajBxJlm1R2v6PAL_xESnJLMnNAEAAk8MaxvOOoFF1zp_vvGdIcMBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAANBajBxKzL3uAr2cONnNrNmpnjPTZEAAlAMaxvOOoFFAAFXGAQ4ZM-rAQADAgADeQADPAQ",
 "AgACAgEAAxkBAANCajBxMb0Jia1r7G4PvGUW7is0TssAAlEMaxvOOoFFg1szi799es8BAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAANDajBxObhI9oVcc5ANsVUBiORhqhoAAlIMaxvOOoFFm-Lqm3YrfvcBAAMCAAN5AAM8BA",
 "AgACAgEAAxkBAANEajBxPvCuNEo-4yIFsg3HNZAaInoAAlMMaxvOOoFFPcUlpqX4md0BAAMCAAN5AAM8BA"
 "AgACAgEAAxkBAANFajBxcsPUekCR5G_t3rMpxLspqdoAAlQMaxvOOoFFvQABaq9r3HI_AQADAgADeQADPAQ",
   
]

# ========================================
# 3. 引导语文案库
# ========================================
text_templates = [
    "🎐 🪨 半山腰的野果挂在枝头，酸甜汁水在嘴里炸开🌼💧 ☁️",
    "🌷 🪁 河边垂柳慢悠悠晃着枝条，风裹着水汽拂过来🍧🪁 🍃",
    "🦋 🪻 大片花海铺满平缓坡地，蝴蝶绕着花瓣打转🍯✨ 🌞",
    "🌸 🍀 茶在手，暖在心，静享慢时光🌹🌷 🫦",
    "🍃 🎏 老村巷旁河水静静流淌，满是慢悠悠水乡温柔🌾🪨 🪷",
    "✨ 每一天都值得用心，讨好自己。💖",
"☀️ 🧺 落日把河面染成蜜橙色，波光粼粼🍑🦋 🌊",
"🪨 🦋 清晨薄雾裹住整片茶园，茶叶挂着细碎露珠💐🍃 🌫️",
"🎏 🍑 山坳里藏着一方小池塘，几只野鸭自在游来游去🪁🧺 ⛰️",
"💧 🌷 雨后山林到处挂着水珠，每一步都沙沙作响🌼🍧 🌿",
"🧺 🎐 旷野晚风卷着青草气息，烦心抛到脑后🪻🌾 ☁️",
"🪻 💧 狭长栈道沿着湖岸延伸，落日落在水天交界🦋🍑 💋",
"🍧 🪁 山头老树撑开浓密树荫，躲在树下吹风乘凉🫰🧺 ⛰️",
"🌾 🦋 田埂小路弯弯曲曲通向远山，稻穗随风轻轻点头🎏💐 🌱",
"🧸 ❤️ 你要永远记住，这个世界上有人爱你🎏💐 🌱",
"❤️‍🩹 🎄 微光撕开云雾，山峰一点点露出轮廓，山野慢慢苏醒🪨🍃 🌤️",
"🪁 🍃 小溪绕过成片青石滩，赤脚踩进去凉丝丝特别舒服💧🪻 🪨",
"🎐 🍧 漫山野花不分时节肆意生长，天然景致🌷🌾 ☀️",
"💎 💄 漫天繁花之下，你在我身边☔💦 💤",
"❤️ 🎉 世界灿烂盛大，欢迎回家🎊💫 🌟",
"🐝 🐠 风光无限是你，跌落尘埃也是你，重点是你，而不是怎样的你🐬🦀 😿",
"🍎 🍒 未经允许，擅自特别喜欢你，不好意思了🌷🍉 ☀️",
"🍥 🍧 心里有一簇迎着烈日而生的花，滚烫馨香没过胸膛🍤🍡 🍰",
"🍋 🥭 我想在你眼里，撒野奔跑，我想一个眼神，就到老🍷🍭 🍫",
"🥛 🍵 我喜欢你，所以你走的路要繁花盛开，人声鼎沸🍐🍊 🍅",
"💐 🪨 暮色悄悄漫过林间小道，山野慢慢陷入温柔安静🧺🦋 🌙",
"🌊 🎏 湖畔芦苇随风左右摇摆，晚风捎来淡淡花香🍑💧 🍂",
"🦋 🌾 浅淡云层贴在青山腰间，阳光透过云缝洒落🪻🍇 ⛰️",
"🌽 👋 你记得我吗，我走了很远才见到你👄💋 ❤️",
"🍑 🧺 村口荷塘铺满碧绿荷叶粉荷花悄悄冒出头🍧🪁 🪷",
"🎄🎃你要相信，一切都会好起来的🎉✨ 🎊",
"🎈 💟 我爱你，你要记得我🌷🍃 🌱",
"🌫️ 💐 深秋山林铺满红黄叶，挺适合一个人慢慢放空🎐🍃 🍁",
"🪨 🌊 登顶之后视野彻底敞开，心胸跟着开阔起来🦋🍑 ✨",
"🍃 🦋 芦苇丛藏着小虫鸣唱，凑成山野小曲🍁🎏 💧",
"🧺 🌷 春日细雨细细润着山坡，满眼鲜活嫩绿色🪻🍧 ☔",
"🪁 🌾 傍晚云团染上蜜桃粉，倒映在平静湖面，很美💐🪨 🌇",
"🎏 💧 连绵矮丘紧紧挨在一起，薄雾轻轻缠绕像一幅淡彩画作🍑🦋 🍃",
"🌴 🌳 你要自由，要勇敢，要所向披靡🌼🌸 💐",
"🦋 🌫️ 雾气漫过整片郊野，只露出一截山头，朦朦胧胧🍧🌊 🌸",
"🍧 🎏 环湖绿道一路绿树，走走停停自在惬意🌷🪁 🌤️",
"🍄 🍀 沿着这条小路，就能走出大山🌹⭐ 💫",
"🎵 🔥 一定要平平安安，团团圆圆💥♥️ 🔆",
"💨 🌱 是你头顶的云，是你耳畔的风，是你涉过潮来潮去🌲🌾 🍁",
"🚗 👩‍🦰 你不在，即便身处人山人海，一样孤独☔💧 ⚡",
"🌤️ 🌊 万物皆有裂痕，那是光照进来的地方☄️🌟 💨",
"🪻 🌖 悬崖边的藤蔓肆意蔓延，小花一簇簇簇拥💐🎏 🌿",
"👚 🏝️ 愿你肆意且温柔，热烈且自由🌪️💍 👑",
"🌠 🗻 你看，你那么喜欢我，我都看到了🏡🎀 👒",
"🌷 🧺 小鱼游来游去，蹲在岸边能看上好半天🪻🌅 💦",
"🥺 🤓 勇敢的你，给自己一点小小奖励吧🐯🦋 🐝",
"🎐 🌾 多想躺下闭眼吹风，所有疲惫瞬间消散🍧🪁 ☁️",
"🪨 🎐 漫天晚霞粉紫橙红层层交织，氛围感拉满💧🦋 😻",
"🪁 🍑 芦苇伫立河道，飞鸟掠过水面，人间烟火🪻🌅 🛶",
"🦊 💧 幽深山谷清泉顺着石阶流淌，伸手满是清凉🌷🌾 🍂",
"🎏 🦋 春日暖风推着云絮，野花铺满沿路🍧🪨 🌸",
"🐛 🍃 深夜月光轻铺满林间小路，安静只闻虫鸣🧺💐 🌙",
"💐 🌊 四季都有不同景致，随便走走都有惊喜🪁🍑 🌤️",
"🍧 🐥 落日下沉时，万家灯火慢慢依次亮起🐸🦋 ✨",
"🌾 🎏 山边果园挂满熟透果子，果香随风飘向远处🪨🌷 🍎",
"🦋 💧 林间小路阳光碎碎漏下来，光影斑驳特别出片🍑🪁 🍃",
"🍑 🍜 平静湖面整片落日霞光，水天一色，温柔治愈🍄🪻 🥒",
"🥥 🍃 长风吹散堆积云层，远近风光全部尽收眼底💧🥦 🍭",
"🍰 🥔 只要认真且真诚，冰山也会慢慢融化🍭🍫 🍯",
"🍆 🍉 你今天有没有笑一笑呀👀👅 👄"
"💋 💛 做人嘛，当然是开心最重要啦🎊🎄 🥝",
"🍓 🌊 细雨轻轻敲打湖面，安静适合独自散心🪨🍐 ☔",
"💪 🙏 偶尔停下脚步，看看沿途的风景👀💖 ⛄",
"❤️‍🔥 💐 黄昏归鸟成群飞回山林，落日最后一抹暖光🪻🍑 💗",
"🍃 💧 石头缝里冒出野花，生命力旺盛得惊人🎐🌷 🌸",
"🎃 🌾 雨后的泥土混着嫩青草，呼吸都格外舒心🪁🎄 🍃",
"🎱 💧 深夜星河铺满天空，我抬头撞见漫天星光🥇💐 ✨",
"💃 🏆 勇敢的人先享受人生⚽🚗 🚀",
"🏵️ 🪨 村口老榕树遮天蔽日，老人孩童围坐乘凉🌇🍑 🧨",
"🙈 😅 最后的最后，一切归于沉寂💅🍺 🌶️",
"👰 🐇 山涧浅滩水流轻快奔走，治愈所有坏情绪🪻🌊 🕊️",
"🐮 🐈 山坡开满油菜花，风吹过掀起层层金色浪涛🦞🪁 🌼",
"🖥️ 🚿 深山野径草木，最原始纯粹的山野气息👻❄️ 🍂",
"🙆 🌛 夏日山林隔绝燥热了，这里乘凉太舒服📕👍 🫵",
"🌸 💚 薄云零散飘在蓝天之上，青山底色干净纯粹🐟🦌 🌤️",
"🌝 🔻 小溪弯弯曲曲，水草随水流摆动，灵动鲜活🔔🎏 🔆",
"☎️ ⏰ 深秋落日早早沉进山后，余晖染红半边天空💡🔦 🍁",
"💰 💸 乡村矮坡种满各色野花，没有人工雕琢📱📸 🌸",
"🫧 🎖️ 大雾填满幽深山谷朦朦胧胧像走进仙境幻境🎆🏠 ☁️",
"🎐 🌅 石阶小路直通山顶，沿途风光层层变换🌠🏖️ ⛰️",
"🗾 🎡 春日细雨滋润山间草木，满眼是治愈嫩绿🌋🖼️ ☔",
"🌁 ⛲ 大片湖面安安静静铺在群山之间，水面平滑如镜👨‍💼🎏 🌫️",
"🧚‍♀️ 💐 山间野菊秋日开花了，淡淡花香随风四处飘散🧚‍♂️🌅 🌼",
"🍃 🧜‍♂️ 岸边垂柳垂落水面，搅碎一整片温柔落日霞光💧🍑 🌴",
"🧜‍♀️ 🪻 拂晓时分残月挂在山尖，微光淡淡笼罩山野👰🏕️ 🌙",
"🗼 🎏 郊外旷野没有高楼遮挡，视野辽阔，心境舒展💍👗 ✨",
"👑 👜 水乡河道，小桥流水藏着慢悠悠的安逸生活🪭👚 🪷",
"💁‍♀️ 🌍 连绵小山紧紧依偎在一起，柔和得像手绘水彩画🎏⚡ ⛰️",
"🌫️ 💧 雨后天空澄澈透亮，青山翠色浓郁🌒⭐ 🌤️",
"🌨️ ❄️ 草坪上的蒲公英随风飘散，满是温柔童趣🌟🌪️ 🌱",
"🦋 ☔ 山中小湖藏在密林深处，很少有人打扰🌤️🌅 🌊",
"👱‍♀️ ♏ 秋日晚风卷着落叶四处飞舞，安静清幽🧸♈ 🍂",
"⌚ 🧬 淡粉晚霞漫过山脊，柔光铺满每条小路📷💐 🌇",
"🕯️ 🕰️ 清晨飞鸟绕着山头盘旋鸣叫，唤醒沉睡山野🧭⚖️ ☀️",
"🧲 💸 老旧石桥静卧河面多年，藤蔓爬满桥身🔭💈 🛶",
"⏰ 🔌 平缓草坡挨着绵长青山，所有生活烦恼全都放下⚙️⚒️ ☁️",
"🧺 💐 深山泉水质清冽甘甜，洗掉满身疲惫🌾🪻 🌿",
"💎 🏮 暮色覆盖整片郊野，目中远山渐渐模糊🛎️🧽 ⛰️",
"🎼 🌀 这一生，幸而有你在身边☂️ ⛺ 🎸",

]

# ========================================
# 4. 标签池（每次随机选3个，无需任何符号）
# ========================================
tag_pool = ["南城", "东城", "万江", "中堂", "麻涌", "望牛墩", "洪梅", "道滘", "高埗","石碣","石龙","茶山","石排","企石","横沥","桥头","谢岗","东坑","常平","寮步","大岭山","大朗","黄江","樟木头","塘厦","清溪","凤岗","虎门","长安","厚街","沙田","松山湖","东莞会所","东莞95"]

# ========================================
# 5. 固定按钮（改成你自己的链接）
# ========================================
def build_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="🎉东莞快餐🎉", url="https://t.me/bfcj888")
    btn2 = InlineKeyboardButton(text="🎊东莞会所🎊", url="https://t.me/hsdh668")
    keyboard.add(btn1, btn2)
    return keyboard

# ========================================
# 6. 组装消息：随机文字 + 3个剧透标签（点击才显示）
# ========================================

def build_caption():
    text = random.choice(text_templates)
    raw_tags = random.sample(tag_pool, k=3)
    
    spoiler_tags = []
    for tag in raw_tags:
        # 在标签后面加一个空格，这样点开后就有间隔了
        spoiler_tags.append(f"<tg-spoiler>#{tag} </tg-spoiler>")
    
    # 还是用空字符串拼接，因为空格已经在每个块里面了
    tag_str = "".join(spoiler_tags)
    
    return f"{text} {tag_str}"
# ========================================
# 7. 初始化机器人
# ========================================
CHANNEL_IDS = [ch.strip() for ch in CHANNEL_ID.split(",") if ch.strip()]
bot = telebot.TeleBot(BOT_TOKEN)

# ========================================
# 8. 发送一条随机内容
# ========================================
def send_random_post():
    if not CHANNEL_IDS:
        print("❌ 没有频道ID")
        return

    caption = build_caption()
    keyboard = build_keyboard()

    if photo_ids:
        media_id = random.choice(photo_ids)
        for ch_id in CHANNEL_IDS:
            try:
                bot.send_photo(ch_id, media_id,
                               caption=caption,
                               reply_markup=keyboard,
                               parse_mode='HTML')
                print(f"✅ 已发图片到 {ch_id}")
            except Exception as e:
                print(f"❌ 发送图片到 {ch_id} 失败: {e}")
    else:
        for ch_id in CHANNEL_IDS:
            try:
                bot.send_message(ch_id, caption,
                                 reply_markup=keyboard,
                                 parse_mode='HTML')
                print(f"✅ 已发文字到 {ch_id}")
            except Exception as e:
                print(f"❌ 发送文字到 {ch_id} 失败: {e}")

# ========================================
# 9. 主循环：每5分钟发一次
# ========================================
if __name__ == "__main__":
    print("机器人已启动，每5分钟发送一次...")
    while True:
        send_random_post()
        time.sleep(300)
