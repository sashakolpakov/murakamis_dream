# A complete unit-incoming source for the negative outgoing shoulder

Private written proof, 11 November 2026. The original own-four
conditional polynomial has a complete ceiling when its incoming
coordinate is real between one half and seven eighths and its outgoing
coordinate has real part between \(.45\) and \(.5\), at a negative
height. The two noncritical carriers are the moving real-half-input
low rate and the real-half-input half rate. Every physical index and
every finite contour correction is retained.

The outgoing endpoint \(q=.5\) is proved separately below. This is
not an application of an open lower-half-plane branch theorem at a
boundary point. Attachment to the complete first cap and the original
three-factor affine action remains a separate comparison.

## 1. Exact source and statement

Put
\[
 r_N=e^{-2\pi i/N},\qquad P_j=(r_N;r_N)_j,\qquad
 p_j(V)=(r_NV;r_N)_j,
\]
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
The parameters in this note are
\[
 \frac12\le a\le\frac78,\qquad
 y=q+id,\qquad \frac9{20}\le q\le\frac12,\qquad
 -\frac{51}{500}\le d\le-\frac1{1000},
 \qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi iy}.
 \tag{2}
\]
In particular
\[
                 \frac{13}{25}<R:=|Y|<1.
 \tag{3}
\]
For the lower bound, the positive logarithm series gives
\(\log(25/13)>2(6/19+(6/19)^3/3)>51\pi/250\);
the last comparison follows using \(\pi<22/7\).

Retain the original primitive and phase
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,
 \qquad g'(z)=\operatorname{Log}(1-e^{-2\pi iz}).
 \tag{4}
\]
The logarithms initially lie in \(0<\Re z<1\), with their original
constants. Write \(s_*=u_*+ih_*\) for the original zero-lift
critical point, and \(\Theta(a,y)=Q(s_*;a,y)\).
Let
\[
\begin{split}
 J(t)&=\int_0^t\log(2\sin\pi v)\,dv,\\
 I_a(t)&=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv,\\
 I_y(t)&=\int_0^t\log|1-Ye^{-2\pi iv}|\,dv,\\
 E_a(t;y)&=I_a(t)+I_y(t)-3J(t),\\
 \ell(q)&=\frac{23}{40}-q\in[3/40,1/8],\\
 L_q(y)&=E_{1/2}(\ell(q);y),\qquad H_q(y)=E_{1/2}(1/2;y).
\end{split}
 \tag{5}
\]
All real integrals use their continuous limits at zeros.
The incoming chirp in (1) has modulus one on (2), but remains
in the complex phase (4).

**Theorem 1.** For every \(\tau>0\), uniformly on (2), through
both level parities,
\[
 \boxed{\quad
 |C_{1,N}(X,Y)|\le C_\tau N^{B_\tau}
 \exp N\{\max(\Re\Theta(a,y),L_q(y),H_q(y))+\tau\}.
 \quad}
 \tag{6}
\]
Every index \(0\le j<N\) is present. The coherent core retains
its \(+N\) density, and all six weighted cotangent currents retain
their \(N/(2i)\) coefficient. Neither a diagonal polynomial nor
an external halfweight has been removed.

The critical action also satisfies
\[
 \Re\Theta(a,y)\le\Re\Theta(1/2,y).
 \tag{7}
\]
For any fixed \(h_s\in[-51/500,-1/1000]\),
\[
 \Re\Theta(1/2,y)\le
 \max_{1/8\le u\le1/2}\Re Q(u+ih_s;1/2,y).
 \tag{8}
\]
The endpoint in this maximum is the continuous original one-sided
phase limit. Formula (8) is a formal profile comparison, not an
absolute bound for the physical middle rows.

## 2. The original branch at the closed outgoing endpoint

For \(q<1/2\), the
[unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
already covers (2): \(\Im Y<0,\Re Y<1\), with no extra restriction
on its radius. Its unique simple upper root \(v=e^{2\pi is_*}\) obeys
\[
 v(v-X)(v-Y)=X(v-1)^3,\qquad
                  0<\arg v<\Arg X,\qquad Q_s=0.
 \tag{9}
\]
Thus \(0<u_*<1-a\). We now prove the boundary \(q=1/2\),
where \(Y=-R\) with \(13/25<R<1\).

If \(\Im X>0\), a real root in (9) would, by equation (9) of
that source, satisfy
\[
             0=\Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
 \tag{10}
\]
It would be \(v=1\), which (9) excludes because \(Y\ne1\).
At \(X=-1\), the real cubic is
\[
               2v^3+(R-2)v^2+(R+3)v-1=0.
 \tag{11}
\]
Its derivative has discriminant
\(4(R^2-10R-14)<0\), and positive leading coefficient.
Hence the cubic has exactly one real root and a simple conjugate
nonreal pair. Its upper root is the limit of the same branch.
Along a compact parameter path no root can escape to infinity,
since \(1-X\ne0\). Thus the upper root remains unique and simple
also on this closed face.

The incoming-ray exclusion must be retained as well. In equations
(12)--(18) of the branch source, put \(v=sX\), \(s>0\),
\(\delta_X=1-\Re X\). At \(\Im Y=0\) their numerator
\(\mathcal N\) is zero. If \(s<1\), this gives
\[
 \delta_X=\frac{(1-s)(1+s-s^2)}{2s^3},\qquad
 \mathcal S(\delta_X)<0.
 \tag{12}
\]
Since \(s(s-1)<0\), the same exact identity yields \(\Re Y>1\).
If \(s>1\), the equation \(\mathcal N=0\) instead gives
\[
            \mathcal S=(s-1)^2+2\delta_X(s^3-1)>0,
 \tag{13}
\]
again yielding \(\Re Y>1\). Both contradict \(Y<0\).
At \(X=-1\) the ray is real and cannot contain the upper root.
Consequently both strict strip inequalities in (9) persist.
All phase arguments stay in the original strip, and continuation
of the already zero logarithmic lift proves \(Q_s=0\) here too.

The multiplier theorem uses
\[
                         \omega=\frac{v-X}{1-X}.
 \tag{14}
\]
Its boundary calculation excludes \(|\omega|=1\) by proving
\(\Im Y>0\), including the lower-half-plane multiplier case.
It therefore excludes that boundary at \(\Im Y=0\) too.
Continuity from \(q<1/2\) proves \(0<|\omega|<1\) on all of (2).
The unchanged stationary derivative
\(\exp\Theta_a=\omega\) proves (7), without resetting its logarithm.
Simplicity and all strict strip margins are uniform on the compact
set (2).

## 3. A fixed prewall core and all-height curvature

The proof of the
[fixed lower-cut theorem](research_mixed_four_unit_arc_fixed_lower_cut.md)
extends to (2), with the following explicit domain check.
When testing \(0<u\le2/25\), its outgoing argument bound
\(\alpha_{RU}(2\pi(q+u))\le14\pi/25\) still holds, and is stronger
when the shifted real part exceeds one half.
Its remaining-height modulus proof uses only
\[
 \cos(2\pi(q+u))<1/5,\qquad R>1/2,\qquad |X|=1.
 \tag{15}
\]
Here \(q+u\in[9/20,29/50]\), so the cosine inequality is immediate.
Consequently its exact inequalities
\[
\begin{split}
 A&>(U-1)^2+U/16,\qquad D<(U-1)^2+U/4,\\
 B&>1+U^2/4-U/5,\qquad B>24/25
\end{split}
 \tag{16}
\]
apply unchanged to the incoming, own, and outgoing squared moduli.
The two ranges \(1/2<U\le5/4\) and \(5/4\le U<8/5\) give
\(AB>D^3\) by that source's displayed positive polynomials.
For \(U\ge8/5\), the original argument contradiction applies.
The radius bounds in its Section 2 use only \(|Y|\le1\).
We have therefore proved on the new closed domain
\[
                    \frac2{25}<u_*<1-a,\qquad
                    \frac15<|v|<2.
 \tag{17}
\]

In fact \(U=e^{2\pi h_*}<3\). If \(U\ge3\), expand the three
original arguments as in Section 2 of the
[intermediate source](research_mixed_four_conditional_intermediate_real_source.md).
The leading sum is \(-\pi-2\pi q+2\pi u_*\), at most
\(-9\pi/10\), since \(u_*<1-a\le1/2\) and \(q\ge9/20\).
Its total error is less than
\[
                   4\arcsin(1/3)+\arcsin(2/3)<3\pi/4.
 \tag{18}
\]
The inequality uses \(\sin(\pi/8)>1/3\) and
\(\sin(\pi/4)>2/3\). This contradicts \(Q_s=0\).
Thus, with \(H_0=\log3/(2\pi)\),
\[
                         |h_*|<H_0.
 \tag{19}
\]

Choose the fixed lower cut \(\ell_0=3/40\), which lies below
the critical lower guard \(2/25\). Put \(\delta=1-a\).
For any real height \(\sigma\), on
\(\ell_0\le u<\delta\) one has
\[
 0<u<1/2,\qquad 1/2<a+u<1,\qquad 1/2<q+u<1.
 \tag{20}
\]
Therefore the original identity gives
\[
 \Re Q_{ss}(u+i\sigma;a,y)
 =\pi\{\Re\cot\pi(a+s)+\Re\cot\pi(y+s)-3\Re\cot\pi s\}<0.
 \tag{21}
\]
Both shifted cotangents are negative, and the own cotangent is
positive. This holds at every finite height. It supplies horizontal
strict concavity and vertical strict convexity without a height
correlation or a change of primitive.

## 4. A lower carrier that pays every postwall middle row

The half-input physical profile increases on \(0<t\le1/8\).
Its exact derivative is
\[
 e^{E'_{1/2}(t;y)}
   =\frac{2\cos\pi t\,|1-Ye^{-2\pi it}|}{(2\sin\pi t)^3}>1.
 \tag{22}
\]
Indeed \(q+t\in[9/20,5/8]\) has negative cosine, so the second
numerator exceeds one. The other numerator exceeds one, whereas
\((2\sin(\pi/8))^3<1\).
Hence \(L_q(y)\ge E_{1/2}(3/40;y)\).

Here is a uniform explicit lower bound for that carrier:
\[
       L_q(y)>
       \frac{63}{160}+\frac{27}{580}+\frac{27}{980}
       =\frac7{15}+\frac{809}{682080}
       >\frac7{15}+\frac1{1000}.
 \tag{23}
\]
We give the three estimates for this original continuous carrier,
not a proposed lower bound for a finite conditional sum.
First, sine bounded by its argument gives
\[
 -J(3/40)>\frac3{40}\{1+\log(70/33)\}>\frac{21}{160}.
 \tag{24}
\]
For the logarithm, summing the positive exponential tail after
its quadratic term gives
\[
 e^{3/4}
 \le1+\frac34+\frac9{32}
       +\frac{(3/4)^3}{6(1-3/16)}
 =\frac{881}{416}<\frac{70}{33}.
 \tag{25}
\]
The last comparison is \(29073<29120\).
Second, \(2\cos(\pi t)>19/10\) on \(0\le t\le3/40\), using
\(\cos z>1-z^2/2\) and \(3\pi/40<1/4\).
The first positive logarithm-series term gives
\(\log(19/10)>18/29\), so \(I_{1/2}(3/40)>27/580\).
Finally \(q+t\in[9/20,23/40]\) has cosine less than \(-7/8\):
\(\cos(3\pi/20)>7/8\) follows from
\(3\pi/20<33/70\) and the same cosine inequality.
Using (3),
\[
 |1-Ye^{-2\pi it}|^2>
 1+R^2+\frac74R>\left(\frac{29}{20}\right)^2.
 \tag{26}
\]
At \(R=13/25\), the last positive difference is \(779/10000\);
the left expression increases in \(R\).
Since \(\log(29/20)>18/49\), this gives
\(I_y(3/40)>27/980\). These prove (23).

The exact low/high comparisons in Section 4 of the
[far-right physical envelope](research_mixed_initial44_far_right_physical_envelope.md)
give, for the present real \(a\),
\[
 E_a(t;y)\le E_{1/2}(t;y)\quad(0\le t\le1/2),\qquad
 E_a(t;y)\le H_q(y)\quad(1/2\le t\le1).
 \tag{27}
\]
Their proof uses no upper bound \(q\le.45\): the first comparison
concerns only the incoming unit argument, while the second uses
the leg inequality on \(0\le q\le1/2\).
That inequality extends to \(q=1/2\) by its continuous limit.
Thus every low row \(t\le\ell_0\) is paid by \(L_q\), and every
high row is paid by \(H_q\).

For a postwall middle row, \(\delta\le t\le1/2\), exact periodicity
and sine entropy give
\[
 I_a(t)=J(\delta)+J(t-\delta)\le J(t),\qquad
 E_a(t;y)\le I_y(t)-2J(t).
 \tag{28}
\]
The complete numerator estimate, with \(R<1\), bounds
\(I_y(t)\le -2J((1-t)/2)\).
The written scalar bound in the
[low-index kernel proof, Lemma 1](research_mixed_next_low_index_kernel_margin.md)
is
\[
 \max_{0\le t\le1}
 \{-2J((1-t)/2)-2J(t)\}<7/15.
 \tag{29}
\]
Equations (23), (28), and (29) pay the entire postwall middle by
\(L_q-1/1000\), retaining every outgoing dependence in \(L_q\).

Compactness now permits a fixed sufficiently small \(\eta>0\)
such that
\[
 \ell_0<u_*<r(a):=\delta-\eta<\delta,\qquad
 E_a(t;y)<L_q(y)-1/2000
                   \quad(\delta-\eta\le t\le\delta)
 \tag{30}
\]
throughout (2). This uses the strict critical margins (17) and
uniform continuity of the integrated real profiles at the wall.
All omitted physical rows are therefore paid by \(L_q\) or \(H_q\).
The exact zero-safe factorial estimates in the cited sources apply
through \(j=0,N-1\), at both parities.

## 5. Both weighted horizontals, all sides, and both unweighted joins

On the whole fixed prewall core
\(\ell_0\le u\le r(a)\), set
\[
 I(u,\sigma)=\Im Q_s(u+i\sigma;a,y),\qquad
 {\cal R}(u,\sigma)=\Re Q(u+i\sigma;a,y).
 \tag{31}
\]
By (21), \(I\) strictly decreases with \(\sigma\).
The exact original argument limits give
\[
 \lim_{\sigma\to+\infty}I
       =-\pi-2\pi q+2\pi u\ge-37\pi/20.
 \tag{32}
\]
The two shifted arguments are nonpositive at every radius, while
the own argument is positive. Hence also
\[
                         I<2\pi a\le7\pi/4.
 \tag{33}
\]
These are statements on the original strip logarithms. Thus
\[
\begin{split}
 \partial_\sigma({\cal R}-2\pi\sigma)&<-3\pi/20
                                                   &&(\sigma\ge0),\\
 \partial_\sigma({\cal R}+2\pi\sigma)&>\pi/4
                                                   &&(\sigma\le0).
\end{split}
 \tag{34}
\]
Every weighted vertical half is bounded by its current real cut.
If \(M\) is an upper bound for \({\cal R}(u,0)\) on the compact
core family and \(m\) a lower bound for \(\Re\Theta\), choose a
fixed \(T>H_0+1\) with \(3\pi T/20>M-m+1\).
Both full weighted horizontal rates at heights \(\pm T\) are
then less than \(\Re\Theta-1\).
The choice precedes \(N\); no contour is sent to infinite height.

The two unweighted joins from the real cuts to height \(h_*\)
are controlled by vertical convexity (21).
Their real endpoints are paid by \(L_q\), with the additional
right-cut reserve (30); their main-height endpoints are bounded
by \(\Re\Theta\), because horizontal concavity and \(Q_s=0\)
place the maximum at the same original critical point.

## 6. The literal finite residue identity

Retain the exact numerator and reciprocal factors
\[
 \Pi_N(w)=G_N(Nw)
  \exp\{\tfrac{\pi i}{2}[N(w-w^2)-w]\},\qquad E_N(w)=1/\Pi_N(w)
 \quad(0<\Re w<1),
 \tag{35}
\]
and
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                              E_N(a)E_N(y)E_N(s)^3.
 \tag{36}
\]
The [joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md),
equations (2), (4), and (6), proves the exact recurrence and
physical equality. Thus \(T_N(j/N)\) is the summand in (1);
it is not merely an off-grid representative agreeing asymptotically.
All factorial arguments on the chosen rectangle remain in fixed
compact subsets of \(0<\Re w<1\), at arbitrary fixed heights.

Use the half-grid cuts
\[
\begin{split}
 L_N&=\lfloor N\ell_0\rfloor+1,\qquad M_N=\lceil Nr(a)\rceil,\\
 \ell_N&=(L_N-\tfrac12)/N,\qquad r_N=(M_N-\tfrac12)/N.
\end{split}
 \tag{37}
\]
They still enclose the critical point and remain prewall for
sufficiently large \(N\). The exact split-cotangent identity,
equations (34)--(36) of the intermediate source, gives
\[
 C_{1,N}=C_N^{\rm low}
          +N\int_{\ell_N}^{r_N}T_N(s)\,ds
          +{\cal E}_N+C_N^{\rm later},
 \tag{38}
\]
\[
 {\cal E}_N=\frac{N}{2i}
 \left\{\int_{\partial R^+_{\rm off}}T_N(\cot\pi Ns+i)\,ds
       +\int_{\partial R^-_{\rm off}}T_N(\cot\pi Ns-i)\,ds\right\}.
 \tag{39}
\]
The induced orientations are unchanged. There are two horizontal
weighted currents and four vertical half-currents. The low sum is
\(j<L_N\); the later sum is \(j\ge M_N\), through \(N-1\).
Section 4 pays both complete sums.

Deform the unweighted integral in (38) to height \(h_*\), retaining
both oriented joins. Section 5 pays all these terms. On half-grid
verticals the matching cotangent remainder has modulus at most
\(2e^{-2\pi N|\Im s|}\), and on the two fixed horizontals at
most \(4e^{-2\pi NT}\), for large \(N\).
The canonical finite-height factorial bounds bound (36) by its
original \(Q\) rate with polynomial cost. The strict margins,
the \(O(N^{-1})\) cut displacements, and the zero-safe physical
row errors fit any prescribed total allowance \(\tau\).
This proves (6), retaining all factors and both parities.

For (8), fix the real coordinate \(u_*\) of the half-input
critical point. All-height vertical convexity and
\({\cal R}_\sigma(u_*,h_*)=0\) give
\[
 \Re\Theta(1/2,y)\le\Re Q(u_*+ih_s;1/2,y).
 \tag{40}
\]
If \(u_*\ge1/8\), this is included in the stated maximum.
If \(2/25<u_*<1/8\), the fixed-height profile increases to \(1/8\).
Indeed, putting \(U=e^{2\pi h_s}\in(1/2,1)\), both shifted
squared moduli exceed one, while
\[
 |1-Ue^{-2\pi iu}|^2
 \le\max_{U=1/2,1}\{1+U^2-\sqrt2\,U\}<3/5
                         \quad(2/25\le u\le1/8).
 \tag{41}
\]
The incoming carrier at \(a=1/2\) has modulus one.
The exact main force therefore exceeds one.
Its real logarithmic derivative is positive, proving (8).
The endpoint phase limit at \(u=1/2\) is finite because \(h_s<0\)
and \(d+h_s<0\); no finite row at that endpoint was substituted.

## 7. Scope and attachment still required

The theorem supplies a complete source on the real first arc
\([1/2,7/8]\) for the negative outgoing shoulder, with a strict
postwall carrier reserve and an original critical-action comparison.
It does not estimate a positive replacement for the coherent core.
External complete caps, either full first Fourier term, the whole
second diagonal polynomial, and the third halfweight may be
multiplied literally, including at their zeros.

To obtain a full \(f_{44,N}\) shoulder theorem one must still
calibrate these three carriers with those external factors and
the unchanged \(\Lambda_{123}\), and combine the other first
contour pieces. Neither that attachment nor a full second-period
or nonzero whole-word conclusion is asserted here.

## Direct source versions

| Source | Direct implication | SHA-256 |
|---|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | original cubic, real-root and ray identities, zero lift | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_conditional_unit_multiplier.md | exact unit-multiplier exclusion, including lower-half multipliers | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |
| research_mixed_four_unit_arc_fixed_lower_cut.md | complete lower-cut force proof and radius bounds, with new outgoing range checked in Section 3 | a2e6a56f0ff12705e6c2b7a738122ed5bd98d095cfef6bb7a593a864b2c06293 |
| research_mixed_four_conditional_intermediate_real_source.md | exact full residue identity, finite-height symbols and all finite corrections | e5eff44816440f4675f6a216d09f614330ebe4f72a2bdcc2ddf20939b711710d |
| research_mixed_initial44_far_right_physical_envelope.md | exact incoming low/high reflection and postwall entropy identities | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_next_low_index_kernel_margin.md | full disk numerator bound and written \(M_1(0)<7/15\) | 35de8662e57070a4f19aef409f82c921283493ba3f0e17268f1c11a7eac1738c |
| research_mixed_all_angle_high_row_sign_class.md | legwise inequality and zero-safe finite upper estimates through both true ends | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_fourier_right_cap_joint_global_chart.md | exact numerator/reciprocal factorial recurrence and off-grid identity | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |

The author read back the entire proof and all eight directly used
source implications, and checked their listed versions. Independent
full proof and direct-source review is required before adoption. No
mathematical numerical evaluation, test, import, compilation, or
frozen-source edit is used.
