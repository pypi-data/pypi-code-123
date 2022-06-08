from sqlite3 import paramstyle
from typing import List
import httpx
import traceback
import jinja2
import re
from pathlib import Path
from .data_source import servers,set_infoparams
from .utils import match_keywords
from .publicAPI import get_AccountIdByName
from nonebot_plugin_htmlrender import html_to_pic
from nonebot import get_driver
from nonebot.log import logger
from httpx import ConnectTimeout
from asyncio.exceptions import TimeoutError

dir_path = Path(__file__).parent
template_path = dir_path / "template"
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_path), enable_async=True
)

headers = {
    'Authorization': get_driver().config.api_token
}
  
async def get_AccountInfo(qqid,info):
    try:
        url,params = '',''
        if isinstance(info,List):
            for i in info:
                if str(i).lower() == 'me':
                    url = 'https://api.wows.linxun.link/public/wows/account/v2/user/info'
                    params = {
                    "server": "QQ",
                    "accountId": str(qqid)
                    }
                    break
                match = re.search(r"CQ:at,qq=(\d+)",i)
                if match:
                    url = 'https://api.wows.linxun.link/public/wows/account/v2/user/info'
                    params = {
                    "server": "QQ",
                    "accountId": match.group(1)
                    }
                    break
            if not params and len(info) == 2:
                param_server,info = await match_keywords(info,servers)
                if param_server:
                    param_accountid = await get_AccountIdByName(param_server,str(info[0]))
                    if param_accountid and param_accountid != 404:
                        url = 'https://api.wows.linxun.link/public/wows/account/v2/user/info'
                        params = {
                        "server": param_server,
                        "accountId": param_accountid
                        }
                    elif param_accountid == 404:
                        return '无法查询该游戏昵称Orz，请检查昵称是否存在'
                    else:
                        return '发生了错误，有可能是网络波动，请稍后再试'
                else:
                    return '服务器参数似乎输错了呢'
            elif params:
                logger.info(f"{params}")
            else:
                return '您似乎准备用游戏昵称查询，请检查参数中是否包含服务器和游戏昵称，以空格区分'
        else:
            return '参数似乎出了问题呢'
        logger.info(f"下面是本次请求的参数，如果遇到了问题，请将这部分连同报错日志一起发送给麻麻哦\n{url}\n{params}")
        async with httpx.AsyncClient(headers=headers) as client:
            resp = await client.get(url, params=params, timeout=20)
            logger.info(f"本次请求返回的状态码:{resp.status_code}")
            result = resp.json()
            logger.info(f"本次请求服务器计算时间:{result['queryTime']}")
        if result['code'] == 200 and result['data']:
            template = env.get_template("wws-info.html")
            template_data = await set_infoparams(result['data'])
            content = await template.render_async(template_data)
            return await html_to_pic(content, wait=0, viewport={"width": 920, "height": 1000})
        elif result['code'] == 403:
            return f"{result['message']}\n请先绑定账号"
        elif result['code'] == 404 or result['code'] == 405:
            return f"{result['message']}"
        elif result['code'] == 500:
            return f"{result['message']}\n这是服务器问题，请联系雨季麻麻"
        else:
            return 'wuwuu好像出了点问题，过一会儿还是不行的话请联系麻麻'
    except (TimeoutError, ConnectTimeout):
        logger.warning(traceback.format_exc())
        return '请求超时了，请过会儿再尝试哦~'
    except Exception:
        logger.error(traceback.format_exc())
        return 'wuwuwu出了点问题，请联系麻麻解决'