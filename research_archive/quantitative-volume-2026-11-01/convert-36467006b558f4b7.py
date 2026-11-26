from pathlib import Path
import json,re,subprocess,hashlib,copy
ROOT=Path('/private/tmp/murakamis_dream-publication')
OUT=Path('/private/tmp/md-quantitative-appendices')
PANDOC='/opt/homebrew/bin/pandoc'
specs=[
 ('actual_all_circle_curvature_filling_limit.md','qe','Finite sums under the degree and twist criterion','E'),
 ('all_circle_uniform_newton_bounds.md','qu','Uniform Newton bounds with explicit constants','E'),
 ('actual_all_circle_octahedral_decomposition.md','ft','The ordered octahedral decomposition','F'),
 ('actual_all_circle_angular_octahedra.md','fa','Positive angular coordinates on each edge block','F'),
 ('actual_all_circle_geometric_completion.md','fg','Completing the actual fillings and calibrating volume','F'),
 ('actual_all_circle_preferred_cusp.md','fc','The preferred cusp along the filling path','F'),
]
notes={name:(prefix,title,app) for name,prefix,title,app in specs}
def pandoc(data,frm,to):
 p=subprocess.run([PANDOC,'--from='+frm,'--to='+to,'--wrap=none'],input=data,text=True,capture_output=True,check=True)
 if p.stderr: (OUT/'pandoc-warnings.txt').open('a').write(p.stderr)
 return p.stdout
parsed={name:json.loads(pandoc((ROOT/'notes'/name).read_text(),'markdown+tex_math_single_backslash+tex_math_dollars','json')) for name,*_ in specs}
api=next(iter(parsed.values()))['pandoc-api-version']
def render(inlines):
 return pandoc(json.dumps({'pandoc-api-version':api,'meta':{},'blocks':[{'t':'Plain','c':inlines}]}),'json','latex').strip()
def rawinline(x):return {'t':'RawInline','c':['latex',x]}
def rawblock(x):return {'t':'RawBlock','c':['latex',x]}
def collect(node,key):
 if isinstance(node,dict):
  if node.get('t')==key:yield node
  for x in node.values():yield from collect(x,key)
 elif isinstance(node,list):
  for x in node:yield from collect(x,key)
def header_text(h):return ''.join(x['c'] if x['t']=='Str' else ' ' if x['t']=='Space' else '' for x in h['c'][2])
sections={}
for name,prefix,_,_ in specs:
 for h in collect(parsed[name]['blocks'],'Header'):
  txt=header_text(h); m=re.match(r'(\d+)\.\s*',txt)
  if h['c'][0]==2 and m: sections[name,int(m.group(1))]=f'sec:{prefix}-{m.group(1)}'
# These paragraphs explicitly refer to equation numbers in other notes.
foreign_phrases={
 'actual_all_circle_octahedral_decomposition.md':['relevant moves','original proof of these primitive words'],
 'actual_all_circle_angular_octahedra.md':['These are the actual maps of'],
 'actual_all_circle_preferred_cusp.md':['joint-wire Legendre identity is','Let \\(L_{\\mathrm{path}}\\)'],
}
manifest={}; outputs={'E':[],'F':[]}
for name,prefix,title,app in specs:
 doc=parsed[name]; original_math=[n['c'][1] for n in collect(doc['blocks'],'Math')]
 tags=set(re.findall(r'\\tag\{([^}]+)\}','\n'.join(original_math)))
 localnums={n for f,n in sections if f==name}
 def transform_inlines(items,protect=False):
  ans=[]
  for item in items:
   t=item.get('t'); c=item.get('c')
   if t=='Math' and c[0]['t']=='DisplayMath':
    found=re.search(r'\\tag\{([^}]+)\}',c[1]); body=c[1]
    if found:
     tag=found.group(1); body=re.sub(r'\\tag\{[^}]+\}','',body).strip()
     ans.append(rawinline('\\begin{equation}\n'+body+'\n\\label{eq:'+prefix+'-'+tag+'}\n\\end{equation}'))
    else:ans.append(item)
   elif t=='Str' and not protect:
    last=0
    for m in re.finditer(r'\(([0-9]+[a-z]?)\)',c):
     if m.group(1) not in tags:continue
     if m.start()>last:ans.append({'t':'Str','c':c[last:m.start()]})
     ans.append(rawinline(r'\eqref{eq:'+prefix+'-'+m.group(1)+'}')); last=m.end()
    if last: 
     if last<len(c):ans.append({'t':'Str','c':c[last:]})
    else:ans.append(item)
   elif t=='Link':
    attrs,label,target=c; url=target[0]; base=url.split('#')[0]
    if base in notes:
     targetprefix=notes[base][0]; ans.append(rawinline(r'\hyperref[sec:'+targetprefix+']{'+render(label)+'}'))
    elif base=='actual_all_circle_quantitative_volume.md':ans.append(rawinline(r'\hyperref[ch:quantitative-circle-trees]{'+render(label)+'}'))
    else:
     if url.endswith('.md') or '.md#' in url:
      url='https://sashakolpakov.github.io/murakamis_dream/notes/'+url.replace('.md','.html')
     elif url.startswith('../'):
      url='https://sashakolpakov.github.io/murakamis_dream/'+url[3:]
     ans.append({'t':'Link','c':[attrs,label,[url,target[1]]]})
   elif t in ('Emph','Strong','SmallCaps','Strikeout','Superscript','Subscript'):
    ans.append({'t':t,'c':transform_inlines(c,protect)})
   else:ans.append(item)
  return ans
 def block(b):
  t=b.get('t');c=b.get('c')
  if t=='Header':
   level,attrs,inlines=c
   if level==1:return None
   txt=render(inlines); mm=re.match(r'(\d+)\.\s*',txt)
   num=mm.group(1) if mm else 'reproduction'
   txt=re.sub(r'^\d+\.\s*','',txt)
   cmd={2:'subsection',3:'subsubsection',4:'paragraph'}.get(level,'paragraph')
   return rawblock('\\'+cmd+'{'+txt+'}\\label{sec:'+prefix+'-'+num+'}')
  if t in ('Para','Plain'):
   txt=render(c)
   if txt.strip()=='1 November 2026.':return None
   protect=any(x in txt for x in foreign_phrases.get(name,[]))
   has_link=bool(list(collect(c,'Link')))
   transformed=transform_inlines(c,protect)
   tex=render(transformed)
   if not has_link:
    # Only local prose references; math expressions are left untouched.
    def sec(m):
     word=m.group(1);seq=m.group(2)
     seq=re.sub(r'\b\d+\b',lambda q:r'\ref{'+sections[(name,int(q.group()))]+'}' if int(q.group()) in localnums else q.group(),seq)
     return word+'~'+seq
    tex=re.sub(r'\b(Sections?|sections?)\s+(\d+(?:(?:--|–|\s+and\s+|,\s*)\d+)*)',sec,tex)
   tex=tex.replace('This note proves','This section proves').replace('This note gives','This section gives').replace('This\nnote identifies','This section identifies')
   return rawblock(tex)
  if t=='CodeBlock':return rawblock('\\begin{verbatim}\n'+c[1]+'\n\\end{verbatim}')
  if t=='BulletList':return {'t':t,'c':[[y for x in li if (y:=block(x)) is not None] for li in c]}
  if t=='OrderedList':return {'t':t,'c':[c[0],[[y for x in li if (y:=block(x)) is not None] for li in c[1]]]}
  if t=='BlockQuote':return {'t':t,'c':[y for x in c if (y:=block(x)) is not None]}
  return b
 blocks=[y for x in doc['blocks'] if (y:=block(x)) is not None]
 tex=pandoc(json.dumps({'pandoc-api-version':api,'meta':{},'blocks':blocks}),'json','latex').replace('\\tightlist','')
 # Include the original note only as an optional source reference.
 prefixtext='\\section{'+title+'}\\label{sec:'+prefix+'}\n\n'
 prefixtext+='The separately available version of this section is \\href{https://sashakolpakov.github.io/murakamis_dream/notes/'+name.replace('.md','.html')+'}{'+title.lower()+'}. The proof is reproduced here in full.\n\n'
 out=prefixtext+tex
 (OUT/(prefix+'.tex')).write_text(out)
 outputs[app].append(out)
 manifest[name]={'sha256':hashlib.sha256((ROOT/'notes'/name).read_bytes()).hexdigest(),'display_count':sum(n['c'][0]['t']=='DisplayMath' for n in collect(doc['blocks'],'Math')),'math_count':len(original_math),'tags':sorted(tags),'prefix':prefix}
(OUT/'converted-E.tex').write_text('\n\n'.join(outputs['E']))
(OUT/'converted-F.tex').write_text('\n\n'.join(outputs['F']))
(OUT/'conversion-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
