#-*-coding:utf8-*-
"""
item cf main Algo

"""
import sys
sys.path.append('../util')
import util.reader as reader
def cal_item_sim(user_click):
    """
    Args:
        user_click:dict,key userid value[itemid1,itemid2]
    :return:
        dict, key:itemid_i,value dict,value_key itemid_j,value_value simscore
    """
    co_appear = {}
    item_user_click_item = {}
    for user,itemlist in user_click.items():
        for index_i in range(0,len(itemlist)):
            itemid_i = itemlist[index_i]
            item_user_click_item.setdefault(itemid_i,0)
            item_user_click_item[itemid_i]+=1
            for index_j in range(index_i+1,len(itemlist)):
                itemid_j = itemlist[index_j]
                co_appear.setdefault(itemid_i,{})
                co_appear[itemid_i].setdefault()
def main_flow():
    """
    main flow of itemcf
    :return:
    """
    user_click = reader.get_user_click('../data/ratings.txt')
    sim_info = cal_item_sim(user_click)
    recom_result = cal_recom_result(sim_info,user_click)