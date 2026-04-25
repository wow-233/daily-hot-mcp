"""
中国热门新闻抓取器 - 36氪、知乎、微博等
"""
import requests
import logging
from typing import List, Dict
from config import Config

logger = logging.getLogger(__name__)

class ChineseHotNewsScraper:
    """中国热门新闻抓取器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        })
        # 应用代理
        proxy = Config.get_proxy_dict()
        if proxy:
            self.session.proxies.update(proxy)
            logger.info(f"已启用代理: {proxy}")
    
    def get_hot_news(self, sources: List[int] = None) -> List[Dict]:
        """
        获取热门新闻
        
        Args:
            sources: 平台ID列表
                1: 知乎
                2: 36氪
                3: 百度
                4: B站
                5: 微博
                6: 抖音
                7: 虎扑
                8: 豆瓣
                9: IT之家
        
        Returns:
            新闻列表
        """
        if sources is None:
            sources = [2, 1, 5]  # 默认: 36氪, 知乎, 微博
        
        all_news = []
        
        for source_id in sources:
            try:
                news = self._fetch_by_id(source_id)
                all_news.extend(news)
            except Exception as e:
                logger.error(f"抓取平台 {source_id} 失败: {e}")
        
        return all_news
    
    def _fetch_by_id(self, source_id: int) -> List[Dict]:
        """根据ID抓取"""
        # 使用 vvhan API 获取热点
        url = f"https://api.vvhan.com/api/hotlist?cid={source_id}"
        
        try:
            response = self.session.get(url, timeout=30, verify=Config.get_verify_ssl())
            response.raise_for_status()
            data = response.json()
            
            if data.get('success'):
                items = data.get('data', [])
                return self._parse_items(source_id, items)
            return []
        except Exception as e:
            logger.error(f"API请求失败: {e}")
            return []
    
    def _parse_items(self, source_id: int, items: List) -> List[Dict]:
        """解析数据"""
        source_name = {
            1: "知乎", 2: "36氪", 3: "百度", 4: "B站",
            5: "微博", 6: "抖音", 7: "虎扑", 8: "豆瓣", 9: "IT之家"
        }.get(source_id, "未知")
        
        news_list = []
        for item in items[:10]:  # 取前10条
            news_list.append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'hot': item.get('hot', ''),
                'source': source_name,
                'type': 'chinese'
            })
        
        return news_list