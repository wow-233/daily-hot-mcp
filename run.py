#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub Trending 工具启动脚本
"""

import os
import sys
import subprocess
from datetime import datetime

def print_menu():
    """打印菜单"""
    print("=" * 50)
    print("🚀 GitHub 每日趋势工具")
    print("=" * 50)
    print("1. 执行一次抓取任务")
    print("2. 启动定时任务")
    print("3. 构建网站")
    print("4. 启动开发服务器")
    print("5. 部署到GitHub Pages")
    print("6. 查看帮助")
    print("0. 退出")
    print("=" * 50)

def run_command(command, description):
    """运行命令"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"✅ {description}完成！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description}失败: {e}")
        return False
    except KeyboardInterrupt:
        print(f"⏹️ {description}被用户中断")
        return False

def main():
    """主函数"""
    while True:
        print_menu()
        
        try:
            choice = input("\n请选择操作 (0-6): ").strip()
            
            if choice == "0":
                print("👋 再见！")
                break
            elif choice == "1":
                run_command("python main.py", "执行抓取任务")
            elif choice == "2":
                print("⏰ 启动定时任务（按Ctrl+C停止）...")
                run_command("python scheduler.py", "定时任务")
            elif choice == "3":
                run_command("python build_site.py build", "构建网站")
            elif choice == "4":
                print("🌐 启动开发服务器（按Ctrl+C停止）...")
                run_command("python build_site.py serve", "开发服务器")
            elif choice == "5":
                run_command("python build_site.py deploy", "部署到GitHub Pages")
            elif choice == "76":
                print_help()
            else:
                print("❌ 无效选择，请重新输入")
                
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

def print_help():
    """打印帮助信息"""
    print("\n" + "=" * 50)
    print("📖 帮助信息")
    print("=" * 50)
    print("1. 执行一次抓取任务 - 手动运行GitHub Trending抓取")
    print("2. 启动定时任务 - 启动定时调度器，每日自动执行")
    print("3. 构建网站 - 使用MkDocs构建静态网站")
    print("4. 启动开发服务器 - 启动本地开发服务器预览网站")
    print("5. 部署到GitHub Pages - 部署网站到GitHub Pages")
    print("6. 查看帮助 - 显示此帮助信息")
    print("0. 退出 - 退出程序")
    print("\n💡 提示:")
    print("- 首次使用前请确保已配置.env文件")
    print("- 需要DeepSeek API密钥才能使用翻译功能")
    print("- 部署到GitHub Pages需要Git仓库权限")
    print("=" * 50)

if __name__ == "__main__":
    main()
