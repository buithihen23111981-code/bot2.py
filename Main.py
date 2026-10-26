
import os,sys,csv,time,random,string,re,threading
import asyncio,traceback,json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
TK="8701610980:AAHan8y-6yfa4eRLzJ2DyEy"
TK+="EL1X_vg05yZ0"
ADMIN=8667824227
GI=-1004460956126
GL="https://t.me/sharehackffiosadr"
GN="Hack cheat adr-ios chat"
MJ=10
AT=45
PT=4
MD="Markdown"
GP=0.05
OTP=25
SRC=[
"https://raw.githubusercontent.com/proxy-free"
"/free-proxy-list/main/socks5.txt",
"https://raw.githubusercontent.com/proxy-free"
"/free-proxy-list/main/http.txt",
"https://raw.githubusercontent.com/TheSpeedX"
"/PROXY-List/master/socks5.txt",
"https://raw.githubusercontent.com/TheSpeedX"
"/PROXY-List/master/http.txt",
"https://raw.githubusercontent.com/monosans"
"/proxy-list/main/proxies/socks5.txt"]

def dp():
    n=[]
    pk=[("requests","requests"),
        ("socks","PySocks"),
        ("telegram","python-telegram-bot")]
    for m,p in pk:
        try: __import__(m)
        except: n.append(p)
    if n:
        c=sys.executable
        c+=" -m pip install --quiet "
        os.system(c+" ".join(n))

dp()
import requests
from telegram import Update,BotCommand
from telegram import MenuButtonCommands
from telegram import BotCommandScopeChat
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import ContextTypes

UA=[
"Mozilla/5.0 (Windows NT 10.0; Win64; x64"
") AppleWebKit/537.36 Chrome/122",
"Mozilla/5.0 (Macintosh; Intel Mac OS X "
"10_15_7) AppleWebKit/537.36 Chrome/122",
"Mozilla/5.0 (Linux; Android 14) AppleW"
"ebKit/537.36 Chrome/122 Mobile"]

RG="https://backend-api.genplay.io"
RG+="/api/user/register"
VR="https://backend-api.genplay.io"
VR+="/api/user/verify"
TF="genplay_accs.txt"
CF="genplay_accs.csv"
PF="proxies.txt"
UF="users.json"
MF="mails.json"
FL=threading.Lock()
JS=threading.Semaphore(MJ)
JB={}
WAIT={}
USER_REF={}

def load_users():
    if not os.path.exists(UF): return {}
    try:
        with open(UF,encoding="utf-8") as f:
            return json.load(f)
    except: return {}

def save_users(d):
    try:
        with open(UF,"w",encoding="utf-8") as f:
            json.dump(d,f,ensure_ascii=False)
    except: pass

def add_user(u):
    if not u: return
    uid=str(u.id)
    d=load_users()
    if uid not in d:
        d[uid]={
          "id":u.id,
          "name":u.full_name or "",
          "user":u.username or "",
          "first_seen":datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")}
        save_users(d)

def is_admin(u):
    return u and u.id==ADMIN

def load_mails():
    if not os.path.exists(MF): return {}
    try:
        with open(MF,encoding="utf-8") as f:
            return json.load(f)
    except: return {}

def save_mails(d):
    try:
        with open(MF,"w",encoding="utf-8") as f:
            json.dump(d,f,ensure_ascii=False)
    except: pass

def fp(s):
    if not s: return None
    s=s.strip()
    if s.startswith(("http","socks")):
        return {"http":s,"https":s}
    p=s.split(":")
    if len(p)==4:
        f="http://"+p[2]+":"+p[3]
        f+="@"+p[0]+":"+p[1]
    elif len(p)==2:
        f="http://"+p[0]+":"+p[1]
    else: f=s
    return {"http":f,"https":f}

def ss(px=None):
    s=requests.Session()
    if px:
        p=fp(px)
        if p: s.proxies.update(p)
    return s

def alv(p):
    try:
        u="https://api.ipify.org?format=json"
        r=ss(p).get(u,timeout=PT)
        if r.status_code==200:
            return True,r.json().get("ip")
    except: pass
    return False,None

def ck(l,w=100):
    o=[]
    if not l: return o
    with ThreadPoolExecutor(max_workers=w) as ex:
        f={ex.submit(alv,p):p for p in l}
        for x in as_completed(f):
            try:
                k,i=x.result()
                if k: o.append((f[x],i))
            except: pass
    return o

def pl():
    a=set()
    try:
        r=requests.get("https://openproxylist.xyz/socks5.txt",timeout=12)
        if r.status_code==200:
            for l in r.text.splitlines():
                l=l.strip()
                if l and ":" in l: a.add(l)
    except: pass
    pt=re.compile(r"^\d+\.\d+\.\d+\.\d+:\d+$")
    for u in SRC:
        try:
            r=requests.get(u,timeout=12)
            if r.status_code!=200: continue
            for l in r.text.splitlines():
                l=l.strip()
                if pt.match(l): a.add(l)
        except: continue
    return list(a)

def fsv(mn=3,lm=600,lg=None):
    def L(m):
        if lg: lg(m)
    L("[FETCH] pull...")
    r=pl()
    if not r:
        L("[FETCH] fail");return []
    L("[FETCH] "+str(len(r))+" raw")
    random.shuffle(r)
    s=r[:lm]
    g=ck(s)
    L("[FETCH] "+str(len(g))+"/"+str(len(s)))
    tries=0
    while len(g)<mn and tries<5:
        tries+=1
        L("[FETCH] thử thêm lần "+str(tries))
        g+=ck(r[lm*tries:lm*(tries+1)])
        L("[FETCH] +"+str(len(g)))
    if not g: return []
    with open(PF,"w",encoding="utf-8") as f:
        for p,_ in g: f.write(p+"\n")
    L("[FETCH] saved "+str(len(g)))
    return [p for p,_ in g]

def rp(n=12):
    p=[random.choice(string.ascii_uppercase),
       random.choice(string.ascii_lowercase),
       random.choice(string.digits),
       random.choice("!@#$%^&*")]
    p+=random.choices(
        string.ascii_letters+string.digits,k=n-4)
    random.shuffle(p)
    return "".join(p)

def xo(t):
    if not t: return None
    m=re.search(r"(?:code is|otp is|verification code|mã xác minh|code|otp)[:\s]+([0-9]{4,8})",t,re.I)
    if m: return m.group(1).strip()
    m=re.search(r"verification code is[:\s]+([A-Za-z0-9]{6,8})",t,re.I)
    if m: return m.group(1).strip()
    codes = re.findall(r"\b([0-9]{4,8})\b", t)
    if codes:
        for c in codes:
            if len(c) >= 4 and len(c) <= 8 and not c.startswith("20"):
                return c
    codes_alphanum = re.findall(r"\b([A-Za-z0-9]{6,8})\b",t)
    bad=["platform","activate","welcome","account","support","genplay","password","register","vmos","umocloud"]
    for c in codes_alphanum:
        if c.isdigit(): continue
        if c.lower() in bad: continue
        if any(char.isdigit() for char in c):
            if re.match(r"^[0-9a-fA-F]+$", c) and not any(char.isalpha() and not char in "abcdefABCDEF" for char in c):
                 continue
            return c.strip()
    return None

def sv(e,pw,rf):
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ln=e+"|"+pw+"|"+(rf or "N/A")+"|OK|"+ts+"\n"
    with FL:
        with open(TF,"a",encoding="utf-8") as f:
            f.write(ln)
        ex=os.path.exists(CF)
        with open(CF,"a",newline="",encoding="utf-8") as f:
            w=csv.writer(f)
            if not ex:
                w.writerow(["Email","Password","Ref","Status","Ts"])
            w.writerow([e,pw,rf or "N/A","OK",ts])

def mk(nm):
    s=ss()
    try:
        if nm=="TL":
            u1="https://api.tempmail.lol/v2/inbox/create"
            r=s.post(u1,timeout=8)
            if r.status_code not in (200,201): return None
            d=r.json()
            e=d.get("address"); t=d.get("token")
            if not e or not t: return None
            u="https://api.tempmail.lol/v2/inbox?token="+str(t)
        elif nm=="MG":
            r=s.get("https://api.mail.gw/domains",timeout=6)
            a=r.json().get("hydra:member")
            if not a: return None
            d=random.choice(a)["domain"]
            e="u"+str(random.randint(100000,999999))+"@"+d
            p="P"+str(random.randint(100000,999999))
            b={"address":e,"password":p}
            r=s.post("https://api.mail.gw/accounts",json=b,timeout=6)
            if r.status_code not in (200,201): return None
            r=s.post("https://api.mail.gw/token",json=b,timeout=6)
            if r.status_code!=200: return None
            t=r.json().get("token"); u="https://api.mail.gw/messages"
        elif nm=="MT":
            r=s.get("https://api.mail.tm/domains",timeout=8)
            a=r.json().get("hydra:member")
            if not a: return None
            ds=[x["domain"] for x in a]; random.shuffle(ds)
            for d in ds:
                e="u"+str(random.randint(1000000,9999999))+"@"+d
                p="P"+str(random.randint(1000000,9999999))
                b={"address":e,"password":p}
                r=s.post("https://api.mail.tm/accounts",json=b,timeout=8)
                if r.status_code in (200,201):
                    r2=s.post("https://api.mail.tm/token",json=b,timeout=8)
                    if r2.status_code==200:
                        t=r2.json().get("token")
                        u="https://api.mail.tm/messages"
                        break
                elif r.status_code==429: time.sleep(1)
            else: return None
        elif nm=="GM":
            u2="https://api.guerrillamail.com/ajax.php?f=get_email_address"
            d=s.get(u2,timeout=6).json()
            e=d.get("email_addr"); t=d.get("sid_token")
            if not e or "guerrillamailblock" in e: return None
            u="https://api.guerrillamail.com/ajax.php?f=check_email&seq=0&sid_token="+str(t)
        else: return None
        
        def go(to=OTP):
            st=time.time(); sn=set()
            while time.time()-st<to:
                try:
                    if nm=="TL":
                        r=s.get(u,timeout=6)
                        if r.status_code==200:
                            for m in r.json().get("emails",[]):
                                i=m.get("id") or m.get("date")
                                if i in sn: continue
                                sn.add(i)
                                b=str(m.get("subject",""))+" "+str(m.get("body",""))+" "+str(m.get("html",""))
                                c=xo(b)
                                if c: return c
                    elif nm=="GM":
                        r=s.get(u,timeout=5)
                        if r.status_code==200:
                            for it in r.json().get("list",[]):
                                i=it.get("mail_id")
                                if i in sn: continue
                                sn.add(i)
                                b=it.get("mail_subject","")+" "+it.get("mail_excerpt","")
                                c=xo(b)
                                if c: return c
                    else:
                        h={"Authorization":"Bearer "+str(t)}
                        r=s.get(u,headers=h,timeout=6)
                        if r.status_code==200:
                            for m in r.json().get("hydra:member") or []:
                                i=m.get("id")
                                if i in sn: continue
                                sn.add(i)
                                u2=u+"/"+str(i)
                                d2=s.get(u2,headers=h,timeout=6).json()
                                b=""
                                for pp in d2.get("html") or []: b+=str(pp)
                                if d2.get("text"): b+=str(d2["text"])
                                c=xo(str(d2.get("subject",""))+" "+b)
                                if c: return c
                except: pass
                time.sleep(0.4)
            return None
        return e,go,str(t)
    except: return None

def nm(tries=2):
    for _ in range(tries):
        for n in ("TL","MG","MT","GM"):
            r=mk(n)
            if r: return (n,)+r
        time.sleep(0.2)
    return None

def hd(rf):
    h={"User-Agent":random.choice(UA),"Content-Type":"application/json","Accept":"application/json, text/plain, */*","Accept-Language":"en-US,en;q=0.9","Origin":"https://app.genplay.io","Referer":"https://app.genplay.io/","sec-ch-ua":'"Chromium";v="122"',"sec-ch-ua-mobile":"?0","sec-ch-ua-platform":'"Windows"',"Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site"}
    if rf: h["Cookie"]="referral="+rf.strip()
    return h

def rg(s,e,pw,rf,rt=2,lg=None):
    pl={"email":e,"password":pw}
    if rf: pl["referral_code"]=rf.strip()
    last=None
    for i in range(1,rt+1):
        try:
            r=s.post(RG,json=pl,headers=hd(rf),timeout=12)
            try: d=r.json()
            except: d={"raw":r.text[:400]}
            ok=(r.status_code==200 and (d.get("code")=="200000" or str(d.get("message","")).lower()=="success"))
            if ok: return True,None
            last={"s":r.status_code,"b":str(d)[:400]}
            if lg: lg("reg "+str(i)+" "+str(r.status_code))
            bad=(r.status_code==429 or "too many" in str(d).lower())
            if bad and i<rt:
                time.sleep(2+i*2); continue
            return False,last
        except Exception as e:
            last={"e":str(e)[:200]}
            if lg: lg("reg "+str(i)+" "+str(e)[:80])
            if i<rt: time.sleep(1+i); continue
            return False,last
    return False,last

def vf(s,e,o):
    try:
        r=s.post(VR,json={"email":e,"code":o.strip()},headers=hd(None),timeout=12)
        d=r.json()
        return (r.status_code==200 and (d.get("code")=="200000" or str(d.get("message","")).lower()=="success"))
    except: return False

def tw(fn,to,*a,**kw):
    r=[None];e=[None];dn=threading.Event()
    def t():
        try: r[0]=fn(*a,**kw)
        except Exception as x: e[0]=x
        finally: dn.set()
    threading.Thread(target=t,daemon=True).start()
    if not dn.wait(to): return None
    if e[0]: return {"err":str(e[0])}
    return r[0]

def ma(wid,rf,cp,px,lg=None):
    def L(m):
        if lg: lg("[#"+str(wid)+"] "+m)
    def impl():
        L("mail")
        r=nm(2)
        if not r: L("mail FAIL");return False
        n,e,go,tk=r
        pw=cp or rp()
        L("mail "+e+" ["+n+"]")
        s=ss(px)
        L("reg "+(px or "direct"))
        ok,er=rg(s,e,pw,rf,lg=L)
        if not ok: L("reg FAIL");return False
        L("OTP")
        o=go(OTP)
        if not o: L("OTP FAIL");return False
        L("verify "+o)
        if vf(s,e,o):
            L("OK "+e); sv(e,pw,rf); return True
        L("verify FAIL"); return False
    r=tw(impl,AT)
    if r is None: L("TIMEOUT");return False
    if isinstance(r,dict) and "err" in r: L("ERR "+r["err"][:80]); return False
    return bool(r)

def lp():
    if os.path.exists(PF):
        try:
            with open(PF,encoding="utf-8") as f:
                l=[x.strip() for x in f if x.strip() and not x.startswith("#")]
            if l: return l
        except: pass
    return []

def inc(cid,uid):
    try:
        u="https://api.telegram.org/bot"+TK+"/getChatMember"
        r=requests.get(u,params={"chat_id":cid,"user_id":uid},timeout=8)
        d=r.json()
        if not d.get("ok"): return False
        return d["result"]["status"] in ("member","administrator","creator","restricted")
    except: return False

def mc(uid):
    m=[]
    if GI and not inc(GI,uid): m.append((GN,GL))
    return m

def jkb(m):
    b=[]
    for n,l in m: b.append([InlineKeyboardButton("📢 "+n,url=l)])
    b.append([InlineKeyboardButton("✅ Đã vào — kiểm tra",callback_data="rc")])
    return InlineKeyboardMarkup(b)

async def nj(u):
    m=mc(u.effective_user.id)
    if not m: return False
    t="⚠️ *Bắt buộc vào nhóm trước*\n\n"
    for n,l in m: t+="❌ "+n+"\n"
    t+="\nVào nhóm rồi bấm nút dưới."
    await u.message.reply_text(t,parse_mode=MD,reply_markup=jkb(m))
    return True

def mkb_main():
    b=[
      [InlineKeyboardButton("🚀 Buff KC GenPlay",callback_data="menu_gen")],
      [InlineKeyboardButton("📧 Tạo mail ảo",callback_data="menu_mail"),
       InlineKeyboardButton("🔑 Check OTP",callback_data="menu_otp")],
      [InlineKeyboardButton("🔧 Proxy",callback_data="menu_proxy"),
       InlineKeyboardButton("📊 Trạng thái",callback_data="menu_st")],
      [InlineKeyboardButton("📁 Tải file",callback_data="menu_files"),
       InlineKeyboardButton("📖 Hướng dẫn",callback_data="menu_help")],
    ]
    return InlineKeyboardMarkup(b)

def mkb_gen():
    b=[
      [InlineKeyboardButton("▶️ 5 acc / 3 luồng",callback_data="gen|0|5|3")],
      [InlineKeyboardButton("▶️ 10 acc / 5 luồng",callback_data="gen|0|10|5")],
      [InlineKeyboardButton("▶️ 20 acc / 8 luồng",callback_data="gen|0|20|8")],
      [InlineKeyboardButton("✏️ Nhập ref riêng",callback_data="gen_custom")],
      [InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")],
    ]
    return InlineKeyboardMarkup(b)

def mkb_proxy():
    b=[
      [InlineKeyboardButton("🔄 Pull proxy mới",callback_data="proxy_fetch")],
      [InlineKeyboardButton("🔍 Test proxy có sẵn",callback_data="proxy_test")],
      [InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")],
    ]
    return InlineKeyboardMarkup(b)

def mkb_mail():
    b=[
      [InlineKeyboardButton("📧 tempmail.lol",callback_data="mail|TL"),
       InlineKeyboardButton("📧 mail.gw",callback_data="mail|MG")],
      [InlineKeyboardButton("📧 mail.tm",callback_data="mail|MT"),
       InlineKeyboardButton("📧 guerrilla",callback_data="mail|GM")],
      [InlineKeyboardButton("📋 Xem mail đã tạo",callback_data="mail_list")],
      [InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")],
    ]
    return InlineKeyboardMarkup(b)

def mkb_otp():
    b=[
      [InlineKeyboardButton("🔑 mail.tm",callback_data="otp|MT"),
       InlineKeyboardButton("🔑 mail.gw",callback_data="otp|MG")],
      [InlineKeyboardButton("🔑 tempmail.lol",callback_data="otp|TL")],
      [InlineKeyboardButton("✏️ Nhập email check",callback_data="otp_custom")],
      [InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")],
    ]
    return InlineKeyboardMarkup(b)

def mkb_help():
    b=[[InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")]]
    return InlineKeyboardMarkup(b)

def mkb_back():
    b=[[InlineKeyboardButton("🔙 Quay lại",callback_data="menu_home")]]
    return InlineKeyboardMarkup(b)

def help_text():
    t="*📖 Hướng dẫn*\n\n"
    t+="*1. 🚀 Buff KC GenPlay*\n"
    t+="• Gõ `/ref <mã>` lưu mã mời\n"
    t+="• Bấm `🚀 Buff KC GenPlay`\n\n"
    t+="*Lệnh:*\n"
    t+="• `/start` `/ref` `/check`\n\n"
    t+="*Admin:*\n"
    t+="/buffkc /proxy /users /thongbao\n"
    return t

async def menu_show(u,c):
    uid=u.effective_user.id
    if str(uid) in WAIT: del WAIT[str(uid)]
    t="*🎮 GenPlay Bot*\n\nChọn chức năng:"
    await u.message.reply_text(t,parse_mode=MD,reply_markup=mkb_main())

async def cs(u,c):
    add_user(u.effective_user)
    if await nj(u): return
    if is_admin(u.effective_user):
        cmds=[
            BotCommand("start","Menu"),
            BotCommand("ref","Lưu mã ref GenPlay"),
            BotCommand("check","Lấy OTP"),
            BotCommand("buffkc","Buff KC nhanh (admin)"),
            BotCommand("proxy","Pull+test N proxy"),
            BotCommand("users","Đếm user"),
            BotCommand("thongbao","Broadcast")]
        try:
            await u.message.bot.set_my_commands(cmds,scope=BotCommandScopeChat(chat_id=u.effective_user.id))
        except: pass
    await menu_show(u,c)

async def cref(u,c):
    add_user(u.effective_user)
    if await nj(u): return
    a=c.args
    if not a:
        await u.message.reply_text("*✏️ Nhập mã ref GenPlay*\n\nCú pháp: `/ref <mã>`",parse_mode=MD)
        return
    rf=a[0].strip()
    USER_REF[str(u.effective_user.id)]=rf
    await u.message.reply_text("✅ *Đã lưu ref:* `"+rf+"`",parse_mode=MD)

async def ccheck(u,c):
    add_user(u.effective_user)
    if await nj(u): return
    a=c.args
    if not a:
        await u.message.reply_text("`/check <email>`",parse_mode=MD)
        return
    em=a[0].strip()
    await u.message.reply_text("🔑 Check `"+em+"`...",parse_mode=MD)
    m=load_mails()
    prov="MT"
    for k,lst in m.items():
        for x in lst:
            if x["email"]==em:
                prov=x.get("provider","MT")
                break
    otp=await fetch_otp(prov,"",OTP)
    if not otp: otp=await fetch_otp("MG","",OTP)
    if otp: await u.message.reply_text("✅ OTP: `"+otp+"`",parse_mode=MD)
    else: await u.message.reply_text("❌ Chưa có OTP.")

async def cbuffkc(u,c):
    add_user(u.effective_user)
    if not is_admin(u.effective_user): return
    a=c.args
    uid=str(u.effective_user.id)
    if len(a)<1:
        rf=USER_REF.get(uid,"")
        if not rf:
            await u.message.reply_text("`/buffkc <ref> [qty] [th]`\nvd: `/buffkc ABC123 20 5`",parse_mode=MD)
            return
        q=5;th=3
    else:
        rf=a[0].strip(); q=5;th=3
        if len(a)>=2 and a[1].isdigit(): q=int(a[1])
        if len(a)>=3 and a[2].isdigit(): th=int(a[2])
    USER_REF[uid]=rf
    asyncio.create_task(run_job(u,u.message,rf,q,th,None))

async def cproxy(u,c):
    add_user(u.effective_user)
    if not is_admin(u.effective_user): return
    a=c.args
    if not a or not a[0].isdigit():
        await u.message.reply_text("`/proxy <số lượng>`",parse_mode=MD)
        return
    n=int(a[0])
    await u.message.reply_text("🔄 Pull + test "+str(n)+" proxy...")
    lp2=asyncio.get_running_loop()
    bf=[];bk=threading.Lock()
    def lg(m):
        with bk: bf.append(m)
    def run():
        try: return fsv(3,n,lg)
        except Exception as e:
            lg("crash "+str(e)); return []
    g=await lp2.run_in_executor(None,run)
    with bk: tl="\n".join(bf)[-400:]
    if g:
        head="\n".join(g[:20])
        msg=f"*✅ Pull xong*\n\n```\n{tl}\n```\nSống: *{len(g)}* / {n}\n\n```\n{head}\n```"
        try: await u.message.reply_text(msg[:3900],parse_mode=MD)
        except: pass
    else:
        try: await u.message.reply_text("```\n"+tl+"\n```\n❌ 0 proxy sống.",parse_mode=MD)
        except: pass

async def cb_handler(u,c):
    q=u.callback_query
    await q.answer()
    uid=q.from_user.id
    d=q.data
    if d=="rc":
        m=mc(uid)
        if not m:
            await q.edit_message_text("✅ Xác minh xong.",parse_mode=MD)
            try: await q.message.reply_text("*🎮 GenPlay Bot*\n\nChọn chức năng:",parse_mode=MD,reply_markup=mkb_main())
            except: pass
        else:
            await q.edit_message_text("❌ Chưa vào nhóm.\nVào rồi bấm lại.",reply_markup=jkb(m))
        return
    if d=="menu_home":
        try: await q.edit_message_text("*🎮 GenPlay Bot*\n\nChọn chức năng:",parse_mode=MD,reply_markup=mkb_main())
        except: pass
        return
    if d=="menu_gen":
        rf=USER_REF.get(str(uid),"")
        t="*🚀 Buff KC GenPlay*\n\n"
        if rf: t+="Ref đã lưu: `"+rf+"`\n\n"
        else: t+="⚠️ Chưa có ref. Gõ `/ref <mã>` trước.\n\n"
        t+="Chọn số lượng:"
        try: await q.edit_message_text(t,parse_mode=MD,reply_markup=mkb_gen())
        except: pass
        return
    if d=="menu_proxy":
        l=lp()
        t="*🔧 Proxy*\n\nCó: *"+str(len(l))+"*"
        try: await q.edit_message_text(t,parse_mode=MD,reply_markup=mkb_proxy())
        except: pass
        return
    if d=="menu_mail":
        try: await q.edit_message_text("*📧 Tạo mail ảo*\n\nChọn provider:",parse_mode=MD,reply_markup=mkb_mail())
        except: pass
        return
    if d=="menu_otp":
        try: await q.edit_message_text("*🔑 Check OTP*\n\nChọn:",parse_mode=MD,reply_markup=mkb_otp())
        except: pass
        return
    if d=="menu_help":
        try: await q.edit_message_text(help_text(),parse_mode=MD,reply_markup=mkb_help())
        except: pass
        return
    if d=="menu_st":
        st=JB.get(q.message.chat.id,{})
        if st.get("running"):
            el=round(time.time()-st.get("start",time.time()),1)
            t=f"*📊 Job đang chạy*\n⏳ {el}s\n✅ ok {st.get('ok',0)}\n❌ fail {st.get('fail',0)}"
        else: t="💤 *Không có job*"
        try: await q.edit_message_text(t,parse_mode=MD,reply_markup=mkb_back())
        except: pass
        return
    if d=="menu_files":
        sd=False
        for p in (TF,CF,MF):
            if os.path.exists(p) and os.path.getsize(p):
                try:
                    with open(p,"rb") as f: await q.message.reply_document(document=f,filename=os.path.basename(p))
                    sd=True
                except: pass
        if not sd: await q.message.reply_text("Chưa file.")
        return
    if d=="proxy_fetch":
        await q.edit_message_text("🔄 Đang pull proxy...")
        lp2=asyncio.get_running_loop(); bf=[];bk=threading.Lock()
        def lg(m):
            with bk: bf.append(m)
        def run():
            try: return fsv(3,600,lg)
            except: return []
        g=await lp2.run_in_executor(None,run)
        with bk: tl="\n".join(bf)[-400:]
        if g: msg="```\n"+tl+"\n```\n✅ Lưu "+str(len(g))+" proxy"
        else: msg="```\n"+tl+"\n```\n❌ Không có proxy sống."
        try: await q.edit_message_text(msg,parse_mode=MD,reply_markup=mkb_back())
        except: pass
        return
    if d=="proxy_test":
        l=lp()
        if not l:
            await q.edit_message_text("Chưa có proxy.",reply_markup=mkb_back())
            return
        await q.edit_message_text("🔍 Test "+str(len(l))+"...")
        def run():
            g=ck(l,min(100,len(l)))
            if not g: return "✗ 0/"+str(len(l))
            o=[f"✓ {len(g)}/{len(l)}"]
            for p,i in g[:10]: o.append(p+" → "+str(i))
            return "\n".join(o)
        loop=asyncio.get_running_loop()
        res=await loop.run_in_executor(None,run)
        try: await q.edit_message_text("```\n"+res[:3000]+"\n```",parse_mode=MD,reply_markup=mkb_back())
        except: pass
        return
    if d=="mail_list":
        m=load_mails()
        um=m.get(str(uid),[])
        if not um:
            await q.edit_message_text("Chưa có mail. Tạo trước.",reply_markup=mkb_mail())
            return
        t="*📋 Mail đã tạo*\n\n"
        for x in um[-10:]: t+="📧 `"+x["email"]+"`\nProvider: "+x["provider"]+"\nTạo: "+x["created"]+"\n\n"
        await q.edit_message_text(t[:3800],parse_mode=MD,reply_markup=mkb_mail())
        return
    if d.startswith("mail|"):
        prov=d.split("|")[1]
        await q.edit_message_text("📧 Đang tạo mail "+prov+"...")
        def run(): return mk(prov)
        loop=asyncio.get_running_loop()
        r=await loop.run_in_executor(None,run)
        if not r:
            await q.edit_message_text("❌ Fail. Thử provider khác.",reply_markup=mkb_mail())
            return
        em,go,tk=r
        m=load_mails()
        if str(uid) not in m: m[str(uid)]=[]
        m[str(uid)].append({"email":em,"provider":prov,"token":tk,"created":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        save_mails(m)
        t=f"*✅ Mail đã tạo*\n\n📧 `{em}`\nProvider: {prov}\n\nDùng đăng ký umocloud.\nSau khi gửi OTP, bấm `🔑 Check OTP` hoặc gõ `/check {em}`."
        b=[[InlineKeyboardButton("🔑 Check OTP",callback_data="otp|"+prov)],[InlineKeyboardButton("📧 Tạo mail khác",callback_data="menu_mail")],[InlineKeyboardButton("🔙 Menu",callback_data="menu_home")]]
        try: await q.edit_message_text(t,parse_mode=MD,reply_markup=InlineKeyboardMarkup(b))
        except: pass
        return
    if d=="otp_custom":
        WAIT[str(uid)]="otp_email"
        try: await q.edit_message_text("*✏️ Nhập email*\n\nGõ email cần check OTP vào tin nhắn tiếp theo.",parse_mode=MD)
        except: pass
        return
    if d.startswith("otp|"):
        prov=d.split("|")[1]
        m=load_mails()
        um=m.get(str(uid),[])
        target=None
        for x in reversed(um):
            if x["provider"]==prov:
                target=x
                break
        if not target:
            await q.edit_message_text("Chưa có mail "+prov+".",reply_markup=mkb_otp())
            return
        em=target["email"]
        await q.edit_message_text("🔑 Check `"+em+"`...",parse_mode=MD)
        otp=await fetch_otp(prov,target.get("token",""),OTP)
        if otp:
            t=f"*✅ OTP*\n\n📧 `{em}`\n🔑 `{otp}`\n\nCopy nhập umocloud."
            try: await q.edit_message_text(t,parse_mode=MD,reply_markup=mkb_otp())
            except: pass
        else:
            try: await q.edit_message_text("❌ Chưa có OTP ("+str(OTP)+"s).\nĐợi 15s bấm lại.",reply_markup=mkb_otp())
            except: pass
        return
    if d=="gen_custom":
        WAIT[str(uid)]="ref"
        try: await q.edit_message_text("*✏️ Nhập ref*\n\nGõ: `<ref> <qty> <threads>`\nvd: `ABC123 10 3`",parse_mode=MD)
        except: pass
        return
    if d.startswith("gen|"):
        parts=d.split("|")
        rf=parts[1] if parts[1]!="0" else ""
        if not rf: rf=USER_REF.get(str(uid),"")
        if not rf:
            t="⚠️ *Chưa có mã ref*\n\nBạn cần nhập mã ref GenPlay trước khi buff.\n\nGõ lệnh `/ref <mã>` hoặc bấm nút dưới."
            b=[[InlineKeyboardButton("✏️ Nhập mã ref",callback_data="gen_custom")],[InlineKeyboardButton("🔙 Quay lại",callback_data="menu_gen")]]
            try: await q.edit_message_text(t,parse_mode=MD,reply_markup=InlineKeyboardMarkup(b))
            except: pass
            return
        qty=int(parts[2]); th=int(parts[3])
        asyncio.create_task(run_job(u,q.message,rf,qty,th,None))
        return

async def fetch_otp(prov,tok,to=60):
    def run():
        s=ss(); st=time.time(); sn=set()
        while time.time()-st<to:
            try:
                if prov=="MT":
                    h={"Authorization":"Bearer "+str(tok)}
                    u="https://api.mail.tm/messages"
                    r=s.get(u,headers=h,timeout=6)
                    if r.status_code==200:
                        for m in r.json().get("hydra:member") or []:
                            i=m.get("id")
                            if i in sn: continue
                            sn.add(i)
                            d=s.get(u+"/"+str(i),headers=h,timeout=6).json()
                            b="".join(str(pp) for pp in d.get("html") or [])+str(d.get("text",""))
                            c=xo(str(d.get("subject",""))+" "+b)
                            if c: return c
                elif prov=="MG":
                    h={"Authorization":"Bearer "+str(tok)}
                    u="https://api.mail.gw/messages"
                    r=s.get(u,headers=h,timeout=6)
                    if r.status_code==200:
                        for m in r.json().get("hydra:member") or []:
                            i=m.get("id")
                            if i in sn: continue
                            sn.add(i)
                            d=s.get(u+"/"+str(i),headers=h,timeout=6).json()
                            b="".join(str(pp) for pp in d.get("html") or [])+str(d.get("text",""))
                            c=xo(str(d.get("subject",""))+" "+b)
                            if c: return c
                elif prov=="TL":
                    u="https://api.tempmail.lol/v2/inbox?token="+str(tok)
                    r=s.get(u,timeout=6)
                    if r.status_code==200:
                        for m in r.json().get("emails",[]):
                            i=m.get("id") or m.get("date")
                            if i in sn: continue
                            sn.add(i)
                            b=str(m.get("subject",""))+" "+str(m.get("body",""))+" "+str(m.get("html",""))
                            c=xo(b)
                            if c: return c
                elif prov=="GM":
                    u="https://api.guerrillamail.com/ajax.php?f=check_email&seq=0&sid_token="+str(tok)
                    r=s.get(u,timeout=6)
                    if r.status_code==200:
                        for it in r.json().get("list",[]):
                            i=it.get("mail_id")
                            if i in sn: continue
                            sn.add(i)
                            b=it.get("mail_subject","")+" "+it.get("mail_excerpt","")
                            c=xo(b)
                            if c: return c
            except: pass
            time.sleep(0.4)
        return None
    return await asyncio.get_running_loop().run_in_executor(None,run)

async def msg_handler(u,c):
    uid=u.effective_user.id
    if str(uid) not in WAIT: return
    mode=WAIT[str(uid)]
    if mode=="ref":
        del WAIT[str(uid)]
        txt=u.message.text.strip(); parts=txt.split()
        if not parts: return
        rf=parts[0]; USER_REF[str(uid)]=rf; q=5;th=3
        if len(parts)>=2 and parts[1].isdigit(): q=int(parts[1])
        if len(parts)>=3 and parts[2].isdigit(): th=int(parts[2])
        await u.message.reply_text(f"✅ Đã lưu ref: `{rf}`\n🚀 Đang chạy {q} acc...",parse_mode=MD)
        asyncio.create_task(run_job(u,u.message,rf,q,th,None))
    elif mode=="otp_email":
        del WAIT[str(uid)]
        em=u.message.text.strip()
        await u.message.reply_text("🔑 Check `"+em+"`...",parse_mode=MD)
        otp=await fetch_otp("MT","",OTP) or await fetch_otp("MG","",OTP)
        if otp: await u.message.reply_text("✅ OTP: `"+otp+"`",parse_mode=MD)
        else: await u.message.reply_text("❌ Chưa có OTP.")

async def run_job(u,msg,rf,q,th,pw):
    cid=msg.chat.id
    if JB.get(cid,{}).get("running"):
        await msg.reply_text("⚠️ Đang chạy.")
        return
    JB[cid]={"running":True,"ok":0,"fail":0,"start":time.time()}
    
    # 1. Gửi tin nhắn khởi tạo (Giao diện gọn)
    status_msg = await msg.reply_text(
        f"🚀 *Đang buff KC GenPlay...*\n"
        f"└ Số lượng: `{q}` acc | Luồng: `{th}`\n"
        f"└ Trạng thái: ⏳ Đang xử lý...",
        parse_mode=MD
    )
    
    lp2=asyncio.get_running_loop()
    
    def wk():
        ok_count = 0
        fail_count = 0
        try:
            with JS:
                ps=[]
                rw=lp()
                if rw:
                    g=ck(rw,min(100,len(rw)))
                    al=[p for p,_ in g]
                    if not al: al=fsv(3,400,None)
                    ps=al
                else:
                    ps=fsv(3,400,None)
                random.shuffle(ps)
                
                cnt={"ok":0,"fail":0}; lk=threading.Lock()
                def tk(i):
                    time.sleep(GP*(i%max(1,th)))
                    p=ps[(i-1)%len(ps)] if ps else None
                    try: r=ma(i,rf,pw,p,None)
                    except Exception: r=False
                    with lk:
                        if r: cnt["ok"]+=1
                        else: cnt["fail"]+=1
                        
                with ThreadPoolExecutor(max_workers=th) as ex:
                    fss=[]
                    for i in range(q):
                        if i: time.sleep(0.05)
                        fss.append(ex.submit(tk,i+1))
                    for f in as_completed(fss):
                        try: f.result()
                        except: pass
                
                ok_count = cnt["ok"]
                fail_count = cnt["fail"]
                JB[cid]["ok"]=ok_count
                JB[cid]["fail"]=fail_count
        except Exception:
            pass
        finally:
            JB[cid]["running"]=False
            elapsed = round(time.time() - JB[cid]["start"], 2)
            
            # 2. Gửi bảng tổng kết đẹp mắt
            lines = [
                "====================",
                "   BUFF KIM CƯƠNG GENPLAY",
                "====================",
                f"Thời gian thực thi : {elapsed} giây",
                f"Thành công         : {ok_count}/{q}",
                f"Thất bại           : {fail_count}",
                "--------------------",
                "Đang gửi file tài khoản cho bạn...",
                "===================="
            ]
            report = "\n".join(lines)
            
            async def finish():
                try:
                    await status_msg.edit_text(
                        report,
                        parse_mode=MD,
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("Quay Lại Menu Chính", callback_data="menu_home")
                        ]])
                    )
                except: pass
                
                # Tự động gửi file txt
                if os.path.exists(TF) and os.path.getsize(TF)>0:
                    try:
                        with open(TF,"rb") as f:
                            await msg.reply_document(
                                document=f, 
                                filename="genplay_accounts.txt",
                                caption="Danh sách tài khoản Genplay đã tạo thành công."
                            )
                    except: pass
                    
            asyncio.run_coroutine_threadsafe(finish(), lp2)

    threading.Thread(target=wk,daemon=True).start()

async def ctb(u,c):
    add_user(u.effective_user)
    if not is_admin(u.effective_user):
        await u.message.reply_text("⛔ Admin.")
        return
    a=c.args
    if not a:
        await u.message.reply_text("`/thongbao <nội dung>`",parse_mode=MD)
        return
    txt=" ".join(a)
    d=load_users()
    await u.message.reply_text(f"📢 Gửi tới {len(d)} user...")
    ok=0;fail=0;errs=[]
    for uid in list(d.keys()):
        try:
            await c.bot.send_message(chat_id=int(uid),text="📢 *Thông báo*\n\n"+txt,parse_mode=MD)
            ok+=1
        except Exception as e:
            fail+=1
            errs.append(f"`{uid}`: {str(e)[:60]}")
            if "blocked" in str(e).lower() or "chat not found" in str(e).lower():
                if uid in d:
                    del d[uid]
                    save_users(d)
        await asyncio.sleep(0.05)
    
    msg=f"✅ ok {ok} | fail {fail}"
    if errs:
        msg+="\n\n*Lỗi:*\n"+"\n".join(errs[:5])
        if len(errs)>5: msg+="\n..."
    await u.message.reply_text(msg,parse_mode=MD)

async def cu(u,c):
    add_user(u.effective_user)
    if not is_admin(u.effective_user):
        await u.message.reply_text("⛔ Admin.")
        return
    d=load_users()
    t=f"👥 *Tổng user:* {len(d)}\n\n*10 user gần đây:*\n"
    for x in list(d.values())[-10:]:
        t+=f"• `{x.get('id')}` — {(x.get('name') or '?')}\n"
    await u.message.reply_text(t,parse_mode=MD)

async def pi(app):
    cmds=[
        BotCommand("start","Menu"),
        BotCommand("ref","Lưu mã ref GenPlay"),
        BotCommand("check","Lấy OTP")]
    await app.bot.set_my_commands(cmds)
    await app.bot.set_chat_menu_button(menu_button=MenuButtonCommands())

def main():
    print("[*] Bot chạy — clean UI mode")
    b=Application.builder().token(TK)
    app=b.post_init(pi).build()
    app.add_handler(CommandHandler("start",cs))
    app.add_handler(CommandHandler("ref",cref))
    app.add_handler(CommandHandler("check",ccheck))
    app.add_handler(CommandHandler("buffkc",cbuffkc))
    app.add_handler(CommandHandler("proxy",cproxy))
    app.add_handler(CommandHandler("thongbao",ctb))
    app.add_handler(CommandHandler("users",cu))
    app.add_handler(CallbackQueryHandler(cb_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg_handler))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__=="__main__": main()
