# A taller mixed-height edge packet and the signed central inner source

Private written finite-source theorem, 9 November 2026. The complete
shortened-edge packet extends to outgoing heights through \(7/10\),
with independent first heights in \([-1,1]\). A stronger original
endpoint-action comparison supplies the missing margin. The exact
signed central horizontal of the inner-three trace consequently
retains its selected-action upper bound on the taller lower rectangle.

The high right current, its attached endpoint sector, and subsequent
low and far connectors are separate. No complete inner or ordinary
closing theorem is asserted. No mathematical numerical evaluation,
saved-value arithmetic, import, compilation, or frozen edit is used.

## 1. Exact source and the independent box

Fix \(0<a_L\le\pi/2\). Put
\[
\begin{gathered}
 \mathcal B_L=\{(t,u):t=a+iS,\quad a_L\le a\le\pi/2,\quad
 |S|\le1,\quad u=b-iK,\quad0\le b\le\pi/2,\quad0\le K\le7/10\},\\
 D_N=N-1,\quad U_N=\lfloor N/2\rfloor-1,\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_j(X)=S_j^{-2}\prod_{\nu<j}(c_\nu-X),\\
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
\end{gathered}                                                    \tag{1}
\]
The source has exactly the cutoff in the
[original mixed-height theorem](research_mixed_next_shortened_edge_mixed_height_packet.md).
In particular the odd middle row is not added. Write
\[
 c=\cos(t/2),\quad C=\cos(u/2),\quad A=c^2,\quad B=C^2,\quad
 D_0=A+B-AB,\quad W=AB/D_0.
                                                                    \tag{2}
\]

**Theorem 1.** On a fixed independent complex neighborhood of
\(\mathcal B_L\), uniformly through both parities,
\[
 K_N^<(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \qquad
 a_e(t,u)=\frac1{4\sqrt{D_0}\,W^{1/4}}\ne0.                         \tag{3}
\]
The phase, its additive constant, and the roots are continued from
the original real-angle branch. The normalized error is holomorphic;
every fixed mixed derivative is \(O(N^{-1})\) on smaller fixed
neighborhoods. The statement concerns the exact shortened kernel.

We first prove a box-wide phase and endpoint lemma, allowing \(a=0\).
This zero angle is not included in the finite packet (3); the inner
central interval will instead be estimated by exact polynomial
continuation.

## 2. Original returns and strict angular concavity

The written series bounds in the
[taller cubic theorem, (5)](research_mixed_symmetric_closing_strip_phase_and_tail.md)
give \(\cosh(7/20)<17/16\). Hence
\[
 \cosh(7/10)=2\cosh^2(7/20)-1<161/128<4/3.
                                                                    \tag{4}
\]
The old first-height bound remains \(\cosh1<8/5\). On the signed
box \(|a|\le\pi/2,\ |S|\le1,\ 0\le b\le\pi/2,\ 0\le K\le7/10\),
\[
 |1-A|<4/5,\quad |1-B|<2/3,\quad |D_0-1|<8/15,\quad
 \Re D_0>7/15,
                                                                    \tag{5}
\]
\[
 |\arg c|<1/2,\qquad |\arg C|<7/20,\qquad
                         |\arg\sqrt{D_0}|<1/3.                    \tag{6}
\]
For the last assertion, the disk in (5) and
\(\sin(2/3)>2/3-(2/3)^3/6=50/81>8/15\) give
\(|\arg D_0|<2/3\). The half-cosine estimates use
\(|\tan(a/2)\tanh(S/2)|<1/2\) and
\(\tan(b/2)\tanh(K/2)<7/20\).

The exact identities
\[
 1+\{C\tan(t/2)\}^2=D_0/c^2,\qquad
 1+\{c\tan(u/2)\}^2=D_0/C^2                                \tag{7}
\]
exclude both inverse-hyperbolic-sine cuts: the arguments on the
right stay strictly between \(-\pi\) and \(\pi\), since
\(2/3+1<\pi\) and \(2/3+7/10<\pi\).
As in the [original signed primitive](research_mixed_next_inner_three_negative_horizontal_phase.md),
the nonzero roots
\(c\sqrt{1+\{C\tan(t/2)\}^2}\) and
\(C\sqrt{1+\{c\tan(u/2)\}^2}\) both equal the principal
\(\sqrt{D_0}\), by connected continuation from completeness.
The closed original one-form therefore remains
\[
 d\psi=-\pi^{-1}(r_t\,dt+r_u\,du),\quad
 r_t=\operatorname{arsinh}(C\tan(t/2)),\quad
 r_u=\operatorname{arsinh}(c\tan(u/2)),\quad
 \psi(0,0)=-8J(1/4).                                             \tag{8}
\]
No additive period or logarithmic charge is changed.

Its second derivatives are
\[
 \psi_{tt}=-\frac{C}{2\pi c\sqrt{D_0}},\qquad
 \psi_{uu}=-\frac{c}{2\pi C\sqrt{D_0}}.                            \tag{9}
\]
The arguments of both ratios have absolute value less than
\[
             \frac12+\frac7{20}+\frac13=\frac{71}{60}
                                      <\frac32<\frac\pi2.
\]
Thus \(\Re\psi\) is strictly concave in each real angular
coordinate on this box. This conclusion is about the original
primitive, not a finite-source estimate.

## 3. The larger endpoint-action gap

**Lemma 2.** On \(0\le a,b\le\pi/2,\ |S|\le1,\ 0\le K\le7/10\),
\[
             \Re\psi(a+iS,b-iK)>\frac{|S|+K}{2}+\frac1{400}.
                                                                    \tag{10}
\]

First consider the same-sign case \(S=-H\), \(H\ge0\).
The product formulas in the
[original endpoint proof](research_mixed_next_shortened_edge_endpoint_gap.md),
(4)--(7), still give \(\Re r_t,\Re r_u\ge0\).
At a purely imaginary argument the possible moduli are bounded by
\[
 \tanh(1/2)\cosh(7/20)<17/32<1,\qquad
 \tanh(7/20)\cosh(1/2)<(7/20)(8/7)=2/5<1.
                                                                    \tag{11}
\]
Here \(\cosh(1/2)<8/7\) is the old bound. Thus these are the same
cut-safe principal returns. For
\(G=\Re\psi-(H+K)/2\), its two real-angle derivatives are
nonpositive and its two height derivatives are strictly negative:
\[
 G_a=-\Re r_t/\pi,\quad G_b=-\Re r_u/\pi,\quad
 G_H=-\Im r_t/\pi-1/2,\quad G_K=-\Im r_u/\pi-1/2.
                                                                    \tag{12}
\]
It suffices to estimate the corner \(a=b=\pi/2,H=1,K=7/10\).

The stronger written log-sine inequality in
[endpoint dominance, (9)](research_mixed_next_positive_transition_endpoint_dominance.md)
is \(-J(1/6)>61/378\). The unchanged real wire calculation gives
\[
                    \psi(\pi/2,\pi/2)=-5J(1/6)>305/378.           \tag{13}
\]
Follow \(t=\pi/2-i\tau,\ u=\pi/2-7i\tau/10\), \(0\le\tau\le1\).
Both tangent moduli are one. If \(r=\xi+i\nu\) is a principal
return, then \(\cosh^2\xi\le1+|\sinh r|^2\).
Accordingly \(\cosh\Re r_t<\sqrt{5/3}\) and
\(\cosh\Re r_u<\sqrt{9/5}\).
The exact imaginary return arguments are negative, with
\[
\begin{split}
 -\Im(C\tan(t/2))
 &=\frac{\cosh(7\tau/20)}{\sqrt2}
       \{\tanh\tau-\tanh(7\tau/20)\operatorname{sech}\tau\},\\
 -\Im(c\tan(u/2))
 &=\frac{\cosh(\tau/2)}{\sqrt2}
       \{\tanh(7\tau/10)-\tanh(\tau/2)
                                      \operatorname{sech}(7\tau/10)\}.
\end{split}                                                       \tag{14}
\]
Positivity follows respectively from
\(\sinh\tau>\tanh(7\tau/20)\) and
\(\sinh(7\tau/10)>\tanh(\tau/2)\) for \(\tau>0\).
The relation \(-\Im\sinh r=\cosh\xi\sin(-\nu)\) implies
\(-\nu\ge-\Im\sinh r/\cosh\xi\). Both ratios
\(\cosh(7\tau/20)/(\sqrt2\cosh\Re r_t)\) and
\(\cosh(\tau/2)/(\sqrt2\cosh\Re r_u)\) are greater than \(1/2\).
Using \(\tanh x\le x\) and \(\operatorname{sech}x\le1\) in (14)
therefore yields
\[
 \frac d{d\tau}\Re\psi(t,u)
 \ge\frac1{2\pi}
 \{\tanh\tau+(7/10)\tanh(7\tau/10)-(7/10)\tau\}.
                                                                    \tag{15}
\]
Integration gives a gain greater than
\[
 \frac{\log\cosh1+\log\cosh(7/10)-7/20}{2\pi}
                         >\frac{49}{1056}.                         \tag{16}
\]
Here \(\cosh1>37/24\), \(\cosh(7/10)>249/200\), and
\(\log v>2(v-1)/(v+1)\) for \(v>1\), by integration of
\(\operatorname{artanh}\). Hence
\[
 \log\cosh1>26/61>17/40,\qquad
 \log\cosh(7/10)>98/449>13/60.
 \tag{17}
\]
The last comparisons are \(1040>1037\) and \(5880>5837\).
Their sum minus \(7/20\) is greater than \(7/24\);
\(\pi<22/7\) proves (16).
Finally
\[
 \frac{305}{378}+\frac{49}{1056}-\frac{17}{20}
 =\frac{49}{1056}-\frac{163}{3780}>\frac1{400}.                    \tag{18}
\]
Indeed \(49/1056>11/240\) and \(163/3780<13/300\), by
\(11760>11616\) and \(48900<49140\); their difference is \(1/400\).
This proves (10) for the whole same-sign box.

For \(S=H\ge0\), the two return arguments have respectively
nonnegative and nonpositive imaginary parts. Thus increasing either
mixed depth increases \(\Re\psi\), whereas
\[
 \partial_HG=\Im r_t/\pi-1/2<0,\qquad
 \partial_KG=-\Im r_u/\pi-1/2<0.
                                                                    \tag{19}
\]
The minimum is again at \(H=1,K=7/10\). At these fixed heights,
the two separate concavities (9) put its angular minimum at a corner.
At the three corners having \(a=0\) or \(b=0\), the real action is
at least \(\psi(\pi/2,0)>239/250\), by
[the complete-edge proof, (14)](research_internal_pair_complete_edge_gap.md).
Mixed depth only increases it. The resulting gap is
\(239/250-17/20=53/500>1/400\).

At \(a=b=\pi/2\), first raise the upper first height from zero to one
while keeping \(K=0\). The return argument has modulus \(1/\sqrt2\)
and imaginary part \(\tanh H/\sqrt2\).
Thus \(\cosh\Re r_t\le\sqrt{3/2}\) and
\(\Im r_t\ge\tanh H/\sqrt3\). The increase is at least
\[
 \frac{\log\cosh1}{\pi\sqrt3}>\frac4{55},                           \tag{20}
\]
using \(\log\cosh1>\log(3/2)>2/5\),
\(\sqrt3<7/4\), and \(\pi<22/7\).
Increasing \(K\) subsequently cannot reduce the action.
Even the weaker old real anchor \(50/63\) gives the remaining gap
\[
              \frac{50}{63}+\frac4{55}-\frac{17}{20}
                           =\frac{227}{13860}>\frac1{400}.
                                                                    \tag{21}
\]
This proves (10) for mixed signs as well. All strict estimates hold
on a compact box, so their slightly smaller margins persist on a
fixed complex neighborhood.

## 4. Cut forces, the unique saddle, and the real sampling profile

The original half-strip force and numerator cuts are unchanged:
\[
 F(y;t,u)=-\sum_{z=t,u}
   \{J(1/2-y+z/(2\pi))+J(1/2-y-z/(2\pi))+2J(y)\},
\]
\[
 e^{F_y}-1=-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
 \qquad z_y=\tan(\pi y).                                          \tag{22}
\]
The cut of an angle \(z=\theta+iA_0\) starts at
\(1/2-\theta/(2\pi)-iA_0/(2\pi)\) and runs to the right.
All \(J\)'s are the original sidewise reciprocal-factorial branches.

The factorization used in the old positive-horizontal proof gives
\[
 \Re(1/A)>10/13,\quad \Re(1/B)>6/7,\quad
                         \Re(1/W)>57/91.                          \tag{23}
\]
For completeness, writing \(C_0=\cosh A_0,\ c_0=\cos\theta\),
\[
 (1+c_0C_0)(1+C_0)-(C_0+c_0)^2
     =(1-c_0)(c_0+1+C_0-C_0^2)\ge0.
 \tag{24}
\]
Both height ranges have \(C_0<8/5\), where
\(1+C_0-C_0^2>1/25\). Equation (24) proves
\(\Re\{1/\cos^2(z/2)\}\ge2/(1+C_0)\), and hence (23).
Thus the unique finite critical root in \(0<\Re y<1/2\) is
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0.                \tag{25}
\]
The imaginary part of \(y_*\) may have either sign or vanish.

The sign-independent cut calculation in the old mixed proof,
(10)--(11), bounds the full force by
\[
 \frac{\sqrt{2C_0^2-1}}{C_0+1}\frac{C_0+M}{C_0+1},
 \tag{26}
\]
where \(M\) bounds the other cosine. The first factor increases
with \(C_0\), and the second is at most \((1+M)/2\).
Our outgoing cut therefore has bound
\[
             \frac{13\sqrt{23}}{70}<1
                          \quad(3887<4900),
\]
and the incoming cut has bound
\[
             \frac{7\sqrt{103}}{78}<1
                          \quad(5047<6084).                       \tag{27}
\]
These inequalities include initial zeros by continuity, and cuts
on the real wire when a height vanishes. Consequently the critical
root never crosses an original cut or zero. Continue from the old
real-angle case by scaling the two heights. The original
\(F_y(y_*)\in2\pi i\mathbb Z\) remains zero; (8) identifies
\(F(y_*)=\psi(t,u)\) with its original additive constant.

Here is also the full real-row check. For \(v=\sin^2(\pi x)\),
\[
 q_A(v)=|A-v|/v,\quad q_B(v)=|B-v|/v,\quad
 \partial_x\mathfrak F(x)=\log(q_Aq_B),\qquad
 (\log q_A)'=\frac{\Re A\,v-|A|^2}{v|A-v|^2}.
 \tag{28}
\]
If the last derivative is nonnegative, \(v\ge1/2\) and
\(q_A^2\le1-1/(2v)\le1/2\).
The old separately convex expression, with \(w=1/v\in[1,2]\),
\[
 q_B^2=1-(1+C_0c_0)w+(C_0+c_0)^2w^2/4,
 \tag{29}
\]
has maximum at most \(16/9\) on
\(1\le C_0\le4/3,\ 0\le c_0\le1\).
One checks its four \((w,c_0)\) corners: their values are
\(C_0^2/4,\ C_0^2-1,\ (C_0-1)^2/4,\ C_0^2\).
Thus \(q_A^2q_B^2\le8/9<1\).
If instead \((\log q_B)'\ge0\), then \(q_B^2\le1-w/2\).
The incoming bound remains exactly the old one:
\[
 q_A^2\le\max\{1-w+16w^2/25,\ (1-13w/10)^2\}.
 \tag{30}
\]
The first expression is at most \(39/25\). For the second,
split \(w\in[1,3/2]\) and \([3/2,2]\): its respective bounds
are \(361/400\) and \(64/25\), while \(q_B^2\le1/2\) and
\(q_B^2\le1/4\). Each product is strictly below one.
Hence whenever \(q_Aq_B\ge1\), both logarithmic derivatives
are negative. The force modulus starts at infinity and ends at
\(|1-A||1-B|<8/15\). It crosses one exactly once, downward.
Numerator zeros have force zero and introduce no further crossings.
The original real profile has a unique maximum and no local minimum.
If \(W\) is real, this is its actual critical point, with
\(\Re F_{yy}<0\).

## 5. Complete main and alias paths

We verify the precise hypotheses of the original mixed contour proof;
no inference from the critical root alone is used.
Its continuous sidewise envelope \(\mathfrak F\) is subharmonic,
with positive \(2\pi\) derivative jumps at the cuts and vanishing
starting-zero flux. Equation (27) gives strict horizontal descent
on every cut. The unweighted left-side outward derivative is the
sum of two one-leg expressions
\[
 \pi\ \pm\{\vartheta_r(s+v)+\vartheta_r(s-v)\},\quad
 \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)),\quad
 r\in[0,1/4],
 \tag{31}
\]
whose brace has absolute value at most \(2\pi r\).
Thus the left sublevel below \(m=\Re\psi>0\) is connected.
At sufficiently large fixed heights the unweighted rate exceeds
\(m+1\), uniformly.

The right-side connectedness proof also remains valid. With
same-sign lower heights its minimum occurs at the smaller cut
height, irrespective of their ordering. With mixed signs write
\(\cos(a-i|S|)=P_t+iQ_t,\ \cos(b-iK)=P_u+iQ_u\).
The original derivative between cut heights has sign equal to that
of
\[
        Q_tP_u-Q_uP_t+\cosh(2\pi v)(Q_u-Q_t).                      \tag{32}
\]
At an upper local maximum the aligned vectors have lengths
\(\lambda>\mu>0\) and common argument \(0<\theta<\pi\).
The original identity then is
\[
 \Im(1/W)=
 \frac{2\sin\theta(\lambda-\mu)((1+C_v)^2-\lambda\mu)}
 {|1+P_t+iQ_t|^2|1+P_u+iQ_u|^2},\quad C_v=\cosh(2\pi v).
 \tag{33}
\]
Each length is smaller than \(1+C_v\). Indeed
\(|\cos z|^2-1\le\sinh^2|\Im z|<39/25<2
\le2C_v(1+\Re\cos z)\); the outgoing bound is smaller.
Thus an upper maximum forces \(\Im W<0\), and a lower maximum
forces \(\Im W>0\). Neither occurs in the half-plane of its saddle.
The zero-\(Q_u\), zero-height, coincident-vector, and \(v=0\) cases
are exactly the one-leg limits in the old mixed proof, Section 4:
they give minima or the real-saddle case, not an omitted maximum.
Its right sublevel starts at \((|S|+K)/2<m\) by (10), and is
connected in the saddle half-plane.

The real profile (28)--(30), the cut descent, the unique saddle,
and these two connected side traces are therefore all the
hypotheses of the original component/Jordan argument. Its two
descending germs reach different sides. We obtain a left-to-right
main contour through \(y_*\), with strict remote gaps. At a real
saddle use the real maximum and a local Morse deformation.
Compactness gives bounded path lengths and a finite set of charts.
The coefficient remains \(+1\) from the old real branch. The physical
endpoint rates are \(0,(|S|+K)/2\); (10) and the zero-safe original
finite-product bounds pay fixed endpoint intervals at both ends,
including their possible numerator zeros.

For both complete Fourier corrections, the original side formulas
give at every \(v\ge0\)
\[
 \mathfrak F(\pm iv)-2\pi v\le(a|S|+bK)/(2\pi)
                                      \le(|S|+K)/4,
\]
\[
 \mathfrak F(1/2\pm iv)-2\pi v\le(|S|+K)/2.                       \tag{34}
\]
For example the right one-leg formula is exactly
\(-L(r,s-v)+L(r,s+v)+\pi|s+v|\), with
\(L(r,s)=\Re J(r+is)\), even in \(s\), and
\(|L_s|\le\pi/2\); separating \(v\le|s|\) and \(v\ge|s|\)
proves (34) at either sign. No reflection term is discarded.

Use deep alias height \(v=2\). The original \(J_+,J_-\)
dilogarithm formulas in
[lower continuation, (15)--(20)](research_mixed_next_shortened_edge_lower_continuation.md)
give polynomial part of absolute value at most
\((a|S|+bK)/(2\pi)\) after the \(2\pi v\) penalty.
Every exponential in their remainders has modulus at most
\[
 e^{1-4\pi}<e^{-11}<2^{-11}=1/2048.
 \tag{35}
\]
Here \(\pi>3\) and \(e>2\) suffice. The total coefficient norm
of the two-leg dilogarithms is \(4/\pi\), so the remainder is
smaller than
\[
                    4/(2047\pi)<4/6141<1/800.                    \tag{36}
\]
Together (10), (34)--(36) pay both complete deep horizontals.
Uniform continuity moves the two side estimates to fixed
interior cuts \(0<\alpha<\gamma<1/2\), within the already paid
physical endpoint intervals. Choose a fixed small endpoint
height \(h_c>0\). The alias paths are
\[
 \alpha\pm ih_c\longrightarrow\alpha\pm2i
 \longrightarrow\gamma\pm2i\longrightarrow\gamma\pm ih_c.
 \tag{37}
\]
All their portions retain fixed exponential gaps. The same
endpoint collars pay the external caps at height \(h_c\).

## 6. Exact finite identity, all caps, and the coefficient

The [original joined-contour identity](research_mixed_next_shortened_edge_joined_contour.md)
uses the unchanged canonical interpolation
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},
 \qquad T_N=B_N(y,t)B_N(y,u).
 \tag{38}
\]
It is holomorphic on the whole open wire strip at finite height.
Take
\(\alpha_N=(\lfloor N\alpha\rfloor+1/2)/N\),
\(\gamma_N=(\lceil N\gamma\rceil-1/2)/N\), and
\(\zeta=e^{2\pi iNy}\).
The exact original sum consists of the upper and lower integrals
with multipliers \(N/(1-\zeta)\), \(N/(\zeta-1)\), its two
external caps, and both physical endpoint sums.
Splitting \(1/(1-\zeta)=1+\zeta/(1-\zeta)\), move only the
unweighted entire integral to the main contour. The exact additional
caps, with their original signs, are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.                           \tag{39}
\]
The two remaining full alias integrals are
\[
 N\int_{\Gamma_+}T_N\frac{\zeta}{1-\zeta}\,dy,\qquad
 N\int_{\Gamma_-}T_N\frac1{\zeta-1}\,dy.                            \tag{40}
\]
Use the rounded paths (37); the multipliers are bounded by
\(2e^{-2\pi N|\Im y|}\). No real residue is crossed by these
deformations. The original external half-grid denominators have
modulus at least one. The uniform zero-safe factorial theorem
applies on these fixed compact paths, through every reflected
strip and endpoint group. Thus all of (39)--(40), the external
caps, and the two physical sums are exponentially lower.
The zero row, exact last retained row, and both parity cutoffs
are unchanged.

Near the saddle the original midpoint symbol, including the exact
reciprocal-factorial continuations, is
\[
 T_N(y;t,u)=\frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                                  (1+O(N^{-1})).                 \tag{41}
\]
It is used only off its original cuts and zeros, as secured by
(27). The Gaussian of the main integral is
\[
 N\cdot N^{-2}\cdot N^{-1/2}
 \frac{\sqrt{2\pi}}{4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*)}}
             =N^{-3/2}\frac1{4\sqrt{D_0}\,W^{1/4}}.               \tag{42}
\]
The Morse orientation and its roots are the continued original
ones. Strict remote margins, zero-safe endpoint estimates, and
the local symbol persist on fixed independent parameter charts.
A finite cover gives the common neighborhood in Theorem 1.
Cauchy's formula after exponential normalization gives all fixed
derivatives claimed there. This proves the complete finite
statement, rather than only the stationary equation.

## 7. Consequence for the signed central inner horizontal

Use the actual original cubic branch from the taller strip theorem
on
\[
 \mathcal V_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le7/10\},
 \quad t_*(u)=a_*(u)-iH(u),\quad s(u)=\Re S_3(0,u).
 \tag{43}
\]
It gives \(0<a_*<\pi/2,\ 0<H<1\) uniformly on this compact set.
Keep the full first edge
\[
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\quad
 g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\quad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\quad\eta_N=(-1)^{N-1}.
 \tag{44}
\]
Its integral has the original trace prefactor
\(-N^2C_{N,3}/(\pi i)\), \(|C_{N,3}|=1\).

**Corollary 3.** The intact signed central integral satisfies
\[
 \frac{N^2}{\pi}\int_{-\pi/2}^{\pi/2}
       |g_N(a-iH(u),u)W_N(a-iH(u))|\,da
                         \le CN^A e^{Ns(u)}.                     \tag{45}
\]
Every fixed angular portion separated from \(a_*(u)\), including
a fixed central interval around zero, has a uniform exponential
gap below \(s(u)\), after absorption of its polynomial factors.
The same conclusions hold if the first edge is shortened.
No far sample, vertical connector, or right middle current is
included in (45).

Indeed (6),(9) and the exact original phase
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it
 \tag{46}
\]
give \(\Re\Phi_{tt}<-1/(4\pi)\). For the first term,
\(\Re(1/c)>1/2\): \(\Re c\ge1/\sqrt2\) and
\(|c|^2<13/10\), while \(20>13\sqrt2\).
The second ratio has positive real part by (6).
Stationarity on the unchanged cubic sheet yields
\[
 \Re\Phi(a-iH(u),u)
                 \le s(u)-(a-a_*(u))^2/(8\pi),
                         \quad-\pi/2\le a\le\pi/2.                \tag{47}
\]
For any fixed positive cutoff \(\eta\), Theorem 1 supplies the
second-edge packet on \(\eta\le|a|\le\pi/2\): use evenness
to replace a negative first real part by the corresponding
positive real part and opposite first height. Equation (8)
calibrates that evenness. The complete first-edge theorem
(16)--(18) supplies the full first factor with polynomial error
in its exponential, at either first-height sign. All original
first-edge rows are retained. The exact multiplier obeys
\[
 |W_N(a-iH)|\le e^{-NH}(1-e^{-NH})^{-2}\le Ce^{-NH}.
 \tag{48}
\]
Consequently (47) bounds these signed portions with their
complete trace charge.

For clarity the central interval uses the exact polynomial proof,
not a packet at \(a=0\). Let
\[
 a_0=\min a_*(u)>0,\quad \epsilon_0=a_0^2/(32\pi).
 \tag{49}
\]
Choose \(0<A<a_0/2\) with
\((3/2)\log(1+\tan^2(A/2))<\epsilon_0/8\).
On every fixed \(\eta\le a\le A\), (47) and the finite-source
bound just proved give
\(|f_N(a-iH,u)|\le CN^B e^{N(s-\epsilon_0+H)}\).
Its spectral degree is
\(d_N=D_N+U_N<3N/2\). With \(x=\tan(a/2)\),
\[
 (1+x^2)^{d_N}
 f_N\!\left(a-iH,u\right)
 =(1+x^2)^{d_N}F_N\!\left(
 -2\frac{\cosh H(1-x^2)+2i\sinh H\,x}{1+x^2},u\right)
 \tag{50}
\]
is an exact polynomial of degree at most \(2d_N<3N\).
Writing \(x_\eta=\tan(\eta/2),x_A=\tan(A/2)\), Chebyshev
continuation from \([x_\eta,x_A]\) to
\([-x_\eta,x_\eta]\) costs at most a polynomial factor times
\[
 \exp\left\{3N\operatorname{arcosh}
       \left(1+\frac{4x_\eta}{x_A-x_\eta}\right)\right\}.
 \tag{51}
\]
Choose \(\eta\) so this exponent divided by \(N\), and
\(3\eta/(2\pi)\), are each below \(\epsilon_0/8\).
The clearing-factor cost is already below \(\epsilon_0/8\).
Restoring (48) cancels the \(NH\) term exactly; the crossing
cost is at most \(3N\eta/(2\pi)\). The remaining gap is at
least \(5\epsilon_0/8\) before polynomial absorption.
This is the original center-bridge proof with the newly proved
source input. For two shortened factors the degree is smaller.

For a shortened first edge, the exact pointwise difference from
the full first edge is at most \(CN^B e^{D_NH}\), as in
[incoming-color bounds, (8)--(10)](research_mixed_next_incoming_color_kernel_upper_bounds.md).
It includes the odd middle row. The original complete-edge gap
\(\Re\psi(t,0)>H+1/500\) makes that difference exponentially
lower, so the same first-factor upper bound applies. The smaller
two-short degree then proves the same center conclusion.

Thus the whole signed horizontal, its exact \(N^2/\pi\), and
its central interval obey (45). The odd central physical node
has not been deleted or estimated separately: the path stays
at a fixed positive depth and retains the full Hermite sampling
kernel. This corollary supplies only this part of that full trace.

## Frozen source bindings

- Original mixed packet and full contour/topology inventory:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Signed primitive and original additive constant:
  fd3f89e30e108e1b9911d0bcb55f0948b41b2c91ffa3aadefa894ea4224fd347.
- Taller actual cubic phase and first-edge compact:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Stronger original real-corner witness:
  85d5c740d1c8c3481f5d6be5dd29d826879a366f5d07a079700cb4cbd7c92804.
- Complete first edge, all rows, and real anchor:
  1ac5e324eeb4f11425b6937332e08a682c802ce3d1fb3b6646cf7ecffed38ac3.
- Uniform original factorial and reciprocal-reflection bounds:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Exact main/alias separation and all external caps:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Original deep-height series and polynomial constants:
  79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c.
- Original component/Jordan proof:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Exact degree continuation through the inner center:
  0ddff6c7a588128a32f862e113f4e8253d9da6f3e56a4fc3bc5955cab02f7097.
- Exact first-short versus full pointwise difference, both parities:
  9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
