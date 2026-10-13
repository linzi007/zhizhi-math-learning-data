from pathlib import Path
p=Path(__file__).parent
sections=[('一、进位加法和退位减法',['8+6','9+7','17+8','18+6','12-7','15-8']),('二、100以内加减法',['27+35','46+18','43-17','60-24','80-46','100-57']),('三、乘法口诀',['3*9','8*4']),('四、乘加、乘减',['24+6*6','50-7*4'])]
for key in [False,True]:
 s='''<!doctype html><meta charset="utf-8"><style>@page{size:A4;margin:15mm}body{font-family:"Noto Sans CJK SC",sans-serif;color:#111}h1{text-align:center;font-size:24px}h2{font-size:17px;margin-top:24px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px 35px}.q{font-size:21px;height:30px}.meta{font-size:14px;line-height:2}.foot{font-size:13px;margin-top:35px}</style><h1>芝芝口算小练'''+(' · 参考答案' if key else '')+'</h1><div class="meta">姓名：____________　日期：____________<br>共16题｜先不计时，可以写中间过程。</div>'
 n=0
 for title,es in sections:
  s+='<h2>'+title+'</h2><div class="grid">'
  for e in es:
   n+=1;a=eval(e);assert 0<=a<=100
   s+='<div class="q">'+str(n)+'. '+e.replace('*','×').replace('-','－').replace('+','＋')+'＝'+(str(a) if key else '______')+'</div>'
  s+='</div>'
 s+='<div class="foot">'+('家长记录：独立完成／想得慢／提示后完成，请分开记录。' if key else '自查：□ 进位、退位　□ 减法顺序　□ 混合运算顺序')+'</div>'
 (p/('answer-key.html' if key else 'worksheet.html')).write_text(s)
