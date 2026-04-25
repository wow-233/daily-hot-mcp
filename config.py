import os
import datetime
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置类"""
    
    # OpenAI 兼容 API 配置
    API_KEY = os.getenv('API_KEY', '')
    BASE_URL = os.getenv('BASE_URL', 'https://api.deepseek.com')  # 默认 DeepSeek
    MODEL = os.getenv('MODEL', 'deepseek-chat')
    
    # 兼容旧配置（DeepSeek）
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '') or API_KEY
    DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL', '') or BASE_URL
    
    # 代理配置
    PROXY = os.getenv('PROXY', '')  # 例如: 127.0.0.1:1080
    
    # 输出路径配置 - 默认当前目录下的 output 文件夹
    OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    OBSIDIAN_PATH = OUTPUT_DIR
    
    @classmethod
    def get_proxy_dict(cls):
        """获取代理配置字典"""
        if cls.PROXY:
            return {
                'http': f'http://{cls.PROXY}',
                'https': f'http://{cls.PROXY}'
            }
        return None
    
    @classmethod
    def get_verify_ssl(cls):
        """是否验证SSL证书"""
        return os.getenv('VERIFY_SSL', 'false').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """验证配置"""
        # 确保输出目录存在
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        
        return True

