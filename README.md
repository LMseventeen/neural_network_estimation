# 神经网络系统状态估计

本项目实现了一个带有混合时滞的神经网络系统的状态估计方案，包含事件触发机制。

# 在pycharm打开项目 neural_network_estimation
# 打开终端，运行以下指令

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行仿真

```bash
python -m simulation.main
```

## 项目结构

- src/: 源代码目录
  - system.py: 系统模型和参数
  - nonlinear.py: 非线性函数
  - estimator.py: 状态估计器
  - event_trigger.py: 事件触发机制
- simulation/: 仿真程序
- visualization/: 可视化函数

## 功能特点

1. 混合时滞处理
2. 事件触发机制
3. 状态估计
4. 性能分析
5. 可视化展示

## 性能分析

系统会生成以下性能图：
1. 系统状态和估计值对比图
2. 估计误差图
3. 事件触发时刻图
4. 性能指标统计图
![bfe2d67a3342aef4cdce491422712de](https://github.com/user-attachments/assets/fabb05e0-33a8-4f43-8122-340b1c8fc9d2)
![926bb828d1c34c5a564ca01cf9277d1](https://github.com/user-attachments/assets/e89385bd-6fae-4a23-a6db-b06a61e87b67)
![1fd62a42593740087cbc707078d1eff](https://github.com/user-attachments/assets/54088515-4c7c-4d90-859c-b679830e38bc)
![5e13615428dc5bdcc9410bac4eae653](https://github.com/user-attachments/assets/fb8d81f5-d491-4af9-ab11-5e791aff313b)


