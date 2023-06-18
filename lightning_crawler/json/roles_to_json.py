import json
roles = {
    '王馨瑶_Yanni': 'https://www.xsnvshen.com/girl/17424',
    '杨晨晨_Yome': 'https://www.xsnvshen.com/girl/22162',  # ycc
    '芝芝_Booty': 'https://www.xsnvshen.com/girl/22899',   # zhizhii
    '肉肉_Lavinia': 'https://www.xsnvshen.com/girl/26038',  # rourou
    '鱼子酱_Fish': 'https://www.xsnvshen.com/girl/28036',  # yuzijiang
    '周妍希_Carol': 'https://www.xsnvshen.com/girl/20763',  # zhouyanxi zyx naiping
    '安然_Maleah': 'https://www.xsnvshen.com/girl/27854',  # anrang
    '绮里嘉_Ula': 'https://www.xsnvshen.com/girl/18220',  # qilijia
    '尤妮丝_Egg': 'https://www.xsnvshen.com/girl/24936',  # younisi
    '周于希_Sally': 'https://www.xsnvshen.com/girl/24410',  # zhouyuxi
    '陆萱萱_LuXuanxuan': 'https://www.xsnvshen.com/girl/27559',  # luxuanxuan
    '梦心玥_Candice': 'https://www.xsnvshen.com/girl/23100',  # mengxinyue
    '小蛮妖_Yummy': 'https://www.xsnvshen.com/girl/27781',  # xiaomanyao
    '张思允_Nice': 'https://www.xsnvshen.com/girl/28252',  # zhangsiyun
    '小海臀_Rena': 'https://www.xsnvshen.com/girl/28190',  # xiaohaitun
    '朱可儿_Flora': 'https://www.xsnvshen.com/girl/17204',  # zhukeer
    '谢芷馨_Cheery': 'https://www.xsnvshen.com/girl/22514',  # xiezhixin cherry
    '唐安琪_TangAnqi': 'https://www.xsnvshen.com/girl/28098',  # tanganqi
    '熊小诺_XiongXiaonuo': 'https://www.xsnvshen.com/girl/28175',  # xiong xiaonuo
    '林星阑_LinXinglan': 'https://www.xsnvshen.com/girl/28158',  # lin xinglan
    '张欣欣_ZhangXinxin': 'https://www.xsnvshen.com/girl/28096',  # zhangxinxin
    '利世_LiShi': 'https://www.xsnvshen.com/girl/28202',  # lishi
    '妲己_Toxic': 'https://www.xsnvshen.com/girl/22359',  # tanji
    '诗诗_Kiki': 'https://www.xsnvshen.com/girl/19550',  # shishi
    '优优_Yoo': 'https://www.xsnvshen.com/girl/27863',  # youyou
    '糯美子_Minibabe': 'https://www.xsnvshen.com/girl/19411',  # mini
    '可乐_Vicky': 'https://www.xsnvshen.com/girl/22152',  # kele
    '王雨纯_WangYuchun': 'https://www.xsnvshen.com/girl/19702',  # wangyuchun
    '玛鲁娜_Manuela': 'https://www.xsnvshen.com/girl/20625',  # maluna
    '果儿_Victoria': 'https://www.xsnvshen.com/girl/19551',  # songguoer
    '小琪_Angela': 'https://www.xsnvshen.com/girl/22204',  # xiaoqi
    '尹菲_Emily': 'https://www.xsnvshen.com/girl/25332',  # SOLO
    '允薾_YunEr': 'https://www.xsnvshen.com/girl/28081',  # yuner
    '就是阿朱啊_JiuShiAZhuA': 'https://www.xsnvshen.com/girl/26002',  # jiushiazhu
    '何嘉颖_HeJiaying': 'https://www.xsnvshen.com/girl/21790',  # xingyi
    '沈梦瑶_ShenMengyao': 'https://www.xsnvshen.com/girl/21036',  # shemengyao
    '江真真_JiangZhenzhen': 'https://www.xsnvshen.com/girl/28290',
    '夏沫沫_Tifa': 'https://www.xsnvshen.com/girl/28231',
    '月音瞳_YueYintong': 'https://www.xsnvshen.com/girl/22490',
    '周九九_JojoBaby': 'https://www.xsnvshen.com/girl/28306',
    '夏诗雯_Sally': 'https://www.xsnvshen.com/girl/27761',
    '甜妮_Tianni': 'https://www.xsnvshen.com/girl/28250',
    '阿娇_Laura': 'https://www.xsnvshen.com/girl/28288',
    '林乐一_LinLeyi': 'https://www.xsnvshen.com/girl/28270',
    '温心怡_WenXinyi': 'https://www.xsnvshen.com/girl/22067',
    '吴雪瑶_WuXueyao': 'https://www.xsnvshen.com/girl/28134',
    '林依娜_Yina': 'https://www.xsnvshen.com/girl/25888',
    '尹甜甜_YinTiantian': 'https://www.xsnvshen.com/girl/28144',
    '雅雯_Yawen': 'https://www.xsnvshen.com/girl/16271',
    '林子遥_LinZiyao': 'https://www.xsnvshen.com/girl/28303',
    '媛媛酱_Belle': 'https://www.xsnvshen.com/girl/28199',
    '萌汉药_Baby': 'https://www.xsnvshen.com/girl/15769',
    '是小逗逗_DouDou': 'https://www.xsnvshen.com/girl/28210',
    '田冰冰_TianBingbing': 'https://www.xsnvshen.com/girl/27859',
    '玉兔_Miki': 'https://www.xsnvshen.com/girl/22186',
    '李浅浅_Danny': 'https://www.xsnvshen.com/girl/27667',
    '77_Qiqi': 'https://www.xsnvshen.com/girl/28192', # 16
    '茜茜_Kimi': 'https://www.xsnvshen.com/girl/22149',  # 6
    '余贝拉_Kimi': 'https://www.xsnvshen.com/girl/21017',  # 52

}

# girls_urls = [
#     # "https://www.xsnvshen.com/girl/22899",  # zhizhii
#     "https://www.xsnvshen.com/girl/22162",  # ycc
#     "https://www.xsnvshen.com/girl/17424",  # wangxinyao
#     "https://www.xsnvshen.com/girl/26038",  # rourou
#     "https://www.xsnvshen.com/girl/28036",  # yuzijiang
#     "https://www.xsnvshen.com/girl/20763",  # zhouyanxi zyx naiping
#     "https://www.xsnvshen.com/girl/27854",  # anrang
#     "https://www.xsnvshen.com/girl/18220",  # qilijia
#     "https://www.xsnvshen.com/girl/24936",  # younisi
#     "https://www.xsnvshen.com/girl/24410",  # zhouyuxi
#     "https://www.xsnvshen.com/girl/27559",  # luxuanxuan
#     "https://www.xsnvshen.com/girl/23100",  # mengxinyue
#     "https://www.xsnvshen.com/girl/27781",  # xiaomanyao
#     "https://www.xsnvshen.com/girl/28252",  # zhangsiyun
#     "https://www.xsnvshen.com/girl/28190",  # xiaohaitun
#     "https://www.xsnvshen.com/girl/17204",  # zhukeer
#     "https://www.xsnvshen.com/girl/22514",  # xiezhixin cherry
#     "https://www.xsnvshen.com/girl/28098",  # tanganqi
#     "https://www.xsnvshen.com/girl/28175",  # xiong xiaonuo
#     "https://www.xsnvshen.com/girl/28158",  # lin xinglan
#     "https://www.xsnvshen.com/girl/28096",  # zhangxinxin
#     "https://www.xsnvshen.com/girl/28202",  # lishi
#     "https://www.xsnvshen.com/girl/22359",  # tanji
#     "https://www.xsnvshen.com/girl/19550",  # shishi
#     "https://www.xsnvshen.com/girl/27863",  # youyou
#     "https://www.xsnvshen.com/girl/19411",  # mini
#     "https://www.xsnvshen.com/girl/22152",  # kele
#     "https://www.xsnvshen.com/girl/19702",  # wangyuchun
#     "https://www.xsnvshen.com/girl/20625",  # maluna
#     "https://www.xsnvshen.com/girl/19551",  # songguoer
#     "https://www.xsnvshen.com/girl/22204",  # xiaoqi
#     "https://www.xsnvshen.com/girl/25332",  # SOLO
#     "https://www.xsnvshen.com/girl/28081",  # yuner
#     "https://www.xsnvshen.com/girl/26002",  # jiushiazhu
#     "https://www.xsnvshen.com/girl/21790",  # xingyi
#     "https://www.xsnvshen.com/girl/21036",  # shemengyao
#     "https://www.xsnvshen.com/girl/28290"  # jiangzhenzhen
#
# ]


with open('roles.json', 'w', encoding='utf8') as f:
    json.dump(roles, f, ensure_ascii=False)

with open('roles.json', 'r') as f:
    a = json.load(f)
# print(a['优优_Yoo'])
# print(json.dumps(a, indent=4))
print(json.dumps(a, ensure_ascii=False, indent=4))