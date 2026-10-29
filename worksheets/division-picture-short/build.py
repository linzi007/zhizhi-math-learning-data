from pathlib import Path
p=Path(__file__).parent
css='@page{size:A4;margin:14mm}body{font-family:"Noto Sans CJK SC";font-size:16px;line-height:1.7}h1{text-align:center;font-size:23px}h2{font-size:17px;margin:15px 0 7px}.space{height:48px}.note{font-size:12px}.g{display:inline-block;border:1px solid;padding:5px 9px;border-radius:12px;margin:4px}'
questions=[('1. 有12颗珠子，平均放进4个盒子，每盒放几颗？','画图表示，再列式解答。'),('2. 有12颗珠子，每个盒子放4颗，需要几个盒子？','画图表示，再列式解答。'),('3. 上面两题中的“3”分别表示什么？','第1题：________________　　第2题：________________'),('4. 看图，用一道乘加和一道乘减算式求圆点总数。',''.join('<span class="g">'+'●'*n+'</span>' for n in [4,4,4,3])+'<br>乘加：________________　乘减：________________'),('5. 每个沙包3元，每把水枪4元。','请提出一个用除法解决的问题，并列式解答。'),('6. 两包同样的彩纸，甲包18元，乙包15元。买哪包更省钱？少花多少元？','算式和答句：')]
s='<meta charset="utf-8"><style>'+css+'</style><h1>分得清，看得懂 · 考前短练</h1><div class="note">姓名：____________　日期：____________<br>共6题｜约15分钟｜先独立完成，可以画图。完成后检查得数、单位和答句。</div>'
for title,desc in questions:s+='<h2>'+title+'</h2><div>'+desc+'</div><div class="space"></div>'
p.joinpath('worksheet.html').write_text(s)
ans=['12÷4＝3（颗）。画4组，每组3颗。','12÷4＝3（个）。每4颗一组，画3组。','第1题：每盒3颗珠子；第2题：需要3个盒子。','4×3＋3＝15（个）；4×4－1＝15（个）。先当作4组4个，多算1个，减去1。','示例：12元可以买几把水枪？12÷4＝3（把）。其他条件充分、符合价格且在1—6口诀范围内的除法问题也可。','乙包更省钱，18－15＝3（元），少花3元。']
p.joinpath('answer-key.html').write_text('<meta charset="utf-8"><style>'+css+'</style><h1>考前短练 · 家长答案</h1>'+''.join('<h2>第'+str(i+1)+'题</h2><p>'+a+'</p>' for i,a in enumerate(ans))+'<p>先让孩子独立做，再询问每个数表示什么。提示后完成请注明。画图分组结构比图形是否美观重要；不能仅凭得数正确判定理解。</p>')
import json
p.joinpath('answer-manifest.json').write_text(json.dumps([{'id':i+1,'question':q,'answer':a,'source':'期中卷除法含义、乘减图示、自编除法及差额错误','status':'已生成/待完成'} for i,(q,a) in enumerate(zip(questions,ans))],ensure_ascii=False,indent=2))
