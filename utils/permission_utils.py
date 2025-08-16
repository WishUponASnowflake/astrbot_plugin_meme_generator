"""权限检查工具模块"""

from astrbot.core.platform import AstrMessageEvent


class PermissionUtils:
    """权限检查工具类"""

    @staticmethod
    def is_bot_admin(event: AstrMessageEvent) -> bool:
        """
        检查用户是否为Bot管理员

        Args:
            event: 消息事件

        Returns:
            是否为Bot管理员
        """
        try:
            # 检查是否为超级用户（AstrBot框架的管理员检查）
            if hasattr(event, 'is_admin') and callable(event.is_admin):
                return event.is_admin()

            # 如果框架没有提供is_admin方法，尝试其他方式
            # 可以通过配置文件中的管理员列表来检查
            # 这里可以添加更多的Bot管理员检查逻辑

            return False

        except Exception:
            # 权限检查出错时，为了安全起见返回False
            return False
    
    @staticmethod
    def get_permission_denied_message() -> str:
        """
        获取权限不足的提示消息

        Returns:
            权限不足提示
        """
        return "❌ 权限不足，此命令仅限Bot管理员使用"
    
    @staticmethod
    def get_plugin_disabled_message() -> str:
        """
        获取插件已禁用的提示消息
        
        Returns:
            插件禁用提示
        """
        return "🔒 表情包生成功能已被管理员禁用"
