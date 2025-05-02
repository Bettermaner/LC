import copy
import math

def get_ndcg(x):
    """
    compute the NDCG value according to the formula ndcg = sum(1/(log2(posRanki+1)))/IDCG,
    where posRanki is the positive cases' rank index, and IDCG is the scaled DCG value
    :param x: list [(label_i,score_i),...]
    :return: NDCG value
    """
    # 深拷贝输入列表x，避免修改原始数据
    l = copy.deepcopy(x)
    
    # 根据score对l进行降序排序
    l.sort(key=lambda x: x[1], reverse=True)
    
    # 定义一个lambda函数来计算DCG值
    get_dcg = lambda rel: sum([rel / math.log((idx + 1 + 1),2) for idx, rel in enumerate(rel)])
    
    # 提取排序后的标签列表
    rel = [i[0] for i in l]
    
    # 如果没有正例，则返回0.0
    if not any(rel):
        return 0.0
    
    # 计算DCG值
    dcg = get_dcg(rel)
    
    # 对标签列表进行降序排序以计算IDCG值
    rel.sort(reverse=True)
    
    # 计算IDCG值
    idcg = get_dcg(rel)
    
    # 计算并返回NDCG值
    ndcg = dcg / idcg
    return ndcg