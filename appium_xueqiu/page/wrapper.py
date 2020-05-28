from functools import wraps
from selenium.webdriver.common.by import By


#
# def handle_black(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         _black_list = [
#             (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
#             (By.XPATH, "//*[@text='确认']"),
#             (By.XPATH, "//*[@text='下次再说']"),
#             (By.XPATH, "//*[@text='确定']")
# 
#         ]
#         _max_num = 3
#         _error_num = 0
#         instance= args[0]
#         try:
#             element = func(*args, **kwargs)
#             _error_num = 0
#             # 隐式等待回复原来的等待，
#             return element
#         except Exception as e:
#             # 判断异常处理次数
#             if _error_num > _max_num:
#                 raise e
#             _error_num += 1
#             instance._driver.implicitly_wait(0)
#             # 处理黑名单里面的弹框
#             for ele in _black_list:
#                 elelist = instance.finds(*ele)
#                 if len(elelist) > 0:
#                     elelist[0].click()
#                     instance._driver.implicitly_wait(3)
#                     # 处理完弹框，再将去查找目标元素
#                     return wrapper(*args, **kwargs)
#             raise e
# 
#     return wrapper


def handle_black(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']")

        ]
        _max_num = 3
        _error_num = 0
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            return element
        except Exception as e:
            from appium_xueqiu.page.base_page import BasePage
            instance: BasePage = args[0]
            # 出现异常， 将隐式等待设置小一点，快速的处理弹框
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return wrapper(*args, **kwargs)

            raise e
    return wrapper
