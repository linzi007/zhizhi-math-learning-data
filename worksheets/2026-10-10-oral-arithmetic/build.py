from pathlib import Path
import json,html
p=Path(__file__).parent
sections=[('一、100以内加减法',['36+27','72-38','45+19','80-26','28+35','91-47','56+18','63-29','47+26','70-34','18+46','85-39','39+24','62-27','26+58','100-46']),('二、乘法口诀',['3*4','6*5','7*2','8*3','4*6','9*2','5*7','6*6','8*4','7*6','9*3','8*7','9*5','7*7','8*8','9*9']),('三、乘法和加减法混合',['3*4+8','5*6-9','7+4*5','40-6*4','2*8+15','7*3-6','18+5*4','60-7*6','6*5+27','8*4-18','16+9*3','70-8*7','7*7+14','9*5-26','25+6*6','90-9*8'])]
items=[]
for title,exprs in sections:
 for e in exprs:
  a=eval(e,{'__builtins__':{}}); assert 0<=a<=100
  items.append({'id':len(items)+1,'concept':title,'expression':e,'answer':a,'source':'用户指定范围原创'})
assert len(items)==48 and len({i['expression'] for i in items})==48
css='''@page{size:A4;margin:12mm}*{box-sizing:border-box}body{font-family:"Noto Sans CJK SC",sans-serif;margin:0;color:#111}h1{text-align:center;font-size:22px;margin:0 0 10px}.meta{font-size:13px;margin-bottom:12px}.note{font-size:12px;padding:8px;border:1px solid #aaa}h2{font-size:16px;margin:20px 0 10px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0 10px}.q{font-size:17px;height:40px;white-space:nowrap}.num{font-size:10px;color:#555;margin-right:4px}.foot{font-size:12px;margin-top:20px}'''
for key in [False,True]:
 out=['<!doctype html><meta charset="utf-8"><style>'+css+'</style><h1>二年级口算练习'+(' · 答案' if key else '')+'</h1><div class="meta">姓名：____________　日期：____________　用时：________</div><div class="note">共48题｜建议15—20分钟｜'+('与学生卷题号一一对应。' if key else '先算乘法，再算加减法；做完检查进位和退位。')+'</div>']
 for title,_ in sections:
  out+=['<h2>'+title+'（16题）</h2><div class="grid">']
  for i in items:
   if i['concept']!=title:continue
   e=i['expression'].replace('*','×').replace('-','−').replace('+','＋')
   out+=['<div class="q"><span class="num">'+str(i['id'])+'.</span>'+e+'＝'+(str(i['answer']) if key else '___')+'</div>']
  out+=['</div>']
 out+=['<div class="foot">'+('混合运算：先求乘积，再完成加法或减法。' if key else '自查：□ 进位、退位　□ 乘法口诀　□ 先乘后加减')+'</div>']
 (p/('answer-key.html' if key else 'worksheet.html')).write_text(''.join(out))
(p/'answer-manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
(p/'worksheet-spec.json').write_text(json.dumps({'title':'二年级口算练习','status':'已生成/待完成','language':'zh-CN','sections':sections,'count':48},ensure_ascii=False,indent=2))
(p/'answer-key.md').write_text('# 参考答案\n\n'+'\n'.join(f"{i['id']}. {i['expression']} = {i['answer']}" for i in items))
print('Verified 48 unique expressions; all answers in 0–100.')
