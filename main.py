import json as j,os,urllib.request as u
U=os.environ['MAKEFUN_ENV_URL']
post=lambda p,b:j.load(u.urlopen(U+p,j.dumps(b).encode()))
V=[0,100,320,330,500,900,0]
P=['',b'KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKK',b'ACEECGKLELMNEKNOELNOEKMNCGKKACEE',0,0,0,b'OQMKOOKKIGGGGEECECCAECCAECCAECCA']
J=[-33,-31,-18,-14,14,18,31,33];D=[-17,-15,15,17];R=[-16,-1,1,16];O=(0,0,J,D,R,D+R,D+R)
M=9e3;BD=15e4;N=0;S=[];TT={};A=Exception
def val(p,s):
 t=p%6 or 6;q=s if p<7 else s^112;return(V[t]+((P[t][(q>>4)*4+min(q&7,~q&7)]if t in(1,2,6)else 75)-75)*5)*((p<7)*2-1)
hb=lambda:bytes(B+[T&255])
def att(s,b):
 q=7-6*(b>0)
 for d in J+D+R:
  x=s+d;p=0 if x&136 else B[x]
  if p==q+1 and d in J or p==q+5 or p==q and d*b in(-15,-17):return 1
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
 m=[]
 for f,p in enumerate(B):
  if not p or(p<7)^(T>0):continue
  t=p%6 or 6
  if t==1:
   d=16*T;x=f+d;r=7*(T>0)
   if not x&136 and not B[x]:
    if x>>4==r:m.append(f|(x<<7)|(5<<14))
    elif not z:m.append(f|(x<<7));f>>4==1+5*(T<0)and not B[f+2*d]and m.append(f|((f+2*d)<<7))
   for x in(f+d-1,f+d+1):
    if not x&136 and(x==E or B[x]and(B[x]<7)^(T>0)):m+=[f|(x<<7)|(5<<14)]if x>>4==r else[f|(x<<7)]
  else:
   for d in O[t]:
    x=f+d
    while not x&136:
     if B[x]:(B[x]<7)^(T>0)and m.append(f|(x<<7));break
     elif not z:m.append(f|(x<<7))
     if t%4==2:break
     x+=d
 if not z:
  for b,ks,ts in((1,4,6),(2,4,2),(4,116,118),(8,116,114)):
   es=(ks+1,ks+2)if ts>ks else(ks-3,ks-2,ks-1)
   if C&b and(T>0)==(b<4)and not any(B[x]for x in es)and not any(att(x,-T)for x in(ks,(ks+ts)//2,ts)):m.append(ks|(ts<<7))
 return m
def mk(m):
 global T,C,E,WK,BK,SC;S.append((B[:],C,E,WK,BK,T,SC))
 f=m&127;t=m>>7&127;q=m>>14&7;p=B[f];cap=B[t];cs=t
 if p%6==1 and t==E and not cap:cs=t-16*T;cap=B[cs];B[cs]=0
 np=q+6*(T<0)if q else p;SC+=val(np,t)-val(p,f);B[t]=np;B[f]=0
 if cap:SC-=val(cap,cs)
 if p%6==0 and abs(t-f)==2:u=t+1 if t>f else t-2;v=u-2 if t>f else u+3;B[v]=B[u];B[u]=0;SC+=val(B[v],v)-val(B[v],u)
 if p==6:WK=t;C&=~3
 elif p==12:BK=t;C&=~12
 for s,b in((0,2),(7,1),(112,8),(119,4)):
  if s in(f,t):C&=~b
 E=f+16*T if p%6==1 and t-f==32*T else-1;T=-T
def un():
 global T,C,E,WK,BK,SC;B[:],C,E,WK,BK,T,SC=S.pop()
od=lambda ms,tm:ms.sort(key=lambda m:2e4 if m==tm else 1e4+10*V[B[m>>7&127]%6 or 6]-V[B[m&127]%6 or 6]if B[m>>7&127]else 0,reverse=1)
def qs(a,b,pl):
 global N;N+=1
 if N>BD:raise A
 s=SC*T;ic=att(WK if T>0 else BK,-T)
 if not ic:
  if s>=b:return b
  if s>a:a=s
 ms=gen(0)if ic else gen(1);od(ms,0);n=0
 for m in ms:
  if not lg(m):continue
  n+=1;v=-qs(-b,-a,pl+1);un()
  if v>=b:return b
  a=max(a,v)
 if ic and not n:return-M+pl
 return a
def sr(d,a,b,pl):
 global N;N+=1
 if N>BD:raise A
 ic=att(WK if T>0 else BK,-T)
 if d<1:return qs(a,b,pl)
 h=hb();e=TT.get(h)
 if e and e[0]>=d:return e[1]
 ms=gen(0);od(ms,e[2]if e else 0);n=0;bm=0
 for m in ms:
  if not lg(m):continue
  n+=1;v=-sr(d-1,-b,-a,pl+1);un()
  if v>a:a=v;bm=m
  if a>=b:break
 if not n:return-M+pl if ic else 0
 if bm and a<b:TT[h]=(d,a,bm)
 return a
def uci(m):
 f=m&127;t=m>>7&127;q=m>>14&7;return chr(97+f%8)+str(f//16+1)+chr(97+t%8)+str(t//16+1)+(q and'q'or'')
def parse(fen):
 global B,T,C,E,WK,BK,SC;w=fen.split();B=[0]*128;s=112;SC=0
 for ch in w[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   c='PNBRQKpnbrqk'.index(ch)+1;B[s]=c;SC+=val(c,s)
   if c==6:WK=s
   elif c==12:BK=s
   s+=1
 T=1 if w[1]=='w'else-1;C=sum(1<<'KQkq'.find(ch)for ch in w[2]if ch!='-');E=ord(w[3][0])-97+(int(w[3][1])-1)*16 if w[3]!='-'else-1
def choose(legal):
 global N;ms=[m for m in gen(0)if uci(m)in legal];N=0;bm=ms[0]
 try:
  for d in range(8):
   a=-M;od(ms,bm)
   for m in ms:
    if not lg(m):continue
    v=-sr(d,-M,-a,1);un()
    if v>a:a=v;bm=m
 except A:pass
 return uci(bm)
while 1:
 g=post('/game',{})
 if g['status'][0]=='d':break
 while g['status'][0]=='y':parse(g['fen']);g=post('/move',{'game':g['game'],'move':choose(g['legal_moves'])})