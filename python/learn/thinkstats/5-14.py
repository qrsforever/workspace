#!/usr/bin/python3
# -*- coding: utf-8 -*-

def effectiveness(drug_rate, sensitivity, specificity):
    """
    计算后验概率(贝叶斯定理), 结果为阳性, 用药的概率
    drug_rate: 先验概率, (看到检验结果之前)用药率
    sensitivity: 灵敏度(似然值), 用药的情况下, 检验显示阳性的概率
    specificity: 特异性, 1-假阳性的概率

            未检验之前, 用药的概率
            先验概率
              ^           用药之后显示阳性的概率
              |     +---> 似然值(灵敏度)
              |     |
              |     |
              |    P(E|D)           P(D)*P(E|D)
    P(D|E) = P(D)*------- = ---------------------------
     |              P(E)     P(D)*P(E|D) + P(N)*P(E|N)
     |               |
     |               |
     v               +---> 归一化常量, 阳性概率, P(用药显示阳性)   +   P(不用药显示阳性)
    后验概率                                        真阳性         假阳性 = P(不用药)(1-特异性)
    结果显示阳性, 用药的概率

    """
    return (drug_rate * sensitivity) / (drug_rate * sensitivity + (1-drug_rate)*(1-specificity))

def main():
    drug_rates = [0.1, 0.05]
    sensitivity, specificity = 0.6, 0.99
    for rate in drug_rates:
        print("effectiveness(%.3f, %.3f, %.3f) = %.3f" % 
                (rate, sensitivity, specificity, effectiveness(rate, sensitivity, specificity)))

if __name__ == "__main__":
    main()
