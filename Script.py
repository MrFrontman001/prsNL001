class script(object):

    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴀꜱ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ... ɪᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ᴍᴏᴠɪᴇꜱ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ... ♻️</b>"""

    MY_ABOUT_TXT = """★ Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://t.me/HydrogramNews>Hydrogram</a>"""

    PROMOTE_TXT = """Reach more audience by promoting your channel, group or bot here. Contact ADMIN for more details."""

    STATUS_TXT = """👤 Total Users: <code>{}</code>
😎 Premium Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
🗳 Data database used: <code>{}</code>

🗂 1st database Files: <code>{}</code>
🗳 1st files database used: <code>{}</code>

🗂 2nd database Files: <code>{}</code>
🗳 2nd files database used: <code>{}</code>

🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """<b>ʜᴇʏ {} 🎀,
➠ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

➠ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴡɪᴛʜ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ 😃

➠ ᴘʟᴇᴀsᴇ ʀᴇᴀᴅ ᴛʜᴇ ɪɴsᴛʀᴜᴄᴛɪᴏɴs ᴀɴᴅ ʀᴜʟᴇs ᴛᴏ ɢᴇᴛ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛs.

➠ ᴏʀ ɴᴏᴛ ʙᴇᴇɴ ʀᴇʟᴇᴀsᴇᴅ ʏᴇᴛ

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./) </b>"""
    
    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<b>{file_caption}</b>"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    RULES_TXT = """<blockquote><b>🌐 Movies/Series Search Rules 🔍</blockquote>
    
    ➜ ᴀʟᴡᴀʏꜱ ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ/ꜱᴇʀɪᴇꜱ ɪɴ ᴇɴɢʟɪꜱʜ. ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴏᴛʜᴇʀꜱ ʟᴀɴɢᴜᴀɢᴇ.

◉ ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ ʟɪᴋᴇ ᴛʜɪꜱ :- 
› ꜱᴀʟᴀᴀʀ 2023 ✔️ 
› ꜱᴀʟᴀᴀʀ ʜɪɴᴅɪ ✔️ 
› ꜱᴀʟᴀᴀʀ ꜱᴏᴜᴛʜ ᴍᴏᴠɪᴇ ❌ 
› ꜱᴀʟᴀᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ ❌ 

◉ ꜱᴇᴀʀᴄʜ ꜱᴇʀɪᴇꜱ ʟɪᴋᴇ ᴛʜɪꜱ :- 
› ᴠɪᴋɪɴɢꜱ ✔️ 
› ᴠɪᴋɪɴɢꜱ ꜱ01 ✔️ 
› ᴠɪᴋɪɴɢꜱ ꜱᴇᴀꜱᴏɴ 1 ❌ 
› ᴠɪᴋɪɴɢꜱ ᴡᴇʙ ꜱᴇʀɪᴇꜱ ❌ 
<blockquote>➜ ɪғ ᴍᴏᴠɪᴇ/ꜱᴇʀɪᴇꜱ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ ꜱᴇɴᴅ ɴᴀᴍᴇ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.</blockquote></b>"""

    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇


/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels
/add_prm - to add new premium user
/rm_prm - to add remove premium user
/delreq - to delete join request in db (if change REQUEST_FORCE_SUB_CHANNELS using /set_req_fsub then must need use this command)
/set_req_fsub - to set request force subscribe channel
/set_fsub - to set force subscribe channels</b>"""
    
    PLAN_TXT = """Activate any premium plan to get exclusive features.

You can activate any premium plan and then you can get exclusive features.

- INR {} for pre day -

Basic premium features:
Ad free experience
Online watch and fast download
No need joind channels
No need verify
No shortlink
Admins support
And more...

Support: {}"""

    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/myplan - to check my activated premium plan
/plan - to view premium plan details
/img_2_link - upload image to uguu.se and get link
/settings - to change group settings as your wish
/connect - to connect group settings to PM
/id - to check group or channel id</b>"""
    
    DMCA_TXT = """<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.
ɪғ ᴡᴇ ʜᴀᴠᴇ ᴠɪᴏʟᴀᴛᴇᴅ ᴀɴʏᴛʜɪɴɢ, ᴘʟᴇᴀꜱᴇ <a href=https://t.me/DevThanos>ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ</a>.
</b>"""

