# coding=utf-8
"""
第一个策略：先计算过去90日内处于目标价格区间[0, a]的天数（down）,
和处于区间[1.1a, max]的天数(up)，再计算比值up/down，决定买入或卖出
"""
from ctaBase import *
from ctaTemplate import CtaTemplate

class Up2downRate(CtaTemplate):
    """高低比率策略"""
    className = 'Up2DownRate'
    author = 'greglchen'

    # 策略参数
    priceType = 'C'     # OHLC中的某一种价格
    beta = 1.1          # 价格浮动区间
    highRate = 0.6667   # up/down的临界值，高于此值买入
    lowRate = 0.3333    # up/down的临界值，低于此值卖出
    lookbackDays = 365  # 回测区间长度

    # 策略变量
    bar = None
    barDay = EMPTY_STRING
    secId = EMPTY_STRING   #股票ID
    upDays = EMPTY_INT     # up日期天数
    downDays = EMPTY_INT   # down日期天数
    preBars = None         # 最近的行情BAR DATAFRAME

    paramList = ['name',
                 'className',
                 'author',
                 'vtSymbol',
                 'priceType',
                 'beta',
                 'highRate',
                 'lowRate',
                 'lookbackDays']

    varList = ['inited',
               'trading',
               'pos',
               'secId',
               'upDays',
               'downDays']

    def __init__(self, ctaEngine, setting, secId):
        super(Up2downRate, self).__init__(ctaEngine, setting)
        self.upDays = 0
        self.downDays = 0
        self.secId = secId
        self.preBars =

    def getUpDownDays(self, barList, initPrice):
        high_filter = barList['highestPrice'] >= initPrice * self.beta
        low_filter = barList['lowestPrice'] <= initPrice
        return len(barList[high_filter].index), len(barList[low_filter].index)

    def onInit(self):
        self.writeCtaLog(u'UP2DOWN策略初始化')

        self.preBars = self.loadStockBar(self.lookbackDays, self.secId)
        if self.priceType == 'C':
            initPrice = self.preBars[-1]['closePrice'].values[0]
        self.upDays, self.downDays = self.getUpDownDays(self.preBars, initPrice)
        self.putEvent()





