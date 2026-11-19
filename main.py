import json as j,os,urllib.request as u
U=os.environ['MAKEFUN_ENV_URL']
post=lambda p,b:j.load(u.urlopen(U+p,j.dumps(b).encode()))
V=[0,100,320,330,500,900,0]
P=['',b'KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKK',b'ACEECGKLELMNEKNOELNOEKMNCGKKACEE',0,0,0,b'OQMKOOKKIGGGGEECECCAECCAECCAECCA']
J=[-33,-31,-18,-14,14,18,31,33];D=[-17,-15,15,17];R=[-16,-1,1,16];O=(J,D,R,D+R,D+R)
M=9e3;BD=15e4;N=0;S=[];TT={};A=Exception
def val(p,s):
 t=p%6 or 6;q=s^112*(p>6);return(V[t]+((P[t]and P[t][(q>>4)*4+min(q&7,~q&7)]or 75)-75)*5)*((p<7)*2-1)
def att(s,b):
 q=7-6*(b>0)
 for d in J+D+R:
  x=s+d;p=B[x]if not x&136 else 0
  if p-q in(1,5)and(d in J)==(p-q==1)or p==q and d*b in(-15,-17):return 1
 for d in D+R:
  x=s+d
  while not x&136:
   if(p:=B[x])and(p==q+4 or p==(q+2 if d in D else q+3)):return 1
   if p:break
   x+=d
 return 0
def lg(m):
 mk(m)
 if att(WK if T<0 else BK,T):un();return 0
 return 1
def gen(z):
 m=[];ap=m.append;w=T>0
 for f,p in enumerate(B):
  if not p or(p<7)^w:continue
  t=p%6 or 6
  if t==1:
   d=16*T;x=f+d;r=7*w;pb=(x>>4==r)*81920
   if not x&136 and not B[x]:
    if pb:ap(f|(x<<7)|pb)
    elif not z:ap(f|(x<<7));f>>4==6-5*w and not B[f+2*d]and ap(f|((f+2*d)<<7))
   for x in(f+d-1,f+d+1):
    if not x&136 and(x==E or B[x]and(B[x]<7)^w):ap(f|(x<<7)|pb)
  else:
   for d in O[t-2]:
    x=f+d
    while not x&136:
     if B[x]:(B[x]<7)^w and ap(f|(x<<7));break
     elif not z:ap(f|(x<<7))
     if t%4==2:break
     x+=d
 if not z:
  for b,ks,ts,es in((1,4,6,(5,6)),(2,4,2,(1,2,3)),(4,116,118,(117,118)),(8,116,114,(113,114,115))):
   if C&b and w==(b<4)and not any(B[x]for x in es)and not any(att(x,-T)for x in(ks,(ks+ts)//2,ts)):ap(ks|(ts<<7))
 return m
def mk(m):
 global T,C,E,WK,BK,SC;S.append((B[:],C,E,WK,BK,T,SC))
 if not m:E=-1;T=-T;return
 f=m&127;t=m>>7&127;q=m>>14&7;p=B[f];cap=B[t];cs=t
 if p%6==1 and t==E and not cap:cs=t-16*T;cap=B[cs];B[cs]=0
 np=q+3-3*T if q else p;SC+=val(np,t)-val(p,f);B[t]=np;B[f]=0
 if cap:SC-=val(cap,cs)
 if p%6==0 and abs(t-f)==2:u,v=(t+1,t-1)if t>f else(t-2,t+1);B[v]=B[u];B[u]=0;SC+=val(B[v],v)-val(B[v],u)
 if p==6:WK=t;C&=~3
 elif p==12:BK=t;C&=~12
 for s,b in((0,2),(7,1),(112,8),(119,4)):C&=~b if s in(f,t)else C
 E=f+16*T if p%6==1 and t-f==32*T else-1;T=-T
def un():
 global T,C,E,WK,BK,SC;B[:],C,E,WK,BK,T,SC=S.pop()
od=lambda ms,tm:ms.sort(key=lambda m:1e4 if m==tm else 10*V[B[m>>7&127]%6 or 6]-V[B[m&127]%6 or 6]if B[m>>7&127]else 0,reverse=1)
def sr(d,a,b):
 global N;N+=1
 if N>BD:raise A
 ic=att(WK if T>0 else BK,-T);d+=ic
 if d<1:
  s=SC*T
  if s>=b:return b
  if s>a:a=s
  ms=gen(1);od(ms,0)
  for m in ms:
   if not lg(m):continue
   v=-sr(0,-b,-a);un()
   if v>=b:return b
   a=max(a,v)
  return a
 h=(bytes(B),T,C,E);e=TT.get(h)
 if e and e[0]>=d and(e[1]==0 or e[1]==1 and e[2]>=b or e[1]==2 and e[2]<=a):return e[2]
 if d>2 and not ic and SC*T>=b:
  mk(0);v=-sr(d-3,-b,-b+1);un()
  if v>=b:return b
 ms=gen(0);od(ms,e[3]if e else 0);n=0;bm=0
 for m in ms:
  t=m>>7&127;cap=B[t]
  if not lg(m):continue
  n+=1
  r=d>2 and n>3 and not ic and not cap and m<16384
  v=-sr(d-1-r,-b if n==1 else-a-1,-a)
  if n>1 and v>a and(r or v<b):v=-sr(d-1,-b,-a)
  un()
  if v>a:a=v;bm=m
  if a>=b:break
 if not n:return-M+len(S) if ic else 0
 TT[h]=(d,(a>=b)+2*(bm==0),a,bm)
 return a
uci=lambda m:chr(97+m%8)+str((m&127)//16+1)+chr(97+(m>>7)%8)+str((m>>7&127)//16+1)+'q'*(m>16383)
while 1:
 g=post('/game',{});TT.clear()
 if g['status'][0]=='d':break
 while g['status'][0]=='y':
  S=[];w=g['fen'].split();B=[0]*128;s=112;SC=0
  for ch in w[0]:
   if ch=='/':s-=24
   elif ch.isdigit():s+=int(ch)
   else:
    c='PNBRQKpnbrqk'.index(ch)+1;B[s]=c;SC+=val(c,s);s+=1
    if c==6:WK=s-1
    elif c==12:BK=s-1
  T=1-2*(w[1]!='w');C=sum(1<<'KQkq'.find(ch)for ch in w[2]if ch!='-');E=ord(w[3][0])-97+(int(w[3][1])-1)*16 if w[3]!='-'else-1
  ms=[m for m in gen(0)if uci(m)in g['legal_moves']];N=0;bm=ms[0]
  try:
   for d in range(1,13):
    a=-M;od(ms,bm);cb=bm
    for m in ms:
     if not lg(m):continue
     v=-sr(d-1,-M,-a);un()
     if v>a:a=v;cb=m
    bm=cb
  except A:pass
  g=post('/move',{'game':g['game'],'move':uci(bm)})
