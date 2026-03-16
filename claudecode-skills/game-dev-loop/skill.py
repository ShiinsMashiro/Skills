#!/usr/bin/env python3
"""
Game Dev Loop - 自动化游戏开发循环

当游戏开发到终极状态后，自动深度研究同类游戏，生成新版本迭代。
"""

import json
import os
from datetime import datetime
from pathlib import Path

# 状态文件路径
STATE_FILE = Path.home() / ".claude" / "projects" / "-Users-huangpaopao" / "memory" / "game_dev_loop.json"

# 项目路径
PROJECT_PATH = Path.home() / "Documents" / "Revolution" / "project"

class GameDevLoop:
    def __init__(self):
        self.state = self._load_state()
        self.current_version = self.state.get("current_version", "V5")
        self.loop_count = self.state.get("loop_count", 0)
        self.status = self.state.get("status", "idle")

    def _load_state(self) -> dict:
        """加载状态"""
        if STATE_FILE.exists():
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        return {
            "current_version": "V5",
            "loop_count": 0,
            "research_count": 0,
            "status": "idle",
            "last_update": datetime.now().strftime("%Y-%m-%d"),
            "milestones": {}
        }

    def _save_state(self):
        """保存状态"""
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)

    def start_loop(self):
        """启动循环"""
        self.state["status"] = "running"
        self._save_state()
        return "🚀 游戏开发循环已启动！\n" + self.get_status()

    def stop_loop(self):
        """停止循环"""
        self.state["status"] = "stopped"
        self._save_state()
        return "⏹️ 游戏开发循环已停止"

    def get_status(self) -> str:
        """获取当前状态"""
        return f"""📊 游戏开发循环状态

当前版本: {self.current_version}
循环次数: {self.loop_count}
研究次数: {self.state.get('research_count', 0)}
状态: {self.state['status']}

里程碑:
{self._format_milestones()}"""

    def _format_milestones(self) -> str:
        """格式化里程碑"""
        milestones = self.state.get("milestones", {})
        if not milestones:
            return "无记录"
        lines = []
        for v, info in milestones.items():
            features = ", ".join(info.get("features", []))
            lines.append(f"  {v}: {features}")
        return "\n".join(lines)

    def check_project_state(self) -> dict:
        """检查项目状态"""
        # 检查核心文件是否存在
        checks = {
            "main_scene": (PROJECT_PATH / "scenes" / "main" / "main.gd").exists(),
            "game_manager": (PROJECT_PATH / "scripts" / "core" / "game.gd").exists(),
            "unit_system": (PROJECT_PATH / "scripts" / "core" / "unit_manager.gd").exists(),
            "combat_system": (PROJECT_PATH / "scripts" / "core" / "combat.gd").exists(),
            "economy_system": (PROJECT_PATH / "scripts" / "core" / "economy.gd").exists(),
            "diplomacy_system": (PROJECT_PATH / "scripts" / "core" / "diplomacy.gd").exists(),
            "ai_system": (PROJECT_PATH / "scripts" / "core" / "ai_player.gd").exists(),
            "tech_system": (PROJECT_PATH / "scripts" / "core" / "tech.gd").exists(),
        }

        # 检查已完成的任务
        completed_count = sum(1 for v in checks.values() if v)

        return {
            "checks": checks,
            "completed": completed_count,
            "total": len(checks),
            "is_ultimate": completed_count >= len(checks)
        }

    def increment_loop(self):
        """增加循环计数"""
        self.state["loop_count"] = self.state.get("loop_count", 0) + 1
        self.state["last_update"] = datetime.now().strftime("%Y-%m-%d")
        self._save_state()

    def get_current_version_number(self) -> int:
        """获取当前版本号"""
        v = self.current_version.replace("V", "")
        try:
            return int(v)
        except:
            return 5

def main():
    loop = GameDevLoop()

    import sys
    if len(sys.argv) < 2:
        print(loop.get_status())
        sys.exit(0)

    command = sys.argv[1]

    if command == "start":
        print(loop.start_loop())
    elif command == "stop":
        print(loop.stop_loop())
    elif command == "status":
        print(loop.get_status())
    elif command == "check":
        result = loop.check_project_state()
        print(f"项目检查: {result['completed']}/{result['total']} 系统完成")
        print(f"终极状态: {'是' if result['is_ultimate'] else '否'}")
        for name, exists in result["checks"].items():
            status = "✅" if exists else "❌"
            print(f"  {status} {name}")
    elif command == "next":
        loop.increment_loop()
        print(f"循环次数: {loop.loop_count}")
    else:
        print("未知命令")
        sys.exit(1)

if __name__ == "__main__":
    main()
