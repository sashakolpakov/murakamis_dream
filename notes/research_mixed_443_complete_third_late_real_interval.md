# The complete third factor after the second real angle passes 18/25

Private written proof, 11 November 2026. The complete type-three
factor has a nonincreasing upper envelope on the second real interval
from \(18/25\) to \(7/8\). The apparent obstruction at
\(b+1-q=1/2\) is removed by comparing its real incoming-wall rate
to the already calibrated left-cut rate at the half face. A
comparison of that wall with the actual-height main profile is
unnecessary.

The author completed the full written readback and direct-source
checks. Independent full proof and source review is required before
adoption. No frozen source or public document is changed.

## 1. The finite source and the retained comparison rates

Use the actual reference of a positive three/four word beginning
with \(443\), of length at least four, as in the complete half-face
theorem. Keep the third target and private height in their original
ranges:
\[
 z=b+ic_3,\qquad 11/50\le b\le9/20,\qquad
 -13/200\le c_3,h_3\le17/250.                           \tag{1}
\]
The heights remain those of the same fixed word. Put
\[
 q_0=18/25,\qquad q_1=17/20,\qquad q_2=7/8,
 \qquad Y=e^{-2\pi iq},\quad Z=e^{-2\pi iz}.
\]
For \(r=e^{-2\pi i/N}\), let
\[
 P_j=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\qquad
 C_{0,N}(Y,Z)=\sum_{j=0}^{N-1}
                     \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}. \tag{2}
\]
Every index through \(N-1\) is present, also when \(Y\) is
not a physical root. The incoming monomial is retained.

Write the original continuous physical rate as
\[
 E(t;q,z)=I_q(t)+I_z(t)-2J(t),\qquad
 I_z(t)=\int_0^t\log|1-e^{-2\pi i(z+v)}|\,dv,
\]
\[
 J(t)=\int_0^t\log(2|\sin\pi v|)\,dv,\qquad
 I_q(t)=J(q+t)-J(q).                                   \tag{3}
\]
The function \(J\) is extended continuously and periodically.
Its values at \(0,1/2,1\) are zero. Define three fixed
half-face carriers:
\[
 \mathsf L(z)=E(3/20;1/2,z),\qquad
 \mathsf H(z)=E(1/2;1/2,z),\qquad
 \mathsf T(z)=2\pi(c_3)_+.                              \tag{4}
\]
They are continuous rates, not finite row values. They are exactly
the third real-left, half, and last rates retained by the half-face
and complete core-pair proofs.

Choose \(0<\varepsilon<1/100\), sufficiently small, before
\(N\). On \([q_0,q_1]\), set
\[
 I_q=[1/8,1-q-\varepsilon],\qquad
 B_\sigma(q,z)=\max_{t\in I_q}\Re Q_0(t+i\sigma;q,z),
\]
\[
 Q_0(s;q,z)=g(q+s)+g(z+s)-2g(s)-g(q)-g(z)+2\pi iqs,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}).        \tag{5}
\]
All constants and branches are original. These are the prewall
intervals of the paired-upper proof, with its fixed right cut
chosen above \(7/25\). They are nonempty uniformly, even at
\(q=q_1\). Define
\[
 \begin{split}
 \mathcal R(q,z)=\max\{&B_{h_3}(q,z),\,
 B_{-13/200}(q,z)-13\pi/100,\,
 B_{1/5}(q,z)-2\pi/5,\,
 \mathsf L(z),\mathsf H(z),\mathsf T(z)\}.
 \end{split}                                           \tag{6}
\]
For \(q_1<q\le q_2\), define instead
\[
 \mathcal R(q,z)=\max\{\mathsf L(z),\mathsf H(z),
                                            \mathsf T(z)\}.
                                                               \tag{7}
\]

**Theorem.** The function \(q\mapsto\mathcal R(q,z)\) is
nonincreasing, allowing a downward jump after \(q_1\). For every
\(\tau>0\), uniformly on (1) and \(q_0\le q\le q_2\),
through both level parities,
\[
 |C_{0,N}(Y,Z)|\le C_\tau N^{A_\tau}
                   e^{N\{\mathcal R(q,z)+\tau\}}.       \tag{8}
\]
The same bound holds after multiplying by the complete original
\(d_N(Y)Y^{-\mu N}\), for either \(\mu\in\{0,1\}\), with
the total allowance still \(\tau\). No outgoing halfweight occurs.
In particular \(\mathcal R(q_0,z)\) is one common ceiling on
this whole interval. It is the complete third envelope already
used at the endpoint of the adopted core-pair theorem.

This is a bound for the whole third factor. It does not estimate
the preceding complete first message on the new second interval.
That attachment must keep its own original cap and conditional
rates. No lower estimate or nonzero leading coefficient is asserted.

## 2. A uniformly paid postwall middle block

Put \(\delta=1-q\). For every real \(1/2\le q<1\) and
\(\delta\le t\le1\), the exact sine-binomial comparison is
\[
 I_q(t)=J(\delta)+J(t-\delta)\le J(t).                  \tag{9}
\]
Its proof, included in the far-right physical-envelope note,
differentiates \(J(t)-J(\delta)-J(t-\delta)\). This difference
vanishes at both endpoints, increases until
\((1+\delta)/2\), and then decreases. It is nonnegative
on the whole interval. Hence the postwall physical rate satisfies
\[
                         E(t;q,z)\le I_z(t)-J(t).       \tag{10}
\]

Let \(\ell=3/20\) temporarily. The elementary radius bounds are
\(13/20<R:=e^{2\pi c_3}<31/20\), as in the paired-upper proof.
On \(0\le v\le\ell\), \(b+v\in[11/50,3/5]\), whose
cosine is less than \(1/5\): its maximum is
\(\cos(11\pi/25)=\sin(3\pi/50)<33/175<1/5\). Thus
\[
 |1-Re^{-2\pi i(b+v)}|^2
 >1+R^2-2R/5>1,
\]
so \(I_z\) increases on this whole initial interval. Globally
its integrand is at most
\(C:=\log(51/20)<1\). The last inequality follows from
\(e>1+1+1/2+1/6=8/3>51/20\).

For \(\ell\le t\le1/2\), subtracting the fixed carrier in
(4) from (10) gives
\[
 \begin{split}
 I_z(t)-J(t)-\mathsf L(z)
 &\le C(t-\ell)-J(t)+2J(\ell)-I_{1/2}(\ell)\\
 &\le (7/20)C+2J(\ell)-I_{1/2}(\ell).
 \end{split}                                           \tag{11}
\]
Indeed \(Ct-J(t)\) strictly increases: \(C>\log2\), whereas
\(J'(t)\le\log2\). The last value in (11) is its value
at \(t=1/2\).

Here are explicit lower bounds for the two favorable terms.
The sine upper bound and \(\pi<22/7\) give
\[
 -J(3/20)>
 \frac3{20}\{1+\log(35/33)\}>\frac{27}{170},
                                                               \tag{12}
\]
since \(\log(35/33)>1/17\). Also
\(2\cos(3\pi/20)>7/4\), by \(3\pi/20<1/2\) and
\(\cos x>1-x^2/2\). Therefore
\[
 I_{1/2}(3/20)>\frac3{20}\log(7/4)>\frac9{110},        \tag{13}
\]
using \(\log(7/4)>6/11\). Equations (11)--(13) give a
uniform deficit greater than
\[
                \frac{27}{85}+\frac9{110}-\frac7{20}
                      =\frac{37}{748}>\frac1{25}.     \tag{14}
\]
All logarithmic bounds here are the first positive term of
\(\log x=2\operatorname{artanh}((x-1)/(x+1))\).

For \(\delta\le t\le\ell\), use instead the increase of
\(I_z\) just proved and \(-J(t)<1/6\). The latter elementary
bound is proved by integrating \(2\sin\pi t>6t\) on
\((0,1/6)\), where \(-J\) reaches its maximum. Then
\[
 I_z(t)-J(t)-\mathsf L(z)
 <\frac16-\frac{27}{85}-\frac9{110}<-\frac1{25}.
\]
Consequently, throughout the entire postwall middle block,
\[
 E(t;q,z)<\mathsf L(z)-1/25,
                      \qquad \delta\le t\le1/2.       \tag{15}
\]
This proof uses no sign of \(c_3\) or \(h_3\). In particular
the incoming-wall rate \(E(\delta;q,z)\) is paid by the same
carrier even after \(b+\delta\) passes below \(1/2\).

## 3. The entire high block down to an incoming wall at 1/8

For \(q_0\le q\le q_2\), we have \(1/8\le\delta\le7/25\).
Put \(d=c_3\), \(H=|d|\), and retain the original disk
primitive \(G_H(u)=\Re g(u-iH)\). For \(t=1-v\),
\(0\le v\le1/2\), the exact reflected rate is
\[
 \begin{split}
 E(1-v;q,z)={}&J(\delta)-J(\delta+v)
       +G_H(b-v)-G_H(b)+2J(v)\\
       &+2\pi d_+(1-v).
 \end{split}                                           \tag{16}
\]
This is the normalization in the paired-upper proof, including
the positive outgoing-height drift.

First suppose \(0<v\le3/20\). On the incoming interval,
\(\delta+u\in[1/8,43/100]\), so
\(2\sin\pi(\delta+u)>3/4\). On the outgoing interval,
\(b-u\in[7/100,9/20]\), and its disk modulus is greater
than \(2/5\). Below one quarter, the minimum over all disk
radii is its sine \(\sin(2\pi(b-u))\); above one quarter
the modulus is at least one. The sine minimum is
\(\sin(7\pi/50)>2/5\), as follows from
\(7\pi/50>7/16\) and \(\sin x\ge x-x^3/6\).
It follows that
\[
 J(\delta)-J(\delta+v)<v\log(4/3)<v/3,
 \qquad G_H(b-v)-G_H(b)<v\log(5/2)<v.
\]
Meanwhile \(J(v)<-v\), because \(2\pi v\le3\pi/10<1\)
and the sine upper bound gives
\(J(v)<v\{\log(2\pi v)-1\}\). Subtracting
\(\mathsf T(z)=2\pi d_+\) in (16) now proves
\[
                 E(1-v;q,z)<\mathsf T(z)-2v/3.
                                                               \tag{17}
\]
The limiting last rate at \(v=0\) is exactly \(\mathsf T\).

For \(3/20\le v\le1/2\), apply the leg inequality
\[
               G_H(b-v)+J(v)+G_H(1/2-b)\le0
\]
from the all-angle high-row proof. With
\(F_\delta(v)=J(\delta)+J(v)-J(\delta+v)\), (16) becomes
\[
 E(1-v;q,z)\le\mathsf H(z)+F_\delta(v)
                                   +\pi d_+(1-2v).     \tag{18}
\]
We give a stronger chord estimate on this new interval.
The function \(F_\delta\) is convex, since
\[
 F_\delta''(v)=\pi\cot\pi v-\pi\cot\pi(\delta+v)>0,
 \qquad F_\delta(1/2)=J(\delta)+J(1/2-\delta)\le0.
\]
The increment \(J(\delta+3/20)-J(\delta)\) is positive
for every \(1/8\le\delta\le7/25\). Indeed its integrand
increases throughout the possible integration intervals, all of
which lie below \(1/2\), so its minimum is at \(\delta=1/8\).
On that interval pair \(u\) with \(2/5-u\). The product
\[
             4\sin\pi u\sin\pi(2/5-u)
\]
equals \(2\cos(\pi(2u-2/5))-2\cos(2\pi/5)\). It has its
minimum at \(u=1/8,11/40\), and that minimum exceeds
\((3/4)(3/2)=9/8>1\). The first factor bound is
\(2\sin(\pi/8)>3/4\); the second follows from
\(11\pi/40>55/64\) and
\(\sin(55/64)\ge55/64-(55/64)^3/6>3/4\).
Taking logarithms and integrating proves the positivity.
Therefore (12) yields
\[
 F_\delta(3/20)<J(3/20)<-27/170,
 \qquad
 F_\delta(v)\le-\frac{27}{119}(1-2v).                 \tag{19}
\]
The last inequality is the chord between \(3/20\) and \(1/2\).
Since
\[
                \frac{27}{119}>\frac{17\pi}{250}
                                      \ge\pi d_+,
\]
equations (18)--(19) pay this entire range by \(\mathsf H\).
Together with (17),
\[
 E(t;q,z)\le\max\{\mathsf H(z),\mathsf T(z)\},
                   \qquad1/2\le t\le1,\quad q_0\le q\le q_2.
                                                               \tag{20}
\]

## 4. The central contour through q=17/20

For \(q_0\le q\le q_1\), use precisely the interpolation
and heights in (5)--(6). Its prewall curvature is negative:
\[
 \Re Q_{0,ss}
 =\pi\{\Re\cot\pi(q+s)+\Re\cot\pi(z+s)
                                     -2\Re\cot\pi s\}<0.
                                                               \tag{21}
\]
The incoming shifted cotangent is negative. The outgoing-versus-own
comparison in Section 4 of the paired-upper proof applies on the
whole interval \(1/8\le\Re s<1-q\). When the outgoing cotangent
is positive, its real argument lies between \(69/200\) and
\(1/2\); that proof's explicit two rational cotangent bounds
give (21) at every height. Its argument did not require
\(b+1-q\ge1/2\).

At the left real cut, the unit-input inequality gives
\(I_q(t)\le I_{1/2}(t)\) for all \(0\le t\le1/2\).
Moreover \(E(t;1/2,z)\) increases on \(0<t\le3/20\).
The incoming modulus exceeds \(7/4\), the outgoing modulus
exceeds one by Section 2, and the denominator square is below
one. Thus the left cut and all omitted low rows are paid by
\(\mathsf L\).

At the right cut, (15) pays the continuous wall by
\(\mathsf L-1/25\). Uniform continuity of the integrated
rates permits a fixed sufficiently small \(\varepsilon\)
so that the right cut and its entire collar up to the wall
are paid by \(\mathsf L\), with a strict reserve. Every
postwall middle row is paid by (15), and every high row by (20).

By (21), each unweighted vertical join to the original height
\(h_3\) is bounded by its two endpoints: the real endpoint
is paid by \(\mathsf L\), and the main endpoint by
\(B_{h_3}\). There is no comparison of the real wall with
an unretained main point beyond the cut.

At every point of the prewall rectangle, the imaginary derivative
is strictly decreasing with height. Its two exact limits are
\(2\pi q\) below and \(-2\pi b\) above. Consequently
\[
                 -9\pi/10<\Im Q_{0,s}<17\pi/10<2\pi.
                                                               \tag{22}
\]
Both weighted vertical halves decrease away from their real
endpoints. All four sides are therefore paid by the two real-cut
bounds. The actual horizontal, lower correction, and upper
correction have exactly the three rates in (6).

The original factorial interpolation is
\[
 T_N(s;q,z)=e^{2\pi iNqs}\Pi_N(q+s)\Pi_N(z+s)
                             E_N(q)E_N(z)E_N(s)^2.      \tag{23}
\]
All arguments on these actual contours stay in compact original
strips. Inward half-grid cuts and the exact split-cotangent identity
retain its \(+N\) zero-mode integral, both oriented joins,
two horizontal sampling currents with coefficient \(N/(2i)\),
and all four weighted vertical halves. All rows outside the cuts
remain in the finite low, collar, postwall, and high groups just
estimated. The zero-safe finite-product upper estimates apply
uniformly through every numerator zero and both true index ends.
They give (8) on \([q_0,q_1]\) after one prescribed allowance.

## 5. A positive complete bound from q=17/20 to 7/8

For \(q_1\le q\le q_2\), the incoming wall satisfies
\(1/8\le\delta\le3/20\). Every row before that wall
lies in the low interval of Section 4 and is bounded by
\(\mathsf L\). Rows from the wall to \(1/2\) satisfy (15),
and all higher rows satisfy (20). Applying the same zero-safe
finite row estimates to the whole original sum yields
\[
 \sum_{j=0}^{N-1}\left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|
 \le C_\tau N^{A_\tau}
       e^{N\{\max(\mathsf L,\mathsf H,\mathsf T)+\tau\}}.
                                                               \tag{24}
\]
No contour shrinks to zero length as \(q\uparrow7/8\).
No factor \(1-Y^N\), or terminating physical support, has
been removed. Equation (24) bounds the original off-grid sum
including all revived rows and proves (8) on this closed interval.

## 6. Decrease of the envelope, weights, and precise scope

Section 3 of the paired-upper proof proves separately that every
third maximizing numerator satisfies \(N_3<D\) once
\(q\ge21/40\). Its range from \(7/10\) to \(7/8\) is
pointwise on the prewall interval, for all actual main and lower
heights in (1); its distinct upper-height estimate gives the same
conclusion at \(1/5\). The original incoming derivative is
\(\log(N_3/D)\). At a maximizing moving right endpoint,
the private derivative is nonnegative and its endpoint velocity
is \(-1\), so the additional term is nonpositive.
Thus each \(B_\sigma(q,z)\) in (6) is nonincreasing.
All rates are smooth on the fixed-distance prewall family;
the usual locally Lipschitz maximum argument applies. The three
physical carriers are fixed in \(q\). This proves the stated
monotonicity, including the permissible downward change to (7).

The absolute Fourier theorem gives upper rate zero for the full
\(d_N(Y)\) on the compact real interval \([q_0,q_2]\),
because \(J(q)\ge0\). Both \(Y^{-\mu N}\) have modulus
one. Multiplying them into the complete estimates, with a share
of the arbitrary total allowance, proves the weighted assertion.
Every original factor is retained at its zeros.

The theorem supplies the complete third envelope required for
an extension of the preceding first message. It keeps the
three half-face physical carriers and the original third
horizontal phases, so their earlier calibrations can be used
without a new additive constant. Such a product theorem still
needs a bound for every piece of that preceding message on
\((18/25,7/8]\). Equation (8) alone is not that theorem.

## Direct sources

| Source | Direct implication | SHA-256 |
|---|---|---|
| research_mixed_443_complete_second_half_face.md | original actual reference, third heights, and half-face carriers | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b |
| research_mixed_443_paired_upper_prewall_currents.md | original third phases, prewall curvature, reflected rate, finite currents, and independent third derivative estimates | 9b851f2e88f14be3116be661d8377bae514c77c28fbe594011b5966acc4ea77e |
| research_mixed_443_core_first_complete_right_pair.md | complete third envelope and retained raw calibration at q=18/25 | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_initial44_far_right_physical_envelope.md | entire unit-input comparison and sine-binomial inequality | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_all_angle_high_row_sign_class.md | normalized disk primitive and the legwise high-row inequality | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_elementary_one_numerator_rate_bound.md | elementary proof of the global bound -J<1/6 | f2376d1732f241ef3214a413259615b56de935a7fde7ae17370e95f72dac4289 |
| research_mixed_conditional_contour_allowance.md | zero-safe complete finite row estimates with arbitrary allowance | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_fourier_right_cap_joint_global_chart.md | exact interpolation, holomorphy, physical equality and unchanged scalar | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| research_mixed_fourier_weight_continuation.md | absolute upper rate of the complete Fourier polynomial | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The author read back the entire final proof and all nine directly
used source implications, and checked their hashes. All new scalar
inequalities have written elementary proofs above. No mathematical
numerical evaluation, saved-value arithmetic, test, import,
compilation, or frozen-source edit was used.
