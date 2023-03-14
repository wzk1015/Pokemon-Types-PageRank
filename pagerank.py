import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# from pylab import mpl
from pprint import pprint
 
# 设置中文显示字体
# mpl.rcParams["font.sans-serif"] = ["Arial"]
# mpl.rcParams['axes.unicode_minus']=False
# plt.rcParams['font.family']='sans-serif'

# """ types = ['一般', '格斗', '飞行', '毒', '地面', '岩石', '虫', '幽灵', '钢', '火', '水', '草', '电', '超能力', '冰', '龙', '恶', '妖精'] """
types = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']
edges = [ # https://wiki.52poke.com/wiki/%E5%B1%9E%E6%80%A7%E7%9B%B8%E5%85%8B%E8%A1%A8
    [1,1,1,1,1, 0.5,1,0,0.5,1, 1,1,1,1,1, 1,1,1],
    [2,1,0.5,0.5,1, 2,0.5,0,2,1, 1,1,1,0.5,2, 1,2,0.5],
    [1,2,1,1,1, 0.5,2,1,0.5,1, 1,2,0.5,1,1, 1,1,1],
    [1,1,1,0.5,0.5, 0.5,1,0.5,0,1, 1,2,1,1,1, 1,1,2],
    [1,1,0,2,1, 2,0.5,1,2,2, 1,0.5,2,1,1, 1,1,1],
    [1,0.5,2,1,0.5, 1,2,1,0.5,2, 1,1,1,1,2, 1,1,1],
    [1,0.5,0.5,0.5,1, 1,1,0.5,0.5,0.5, 1,2,1,2,1, 1,2,0.5],
    [0,1,1,1,1, 1,1,2,1,1, 1,1,1,2,1, 1,0.5,1],
    [1,1,1,1,1, 2,1,1,0.5,0.5, 0.5,1,0.5,1,2, 1,1,2],
    [1,1,1,1,1, 0.5,2,1,2,0.5, 0.5,2,1,1,2, 0.5,1,1],
    [1,1,1,1,2, 2,1,1,1,2, 0.5,0.5,1,1,1, 0.5,1,1],
    [1,1,0.5,0.5,2, 2,0.5,1,0.5,0.5, 2,0.5,1,1,1, 0.5,1,1],
    [1,1,2,1,0, 1,1,1,1,1, 2,0.5,0.5,1,1, 0.5,1,1],
    [1,2,1,2,1, 1,1,1,0.5,1, 1,1,1,0.5,1, 1,0,1],
    [1,1,2,1,2, 1,1,1,0.5,0.5, 0.5,2,1,1,0.5, 2,1,1],
    [1,1,1,1,1, 1,1,1,0.5,1, 1,1,1,1,1, 2,1,0],
    [1,0.5,1,1,1, 1,1,2,1,1, 1,1,1,2,1, 1,0.5,0.5],
    [1,2,1,0.5,1, 1,1,1,0.5,0.5, 1,1,1,1,1, 2,2,1]
] 

# 画网络图
def show_graph(graph):
    # 使用Spring Layout布局，类似中心放射状
    positions=nx.spring_layout(graph)
    # 设置网络图中的节点大小，大小与pagerank值相关，因为pagerank值很小所以需要*20000
    min_pagerank = min([x['pagerank'] for v,x in graph.nodes(data=True)])
    nodesize = [(1500 - (x['pagerank']-min_pagerank)*75000) for v,x in graph.nodes(data=True)]
    # print(nodesize)
    
    new_edges = [edge for edge in graph.edges(data=True) if edge[2]['weight'] != 1]
    
    
    # exit()
    # 设置网络图中的边长度
    # edgesize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
    # edgecolor = [e[2]['weight'] for e in graph.edges(data=True)]
    # colormap = {
    #     2 : "blue",
    #     # 1 :
    #     0.5 : "yellow",
    #     0 : "red",
    # }
    # edgecolor = [colormap[e[2]['weight']] for e in new_edges]
    edgecolor = [e[2]['weight'] for e in new_edges]
    
    # 绘制节点
    nx.draw_networkx_nodes(graph, positions, node_size=nodesize, alpha=0.4)
    # 绘制边
    nx.draw_networkx_edges(graph, positions, edgelist=new_edges, edge_color=edgecolor, alpha=0.9, edge_cmap=plt.cm.tab20, min_source_margin=20, min_target_margin=20)
    # nx.draw_networkx_edges(graph, positions, width=edgesize, alpha=0.2)
    # nx.draw_networkx_edges(graph, positions, alpha=0.2)
    # 绘制节点的label
    nx.draw_networkx_labels(graph, positions, font_size=7)
    # 输出希拉里邮件中的所有人物关系图
    plt.show()


def get_type_edges(mode="regular", ignore=None):
    edge_weights= []
    for idx, edge in enumerate(edges):
        assert len(edge) == len(types) == len(edges) == 18, edge
        for idy, weight in enumerate(edge):
            assert weight in [0, 0.5, 1, 2]
            if mode == 'attack':
                if idy != ignore:
                    edge_weights.append([types[idy], types[idx], weight])
            elif mode == 'defense':
                if idx != ignore:
                    edge_weights.append([types[idx], types[idy], weight])
            # if mode == "attack":
            #     if weight == 2:
            #         edge_weights.append([types[idx], types[idy], 2])
            # elif mode == "defense":
            #     if weight == 0.5:
            #         edge_weights.append([types[idx], types[idy], 1])
            #     elif weight == 0:
            #         edge_weights.append([types[idx], types[idy], 2])
            
            # if mode == "attack":
            #     if idx >= idy:
            #         edge_weights.append([types[idx], types[idy], weight])
            # elif mode == "defense":
            #     if idx <= idy:
            #         edge_weights.append([types[idx], types[idy], weight])

            elif mode == "inverse":
                if weight == 2:
                    edge_weights.append([types[idx], types[idy], 0.5])
                elif weight == 0.5:
                    edge_weights.append([types[idx], types[idy], 2])
                elif weight == 1:
                    edge_weights.append([types[idx], types[idy], 1])
                elif weight == 0:
                    edge_weights.append([types[idx], types[idy], 2])
            else:
                assert mode == 'regular'
                edge_weights.append([types[idx], types[idy], weight])
    return edge_weights


def get_pagerank_results(mode, ignore=None):
    edges_weights = get_type_edges(mode, ignore)
    # 创建一个有向图
    graph = nx.DiGraph()
    # 设置有向图中的路径及权重(from, to, weight)
    graph.add_weighted_edges_from(edges_weights)
    # 计算每个节点（人）的PR值，并作为节点的pagerank属性
    pagerank = nx.pagerank(graph)
    # 获取每个节点的pagerank数值
    pagerank_list = {node: rank for node, rank in pagerank.items()}
    return graph, pagerank_list


if __name__ == "__main__":
    mode = 'regular'
    # mode = 'attack'
    # mode = 'defense'
    # mode = 'inverse'
    
    if mode in ['attack', 'defense']:
        pagerank_list = {}
        for i in range(18):
            _, tmp_pagerank_list = get_pagerank_results(mode, ignore=i)
            pagerank_list[types[i]] = tmp_pagerank_list[types[i]]
            # print(tmp_pagerank_list)
        print("MODE:", mode)
        pprint(sorted([(k,round(v,4)) for k,v in pagerank_list.items()], key=lambda x: (-x[1] if mode == 'attack' else x[1])))

    else:
        graph, pagerank_list = get_pagerank_results(mode)
        print("MODE:", mode)
        pprint(sorted([(k,round(v,4)) for k,v in pagerank_list.items()], key=lambda x: x[1]))

        # 将pagerank数值作为节点的属性
        nx.set_node_attributes(graph, name = 'pagerank', values=pagerank_list)
        # 画网络图
        show_graph(graph)

    # # 将完整的图谱进行精简
    # # 设置PR值的阈值，筛选大于阈值的重要核心节点
    # pagerank_threshold = 0.005
    # # 复制一份计算好的网络图
    # small_graph = graph.copy()
    # # 剪掉PR值小于pagerank_threshold的节点
    # for n, p_rank in graph.nodes(data=True):
    #     if p_rank['pagerank'] < pagerank_threshold: 
    #         small_graph.remove_node(n)
    # # 画网络图
    # show_graph(small_graph)