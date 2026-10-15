from pathlib import Path
p=Path(__file__).parent
sections=[('一、加减法热身', ['9+6', '17+7', '13-7', '16-9', '28+34', '45+27']), ('二、减法练习（可以列竖式）', ['54-28', '70-43', '100-26', '100-48']), ('三、乘法口诀', ['3*9', '4*7', '8*6', '7*8']), ('四、乘加、乘减', ['23+6*6', '60-7*4'])]
for key in [False,True]:
 s='''<!doctype html><meta charset="utf-8"><style>@page{size:A4;margin:15mm}body{font-family:"Noto Sans CJK SC",sans-serif;color:#111}h1{text-align:center;font-size:24px}h2{font-size:17px;margin-top:24px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px 35px}.q{font-size:21px;height:38px}.meta{font-size:14px;line-height:2}.foot{font-size:13px;margin-top:35px}</style><h1>口算小练 · 10月15日'''+(' · 参考答案' if key else '')+'</h1><div class="meta">姓名：____________　日期：____________<br>共16题｜先不计时，可以写中间过程。</div>'
 n=0
 for title,es in sections:
  s+='<h2>'+title+'</h2><div class="grid">'
  for e in es:
   n+=1;a=eval(e);assert 0<=a<=100
   s+='<div class="q">'+str(n)+'. '+e.replace('*','×').replace('-','－').replace('+','＋')+'＝'+(str(a) if key else '______')+'</div>'
  s+='</div>'
 s+='<div class="foot">'+('家长记录：独立完成／想得慢／提示后完成，请分开记录。' if key else '自查：□ 进位、退位　□ 减法顺序　□ 混合运算顺序')+'</div>'
 (p/('answer-key.html' if key else 'worksheet.html')).write_text(s)
