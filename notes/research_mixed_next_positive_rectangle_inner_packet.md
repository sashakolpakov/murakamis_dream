# A complete inner packet on an independent positive rectangle

Private finite-source extension, 9 November 2026. The original inner
packet holds on the whole independent rectangle
\[
 \mathcal R=\{\beta-iK:0\le\beta\le8/7,\ 0\le K\le2/5\}.
\tag{1}
\]
The already proved wedge handles \(K\le\beta/2\). On its complement,
a stronger action floor and a shorter low horizontal make the
complete remaining current small. No relation between the independent
parameters and the outer critical equation is imposed.

This is written analysis only. No mathematical numerical evaluation,
saved-value arithmetic or frozen-source edit is used.

## 1. Original packet and division of the domain

Keep the original \(Q_N^{\rm sh},Q_N^{\rm full},C_{N,3},S,\mathcal A\)
from the selected-curve assembly and outgoing-tail restoration.
The first superscript shortens only the second edge; both sources
retain the full original inner Hermite trace.

**Theorem.** Uniformly on (1), at both parities,
\[
 Q_N^\star(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                  \{1+O(N^{-1})\},
                \qquad\star\in\{{\rm sh},{\rm full}\}.
\tag{2}
\]
The action and nonzero amplitude are the original holomorphic
ones on a neighborhood of \(\mathcal U_+\). Thus every fixed
derivative of either normalized error is \(O(N^{-1})\) on every compact
subset of the interior of \(\mathcal R\). The statement does
not assert a packet outside this rectangle or on an entire
outer contour.

The closed part \(K\le\beta/2\) is the adopted independent-wedge
theorem. It remains to treat
\[
 \mathcal R_>=\{u\in\mathcal R:K\ge\beta/2\}.
\tag{3}
\]
This is a compact set with \(\beta\le4/5\). Its overlap with
the wedge is harmless; no source subtraction is performed
when dividing the parameter set.

## 2. Stronger action floor off the wedge

Use the original derivative
\[
 S'(u)=-\pi^{-1}\operatorname{arsinh}
             \{c_*(u)\tan(u/2)\},\qquad
 \Re c_*>3/4,\quad1/6<\Im c_*<1/3,\quad |c_*|<16/17.
\tag{4}
\]
The real-then-vertical proof of the adopted action-floor note
uses only these whole-cubic guards. On (3), its real loss is
\[
 D_{\rm real}
 \le-\frac{32}{17\pi}\log\cos(\beta/2)
 <\frac{32}{17\pi}\log(25/23)
 <\frac{64}{1173}.
\tag{5}
\]
Indeed \(\beta/2\le2/5\), \(\cos(2/5)>23/25\),
\(\log(25/23)<2/23\), and \(\pi>3\).
On the vertical path its imaginary-return estimate gives
\[
 D_{\rm vert}\le\frac{K\tan(\beta/2)}{3\pi}
             <\frac{4}{207},
\tag{6}
\]
using \(\tan(2/5)<10/23\) and \(K\le2/5\).
The sum is less than \(1/10\), since
\[
                  \frac{64}{1173}+\frac4{207}
                         =\frac{260}{3519}<\frac1{10}.
\]
The original \(M_3>9/5\) therefore implies
\[
                         s(u):=\Re S(u)>17/10
                                      \qquad(u\in\mathcal R_>).
\tag{7}
\]
Zero endpoints in (5)--(6) only improve the inequality.

The same original cubic imaginary equation, since
\(\Im\cos(u/2)\ge0\) on (1), gives
\[
                     2/3<H_*(u)<1,\qquad 0<a_*(u)<\pi/2.
\tag{8}
\]
Its proof is exactly the monotone \(b\)-equation used in the
wedge and axis theorems, with no outer stationarity assumption.

## 3. Independent second-edge upper envelopes

For \(u\in\mathcal R\),
[the independent-rectangle cut lemma](research_mixed_next_independent_rectangle_cut_guards.md) supplies
the original upper-cut and root guards on
\[
       \pi/2\le a\le2\pi/3,\qquad1/10\le H\le1,
       \qquad t=a-iH.
\tag{9}
\]
In particular, with \(P+iQ=\cos u\),
\[
 |\cos u|<13/12,\quad P>7/30,\quad Q\ge0,
\tag{10}
\]
the incoming force is at most \(39/(32\sqrt3)\) for negative
cut coordinate and its square is at most \(77/80\) for
nonnegative cut coordinate. The outgoing-cut bound is still
\(13\sqrt{79}/150<1\). The same lemma proves the compact
\(A,B,D,W\) guards and the original zero-charge saddle.

We also need a smaller extension of the low horizontal than
the wedge theorem. Put
\[
                  h_0=1/10,\qquad a_1=\arccos(-3/5).
\tag{11}
\]
For
\[
        2\pi/3\le a\le a_1,\qquad H=h_0,\qquad u\in\mathcal R,
\tag{12}
\]
write \(d=-\cos a\in[1/2,3/5]\), \(C=\cosh h_0<101/100\),
and \(q=-\cos2\pi x\in[-d,1]\) on the incoming upper cut.
The unchanged first-numerator calculation gives
\[
 |\cos2\pi y+\cos t|\le(51/50)(q+d).
\tag{13}
\]
This is the exact factorization in the original initial
low-horizontal proof, now on the smaller interval for \(d\).

Let \(M=13/12\). For \(q=-v\le0\), (10) gives
\[
 |\cos2\pi y+\cos u|\le M(C+v).
\tag{14}
\]
To check this without an assumption \(|\cos u|\le1\), square
the left side:
\[
 C^2-1+v^2+|\cos u|^2+2CvP
             -2\sqrt{C^2-1}\sqrt{1-v^2}\,Q.
\]
It is at most \(C^2-1+v^2+M^2+2CvM\), which is no greater
than \(M^2(C+v)^2\); their difference is
\((M^2-1)(C^2+v^2-1)+2Cv(M^2-M)\ge0\).
For \(q\ge0\), discard the two negative mixed terms instead.
The same comparison gives
\[
                      |\cos2\pi y+\cos u|\le M(C+q).
\tag{15}
\]
Here the difference of squares is at least
\((M^2-1)(C^2+q^2-1)+2M^2Cq\ge0\).

Equations (13)--(15) and the exact denominator \((C+q)^2\)
now yield on both parts of the cut
\[
\begin{split}
 q=-v\le0:\quad
 \mathfrak f
 &\le M\frac{51}{50}
          \frac{(d-v)(1+v)}{(1-v)^2}
 \le M\frac{51}{50}\frac{(1+d)^2}{8(1-d)}
 \le\frac{221}{250},\\
 q\ge0:\quad
 \mathfrak f
 &\le M\frac{51}{50}\frac{q+d}{C+q}
 \le M\frac{51}{50}\frac{1+d}{2}
 \le\frac{221}{250}<1.
\end{split}
\tag{16}
\]
The first reduction decreases with \(C\ge1\); the following
maximization is the original perfect square
\(((3-d)v-(3d-1))^2\ge0\).
The outgoing cut retains \(13\sqrt{79}/150<1\).

The same low-family incoming bounds give
\(\Re A>1/6\), \(|A|<1/3\), \(|1-A|<83/100\).
The rectangle lemma gives \(\Re(1/B)>24/25\) and
\(|1-B|<17/40\). Hence
\[
 \Re(1/W)>3/2+24/25-1=73/50,\qquad
 |1-D|<1411/4000<1/2 .
\tag{17}
\]
Together with \(\Im(1/W)<0\), these guards continue the
same original simple saddle and zero logarithmic charge
from \(a=2\pi/3\) along (12).

We spell out why these guards give the complete source
rather than only the saddle equation. On \(\beta,K>0\)
the original two real-wire logarithms have arguments
in \((0,\pi)\), so the upward normal derivative is negative.
At \(K=0,\beta>0\), the outgoing real cut is handled by its
strict horizontal force, as in the independent-wedge proof.
At \(\beta=0\), the incoming leg alone supplies the negative
normal derivative, while the outgoing quotient is positive.
The degenerate right-side derivative is zero below its
outgoing height and \(\pi\) above, exactly as in the axis proof.
Thus, in all cases, bottom and cut minima are excluded and
both side strict-sublevel traces are connected or empty.

The original positive cut jumps, zero starting-point flux,
large-height growth, and simple saddle supply the same
component/Jordan upper path at rate
\(\max\{\Re\psi(t,u),(H+K)/2\}+\varepsilon\).
All these parameter families are compact. Finite path
covers give uniform constants.

The original sidewise penalized bounds and all physical
endpoint limits remain unchanged. On (9) their left reserve
is at least \(H/6+K/4\ge1/60\). On (12), since
\(a_1<3\pi/4\), it is at least \(H/8+K/4\ge1/80\).
The two complete alias horizontals can both use height
two, with the unchanged full remainder less than \(1/600\).
This leaves a strict reserve in both families.
The literal reciprocal-factorial interpolation, its two
midpoint caps, both original endpoint connectors, exact
residue factors \(N\), and all physical \(0\le j\le U_N\)
are exactly the formula (20) of the axis theorem, with
\(-iK\) replaced by \(\beta-iK\). The shifted factorial
real arguments still stay in a fixed compact subinterval
of \((-1,1)\), and their zero-safe endpoint bounds apply.

Consequently both on (9) and on (12), for every fixed
\(\tau>0\),
\[
 |K_N^<(t,u)|\le C_\tau
       \exp N\{\max(\Re\psi(t,u),(H+K)/2)+\tau\}.
\tag{18}
\]
This bound retains both complete aliases and every
endpoint row at both parities.

## 4. The low geometric endpoint without the wedge condition

Let \(t_0=2\pi/3-i/10\). The original first-edge estimate is
\[
                 2\Re\psi(t_0,0)<19/12+1/300.
\tag{19}
\]
Along \(u=\beta-ik\), \(0\le k\le K\), set
\(c=\cos(t_0/2)\), \(A=c^2\), \(C_u=\cos(u/2)\),
\(B=C_u^2\), \(D=A+B-AB\).
The bounds
\[
 \Re B\ge\cos^2(\beta/2)>(41/49)^2,\quad
 0<\Re A<1,\quad \Im A,\Im B\ge0
\]
hold on the whole rectangle. If \(\Re B\le1\), then
\(\Re D\ge\Re B\). If \(\Re B>1\), then
\[
 \Re D=1+(\Re B-1)(1-\Re A)+\Im A\Im B\ge1 .
\]
Thus in either case
\[
       \Re D>(41/49)^2,\qquad |C_u|>41/49,\qquad |c|<13/25.
\tag{20}
\]
These replace the unnecessary wedge restriction
\(\Re B\le1\) in the original proof. Its original derivative
therefore still satisfies
\[
 |\psi_{uu}(t_0,u)|
       =\left|\frac{c}{2\pi C_u\sqrt D}\right|
       <\frac{31213}{84050\pi}<\frac2{5\pi}.
\tag{21}
\]
At real outgoing \(\beta\), both the change from zero
real angle and the initial downward height derivative
are nonpositive, on the original principal branch.
Integrating (21) gives
\[
 \Re\psi(t_0,\beta-iK)
       <\Re\psi(t_0,0)+4/375.
\]
Since the crossing-plus-charge rate vanishes at \(a=2\pi/3\),
\[
                  \Re\Phi(t_0,u)<8/5
                                     \qquad(u\in\mathcal R).
\tag{22}
\]

## 5. An earlier slit tail for the stronger action floor

The cut in (11) obeys
\[
                         11/5<a_1<3\pi/4.
\tag{23}
\]
For the first inequality, \(0<11/5-\pi/2<16/25\), using
\(\pi>25/8\). The alternating sine bound gives
\[
 \sin(16/25)
 \le16/25-\frac{(16/25)^3}{6}
                 +\frac{(16/25)^5}{120}
 <16/25-\frac{13}{300}+\frac1{1000}
 =\frac{1793}{3000}<3/5.
\]
The two strict rational comparisons use
\(1228800>1218750\) and \(1048576<1171875\).
Thus \(\cos(11/5)>-3/5\).
The second inequality in (23) follows from
\(\sqrt2/2>3/5\).

The original secant-polynomial proof gives
\[
 2\psi(a,0)\le4b_2-\frac{a^2}{2\pi}
                    -\frac{a^4}{96\pi}
                    -\frac{a^6}{2304\pi},\qquad4b_2<7/3.
\tag{24}
\]
At \(a=a_1\), (23) and \(\pi<22/7\) imply
\[
 \frac{a_1^2}{2\pi}>\frac{77}{100},\qquad
 \frac{a_1^4}{96\pi}>\frac3{40},\qquad
 \frac{a_1^6}{2304\pi}>\frac3{200}.
\tag{25}
\]
For the latter two inequalities the intermediate fractions
are \(102487/1320000\) and \(12400927/792000000\);
their numerator reserves are respectively \(3487\) and
\(520927\). The first is strict over
\(847/1100=77/100\).

The height cost for two first-edge copies at height \(h_0\)
is at most
\(h_0^2\sec(a_1/2)/(2\pi)\).
Here \(\sec(a_1/2)=\sqrt5<8/3\), so this cost is less
than \(1/225\).
The full slit rate, including the exact crossing and trace
penalty, is
\[
 R(a,u)=2\Re\psi(a-i/10,0)+K/2+3a/(20\pi)-1/10.
\tag{26}
\]
Since \(a_1<3\pi/4\) and \(K\le2/5\), equations (24)--(25)
give
\[
\begin{split}
 R(a_1,u)
 &<\frac73-\frac{77}{100}-\frac3{40}-\frac3{200}
                   +\frac1{225}+\frac15+\frac1{80}\\
 &=\frac{1217}{720}=\frac{17}{10}-\frac7{720}.
\end{split}
\tag{27}
\]
The original return bound beyond \(2\pi/3\) gives
\(R_a<-7/(4\pi)\), so this rate decreases all the way to
\(5\pi/6\).

The full-period slit theorem applies on that fixed compact
angular horizontal. Its second short edge has the same
first-edge rate plus the exact degree cost \(K/2\).
The original \(W_N\) retains rate \(-1/10\), with all
sampling corrections. Taking fixed tolerances below the
reserve in (27) and absorbing \(N^2\) proves a strict
finite-current gap from (7) on this last segment.

## 6. Exact remaining-current assembly

For \(u\in\mathcal R_>\), use the lower angular path
\[
 \pi/2-iH_*(u)\longrightarrow2\pi/3-iH_*(u)
 \longrightarrow2\pi/3-i/10
 \longrightarrow a_1-i/10
 \longrightarrow5\pi/6-i/10.
\tag{28}
\]
Its endpoints are those of the original remaining current.
The short-by-short kernel is entire in \(t\), and the full
trace denominator has no pole in this lower half-plane
homotopy. The original scalar and orientation are retained:
\[
 -\frac{N^2C_{N,3}}{\pi i}
 \int_{(28)}\sin t\,K_N^<(t,0)K_N^<(t,u)
                e^{3iNt^2/(4\pi)}W_N(t)\,dt .
\tag{29}
\]

On the first segment the geometric rate has a compact
strict horizontal-saddle gap from \(s(u)\), by the original
whole-\(\mathcal U_+\) concavity/positive extension and
\(\max_{\mathcal R}a_*<\pi/2\). Its endpoint-sector rate
is less than \(33/20\), by the independent endpoint-sector
calculation. The stronger action floor (7) pays it.

On the vertical, the geometric rate is convex in height.
Its upper endpoint has the preceding gap and its lower
endpoint is less than \(8/5\) by (22). The endpoint-sector
rate increases with height, so its maximum is already
paid at the upper endpoint. Equation (18) pays the
whole finite vertical.

Along the initial low horizontal in (28), both original
geometric and endpoint-sector rates decrease with \(a\),
by the original return bounds through \(a<\pi\) on the
whole outgoing \(\mathcal U_+\). Their initial bounds are
the paid low vertical endpoint bounds. Thus the complete
upper estimate (18) pays this segment. Equation (27)
pays the final horizontal.

All four gaps are uniform on the compact set (3).
Fix the edge tolerances below them. The unchanged
polynomial prefactors, including both factors \(N\)
from the original construction, can then be absorbed.
The full current (29) is exponentially smaller than
\(e^{Ns(u)}\).

The original one-current identity was already proved on
all of \(\mathcal U_+\). Its other currents, all removed
physical rows and normals, odd central term and full
Gaussian coefficient remain unchanged. Therefore the
preceding estimate proves (2) for \(Q_N^{\rm sh}\) on (3).
Together with the adopted wedge theorem it proves the
same statement on the whole rectangle.

The action-floor proof also gives \(s>331/200\) on all
of (1): its real and vertical integration never required
\(K\le\beta/2\). The independent outgoing-tail theorem
bounds \(Q_N^{\rm full}-Q_N^{\rm sh}\) by
\(CN^Ae^{47N/30}\) there, leaving a gap greater than
\(53/600\). Adding this whole exact difference proves
(2) for the full source as well.

The errors normalized by the unchanged holomorphic
\(\mathcal A e^{NS}\) are holomorphic. The uniform estimate
on the interior and Cauchy's formula give the asserted
fixed derivative bounds on its compact subsets.
Neither this argument nor the parameter partition
replaces a coherent outer error by a pointwise
asymptotic inside an unevaluated sum.

## Frozen source bindings

- Independent-rectangle cut guards and original root:
  7f3c6a64aab48f54e60dcf4c0c192f348f0d8e64c0f3547fd5783c9ef3b11ca5.
- Independent wedge packet:
  2b306e4ba11039f88c1c1e3daad75da87223313623e37f0a34b80a81ce2a4e9e.
- Original selected-curve source/one-current assembly:
  e3bc75e93e1c1834faa920ff2f4ef0711c8f6cc7906b6c0c5b59bbadc86f57b7.
- Axis boundary limits and complete alias assembly:
  8cdfab84a1b0dfb817efe41b79caa5cc74fc62fce01bac54adddd54115507d90.
- Original action integration and endpoint ceiling:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Original low-height geometric endpoint:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Original low incoming-cut factor:
  2f0287cf9655c04d2b9ca0a1545707619b57f23e899c3b76430c73b143929141.
- Original secant-polynomial far bound and full slit attachment:
  1cb4d220d4fbf5fddeaf9ecb24b572908a4485e907ac4634ea2623acee0b34bd.
- Full source restoration:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.

