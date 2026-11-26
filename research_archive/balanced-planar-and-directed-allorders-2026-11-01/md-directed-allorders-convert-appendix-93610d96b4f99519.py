from pathlib import Path
import re,subprocess,json,hashlib
src=Path('/private/tmp/actual_all_circle_directed_all_orders.md')
s=src.read_text(); original=s
# Preserve external directed-equation references before rewriting local ones.
s=s.replace('equations (3), (8), and (9) of [the directed theorem](actual_all_circle_directed_volume.md)',r'equations \eqref{dk:eq-3}, \eqref{dk:eq-8}, and \eqref{dk:eq-9} of Appendix~\ref{app:directed-circle-messages}')
s=s.replace('directed equations (4)–(7)',r'equations \eqref{dk:eq-4}--\eqref{dk:eq-7} of Appendix~\ref{app:directed-circle-messages}')
for a,b in [('directed (25)–(26)',r'equations \eqref{dk:eq-25}--\eqref{dk:eq-26}'),('directed (43)',r'\eqref{dk:eq-43}'),('directed (24)',r'\eqref{dk:eq-24}'),('directed (28)',r'\eqref{dk:eq-28}'),('directed §§2–6',r'Sections~\ref{dk:sec-2}--\ref{dk:sec-6}'),('directed §7',r'Section~\ref{dk:sec-7}')]:s=s.replace(a,b)
# The five numbered dependency items refer entirely to the directed appendix.
a=s.index('1. Equations (N1)');b=s.index('\n\nThe [exact interpolation theorem]',a)
part=s[a:b]
part=re.sub(r'\((N[1-4]|\d+)\)',lambda m:r'\eqref{dk:eq-'+m.group(1)+'}',part)
s=s[:a]+part+s[b:]
# External numbered section references stay explicitly attached to their source.
s=s.replace('§10, fix','Section 10 of that source, fix').replace('§§2–4, fixes','Sections 2--4 of that source, fixes').replace('§§5–10, supplies','Sections 5--10 of that source, supplies').replace("with §5's complete filled-point anchor",'with its Section 5 complete filled-point anchor')
for a,b in [('§2–3',r'Sections~\ref{dao:sec-2}--\ref{dao:sec-3}'),('§§3–5',r'Sections~\ref{dao:sec-3}--\ref{dao:sec-5}')]:s=s.replace(a,b)
s=re.sub(r'§([1-9])(?![\d.])',lambda m:r'Section~\ref{dao:sec-'+m.group(1)+'}',s)
tags=re.findall(r'\\tag\{([^}]+)\}',s)
parts=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',s,flags=re.S)
for i in range(0,len(parts),2):
    for tag in sorted(tags,key=len,reverse=True):
        parts[i]=parts[i].replace('('+tag+')',r'\eqref{dao:eq-'+tag+'}')
s=''.join(parts)
def display(m):
 body=m.group(1);t=re.search(r'\\tag\{([^}]+)\}',body)
 if not t:return m.group(0)
 body=re.sub(r'\\tag\{[^}]+\}','',body).strip()
 return '\n'+r'\begin{equation}\label{dao:eq-'+t.group(1)+'}\n'+body+'\n'+r'\end{equation}'+'\n'
s=re.sub(r'\\\[(.*?)\\\]',display,s,flags=re.S)
s=re.sub(r'^# (.*)$',lambda m:r'\chapter{'+m.group(1)+'}'+ '\n'+r'\label{app:directed-all-orders}',s,flags=re.M)
s=re.sub(r'^## (\d+)\. (.*)$',lambda m:r'\section{'+m.group(2)+'}'+r'\label{dao:sec-'+m.group(1)+'}',s,flags=re.M)
s=re.sub(r'^### (\d+\.\d+)\. (.*)$',lambda m:r'\subsection{'+m.group(2)+'}'+r'\label{dao:sec-'+m.group(1)+'}',s,flags=re.M)
s=re.sub(r'^### (.*)$',lambda m:r'\subsection{'+m.group(1)+'}'+r'\label{dao:cusp-correction}',s,flags=re.M)
def link(m):
 label,target=m.groups()
 if target.endswith('.md') or '.md#' in target:
  path,sep,anchor=target.partition('#');target='https://sashakolpakov.github.io/murakamis_dream/notes/'+Path(path).stem+'.html'+(sep+anchor if sep else '')
 return '['+label+']('+target+')'
s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
s=s.replace('This note proves','This appendix proves').replace('in this note','in this appendix')
intermediate=Path('/private/tmp/md-directed-allorders-appendix-input.md');intermediate.write_text(s)
r=subprocess.run(['pandoc',str(intermediate),'-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--top-level-division=chapter','--wrap=preserve'],text=True,capture_output=True,check=True)
tex=r.stdout.replace(r'\tightlist','').replace(r'\textasciitilde{}', '~').replace('This is equations ', 'These are equations ')
out=Path('/private/tmp/M-directed-all-orders.tex');out.write_text(tex)
norm=lambda x:re.sub(r'\s+','',re.sub(r'\\(?:tag|label)\{[^}]*\}','',x))
a=[norm(x) for x in re.findall(r'\\\[(.*?)\\\]',original,re.S)]
b=[norm(x) for x in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',tex,re.S)]
ai=re.findall(r'\\\((.*?)\\\)',original,re.S);bi=re.findall(r'\\\((.*?)\\\)',tex,re.S)
labels=re.findall(r'\\label\{([^}]+)\}',tex)
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'appendix_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'displays':len(a),'displays_preserved':a==b,'inline_count':len(ai),'inline_preserved':ai==bi,'pandoc_stderr':r.stderr,'duplicate_labels':[x for x in set(labels) if labels.count(x)>1],'remaining_numeric_sections':re.findall(r'\b[Ss]ections? \d[^\n]*',tex),'private_paths':re.findall(r'/private/\S+|/Users/\S+',tex),'controls':[(i,ord(c)) for i,c in enumerate(tex) if ord(c)<32 and c not in '\n\r\t']}
Path('/private/tmp/md-directed-allorders-appendix-fidelity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));assert a==b and ai==bi
