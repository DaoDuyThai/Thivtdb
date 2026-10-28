# -*- coding: utf-8 -*-
"""Tra đáp án theo nội dung câu hỏi (kể cả khi đề xáo A-D).
  py tools/tra_cuu.py "nội dung câu hỏi (+ các đáp án nếu có)"     hoặc   echo ... | py tools/tra_cuu.py -
In top 3 câu gần nhất kèm NỘI DUNG đáp án đúng; nếu bank không có đáp án sẽ báo 'CHƯA CÓ ĐÁP ÁN'."""
import sys, json, re, difflib, os
sys.stdout.reconfigure(encoding='utf-8')
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')
def norm(s): return re.sub(r'[^\w]+',' ',s.lower()).strip()
def load():
    items=[]
    for x in json.load(open(D+'/pl400.json',encoding='utf-8')):
        items.append(dict(src=f"PL-{x['n']} (Pháp luật 400)",text=x['q']+' '+' '.join(x['opts'].values()),q=x['q'],ans=x['ans'],anstxt=x['opts'].get(x['ans'][0],''),note=x['expl']))
    for x in json.load(open(D+'/kt196.json',encoding='utf-8')):
        items.append(dict(src=f"KT-{x['n']} (Khai thác 196)",text=x['q']+' '+' '.join(x['opts'].values()),q=x['q'],ans=x['ans'],anstxt=x['opts'].get(x['ans'],''),note=''))
    S=json.load(open(D+'/tk_sets.json',encoding='utf-8'))
    AN=json.load(open(D+'/tk_answers.json',encoding='utf-8'))
    for nm in ('A','B','C','D1','D2'):
        for b in S[nm]:
            full=b['head']+' '+' '.join(b['lines'])
            v=AN[nm].get(str(b['n'])) or {}
            ans=v.get('ans'); note=('⚠ ĐỘ CHẮC CHẮN THẤP. ' if v.get('low') else '')+v.get('note','')
            at=''
            if ans and len(ans)==1:
                if nm in('D1','D2'):
                    opts=b['lines'][:4]; i=ord(ans)-65; at=opts[i] if i<len(opts) else ''
                else:
                    at=(b.get('opts') or {}).get(ans,'')
                    if not at:
                        for ln in b['lines']:
                            if ln.strip()[:2].upper()==ans+'.' or ln.strip()[:2].upper()==ans+')': at=ln.strip(); break
                        if not at and b['lines'][:4]: i=ord(ans)-65; at=b['lines'][i] if i<4 and i<len(b['lines']) else ''
            items.append(dict(src=f"TK-{nm}-{b['n']} (Thống kê)",text=full,q=b['head'],ans=ans,anstxt=at,note=note))
    return items
def main():
    q=' '.join(sys.argv[1:]) if len(sys.argv)>1 and sys.argv[1]!='-' else sys.stdin.read()
    nq=norm(q); items=load()
    sc=sorted(((difflib.SequenceMatcher(None,nq,norm(i['text'])).ratio()+ (0.5 if nq[:60] in norm(i['text']) else 0),i) for i in items),key=lambda t:-t[0])[:3]
    for s,i in sc:
        print(f"\n[{s:.2f}] {i['src']}\n  Hỏi: {i['q'][:160]}")
        print(f"  => ĐÁP ÁN: {i['ans']} — {i['anstxt']}" if i['ans'] else '  => CHƯA CÓ ĐÁP ÁN trong tài liệu')
        if i['note']: print('  Giải thích:',i['note'][:300])
    print('\n(Nhớ: đề thật có thể xáo A-D → chọn theo NỘI DUNG đáp án ở trên.)')
main()
