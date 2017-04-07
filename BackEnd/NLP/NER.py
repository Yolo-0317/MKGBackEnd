# -*- coding: utf-8 -*-
from BackEnd.NLP import CUT

import jieba
import jieba.posseg as pseg

# jieba.load_userdict("userdict.txt")

nerDit = {
    "PM": ('螺纹', '三角形螺纹', '矩形螺纹', '梯形螺纹', '锯齿形螺纹', '管螺纹', '粗牙普通螺纹', '细牙普通螺纹', '管联接用细牙普通螺纹',
           '非螺纹密封的55°圆柱管螺纹', '用螺纹密封的55°圆柱管螺纹', '60°圆锥管螺纹', '米制锥螺纹', '圆弧螺纹', '普通平键', '导向平键',
           '薄型平键', '滑键联接', '半圆键', '普通楔键', '钩头楔键', '切向键', '圆头普通平键(A型)', '平头普通平键(B型)', '单圆头普通平键(C型)',
           '普通切向键', '强力切向键', '花键', '花键联接', '矩形花键', '渐开线花键', '钢铆钉', '铜铆钉', '铝铆钉', '半圆头铆钉', '沉头铆钉',
           '半圆头钢铆钉', '沉头钢铆钉', '半沉头铆钉', '开口型扁圆头铆钉', '标牌铆钉', '熔化焊', '气焊', '电弧焊', '手工电弧焊', '埋弧焊',
           '氩弧焊', '二氧化碳气体保护焊', '真空电子束焊', '电渣焊', '对焊', '点焊', '缝焊', '钎焊', '碳钢焊条', '低合金钢焊条', '不锈钢焊条',
           '堆焊焊条', '铸铁焊条', 'E4300', 'E4301', 'E5001', 'E4303', 'E5003', 'E4311', 'E5011', 'E4313', 'E4353', 'E5015', 'E4316',
           'E4315', 'E5016', 'E4320', 'E4323', 'E4324', 'E5024', 'E4327', 'E5027', 'E5028', 'E5015-A1', 'E5500-B1', 'E5503-B1',
           'E5515-B1', 'E5515-B2', 'E5500-B2-V', 'E5515-B2-V', 'E5515-B2-VNb', 'E5515-B2-VW', '有机胶粘剂', '天然胶粘剂', '动物胶',
           '植物胶', '合成胶粘剂', '热塑性树脂型胶粘剂', '热固性树脂型胶粘剂', '橡胶型树脂型胶粘剂', '混合型胶粘剂', '无机胶粘剂', '磷酸盐型',
           '磷酸盐型胶粘剂', '硅酸盐型', '硅酸盐型胶粘剂', '硼酸盐型', '硼酸盐型胶粘剂', '结构型胶粘剂', '溶剂型胶粘剂', '反应型胶粘剂',
           '热塑性胶粘剂', '溶液型胶粘剂', '乳液型胶粘剂', '膏糊型胶粘剂', '粉末型胶粘剂', '环氧树脂胶粘剂', '酚醛树脂胶粘剂', '丙烯酸酯胶粘剂',
           '聚氨酯胶粘剂', '杂环高分子胶粘剂', '不饱和聚酯树脂胶粘剂', '螺栓联接', '双头螺柱联接', '螺钉联接', '紧定螺钉联接', '对顶螺母',
           '弹簧垫圈', '自锁螺母', '开口销与六角开槽螺母', '止动垫圈', '串联铁丝', '圆柱管螺纹', '左旋螺纹', '右旋螺纹', '单线螺纹', '粗牙螺纹',
           '细牙螺纹', '普通螺纹', '公制螺纹', '英制螺纹', '圆锥管螺纹', '英制细牙螺纹', '传动螺纹', '标准螺纹', '内螺纹', '外螺纹',
           '螺栓', '橡胶垫', '螺母', '垫圈', '垫片', '弹簧', '螺杆', ' 双头螺柱', ' 对顶螺母', '方牙螺纹', '圆弧形螺纹', '三角螺纹',
           '圆柱螺纹', '圆锥螺纹', '轴承衬', '轴瓦', '固体润滑剂轴承', '半固体润滑剂轴承', '液体润滑剂轴承', '高速轴承', '中速轴承',
           '低速轴承', '重载轴承', '中载轴承', '轻载轴承', '干摩擦轴承', '液体摩擦轴承', '液体润滑静压轴承', '动静压轴承', '液体动压轴承',
           '液体静压轴承', '非液体摩擦轴承', '径向-推力轴承', '推力轴承', '环形推力轴承', '空心推力轴承', '实心推力轴承', '整体式轴承', '剖分式轴承',
           '轴瓦', '轴承座', '轴承衬', '轴承盖', '双列角接触球轴承', '滚子轴承', '外球面球轴承', '四点接触球轴承', '圆锥孔外球面球轴承',
           '带偏心套外球面球轴承', '带顶丝外球面球轴承', '球面滚子轴承', '圆锥滚子轴承', '圆柱滚子轴承', '内圈无挡边双列圆柱滚子轴承',
           '双列圆柱滚子轴承', '外圈单挡边圆柱滚子轴承', '内圈单挡边圆柱滚子轴承', '内圈无挡边圆柱滚子轴承', '外圈无挡边圆柱滚子轴承',
           '球轴承', '推力圆柱滚子轴承', '向心滚动轴承', '推力滚动轴承', '推力圆柱滚子轴承', '角接触轴承', '深沟球轴承', '推力球轴承',
           '双向推力球轴承', '单向推力球轴承', '双列深沟球轴承', '调心滚子轴承', '调心球轴承', '保持架', '滚动体', '外圈', '内圈',
           '六角螺母', '圆螺母', '异型螺母', '扣紧螺母', '环形螺母', '盖形螺母', '组合式盖形螺母', '蝶形螺母', '', '', '', '', '', '', '', '',
           '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',),
    "MA": ('金属', '塑料', '橡胶', '玻璃', '铸铁', '碳素钢', '合金钢', '钢', '青铜', '多孔青铜', '多孔铁', '轴承青铜', '巴氏合金',
           '白合金', '铝青铜', '锡青铜', '铜锡的硬晶粒', '悬浮锡锑', '铅基合金', '锡基合金', '中碳钢', '低碳合金钢', '低碳钢', '',
           '', '', '', '', '', '', ''
    ),
    "STR": ('挤压强度', '剪切强度', '', '', '', '', ''),
    "TO": ('测力矩扳手', '定力矩扳手', '', '', '', '', ''),
    "PRC": ('刀具', '工件', '砂轮', '回火', '正火', '退火', '淬火', '', '', '', '', '', '', '', '', ''),
    "PARAM": ('公称直径', '最大直径', '最小直径', '导程', '线数', '螺距', '中径', '牙型')
}

def handleSentence(senStr):
    seg_list = CUT.jiebaCut(senStr)
    se = ''
    for i in seg_list:
        se += i + ' '

    words = pseg.cut(se)

    res = ''
    nerPM = []
    nerMA = []
    nerSTR = []
    nerTO = []
    nerPRC = []
    nerPARAM = []

    for word, flag in words:
        if (flag == 'n'):
            res += word + ' '
            if(word in nerDit['PM'] and (not word + '-PM' in nerPM)):
                nerPM.append(word + '-PM')
            elif(word in nerDit['MA'] and (not word + '-MA' in nerMA)):
                nerMA.append(word + '-MA')
            elif (word in nerDit['STR'] and (not word + '-STR' in nerSTR)):
                nerSTR.append(word + '-STR')
            elif (word in nerDit['TO'] and (not word + '-TO' in nerTO)):
                nerTO.append(word + '-TO')
            elif (word in nerDit['PRC'] and (not word + '-PRC' in nerPRC)):
                nerPRC.append(word + '-PRC')
            elif (word in nerDit['PARAM'] and (not word + '-PARAM' in nerPARAM)):
                nerPARAM.append(word + '-PARAM')
    return [
        {
            'type': '零件名称',
            'array': nerPM
        },
        {
            'type': '材料',
            'array': nerMA
        },
        {
            'type': '强度',
            'array': nerSTR
        },
        {
            'type': '工具',
            'array': nerTO
        },
        {
            'type': '加工',
            'array': nerPRC
        },
        {
            'type': ' 参数',
            'array': nerPARAM
        }
    ]

def nerForRE(senStr):
    seg_list = jieba.cut(senStr)
    se = ''
    for i in seg_list:
        se += i + ' '

    words = pseg.cut(se)

    res = ''
    nerPM = []
    nerMA = []
    nerSTR = []
    nerTO = []
    nerPRC = []
    nerPARAM = []
    allNer = []

    for word, flag in words:
        if (flag == 'n'):
            res += word + ' '
            if (word in nerDit['PM'] and (not word + '-PM' in nerPM)):
                nerPM.append(word + '-PM')
                allNer.append(word)
            elif (word in nerDit['MA'] and (not word + '-MA' in nerMA)):
                nerMA.append(word + '-MA')
                allNer.append(word)
            elif (word in nerDit['STR'] and (not word + '-STR' in nerSTR)):
                nerSTR.append(word + '-STR')
                allNer.append(word)
            elif (word in nerDit['TO'] and (not word + '-TO' in nerTO)):
                nerTO.append(word + '-TO')
                allNer.append(word)
            elif (word in nerDit['PRC'] and (not word + '-PRC' in nerPRC)):
                nerPRC.append(word + '-PRC')
                allNer.append(word)
            elif (word in nerDit['PARAM'] and (not word + '-PARAM' in nerPARAM)):
                nerPARAM.append(word + '-PARAM')
                allNer.append(word)
    return  allNer