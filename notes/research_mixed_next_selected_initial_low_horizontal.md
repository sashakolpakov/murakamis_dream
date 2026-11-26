# The first low right horizontal on the selected curve

Private finite-source deduction, 9 November 2026. At first height
\(1/10\), the complete shortened second-edge upper envelope
extends from \(2\pi/3\) to \(a_0=\arccos(-13/20)\).
Both resulting inner rates decrease along this interval.
Consequently the original two-short-edge current on this
horizontal has a fixed exponential gap.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used.

## 1. Family and conclusions

Retain the original selected curve \(u=u_\delta=\beta-iK\),
\(0\le\delta\le1/2\), and the original calibrated \(\psi,\Phi,S\).
Write \(s(u)=\Re S(u)\). Put
\[
 h=\frac1{10},\qquad a_0=\arccos(-13/20),\qquad
 t=a-ih,\quad \frac{2\pi}{3}\le a\le a_0.
\tag{1}
\]
The inverse cosine is its real value in \((0,\pi)\). One has
\[
                  \frac{2\pi}{3}<a_0<\frac{3\pi}{4},
\tag{2}
\]
by monotonicity of cosine and \(13/20<\sqrt2/2\).

Use the exact ordinary source
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
\tag{3}
\]
Set \(m=\Re\psi(t,u)\), \(e=(h+K)/2\), and \(M=\max(m,e)\).

**Theorem.** For every fixed \(\tau>0\), uniformly on (1) at
both parities and all sufficiently large \(N\),
\[
                         |K_N^<(t,u)|
                      \le C_\tau e^{N(M+\tau)}.
\tag{4}
\]
Furthermore, with the exact \(g_N^{<<},W_N,C_{N,3}\) of
[the vertical-current theorem, (3)](research_mixed_next_selected_inner_vertical_payment.md),
\[
 \left|-\frac{N^2C_{N,3}}{\pi i}
   \int_{2\pi/3-i/10}^{a_0-i/10}
                  g_N^{<<}(t,u)W_N(t)\,dt\right|
                 \le C e^{N(s(u)-1/1000)}.
\tag{5}
\]
The proof also bounds the corresponding absolute integral.
All rows, wire aliases, caps, angular sampling corrections
and original orientations are retained.

## 2. The new incoming cut bound

The selected guards give
\[
 \cos u=P+iQ,\qquad P>0,\quad Q\ge0,\quad
 |\cos u|\le1,\qquad \cosh K<8/7.
\tag{6}
\]
Equality and \(Q=0\) at \(u=0\) cause no exception.

Put
\[
 d=-\cos a\in[1/2,13/20],\qquad
 C=\cosh h<101/100,\qquad S=\sinh h .
\]
For the last bound, the positive hyperbolic cosine series gives
\(\cosh(1/10)<1+6/1199=1205/1199<101/100\).
On the incoming upper zero cut
\(y=x+ih/(2\pi)\), \(x\ge1/2-a/(2\pi)\), write
\[
 q=-\cos(2\pi x)\in[-d,1],\qquad s_q=\sqrt{1-q^2}.
\]
Then
\[
 \cos(2\pi y)=-Cq-iSs_q,\qquad
 |1-\cos(2\pi y)|=C+q>0.
\tag{7}
\]
The square of the incoming numerator is exactly
\[
 O=C^2(q+d)^2+(C^2-1)
                 \{\sqrt{1-q^2}-\sqrt{1-d^2}\}^2.
\tag{8}
\]

For every \(-d\le q\le1\),
\[
 \left|\sqrt{1-q^2}-\sqrt{1-d^2}\right|
             \le\frac{d}{\sqrt{1-d^2}}(q+d).
\tag{9}
\]
To check (9), divide its factorization by \(q+d\), with
the limiting value at \(q=-d\), and consider
\[
 \frac{|d-q|}{\sqrt{1-q^2}+\sqrt{1-d^2}}
                  \le\frac{d}{\sqrt{1-d^2}} .
\]
For \(q\le0\), squaring the remaining positive comparison
reduces to \(q^2\le d^2\). For \(0\le q\le d\) it is
immediate after subtracting \(d\sqrt{1-d^2}\).
For \(q\ge d\), use \(q\le1\le2d\).
Consequently
\[
 \sqrt O\le(q+d)\sqrt{\frac{C^2-d^2}{1-d^2}}
                         \le\frac{51}{50}(q+d).
\tag{10}
\]
Indeed the square of the middle factor is less than
\(1+67/1925<(51/50)^2\); the final comparison is
\(167500<194425\).

For \(q=-v\le0\), the other numerator obeys
\[
 |\cos(2\pi y)+\cos u|\le C+v.
\tag{11}
\]
Its squared difference from \((C+v)^2\) is
\(|\cos u|^2-1-2Cq(P-1)-2Ss_qQ\le0\), by (6).
The full force therefore satisfies
\[
 \mathfrak f:=
 \left|\frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
                   {(1-\cos2\pi y)^2}\right|
 \le\frac{51}{50}\frac{(d-v)(C+v)}{(C-v)^2}
 \le\frac{51}{50}\frac{(d-v)(1+v)}{(1-v)^2}.
\tag{12}
\]
The second inequality follows because
\((C+v)/(C-v)^2\) decreases with \(C\ge1\).
For \(0\le v\le d<1\),
\[
 \frac{(d-v)(1+v)}{(1-v)^2}
                       \le\frac{(1+d)^2}{8(1-d)}.
\]
After clearing denominators this is precisely
\(\{(3-d)v-(3d-1)\}^2\ge0\).
The last bound increases with \(d\); hence
\[
                     \mathfrak f\le\frac{55539}{56000}<1
                        \quad(q\le0).
\tag{13}
\]

For \(q\ge0\), (6) gives
\[
 |\cos(2\pi y)+\cos u|^2
 \le C^2+q^2-2CqP-2Ss_qQ\le(C+q)^2.
\]
Using (10),
\[
 \mathfrak f\le\frac{51}{50}\frac{q+d}{C+q}
 \le\frac{51}{50}\frac{1+d}{2}
 \le\frac{1683}{2000}<1.
\tag{14}
\]
The last maximization uses \(C\ge1\) and the increase of
\((q+d)/(1+q)\) in \(q\in[0,1]\).

On the outgoing upper cut, the original nonnegative-coordinate
calculation in
[the mixed-height theorem, (10)--(12)](research_mixed_next_shortened_edge_mixed_height_packet.md)
still applies. Its own angle is \(\beta<\pi/2\), its height
has \(\cosh K<8/7\), and the other leg has
\(|\cos t|\le C<101/100<8/5\). Thus
\[
                     \mathfrak f\le
                         \frac{13\sqrt{79}}{150}<1.
\tag{15}
\]
All these bounds include cut intersections and starting zeros.

## 3. Original critical root and the complete upper path

Put \(A=\cos^2(t/2)\), \(B=\cos^2(u/2)\),
\(D=A+B-AB\), and \(W=AB/D\). The present guards give
\[
 \Re A>\frac{687}{4000}>\frac16,\quad |A|<\frac{51}{200}<\frac13,
 \quad |1-A|<\frac{83}{100},\quad \Im A>0.
\tag{16}
\]
The unchanged actual output guards give
\[
 \Re B>37/60,\quad |B|^2\le\Re B,\quad
 |1-B|<9/20,\quad\Im B\ge0.
\tag{17}
\]
Consequently
\[
 \Re D>\frac{1253}{2000}>\frac12,\qquad
 \Re(1/W)=\Re(1/A)+\Re(1/B)-1>\frac32,\qquad
 \Im(1/W)<0.
\tag{18}
\]
In particular \(W\) stays in a compact subset of the upper
right quadrant. The principal point
\(y_*=\pi^{-1}\arctan\sqrt W\) stays in the upper half-strip,
is simple, and is the unique finite algebraic root there of
\[
 e^{F_y}-1
   =-\frac{(z_y^2+1)(Dz_y^2-AB)}{z_y^4},
                     \qquad z_y=\tan\pi y.
\tag{19}
\]
Start at \(a=2\pi/3\), where
[the vertical-edge theorem](research_mixed_next_selected_right_edge_vertical_upper_envelope.md)
has already fixed the original charge and critical value.
Vary \(a\) continuously in (1).
Equations (13)--(19) prevent any original cut or zero crossing.
The original logarithmic derivative therefore remains zero,
and \(F(y_*)=\psi(t,u)\), with no additive constant change.

The zero-safe factorial envelope \(\mathcal V\) has the
same positive derivative jump \(2\pi\) on each upper cut
and zero flux at its starting zero as in the previous upper
proof. It is continuous and subharmonic. Equations
(13)--(15) exclude minima on the cuts and their starting
points. Away from cuts it is nonconstant harmonic.
On the real bottom, the incoming derivative has its
original argument in \((0,\pi)\), since
\(\Im\cos t>0\). The outgoing argument is in \((0,\pi)\)
for positive charge and is zero at \(u=0\).
The source lift at \(x\downarrow0\) is
\(2\arg\cos(z/2)\), as in the vertical-edge proof.
Thus \(\mathcal V_v(x,0+)<0\); there is no bottom minimum.

The original left-side derivative is at least
\(\pi-a>\pi/4\) for the incoming leg, and is positive
for the outgoing leg. The left rate increases from zero.
The original right-side rate decreases until
\(\min(h,K)/(2\pi)\), then increases, including equal heights
and \(K=0\). Its real endpoint value is \(e\).
Every strict side sublevel is connected or empty.
Finally, uniformly at a sufficiently large upper height,
\[
 \mathcal V(x+iv)=2\pi v-\frac{ah+\beta K}{2\pi}+o(1).
\tag{20}
\]
These are exactly the hypotheses verified, with the original
sidewise lifts, in Sections 3 of the preceding two upper-envelope
proofs.

Apply their full component/Jordan argument at level \(m\).
Every nonempty strict-sublevel component must reach a vertical
side; there are at most two components. The two saddle sectors
cannot join in one component, because the resulting Jordan loop
would enclose an ascending sector and contradict subharmonicity.
They therefore reach different sides. Following those sides to
the real endpoints costs at most \(\max(m,e)\).
For every fixed tolerance, finite parameter covers and endpoint
collars consequently give a uniformly bounded upper path with
\[
                        \mathcal V\le M+\varepsilon.
\tag{21}
\]
No new global continuous choice of paths or unproved relative
packet is needed.

## 4. Complete aliases, physical endpoints and residues

Use the literal original interpolation
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},
 \qquad T_N=B_N(y,t)B_N(y,u).
\tag{22}
\]
Its shifted real arguments now lie between \(-3/8\) and \(7/8\),
still a fixed distance from the outer singular boundaries.
The same reciprocal reflection identity proves holomorphy
in \(0<\Re y<1/2\) at every bounded height.
The uniform zero-safe factorial theorem gives
\(|T_N|\le C N^{-2}e^{N\mathcal V}\) on compact paths.
The original endpoint proof with
\(N|J(x+1/(2N))-J(x)|=O(\log N)\) gives the same exponential
rate with polynomial factors for every \(0\le j\le U_N\),
including zero rows and the true odd last index.

Both original penalized side bounds remain valid:
\[
 \mathcal V(\pm iv)-2\pi v\le D_1:=\frac{ah+\beta K}{2\pi},
 \qquad
 \mathcal V(1/2\pm iv)-2\pi v\le e.
\tag{23}
\]
Their only real-angle restriction is that both angles are less
than \(\pi\). By (2) and \(\beta<\pi/2\),
\[
             D_1\le\frac{3h}{8}+\frac K4,\qquad
                    e-D_1\ge\frac h8+\frac K4\ge\frac1{80}.
\tag{24}
\]
At wire heights \(v=2\), the original complete \(J_\pm\)
expansions have penalized polynomial part of absolute value
at most \(D_1\). Their full dilogarithmic remainder is less
than \(4/(9999\pi)<1/600\), by exactly the height-two argument
in the vertical-edge theorem. Therefore
\[
                 \mathcal V(x\pm2i)-4\pi<e-\frac1{100}.
\tag{25}
\]
No reflection or period term is removed.

Choose small fixed endpoint cuts \(\alpha,\gamma\) and cap
height \(h_c>0\), then their original midpoints
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N .
\]
Both complete alias paths go from the first midpoint at
height \(\pm h_c\), vertically to \(\pm2i\), horizontally to
the second midpoint, and back to height \(\pm h_c\).
The side estimates and uniform continuity pay their endpoint
columns and both physical endpoint groups at \(e+\varepsilon\).

With both alias paths oriented left to right and
\(\zeta=e^{2\pi iNy}\), retain the exact residue identity
\[
\begin{split}
 K_N^<={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy+
          N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy+C_N+E_N,\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
              \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
              \frac{T_N}{\zeta-1}\,dy,\\
 E_N={}&\sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
       +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
\end{split}
\tag{26}
\]
It has the original residue \(1/(2\pi iN)\) and the original
positive \(N\) factors. On the midpoint columns the cap
reciprocal has modulus at most one.
Split the upper multiplier as
\((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\).
Moving its whole unweighted part to (21) adds exactly
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.
\tag{27}
\]
Both are in the paid endpoint collars.
The two remaining rational terms retain their complete
denominators and the penalty \(e^{-2\pi N|\Im y|}\).
Equations (21)--(27), including all physical endpoints,
prove (4) after polynomial absorption.

## 5. The original inner current

The complete primitive on this interval is the one in
[positive horizontal phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
Its return comparison, for \(a\ge2\pi/3\) and \(0<h\le1\), gives
\[
 \Re\operatorname{arsinh}\tan((a-ih)/2)>\frac{19}{20},
 \qquad
 \Re\operatorname{arsinh}\{\cos(u/2)\tan((a-ih)/2)\}>\frac35.
\tag{28}
\]
It follows at \(h=1/10\) that the geometric attached rate
\(\Re\Phi(a-ih,u)\) decreases strictly with \(a\).
Its initial value is less than \(8/5\), by
[the vertical payment, (6)](research_mixed_next_selected_inner_vertical_payment.md).

The endpoint rate also decreases:
\[
 \frac{d}{da}
 \left\{\Re\psi(a-ih,0)+\frac{h+K}{2}
                          +\frac{3ah}{2\pi}-h\right\}
 < -\frac{19}{20\pi}+\frac{3}{20\pi}
 =-\frac4{5\pi}.
\tag{29}
\]
At the initial point its gap below \(s(u)\) is \(1/200\),
by the same vertical theorem. Thus both complete attached
rates stay below \(s(u)-1/200\) on (1).

The first shortened kernel is controlled by the original
slit theorem at rate \(\Re\psi(t,0)+\tau\); the second
uses (4). The exact multiplier satisfies
\[
 |W_N(a-i/10)|
 \le\frac{e^{-N/10}}{(1-e^{-N/10})^2}.
\tag{30}
\]
Multiplying the unchanged crossing exponential, sine,
and \(N^2C_{N,3}/(\pi i)\), and taking
\(\tau=1/10000\) for each edge, proves (5) and its
absolute-integral version by polynomial absorption.

This pays only the interval stated in (5). Its subsequent
connection from \(a_0-i/10\) is supplied separately by
the complete slit-based far-horizontal estimate.
No whole outer observation, derivative packet, or
first-full-edge pointwise estimate is inferred.

## Frozen source bindings

- Original selected cut guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Complete selected upper envelope:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Complete vertical-edge upper envelope:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Original mixed-height source and side formulas:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Original joined representation:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Upper component/Jordan proof:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Uniform zero-safe factorial source:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Original positive phase extension:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- First-short slit source:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Complete selected vertical-current payment:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.

