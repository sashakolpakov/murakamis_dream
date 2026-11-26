# A calibrated positive cap–physical-row bound on the far real right arc

Private written deduction, 10 November 2026. On the real interval
\([7/8,1-\rho]\), for any fixed \(0<\rho<1/8\), the complete
first-four cap multiplied by the low or high physical block of
the next-four conditional polynomial lies strictly below the
original initial44 affine action. The comparison retains both
first Fourier choices, the outgoing halfweight, all cap rows and
the actual coupled reference.

The positive bound is used only after the full inner endpoint
coefficient has been retained coherently. It is not a positive
replacement for that coefficient's Newton sum. The middle
conditional indices and a complete conditional contour remain
outside this theorem.

## 1. Source and original calibration

Fix an actual positive three/four word of length \(m\ge3\)
beginning with four and four. Use the same reference and notation
as the [right-half theorem](research_mixed_initial44_right_half_interval.md):
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\quad
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 -.102\le d\le-.001 .
 \tag{1}
\]
Let \(\kappa=1/2500000\), \(\delta_R=\kappa(9/20-a_0)^2\),
and let \(\Lambda(z)\) be that theorem's original affine pair
action. The new targets are
\[
 a=x,\quad 7/8\le x\le1-\rho,\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
 \tag{2}
\]
Put \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), and \(X=e^{-2\pi ix}\),
\(Y=e^{-2\pi ib}\). The literal factors are
\[
 U_{1,N}(w,X)=\sum_{i=0}^{N-1}
                H_N(w,q_N^{-i})\,\frac{p_i(X)}{P_i^2},
 \qquad
 R_{j,N}(X,Y)=\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{3}
\]
The full first weight is \(d_N(X)X^{-N\epsilon}\),
\(\epsilon=0,1\), and the outgoing allocation is
\(|d_N(Y)|^{1/2}\). No weight is divided out.

Let \(J\) denote the original real sine primitive, extended
continuously and periodically for modulus integrals:
\(J'(t)=\log|2\sin\pi t|\), \(J(0)=J(1/2)=J(1)=0\).
It obeys \(J(1-t)=-J(t)\) and \(J(t)\le0\) on
\([0,1/2]\). For \(H\ge0\), retain the original radial primitive
\[
 G_H(t)=\Re g(t-iH).
 \tag{4}
\]
It is odd and periodic, with \(G_H(t)\le0\) on \([0,1/2]\).
These are modulus primitives with their stated normalization;
no new primitive constant is inserted in an action.

## 2. An elementary global upper bound for the coherent coefficient

Write \(\lambda(s)=\Re S(s)\) for the original full-index
endpoint coefficient action, and
\(\lambda_*=\lambda(1/2)\). The
[complete-column theorem](research_mixed_symmetric_closing_complete_column_norm.md),
Sections 2 and 5, proves
\[
 f(s):=\lambda(s)+J(s)\le\lambda_*,
 \qquad \lambda_*<175/216<13/16 .
 \tag{5}
\]
Its exact derivative identities give a useful global estimate
without any saved action enclosure.

On \(0<s<1/2\), write the original square root
\(\sqrt{1-2e^{2\pi is}}=\alpha+i\beta\), where \(\beta<0\),
and put \(\zeta=\sqrt{1-\beta^2}\in(0,1)\). That source gives
\[
 f'(s)=\tfrac12\log\frac{1-\beta}{1+\beta},
 \qquad 2\sin^2\pi s=\zeta(1+\zeta).
 \tag{6}
\]
Differentiating these exact identities and using
\(\sin^2(2\pi s)=\zeta(1-\zeta^2)(\zeta+2)\) yields
\[
 f''(s)=-\frac{2\pi}{1+2\zeta}
                   \sqrt{\frac{\zeta+2}{\zeta}}
                      \le-\frac{2\pi}{\sqrt3}.
 \tag{7}
\]
Indeed the squared comparison is precisely
\[
 3(\zeta+2)-\zeta(1+2\zeta)^2
          =2(1-\zeta)(2\zeta^2+4\zeta+3)\ge0.
 \tag{8}
\]
Since \(J''(s)=\pi\cot\pi s\ge0\),
\(\lambda''\le-2\pi/\sqrt3\) there. At the midpoint
\(\lambda'(1/2)=-\log2\), again from the original identities.
Taylor's integral inequality, followed by completing a square,
therefore gives
\[
 \lambda(s)
 \le\lambda_*+\log2(1/2-s)
                       -\frac{\pi}{\sqrt3}(1/2-s)^2
 \le\lambda_*+\frac{\sqrt3(\log2)^2}{4\pi}
                 <\frac{353}{400}<\frac9{10}.
 \tag{9}
\]
For the last bounds use
\(\sqrt3<7/4\), \(\log2<7/10\), and \(\pi>25/8\);
their added term is less than \(343/5000<7/100\).
The logarithm bound has the positive-series witness
\(\log2\le2/3+2/81+1/540<7/10\).
For \(s\ge1/2\), (5) and \(J(s)\ge0\) give
\(\lambda(s)\le\lambda_*<9/10\). Thus (9)'s final ceiling
holds on the entire open physical index interval.

## 3. The whole positive outer-cap envelope

At a physical cap index \(e=i/N\), the exact normalization of
the [real-color coefficient theorem](research_mixed_endpoint_real_color_decay.md)
is
\[
 |H_N(w,q_N^{-i})|=|P_i|\,|C_N(e,w)|.
 \tag{10}
\]
On every fixed compact subinterval of \(0<e<1\), that theorem
bounds the whole coherent \(C_N(e,w)\), uniformly for
\(w\in[-2,2]\), by a polynomial times \(e^{N\lambda(e)}\).
No complete-color Newton value is divided out.
Consequently the continuous upper rate of the cap row in (3) is
\[
 \lambda(e)+I_x(e)-J(e),\qquad
 I_x(e)=\int_0^e\log|1-e^{-2\pi i(x+t)}|\,dt.
 \tag{11}
\]
Put \(u=1-x\in[0,1/8]\). Periodicity and oddness give exactly
\[
 I_x(e)=J(e-u)+J(u).
 \tag{12}
\]

If \(e\ge u\), the sine-binomial entropy inequality is
\[
                     J(u)+J(e-u)\le J(e),\qquad u\le e\le1.
 \tag{13}
\]
For a direct proof at \(u>0\), the difference
\(J(e)-J(u)-J(e-u)\) vanishes at \(e=u,1\).
Its derivative is
\(\log(\sin\pi e/\sin\pi(e-u))\), positive before
\((1+u)/2\) and negative afterwards. Thus the difference
is nonnegative. At \(u=0\) it is zero. Equations (9),
(11)--(13) bound all these compact rows by \(9/10\).

For \(0<e<u\), use instead the exact elementary coefficient
bound, valid for every ordinary real color:
\[
 |C_N(i/N,w)|
 \le\sum_{\ell=0}^{i}
        \frac{4^\ell}{S_\ell^3S_{i-\ell}},\qquad S_j=|P_j|.
 \tag{14}
\]
The complete endpoint proof supplies this literal inequality.
Since \(J\) decreases on \([0,1/8]\), the uniform sine-product
estimate bounds its rate by \(2e\log2-4J(e)\).
The other part of (11) is
\[
 I_x(e)-J(e)=J(u)-J(e)-J(u-e)
          \le A(u):=J(u)-2J(u/2)\le u\log2.
 \tag{15}
\]
The first maximum is at \(e=u/2\), by strict concavity and
symmetry on this interval. The second inequality follows from
\(A(0)=0\) and \(A'(u)=\log(2\cos(\pi u/2))\le\log2\).
Using \(e\le u\le1/8\) in (14)--(15), the cap-row rate is at most
\[
 3u\log2-4J(u)
 \le\frac38\log2-4J(1/8)
                     <\frac{21}{80}+\frac23=\frac{223}{240}.
 \tag{16}
\]
Here sine concavity gives \(2\sin\pi t\ge6t\) on
\([0,1/6]\), so
\[
 -J(1/8)\le\tfrac18\{1-\log(3/4)\}<\tfrac16,
 \tag{17}
\]
using \(\log(4/3)<1/3\). Every comparison is with a continuous
rate, not a finite cap row that might vanish.

The actual index ends are not inferred from a compact packet.
Section 4 of [the complete lower-right cap proof](research_mixed_first_four_cap_lower_right_horizontal.md)
gives common sufficiently small fixed endpoint groups with rates
less than \(1/4\) and \(3/5\), uniformly on the entire disk
\(|X|\le1\), all real colors and both parities. Their exact
coefficient formulas include the odd endpoint. Both ceilings
are smaller than \(223/240\).
On the remaining compact index interval use (10)--(16).
The numerator logarithms admit the original zero-safe uniform
upper Riemann estimate through \(e=u\); the integrable zero is
not divided out. Its rate allowance is arbitrary, and the
denominator factorial has uniform \(O(\log N)\) error.
Summing all at most \(N\) original cap rows proves
\[
 \boxed{\quad
 |U_{1,N}(w,e^{-2\pi ix})|
 \le\sum_{i=0}^{N-1}
        \left|H_N(w,q_N^{-i})\frac{p_i(e^{-2\pi ix})}{P_i^2}\right|
 \le C_\tau N^{A_\tau}e^{N(223/240+\tau)}
 \quad}
 \tag{18}
\]
for \(7/8\le x\le1\), both parities and all \(w\in[-2,2]\).
Thus this cap estimate itself retains every finite cap contribution;
there is no unpaid cap contour or alias in (18).

## 4. Physical ordinary rows reduce to calibrated half-face rates

For real incoming \(x\in[1/2,1]\), write their original rate as
\[
 E_x(t)=I_x(t)+G_{-d}(z+t)-G_{-d}(z)-3J(t),
                         \qquad 0\le t\le1.
 \tag{19}
\]
The incoming chirp has modulus one. There are two different
reductions:
\[
 \begin{split}
 E_x(t)&\le E_{1/2}(t),&&0\le t\le1/2,\\
 E_x(t)&\le E_{1/2}(1/2),&&1/2\le t\le1.
 \end{split}
 \tag{20}
\]
Neither compares two literal finite rows.

For the first, at fixed \(0<t\le1/2\) the derivative of
\(I_x(t)\) is
\(\log|\sin\pi(x+t)/\sin\pi x|\).
It is nonpositive up to \(x=1-t/2\), and nonnegative after
that point; the numerator zero is handled by integration.
The maximum on \([1/2,1]\) is consequently at an endpoint.
Those values are
\[
 I_{1/2}(t)=-J(1/2-t)\ge0,\qquad I_1(t)=J(t)\le0.
 \tag{21}
\]
This proves the first line, including \(t=0\) by continuity.

For the second put \(v=1-t\in[0,1/2]\) and \(u=1-x\).
The original reflected row identity gives
\[
 E_x(1-v)=J(u)-J(u+v)
        +G_{-d}(z-v)-G_{-d}(z)+3J(v).
 \tag{22}
\]
Lemma 1 of the
[all-angle high-row theorem](research_mixed_all_angle_high_row_sign_class.md),
applied only to the outgoing leg \(z\in(0,1/2)\), gives
\[
 G_{-d}(z-v)+J(v)+G_{-d}(1/2-z)\le0.
 \tag{23}
\]
The remaining expression satisfies
\[
                         J(u)+2J(v)-J(u+v)\le0.
 \tag{24}
\]
If \(u+v\le1/2\), the increasing derivative \(J'\) on
\((0,1/2)\) gives \(J(u+v)\ge J(u)+J(v)\), and
\(J(v)\le0\). If \(u+v\ge1/2\), use
\(J(u),J(v)\le0\) and \(J(u+v)\ge0\). Thus (22)--(24)
give
\[
 E_x(1-v)\le-G_{-d}(z)-G_{-d}(1/2-z)
                            =E_{1/2}(1/2),
 \tag{25}
\]
as asserted. The incoming angle need not be below one half:
only the outgoing leg uses the earlier legwise theorem.

## 5. The original affine rate pays the positive envelope

Let \(T=\mathcal T_1\) be the original bare first-cap action.
Use its bare plane at the old right plateau face, rather than
rename the allocated half-face plane:
\[
 B_0=\Re T(a_*)+\Re T'(a_*)(9/20-a_0)
                         -\kappa(9/20-a_0)^2 .
 \tag{26}
\]
The [sharper cap-floor proof](research_mixed_initial44_sharper_half_face_floor.md)
gives \(\Re T(a_*)>1\) and \(\Re T'(a_*)>-1/3\) in
this exact normalization. Since
\(0<9/20-a_0<51/250\), it follows that
\[
                         B_0>\frac{233}{250}-\kappa .
 \tag{27}
\]

Apply the formal-constant argument in Section 4, equation (10), of
[the physical-row comparison](research_mixed_initial44_lower_right_physical_rows.md),
retaining the bare plane \(B_0\) before a rational floor is used.
For clarity, if \(a_R=9/20+ic\) and \(\Delta=9/20-a_0\),
the actual cap allocated plane satisfies
\[
 B_L(9/20)-\{B_0-\tfrac12\Re g(a_R)\}
 =\tfrac12\Re\{g(a_R)-g(a_*)-g'(a_*)\Delta\}\ge0.
 \tag{27a}
\]
The inequality is the original convexity of \(\Re g\) on this
actual-height horizontal. Add (27a) to the complete ordinary
physical-row plane for
\(E(t;a_R,b)-\Re g(a_R)/2-\Re g(b)/2\). Original
stationarity cancels the first marginal and gives
\[
 B_0+E(t;9/20+ic,b)-\Re g(9/20+ic)-\tfrac12\Re g(b)
 \le\Lambda(z)-\kappa(z-b_0)^2-2\delta_R
 \tag{28}
\]
for the high rows and the left cut; lower rows reduce to that
cut. This is a comparison of formal rates, not a lower bound
on a cap modulus. The cap allocation uses the original convex
remainder of \(\Re g\), with the same reference marginal.

Hold \(B_0\) constant and transport (28) to \(1/2+ic\).
The first-coordinate derivative is
\(\log(N_t/D^2)<0\) for the cut and high rows, by that
same proof; the lower rows again reduce to the current cut.
At one half the first factorial rate is zero. Next increase
the incoming height from \(c\) to zero: equations (20), (23)
of [the half-face connection](research_mixed_initial44_half_face_height_connections.md)
show that every physical row is nonincreasing. Therefore
\[
 B_0+E_{1/2}(t)-\tfrac12\Re g(b)
 \le\Lambda(z)-\kappa(z-b_0)^2-2\delta_R,
 \quad t\in[0,2/25]\cup[1/2,1].
 \tag{29}
\]
No new conditional action value is required for (29).

The rational cap surplus is uniform:
\[
 B_0-\frac{223}{240}>
       \frac{17}{6000}-\kappa>\frac1{400},
 \tag{30}
\]
since \(17/6000-1/400=1/3000>\kappa\).
Equations (18), (20), and (29)--(30) now supply the desired
calibrated comparison with \(\Lambda\).

**Theorem 1.** For every fixed \(0<\rho<1/8\), every
\(\tau>0\), both parities and \(\epsilon=0,1\),
\[
\begin{split}
 &|U_{1,N}(w,X)d_N(X)X^{-N\epsilon}|\,
          |d_N(Y)|^{1/2}
     \sum_{j\in\mathcal I_N}|R_{j,N}(X,Y)|\\
 &\qquad\le C_{\rho,\tau}N^{A_{\rho,\tau}}
       \exp N\{\Lambda(z)-\kappa(z-b_0)^2-2\delta_R-1/400+\tau\},
 \\
 &\mathcal I_N=\{0,\ldots,\lfloor2N/25\rfloor\}
                  \cup\{\lceil N/2\rceil,\ldots,N-1\}.
\end{split}
 \tag{31}
\]
The targets are (2). The same rate pays limiting real cuts at
\(2/25,1/2\), with arbitrarily small fixed rate allowance for
their half-grid displacement. All real \(w\in[-2,2]\), fixed
sufficiently small ordinary-color disks, and fixed derivatives
on smaller disks are included.

*Proof.* The zero-safe row estimate in the all-angle source
bounds every literal ordinary row by its rate (19), with a
uniform arbitrary allowance and polynomial factor. Its proof
uses regularized numerator products on compact target sets and
the uniform denominator sine factorial; it applies also to
the real incoming interval (2). Apply the first line of (20)
to the low block and the second to the high block, then (29).
Multiply by the complete cap bound (18) and use (30).

The complete [Fourier upper bound](research_mixed_fourier_weight_continuation.md)
has rate \(\max\{-J(x),0\}=0\) on (2), and the selected
monomial has modulus one. The outgoing halfweight has its
original rate \(-\Re g(b)/2\); it was already present in
(29). Finite sums, parity shifts, original residue measures
and scalar powers have only polynomial cost. Divide one total
allowance among these bounds. This proves (31), retaining
every index in the two displayed blocks, including \(0,N-1\).

The cap's exact degree in \(w\) is less than \(N\).
Continuation from its whole real-color interval by the original
[ordinary-color extension](research_mixed_horizontal_complex_extension.md)
costs an arbitrary fixed rate allowance on a small fixed disk;
the remaining factors are constant multipliers in that argument.
Cauchy's formula supplies the fixed derivative bounds on smaller
disks. No outgoing halfweight is divided out, including at its
zeros. \(\square\)

This is a full-cap estimate against the displayed physical
conditional blocks, with the original affine rate explicitly
restored. It does not pay the intervening conditional physical
indices, its entire complex main or residue correction contours,
or the critical exponential on an uncalibrated starting region.
It does not by itself complete the real first-coordinate arc,
the first period, later-coordinate sectors or the open word.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_symmetric_closing_complete_column_norm.md | 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519 |
| research_mixed_endpoint_real_color_decay.md | 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_initial44_sharper_half_face_floor.md | eeb48098cf6a53eb7e9cee54ec1eb944f5607252e42550fbc69599f4a76c672a |
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The whole written proof and directly used source implications were
read; all ten bindings were checked. No mathematical numerical
evaluation, saved-value arithmetic, import, test, compilation or
frozen-source edit was used. Independent review is required before
adoption.
