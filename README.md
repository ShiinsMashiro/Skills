# Skills

Claude Code 技能集合。

## 目录结构

```
Skills/
├── core-skills/           # 核心技能
│   ├── skill-manager/     # 技能调度器
│   ├── skill-tracker/     # 技能追踪器
│   ├── nopua/            # 常驻技能
│   ├── main-controller/   # 中央控制器
│   ├── skill-loader/      # 技能加载器
│   └── skill-flow-tree/   # 技能流程树
│
├── workflow-skills/       # 工作流技能
│   ├── auto-pilot/        # 自动驾驶
│   ├── parallel-worker/   # 并行任务处理器
│   ├── async-runner/      # 异步执行器
│   └── project-planner/   # 项目规划器
│
├── app-skills/           # 应用技能
│   └── disc-generator/    # 讨论课生成器
│
└── project-integrations/ # 项目集成
    └── obsidian-vision/  # Obsidian集成
```

## 核心技能

### skill-manager
技能调度器，遵循 s02 原理，动态 dispatch 技能。

### skill-tracker
技能调用追踪器，实时显示技能调用链。

### nopua
常驻技能，每次交互都用爱与尊重。

## 使用方法

在 Claude Code 中使用 `/skill-name` 调用技能。

## 许可证

MIT
