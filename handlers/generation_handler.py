"""表情包生成命令处理器"""

from astrbot.core.platform import AstrMessageEvent
import astrbot.core.message.components as Comp
from astrbot import logger
from ..core import MemeManager


class GenerationHandler:
    """表情包生成命令处理器"""
    
    def __init__(self, meme_manager: MemeManager):
        self.meme_manager = meme_manager
    
    async def handle_generate_meme(self, event: AstrMessageEvent):
        """
        处理表情包生成请求

        Args:
            event: 消息事件
        """
        try:
            image = await self.meme_manager.generate_meme(event)
            if image:
                # 记录成功生成的日志
                user_id = event.get_sender_id()
                message_str = event.get_message_str()
                logger.info(f"表情包生成成功 - 用户: {user_id}, 消息: {message_str[:50]}{'...' if len(message_str) > 50 else ''}")

                chain = [Comp.Image.fromBytes(image)]
                yield event.chain_result(chain)
        except Exception as e:
            # 记录生成失败的日志
            user_id = event.get_sender_id()
            message_str = event.get_message_str()
            logger.error(f"表情包生成异常 - 用户: {user_id}, 消息: {message_str[:50]}{'...' if len(message_str) > 50 else ''}, 错误: {e}")
            pass  # 静默失败，不响应用户
