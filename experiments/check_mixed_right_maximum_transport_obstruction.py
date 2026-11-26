#!/usr/bin/env python3
"""An actual cyclic obstruction to monotone right-maximum transport."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_right_maximum_transport_obstruction.md'
DEPS = [
 'notes/research_mixed_cyclic_critical_localization.md',
 'notes/research_mixed_minimum_neighbor_contour.md',
 'notes/research_mixed_unselected_right_taper_products.md',
 'experiments/certify_mixed_right_square_conditional_packets.py',
 'repro/results/research-mixed-right-square-conditional-packets.json',
 'notes/research_mixed_fourier_weight_continuation.md',
 'notes/research_mixed_conditional_torus_composition.md',
]

# Exact rational-decimal proposals only. Every original logarithmic equation
# is subsequently enclosed by a fresh Newton self-map.
REF = [
 ['.36964355141653992788871813215064855503755175080382009548','-.00823994592758099646739318068365774636552995483261755246'],
 ['.32123196407792179054522335515769066030570367752710207681','-.00967532321895442813686994070475014112844517363919663466'],
 ['.33783249517528865161761421261557842004870288776403430754','-.00391277392144735913763427168181042150956455755994205643'],
 ['.33783249517528865161761421261557842004870288776403430754','-.00391277392144735913763427168181042150956455755994205643'],
 ['.32123196407792179054522335515769066030570367752710207681','-.00967532321895442813686994070475014112844517363919663466'],
 ['.36964355141653992788871813215064855503755175080382009548','-.00823994592758099646739318068365774636552995483261755246'],
 ['.27614255857554293681124960726479110119704061324370251880','-.04450437396877903515233136551464755658336533839992226874'],
 ['.30795361481679421308235352679986123618588947628348830674','-.04883154597491267248209027451649488143933073567259776477'],
 ['.30795361481679421308235352679986123618588947628348830674','-.04883154597491267248209027451649488143933073567259776477'],
 ['.27614255857554293681124960726479110119704061324370251880','-.04450437396877903515233136551464755658336533839992226874'],
]
INNER = [
 ['.29004610058204966801737322492846555103467311026748880951','-.10440773337875302416208926421016700007872296740810329015'],
 ['.25007283245166887820664431339270339537997733419828347326','-.00001893482623570435021562487955214106200621991506110643'],
 ['.24777895573425146868910638377579611234325316892045271201','.00705393204454088297185684390374150571628834889260315807'],
 ['.27319714514175278249703655851984330626091169561710511975','-.15539569583059173709176485975925453521526677720280880669'],
 ['.29002743488405307715303083476827705244779156795777148494','.10448831014202761630810696404813155995638554295486690060'],
]


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ar(x):
 q = F(x)
 return arb(q.numerator) / q.denominator
def az(v): return acb(ar(v[0]), ar(v[1]))


def main():
 ap = argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision', type=int, default=256)
 ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-right-maximum-transport-obstruction.json')
 args = ap.parse_args(); assert args.precision >= 160; ctx.prec = args.precision
 deps = {p: sha(ROOT/p) for p in DEPS}; ph, sh = sha(PROOF), sha(__file__)
 rec = json.loads((ROOT/DEPS[4]).read_text()); assert rec['status'] == 'passed'
 assert rec['proof_sha256'] == deps[DEPS[2]] and rec['script_sha256'] == deps[DEPS[3]]
 for key in ('dependencies', 'dependencies_sha256'):
  for p, h in rec.get(key, {}).items(): assert sha(ROOT/p) == h, p
 pi, ii = arb.pi(), acb(0, 1); word = (0, 0, 0, 1, 1); checks = []
 def check(name, valid, value=None):
  assert valid, (name, value)
  checks.append(dict(name=name, value=str(value)))
 def gp(z): return (1-(-2*pi*ii*z).exp()).log()
 def gpp(z): return 2*pi*ii / ((2*pi*ii*z).exp()-1)
 def g(z): return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
 def system(z):
  ff, jj = acb_mat(10, 1), acb_mat(10, 10)
  for v, e in enumerate(word):
   for j, k, p in ((2*v, 2*v+1, (2*v-1)%10), (2*v+1, 2*v, (2*v+2)%10)):
    ff[j, 0] = gp(z[j]+z[k])+gp(z[j]+z[p])-(2+e)*gp(z[j])+2*pi*ii*z[p]
    jj[j, j] += gpp(z[j]+z[k])+gpp(z[j]+z[p])-(2+e)*gpp(z[j])
    jj[j, k] += gpp(z[j]+z[k]); jj[j, p] += gpp(z[j]+z[p])+2*pi*ii
  return ff, jj
 center = list(map(az, REF)); radius = ar('1e-24')
 box = [z+acb(arb(0, radius), arb(0, radius)) for z in center]
 ff, jac = system(center); inverse = jac.inv(); eye = acb_mat(10, 10)
 for j in range(10): eye[j, j] = 1
 err = eye-inverse*system(box)[1]; residual = inverse*ff
 q = max(sum((abs(err[j,k]) for k in range(10)), arb(0)).upper() for j in range(10))
 r = max(abs(residual[j,0]).upper() for j in range(10))
 check('ten-variable Newton contraction', q < ar('1e-18'), q)
 check('ten-variable Newton self-map', r+q*radius < radius, r+q*radius)
 for j, z in enumerate(box):
  check(f'reference {j} in original uniqueness chamber', ar('.23') < z.real < ar('.45') and abs(z.imag) < ar('.12'), z)
  for k in ((j//2)*2+(1-j%2), (j-1)%10 if j%2 == 0 else (j+1)%10):
   check(f'reference log strip {j},{k}', 0 < (z+box[k]).real < 1, z+box[k])
 refs = box[1::2]; heights = [z.imag for z in refs]
 x = list(map(F, ['.22', '.4998', '.4999', '.22', '.4998']))
 cutoff = [min(F(1), 20*(F(1,2)-v)) for v in x]
 levels = [min(cutoff[(j-1)%5], cutoff[j], cutoff[(j+1)%5]) for j in range(5)]
 assert levels == list(map(F, ['.004', '.002', '.002', '.002', '.004']))
 assert x[2] > max(x[:2]+x[3:])
 # For 0 < d tau < .002 only coordinate 2 moves. Exactly heights 1,2,3
 # follow it; levels 0,4 remain fixed at .004.
 assert cutoff[2] == F(1,500) and cutoff[1] == cutoff[4] == F(1,250)
 target = [acb(ar(x[j]), heights[j]*ar(levels[j])) for j in range(5)]
 inner_boxes, gradients = [], []
 for j in range(5):
  a, b = target[j], target[(j+1)%5]; eta, e = word[j], word[(j+1)%5]
  c = az(INNER[j]); sr = ar('1e-20'); sb = c+acb(arb(0,sr),arb(0,sr))
  def f(s): return gp(s+a)+gp(s+b)-(2+e)*gp(s)+2*pi*ii*a
  def fp(s): return gpp(s+a)+gpp(s+b)-(2+e)*gpp(s)
  inv = 1/fp(c); contraction = abs(1-inv*fp(sb)); resid = abs(inv*f(c))
  check(f'conditional {j} contraction', contraction < ar('1e-15'), contraction)
  check(f'conditional {j} self-map', resid+contraction*sr < sr, resid+contraction*sr)
  check(f'conditional {j} original source root rectangle', ar('.2') < sb.real < ar('.46') and abs(sb.imag) < ar('.17'), sb)
  for k, v in enumerate((sb, sb+a, sb+b)):
   check(f'conditional {j} log strip {k}', 0 < v.real < 1, v.real)
  da = gp(sb+a)+2*pi*ii*sb-ar(1+F(eta,2))*gp(a)
  db = gp(sb+b)-ar(1+F(e,2))*gp(b)
  gradients.append((da,db)); inner_boxes.append(sb)
 G = [gradients[(j-1)%5][1]+gradients[j][0] for j in range(5)]
 p = [-heights[j]*G[j].imag for j in (1,2,3)]
 check('neighbor height term positive', p[0] > 0, p[0])
 check('center height term negative', p[1] < 0, p[1])
 check('other neighbor height term negative', p[2] < 0, p[2])
 main_term = -ar(F(1,20))*G[2].real
 sufficient = main_term+p[1]+p[2]
 actual = main_term+sum(p,arb(0))
 check('sufficient local derivative below -1/250', sufficient < -ar(F(1,250)), sufficient)
 check('actual maximum-transport derivative below -3/1000', actual < -ar(F(3,1000)), actual)
 check('actual maximum-transport derivative above -1/300', actual > -ar(F(1,300)), actual)
 for j,z in enumerate(target):
  check(f'target {j} below real half endpoint', 0 < z.real < ar('.5'), z.real)
  check(f'target {j} negative height', z.imag < 0, z.imag)
  check(f'target {j} positive Fourier relative margin', -g(z).real > 0, -g(z).real)
 assert deps == {p:sha(ROOT/p) for p in DEPS} and ph == sha(PROOF) and sh == sha(__file__)
 result = dict(status='passed',precision_bits=args.precision,outward_comparisons=len(checks),checks=checks,
   word=list(word),reference_radius='1e-24',reference_centers=REF,conditional_centers=INNER,
   target_real_parts=list(map(str,x)),cutoff_levels=list(map(str,levels)),
   local_sufficient_derivative=str(sufficient),actual_transport_derivative=str(actual),
   original_outer_reference=[str(z) for z in refs],target_coordinates=[str(z) for z in target],
   proof_sha256=ph,script_sha256=sh,dependencies=deps,
   scope='Actual five-cycle counterexample to nondecreasing right-maximum phase transport on the minimum-neighbor contour with every real coordinate at least .22. No obstruction to a global source bound or volume asymptotic.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',len(checks),'outward comparisons; actual derivative',actual,flush=True)


if __name__ == '__main__': main()
