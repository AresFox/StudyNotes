
# for x in range(10):
#     cmds.polyCube()
#     cmds.move(x*2, 0, 0)
#
#
# cmds.polyClean()
# cmds.polyCube()

# 实现一个分形，一个三角形，分为四个小三角形，每个小三角形又分为四个小三角形，如此递归
# 1. 画一个三角形
# 2. 画一个三角形的中心点
# 3. 画三个小三角形
# 4. 递归
# 代码：

# ------------------- 代码实现 ------------------- 可以生成一堆三角形
# from maya import cmds
#
# cmds.file(new=True, force=True)
# def draw_triangle(points, name):
#     """根据给定的三角形顶点绘制三角形"""
#     cmds.polyCreateFacet(p=points, n=name)
#
# def mid_point(p1, p2):
#     """计算两个点的中点"""
#     return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2]
#
# def create_fractal_triangle(p1, p2, p3, depth):
#     """递归创建分形三角形"""
#     if depth == 0:
#         return
#
#     # 绘制当前三角形
#     draw_triangle([p1, p2, p3], f"FractalTriangle_depth{depth}")
#
#     # 计算中点
#     m1 = mid_point(p1, p2)
#     m2 = mid_point(p2, p3)
#     m3 = mid_point(p3, p1)
#
#     # 递归绘制三个小三角形
#     create_fractal_triangle(p1, m1, m3, depth - 1)  # 左侧小三角形
#     create_fractal_triangle(m1, p2, m2, depth - 1)  # 中间小三角形
#     create_fractal_triangle(m3, m2, p3, depth - 1)  # 右侧小三角形
#
# # 设置三角形的顶点
# point1 = [0, 0, 0]
# point2 = [1, 0, 0]
# point3 = [0.5, 0.866, 0]  # 高度为 sqrt(3)/2 的等边三角形
#
# # 设置递归深度
# depth = 6
#
# # 创建分形三角形
# create_fractal_triangle(point1, point2, point3, depth)
#


# ------------------- 代码实现 -------------------
# from maya import cmds
#
# # 清空场景
# cmds.file(new=True, force=True)
#
# def draw_triangle(points, name):
#     """根据给定的三角形顶点绘制三角形"""
#     cmds.polyCreateFacet(p=points, n=name)
#
#
# def mid_point(p1, p2):
#     """计算两个点的中点"""
#     return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2]
#
#
# def create_fractal_triangle(p1, p2, p3, depth):
#     """递归创建分形三角形"""
#     if depth == 0:
#         return
#
#     # 计算三角形的中点
#     m1 = mid_point(p1, p2)
#     m2 = mid_point(p2, p3)
#     m3 = mid_point(p3, p1)
#
#     # 绘制当前三角形的边界
#     draw_triangle([p1, p2, p3], f"FractalTriangle_depth{depth}")
#
#     # 递归绘制三个小三角形
#     create_fractal_triangle(p1, m1, m3, depth - 1)  # 左侧小三角形
#     create_fractal_triangle(m1, p2, m2, depth - 1)  # 中间小三角形
#     create_fractal_triangle(m3, m2, p3, depth - 1)  # 右侧小三角形
#
#
# # 设置初始三角形的顶点
# point1 = [0, 0, 0]
# point2 = [1, 0, 0]
# point3 = [0.5, (3 ** 0.5) / 2, 0]  # 高度为 sqrt(3)/2 的等边三角形
#
# # 设置递归深度
# depth = 4  # 你可以调整这个值来改变分形的复杂度
#
# # 创建分形三角形
# create_fractal_triangle(point1, point2, point3, depth)


#  ------------------- 代码实现 -------------------  错的
# from maya import cmds
#
# # 清空场景
# cmds.file(new=True, force=True)
# def draw_single_fractal_triangle(p1, p2, p3, depth):
#     """递归绘制一个完整的分形三角形"""
#     if depth == 0:
#         # 当达到深度时，绘制三角形
#         cmds.polyCreateFacet(p=[p1, p2, p3], n=f"FractalTriangle_depth_{depth}")
#         return
#
#     # 计算三角形的中点
#     m1 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2]
#     m2 = [(p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2, (p2[2] + p3[2]) / 2]
#     m3 = [(p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2, (p3[2] + p1[2]) / 2]
#
#     # 在中间位置添加一个新顶点，使得形成一个向上突出的三角形
#     peak = [
#         (m1[0] + m2[0]) / 2,
#         (m1[1] + m2[1]) / 2 + ((3 ** 0.5) / 4 * ((p1[1] - p3[1]) ** 2 + (p1[0] - p3[0]) ** 2) ** 0.5),
#         (m1[2] + m2[2]) / 2
#     ]
#
#     # 递归绘制新的小三角形
#     draw_single_fractal_triangle(p1, m1, peak, depth - 1)
#     draw_single_fractal_triangle(m1, p2, peak, depth - 1)
#     draw_single_fractal_triangle(p2, m2, peak, depth - 1)
#     draw_single_fractal_triangle(m2, p3, peak, depth - 1)
#     draw_single_fractal_triangle(p3, m3, peak, depth - 1)
#     draw_single_fractal_triangle(m3, p1, peak, depth - 1)
#
#
# # 设置初始三角形的顶点
# point1 = [0, 0, 0]
# point2 = [1, 0, 0]
# point3 = [0.5, (3 ** 0.5) / 2, 0]  # 高度为 sqrt(3)/2 的等边三角形
#
# # 设置递归深度
# depth = 4  # 可以根据需要调整这个值
#
# # 创建分形三角形
# draw_single_fractal_triangle(point1, point2, point3, depth)


# ------------------- 代码实现 -------------------
# import maya.cmds as cmds
# from maya import cmds
# import math
# def create_koch_snowflake(iterations, size):
#     # 创建基础三角形的三个顶点
#     p1 = [0, 0, 0]
#     p2 = [size, 0, 0]
#     p3 = [size / 2, size * (math.sqrt(3) / 2), 0]
#
#     # 创建多边形
#     base_triangle = cmds.polyCreateFacet(p=[p1, p2, p3])[0]
#
#     # 进行科赫细分
#     for _ in range(iterations):
#         edges = cmds.polyListComponentConversion(base_triangle, toEdge=True)
#         edges = cmds.filterExpand(edges, selectionMask=32)
#
#         new_edges = []
#         for edge in edges:
#             # 获取当前边的端点
#             verts = cmds.polyEdgeVertices(edge)
#             v1 = cmds.xform(verts[0], query=True, translation=True, worldSpace=True)
#             v2 = cmds.xform(verts[1], query=True, translation=True, worldSpace=True)
#
#             # 计算中间点和压缩三角形的顶点
#             mid1 = [(v1[0] + v2[0]) / 3, (v1[1] + v2[1]) / 3, (v1[2] + v2[2]) / 3]
#             mid2 = [(v1[0] + v2[0]) * 2 / 3, (v1[1] + v2[1]) * 2 / 3, (v1[2] + v2[2]) * 2 / 3]
#             peak = [(mid1[0] + mid2[0]) / 2, (mid1[1] + mid2[1]) + ((math.sqrt(3) / 6) * size), (mid1[2] + mid2[2]) / 2]
#
#             # 创建新三角形
#             new_faces = cmds.polyCreateFacet(p=[v1, mid1, peak])[0]
#             new_faces = cmds.polyCreateFacet(p=[mid1, mid2, peak])[0]
#             new_faces = cmds.polyCreateFacet(p=[v2, mid2, peak])[0]
#
#             new_edges.append(new_faces)
#
#         # 合并所有新面
#         base_triangle = cmds.polyUnite(new_edges, ch=False)[0]
#         cmds.polyMergeVertex(base_triangle, distance=0.001)
#
#     # 删除历史记录
#     cmds.delete(base_triangle, constructionHistory=True)
#
# # 使用函数并指定迭代次数和大小
# create_koch_snowflake(iterations=4, size=5)


# ------------------- 代码实现 -------------------  不报错了 但是是错误的
# import maya.cmds as cmds
# import math
#
# def create_koch_snowflake(iterations, size):
#     # 创建基础三角形的三个顶点
#     p1 = [0, 0, 0]
#     p2 = [size, 0, 0]
#     p3 = [size / 2, size * (math.sqrt(3) / 2), 0]
#
#     # 创建初始三角形
#     base_triangle = cmds.polyCreateFacet(p=[p1, p2, p3])[0]
#
#     for _ in range(iterations):
#         edges = cmds.polyListComponentConversion(base_triangle, toEdge=True)
#         edges = cmds.filterExpand(edges, selectionMask=32)
#
#         new_faces = []
#
#         for edge in edges:
#             # 转换为顶点并获取顶点索引
#             vertices = cmds.polyListComponentConversion(edge, toVertex=True)
#             vertex_indices = cmds.filterExpand(vertices, selectionMask=31)
#
#             if len(vertex_indices) < 2:
#                 continue  # 如果没有找到两个顶点，跳过该边
#
#             # 获取顶点的位置
#             v1_index = int(vertex_indices[0].split('[')[-1].split(']')[0]) # 提取索引
#             v2_index = int(vertex_indices[1].split('[')[-1].split(']')[0]) # 提取索引
#
#             v1 = cmds.xform(f"{base_triangle}.vtx[{v1_index}]", query=True, translation=True, worldSpace=True)
#             v2 = cmds.xform(f"{base_triangle}.vtx[{v2_index}]", query=True, translation=True, worldSpace=True)
#
#             # 计算中间点和向外的顶点
#             mid1 = [(v1[0] + v2[0]) / 3, (v1[1] + v2[1]) / 3, (v1[2] + v2[2]) / 3]
#             mid2 = [(v1[0] + v2[0]) * 2 / 3, (v1[1] + v2[1]) * 2 / 3, (v1[2] + v2[2]) * 2 / 3]
#             peak = [(mid1[0] + mid2[0]) / 2, mid1[1] + (math.sqrt(3) * size / 6), (mid1[2] + mid2[2]) / 2]
#
#             # 创建新面
#             new_faces.append(cmds.polyCreateFacet(p=[v1, mid1, peak])[0])
#             new_faces.append(cmds.polyCreateFacet(p=[mid1, mid2, peak])[0])
#             new_faces.append(cmds.polyCreateFacet(p=[v2, mid2, peak])[0])
#
#         # 合并所有新面
#         base_triangle = cmds.polyUnite(new_faces, ch=False)[0]
#         cmds.polyMergeVertex(base_triangle, distance=0.001)
#
#     # 删除历史记录
#     cmds.delete(base_triangle, constructionHistory=True)
#
# # 使用函数并指定迭代次数和大小
# create_koch_snowflake(iterations=2, size=5)
#

# # ------------------- 代码实现 -------------------
# import maya.cmds as cmds  # 导入Maya命令模块
# import math  # 导入数学模块
#
# # 定义常量
# SNOW_LEVELS_COUNT = 0  # 可以根据需要更改此值，分形的层数
# YD_SNOW_RADIUS = 5.0  # 雪花的半径
#
# def Zhe(vStart, vEnd):
#     # 定义函数Zhe，用于生成分形的边
#     vSub = [vEnd[i] - vStart[i] for i in range(3)]  # 计算起始点和结束点之间的向量差
#
#     # 计算三个新点
#     p1 = vStart  # 起始点
#     p2 = [vStart[i] + vSub[i] / 3 for i in range(3)]  # 第一个新点为起始点向前移动1/3
#     p3 = [0, 0, 0]  # 占位符，用于后面的峰顶
#     p4 = [vStart[i] + vSub[i] * 2 / 3 for i in range(3)]  # 第二个新点为起始点向前移动2/3
#     p5 = vEnd  # 结束点
#
#     # 计算峰顶的角度和位置
#     alpha = math.atan2(vSub[1], vSub[0]) + math.pi / 3  # 计算峰顶的角度
#     l = math.sqrt(sum((v ** 2 for v in vSub))) / 3  # 计算线段的长度并除以3
#     p3[0] = p2[0] + math.cos(alpha) * l  # 根据角度和长度计算峰顶的X坐标
#     p3[1] = p2[1] + math.sin(alpha) * l  # 根据角度和长度计算峰顶的Y坐标
#     p3[2] = 0.0  # Z坐标设为0
#
#     return [p1, p2, p3, p4, p5]  # 返回新的五个点
#
# def Fractal(vertices, level):
#     # 定义递归函数生成分形
#     if level == 0:
#         # 基本情况：仅添加原始线段
#         return vertices
#
#     # 获取当前顶点
#     current_vertices = []  # 存储当前顶点列表
#
#     # 处理每一对顶点
#     for i in range(len(vertices) - 1):  # 遍历所有顶点对
#         start = vertices[i]  # 当前起始点
#         end = vertices[i + 1]  # 当前结束点
#
#         # 从起始点到结束点生成段
#         segments = Zhe(start, end)  # 调用Zhe函数生成新段
#         current_vertices.extend(segments[:-1])  # 将生成的段添加到当前顶点列表中，不添加最后一个点以避免重复
#
#     current_vertices.append(vertices[-1])  # 添加最后一个顶点
#
#     # 递归到下一个层级
#     return Fractal(current_vertices, level - 1)  # 继续递归调用
#
# def create_koch_snowflake():
#     # 定义初始三角形的顶点
#     p1 = [0.0, YD_SNOW_RADIUS, 0.0]  # 顶点1
#     p2 = [YD_SNOW_RADIUS * math.sin(math.pi / 3), -YD_SNOW_RADIUS * math.sin(math.pi / 6), 0.0]  # 顶点2
#     p3 = [-p2[0], p2[1], 0.0]  # 顶点3（对称）
#
#     # 开始使用三角形的顶点
#     vertices = [p1, p2, p3, p1]  # 闭合三角形
#
#     # 使用分形函数生成顶点
#     vertices = Fractal(vertices, SNOW_LEVELS_COUNT)  # 生成分形顶点
#
#     # 在Maya中创建多边形网格
#     if vertices:  # 如果存在顶点
#         cmds.polyCreateFacet(p=vertices)  # 创建多边形面
#
# # 执行函数以创建科赫雪花
# create_koch_snowflake()  # 调用创建雪花的函数


# ------------------- 代码实现 -------------------
# from maya import cmds  # 导入 Maya 命令模块
# import math  # 导入数学模块以便进行三角函数计算
# cmds.file(new=True, force=True)
#
# def draw_line(start_pos, end_pos):
#     """在起始位置和结束位置之间绘制一条线。"""
#     # 确保使用适合 Maya 的格式（3D 点）
#     cmds.curve(d=1, p=[(start_pos[0], start_pos[1], 0), (end_pos[0], end_pos[1], 0)])
#
#
# def apply_rules(axiom, iterations):
#     """根据指定迭代次数应用 L 系统规则。"""
#     rules = {'A': 'B-A-B', 'B': 'A+B+A'}  # 定义替换规则
#     result = axiom  # 初始化结果为公理
#
#     for _ in range(iterations):  # 循环迭代次数
#         # 根据规则生成下一个结果字符串
#         next_result = ''.join(rules.get(char, char) for char in result)
#         result = next_result  # 更新结果为新的字符串
#
#     return result  # 返回最终生成的字符串
#
#
# def sierpinski_arrowhead_curve(axiom, order, length):
#     """使用生成的字符串绘制谢尔宾斯基箭头曲线。"""
#     instructions = apply_rules(axiom, order)  # 应用 L 系统规则生成指令字符串
#
#     # 初始位置和角度
#     pos = (0, 0)  # 起始位置
#     angle = 0  # 初始角度为 0
#
#     # 根据指令绘制曲线
#     stack = []  # 用于存储状态的栈（未使用）
#
#     for command in instructions:  # 遍历指令字符串中的每个命令
#         if command == 'A' or command == 'B':  # 如果命令为 A 或 B
#             # 基于当前的位置和角度计算终点
#             end_x = pos[0] + length * math.cos(math.radians(angle))  # 计算 X 坐标
#             end_y = pos[1] + length * math.sin(math.radians(angle))  # 计算 Y 坐标
#             draw_line(pos, (end_x, end_y))  # 绘制从当前位置到终点的线段
#             pos = (end_x, end_y)  # 更新当前位置为终点
#         elif command == '+':  # 如果命令为 '+'
#             angle += 60  # 向右转 60 度
#         elif command == '-':  # 如果命令为 '-'
#             angle -= 60  # 向左转 60 度
#
#
# # 初始化变量
# depth = 7  # 设置递归深度
# length = 10  # 设置初始长度
# axiom = 'A'  # 起始公理
#
# # 开始绘制谢尔宾斯基箭头曲线
# sierpinski_arrowhead_curve(axiom, depth, length)



# ------------------- 代码实现 -------------------雪花
# ------------------- 代码实现 -------------------
import maya.cmds as cmds  # 导入Maya命令模块
import math  # 导入数学模块
cmds.file(new=True, force=True)
# 定义常量
SNOW_LEVELS_COUNT = 5  # 可以根据需要更改此值，分形的层数
YD_SNOW_RADIUS = 5.0  # 雪花的半径

def Zhe(vStart, vEnd):
    # 定义函数Zhe，用于生成分形的边
    vSub = [vEnd[i] - vStart[i] for i in range(3)]  # 计算起始点和结束点之间的向量差

    # 计算三个新点
    p1 = vStart  # 起始点
    p2 = [vStart[i] + vSub[i] / 3 for i in range(3)]  # 第一个新点为起始点向前移动1/3
    p3 = [0, 0, 0]  # 占位符，用于后面的峰顶
    p4 = [vStart[i] + vSub[i] * 2 / 3 for i in range(3)]  # 第二个新点为起始点向前移动2/3
    p5 = vEnd  # 结束点

    # 计算峰顶的角度和位置
    alpha = math.atan2(vSub[1], vSub[0]) + math.pi / 3  # 计算峰顶的角度
    l = math.sqrt(sum((v ** 2 for v in vSub))) / 3  # 计算线段的长度并除以3
    p3[0] = p2[0] + math.cos(alpha) * l  # 根据角度和长度计算峰顶的X坐标
    p3[1] = p2[1] + math.sin(alpha) * l  # 根据角度和长度计算峰顶的Y坐标
    p3[2] = 0.0  # Z坐标设为0

    return [p1, p2, p3, p4, p5]  # 返回新的五个点

def Fractal(vertices, level):
    # 定义递归函数生成分形
    if level == 0:
        # 基本情况：仅添加原始线段
        return vertices

    # 获取当前顶点
    current_vertices = []  # 存储当前顶点列表

    # 处理每一对顶点
    for i in range(len(vertices) - 1):  # 遍历所有顶点对
        start = vertices[i]  # 当前起始点
        end = vertices[i + 1]  # 当前结束点

        # 从起始点到结束点生成段
        segments = Zhe(start, end)  # 调用Zhe函数生成新段
        current_vertices.extend(segments[:-1])  # 将生成的段添加到当前顶点列表中，不添加最后一个点以避免重复

    current_vertices.append(vertices[-1])  # 添加最后一个顶点

    # 递归到下一个层级
    return Fractal(current_vertices, level - 1)  # 继续递归调用

def create_koch_snowflake():
    # 定义初始三角形的顶点
    p1 = [0.0, YD_SNOW_RADIUS, 0.0]  # 顶点1
    p2 = [YD_SNOW_RADIUS * math.sin(math.pi / 3), -YD_SNOW_RADIUS * math.sin(math.pi / 6), 0.0]  # 顶点2
    p3 = [-p2[0], p2[1], 0.0]  # 顶点3（对称）

    # 开始使用三角形的顶点
    vertices = [p1, p2, p3, p1]  # 闭合三角形

    # 使用分形函数生成顶点
    vertices = Fractal(vertices, SNOW_LEVELS_COUNT)  # 生成分形顶点

    # 在Maya中创建多边形网格
    if vertices:  # 如果存在顶点
        cmds.polyCreateFacet(p=vertices)  # 创建多边形面

# 执行函数以创建科赫雪花
create_koch_snowflake()  # 调用创建雪花的函数
