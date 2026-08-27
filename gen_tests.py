# -*- coding: utf-8 -*-
"""生成 T2-T6 五张不同主题的星座测试 H5（自包含，零外链）。
T1（隐藏星座能量）已存在于仓库根目录 index.html，本脚本不再生成。
运行：python gen_tests.py
"""
import json, os

# 每个测试：目录、标题、封面、配色、题库、结果
TESTS = [
{
  "dir": "pair",
  "title": "你和哪个星座最有缘分？",
  "h1": "你和哪个星座<br>最有缘分？",
  "sub": "不考星座知识，只测你骨子里的吸引力类型。<br>8 个小问题，2 分钟，看清你最合拍的那类人。",
  "grad": ["#5b2a4a", "#9c3f7a", "#c95b9e"],
  "accent": "#ffd0e6",
  "card": "星座缘分测试",
  "foot_cover": "关注【时光里的星与心】<br>回复「测试」随时再测",
  "foot_result": "关注【时光里的星与心】回复「测试」随时再测<br>对的人，值得被遇见。",
  "questions": [
    {"q":"你最被哪种人吸引？","o":[
      {"t":"敢爱敢恨、说干就干的","d":"A"},{"t":"踏实靠谱、说话算数的","d":"B"},
      {"t":"脑洞大、聊不完的","d":"C"},{"t":"敏感温柔、懂你情绪的","d":"D"}]},
    {"q":"吵架后你通常？","o":[
      {"t":"当场吵完就翻篇","d":"A"},{"t":"先冷静，再讲道理","d":"B"},
      {"t":"吐槽完就当没发生","d":"C"},{"t":"闷在心里，但记很久","d":"D"}]},
    {"q":"理想周末约会？","o":[
      {"t":"一起去冒险 / 运动","d":"A"},{"t":"在家做饭、安稳相处","d":"B"},
      {"t":"看展 / 逛市集 / 认识新朋友","d":"C"},{"t":"深夜长谈、互相交心","d":"D"}]},
    {"q":"对方怎么做最让你安心？","o":[
      {"t":"直接表达喜欢，不猜","d":"A"},{"t":"默默把你照顾周到","d":"B"},
      {"t":"跟你分享新鲜事和想法","d":"C"},{"t":"记得你的小情绪","d":"D"}]},
    {"q":"你给恋人的关键词？","o":[
      {"t":"热烈","d":"A"},{"t":"可靠","d":"B"},{"t":"有趣","d":"C"},{"t":"懂我","d":"D"}]},
    {"q":"感情里你最怕？","o":[
      {"t":"被冷落、被忽视","d":"A"},{"t":"不稳、没保障","d":"B"},
      {"t":"被绑死、没自由","d":"C"},{"t":"冷漠、不沟通","d":"D"}]},
    {"q":"你表达爱的方式？","o":[
      {"t":"行动直接、大方示爱","d":"A"},{"t":"用行动和承担","d":"B"},
      {"t":"逗你开心、一起玩","d":"C"},{"t":"细腻陪伴、共情","d":"D"}]},
    {"q":"用一种元素形容你的爱？","o":[
      {"t":"火","d":"A"},{"t":"大地","d":"B"},{"t":"风","d":"C"},{"t":"水","d":"D"}]},
  ],
  "results": {
    "A":{"tag":"火象缘份","title":"你是「火象缘份」","const":"最合：白羊 / 狮子 / 射手",
      "desc":"你爱得直接又热烈，最吃不消暧昧拉扯。你需要一个也敢爱敢恨、能和你并肩往前冲的人。和火象在一起，日子永远有劲、不无聊。",
      "quote":"你要的爱，是明目张胆、不含糊的。"},
    "B":{"tag":"土象安稳","title":"你是「土象安稳」","const":"最合：金牛 / 处女 / 摩羯",
      "desc":"你向往的稳定，不是 boring，是「有人在」的踏实。你不需要天天惊喜，但要信得过、靠得住。土象给你的，是能把日子过踏实的那份安心。",
      "quote":"你要的浪漫，是落在日子里的靠谱。"},
    "C":{"tag":"风象同频","title":"你是「风象同频」","const":"最合：双子 / 天秤 / 水瓶",
      "desc":"你先被脑子吸引，再被心打动。你需要一个能接住你奇思妙想、也给你自由的人。和风象在一起，是聊不完的天、玩不尽的新鲜。",
      "quote":"你要的爱，是灵魂同频、各自自由。"},
    "D":{"tag":"水象深情","title":"你是「水象深情」","const":"最合：巨蟹 / 天蝎 / 双鱼",
      "desc":"你爱得深，也敏感。你渴望被懂，而不是被道理说服。和水象在一起，是情绪被接住、心事有人接盘的温柔。",
      "quote":"你要的爱，是被读懂、被温柔以待。"},
  },
},
{
  "dir": "love",
  "title": "你的隐藏恋爱体质是哪一种？",
  "h1": "你的隐藏恋爱体质<br>是哪一种？",
  "sub": "不考恋爱经验，只测你骨子里的爱人方式。<br>8 个小问题，2 分钟，看清你是怎么去爱的。",
  "grad": ["#6b1f3a", "#b03a5e", "#e0658f"],
  "accent": "#ffb3c8",
  "card": "恋爱体质测试",
  "foot_cover": "关注【时光里的星与心】<br>回复「测试」随时再测",
  "foot_result": "关注【时光里的星与心】回复「测试」随时再测<br>你的爱，值得被好好接住。",
  "questions": [
    {"q":"恋爱里你最常扮演？","o":[
      {"t":"照顾对方的人","d":"A"},{"t":"保持自我的那个人","d":"B"},
      {"t":"一起规划未来的人","d":"C"},{"t":"安抚对方情绪的人","d":"D"}]},
    {"q":"对方加班很累，你？","o":[
      {"t":"默默准备好饭和热水","d":"A"},{"t":"让 TA 好好休息，别打扰","d":"B"},
      {"t":"帮 TA 把明天安排好","d":"C"},{"t":"陪着听 TA 吐槽","d":"D"}]},
    {"q":"你最在意的承诺是？","o":[
      {"t":"我会一直在","d":"A"},{"t":"我们各自自在","d":"B"},
      {"t":"一起把日子过好","d":"C"},{"t":"我懂你","d":"D"}]},
    {"q":"吵架时你？","o":[
      {"t":"先哄、怕关系裂","d":"A"},{"t":"需要空间、别逼我","d":"B"},
      {"t":"讲清楚问题再和好","d":"C"},{"t":"先缓和气氛、别伤感情","d":"D"}]},
    {"q":"你给恋人的感觉？","o":[
      {"t":"安心","d":"A"},{"t":"自由","d":"B"},{"t":"踏实有盼头","d":"C"},{"t":"温暖","d":"D"}]},
    {"q":"你最怕的恋爱状态？","o":[
      {"t":"对方不需要我","d":"A"},{"t":"被控制失去自我","d":"B"},
      {"t":"看不见未来","d":"C"},{"t":"冷漠疏离","d":"D"}]},
    {"q":"表达爱靠？","o":[
      {"t":"行动照顾","d":"A"},{"t":"给彼此空间","d":"B"},
      {"t":"一起成长规划","d":"C"},{"t":"共情陪伴","d":"D"}]},
    {"q":"用一词形容你的爱？","o":[
      {"t":"守护","d":"A"},{"t":"自由","d":"B"},{"t":"深耕","d":"C"},{"t":"治愈","d":"D"}]},
  ],
  "results": {
    "A":{"tag":"守护型恋人","title":"你是「守护型恋人」","const":"爱的方式：把 TA 稳稳接住",
      "desc":"你不擅长说漂亮话，却总在用行动把对方护在身后。你给的安心，是「有我在」三个字。被你爱着的人，往往最舍不得离开。",
      "quote":"你的爱，是沉默却最稳的靠山。"},
    "B":{"tag":"自由型恋人","title":"你是「自由型恋人」","const":"爱的方式：亲密也各自生长",
      "desc":"你相信好的爱情是两人都自由。你给得了空间，也渴望空间。你不爱捆绑，却能在自由里把关系处得松弛又长久。",
      "quote":"你的爱，是亲密里也留给彼此天地。"},
    "C":{"tag":"深耕型恋人","title":"你是「深耕型恋人」","const":"爱的方式：把未来一点点种出来",
      "desc":"你谈恋爱像种树，不急着开花，先扎根。你愿意和一个人慢慢把日子经营成想要的样子。你的长情，是最被低估的浪漫。",
      "quote":"你的爱，是慢慢长成未来的样子。"},
    "D":{"tag":"治愈型恋人","title":"你是「治愈型恋人」","const":"爱的方式：接住对方的情绪",
      "desc":"你天生敏感温柔，总能先察觉对方的不对劲。你用共情把关系里的毛刺抚平。和你在一起，很多人第一次觉得「被懂」原来这么暖。",
      "quote":"你的爱，是别人也想靠近的暖。"},
  },
},
{
  "dir": "career",
  "title": "你的事业天赋星图是哪一张？",
  "h1": "你的事业天赋星图<br>是哪一张？",
  "sub": "不考简历，只测你骨子里的职场能量。<br>8 个小问题，2 分钟，看清你最被低估的天赋。",
  "grad": ["#5a3a12", "#a06a1e", "#e0a23c"],
  "accent": "#ffe0a0",
  "card": "事业天赋测试",
  "foot_cover": "关注【时光里的星与心】<br>回复「测试」随时再测",
  "foot_result": "关注【时光里的星与心】回复「测试」随时再测<br>你的天赋，值得被看见。",
  "questions": [
    {"q":"接新项目你第一反应？","o":[
      {"t":"冲上去试试","d":"A"},{"t":"先把基础打牢","d":"B"},
      {"t":"找人组队一起","d":"C"},{"t":"想清楚再出手","d":"D"}]},
    {"q":"你最享受的工作状态？","o":[
      {"t":"开荒、从 0 到 1","d":"A"},{"t":"把一件事做到极致","d":"B"},
      {"t":"和人协作碰撞","d":"C"},{"t":"从框架到细节都自己控","d":"D"}]},
    {"q":"同事怎么形容你？","o":[
      {"t":"敢闯","d":"A"},{"t":"靠谱","d":"B"},{"t":"会来事","d":"C"},{"t":"有想法","d":"D"}]},
    {"q":"你最怕的工作？","o":[
      {"t":"重复没变化","d":"A"},{"t":"浮于表面不落地","d":"B"},
      {"t":"单打独斗没团队","d":"C"},{"t":"杂乱没章法","d":"D"}]},
    {"q":"你的优势在？","o":[
      {"t":"嗅觉和冲劲","d":"A"},{"t":"耐心和执行","d":"B"},
      {"t":"沟通和统筹","d":"C"},{"t":"审美和体系","d":"D"}]},
    {"q":"升职你更想？","o":[
      {"t":"去新业务线","d":"A"},{"t":"把本职做成专家","d":"B"},
      {"t":"带团队","d":"C"},{"t":"主导一个产品","d":"D"}]},
    {"q":"做事风格？","o":[
      {"t":"先行动再修正","d":"A"},{"t":"准备充分才动","d":"B"},
      {"t":"边聊边推进","d":"C"},{"t":"先搭框架","d":"D"}]},
    {"q":"用一词形容你的职场力？","o":[
      {"t":"开拓","d":"A"},{"t":"深耕","d":"B"},{"t":"联结","d":"C"},{"t":"缔造","d":"D"}]},
  ],
  "results": {
    "A":{"tag":"开拓者","title":"你是「开拓者」","const":"天赋：嗅觉 + 冲劲",
      "desc":"你天然对机会敏感，别人还在犹豫，你已经迈出第一步。你不惧从 0 到 1 的荒原，反而享受开荒的爽感。把你的冲劲配上一个能落地的搭档，就是王炸。",
      "quote":"你最擅长的事，是把空白变成可能。"},
    "B":{"tag":"深耕者","title":"你是「深耕者」","const":"天赋：耐心 + 执行",
      "desc":"你信慢就是快。一件事交给你，你能磨到极致、落到地上。你不追风口，却总在时间里把结果挣回来。你的靠谱，是团队最硬的底层。",
      "quote":"你默默扎根的样子，时间都看得到。"},
    "C":{"tag":"联结者","title":"你是「联结者」","const":"天赋：沟通 + 统筹",
      "desc":"你是团队里的黏合剂。你懂人性、会协调，能把不对付的人拧成一股绳。很多事不是你亲手做，却因你而成了。",
      "quote":"你最厉害的，是让对的人遇上对的事。"},
    "D":{"tag":"缔造者","title":"你是「缔造者」","const":"天赋：审美 + 体系",
      "desc":"你既看得到蓝图，也抠得下细节。你不满足做零件，想亲手把一个东西从骨架搭到成型。给你舞台，你能造出有你印记的作品。",
      "quote":"你想要的，是从无到有的那一整个作品。"},
  },
},
{
  "dir": "social",
  "title": "你的社交面具是哪一种人格？",
  "h1": "你的社交面具<br>是哪一种人格？",
  "sub": "不考社恐社牛，只测你在人群里的真实气质。<br>8 个小问题，2 分钟，看清你的社交面。",
  "grad": ["#143a36", "#1f6e62", "#3cb0a0"],
  "accent": "#b3f0e6",
  "card": "社交面具测试",
  "foot_cover": "关注【时光里的星与心】<br>回复「测试」随时再测",
  "foot_result": "关注【时光里的星与心】回复「测试」随时再测<br>你的样子，本来就很好。",
  "questions": [
    {"q":"聚会里你通常？","o":[
      {"t":"活跃气氛的那位","d":"A"},{"t":"安静听、偶尔接话","d":"B"},
      {"t":"串场、认识新朋友","d":"C"},{"t":"照顾落单的人","d":"D"}]},
    {"q":"陌生人面前你？","o":[
      {"t":"很快自来熟","d":"A"},{"t":"先观察再开口","d":"B"},
      {"t":"聊几句就热络","d":"C"},{"t":"礼貌又体贴","d":"D"}]},
    {"q":"朋友找你帮忙？","o":[
      {"t":"爽快答应","d":"A"},{"t":"评估后再给方案","d":"B"},
      {"t":"帮你想多种办法","d":"C"},{"t":"先安顿你的情绪","d":"D"}]},
    {"q":"你的社交能量来自？","o":[
      {"t":"被大家围着","d":"A"},{"t":"高质量的少数","d":"B"},
      {"t":"新鲜的人和事","d":"C"},{"t":"深度的连接","d":"D"}]},
    {"q":"别人对你的第一印象？","o":[
      {"t":"开朗","d":"A"},{"t":"稳重","d":"B"},{"t":"有趣","d":"C"},{"t":"好相处","d":"D"}]},
    {"q":"你最累的社交？","o":[
      {"t":"冷场尴尬","d":"A"},{"t":"无效寒暄","d":"B"},
      {"t":"被贴标签","d":"C"},{"t":"表面客套","d":"D"}]},
    {"q":"表达观点你？","o":[
      {"t":"直接大方","d":"A"},{"t":"想清楚再说","d":"B"},
      {"t":"换个角度逗趣说","d":"C"},{"t":"委婉体贴","d":"D"}]},
    {"q":"用一词形容你的社交面？","o":[
      {"t":"阳光","d":"A"},{"t":"沉稳","d":"B"},{"t":"灵动","d":"C"},{"t":"温暖","d":"D"}]},
  ],
  "results": {
    "A":{"tag":"阳光型","title":"你是「阳光型」","const":"社交气质：开朗自来熟",
      "desc":"你一进场，气氛就亮了。你不怕冷场，也愿意把 C 位让给快乐。很多人因为你而放松下来。你的热乎劲，是天然的人际润滑剂。",
      "quote":"你所在的地方，尴尬就少一半。"},
    "B":{"tag":"沉稳型","title":"你是「沉稳型」","const":"社交气质：安静有分量",
      "desc":"你话不多，但每句都踩在点上。你不需要喧哗也存在感十足，因为大家知道你靠谱。和你相处，是一种不被消耗的稳定。",
      "quote":"你的安静，本身就是一种力量。"},
    "C":{"tag":"灵动型","title":"你是「灵动型」","const":"社交气质：有趣会串场",
      "desc":"你是社交里的变量，总能把话题拐到新鲜处。你认识人多、聊得来，是聚会上最会破冰的那位。和你聊过，很少有人觉得闷。",
      "quote":"你一开口，气氛就活了。"},
    "D":{"tag":"温暖型","title":"你是「温暖型」","const":"社交气质：体贴会照顾",
      "desc":"你总先看见那个被落单的人。你不抢风头，却让每个人都被照顾到。很多人把你当「安全屋」——靠近你就觉得被接纳。",
      "quote":"你给的体贴，是别人想靠近的理由。"},
  },
},
{
  "dir": "emotion",
  "title": "你的情绪底色是哪一种？",
  "h1": "你的情绪底色<br>是哪一种？",
  "sub": "不考情商高低，只测你骨子里的情绪气质。<br>8 个小问题，2 分钟，看清你是怎么消化情绪的。",
  "grad": ["#1a2a5b", "#2f4a9e", "#4a7bc9"],
  "accent": "#b3c8ff",
  "card": "情绪底色测试",
  "foot_cover": "关注【时光里的星与心】<br>回复「测试」随时再测",
  "foot_result": "关注【时光里的星与心】回复「测试」随时再测<br>你的情绪，值得被自己温柔以待。",
  "questions": [
    {"q":"情绪上来你？","o":[
      {"t":"立刻 externalize 爆发","d":"A"},{"t":"压下去自己消化","d":"B"},
      {"t":"来得快去得快","d":"C"},{"t":"先顾及别人感受","d":"D"}]},
    {"q":"开心时你？","o":[
      {"t":"恨不得全世界知道","d":"A"},{"t":"淡淡地满足","d":"B"},
      {"t":"拉人一起疯","d":"C"},{"t":"想分享给在乎的人","d":"D"}]},
    {"q":"你难过通常？","o":[
      {"t":"明显情绪低落","d":"A"},{"t":"一个人闷着","d":"B"},
      {"t":"换个环境就好了","d":"C"},{"t":"怕别人担心、强撑","d":"D"}]},
    {"q":"别人眼里的你？","o":[
      {"t":"爱憎分明","d":"A"},{"t":"情绪稳定","d":"B"},
      {"t":"善变但可爱","d":"C"},{"t":"温柔体贴","d":"D"}]},
    {"q":"你最怕的情绪？","o":[
      {"t":"委屈","d":"A"},{"t":"失控","d":"B"},
      {"t":"无聊停滞","d":"C"},{"t":"冲突冷战","d":"D"}]},
    {"q":"你处理压力？","o":[
      {"t":"正面刚","d":"A"},{"t":"默默扛","d":"B"},
      {"t":"转移注意力","d":"C"},{"t":"找人聊聊","d":"D"}]},
    {"q":"你的情绪像？","o":[
      {"t":"火","d":"A"},{"t":"深水","d":"B"},
      {"t":"风","d":"C"},{"t":"暖阳","d":"D"}]},
    {"q":"你最想被怎样对待？","o":[
      {"t":"别惹我、懂我","d":"A"},{"t":"给我空间","d":"B"},
      {"t":"陪我折腾","d":"C"},{"t":"抱抱我","d":"D"}]},
  ],
  "results": {
    "A":{"tag":"烈焰型","title":"你是「烈焰型」","const":"情绪底色：爱憎分明",
      "desc":"你的情绪是火，亮起来人人看得见。你不爱藏着，高兴就笑、委屈就闹。乍看难搞，实则最真——你从不对人玩虚的。",
      "quote":"你的真，是藏不住也懒得藏的。"},
    "B":{"tag":"静水型","title":"你是「静水型」","const":"情绪底色：深沉稳定",
      "desc":"你像深潭，表面平静，底下有浪。你习惯自己消化，不轻易示弱。你给人的稳定感，是很多人慌乱时的定海神针。",
      "quote":"你的平静，是很多人想靠的一岸。"},
    "C":{"tag":"疾风型","title":"你是「疾风型」","const":"情绪底色：来去自由",
      "desc":"你情绪来得快去得也快，像一阵风。你不爱纠缠，翻篇比谁都利索。和你相处轻松，因为你不记仇、不内耗。",
      "quote":"你翻篇的快，是对自己最大的温柔。"},
    "D":{"tag":"暖光型","title":"你是「暖光型」","const":"情绪底色：温润体贴",
      "desc":"你总先照顾别人的情绪，自己的委屈往后排。你像暖阳，不刺眼却让人想靠近。偶尔，也请允许自己被照亮。",
      "quote":"你给的暖，别忘了也留一点给自己。"},
  },
},
]

TPL = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>__TITLE__</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  body {
    font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    background: linear-gradient(160deg, __G0__ 0%, __G1__ 55%, __G2__ 100%);
    color: #fff; min-height: 100vh;
    display: flex; justify-content: center; align-items: flex-start;
  }
  #app { width: 100%; max-width: 480px; padding: 24px 20px 40px; }
  .screen { display: none; }
  .screen.active { display: block; animation: fade .35s ease; }
  @keyframes fade { from { opacity: 0; transform: translateY(8px);} to { opacity: 1; transform: none;} }
  .stars { font-size: 28px; text-align: center; margin-bottom: 8px; letter-spacing: 6px; }
  h1 { font-size: 24px; font-weight: 600; text-align: center; line-height: 1.4; margin-bottom: 14px; }
  .sub { text-align: center; font-size: 14px; opacity: .82; line-height: 1.7; margin-bottom: 28px; }
  .btn {
    display: block; width: 100%; padding: 15px; border: none; border-radius: 14px;
    background: __ACCENT__; color: #2a1a06; font-size: 16px; font-weight: 600;
    cursor: pointer; margin-top: 10px; transition: transform .15s;
  }
  .btn:active { transform: scale(.97); }
  .btn.ghost { background: rgba(255,255,255,.14); color: #fff; }
  .progress { height: 6px; background: rgba(255,255,255,.18); border-radius: 99px; margin-bottom: 18px; overflow: hidden; }
  .progress > i { display: block; height: 100%; background: __ACCENT__; width: 0; transition: width .3s; }
  .qcount { font-size: 13px; opacity: .8; margin-bottom: 8px; }
  .qtext { font-size: 18px; font-weight: 500; line-height: 1.6; margin-bottom: 18px; }
  .opt {
    display: block; width: 100%; text-align: left; padding: 15px 16px; margin-bottom: 12px;
    background: rgba(255,255,255,.10); border: 1px solid rgba(255,255,255,.18);
    border-radius: 14px; color: #fff; font-size: 15px; line-height: 1.5; cursor: pointer;
    transition: all .15s;
  }
  .opt:active { background: rgba(255,255,255,.22); border-color: __ACCENT__; }
  .result-tag { display:inline-block; padding:4px 12px; border-radius:99px; background:rgba(255,255,255,.2); color:__ACCENT__; font-size:13px; margin-bottom:12px; }
  .result-title { font-size: 26px; font-weight: 600; margin-bottom: 6px; }
  .result-const { font-size: 14px; opacity: .85; margin-bottom: 16px; }
  .result-desc { font-size: 15px; line-height: 1.85; opacity: .94; margin-bottom: 16px;
    background: rgba(255,255,255,.08); padding: 16px; border-radius: 14px; }
  .result-quote { font-size: 15px; text-align: center; color: __ACCENT__; font-weight: 500;
    padding: 14px; border-top: 1px dashed rgba(255,255,255,.3); border-bottom: 1px dashed rgba(255,255,255,.3); margin-bottom: 20px; line-height:1.6; }
  .sharecard { width: 100%; border-radius: 14px; margin-bottom: 14px; display: none; }
  .tip { text-align: center; font-size: 12px; opacity: .7; margin-top: 10px; line-height: 1.6; }
  .foot { text-align:center; font-size:12px; opacity:.6; margin-top:22px; line-height:1.7; }
</style>
</head>
<body>
<div id="app">
  <section id="cover" class="screen active">
    <div class="stars">✦ ✧ ✦</div>
    <h1>__H1__</h1>
    <p class="sub">__SUB__</p>
    <button class="btn" onclick="start()">开始测试 ✨</button>
    <p class="foot">__FOOT_COVER__</p>
  </section>
  <section id="quiz" class="screen">
    <div class="progress"><i id="bar"></i></div>
    <div class="qcount" id="qcount"></div>
    <div class="qtext" id="qtext"></div>
    <div id="opts"></div>
  </section>
  <section id="result" class="screen">
    <div style="text-align:center">
      <span class="result-tag" id="r-tag"></span>
      <div class="result-title" id="r-title"></div>
      <div class="result-const" id="r-const"></div>
    </div>
    <div class="result-desc" id="r-desc"></div>
    <div class="result-quote" id="r-quote"></div>
    <img class="sharecard" id="card" alt="分享卡">
    <button class="btn" onclick="makeCard()">生成我的分享卡 📲</button>
    <button class="btn ghost" onclick="restart()">再测一次</button>
    <p class="tip">长按上方分享卡即可保存 / 转发给朋友</p>
    <p class="foot">__FOOT_RESULT__</p>
  </section>
</div>
<script>
var questions = __QUESTIONS__;
var results = __RESULTS__;
var i = 0, score = {A:0,B:0,C:0,D:0};
function show(id){ document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active')); document.getElementById(id).classList.add('active'); window.scrollTo(0,0); }
function start(){ i=0; score={A:0,B:0,C:0,D:0}; render(); show('quiz'); }
function render(){
  var q = questions[i];
  document.getElementById('qcount').textContent = "第 " + (i+1) + " / " + questions.length + " 题";
  document.getElementById('bar').style.width = ((i)/questions.length*100) + "%";
  document.getElementById('qtext').textContent = q.q;
  var box = document.getElementById('opts'); box.innerHTML = "";
  q.o.forEach(function(op){
    var b = document.createElement('button');
    b.className = "opt"; b.textContent = op.t;
    b.onclick = function(){ choose(op.d); };
    box.appendChild(b);
  });
}
function choose(d){ score[d]++; i++;
  if(i < questions.length){ render(); }
  else { document.getElementById('bar').style.width = "100%"; finish(); }
}
function finish(){
  var best = "A", max = -1;
  ["A","B","C","D"].forEach(function(k){ if(score[k] > max){ max = score[k]; best = k; } });
  var r = results[best];
  document.getElementById('r-tag').textContent = r.tag;
  document.getElementById('r-title').textContent = r.title;
  document.getElementById('r-const').textContent = r.const;
  document.getElementById('r-desc').textContent = r.desc;
  document.getElementById('r-quote').textContent = r.quote;
  document.getElementById('card').style.display = "none";
  show('result');
}
function restart(){ show('cover'); }
function makeCard(){
  var cv = document.createElement('canvas'); cv.width = 600; cv.height = 800;
  var x = cv.getContext('2d');
  var g = x.createLinearGradient(0,0,0,800);
  g.addColorStop(0,"__G0__"); g.addColorStop(.55,"__G1__"); g.addColorStop(1,"__G2__");
  x.fillStyle = g; x.fillRect(0,0,600,800);
  x.textAlign = "center"; x.fillStyle = "__ACCENT__";
  x.font = "600 26px sans-serif"; x.fillText("✦  __CARD__  ✦", 300, 90);
  x.fillStyle = "#fff"; x.font = "600 52px sans-serif";
  x.fillText(document.getElementById('r-title').textContent.replace("你是「","").replace("」",""), 300, 200);
  x.fillStyle = "__ACCENT__"; x.font = "500 20px sans-serif";
  x.fillText(document.getElementById('r-const').textContent, 300, 250);
  x.fillStyle = "rgba(255,255,255,.92)"; x.font = "16px sans-serif";
  wrapText(x, document.getElementById('r-desc').textContent, 300, 320, 480, 28);
  x.fillStyle = "__ACCENT__"; x.font = "600 22px sans-serif";
  wrapText(x, document.getElementById('r-quote').textContent, 300, 600, 480, 32);
  x.fillStyle = "rgba(255,255,255,.7)"; x.font = "14px sans-serif";
  x.fillText("关注【时光里的星与心】回复「测试」随时再测", 300, 720);
  x.fillText("扫码/搜索公众号：时光里的星与心", 300, 748);
  var img = document.getElementById('card');
  img.src = cv.toDataURL("image/png");
  img.style.display = "block";
  img.scrollIntoView({behavior:"smooth", block:"center"});
}
function wrapText(ctx, text, cx, y, maxW, lh){
  var line = "", lines = [];
  for(var n=0; n<text.length; n++){
    var t = line + text[n];
    if(ctx.measureText(t).width > maxW && line){ lines.push(line); line = text[n]; }
    else line = t;
  }
  if(line) lines.push(line);
  lines.forEach(function(l, k){ ctx.fillText(l, cx, y + k*lh); });
}
</script>
</body>
</html>
"""

def build(t):
    html = TPL
    html = (html
        .replace("__TITLE__", t["title"])
        .replace("__H1__", t["h1"])
        .replace("__SUB__", t["sub"])
        .replace("__G0__", t["grad"][0])
        .replace("__G1__", t["grad"][1])
        .replace("__G2__", t["grad"][2])
        .replace("__ACCENT__", t["accent"])
        .replace("__CARD__", t["card"])
        .replace("__FOOT_COVER__", t["foot_cover"])
        .replace("__FOOT_RESULT__", t["foot_result"])
        .replace("__QUESTIONS__", json.dumps(t["questions"], ensure_ascii=False))
        .replace("__RESULTS__", json.dumps(t["results"], ensure_ascii=False))
    )
    return html

if __name__ == "__main__":
    for t in TESTS:
        d = os.path.join(os.path.dirname(__file__), t["dir"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(build(t))
        print("generated:", t["dir"], "->", t["title"])
    print("done. total tests:", len(TESTS) + 1, "(incl. T1 at root)")
