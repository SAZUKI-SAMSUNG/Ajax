class script(object):
    START_TXT = """ℍ𝔼𝕃𝕃𝕆 {},
𝕄𝕐 ℕ𝔸𝕄𝔼 𝕀𝕊 <a href=https://t.me/{}>{}</a>, 𝕀 ℂ𝔸ℕ  ℙℝ𝕆𝕍𝕀𝔻𝔼 𝕄𝕆𝕍𝕀𝔼𝕊 , 𝕁𝕌𝕊𝕋 𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝕐𝕆𝕌ℝ 𝔾ℝ𝕆𝕌ℙ 𝔸ℕ𝔻 𝕄𝔸𝕂𝔼 𝕄𝔼 𝔸𝔻𝕄𝕀ℕ.. 𝕋ℍ𝔼ℕ 𝕊𝔼𝔼 𝕄𝕐 ℙ𝕆𝕎𝔼ℝ𝕊..  ❗❗"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✮ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
╔════❰𝙁𝙖𝙢𝙞𝙡𝙮 𝙏𝙧𝙚𝙚❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ 𝙈𝙔 𝙉𝘼𝙈𝙀 - <a href="https://t.me/SAZUKI_FILTER_BOT"> ➪𝚅 ᵇᵗˢ </a>
║┣⪼ Ⓓ︎Ⓔ︎Ⓥ︎1 - <a href="https://t.me/TEAM_KERALA"> ➪𝚂𝙰𝚉𝚄𝙺𝙸✞︎🇮🇳[OFFLINE] </a>
║┣⪼ 𝙴𝙳𝙸𝚃𝙸𝙽𝙶 - <a href="https://t.me/TEAM_KERALA"> ➪𝚂𝙰𝚉𝚄𝙺𝙸✞︎🇮🇳[OFFLINE] </a>
║┣⪼ Ⓓ︎Ⓔ︎Ⓥ︎2 - <a href="https://t.me/Peter_parker_10"> 𝙿𝙴𝚃𝙴𝚁✞︎🇮🇳[OFFLINE] </a>
║┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙴𝚁 - <a href="https://t.me/pushpa_Reju"> ᵗᵍ𝕻𝖚𝖘𝖍𝖕𝖆𝕽𝖊𝖏𝖚 </a>
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
║┣⪼ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮 - 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  𝙷𝙴𝚁𝙾𝙺𝚄
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪"""
    SOURCE_TXT = """<b>Donation</b>


<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/Aadhi011><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᗩᒍᗩ᙭ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
➾ /filter - <code>add a filter in chat</code>
➾ /filters - <code>list all the filters of a chat</code>
➾ /del - <code>delete a specific filter in chat</code>
➾ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ᗩᒍᗩ᙭ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᗩᒍᗩ᙭ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text</code>

<b>Alert buttons:</b>
<code>Button Text</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
➾ /connect  - <code>connect a particular chat to your PM</code>
➾ /disconnect  - <code>disconnect from a chat</code>
➾ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of ᗩᒍᗩ᙭

<b>Commands and Usage:</b>
➾ /id - <code>get id of a specifed user.</code>
➾ /info  - <code>get information about a user.</code>
➾ /imdb  - <code>get the film information from IMDb source.</code>
➾ /search  - <code>get the film information from various sources.</code>
➾ /roll  - <code>get the dice roll play fun gameplays.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OᗯᑎEᖇ⚡

<b>Commands and Usage:</b>
➾ /logs - <code>to get the rescent errors</code>
➾ /stats - <code>to get status of files in db.</code>
➾ /delete - <code>to delete a specific file from db.</code>
➾ /users - <code>to get list of my users and ids.</code>
➾ /chats - <code>to get list of the my chats and ids </code>
➾ /leave  - <code>to leave from a chat.</code>
➾ /disable  -  <code>do disable a chat.</code>
➾ /ban  - <code>to ban a user.</code>
➾ /unban  - <code>to unban a user.</code>
➾ /roll  - <code>to roll a only admins.</code>
➾ /channel - <code>to get list of total connected channels</code>
➾ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ 𝔽𝕀𝕃𝔼𝕊: <code>{}</code>
 𝕋𝕆𝕋𝔸𝕃 𝕌𝕊𝔼ℝ𝕊: <code>{}</code>
 𝕋𝕆𝕋𝔸𝕃 ℂℍ𝔸𝕋𝕊: <code>{}</code>
 𝕌𝕊𝔼𝔻 𝕊𝕋𝕆ℝ𝔸𝔾𝔼: <code>{}</code> 𝙼𝚒𝙱
 𝔽ℝ𝔼𝔼 𝕊𝕋𝕆ℝ𝔸𝔾𝔼: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
 𝔾ℝ𝕆𝕌ℙ ›› {}(<code>{}</code>)
 𝕋𝕆𝕋𝔸𝕃 𝕄𝔼𝕄𝔹𝔼ℝ𝕊 ›› <code>{}</code>➪➪ 𝔸𝔻𝔻𝔼𝔻 𝔹𝕐 ›› {}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
 𝕀𝔻 ›› <code>{}</code>
 ℕ𝔸𝕄𝔼 ›› {}
"""
