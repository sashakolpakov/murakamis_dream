# The complete central first plateau on the early second interval for 444

Private written deduction, 11 November 2026. At the original negative
second height, the old first-plateau message \(I_{44,P,N}\), multiplied
by the full next own-four kernel and the full second Fourier weight,
is exponentially small throughout \(1/10\le\Re y\le11/50\).
Both conditional sums are complete. The first cap, all physical
indices, aliases and joins are retained.

This does not yet bound the literal full message \(f_{44,N}\) on
that interval. Its exact difference \(R_{44,N}=f_{44,N}-I_{44,P,N}\)
remains a separate coherent source. Section 6 records the precise
remaining product, without assuming its old plateau estimate away
from that plateau.

## 1. Original source and normalization

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\). Keep its coupled reference \(r_j=a_j+ic_j\), ordinary
color, logarithmic lifts and following leg. Put
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad
 \kappa_0=1/2500000,
\]
\[
 a=x+ic_1,\quad y=q+ic_2,\quad z=u+ic_3,\qquad
 x,u\in P,\quad q\in E .
 \tag{1}
\]
The first44 bounds in equation (2) of
[the negative first-left source](research_mixed_complete44_second_selected_negative_left_connection.md),
and the ordinary typed bounds in
[retained-prefix calibration](research_mixed_retained_prefix_unselected_plateau.md),
give
\[
 -.078<c_1<-.020,\qquad
 -.102<c_2,c_3,h_s,h_t<-.001,\qquad
 a_2\in[.24,.36],
 \tag{2}
\]
where \(h_s=\Im s_2^*\), \(h_t=\Im s_3^*\).
We may use the weaker lower bound \(-.108\) for \(h_t,c_3\).
At \(m=4\) vertex three is ordinary and its following leg is
attached; it is not replaced by a terminal cap. All these are
necessary bounds on the original coupled family, not new independent
reference parameters.

Use \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(V)=(q_NV;q_N)_j\), and
\[
 U_{1,N}(w,X)=\sum_{i<N}H_N(w,q_N^{-i})p_i(X)/P_i^2,\qquad
 C_{1,N}(X,Y)=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \tag{3}
\]
Here \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\),
\(Z=e^{-2\pi iz}\), and \(d_N\) is the original polynomial
interpolating \(d_N(q_N^j)=1/P_j\). Define
\[
 \mathscr K_N(w;a,y,z)
 =U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z).
 \tag{4}
\]
Neither first nor second selected monomial occurs in (4).
The outgoing allocation is \(|d_N(Z)|^{1/2}\), including at zeros.

Retain the original phases
\[
 Q(s;b,c)=g(s+b)+g(s+c)-3g(s)-g(b)-g(c)+2\pi ibs,
\]
\[
 F_2(s;a,y)=Q(s;a,y)-\tfrac12g(a)-\tfrac12g(y),\qquad
 F_3(t;y,z)=Q(t;y,z)-\tfrac12g(y)-\tfrac12g(z),
 \tag{5}
\]
and \(L_1=\mathcal T_1-\tfrac12g\).
Writing \(\phi_2,\phi_3\) for their original stationary values,
set
\[
 \Lambda_{123}(z)=
 \Re\{L_1(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3)
                  +\partial_2\phi_3(r_2,r_3)(z-r_3)\}.
 \tag{6}
\]
This is the same three-factor affine action as in the old
unselected and selected plateau proofs. In particular its constant
is
\[
 \Re\{\mathcal T_1(r_1,-2)+\psi_1(r_1,r_2)+\psi_1(r_2,r_3)
                       -g(r_1)-g(r_2)-\tfrac12g(r_3)\}.
 \tag{7}
\]
No conditional/pre-Gram or terminal correction is added.

**Theorem 1.** On (1), both level parities and a sufficiently
small fixed ordinary-color disk about \(-2\) satisfy
\[
 |\mathscr K_N(w;a,y,z)|\,|d_N(Z)|^{1/2}
 \le C N^B\exp N\{\Lambda_{123}(z)-10^{-11}\}.
 \tag{8}
\]
Consequently the exact old first plateau
\[
 I_{44,P,N}(w,Y)=N\int_{P+ic_1}
       U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y)\,da
 \tag{9}
\]
obeys
\[
 |I_{44,P,N}(w,Y)d_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B\exp N\{\Lambda_{123}(z)-10^{-11}\}.
 \tag{10}
\]
The single density \(N\,da\) in (9) contributes only a polynomial
factor. No exterior whole-word scalar is changed. Fixed ordinary
color derivatives satisfy (8)--(10) on smaller disks, with polynomial
costs and a smaller fixed gap.

## 2. Cap allocation and the old-face anchors

The [complete cap plane](research_mixed_first_cap_plateau_completion.md)
gives
\[
 |U_{1,N}(w,X)|\,|d_N(X)|^{1/2}
 \le C_\tau N^{B_\tau}e^{N(B_L(x)+\tau)},
\]
\[
 B_L(x)=\Re L_1(r_1)+\Re L_1'(r_1)(x-a_1)
                                  -\kappa_0(x-a_1)^2 .
 \tag{11}
\]
This controls the whole cap, including its private aliases,
physical tails and true ends, on its actual fixed height.
The remaining incoming half at \(X\) has rate
\(-\Re g(a)/2\), by
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md).
Thus the outside quantity to attach to bare conditional profiles is
\[
                         B(x)=B_L(x)-\tfrac12\Re g(a).
 \tag{12}
\]
This substitution is made at the level of the product of bounds;
it divides by no finite Fourier factor. The two halves at \(X\)
in (11)--(12) give exactly \(d_N(X)\) in (4).

At \(q_0=11/50\), the
[ordinary-source theorem](research_mixed_three_row_source_assembly.md)
applies to both actual conditional references, with incoming type
four for each. It supplies the original main planes, the real
low and half-cut deficits \(1/2000\), and the strict typed last-row
comparisons, with every revived carrier retained. The first external
input to vertex two is attached; the last input to vertex three is
attached precisely when \(m=4\). Both products are among that
source's stated domains.

The original stationary identities are
\[
 L_1'(r_1)+\partial_1\phi_2(r_1,r_2)=0,\qquad
 \partial_2\phi_2(r_1,r_2)+\partial_1\phi_3(r_2,r_3)=0 .
 \tag{13}
\]
Hence the constants and tangents of these old-face comparisons
sum exactly to (6). In particular two shared quadratic losses
give
\[
 2\kappa_0(a_2-q_0)^2
 \ge 2\kappa_0(1/50)^2
 =1/3125000000>10^{-10}.
 \tag{14}
\]
No numerical margin is assigned to the typed last-row theorem:
only its strict sign is used. The quantitative reserve in (14)
or a real-cut reserve supplies each later comparison.

The earlier lower-left proofs were stated for a first-three cap.
Their cap was used solely through its complete plane and (13).
Here (11)--(13) supply the first-four replacement with the additional
incoming allocation kept explicitly. The wider first height in (2)
requires the three written repairs below; it is not an application
outside the printed first-three hypotheses.

## 3. Main profiles and both real cuts

First, the actual first height gives the sharper elementary bound
\[
 T_a=e^{-2\pi c_1}<33/20 .
 \tag{15}
\]
Indeed \(-2\pi c_1<39\pi/250<1/2\). Also
\[
 \log(33/20)
 =2\operatorname{arctanh}(13/53)
 >26/53+\frac{4394}{446631}>\frac12,
 \tag{16}
\]
where \(4394/446631>1/106\) follows from
\(465764>446631\).

The low-main clipping and horizontal bridge in Sections 2--4 of
[joint lower-left profiles](research_mixed_next_lower_left_joint_main_profiles.md)
now apply to (5). Here is the precise domain and allocation check.
The first low-main force uses only \(T_a\ge1\), \(r_s=e^{2\pi h_s}>1/2\),
and the first real target in \(P\). Its displayed positive quadratic
therefore raises every \(1/8\le s_R<1/6\) to \(1/6\).
The next own-four low-main force uses only negative \(c_2,c_3,h_t\)
and raises \(1/8\le t_R<1/6\) in the same way.

For the bridge from the actual reference to a shared target
\(q\in[1/5,q_0]\), all retained real coordinates after clipping
are in \([1/6,1/2]\), and every height has modulus at most \(.108\).
The determinant identity (8) of that proof makes
\(V(v,w)=g(v+w)-g(v)-g(w)\) horizontally concave there.
The exact decompositions in the present case are
\[
\begin{split}
 F_2&=V(s,a)+V(s,y)-g(s)-\tfrac12g(a)-\tfrac12g(y)+2\pi ias,\\
 F_3&=V(t,y)+V(t,z)-g(t)-\tfrac12g(y)-\tfrac12g(z)+2\pi iyt .
\end{split}
\tag{17}
\]
The extra \(-g(a)/2\), absent from the old first-three allocation,
adds a nonnegative negative-Hessian diagonal. The chirps have
purely imaginary horizontal Hessians. Thus the same straight
bridge retains (14). The positive shared-coordinate derivative
in equations (18)--(22) of that proof uses only
\[
 e^{2\pi c_2},r_s\in[1/2,1],\qquad e^{-2\pi h_t}>13/20,
\]
and not the first incoming height. It transports the bridge
bound through \(E\).

For the real-cut comparisons one additionally needs the first
upper-main clipping to \(s_R\le5/12\). This is the first repair.
On \(5/12\le s_R\le1/2\), set
\[
 D_s=1+r_s^2+12r_s/7,\qquad 1/2\le r_s\le1 .
\]
The incoming shifted cosine is greater than \(-2/3\), and the
own cosine is less than \(-6/7\), exactly as in Section 6.1 of
the joint-profile proof. Using (15), the incoming numerator
square is less than
\((33/20)^2+r_s^2+(11/5)r_s\). The other numerator is at
most \(1+r_s\). The needed two inequalities are
\[
\begin{split}
 D_s-\tfrac75(1+r_s)
 &=r_s^2+\tfrac{11}{35}r_s-\tfrac25\ge\tfrac1{140},\\
 \tfrac{49}{25}D_s-
       \{(33/20)^2+r_s^2+\tfrac{11}{5}r_s\}
 &=-\tfrac{61}{80}+\tfrac{24}{25}r_s^2+\tfrac{29}{25}r_s
 \ge\tfrac{23}{400}>0 .
\end{split}
\tag{18}
\]
Both right-hand polynomials increase for \(r_s\ge1/2\).
Consequently the squared force is less than
\((49/25)(1+r_s)^2/D_s^2<1\), as required.

Sections 6.2--6.3 of the same proof then transport all first-main
by next-real-cut and first-real-low by next-main/real-cut pairs
to \(q_0\). Their exact rational differences use only
\(e^{2\pi c_2}\in[1/2,1]\) and the clipped ranges, so they are
unchanged. For the first real half cut, its vertical comparison is
\[
 \Im Q_s(1/2+i\sigma;a,y)\ge\pi(x-q)\ge0,
                         \qquad h_s\le\sigma\le0 .
 \tag{19}
\]
Only the nonpositive outer heights enter (19).
Thus every pair of original main, real-low and real-half profiles,
with (12) and the shared/outgoing allocations attached, has rate
less than \(\Lambda_{123}(z)-10^{-10}\) on \(E\).

## 4. All physical upper rows and the last alternatives

The physical own-four rate and exact reflection are unchanged:
\[
 E_1(t;b,c)=I_b(t)+I_c(t)-3J(t)-2\pi t\Im b,\qquad
 I_b(t)=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv .
 \tag{20}
\]
For negative outer heights its last carrier is
\(-2\pi\Im b\). The reflected formula (3) of
[own-four upper rows](research_mixed_next_lower_left_own_four_upper_rows.md)
folds the incoming carrier into its numerator; no positive drift
is discarded.

That proof's first small reflected interval \(v\le1/5\) uses
only the centered-arc inequality, \(x\ge.22\), and \(T_a\ge1\).
On \(1/5\le v\le1/2\), its only upper use of the old first
height was the incoming modulus. The second repair is
\[
 |T_a-e^{-2\pi i(x-b)}|^2
 <(33/20)^2+1+\tfrac25(33/20)=\tfrac{1753}{400}
 <\tfrac{563}{128}<e^{3/2},
 \quad v\le b\le1/2 .
 \tag{21}
\]
Here \(|x-b|\le7/25\), so \(\cos(2\pi(x-b))>-1/5\).
The last rational number is the exponential polynomial through
degree four at \(3/2\). The cross-product difference for the
middle inequality is \(225200-224384=816>0\).
Hence the logarithm is still less than \(3/4\).
The outgoing modulus is at most two, with logarithm less than
\(7/10\). The original convex bound
\[
 \Phi(v)-\Phi(1/2)\le\tfrac{29}{20}(1/2-v)+3J(v)
 \tag{22}
\]
and its strict endpoint witness \(-21/2600\) are unchanged.
Thus every first upper row reduces positively to its half or last
rate. The next own-four upper-row proof is unchanged altogether:
it uses \(e^{-2\pi c_2}<2\), \(c_3<0\), and \(u\in P\).
Both reductions retain all \(j<N\), the last row \(N-1\), and
both half-grid parities.

The two one-last comparisons are also retained:

* [Next-four last row](research_mixed_next_lower_left_next_four_last_row.md)
  transports first-main/real-low profiles when \(e^{2\pi c_2}\le7/10\),
  using the repaired clipping (18). The first real half uses (19).
  Above that shared radius its own real-low row exceeds the next
  last carrier by \(1/1100\). Every displayed comparison is
  independent of the old numerical lower bound on \(c_1\).
* [First-last reduction](research_mixed_next_lower_left_first_last_four_reduction.md)
  transports the next main after clipping to \([1/6,9/20]\).
  The first carrier \(\delta_a=-2\pi c_1\) is constant in \(q\).
  Its real-low derivative is positive and its real-half overshoot
  is at most \(1/2250\), paid from the old \(1/2000\) half-row
  reserve. Thus the latter pair retains \(1/18000\).

The old-face anchors for these statements are those in Section 2,
with the incoming type-four allocation. The arguments do not use
a value of a first-three action or an evaluated typed last-row
margin.

For completeness, the double-last comparison needs the third
repair. Put \(R=e^{2\pi c_2}\), \(\delta_y=-2\pi c_2\) and
\(\nu_R(q)=-\Re g(q+ic_2)\). Its only \(q\) dependence is
\(\nu_R\), whose maximum occurs at
\[
 q_R=\frac{\arccos(R/2)}{2\pi}\in(1/6,q_0).
 \tag{23}
\]
This is exactly Section 2 of
[central lower-left completion](research_mixed_next_lower_left_central_four_completion.md).
At this point \(I_{q_R+ic_2}(1/8)\ge0\).
Moreover \(e^{2\pi c_1}>20/33\), and
\(\cos(2\pi(x+v))<1/5\) on \(0\le v\le1/8\).
The incoming squared modulus therefore exceeds
\[
 1+(20/33)^2-\tfrac25(20/33)=1+\tfrac{136}{1089}>1.
 \tag{24}
\]
So \(I_a(1/8)>0\). The same original inequality
\(-J(1/8)>3/20\) now gives
\[
 E_1(1/8;a,q_R+ic_2)-\delta_a
 >\tfrac9{20}-\tfrac78\delta_a
 >\tfrac9{20}-\tfrac{273\pi}{2000}
 >\tfrac{21}{1000},
 \tag{25}
\]
using \(\delta_a<39\pi/250\) and \(\pi<22/7\).
The first real-low cut paired with the next last carrier is
already paid. Equivalently its derivative is the positive
four-range ratio in Section 3 of the first-last reduction and
its old-face real-low deficit is \(1/2000\).
Replacing that real-low rate by the first last carrier therefore
loses at least the additional \(21/1000\) in (25).
This pays the double-last profile at its maximum (23), hence
through all of \(E\), with its original constants.

## 5. Complete finite inventory

Here is the direct source audit needed before passing from these
profiles to (8).

| Finite part | Original argument and the present domain check |
|---|---|
| Both positive low blocks, including \(j=0\) | Equations (5)--(10) of [low physical blocks](research_mixed_next_lower_left_low_physical_blocks.md). The first force uses only \(T_a\ge1\); its printed upper bound \(8/5\) is not used in that force. The next force and all numerator estimates are unchanged. |
| Both middle zero modes and both unweighted joins for each | Sections 5--6 of [complete lower-left currents](research_mixed_next_lower_left_complete_currents.md). First outer heights are nonpositive; next outer heights are nonpositive; private heights have modulus at most \(.108\). Its positive-cotangent comparisons and vertical convexity therefore retain their exact signs. |
| Both horizontal aliases and all four weighted vertical halves for each middle sum | Sections 3--4 of the same source, at heights \(-1/5,+4\). First bounds use the sign \(c_1<0\), not \(-.072<c_1\); all other radial guards use \(c_2,h_s,h_t,c_3\), which are unchanged. Thus its displayed strict argument bounds and original sampling penalties still apply. |
| Both positive upper blocks through \(N-1\) | The first incoming modulus is repaired in (21); the next upper-row proof is unchanged. Their half/last carriers are paid in Sections 3--4. |
| Full cap and all its private/end terms | Equation (11) is the complete cap supporting theorem at the actual first-four reference. No isolated cap profile is substituted for this bound. |
| Both full internal Fourier polynomials | At \(X\) and at \(Y\in E+ic_2\), the original lower-half Fourier criterion bounds their entire polynomials by the factorial rates, including forcing. The outgoing half at \(Z\) remains attached throughout. |

More explicitly the integer decomposition for each conditional sum is
\[
 0\le j<L_N,\quad L_N\le j<M_N,\quad M_N\le j<N,\qquad
 L_N=\lfloor N/8\rfloor+1,\quad M_N=\lceil N/2\rceil .
 \tag{26}
\]
The middle sum's half-grid cuts differ from \(1/8,1/2\) by
\(O(1/N)\). Its exact cotangent formula has the original \(+N\)
main density, two horizontal aliases, four weighted vertical halves,
and two unweighted joins after moving only the zero mode to its
actual private height. There is no omitted physical residue.
All shifted real arguments in these fixed contours stay in the
original regular strips because \(q\ge1/10\).

The quoted current bounds are pointwise in their outside factors.
They may therefore be applied to the two kernels successively
before multiplying by the full cap and weights. Sections 3--4 pay
every resulting main/cut/last pair. Uniform factorial and numerator
bounds retain zeros, both parities and the half-grid errors.
Choose all finitely many source tolerances within the common
profile reserve \(10^{-10}\). Their path lengths, finite sums
and original densities cost only powers of \(N\). Equation (8)
follows with the stated smaller gap; integrating proves (10).

The cap theorem provides a fixed ordinary-color disk after the
source allowance is chosen. Cauchy's formula on a smaller such
disk gives the derivative assertion. If a further small thickening
of \(a,y,z\) is wanted, square the entire expression in (4) and
multiply by \(d_N(Z)\). This is an integer-weight Laurent polynomial
of degree \(O(N)\); the
[horizontal continuation proof](research_mixed_horizontal_complex_extension.md)
gives any prescribed smaller gap on a fixed small neighborhood.
This statement concerns that whole integer-weight product, not
derivatives of separately weighted factors at a zero. No substantial
height change is inferred.

## 6. The exact remaining full-prefix source

Keep the literal definitions of
[pointwise prefix replacement](research_mixed_four_four_pointwise_prefix_replacement.md):
\[
 f_{44,N}(w,Y)
 =N\operatorname{CT}_X
     [U_{1,N}(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)],
\]
\[
 R_{44,N}(w,Y)=f_{44,N}(w,Y)-I_{44,P,N}(w,Y).
 \tag{27}
\]
All three functions are their exact finite polynomials in \(Y\).
Consequently, for every complex \(Y,Z,w\),
\[
\begin{split}
 f_{44,N}(w,Y)d_N(Y)C_{1,N}(Y,Z)
 ={}&I_{44,P,N}(w,Y)d_N(Y)C_{1,N}(Y,Z)\\
 &+R_{44,N}(w,Y)d_N(Y)C_{1,N}(Y,Z).
\end{split}
\tag{28}
\]
The first term is now paid on the substantial interval \(E\) by
(10), with every conditional row and current retained. The second
term is the specific remaining coherent source there. Its earlier
bound on \(P+ic_2\), including a small endpoint collar, does not
bound it on all of \(E+ic_2\). Neither the local packet for \(f_{44,N}\)
nor the fact that \(R_{44,N}\) is a polynomial removes this obligation.

This result makes no new complete-prefix bound on \(E\), no
second-selected bound there, and no full second-period or whole-word
claim. It also does not extend the full-kernel conclusion to next
own type three, whose upper physical rows require different control.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_next_lower_left_joint_main_profiles.md | 07844539d1ba13eadeba216be1f0888da9bbf43fc42e4e946f57199601289f3f |
| research_mixed_next_lower_left_low_physical_blocks.md | cd57a6112faab45b6737c3e154730029807a41b627ae1b7618d635361ca2485c |
| research_mixed_next_lower_left_complete_currents.md | 5d784371488e491be733f475f7f400df5b6230f6083e6e965b0fedfccbdc1d1a |
| research_mixed_next_lower_left_own_four_upper_rows.md | e67a0349acb90ced3c8c24d212388ec6f14237ce0935341a8243a18a849293f4 |
| research_mixed_next_lower_left_next_four_last_row.md | ac8bd37f1b7d775e57d51f33fcf455eb38405f62b442c9605202642c2899c641 |
| research_mixed_next_lower_left_first_last_four_reduction.md | a806c3a017d0362030c76ea560e33c6a51a5e5a284128715702f079212a519f0 |
| research_mixed_next_lower_left_central_four_completion.md | 4aa83b99cabd672c2200480b5abf778d8570e5e6e2ca940fdd99b187dd2b65bd |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_complete44_second_selected_negative_left_connection.md | 878cbd67c6035f6fb9903e76d0b719cae599874d852710d979282e711d7fbf77 |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The author read back the entire proof and all fourteen directly used
source implications, and checked their hashes. Independent full proof
and direct-source review is required before adoption. No mathematical
numerical evaluation, saved-value arithmetic, import, test, compilation
or frozen-source edit is used.
