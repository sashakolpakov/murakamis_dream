# The complete early first four/three pair at its actual fixed heights

Private written corollary, 10 November 2026. The signed one-wall
ordinary contour, together with the complete cap calibrations of its
two wall rates, pays every high row of an actual first four/three
pair. Adding the already proved low and central blocks gives a bound
for the literal complete pair. The first type-four Fourier weight is
retained in full; there is no outgoing own-three halfweight.

The wrapped block is estimated as a signed sum. No bound for the sum
of its absolute physical rows is asserted. All heights are the original
fixed reference heights. This is a finite-source upper bound, not a
whole-word or closed-knot asymptotic.

## 1. Original quantities and a common strict reserve

Fix an actual positive three/four open word of length at least three
beginning with four and three. Retain its coupled reference
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 e_*=u_*+ih_*,\qquad s_*=s_0+ih_0.
\tag{1}
\]
The actual first-four/three source gives
\[
 .246<a_0<.350,\quad -.070<c<-.020,\quad
 -.065\le d\le.068,\qquad -.108\le h_0\le.068.
\tag{2}
\]
There is no sign restriction on \(d\) or \(h_0\). The first
private endpoint and its original critical branch are unchanged.
Take targets
\[
 a=x+ic,\quad b=z+id,\qquad
 x\in E=[1/10,11/50],\quad z\in P=[11/50,9/20].
\tag{3}
\]
Set \(q_N=e^{-2\pi i/N}\), \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi ib}\), \(P_j=(q_N;q_N)_j\), and
\[
 R_{j,N}(a,b)=X^{-j}
 \frac{(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^2},\qquad
 C_{0,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b).
\tag{4}
\]
The first factor is the whole original cap \(U_{1,N}(w,X)\).
The complete unselected first weight is \(d_N(X)\); neither
a selected monomial nor \(1+X^{-N}\) is inserted.

With the original primitives and logarithmic lifts, use
\[
\begin{split}
 \Xi_1(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e)-\tfrac12g(a),\\
 F_{10}(s;a,b)&=g(s+a)+g(s+b)-2g(s)+2\pi ias
                                      -\tfrac32g(a)-g(b),\\
 L_1(a)&=\operatorname{stat}_e\Xi_1(e,a),\qquad
 \phi_{10}(a,b)=\operatorname{stat}_sF_{10}(s;a,b).
\end{split}
\tag{5}
\]
Here \(S\) is the original complete-end action and the critical
values use their original selected branches. Put
\[
\begin{split}
 \kappa&=1/2500000,\qquad \gamma_* =\kappa(a_0-11/50)^2,\\
 \Gamma(z)&=\Re L_1(a_*)+\Re\phi_{10}(a_*,b_*)
 +\Re\partial_b\phi_{10}(a_*,b_*)(z-b_0)-\kappa(z-b_0)^2.
\end{split}
\tag{6}
\]
These are the unchanged allocations and plane in the low, central,
unwrapped and last-row sources. In particular
\(L_1'(a_*)+\partial_a\phi_{10}(a_*,b_*)=0\).

Let \(\nu>0\) be a uniform Schur-complement constant from the
[positive-private-height first-four/three theorem](research_mixed_early_four_three_positive_private_central.md).
Use the common reserve
\[
 \gamma_{43}=\min\{\kappa,\nu/4\}(a_0-11/50)^2>0.
\tag{7}
\]
It is uniformly positive on the actual reference family, since
\(a_0-.22>13/500\). It is at most \(\gamma_*\) and less
than \(1/2000\). We do not strengthen the central source's
unevaluated curvature reserve.

## 2. Paying the two walls with the correct allocations

Write the full bare continuous ordinary rate as
\[
 E_0(s;a,b)=\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt
 +\int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt
                         -2J(s)-2\pi cs.
\tag{8}
\]
The allocated rate used with the cap is
\[
                  \mathcal R(s;a,b)=E_0(s;a,b)-\tfrac12\Re g(a).
\tag{9}
\]
Let \(\mathcal A(a)\) be the complete allocated cap envelope
from the [first-four/three last-row theorem](research_mixed_first_four_three_true_last_row_calibration.md):
its main profile, both real cuts and both aliases have phase
\(\Re\Xi_1\) with the original penalties; its true-end
alternative is retained separately. There is no physical upper-row
allowance for first type four.

The complete [unwrapped high-row proof](research_mixed_unwrapped_stationary_high_row_transport.md),
Section 5, gives the rate comparison itself, not merely a finite
value bound:
\[
           \mathcal A(a)+\mathcal R(1-z;a,b)
                                      \le\Gamma(z)-2\gamma_*.
\tag{10}
\]
The [last-row calibration](research_mixed_first_four_three_true_last_row_calibration.md),
Theorem 1 and its exact reflected rate, give
\[
 \mathcal A(a)+\mathcal R(1-x;a,b)
 \le\mathcal A(a)+\mathcal R(1;a,b)
                                      \le\Gamma(z)-\gamma_*.
\tag{11}
\]
Both inequalities apply individually to every regular cap profile
and to the separate true-end profile. No finite wall coefficient is
divided out, and no rate comparison is inferred from the upper bound
of a possibly zero physical row.

Set
\[
 B(a,b)=\max\{E_0(1-z;a,b),E_0(1-x;a,b)\}.
\]
Equations (9)--(11) imply
\[
           \mathcal A(a)+B(a,b)-\tfrac12\Re g(a)
                                     \le\Gamma(z)-\gamma_*.
\tag{12}
\]
This last half of the first Fourier weight is essential: the
other half was already included in \(\mathcal A\).

## 3. The literal signed high block

The actual ranges (2)--(3) are contained in the compact domain of
the [one-wall contour theorem](research_mixed_negative_height_wrapped_contour.md),
Theorem 1. Define the strict wrapped block
\[
 \mathcal W_N(a,b)=
       \sum_{\substack{0\le j<N\\1-z<j/N<1-x}}R_{j,N}(a,b).
\tag{13}
\]
For every positive tolerance \(\tau_1\), that theorem gives
\[
             |\mathcal W_N(a,b)|
                   \le C_{\tau_1}N^{A_{\tau_1}}
                                       e^{N(B(a,b)+\tau_1)}.
\tag{14}
\]
The original factor \(1-Y^N\) is included in this estimate. Its
exponential cost is exactly the full-period constant \(2\pi d_+\)
already in (8). When it vanishes, the strict wrapped block is exactly
zero. The proof does not divide by it or drop either of the two
Fourier terms in its undivided interpolation identity.

Multiplication of (14) by the complete cap and full \(d_N(X)\),
using (12), yields
\[
 |U_{1,N}(w,X)|\,|d_N(X)|\,|\mathcal W_N(a,b)|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{15}
\]
The cap's five profile families and true ends are kept until after
(12). The original Fourier continuation at \(c<0\) supplies the
full weight rate \(-\Re g(a)\), with precisely the two halves
in (9), (12). No Fourier value is canceled or inverted.

For an exact disjoint partition of every high physical index
\(j\ge\lceil N/2\rceil\), assign it to
\[
\begin{array}{ll}
 I_U:&j/N\le1-z\ \text{and}\ j/N<1-x,\\
 I_W:&1-z<j/N<1-x,\\
 I_L:&j/N\ge1-x.
\end{array}
\tag{16}
\]
The unwrapped theorem pays the sum of absolute rows in \(I_U\);
the last-row theorem pays the sum of absolute rows in \(I_L\).
Equation (15) pays the signed sum in \(I_W\). This convention
assigns any physical wall row exactly once. If \(x=z\), the
wrapped block is empty and the coincident wall belongs to \(I_L\).
Every subset used in the two absolute estimates remains within its
source theorem's complete physical index range.

Applying the triangle inequality only between these three complete
blocks proves
\[
 |U_{1,N}(w,X)|\,|d_N(X)|
 \left|\sum_{j=\lceil N/2\rceil}^{N-1}R_{j,N}(a,b)\right|
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{17}
\]
The bound is not asserted with absolute values inside the wrapped
sum. Its cancellation is the one licensed by the exact finite
one-wall contour, including its collars, main term, two aliases,
and every vertical correction with the original positive density
\(N\).

## 4. The complete pair and ordinary-color scope

**Theorem 1.** For every \(\tau>0\), every actual first
four/three reference above, and all fixed-height targets (3),
\[
 |U_{1,N}(w,X)C_{0,N}(X,Y)|\,|d_N(X)|
 \le C_\tau N^{A_\tau}
                       e^{N\{\Gamma(z)-\gamma_{43}+\tau\}}.
\tag{18}
\]
Both level parities, every original physical row and every cap
correction are included. The estimate holds for the whole real
ordinary-color interval and, with arbitrary additional tolerance,
on a sufficiently small fixed ordinary-color disk about \(-2\).
Every fixed ordinary-color derivative has the same rate on a smaller
disk, with polynomial cost.

*Proof.* Partition (4) into the exact ranges
\[
\begin{split}
 &0\le j\le\lfloor3N/20\rfloor,\\
 &\lfloor3N/20\rfloor<j<\lceil N/2\rceil,\\
 &\lceil N/2\rceil\le j<N.
\end{split}
\tag{19}
\]
The [joint low-row theorem](research_mixed_early_joint_low_tail.md)
pays the first block, even after taking each ordinary row's modulus,
with reserve \(1/2000\). For the second block, if \(h_0\le0\)
use the [complete central source](research_mixed_early_joint_central_source.md),
with reserve \(\gamma_*\). If \(h_0\ge0\), use the
first-four/three central theorem with reserve \(\gamma_{43}\).
Their exact central intervals agree with (19), including the odd
half-level shifts, and their original main, alias and join terms
have already been estimated before assembly. Equation (17) pays
the third block. All three estimates retain precisely
\(|U_{1,N}|\,|d_N(X)|\) and the same plane (6).
Since every reserve is at least \(\gamma_{43}\), splitting the
prescribed tolerance between the finite number of blocks proves
(18).

The complete cap envelopes used in all these proofs are uniform on
the whole real ordinary-color interval. The one-wall transform is
independent of that color. Dropping only the favorable angular loss,
and keeping the separate true-end bound, therefore proves (18)
there first. The product is polynomial of degree less than \(N\)
in the ordinary color. Interval polynomial continuation supplies a
fixed sufficiently small Bernstein ellipse and ordinary disk with
arbitrarily small exponential cost. Cauchy's formula on a smaller
disk gives the derivative conclusion. No error known only at
\(w=-2\) is continued in this argument. \(\square\)

This proves a complete finite first-pair upper bound at the original
fixed heights. Its first-coordinate Fourier alternative remains the
unselected one. No selected first monomial, changing-height join,
new terminal contraction, or full outside scalar has been introduced.
Any later multiplication by the remaining factors must use their
original halfweight allocations and critical marginal cancellation.
The theorem by itself asserts neither a nonzero pair contribution
nor a whole-word or knot asymptotic.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_first_four_three_true_last_row_calibration.md | a1571017529473e88dad8c0f5ec4f3592984a19040962e8279ca9dadb92257de |
| research_mixed_negative_height_wrapped_contour.md | 0f024a3f54087ab3b4fee6f6c992a2e9292644590fc78b21072d6104a0f5c2e6 |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_four_three_positive_private_central.md | b8ffb45bbb9eae0d144b0c2e219207509aa7a119543560b058dfca1734e7c289 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The complete proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or edit to a frozen source was performed.
