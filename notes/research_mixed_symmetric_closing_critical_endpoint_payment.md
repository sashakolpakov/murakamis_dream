# Paying the selected critical endpoint sector

Private written deduction, 10 November 2026. On the actual right
closing hyperbola, the original first-edge endpoint function satisfies
\[
 J(a_*,H_*)<\frac{32}{25}-\frac{451}{240000}.
 \tag{1}
\]
The proof retains the correlation between the two coordinates of the
original cubic root. With the calibrated action floor this pays the
previously retained critical endpoint sector. It does not identify
that sector with the full closing integral or estimate a subsequent
outer connector.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. Original branch and narrower cubic guards

Use exactly the family and primitive of the
[critical endpoint reduction](research_mixed_symmetric_closing_critical_endpoint_reduction.md):
\[
 \begin{gathered}
 u=\beta-iK,\quad K=\frac{\pi K_g}{2\beta},\quad
 \pi/2\le\beta\le2\pi/3,\quad17/30<K_g<7/10,\\
 t_*=a_*-iH_*,\quad c=\cos(t_*/2)=p+iq,\quad C=\cos(u/2),\\
 C=4c^3-4ic^2-3c+i,\quad
 \frac34<p<\frac78,\quad\frac3{10}<q<\frac13,\quad
 0<a_*<2\pi/3,\quad1/10<H_*<1,\\
 J(a,H)=\Re\psi(a-iH,0)-H/2+3aH/(2\pi).
 \end{gathered}
 \tag{2}
\]
The phases keep their original constants and principal unsquared
returns. We first prove
\[
                         p<81/100,\qquad q<21/64.
 \tag{3}
\]
Both \(C_R=\cos(\beta/2)\cosh(K/2)\) and
\(2C_I=2\sin(\beta/2)\sinh(K/2)\) decrease with \(\beta\)
on this hyperbola. For the second write it as a positive constant
times \((\sin(\beta/2)/(\beta/2))(\sinh(K/2)/(K/2))\);
both factors decrease. The original positive-series bounds give
\[
 C_R<85/112,\qquad
 2C_I<\sqrt2\sinh(7/20)<1200/2351<31/60.
 \tag{4}
\]
Here \(\cosh(7/20)<17/16,\ 1/\sqrt2<5/7,\ \sqrt2<10/7\),
and
\[
 \sinh(7/20)<\frac{7/20}{1-49/2400}=840/2351.
 \tag{5}
\]
The last comparison in (4) is \(72000<72881\).

The real cubic is
\[
 C_R=p(4p^2-12q^2+8q-3).
 \tag{6}
\]
Its offset increases for \(3/10<q<1/3\) and exceeds \(-42/25\).
If \(p\ge81/100\), (6) exceeds
\[
 \frac{81}{100}\left(\frac{6561}{2500}-\frac{42}{25}\right)
 =191241/250000>85/112;
 \tag{7}
\]
the witness is \(21418992>21250000\). This proves the first guard.
For the second put \(x=2p,b=2q\). The imaginary cubic is
\[
 2C_I=(3b-2)x^2-b^3+2b^2-3b+2.
 \tag{8}
\]
Its derivative in \(b\in[3/5,2/3]\) is positive for \(x>3/2\).
At \(b=21/32\) its value is
\[
 -x^2/32+19987/32768
 >19987/32768-6561/80000>3/5-1/12=31/60.
 \tag{9}
\]
The separate comparisons are \(99935>98304\) and \(78732<80000\).
Equations (4),(8)--(9) force \(b<21/32\).
No new cubic root is selected.

## 2. Reduction to a constant imaginary coordinate

For the original first return at \(t=a-iH\), write
\[
 r_0(t)=\operatorname{arsinh}\tan(t/2)=X-iB.
 \]
On the positive lower rectangle its exact real expressions are
\[
 X=\operatorname{atanh}\frac{\sin(a/2)}{\cosh(H/2)},\qquad
 B=\arctan\frac{\sinh(H/2)}{\cos(a/2)}.
 \tag{10}
\]
They follow from the original logarithmic identity
\(r_0=\operatorname{atanh}\sin(t/2)\), calibrated at zero.
All ratios stay on the stated real branches. In particular
\[
 \pi J_a=3H/2-X,\qquad \pi J_H=B+3a/2-\pi/2.
 \tag{11}
\]
If \(H_*\le7/10\), the adopted fixed-depth endpoint comparison,
extended to smaller heights by its convex quadratic upper bound,
already gives \(J(a_*,H_*)<123/100\), stronger than (1).
Suppose henceforth that \(H_*>7/10\).

Keep \(p\in[3/4,81/100]\) fixed and increase \(q\) to
\[
                              q_0=21/64.
 \tag{12}
\]
Use the original continuous \(t=2\arccos(p+iq)\).
Its \(a_q,H_q\) are positive: \(\sin(t/2)\) is in the lower
right quadrant and \(t_q=-2i/\sin(t/2)\).
Throughout the enlargement \(H<1\). Indeed the exact identity
\[
 q^2=\sinh^2(H/2)
       \left(1-\frac{p^2}{\cosh^2(H/2)}\right)
 \tag{13}
\]
at \(H=1\) would give
\[
 q^2>\frac14\left(1-\frac{6561}{12500}\right)
       =5939/50000>441/4096=q_0^2,
 \tag{14}
\]
where \(24326144>22050000\).
The right side of (13) increases with \(H\) for these \(p\).
Also \(a>\pi/3\), since
\(\cos(a/2)\le p\le81/100<\sqrt3/2\); and \(a<2\pi/3\),
since \(\cos(a/2)>(3/4)(7/8)=21/32>1/2\).
Thus the enlargement stays on the original derivative branch.

For \(z=\operatorname{sech}^2(H/2)\),
\[
 \frac{\sin^2(a/2)}{\cosh^2(H/2)}
       =z-p^2z^2\le\frac1{4p^2}\le4/9.
 \tag{15}
\]
Hence \(X\le\operatorname{atanh}(2/3)<1\), since \(e^2>5\).
As \(H>7/10\), both derivatives in (11) are positive.
It follows that
\[
 J(a_*,H_*)\le J(a(p,q_0),H(p,q_0)).
 \tag{16}
\]
No monotonicity in \(p\), or along the outgoing hyperbola,
is asserted.

## 3. A fixed interval on the constant-\(q_0\) curve

Use \(a\) as coordinate and put
\[
 H(a)=2\operatorname{arsinh}\frac{q_0}{\sin(a/2)},\qquad
 \mathcal J(a)=J(a,H(a)).
 \tag{17}
\]
All values in (16) lie in
\[
                              7/5<a<5/3.
 \tag{18}
\]
Indeed with \(z=\cos^2(a/2)\),
\[
                         p^2=z+\frac{q_0^2z}{1-z},
 \tag{19}
\]
which decreases with \(a\).
At \(a=7/5\), \(\cos(7/10)>3/4,\ \sin(7/10)<7/10\), so
\[
 p^2>\frac9{16}(1+225/1024)=11241/16384>6561/10000,
 \tag{20}
\]
with witness \(112410000>107495424\).
At \(a=5/3\), the alternating cosine bound gives
\[
 \cos(5/6)<1-25/72+625/31104=20929/31104<27/40.
 \]
Equation (19) then implies
\[
 p^2<729/1600+\frac{729\cdot441}{4096\cdot871}<9/16,
 \tag{21}
\]
whose last cleared comparison is \(514382400<610062336\).
This proves (18).

On the entire interval \([7/5,5/3]\),
\[
                              3/4<H(a)<1.
 \tag{22}
\]
For the lower bound, \(\sinh(H/2)\ge63/160>48/125>\sinh(3/8)\).
For the upper bound use
\[
 \sin(a/2)\ge\sin(7/10)>3857/6000>16/25,\qquad
 \sinh(H/2)<525/1024<25/48<\sinh(1/2).
 \tag{23}
\]
These are respectively the cubic sine bound and positive
hyperbolic-series comparisons.

## 4. Uniform concavity

Put \(d=\tanh(H/2)\cot(a/2)\), \(Y=B+3a/2-\pi/2\), and
\(v=\sec((a-iH)/2)\). Exact differentiation gives
\[
 H'=-d,\qquad
 -d'/d=\tfrac12\tan(a/2)
       +\tfrac12(1+\operatorname{sech}^2(H/2))\cot(a/2),
 \tag{24}
\]
\[
 \begin{split}
 \pi\mathcal J'&=3H/2-X-dY,\\
 \pi\mathcal J''&=-3d-\tfrac12(1-d^2)\Re v+d\Im v-d'Y.
 \end{split}
 \tag{25}
\]
Thus the height motion is included.
On (18),
\[
 47/60<\cot(a/2)<6/5,\quad
 47/180<d<3/5,\quad
 \Re v>7/8,\quad\Im v<0.
 \tag{26}
\]
For the cotangent lower bound use
\(\cos(5/6)>47/72,\ \sin(5/6)<5/6\).
For the upper bound use
\(\cos(7/10)<183601/240000,\ \sin(7/10)>3857/6000\);
the cleared comparison is \(918005<925680\).
For \(d\), \(\tanh(H/2)<1/2\), whereas
\(\tanh(3/8)\ge3/8-(3/8)^3/3=183/512>1/3\).
The secant bounds are the original positive lower-rectangle
bounds, proved also in the positive saddle-path theorem.

Moreover \(0<Y<8/5\). Positivity follows from \(a>\pi/3\).
For the upper bound, \(|a-\pi/2|<1/5\), so \(\sin a>49/50\) and
\[
 B=\arctan(2q_0/\sin a)<\arctan(67/100)<3/5.
 \tag{27}
\]
Here \(525/784<67/100\), and the alternating upper bound
\(x-x^3/3+x^5/5\) at \(x=67/100\) is less than \(3/5\);
their difference has numerator \(-487774679\) and denominator
\(150000000000\). Now \(3a/2<5/2,\ \pi/2>3/2\) give \(Y<8/5\).

Writing \(w=\cot(a/2)\), (24),(26) imply
\[
 -d'/d\le w+(2w)^{-1}\le97/60,
 \tag{28}
\]
because this function increases for \(w\ge47/60>1/\sqrt2\).
Substituting in (25) yields
\[
 \pi\mathcal J''<-\frac{31}{75}d-\frac7{25}
                         <-\frac{5237}{13500}.
 \tag{29}
\]
Since \(\pi<22/7\), this proves
\[
                              \mathcal J''<-3/25;
 \tag{30}
\]
the final comparison is \(36659>35640\).

## 5. Center value and derivative

At \(a_c=\pi/2\), put \(H_c=H(a_c)\). The exact values are
\[
 \sinh(H_c/2)=\frac{21}{32\sqrt2},\quad
 d_c=\frac{21}{\sqrt{2489}},\quad
 X_c=\operatorname{atanh}\frac{32}{\sqrt{2489}},\quad
 B_c=\arctan\frac{21}{32}.
 \tag{31}
\]
They satisfy
\[
 8/9<H_c<9/10,\quad2/5<d_c<3/7,\quad
 3/4<X_c<4/5,\quad23/40<B_c<3/5.
 \tag{32}
\]
Here are written witnesses for all bounds not already given above.
For the height,
\[
 \sinh(4/9)\le108/235<63/136<21/(32\sqrt2),
 \]
using \(\sqrt2<17/12\); and
\[
 \sinh(9/20)>22329/48000>119/256>21/(32\sqrt2),
 \]
using \(\sqrt2>24/17\). The middle comparison in the last line
is \(5716224>5712000\). The \(d_c\) bounds follow already
from \(49<\sqrt{2489}<50\).

For \(X_c\), its argument exceeds \(16/25\). The first four
positive atanh terms exceed respectively
\[
                   16/25,\quad87/1000,\quad1/50,\quad3/500,
 \]
whose sum is \(753/1000>3/4\).
The last three cleared comparisons are
\(4096000>4078125\), \(10485760>9765625\), and
\(134217728000>128173828125\).
Its argument is less than \(13/20\), because \(409600<420641\).
Also
\[
 e^{8/5}>9067/1875>33/7,\qquad63469>61875,
 \]
by the positive exponential series. Thus
\(\operatorname{atanh}(13/20)<4/5\).

For the lower \(B_c\) bound, use
\[
 \arctan x=x-x^3/3+\int_0^x\frac{t^4}{1+t^2}\,dt
            \ge x-x^3/3+\frac{x^5}{5(1+x^2)}.
 \]
At \(x=21/32\), the first pair is
\(55251/98304>281/500\). The last term exceeds \(3/200\):
use \(x>13/20,\ x^2<1/2\), and the cleared comparison
\(742586>720000\) with denominator \(48000000\).
Hence \(B_c>577/1000>23/40\).

Equations (25),(32) and \(25/8<\pi<22/7\) now give
\[
 -89/1470<\pi\mathcal J'(a_c)<23/400,\qquad
                         |\mathcal J'(a_c)|<1/50.
 \tag{33}
\]
For the first inequality use
\(4/3-4/5-(3/7)(3/5+11/14)=-89/1470\).
For the second use
\(27/20-3/4-(2/5)(23/40+25/32)=23/400\).
Division by \(\pi>25/8\) for the lower bound and by \(\pi>3\)
for the upper gives the last assertion:
\(35600<36750\) and \(23<24\).

The original first-edge second derivative and
\(\sec x\ge1+x^2/2\) give
\[
 \psi(\pi/2,0)\le2b_2-\pi/16-\pi^3/3072,\qquad b_2<7/12.
 \tag{34}
\]
A useful sharper height bound is
\[
              \cosh(h/2)/\cosh h\le1-h^2/4\quad(0\le h\le1).
 \tag{35}
\]
To prove it, expand
\((1-h^2/4)\cosh h-\cosh(h/2)\).
The first terms are \(h^2/8-11h^4/128\). Its tail is at least
\(-h^2(\cosh1-3/2)/4\). As \(\cosh1<8/5\), the difference
for \(h>0\) exceeds
\[
                h^2(1/8-11/128-1/40)=9h^2/640>0.
 \]
The exact second derivative at this angle is
\[
 \partial_h^2\Re\psi(\pi/2-ih,0)
       =\frac{\sqrt2}{2\pi}\frac{\cosh(h/2)}{\cosh h}.
 \]
Its first height derivative vanishes at zero. Twice integrating
(35), and then using \(H_c<9/10\), bounds the height cost by
\[
 \frac{\sqrt2}{\pi}(H_c^2/4-H_c^4/96)
                  <62613/700000<9/100.
 \tag{36}
\]
The polynomial increases on \([0,1]\); the rational bound uses
\(\sqrt2<10/7,\ \pi>25/8\).
Also \(\pi^3/3072>99/10000\), with witness
\(156250000>155713536\).
The remaining linear term in \(J(a_c,H_c)\) is
\(H_c/4<9/40\). Therefore
\[
 \mathcal J(a_c)
 <167/120-25/128+801/10000
                  =767/600-451/240000.
 \tag{37}
\]

## 6. Uniform payment and its exact scope

Taylor's upper inequality from (30), completing the square and
then (33) imply throughout (18)
\[
 \mathcal J(a)
 \le\mathcal J(a_c)+\mathcal J'(a_c)(a-a_c)
                          -\frac3{50}(a-a_c)^2
 <\mathcal J(a_c)+1/600.
 \tag{38}
\]
Together with (16),(37), this proves (1) in the high case.
The low case \(J<123/100\) is stronger since
\(1/20>451/240000\).

The original endpoint reduction retains the exact identity
\[
       2E(a_*,H_*;u)+(2\beta/\pi-1)K=2J(a_*,H_*)+K_g.
 \tag{39}
\]
The calibrated floor \(M_g>163/50\), (1), and \(K_g<7/10\)
now give
\[
 2E(a_*,H_*;u)+(2\beta/\pi-1)K
                          <M_g-451/120000.
 \tag{40}
\]
The high endpoint maximum on the original positive saddle path
is bounded by this critical value and the already paid
\(123/100+K/2\) sector. Thus (40) pays precisely its remaining
endpoint comparison, uniformly.

This is an original-phase comparison for the sectors identified
by the finite path and edge theorems. It does not discard the
geometric sector, right-face vertical, low/far currents, physical
trace corrections, full-edge restorations, or a subsequent outer
contour. Their estimates must still be assembled with their
original scalars and orientations. No conclusion for arbitrary
short partial fillings is inferred.

## Frozen direct sources

| Source | SHA-256 |
|---|---|
| research_mixed_symmetric_closing_critical_endpoint_reduction.md | 480ba4e4990679a79d16fcc7c16af953ae96ca7afaa85e766baaf145a1c519b1 |
| research_mixed_symmetric_closing_action_floor_163.md | f0bfaf90d7e331adf1df3ba59980dea76ebc8347b7244d2b52c4e1c692b5f825 |
| research_mixed_symmetric_closing_wider_positive_saddle_path.md | 6e362aec94c3ae00bab51e7d4c1d6928a6c4aff8fdcdbd68a475b7e9346d7e8c |
| research_mixed_symmetric_closing_right_endpoint_sector_budget.md | f6dafa452dab15d307b7d2aad771b66409356ecf20aa441da38c01f45315c6b3 |
| research_mixed_symmetric_closing_diagonal_taper.md | 7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908 |

All direct proofs and their normalization/branch statements were read.
The tighter root-coordinate barriers are proved here rather than
imported from unpreserved correspondence.
