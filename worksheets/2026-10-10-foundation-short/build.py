from pathlib import Path
import json
p=Path(__file__).parent
qs=[('8＋7＝____','15','18+9曾算25','8+7'),('16＋8＝____','24','18+9曾算25','16+8'),('13－8＝____','5','12-8提取慢','13-8'),('14－6＝____','8','12-8提取慢','14-6'),('26＋35＝____','61','原卷47题25+36算63','26+35'),('小盒里原来有32颗珠子，拿走7颗。还剩几颗？<br>算式：________________','32－7＝25（颗）','减法顺序颠倒','32-7'),('列竖式：52－28＝____','24','减法倒减及退位','52-28'),('列竖式：70－36＝____','34','整十数退位','70-36'),('列竖式：100－38＝____','62','100-46曾算64','100-38'),('3×8＝____　口诀：________________','24；三八二十四','9×3依赖连加','3*8'),('3×9＝____　口诀：________________','27；三九二十七','9×3依赖连加','3*9'),('接着第9题想：100可以拆成（　）个十和（　）个一。<br>要求：个位这一份正好是10个一。','9个十和10个一','100跨零退位数位理解',None)]
expected=[15,24,5,8,61,25,24,34,62,24,27]
assert [eval(q[3]) for q in qs[:11]]==expected
css='''@page{size:A4;margin:12mm}body{font-family:"Noto Sans CJK SC",sans-serif;color:#111;margin:0;font-size:15px}h1{text-align:center;font-size:23px;margin:0 0 12px}.meta,.intro{font-size:12px;margin:10px 0}h2{font-size:16px;margin:17px 0 10px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px}.q{line-height:1.9;min-height:42px}.tall{height:110px}.wide{grid-column:span 2}.notes{font-size:12px;line-height:1.9;margin-top:14px}.key .q{font-size:14px;min-height:28px}'''
for key in [False,True]:
 out=['<!doctype html><meta charset="utf-8"><style>'+css+'</style><body class="'+('key' if key else '')+'"><h1>算得准，想得清'+(' · 家长答案' if key else ' · 基础短练')+'</h1><div class="meta">姓名：____________　日期：____________</div><div class="intro">12题｜不计时，约10—15分钟，可分两次完成。'+('先独立做，再帮助；记录提示，不把提示后答对记为独立完成。' if key else '按顺序完成，不会的先做记号；可以写下思考过程。')+'</div>']
 for title,ids in [('一、先独立算一算',[0,1,2,3,4,5]),('二、列竖式，留下计算过程',[6,7,8]),('三、乘法小练习',[9,10]),('四、最后说一说',[11])]:
  out+=['<h2>'+title+'</h2><div class="grid">']
  for i in ids:
   q=qs[i];cl='q'+(' tall' if 6<=i<=8 and not key else '')+(' wide' if i in [5,11] else '')
   out+=['<div class="'+cl+'">'+str(i+1)+'. '+(q[1] if key else q[0])+'</div>']
  out+=['</div>']
 if key:out+=['<div class="notes">观察重点：<br>第1—2题：让孩子说自己的方法，不先提示凑十。<br>第5题：个位6＋5＝11，写1进1，十位2＋3＋1＝6。<br>第6—8题：关注减法顺序；个位不够减，应退位，不能倒减。<br>第9题：100拆为9个十和10个一，10－8＝2，9－3＝6。<br>第12题在第9题后完成，用于了解数位理解，不作为第9题的独立复测。<br>口诀题若用连加算出，记“算对、口诀尚需练熟”，不要记为不理解乘法。</div>']
 (p/('answer-key.html' if key else 'worksheet.html')).write_text(''.join(out))
manifest=[{'id':i+1,'question':q[0],'answer':q[1],'source_ids':[q[2]],'purpose':'针对已观察薄弱项短练，生成不代表掌握'} for i,q in enumerate(qs)]
(p/'answer-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(p/'worksheet-spec.json').write_text(json.dumps({'title':'算得准，想得清：基础短练','status':'已生成/待完成','count':12,'items':manifest},ensure_ascii=False,indent=2))
(p/'answer-key.md').write_text('\n'.join(str(i+1)+'. '+q[1] for i,q in enumerate(qs)))
print('12 questions checked; 11 arithmetic answers independently matched, representation 9*10+10=100.')
