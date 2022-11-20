import sys
from pyrogram import idle
from asyncio import get_event_loop
from aiohttp import web
from app import env, user, user_dict
from app.server import web_server

loop = get_event_loop()

async def start_services():
    print('\n')
    print('[+] Initalizing Telegram Clients ...')
    await user.start()
    print('[√] DONE')
    print('\n')
    print('[+] Initalizing Web Server ...')
    app = web.AppRunner(await web_server())
    await app.setup()
    try:
        await web.TCPSite(app, "0.0.0.0", "8080").start()
    except:
        sys.exit()
    print('[√] DONE')
    print('\n')
    print('Pyrogram Client => {} (@{})'.format(user_dict.first_name, user_dict.username))
    print('Server FQDN => {}'.format(env.FQDN))
    await idle()

if __name__ == '__main__':
    loop.run_until_complete(start_services())
