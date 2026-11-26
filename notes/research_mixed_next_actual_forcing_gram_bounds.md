# Positive Gram bounds for the actual next-three forcing

Research deduction, 7 November 2026. The forcing polynomial in the
first-cardinal outgoing equation is a specified row of the square of
the original positive three-crossing operator. Its complete circle
norm is therefore an actual fourth cap moment. The already proved
second and third cap moments give a substantially sharper range for
that norm than a generic operator estimate.

The same identification gives an explicit, zero-safe angular bound
for the entire forcing polynomial. It does not prove the required
small rate on the correlated next-output family, and it does not
remove the remaining outgoing inverse. No numerical evaluation is used.

## 1. Exact positive conjugacy at the physical nodes

Keep the original conventions
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,\quad S_j=|P_j|,
 \qquad p_j(Z)=(rZ;r)_j .
 \tag{1}
\]
Let \(M\) be the original crossing, \(J\) the Newton reversal, and
\[
 A_3=JM^3,\qquad H=M^*M,\qquad
 U=\operatorname{diag}((-q)^{-j})_{j=0}^D .
 \tag{2}
\]
Thus \(U\) is unitary and \(Ue_0=e_0\). The positive-cycle theorem
proves \(MA_3M^{-1}=\kappa H\) in the full original algebra.

Write
\[
 C_0(Y,Z)=\sum_{j=0}^D
             \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2},
 \qquad K_{ab}=C_0(r^a,r^b).
 \tag{3}
\]
The exact conditional/Fourier bridge, equation (6), together with
the original basis change
\[
 S=\kappa^{-1}\operatorname{diag}(P_j^{-1})UM,
 \tag{4}
\]
gives
\[
 K\operatorname{diag}(P_j)S
       =\kappa^{-1}\operatorname{diag}(P_j)SA_3.
 \tag{5}
\]
Substitute (4), cancel the invertible \(M\), and use (2):
\[
                         \boxed{K=UHU^*.}
 \tag{6}
\]
In particular \(K\) is positive Hermitian. Alternatively, on the unit
circle the finite products give directly
\[
 C_0(Y,Z)=\sum_{j=0}^D\overline{f_j(Y)}f_j(Z),
                       \qquad f_j(Z)=p_j(Z)/P_j.
 \tag{7}
\]
The star in (6) belongs to this particular positive representation.
No Hermitian pairing is inserted in an ordinary tangle contraction.

Let \(d_N\) be the degree-\(D\) polynomial with
\(d_N(r^b)=P_b^{-1}\), and let \(V_{0,N}\) be the actual forcing in
[the outgoing equation](research_mixed_next_low_cardinal_outgoing_equation.md).
That source theorem proves, with every finite row retained,
\[
 C_0(1,Z)=Nd_N(Z),\qquad
 V_{0,N}(Z)=\kappa^2N^2\operatorname{CT}_Y[d_N(Y)C_0(Y,Z)].
 \tag{8}
\]
The \(Y\)-band in the constant term is contained in \([-D,D]\).
Exact root averaging, with no selected second frequency, therefore
gives
\[
 \boxed{\quad
 V_{0,N}(r^b)=\kappa^2(K^2)_{0b},
 \qquad
 V_{0,N}(Z)=\kappa^2 e_0^TH^2U^*\mathfrak l(Z),
 \quad}
 \tag{9}
\]
where
\[
 \mathfrak l_b(Z)=\frac1N\sum_{k=0}^D(Zr^{-b})^k.
 \tag{10}
\]
Indeed \(K_{0a}=N/P_a\), so the physical sum in (8) is the
zeroth row of \(K^2\). Both sides of (9) have degree at most \(D\),
which proves its polynomial assertion. This uses the exact physical
ordinary input \(c_0=2\cos(\pi/N)\), whose Newton vector is \(e_0\);
it is not continuation of a complete-color packet to \(c_0\).

## 2. A fourth-moment identity for the whole circle norm

Put
\[
 \mu_{m,N}=e_0^*H^m e_0,\qquad
 \|F\|_2^2=\int_0^1|F(e^{2\pi ix})|^2\,dx,\qquad
 \|F\|_R=\max_{|Z|\le R}|F(Z)|.
 \tag{11}
\]
The full positive cap moments, their original closing words, and their
normalizations are established in
[positive three-crossing cycles, Section 3](research_positive_three_crossing_cycle.md)
and [the sharp cap seed](research_positive_three_crossing_cap_seed.md).

**Theorem 1.** At every level of either parity,
\[
 \boxed{\qquad
 V_{0,N}(1)=\kappa^2\mu_{2,N}
          =\kappa^2N^2\sum_{b=0}^D S_b^{-2},
 \qquad
 \|V_{0,N}\|_2^2=\frac{\mu_{4,N}}N.
 \qquad}
 \tag{12}
\]
In particular
\[
 \sqrt{\frac{\mu_{4,N}}N}
       \le\|V_{0,N}\|_1\le\sqrt{\mu_{4,N}},
 \qquad
 \frac{\mu_{3,N}^2}{\mu_{2,N}}\le\mu_{4,N}
                         \le\|H\|\mu_{3,N}.
 \tag{13}
\]

*Proof.* The first equation follows from (9) and (6).
Equivalently, (7)--(8) give
\[
 V_{0,N}(1)=\kappa^2N^3\int_0^1
                         |d_N(e^{2\pi ix})|^2\,dx.
 \tag{14}
\]
Parseval and exact root averaging for a degree-\(D\) polynomial
identify the integral with \(N^{-1}\sum_bS_b^{-2}\).
For the second equation in (12), the same averaging and (9) give
\[
 \|V_{0,N}\|_2^2
  =\frac1N\sum_b|(K^2)_{0b}|^2
  =\frac1N(K^4)_{00}=\frac{\mu_{4,N}}N.
 \tag{15}
\]
An \(N\)-coefficient polynomial has circle supremum at most
\(\sqrt N\) times its circle \(L^2\) norm, by Cauchy--Schwarz
on its monomial coefficients. Its supremum is at least its \(L^2\)
norm. This proves the first pair in (13).
The positive spectral measure of \(H\) gives
\(\mu_3^2\le\mu_2\mu_4\) and
\(\mu_4\le\|H\|\mu_3\), proving the remainder. \(\square\)

Let
\[
 c_{\rm b}=-2J(1/6),\quad
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\quad
 A_*=\max_{0<t<1/2}\{\Re I(t)-2J(t)\},
 \tag{16}
\]
with the original branch \(I\) of the proved next-crossing column.
The cited cap-seed theorem supplies
\[
 \mu_{2,N}=C_2N^{3/2}e^{Nc_{\rm b}}(1+O(N^{-1})),\quad
 \mu_{3,N}=C_3N^{3/2}e^{2NA_*}(1+O(N^{-1/2})),
 \quad
 \|H\|=e^{2Nc_{\rm b}}(\sqrt\rho+O(N^{-1/2})),
 \tag{17}
\]
where \(C_2,C_3,\rho>0\) are its fixed constants. Hence
\[
 \begin{split}
 \liminf_{N\to\infty}N^{-1}\log\|V_{0,N}\|_1
       &\ge 2A_*-c_{\rm b}/2,\\
 \limsup_{N\to\infty}N^{-1}\log\|V_{0,N}\|_1
       &\le A_*+c_{\rm b}.
 \end{split}
 \tag{18}
\]
These are inherited bounds, not an asserted limit for \(\mu_4\).
Their difference is \((3c_{\rm b}-2A_*)/2\).
The same written cap-seed theorem records the already proved
\(A_*>9/20\), while \(c_{\rm b}<1/3\) follows from the sine
chord estimate. Thus the lower rate in (18) is strictly greater
than \(11/15\). In particular a whole-disk forcing estimate with
rate at most \(11/15\) is false for this actual source.
This is not a lower bound at a prescribed point of the output arc.

For \(R\ge1\), the polynomial maximum principle gives
\[
 \|V_{0,N}\|_R\le R^D\sqrt{\mu_{4,N}},
 \tag{19}
\]
so the upper rate becomes \(A_*+c_{\rm b}+\log R\). Fixed
outgoing derivatives cost polynomial factors, by Cauchy's formula
at radius \(R(1+1/N)\). This retains the radii above one required
by next-three outputs. It does not extend the positive argument
to the type-four forcing, whose additional \(P_j^{-1}\) weight
is complex.

## 3. The exact suffix vector gives an angular bound

The original half-band cardinal identity is
\[
 (-q)^b\mathfrak l_b(e^{-2\pi iz})
                          =e^{-\pi iDz}h_b(z).
 \tag{20}
\]
Combine it with the exact transformed cardinal vector in
[the traced-vertex source, equation (8)](research_traced_three_vertex_endpoint.md).
The apparent denominators cancel against \(Z^N-1\). For every
complex \(Z\), the result is the polynomial identity
\[
 \boxed{\quad
 \bigl(MU^*\mathfrak l(Z)\bigr)_j
       =\frac{\kappa(-q)^jP_j}{N}
                          \prod_{\nu=j+1}^D(Z-r^\nu).
 \quad}
 \tag{21}
\]
One may first check it for \(Z=e^{-2\pi iz}\ne0\), away from
the finitely many roots, and then use polynomial continuation.
The case \(j=D\) is the constant \(\kappa(-q)^D\);
the case \(j=0\) is \(\kappa\mathfrak l_0(Z)\).
Thus neither endpoint nor any physical zero has been divided out.

Apply Cauchy--Schwarz to
\(e_0^TH^2g=(H^{3/2}e_0)^*H^{1/2}g\),
where \(g=U^*\mathfrak l(Z)\). Since
\(\|H^{1/2}g\|=\|Mg\|\), (9) gives the complete finite bound
\[
 \boxed{\quad
 |V_{0,N}(Z)|
 \le \frac{\sqrt{\mu_{3,N}}}{N}
       \left\{\sum_{j=0}^D S_j^2
          \prod_{\nu=j+1}^D|Z-r^\nu|^2\right\}^{1/2}.
 \quad}
 \tag{22}
\]
The phase cancellations already present in the cap moment \(\mu_3\)
have been retained. Only the displayed transformed boundary vector
is estimated positively.

For a compact set of complex \(Z\), define the continuous envelope
\[
 \mathcal B(Z)=\max_{0\le t\le1}
       \left\{J(t)+\int_t^1
                         \log|Z-e^{-2\pi iu}|\,du\right\}.
 \tag{23}
\]
The integral is finite through its logarithmic zeros and continuous
in \(Z,t\). The uniform sine-factorial bound and the zero-safe upper
product estimate applied to (21) prove, for every \(\tau>0\),
\[
 |V_{0,N}(Z)|\le C_\tau N^{B_\tau}
                e^{N\{A_*+\mathcal B(Z)+\tau\}}.
 \tag{24}
\]
To obtain the product upper bound through a zero, truncate its
logarithm from below before taking a Riemann sum; the resulting
continuous majorant can have arbitrarily small integral excess,
uniformly on the compact set. The finite row count costs only a
polynomial. The exact finite estimate (22) remains preferable
at a physical zero.

On the unit circle (23) has a closed one-variable form. Extend
\(J\) to its continuous odd, one-periodic primitive. For \(0\le x\le1\),
\[
 \boxed{\quad
 \mathcal B(e^{-2\pi ix})
      =-2J((1-x)/2)-J(x)=:\mathcal A_{\rm arc}(x).
 \quad}
 \tag{25}
\]
Indeed its expression before maximization is
\[
                 J(t)-J(x)-J(t-x).
 \tag{26}
\]
For \(0\le t\le x\), this is
\(J(t)+J(x-t)-J(x)\le0\): its derivative has the sign of
\(\sin(\pi t)-\sin(\pi(x-t))\), so it decreases to \(x/2\)
and then increases to its zero endpoint values.
For \(x\le t\le1\), the derivative of (26) has the sign of
\(\sin(\pi t)-\sin(\pi(t-x))\). It changes from positive
to negative at \(t=(1+x)/2\). Its maximum is (25), and is
nonnegative. Continuity handles \(x=0,1\).

The derivative of \(\mathcal A_{\rm arc}\) is
\(-\log(2\sin(\pi x/2))\), so it has its unique maximum at
\(x=1/3\). Sine duplication gives
\[
 \mathcal A_{\rm arc}(1/3)=-3J(1/3)=-2J(1/6)=c_{\rm b}.
 \tag{27}
\]
Thus (24)--(25) recover the whole-circle upper rate in (18)
and retain a strict angular improvement on compact arcs excluding
\(1/3\). The sufficient next-three output enclosures contain that
angle; no uniform loss there follows from (27).

Fixed outgoing derivatives in (24) follow on compact neighborhoods
by Cauchy, with a prescribed small rate tolerance. The identities
hold at both parities and use the original full matrices, including
their normal directions. The forcing here has its ordinary input
fixed at \(c_0\); no assertion about derivatives in a newly free
ordinary input is made.

## 4. Consequence for the remaining transport problem

The coherent seam value in (12) has rate \(c_{\rm b}\), whereas the
whole-disk forcing has the strictly larger lower rate in (18).
Seam positivity therefore cannot be transported by a polynomial
loss to the entire disk. Equations (21)--(24) give a source-dependent
angular estimate that can be combined with a genuine output contour.

They do not bound the complete outgoing response by its forcing
without the homogeneous term. Nor do they remove the exponential
norm of the remaining \(I-\mathcal L\) inverse identified in
[the outgoing function-norm theorem](research_mixed_next_outgoing_response_norms.md).
A source-specific cancellation or an eligible full output-cycle
argument is still needed for that step. Neither a separate-sector
suppression theorem nor a new knot-family conclusion is claimed here.
