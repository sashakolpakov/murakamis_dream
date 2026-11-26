# The finite nine-cell boundary chart and its actual residue packet

Private written proof, 17 November 2026. The literal finite summand
has a decoration-independent rational characteristic after shape
rescaling. Its generic entirely finite boundary is an explicit
pentagon surface. We give a first normal chart there and an oriented
rational residue representative of the actual \(1345\) elimination.
The resulting physical factorial packet is a boundary coefficient;
it is not the restricted action on the pentagon surface. No analytic
deformation of the original full-dilogarithm rays is asserted.

## 1. Exact finite ratios and a rational chart

Use the odd level \(N>2\), \(d=N-1\), and primitive root
\(Q=e^{2\pi i/N}\). The root called \(q\) in [S,C] is our \(Q\).
All source normalizations and charge phases remain those of [S].
Abbreviate the six numerator cells by
\[
 (u,v,t,r,s,z)=(1234,1245,2345,0123,0134,0145)
\]
and the three denominator cells by \(A=0125,B=0235,C=0345\).
Define at the finite level
\[
 (U,V,T,R,S,Z)
  =(\alpha_uQ^u,\alpha_vQ^v,\alpha_tQ^t,
     \alpha_rQ^r,\alpha_sQ^s,\alpha_zQ^z),\qquad
 \kappa_i=Q^{k_i},
\]
\[
 A=\frac{QRSZ}{\kappa_1},\qquad
 B=\frac{Q^2UVSZ}{\kappa_1\kappa_2},\qquad
 C=\kappa_4TVZ.                                      \tag{1}
\]
The same letters \(A,B,C\) now denote their normalized shapes.
The source support is \(\prod_i\kappa_i=Q^2\).

The nine exact shared-root identities [D,(12b)] cancel every
\(\alpha,\beta\) multiplier in the consecutive ratios of
[S,(16)]. Differencing its literal \(\Xi\) in [S,(17)] gives,
in the order \(u,v,t,r,s,z\),
\[
\begin{array}{lll}
 \displaystyle\frac{QTR(1-B)}{1-QU},&
 \displaystyle\frac{QRS(1-B)(1-C)}{1-QV},&
 \displaystyle\frac{QUS(1-C)}{1-QT},\\[5pt]
 \displaystyle\frac{QUV(1-A)}{1-QR},&
 \displaystyle\frac{QVT(1-A)(1-B)}{1-QS},&
 \displaystyle\frac{Q(1-A)(1-B)(1-C)}{1-QZ}.
\end{array}                                                   \tag{2}
\]
For example the \(u\)-step of \(\Xi\) is \(1+t+r\), and its
denominator step is \((1-B)/\beta_B\); the identity
\(\beta_u=\beta_B\alpha_t\alpha_r\) gives the first entry.
The other five identities give the other entries with the same
single \(Q\). These statements precede every limit and retain the
\(+1,+2\) arguments in (1). They require no limit of the auxiliary
root parameters.

Set the six ratios equal to one and clear their denominators.
This defines the finite rational characteristic being considered,
not an approximation theorem for the finite sum. Put
\[
 D_T=Q(U+T)-1+Q(1-Q)UT,\qquad
 D_R=Q(U+R)-1+Q(1-Q)UR.                              \tag{3}
\]
On the chart \(URTD_TD_R\ne0\), all six cleared equations are
equivalent to
\[
\begin{split}
 V&=\frac{D_T}{Q^2UT},\qquad
 S=\frac{D_R}{Q^2UR},\\
 B&=1-\frac{1-QU}{QTR},\\
 A&=1-\frac{QT(1-QR)}{D_T},\qquad
 C=1-\frac{QR(1-QT)}{D_R},\\
 Z&=Q^{-1}-(1-A)(1-B)(1-C),
\end{split}                                                     \tag{4}
\]
together with the three monomial equations (1).
For actual ratio-one points the denominators in (2) must also
be nonzero.

To prove (4), multiply the \(S\)-equation by \(QUR\) and use
the \(R,U\) equations. This gives
\[
 QUR(1-QS)=(1-QR)(1-QU),\qquad Q^2URS=D_R.
\]
Similarly \(Q^2UTV=D_T\). The \(U,R,T,Z\) equations now give
the other four entries of (4). Conversely these substitutions
give those four equations immediately, and the two displayed
polynomial identities give the \(S,V\) equations. This proves
the rational chart without an isolated-critical-point assumption.

## 2. The generic entirely finite limiting boundary

Let \(Q\to1\), with finite nonzero limits of the boundary clocks,
whose product is one. Suppose a sequence of points of the
characteristic has finite limits of all nine normalized shapes.
The cleared equations have the limiting form
\[
\begin{array}{ll}
1-U=TR(1-B),&1-V=RS(1-B)(1-C),\\
1-T=US(1-C),&1-R=UV(1-A),\\
1-S=VT(1-A)(1-B),&1-Z=(1-A)(1-B)(1-C),
\end{array}                                                     \tag{5}
\]
with (1) at \(Q=1\). If all nine limits are nonzero, the
elimination [D,(16)--(19)] still forces all \(\kappa_i=1\).
That elimination never divides by \(1\) minus a shape, so this
remains true even when some of the nonzero limits equal one.
Thus approaching shape one alone cannot evade that conclusion
for a sequence of ratio-one points.

Under the generic conditions
\[
 \kappa_1\ne1,\qquad \kappa_4\ne1,\qquad
                         \kappa_1\kappa_2\ne1,       \tag{6}
\]
every entirely finite limiting solution is on
\[
 Z=A=B=C=0,\qquad
 1-U=TR,\quad1-V=RS,\quad1-T=US,\quad
 1-R=UV,\quad1-S=VT.                                \tag{7}
\]
Conversely (7) satisfies all the limiting equations for every
nonzero boundary clock assignment.

Here are all possible zero cases, including intersections. A zero
of \(A,B,C\) forces a zero among \(U,V,T,R,S,Z\) by the monomials.
If none vanish, the nonzero elimination contradicts (6).
If \(V=0\), (5) gives \(R=S=1\), \(B=C=0\), and \(A=Z\);
since \(A=Z/\kappa_1\), this gives \(Z=0\). If \(S=0\), it gives
\(V=T=1\), \(A=B=0\), and \(C=Z=\kappa_4Z\), again \(Z=0\).
For the remaining cases use
\[
 1-v=s(1-c),\quad1-s=v(1-a),\quad1-z=(1-a)(1-c)
       \quad\Longrightarrow\quad sz=a,\quad vz=c.    \tag{8}
\]
This follows by substitution and uses no division.
If \(U=0\), then \(T=R=1,B=0\); (8) gives \(SZ=A,VZ=C\).
Conditions (6) force both \(SZ,VZ\) to vanish. If \(Z\ne0\),
then \(S=V=0\), contradicting the first equation in (8).
If \(T=0\), then \(U=S=1,C=0\), and the same identity gives
\(RZ=A,VZ=B\); use \(\kappa_1\ne1\) and
\(\kappa_1\kappa_2\ne1\). If \(R=0\), it gives \(U=V=1,A=0\)
and \(SZ=B,TZ=C\); use the other two conditions in (6).
Thus every case gives \(Z=0\), hence \(A=B=C=0\), proving (7).
Limits with infinite shapes are not classified here.

The torus part of (7) has the explicit two-parameter chart
\[
 R=\frac{1-U}{T},\qquad S=\frac{1-T}{U},\qquad
 V=\frac{U+T-1}{UT},                                 \tag{9}
\]
where \(U,T,1-U,1-T,U+T-1\) are nonzero.
This is the pentagon boundary, not a three-parameter physical
crossing action.

## 3. A first normal chart

Write \(\epsilon=Q-1\) and work over the torus part (9).
In the chart where the following limits are finite, put
\[
 Z=\epsilon z+o(\epsilon),\qquad
 U-1+TR=\epsilon f+o(\epsilon),\qquad
 (A,B,C)=\epsilon(A_1,B_1,C_1)+o(\epsilon).            \tag{10}
\]
Expansion of the exact rational chart (4) gives
\[
 B_1=\frac{f+1}{TR},\quad
 A_1=\frac{f+2-U-UT}{U+T-1},\quad
 C_1=\frac{f+2-U-UR}{U+R-1},\quad
 z=A_1+B_1+C_1-1.                                   \tag{11}
\]
All shapes on the right are their boundary values. For example
the numerator of \(B\) is \(Q(U+TR)-1\).
The numerator of \(A\), over \(D_T\), is
\[
 QU-1+Q(1-Q)UT+Q^2TR;
 \quad\epsilon^{-1}\text{ times this numerator }
       \longrightarrow f+2-U-UT.
\]
The calculation for \(C\) exchanges \(T,R\), and
\(Q^{-1}=1-\epsilon+o(\epsilon)\) gives the last equation.
The retained boundary clocks enter through
\[
 A_1=\frac{zRS}{\kappa_1},\qquad
 B_1=\frac{zUVS}{\kappa_1\kappa_2},\qquad
 C_1=z\kappa_4TV.                                    \tag{12}
\]
These are the first normal equations in the specified chart.
They do not assert that every limiting branch has this scale,
or that their solutions select the original period.

For a condensed form put \(P=UVTRS\) and
\(g=zP/(\kappa_1\kappa_2)\). Then
\[
 f+1=g,\qquad
 T(R-U)=g(\kappa_2-1),\qquad
 R(T-U)=g(\kappa_3^{-1}-1),                           \tag{13}
\]
\[
 z\left(\frac{RS}{\kappa_1}
       +\frac{UVS}{\kappa_1\kappa_2}+\kappa_4TV-1\right)=1.
                                                               \tag{14}
\]
In particular \(z\ne0\) here. Multiply (11) by \(UTV,TR,URS\)
and use \(\prod\kappa_i=1\) to obtain (13),(14).
They are equivalent to (11),(12) on (9).

The restricted phase is distinct from this normal dependence.
The primitive [D,(13)] restricts to
\[
 \mathscr S_{\rm face}
 =\sum_{Y\in\{U,V,T,R,S\}}\operatorname{Li}_2(Y)
 +\Log U\Log T+\Log U\Log R+\Log V\Log R
 +\Log V\Log S+\Log T\Log S.                          \tag{15}
\]
On a continued stationary logarithmic branch it is locally
constant: its five logarithmic derivatives vanish by (7).
On \(0<U,T<1,\ U+T>1\), it equals \(\pi^2/2\).
Indeed take \(U\to0,\ T=1-aU\), \(0<a<1\), in (9).
Then \(R,T\to1,S\to a,V\to1-a\), and the value becomes
\(\pi^2/3+\operatorname{Li}_2(a)+\operatorname{Li}_2(1-a)
+\log a\log(1-a)=\pi^2/2\).
The last identity follows by differentiation in \(a\) and its
value at zero. The physical dependence recovered below therefore
cannot be identified with (15).
For the fixed-log products normalized by \(W(0)=1\), their six
numerator and three inverse denominator factors also contribute
the additive constant \(-3\operatorname{Li}_2(1)=-\pi^2/2\).
Their normalized face action is consequently zero on this branch.
The separately retained \(\rho\) and edge scalar line is not
included in that normalization statement.

## 4. The actual \(1345\) pole, with orientation and co-source

After the three literal beta convolutions and polynomial expansions
in [C, Section 3], the actual remaining \(v\)-sum is
\[
 \sum_{v=0}^{d}\frac{Q^{nv}}{1-aQ^v},
 \qquad a=\alpha_{1345}Q^{t+1+\ell},\quad
 n=1+\ell+j,\quad r=[-n]\in\{0,\ldots,d\}.           \tag{16}
\]
Here \(a\ne0\) and \(a^N=\alpha_{1345}^N\ne1\) on the original
regular decoration domain. Define
\[
 \omega_{a,r}(\xi)
  =\frac{N a^r\xi^{N-r-1}}
          {(\xi^N-a^N)(1-\xi)}\,d\xi.                \tag{17}
\]
It is holomorphic at zero and infinity. Its poles are among
the actual sampling points \(\xi=aQ^v\) and the normalized
shape-one point \(\xi=1\). At a sampling point its residue is
\(Q^{-rv}/(1-aQ^v)=Q^{nv}/(1-aQ^v)\).
For the sum \(\Gamma_a\) of positive sampling circles and a
positive circle \(\gamma_1\) about one, the residue theorem gives
\[
 \frac1{2\pi i}\int_{\Gamma_a}\omega_{a,r}
  =-\frac1{2\pi i}\int_{\gamma_1}\omega_{a,r}
  =\frac{N a^r}{1-a^N}
  =\frac{N\alpha_{1345}^r}{1-\alpha_{1345}^N}
                   Q^{-n(t+1+\ell)}.               \tag{18}
\]
This is exactly [C,(16)], including orientation and prefactor.
The representative \(r=[-n]\) makes the differential holomorphic
at both zero and infinity. Using an unreduced positive Fourier
power instead would require its additional infinity contribution.

An arbitrary finite attachment is retained explicitly. Expand its
actual sampling values, including the phase, as
\(Q^{nv}H_v=\sum_{r=0}^d c_rQ^{-rv}\).
Replace the numerator in (17) by
\(N\sum_r c_ra^r\xi^{N-r-1}\). The same proof gives
\[
 \sum_v\frac{Q^{nv}H_v}{1-aQ^v}
       =\frac{N}{1-a^N}\sum_{r=0}^d c_ra^r.          \tag{19}
\]
Thus the co-source is a specified finite polynomial evaluation,
not its uninserted value. Matrix entries and holomorphic
parameters can be retained coefficientwise, as can all parameter
derivatives on the same regular chart. This is a rational
sampling-cycle statement; it does not identify the full-dilogarithm
ray cycle with \(\gamma_1\).

## 5. The retained final residue and physical packet

Use the exact integer representatives of [C]:
\[
 a_0=[-k_1],\quad m=[-k_2],\quad C_0=[k_3-1]+1,\qquad
 F(X)=\sum_{\ell=0}^{m}{m\brack\ell}_Q Q^{a_0\ell}
                  X^\ell(QX;Q)_{a_0+m-C_0-\ell}.    \tag{20}
\]
Negative Pochhammer indices mean the reciprocal products of
[C,(12)]. The original expansion contains both ordinary totals
\(d\) and \(2N-1\). Its exact value [C,(20)] is a retained
prefactor times
\[
 [X^d]F+
       \frac{\alpha_{0345}^N}{1-\alpha_{0345}^N}
                                      [X^{2N-1}]F. \tag{21}
\]
For \(C_0>a_0\), the poles of \(F\) are simple and among
\(1,Q,\ldots,Q^{C_0-a_0-1}\), and its polynomial part has
degree below \(d\). At each pole \(X^N=1\). Partial fractions
therefore give
\[
 c(\mathbf k)=[X^d]F=[X^{2N-1}]F
       =\operatorname{Res}_{X=\infty}F(X)\,dX
       =-\sum_{X\ {\rm finite}}\operatorname{Res}F(X)\,dX .
                                                               \tag{22}
\]
The equality of the two coefficients in (21), together with
\(\beta_{0345}^N=1-\alpha_{0345}^N\), supplies the factor
\(\beta_{0345}^{-N}\). The complete remaining array is
\[
 b(\mathbf k)=\mathcal J Q^{H-k_1}
   \beta_{0235}^{-m}\beta_{0145}^{-a_0}
   \alpha_{0345}^{d}\beta_{0345}^{C_0-m-N}
                                      c(\mathbf k),             \tag{23}
\]
where \(H=(3h_1-1)/2\) and \(\mathcal J\) is exactly [C,(4)],
including all three beta sums, nine normalizations, three powers
of \(N\), and original edge factors. Nothing in (23) is deleted
by the residue. For \(C_0\le a_0\) the array is zero, as in [C].

On its nonzero support put
\[
 J=a_0,\qquad u=C_0-a_0-1,\qquad v=m-u .
\]
Then \(J,u,v\ge0,\ J+u\le d,\ u+v\le d\), and [C,(26)] is
\[
 \boxed{\ c(\mathbf k)=
 Q^{Jv}\frac{p_{u+v}p_{J+u}}{p_vp_up_J},\qquad
 p_j=\prod_{r=1}^{j}(1-Q^r).\ }                      \tag{24}
\]
Outside this support it is zero. This is the physical factorial
packet for the crossing with positive sign, not a nonnegative
coefficient. Its complex phases remain in (24).
The actual port order from [D,(2)] is
\[
       (M_+^0)_{u+v,J;\,J+u,v}=x^{-J-v}c(\mathbf k),
       \qquad x=-e^{-\pi i/N}.                       \tag{25a}
\]
Indeed [C,(29),(31)] and [D,(2)] give
\(M_{v_{\rm out},u_{\rm out};a_{\rm in},b_{\rm in}}
 =Q^{-k_1}x^{u_{\rm out}-b_{\rm in}}c\);
use \(Q^{-k_1}=Q^J\) and \(Qx=x^{-1}\).
For the negative sector, the literal transport [S,(17b)] and
[C,(38)] gives
\(\Phi_{0001}=Q^{k_1-1}\Phi_{1000}=N^2c\) in the same
boundary coordinates. Substitution in [D,(3)] therefore gives
\[
 (M_-^0)_{J,d-v;\,d-u-v,J+u}
                    =x^{d-u-J-v}c(\mathbf k).       \tag{25b}
\]
All displayed head indices lie in \(0,\ldots,d\).
The coefficient symmetry in \(J,v\) is not a port interchange,
and the two exact \(x\)-phases are not suppressed.

Writing \(\alpha=Q^J,\eta=Q^u,\nu=Q^v\), the three packet
ratios, when the shifted indices stay in their actual support, are
\[
 \nu\frac{1-Q\alpha\eta}{1-Q\alpha},\qquad
 \frac{(1-Q\eta\nu)(1-Q\alpha\eta)}{1-Q\eta},\qquad
 \alpha\frac{1-Q\eta\nu}{1-Q\nu}.                    \tag{26}
\]
Their regular local limiting primitive is
\[
\begin{split}
 \mathscr S_{\rm packet}
 ={}&\Log\alpha\Log\nu
 -\operatorname{Li}_2(\eta\nu)-\operatorname{Li}_2(\alpha\eta)\\
 &+\operatorname{Li}_2(\eta)+\operatorname{Li}_2(\alpha)
  +\operatorname{Li}_2(\nu)-\operatorname{Li}_2(1).
\end{split}                                                     \tag{27}
\]
The three-parameter physical dependence is thus recovered in the
actual boundary coefficient, not in the constant face action (15).
Equations (18),(21)--(25b) retain the residues, phases, and carries
which perform that recovery. They neither select a nonzero
geometric component after arbitrary closing nor identify the
original analytic relative ray cycle with a positive ideal-cell
cycle.

## Complete direct sources

- [S] [Literal nine-cell source](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.
- [C] [Exact nine-cell evaluation](research_nine_cell_canonical_crossing_evaluation.md),
  SHA256 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9.
- [D] [Actual clocks and regular stationary gate](research_nine_cell_regular_stationary_gate.md),
  SHA256 a247b104782d41f125c302910e940ef9de0972ab97017f61437971975e8cbb61.

All complete direct texts were read and the used implications checked.
No mathematical program or numerical experiment was used.

