# Complete cap transport on the real incoming half-period

Private written deduction, 10 November 2026. For an actual initial44
reference, the complete first-four cap on every fixed real interval
\([1/2,1-\rho]\) is bounded by the larger of its original real
half-face profile envelope and \(9/10\). The original main current,
both horizontal sampling corrections, all their vertical pieces,
both unweighted joins, and every omitted physical row are retained.

This transports a complete cap upper bound. It does not replace
the real half-face envelope by a negative-height comparison plane,
pay an uncalibrated adjacent conditional factor, or prove a whole
period asymptotic.

## 1. Literal source and the original real half-face envelope

Fix an actual positive three/four word of length \(m\ge3\) beginning
with four and four. Keep its original reference and private height
from
[the half-face height-connection theorem](research_mixed_initial44_half_face_height_connections.md):
\[
 a_*=a_0+ic,\qquad .246<a_0<.350,\quad -.078<c<-.020,
 \qquad -.051<h_e<-.019 .
 \tag{1}
\]
Write \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and
\(p_j(X)=(q_NX;q_N)_j\). The literal cap is
\[
 U_{1,N}(w,X)=\sum_{j=0}^{N-1}
                  H_N(w,q_N^{-j})\frac{p_j(X)}{P_j^2}.
 \tag{2}
\]
The entire inner endpoint polynomial \(H_N\) remains coherent.

Use exactly the five bare profiles of that theorem, at the
real face \(a=1/2\):
\[
 \begin{split}
 A_0(0)&=\max_{27/100\le u\le49/100}
                       \Re\Psi_1(u+ih_e,1/2),\\
 A_L(0)&=\Re\Psi_1(27/100,1/2),\qquad
 A_R(0)=\Re\Psi_1(49/100,1/2),\\
 A_-(0)&=\max_u\Re\Psi_1(u-11i/200,1/2)-11\pi/100,\\
 A_+(0)&=\max_u\Re\Psi_1(u+i/25,1/2)-2\pi/25 .
 \end{split}
 \tag{3}
\]
Here \(S(e)\), \(J\), \(g\), and the type-four phase
\[
 \Psi_1(e,a)=S(e)+J(e+a)-J(a)-i\pi ea-g(e)
 \tag{4}
\]
have the original calibrated branches and constants.
Retain the same constant and envelope as in its equations (5)--(6):
\[
 E_*=\frac35+\frac{2\pi}{100}+\frac{\log4}{100}
          <\frac{69}{100},\qquad
 \mathcal A(0)=
 \max\{A_0(0),A_L(0),A_R(0),A_-(0),A_+(0),E_*\}.
 \tag{5}
\]
In particular \(\mathcal A(0)\) is an explicit maximum of
complete-source rates at the real half face. It is not the logarithm
of a signed cap value.

**Theorem 1.** For every fixed \(0<\rho<1/2\), every \(\tau>0\),
both level parities, and all \(w\in[-2,2]\),
\[
 \boxed{\quad
 |U_{1,N}(w,e^{-2\pi ix})|
 \le C_{\rho,\tau}N^{A_{\rho,\tau}}
       \exp N\{\max(\mathcal A(0),9/10)+\tau\},
       \qquad 1/2\le x\le1-\rho .
 \quad}
 \tag{6}
\]
The same rate holds after multiplication by either full first
weight \(d_N(X)X^{-N\epsilon}\), \(\epsilon=0,1\).
It holds on sufficiently small fixed ordinary-color disks and for
every fixed ordinary derivative on smaller disks, with a separately
reserved arbitrary rate allowance.

## 2. Fixed nonpositive-height profiles

Retain the exact private interpolant from
[the lower-right cap theorem](research_mixed_first_four_cap_lower_right_horizontal.md):
\[
 \mathscr A_{1,N}(e,a,w)=
 D_N(e)^{-1}\mathcal C_N(e,w)
             \frac{\Pi_N(a+e)}{\Pi_N(a)\Pi_N(e)} .
 \tag{7}
\]
Its numerator obeys the exact one-period identity
\[
 \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).
 \tag{8}
\]
On the new domain \(a=x\in[1/2,1)\) and
\[
 e=u+i\eta,\quad 27/100\le u\le49/100,\quad
                      -11/200\le\eta\le1/25,
 \tag{9}
\]
the numerator crosses at most one period wall. Its continuous
zero-safe upper rate is
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q<3/2 .
 \end{cases}
 \tag{10}
\]
This is the same exact continuation used in
[the upper-alias endpoint proof](research_mixed_initial44_upper_cap_alias_endpoint.md).
At a numerator zero the undivided multiplier in (8) is retained.
The two upper-rate expressions have the original continuous wall
limit. The regular denominator arguments are never shifted or
replaced.

For a fixed point \(e\), write its profile, including a fixed
sampling penalty \(p\ge0\), as
\[
 R_p(e,x)=\Re\{S(e)+J(e)-2g(e)\}
                    +\mathfrak p(x+e)-J(x)-p.
 \tag{11}
\]
For an unweighted main or joining point \(p=0\). For a weighted
vertical point \(p=2\pi|\eta|\); the two horizontal corrections
have their corresponding endpoint penalties.

**Lemma 2.** If \(\eta\le0\) in (9), then
\[
                         R_p(e,x)\le R_p(e,1/2)
                         \qquad(1/2\le x<1).
 \tag{12}
\]
The same assertion holds for a real private index \(0<e\le1/2\)
in its physical-row profile.

*Proof.* Put \(q=e^{2\pi\eta}\), \(\phi=2\pi u\), and
\(\theta=2\pi(1-x)\). On both sides of the period wall,
\[
 \partial_xR_p(e,x)
    =\log\frac{|1-qe^{-2\pi i(x+u)}|}
                    {|1-e^{-2\pi ix}|}.
 \tag{13}
\]
The squared numerator minus squared denominator is
\[
 L(\theta)=q^2-1+A\cos\theta-B\sin\theta,\qquad
 A=2(1-q\cos\phi),\quad B=2q\sin\phi .
 \tag{14}
\]
For the nonpositive-height retained points, \(0<q\le1\) and
\(0<u<1/2\), with \(A,B>0\),
\[
 L(0)=1+q^2-2q\cos\phi>0,\qquad
 L(\pi)=q^2-3+2q\cos\phi<0.
 \tag{15}
\]
The last strict bound follows from
\(q^2-3+2q\cos\phi<(q-1)(q+3)\le0\).
As in the upper-alias proof, \(L'\) has exactly one zero
on \((\pi/2,\pi)\), and changes there from negative to
positive. Since \(L(\pi)<0\), the function \(L\) has
exactly one zero on \((0,\pi)\). Reversing from \(\theta\)
to \(x\), the profile has one minimum and hence its maximum
on the closed rate interval is at \(x=1/2\) or \(x=1\).
Zeros at real numerator walls are interpreted by integrating
the logarithmic derivative.

Its endpoint difference is exactly
\[
 R_p(e,1/2)-R_p(e,1)=
                      \Re g(e+1/2)-\Re g(e).
 \tag{16}
\]
Here \(\eta\le0\), so the period term at the endpoint is zero;
the same fixed penalty cancels from the difference.
The original radial primitive
\(G_{-\eta}(v)=\Re g(v+i\eta)\), from
[the all-angle row theorem](research_mixed_all_angle_high_row_sign_class.md),
is nonpositive on \(0\le v\le1/2\), is odd and periodic,
and satisfies
\[
 G_{-\eta}(u+1/2)=-G_{-\eta}(1/2-u)\ge0 .
 \tag{17}
\]
Thus (16) is nonnegative, proving (12).

For a real physical index \(0<e<1/2\), take \(q=1\),
\(u=e\). All the preceding signs persist, and the same
endpoint comparison follows directly from \(J\).
At \(e=1/2\) use the continuous limit. The rate
\(\lambda(e)+I_x(e)-J(e)\) has exactly the derivative
(13), so this proves the physical-row assertion. \(\square\)

## 3. Positive vertical sampling pieces and the upper horizontal

For every fixed \(e=u+i\eta\) with
\(27/100\le u\le49/100\) and \(0\le\eta\le1/25\),
consider the actual weighted profile \(R_{2\pi\eta}\).
At \(x=1\), its numerator period term cancels its sampling
penalty exactly:
\[
 R_{2\pi\eta}(e,1)=
             \Re\{S(e)-i\pi(e-e^2)/2\}.
 \tag{18}
\]
The upper-alias endpoint proof establishes its critical-height
guard and derivative estimate on this entire rectangle,
not only on its top edge. In its notation,
\[
 \Im v_c(e)>\eta,\qquad
 \partial_\eta
    \Re\{S(e)-i\pi(e-e^2)/2\}<3\pi/50,\qquad
                       \Re S(u)<353/400 .
 \tag{19}
\]
Therefore, for every such height,
\[
 R_{2\pi\eta}(e,1)
       <353/400+3\pi/1250<9/10 .
 \tag{20}
\]
Also \(1\le q=e^{2\pi\eta}<4/3\).
With the private angles in (9), \(\cos\phi<0\) and
\(\sin\phi>0\). Thus (14) has \(A,B>0\),
\(L(0)>0\), and
\(L(\pi)<16/9-3<0\).
The same one-minimum argument applies, giving
\[
 R_{2\pi\eta}(e,x)
       \le\max\{R_{2\pi\eta}(e,1/2),9/10\}.
 \tag{21}
\]
This includes both positive vertical sampling halves and
the entire upper horizontal correction.
No vertical convexity at a newly crossed numerator wall
has been assumed.

At the original half face, Section 2 of the height-connection
theorem bounds both unweighted joins and all four weighted
vertical halves by the profiles in (3). Its unweighted joins
have heights between \(h_e<0\) and zero. Combining (12)
and (21) therefore bounds every point of the full retained
private contour by
\[
                           \max\{\mathcal A(0),9/10\}.
 \tag{22}
\]
The main current uses (12), as does the lower horizontal
sampling correction. The two real cuts and the negative
weighted halves use the same lemma. The positive halves and
upper horizontal use (21). This accounts for every retained
current without replacing its original half-face profile.

## 4. Every omitted physical row

At a compact real private index \(e=j/N\in(0,1)\),
the exact original normalization gives the whole-row rate
\[
            \mathcal R(e,x)=\lambda(e)+I_x(e)-J(e),
 \qquad
 I_x(e)=\int_0^e\log|1-e^{-2\pi i(x+t)}|\,dt .
 \tag{23}
\]
The complete coefficient is retained coherently in \(\lambda\).
The all-real-color coefficient bound used in the lower-right
cap proof supplies this same upper rate, with arbitrary
uniform allowance on every compact real-index interval.

For omitted compact rows below the left cut, Lemma 2
gives \(\mathcal R(e,x)\le\mathcal R(e,1/2)\).
The original half-face lower-tail monotonicity bounds the
latter by \(A_L(0)\).
For omitted compact rows from \(49/100\) to \(1/2\),
the same lemma and the original half-face upper-tail
monotonicity give the bound \(A_R(0)\).
These are exactly the real cuts retained in (3).

For \(1/2\le e<1\), put \(u=1-x\in[0,1/2]\).
Then \(u\le e\), and the exact entropy identity and inequality
from equations (12)--(13) of
[the far-right envelope proof](research_mixed_initial44_far_right_physical_envelope.md)
give
\[
           I_x(e)=J(u)+J(e-u)\le J(e).
 \tag{24}
\]
That source also retains the original global seam-profile
maximum and hence
\[
          \lambda(e)\le\lambda(1/2)<175/216<13/16
                                      \qquad(e\ge1/2).
 \tag{25}
\]
Therefore every such compact physical row has rate below
\(13/16<9/10\).
This step covers all rows past the incoming numerator wall;
it is not an endpoint principle for the signed cap sum.

The true finite-index endpoints are estimated separately.
Section 4 of the lower-right cap theorem proves, uniformly
on the entire closed disk \(|X|\le1\), common sufficiently
small fixed endpoint groups with rates below \(1/4\) and
\(3/5\), for all real ordinary colors and both parities.
Its literal coefficient identities retain every odd endpoint
and every physical zero. These ceilings are below \(9/10\).
Use these endpoint groups and the compact estimates above
for the remaining omitted physical rows. Thus no interior
packet is extrapolated to index zero or the last index.

## 5. Complete finite conclusion and the first weights

Apply the original marked cotangent identity to (7), on
the same two half-grid cuts and private heights used at
the half face. The coefficient remains on its original
rectangle. The numerator is continued by (8), keeping
the whole multiplier; no extra current is introduced at
its removable zero. The original \(+N\) constant mode,
the two horizontal sampling corrections, all four weighted
vertical halves and the two unweighted joins are unchanged.

Section 3 pays every retained current. Section 4 pays all
physical rows outside the cuts, including the genuine ends.
The original zero-safe factorial upper estimates are uniform
on every fixed \(x\in[1/2,1-\rho]\).
At a numerator wall, their continuous upper rates use (10);
one never divides by the numerator or drops a zero.
Half-grid displacements cost an arbitrarily small rate
allowance by the same uniform continuity and product
regularization as in the starting source.
Residue factors, finite sums, contour lengths and symbols
cost only a polynomial in \(N\). Distribute a single total
allowance below \(\tau\). Equations (22)--(25) and the
true-end estimates prove (6).

The first Fourier factor is the original polynomial, not
the factorial interpolant. The absolute theorem in
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md)
gives, on this fixed real interval, rate
\(\max\{-J(x),0\}=0\). The selected monomial \(X^{-N}\)
has modulus one. Multiplying by either full first weight
therefore preserves (6), retaining both forcing alternatives.
No allocation to an adjacent conditional kernel is changed.

All estimates are uniform for \(w\in[-2,2]\), by the
same complete-coefficient and finite-end real-color bounds
as in the cited source proofs. The literal cap has degree
less than \(N\) in \(w\). The original
[polynomial continuation argument](research_mixed_horizontal_complex_extension.md)
therefore gives a sufficiently small fixed ordinary-color
disk with any prescribed additional rate allowance.
Cauchy's estimates give all fixed derivatives on smaller
disks. Fourier weights are constant multipliers in this
argument and are not divided out, including at their zeros.
This completes the theorem.

The bound (6) explicitly retains
\(\max\{\mathcal A(0),9/10\}\).
In particular it does not replace \(\mathcal A(0)\) by
the allocated negative-height plane \(B_*\).
Applications must combine its two alternatives with
their respective original conditional comparisons.
The outgoing second coordinate, its halfweight, and
any later-coordinate sectors have not been estimated
by this cap theorem.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_initial44_upper_cap_alias_endpoint.md | adcb2a0a7c035c18a9ff6faa7a1b328c47687ee42c27f78c6a785828a513b67b |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The complete written proof and all directly used source
implications were read, and all seven bindings were checked.
No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation, source replay or frozen-note edit
was used. Independent review is required before adoption.
