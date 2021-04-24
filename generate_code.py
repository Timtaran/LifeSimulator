all1 = open('D:\Timur\LSN\src\\vk\story\courier\story.txt', 'r')
all = all1.read().split('--------')
all1.close()
import os
all_text="""
async def func(message):
"""
for dialog in all:
    d2=dialog.replace('\n', '\\n')
    print(f"""
        {dialog}
    """)
    all_text+=f"""
    await message.answer("{d2}")
    await asyncio.sleep({input("скок ждать?")})
"""
g=open('D:\Timur\LSN\src\\vk\story\courier\codeversion.py', 'w')
g.write(all_text)
g.close()