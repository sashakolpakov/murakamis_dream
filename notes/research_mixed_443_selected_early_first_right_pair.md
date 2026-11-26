# The early selected first interval for the complete 4,4,3 sum

Private written proof, 11 November 2026. This extends the complete
conditional-pair estimate to first real coordinates between \(1/10\)
and \(11/50\), at height \(1/100\), while the second coordinate is
real between \(1/2\) and \(18/25\). Both conditional kernels are
complete finite sums.

Moving the first variable changes its conditional phase by an
expression independent of the second variable. The positive private
height of the upper sampling correction requires a new comparison
with the cap. That comparison is proved below, before the remaining
currents and physical rows are assembled.

Author-frozen after full proof and direct-source readback. Separate
full proof and direct-source review is required before adoption.
Frozen sources and public documents are unchanged. No mathematical
evaluation is used.

## 1. Exact expression and domain

Fix the actual coupled reference of a positive three/four word of
length at least four beginning \(4,4,3\). Use the original markings
and affine action in
[the complete midpoint theorem](research_mixed_443_complete_second_half_face.md).
Set
\[
 P=[11/50,9/20],\quad H=1/100,\quad a=x+iH,\quad
 1/10\le x\le11/50,\quad 1/2\le q\le18/25,\quad
 z=b+ic_3,\quad b\in P.                                      \tag{1}
\]
The actual private heights obey
\[
 -.051<h_e<-.019,\qquad -.102<h_2<-.001,\qquad
 -.065\le h_3,c_3\le.068.                                   \tag{2}
\]
These bounds do not replace the correlated reference.

Put \(\zeta=e^{-2\pi i/N}\), \(P_j=(\zeta;\zeta)_j\),
\(p_j(V)=(\zeta V;\zeta)_j\). The polynomial \(d_N\) has degree
less than \(N\) and values \(d_N(\zeta^j)=P_j^{-1}\).
Keep the original endpoint coefficient \(H_N\) in
\[
 U_{1,N}(w,X)=\sum_{i<N}H_N(w,\zeta^{-i})p_i(X)/P_i^2,\qquad
 C_{\epsilon,N}(X,Y)=\sum_{j<N}
             X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon}.              \tag{3}
\]
For \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iq}\), \(Z=e^{-2\pi iz}\),
the expression is
\[
 \mathcal J_{\mu,N}
 =U_{1,N}(w,X)d_N(X)X^{-N}C_{1,N}(X,Y)
                  d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z),\quad\mu=0,1.  \tag{4}
\]
There is no outgoing halfweight, since the third type is three.

The original phases are
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{\pi i}{2}(e-e^2),\\
 Q_\epsilon(s;a,q)&=g(s+a)+g(s+q)-(2+\epsilon)g(s)
                                  -g(a)-g(q)+2\pi ias,
\end{split}                                                    \tag{5}
\]
where \(g'=\operatorname{Log}(1-e^{-2\pi i u})\), \(g(0)=0\),
and \(S\) is the unchanged cap action. The affine rate
\(\Lambda_{123}(z)\) is exactly equation (5) of
[the complete pair theorem](research_mixed_443_core_first_complete_right_pair.md):
the original critical real action followed by its third-coordinate
tangent. No constant or tangent is reset. If \(a_2\) is the real
second critical coordinate, retain
\[
 \delta=\min\{(9/20-a_2)^2/250000000,\ 10^{-6}\}>0.             \tag{6}
\]

**Theorem.** On a sufficiently small fixed ordinary-color disk
about \(-2\), both parities and both \(\mu\) satisfy, uniformly on
(1),
\[
             |\mathcal J_{\mu,N}|
       \le CN^A e^{N\{\Lambda_{123}(z)-\delta/8\}}.             \tag{7}
\]
Fixed ordinary-color derivatives have the same rate on smaller disks
with polynomial costs. Integrals over the stated first horizontal
segment retain their original density \(+N\,da\).

This does not include the negative first horizontal, its vertical
joins, the real first interval near zero, or the real first arcs
beyond \(1/2\). It does not complete either summation or prove a
new knot limit.

## 2. Cap envelope and midpoint calibration

The [independent-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md)
applies on (1), with zero extra upper-row allowance for type four.
Retain
\[
\begin{array}{ll}
 A_0(a)=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 A_L(a)=\Re\Psi(.27,a),\quad A_R(a)=\Re\Psi(.49,a),\\
 A_-(a)=\max_u\Re\Psi(u-.055i,a)-.11\pi,&
 A_+(a)=\max_u\Re\Psi(u+.04i,a)-.08\pi ,
\end{array}
\]
and \(A_*=\frac35+2\pi H+\log4/100\).
These include all cap rows, joins and sampling corrections.
Section 2 of
[the selected early source](research_mixed_selected_four_four_early_complete_source.md)
gives the cap-only comparisons
\[
 A_\pm<A_0-\frac1{10},\quad A_R<A_0-\frac1{1250},\quad
 A_0=\max_{.27\le u\le.43}\Re\Psi(u+ih_e,a).                  \tag{8}
\]
At \(a_+=11/50+iH\),
\[
                      A_0(a_+)-A_*>\frac{53}{500}.           \tag{9}
\]
The full first selected weight has upper rate
\[
                        W(a)=-\Re g(a)-2\pi H>3/40,          \tag{10}
\]
as in equation (5) of that source; its other upper alternative is
zero. The full second weight has rate zero on (1), because
\(\Re g(q)\ge0\), and both second monomials have unit modulus.

At \(q=1/2\), Sections 2 and 6 of the complete midpoint proof
calibrate every cap alternative, each actual first main or real-cut
profile, and every third profile, with more than \(20\delta\) of
common margin. Its domain includes the entire early selected first
segment (1). This is a profile comparison before finite summation.

The first half-index profile has an additional \(1/30\) margin at
\(a_+\), traced in Section 2 of the complete pair proof. That margin
persists on the early selected interval. Indeed Section 3 of the
selected early source transports the cap times the first half-index
profile pointwise; its derivative only involves
\[
                 g(e+a)+g(s+a)-3g(a)+2\pi ias.                \tag{11}
\]
It is independent of the second target, so its proof applies at
\(s=q=1/2\), using the continuous value of \(g(1)\).
The main cap and left cap cut transport without increase toward
smaller \(x\); (8) pays the other regular profiles. For \(A_*\),
the backward cost is less than \(9/125\), paid by (9) with more
than \(17/500\) left. Thus every cap alternative times the first
half-index profile retains the anchor's extra \(1/30\).

## 3. The upper first correction transports with the cap

Put \(h_U=\log2/(4\pi)\), so \(e^{2\pi h_U}=\sqrt2\).
Keep a fixed right cut \(r_0<1/2\), sufficiently close to \(1/2\).
Let \(\mathcal U(a,q)\) be the maximum upper sampling rate over
\(1/8\le t\le r_0\). Before its shifted numerator crosses a period
the rate is
\[
                \Re Q_1(t+ih_U;a,q)-2\pi h_U .
\]
The exact continuation is important. The complete pair proof keeps
\[
                 \Pi_N(u+1)=(1-e^{-2\pi iNu})\Pi_N(u).         \tag{12}
\]
For \(t+q\ge1\), the multiplier has rate \(2\pi h_U\).
It cancels the sampling penalty: replace \(g(s+q)\) by
\(g(s+q-1)\) and omit that penalty. The two rates agree continuously
at the wall, and the multiplier is independent of \(a\).

Every maximum defining \(\mathcal U\) has \(t\le2/5\).
For \(2/5\le t\le1/2\), the incoming folded square is less than
\((1+3/2)^2=25/4\); the outgoing square is less than \(3\),
since \(q+t\in[9/10,61/50]\) has positive cosine modulo one.
The own square \(3-2\sqrt2\cos2\pi t\) exceeds \(5\).
Thus the squared private force is less than \(3/20<1\).
Thus its real private derivative is negative. The same force
computes that derivative for the postwall continued rate.

Take a main cap point \(e=u+ih_e\), \(.27\le u\le.43\),
or the left cap cut \(e=.27\). Fix \(s=t+ih_U\),
\(1/8\le t\le2/5\). Differentiation, with the chirp and first
weight retained, gives
\[
 \partial_x\{\Re\Psi(e,a)+\text{upper rate}(s;a,q)+W(a)\}
                    =\log(N_eN_s/D^3),                      \tag{13}
\]
where
\[
\begin{gathered}
 r=e^{2\pi H},\quad R=e^{2\pi\Im e},\quad p=1/\sqrt2,\\
 N_e=|1-rRe^{-2\pi i(u+x)}|,\quad
 N_s=|p-re^{-2\pi i(t+x)}|,\quad D=|1-re^{-2\pi ix}|.
\end{gathered}
\]
Neither (13) nor its \(x\)-derivative depends on \(q\).

The derivative in (13) decreases with \(x\). Its next derivative,
divided by \(\pi\), is
\[
 \Re\cot\pi(e+a)+\Re\cot\pi(s+a)-3\Re\cot\pi a<0.              \tag{14}
\]
The first two terms are less than \(3/5\) and \(5/4\): a positive
shifted cotangent is no larger than the cotangent at its real part,
whose minima here are \(.37\) and \(.225\).
Use \(1/\sqrt3<3/5\) and
\(\cot(9\pi/40)<13/11<5/4\), the latter from
\(\tan(\pi/40)<1/12\).
For the last term, \(\Re\cot\pi(x+iH)>4/5\).
Indeed \(\cosh(2\pi H)<101/100\), and its cotangent real part
decreases with \(x\), since \((101/100)\cos(\pi/5)<1\).
At \(x=11/50\) its numerator exceeds \(\sqrt3/2>6/7\)
and its denominator is less than \(101/100\).
For the elementary bounds, \(2\pi H<1/15\) gives
\(\cosh(2\pi H)<225/224<101/100\).
Also \(\tan v\le v/(1-v^2/2)\) at
\(v=\pi/40<11/140\) gives the asserted \(1/12\) bound.

It therefore suffices to check (13) at \(x=11/50\). At that face,
\[
 \frac{N_e^2}{r}>\frac{396}{175},\qquad
 \frac{N_s^2}{r}>\frac{21}{10},\qquad
 \frac{D^6}{r^2}<\frac{19}{4}.                               \tag{15}
\]
For the first bound, \(R>18/25\),
\(u+x\in[.49,.65]\), \(\cos2\pi(u+x)<-4/7\), and
\(r^{-1}+R^2r\ge2R\). The sine witness is
\(\sin(\pi/5)>\sin(5/8)\ge1795/3072>4/7\).
For the second, \(t+x\in[.345,.62]\) has cosine less than
\(-1/2\); use \(p^2/r+r\ge2p\) and \(\sqrt2>7/5\).
For the third, \(r<43/40\), \(r+r^{-1}<201/100\), and
\(\cos(11\pi/25)>37/200\) give \(D^2/r<41/25\), and
\[
                 (41/25)^3(43/40)=2963603/625000<19/4.
\]
The cosine bound follows by writing it as \(\sin(3\pi/50)\),
using \(3/16<3\pi/50<1/5\), and \(\sin v\ge v-v^3/6\).
The radius bound follows directly from
\(e^{2\pi H}<1/(1-1/15)=15/14<43/40\);
then \(r+r^{-1}<43/40+40/43<201/100\).
The numerator product in (15) exceeds
\[
                  (396/175)(21/10)=19/4+1/500.
\]
Thus (13) is positive at the right face and everywhere earlier
by (14). Maximizing after this pointwise transport proves, for
every regular cap profile,
\[
 A_i(a)+\mathcal U(a,q)+W(a)
 \le\max\{A_0(a_+),A_L(a_+)\}
                       +\mathcal U(a_+,q)+W(a_+).             \tag{16}
\]

For \(A_*\) the derivative is instead \(\log(N_s/D^2)\).
Here \(\cos2\pi(t+x)<1/6\), hence
\(N_s^2/r>2p(1-1/6)>7/6\) and \(N_s>1\), while \(D^2<9/5\).
It follows that this derivative exceeds \(-3/5\), since
\(e^{3/5}>1+3/5+9/50+9/250>9/5\).
The backward cost is less than \(9/125\), paid by (9).
Thus (16) also holds for \(A_*\), with \(A_0(a_+)\) on the
right and an additional reserve \(17/500\).

At \(a_+\), the paired-upper theorem and Section 4 of the complete
pair proof already pay this upper correction with every complete
third-factor profile, cap and weight. Their prewall reserve is
\(1/162\); extension to the fixed cut has arbitrarily small
continuity cost. Equation (16) transfers these comparisons to
(1), including the postwall part because (12) has no \(x\)-dependence.

## 4. Main, lower, and real-cut terms

For any fixed negative height \(\sigma\), retain
\[
 B^2_\sigma(q)=\max_{1/8\le t\le r_0}\Re Q_1(t+i\sigma;a,q).
\]
For the third factor use the nested prewall intervals and the three
heights \(h_3,-13/200,1/5\) of
[the paired-upper theorem](research_mixed_443_paired_upper_prewall_currents.md).
Explicitly, choose a sufficiently small fixed \(\varepsilon>0\)
and set
\[
 I_q=[1/8,\min(r_0,1-q-\varepsilon)],\qquad
 B^3_\eta(q)=\max_{t\in I_q}\Re Q_0(t+i\eta;q,z).
\]
The sampling penalties at the latter two heights are kept separately.
Section 3 of the complete pair proof gives
\[
 B^2_\sigma(q)+B^3_\eta(q)
                    \le B^2_\sigma(1/2)+B^3_\eta(1/2).        \tag{17}
\]
Its proof is unchanged: the first outgoing numerator
\(|1-\rho e^{-2\pi i(q+t)}|\), \(0\le\rho\le1\), is independent
of \(a\). Its comparison with \(|1-e^{-2\pi iq}|\), including
the postwall part, only uses \(1/8\le t\le1/2\) and
\(q\le18/25<3/4\). The sharper joint bound near \(1/2\),
the third maximizing-index restriction, and its favorable moving
endpoint term are also independent of \(a\).
The same comparison holds for the first real left cut.

At \(q=1/2\), the first lower correction at height \(-1/5\)
has reserve greater than \(\pi/5\) relative to its same-index
actual main. The all-radius argument bound (18) in the midpoint
proof includes (1) and gives \(\Im Q_{1,s}<\pi\) below zero.
The height cost is less than \(\pi/5\), while the sampling
penalty is \(2\pi/5\).
The third lower and upper corrections retain their respective
reserves \(31\pi/1000\) and \(323\pi/2000\).
The midpoint calibration and (17) therefore pay all these pairs.

Section 6 of the paired-upper proof reduces the remaining complete
third source to those horizontal maxima and its old real-left,
half-index and last-index rates. It covers the wall, its collar,
postwall middle rows, high rows and every vertical term.
The latter three rates do not depend on \(q\).
Each first negative-height or real-left profile is separately
nonincreasing in \(q\), by the same numerator bound, so these
combinations are also paid.

Every third main or lower maximum can increase by less than
\(1/4240\) from its half-face value; its upper maximum never
increases. This is equation (13) of the complete pair proof:
integrate \(\tfrac12\log(54/53)<1/106\) over length \(1/40\);
the later derivative is nonpositive.

## 5. First joins and all physical rows

At the left cut \(t=1/8\), put \(A=\cosh2\pi\eta\).
The outgoing shifted cotangent is negative, and
\[
 3\Re\cot\pi(1/8+i\eta)>
             \frac{21/10}{A-7/10},\qquad
 \Re\cot\pi(1/8+a+i\eta)<
             \frac1{(15/16)A-1/6}.                          \tag{18}
\]
The second estimate uses \(e^{-2\pi H}>15/16\), shifted sine
at most one and shifted cosine below \(1/6\).
Both denominators are positive. Cross multiplication leaves
\((31/32)A+7/20>0\). Therefore \(\Re Q_{1,ss}<0\).
The height rate is convex, and both unweighted and weighted left
joins are paid by their corresponding endpoints.

At the limiting right cut \(t=1/2\), the signs in Section 5
of the complete pair proof still apply. They require
\(0<x\le1/2\), not \(x\ge11/50\): the incoming argument is
at least \(-2\pi x\), the original chirp adds \(2\pi x\),
and the outgoing argument keeps its correct period continuation.
Thus the unweighted join is below its actual-height endpoint,
and the weighted halves are below their real cut.
The multiplier (12) is retained on the upper half.
Uniform continuity permits the fixed cut \(r_0<1/2\) with
arbitrarily small error.

For clarity, the full first physical rate used below is
\[
 E_2(t;a,q)=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
          +J(q+t)-J(q)-3J(t)-2\pi Ht.
\]
Here \(J(u)=\Re g(u)\) on the real interval \([0,1]\),
extended periodically and continuously. Its logarithmic zeros
are interpreted by their integrable limits.
The low physical rates increase to \(t=1/8\). Split at \(1/10\).
Before that point the incoming folded modulus exceeds \(1/2\),
the outgoing modulus exceeds \(4/5\), and the own cube is less
than \(1/4\). After it the respective bounds are \(9/10,4/5\),
and \((4/5)^3\). The incoming bounds are the ones in Section 4
of the midpoint proof, which includes (1). The outgoing bound
follows from \(q+t\in[1/2,169/200]\) and
\(2\sin(3\pi/20)>4/5\). Both numerator products strictly
exceed the own cube. The zero index is included by continuity.

For high rows put \(d=1-q\), \(t=1-v\), and
\(G_H(u)=\Re g(u-iH)\). Exact reflection gives
\[
 E_2(1-v;a,q)=G_H(x-v)-G_H(x)
                  +J(d)-J(d+v)+3J(v).                       \tag{19}
\]
There is no drift because the first height is positive and the
second is zero; the last rate is zero.
If \(v\le1/10\), then \(v\le x\). The derivative \(G_H'\)
increases on \([0,1/2]\), so
\(G_H(x-v)-G_H(x)\le-G_H(v)\le-J(v)\).
Also \(J(d)-J(d+v)\le-v\log(3/2)\). Equation (19) is therefore
nonpositive on this interval.
For \(1/10\le v\le1/2\), the leg inequality of
[the all-angle row proof](research_mixed_all_angle_high_row_sign_class.md)
gives
\[
 E_2(1-v;a,q)\le H_2(a)+F_d(v)+J(v),\quad
 H_2(a)=E_2(1/2;a,1/2),\quad
 F_d(v)=J(d)+J(v)-J(d+v).
\]
The paired-upper proof gives \(F_d(v)\le-9(1-2v)/40\);
also \(J(v)\le0\). Hence every high physical row obeys
\[
                   E_2(t;a,q)\le\max\{H_2(a),0\}.             \tag{20}
\]
This includes revived rows and the literal final index. A fixed
collar below \(1/2\) is paid by uniform continuity.

The extra \(1/30\) for the first half profile in Section 2
pays the possible third increase \(1/4240\).
For the last carrier zero, the half-face real left rate obeys
\[
 E_2(1/8;a,1/2)>
 \frac{93}{200}-\frac3{40}+\frac1{36}-\frac{\pi}{400}
                                      >\frac38.              \tag{21}
\]
Indeed the incoming and outgoing moduli exceed \(3/5,5/4\),
and \(-3J(1/8)>93/200\). Use
\(\log(3/5)>-3/5\), \(\log(5/4)>2/9\), and the chirp
\(-2\pi H/8\). These scalar witnesses are in equations
(19)--(20) of
[the selected first left-connection proof](research_mixed_complete44_second_selected_first_left_connection.md);
the outgoing modulus bound also holds at \(q=1/2\).
The first-left calibration pays this last carrier with \(3/8\)
to spare, more than the possible third-factor increase.

## 6. Exact finite assembly

For the first kernel, use inward half-grid cuts tending to
\(1/8,r_0\), actual height \(h_2\), lower height \(-1/5\)
and upper height \(h_U\). The original normalized factorial is
\(\Pi_N(u)=G_N(Nu)\exp\{(\pi i/2)[N(u-u^2)-u]\}\), with the
same sine-factorial \(G_N\) as the complete pair proof.
Its literal interpolation is
\[
 T_{1,N}(s;a,q)=e^{2\pi iNas}
 \Pi_N(s+a)\Pi_N(s+q)E_N(a)E_N(q)E_N(s)^3,\quad E_N=1/\Pi_N.
 \tag{22}
\]
The split-cotangent identity has zero-mode density \(+N\),
both unweighted joins, lower coefficient
\(N(\cot\pi Ns-i)/(2i)\), oppositely oriented upper coefficient
\(N(\cot\pi Ns+i)/(2i)\), and all four weighted vertical halves.
Sections 3--5 pay every term and all remaining physical groups.

The numerator \(s+a\) stays in its regular strip. The numerator
\(s+q\) can cross a period; (12) is retained. At its real wall,
the exact finite recurrence and uniform upper product argument
in Section 5 of the complete pair proof apply without change.
All denominator strips remain compact and regular. No zero is
divided out. For physical rows, Section 2 of
[the contour-allowance proof](research_mixed_conditional_contour_allowance.md)
gives the stated continuous rates with polynomial prefactors and
an arbitrary fixed allowance.

The third kernel uses precisely the complete partition of the
paired-upper theorem; the cap uses (8)--(9); the first full
weight uses (10), and the second full weight has rate zero.
The main and lower first terms retain more than \(20\delta\)
of raw margin. The upper has its separate fixed margin from
Section 3. The first half and last profiles pay their third-factor
costs by Sections 2 and 5. Choose all fixed collars, source
allowances and color-continuation costs within those margins,
leaving at least \(\delta/8\). The finitely many current lengths,
their \(N\) densities and physical index counts change only the
polynomial prefactor. This proves (7).

The cap bound first holds uniformly for real ordinary colors.
Its degree in \(w\) is less than \(N\); the interval polynomial
continuation already used by these sources gives a fixed disk
with arbitrarily small exponential cost. Cauchy's formula gives
the fixed derivatives on smaller disks. Both parities are retained.

## Direct source versions

The direct inputs are the complete pair's contour/profile proof;
the paired-upper proof's complete third source; the midpoint proof's
early-path calibration; the selected early proof's cap-only and
half-profile transport; the independent-height cap theorem; the
leg inequality; the first left-connection scalar cut bound; and
the zero-safe physical product estimate. Their domains and the
extensions of their proofs used here are specified in the text.

| Source | SHA-256 |
|---|---|
| research_mixed_443_core_first_complete_right_pair.md | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_443_paired_upper_prewall_currents.md | 9b851f2e88f14be3116be661d8377bae514c77c28fbe594011b5966acc4ea77e |
| research_mixed_443_complete_second_half_face.md | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b |
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_complete44_second_selected_first_left_connection.md | f91bbac2d0843fec8fd5e9ddc29b4d35efbbdf708f2e5bd8d4db6c686b58c702 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

The author read the entire final proof and all eight directly used
source implications and checked all eight source hashes. Separate
review is still required. No mathematical numerical evaluation,
saved-value arithmetic, test, import, compilation, or frozen-source
edit was used.

