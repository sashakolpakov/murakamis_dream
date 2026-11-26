# The mixed two-crossing source: exact coefficients and a dominant horizontal contour

Consider the original boundary element
\(T(R^{-2}T(R^2))\). Its two crossing powers have opposite signs.
The finite source has a simple double-factorial formula whose first
index has only a linear oscillatory term. We prove that the horizontal
contour through its cubic critical point has a unique global maximum,
and that the associated ordinary integral has a nonzero asymptotic.
We also bound all original high and outer index sectors, uniformly in
the boundary angle.

These statements alone do not transfer that integral to the original
finite sum. The connecting contour faces and nonconstant lattice
modes are treated in the separate
[complete boundary theorem](research_mixed_two_crossing_boundary_theorem.md),
which now proves that transfer using this note and the exact contour
identity.

## 1. The original source and its exact coefficients

Put \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\[
 S_k=\prod_{r=1}^k2\sin(\pi r/N),\qquad
 F_k=(Q;Q)_k,\qquad S_0=F_0=1.
\]
The original Newton basis, full quotient and trace are
\[
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}
       \left(2\cos\frac{(2r+1)\pi}{N}-z\right),\quad
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),
\]
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad T e_j=e_{D-j}.
\]
Here \(T_N\) is the ordinary Chebyshev polynomial; \(T\) is the
original turn. Equalities in \(\mathcal A_N\) include the first
derivatives at repeated roots.

Let \(M\) be multiplication by the original crossing \(R\), let
\(J\) reverse Newton coefficients, and put
\[
 Z_N(u)=\operatorname{can}\bigl(T(R^{-2}T(R^2))\bigr)(-2\cos u).
                                                               \tag{1}
\]
Its exact coefficient vector is
\[
 JM^{-2}JM^2e_0=(M^2)^*M^2e_0,                         \tag{2}
\]
where \(*\) is conjugate transpose in the Newton coefficient basis.
Indeed multiplication is self-adjoint for the Frobenius matrix \(J\),
so \(JM^{-2}J=(M^{-2})^T\), while \(M^{-1}=\overline M\).
Formula (2) is an identity on the full algebra; it is not a statement
that every boundary evaluation of (1) is a positive norm.

**Proposition 1.** The entire original boundary polynomial is
\[
 \boxed{\displaystyle
 Z_N(u)=N^2\sum_{\substack{a,j\ge0\\a+j<N}}
    i^{-j}q^{aj-j(j-1)/2}
       \frac{S_{a+j}}{S_a^3S_j^2}e_j(-2\cos u).}        \tag{3}
\]
In particular, every denominator has index less than \(N\).

**Proof.** The original two-crossing identities give
\[
 H_{2,N}=T(R^2)=N\sum_{a=0}^D\frac{q^{a^2}}{F_a}e_a,
 \qquad
 \phi_N(R^2e_a e_j)=Nq^{(a-j)^2}\frac{F_{a+j}}{F_a^2F_j^2},
\]
with zero second coefficient if \(a+j\ge N\). Conjugating the latter
identity in the real Newton basis and using
\(\overline{F_k}=(-1)^kq^{-k(k+1)}F_k\) gives
\[
 \phi_N(R^{-2}e_a e_j)
        =N(-q)^{a+j}\frac{F_{a+j}}{F_a^2F_j^2}.
\]
Insert this into the original trace of \(R^{-2}H_{2,N}e_j\).
Finally \(F_k=(-i)^kq^{k(k+1)/2}S_k\) gives exactly (3).
These finite identities were proved with full normal data in the
[terminal calculation](research_two_crossing_terminal_filling.md) and
[two-boundary formula](research_degree_two_power_two_formula.md).
\(\square\)

At the spectral endpoint \(c_0=2\cos(\pi/N)\), only \(e_0\) is nonzero.
Thus (3) and \(S_aS_{D-a}=N\) give the useful exact check
\[
                    Z_N(c_0)=N^2\sum_{a=0}^D S_a^{-2}
                                  =\sum_{a=0}^D S_a^2. \tag{4}
\]
The notation in (4) means spectral evaluation of the polynomial in
(1). Its positivity does not identify the complete-boundary rate
at \(u=0\).

## 2. The exact interpolation and its cubic critical point

Define
\[
 J(z)=\int_0^z\log(2\sin\pi w)\,dw,
\]
initially on \((0,1)\), and continue from that interval in the bulk
strip. On the low Newton-index chart put
\[
 b(y,u)=\int_0^y\log(2\cos2\pi w+2\cos u)\,dw-2J(y).
\]
Its branch starts on \(0<y<1/2,u=0\), where
\(b(y,0)=J(2y)-4J(y)\). For \(x=a/N,y=j/N\), the phase of (3) is
\[
 W(x,y;u)=J(x+y)-3J(x)-2J(y)+b(y,u)
                  +i\pi(xy-y^2/2-y/2).                \tag{5}
\]
Let \(G_N\) be the canonical factorial and \(B_N(y,u)\) the exact
Newton interpolation used in the terminal calculation. The exact
summand interpolation is
\[
 f_N(x,y;u)=N^2 e^{-i\pi Ny/2}
   e^{i\pi N(xy-y^2/2)}e^{i\pi y/2}
       \frac{G_N(N(x+y))}{G_N(Nx)^3G_N(Ny)^2}B_N(y,u).
                                                               \tag{6}
\]
The shifts in \(B_N\) remain \(D/2\), not \(N/2\). On compact
regular bulk sets this has the uniform holomorphic expansion
\[
 f_N(x,y;u)=N^{-1}a(x,y)e^{NW(x,y;u)}(1+O(N^{-1})),
\quad
 a(x,y)=\frac{e^{i\pi y/2}}8
       \frac{\sqrt{\sin\pi(x+y)}}
            {(\sin\pi x)^{3/2}(\sin\pi y)^2}.           \tag{7}
\]
The square roots continue from the strict positive real triangle.
The midpoint factorial terms in \(B_N\) give the factor
\((2N\sin\pi y)^{-1}\); this fixes both the power and the phase in
(7).

Let \(X\) be the root in the upper half-plane of
\[
                         X^3+2X^2+1=0,
\qquad Y=1+2X+2X^2,
\qquad x_*=\frac{\log X}{2\pi i},\quad
       y_* =\frac{\log Y}{2\pi i}.                     \tag{8}
\]
The logarithms have arguments in \((0,\pi)\). They give
\[
 \begin{split}
 x_*&=0.225610088277137\ldots+0.062944643677395\ldots i,\\
 y_*&=0.216668187285767\ldots-0.078767457408271\ldots i.
 \end{split}                                                   \tag{9}
\]
In particular the real parts of \(x_*,y_*,x_*+y_*,2y_*\) are all
strictly between zero and one.

**Proposition 2.** The point (8) is critical for the actual
unexponentiated phase (5) at \(u=0\). Its real action
\(M=\Re W(x_*,y_*;0)\) satisfies
\[
                        M>613/500.                     \tag{10}
\]

To check the algebra, exponentiation of the two derivatives gives
\[
 X^2Y-X=(1-X)^3,
 \qquad (1-XY)(1+Y)^2=(1-Y)^4.                          \tag{11}
\]
Substitution of (8) reduces both to the cubic. None of the divided
factors vanishes. The literal derivatives are
\[
 \begin{split}
 W_x&=\log(2\sin\pi(x+y))-3\log(2\sin\pi x)+i\pi y,\\
 W_y&=\log(2\sin\pi(x+y))-6\log(2\sin\pi y)
             +2\log(2\sin2\pi y)+i\pi(x-y-1/2).
 \end{split}                                                   \tag{12}
\]
Their sine arguments have positive real part at the selected point,
so these are their continued principal logarithms. The certified
enclosures described in Section 4 put each imaginary part between
\(-1\) and \(1\). Equation (11) therefore forces both derivatives
to be zero, rather than a nonzero multiple of \(2\pi i\). The same
enclosures prove (10); they give
\(M=1.2265931093905021954\ldots\).

## 3. The horizontal maximum and its ordinary integral

Set \(h_x=\Im x_*\), \(h_y=\Im y_*\), and
\[
 \mathcal R=[9/50,27/100]\times[17/100,27/100],\qquad
 H(a,b)=\Re W(a+ih_x,b+ih_y;0).
\]
For \(a+b>1\), define the displayed phase by continuation in the
lower half-plane for its \(J(x+y)\) term. This extension is used
only to cover a rectangle in the following inequality; it does not
assert a factorial asymptotic outside the original triangular bulk.

**Theorem 3.** On \([0,1]\times[0,1/2]\), the function \(H\) has its
unique global maximum at \((\Re x_*,\Re y_*)\). More explicitly,
\[
 H<49/40\quad\hbox{outside }\mathcal R,
 \qquad -H''\succeq(\pi/2)I\quad\hbox{on }\mathcal R. \tag{13}
\]
Consequently every fixed closed set avoiding the selected point has
a strict gap below \(M\).

The proof is the finite interval certificate in Section 4, together
with the following Hessian calculation. Put
\[
 A=\Re\cot\pi x,\quad B=\Re\cot\pi y,\quad
 C=\Re\cot\pi(x+y),\quad D=\Re\tan\pi y.
\]
The imaginary polynomial in (5) contributes no horizontal second
derivative to the real action. The double-angle cotangent identity
then gives
\[
 H''=\pi\left[
 C\begin{pmatrix}1&1\\1&1\end{pmatrix}
                   -\begin{pmatrix}3A&0\\0&4B+2D\end{pmatrix}
              \right].                                 \tag{14}
\]
The certificate bounds \(3A-C-|C|\) and \(4B+2D-C-|C|\) strictly
above \(1/2\) throughout \(\mathcal R\). Thus (14) gives (13).
The selected point lies strictly inside this convex rectangle and
has zero gradient by Proposition 2. Strict concavity proves its
unique maximum there; (10),(13) exclude every point outside.

This also proves a nonzero asymptotic for a specified continuous
integral. Fix \(\epsilon=10^{-6}\), let
\[
 \Omega_\epsilon=\{(a,b):a\ge\epsilon,\quad
  \epsilon\le b\le1/2-\epsilon,\quad a+b\le1-\epsilon\},
\]
and define
\[
 I_N(u)=N^2\int_{\Omega_\epsilon}
              f_N(a+ih_x,b+ih_y;u)\,da\,db.             \tag{15}
\]
All factorial arguments on this contour stay in fixed regular bulk
strips, for sufficiently small complex \(u\). The Hessian of \(W\)
at the critical point is invertible because its negative real part
is positive definite. Hence its critical point extends holomorphically
to \((x_*(u),y_*(u))\), with critical action \(S(u)\). On a fixed
complex disk,
\[
 I_N(u)=A_{\mathrm{hor}}(u)e^{NS(u)}(1+O(N^{-1})),
 \qquad
 A_{\mathrm{hor}}(u)=
 \frac{2\pi a(x_*(u),y_*(u))}
             {\sqrt{\det[-W''(x_*(u),y_*(u);u)]}}\ne0. \tag{16}
\]
The square root is fixed by the Gaussian integral with positive
definite real quadratic part. At zero the real horizontal Hessian
bound makes that Gaussian absolutely convergent and nonzero. Away
from a small neighborhood of the point, (13) gives an exponential
gap. Taylor expansion in that neighborhood, rescaling by \(N^{-1/2}\)
and integrating the convergent Gaussian proves (16). For nearby
complex \(u\), move only this interior neighborhood with the
holomorphic critical point; its boundary lies in the existing strict
gap. This gives the uniform holomorphic expansion. The factors are
\(N^2\) from (15), \(N^{-1}\) from (7), and \(N^{-1}\) from the
two-dimensional Gaussian, so no power of \(N\) remains.

Equation (16) concerns the explicitly defined integral (15). We have
not proved that its coefficient is the coefficient of the finite
source (3).

## 4. Reproducible certificate for the horizontal inequalities

The [verifier](../experiments/verify_mixed_two_crossing_horizontal.py)
uses rational partitions and outward-rounded Arb/Acb arithmetic.
The root in (8) is defined without a numerical root guess. Set
\[
 r=-\sqrt[3]{43/54-\sqrt{59/108}}
   -\sqrt[3]{43/54+\sqrt{59/108}}-2/3,
\quad
 X=\frac{-2-r}{2}
       +i\sqrt{-1/r-((-2-r)/2)^2}.
\]
Cardano's identity gives the cubic, and the positive square root
selects its upper root.

For real \(a\) and the fixed nonzero heights used here,
\[
 \Re J(a+ih)=
 -\frac{\Im\operatorname{Li}_2(e^{-2\pi|h|+2\pi ia})}{2\pi}
                    -\frac\pi2|h|(1-2a).              \tag{17}
\]
This follows from the upper-half-plane dilogarithm formula for \(J\)
and Schwarz reflection. In the verifier the exact real phase is
\[
 \begin{split}
 H(a,b)={}&\Re J(a+b+i(h_x+h_y))-3\Re J(a+ih_x)\\
         &-6\Re J(b+ih_y)+\Re J(2b+2ih_y)\\
         &-\pi\{b h_x+(a-b-1/2)h_y\}.
 \end{split}                                                   \tag{18}
\]
No sampled point values enter a subdivision decision.

At 128-bit precision, 256 rational subrectangles certify the
Hessian inequalities on \(\mathcal R\). An adaptive rational binary
partition accepts 36,937 rectangles covering the full area \(1/2\).
Every accepted rectangle either lies wholly inside \(\mathcal R\)
or has its entire phase enclosure below \(49/40\). The exact area
and a hash of all accepted rectangles are recorded. Thus no gap in
coverage is inferred from a floating-point plot. The
[saved certificate](../repro/results/research-mixed-two-crossing-horizontal.json)
also records the action and logarithmic-gradient enclosures.

The numerical method is standard ball arithmetic, as documented in
[Johansson's Arb paper](https://doi.org/10.1109/TC.2017.2690633) and the
official [Arb](https://flintlib.org/doc/arb.html) and
[Acb](https://flintlib.org/doc/acb.html) manuals. The exact source,
phase branches and Hessian identities above are separate inputs to
that arithmetic.

## 5. Original index tails and arbitrary exterior contractions

Changing the second crossing sign has not changed the absolute
value of a summand at a real boundary angle. In (3) it is exactly
\[
             N^2\frac{S_{a+j}}{S_a^3S_j^2}
                                      |e_j(-2\cos u)|. \tag{19}
\]
Therefore the original high-index and outer-face estimates in
[the adjacent-pair tail proof](research_adjacent_two_crossing_global_tails.md)
apply term by term, with every factorial shift and repeated-root
normal retained. In particular the high sector \(2j\ge N\) has
rate at most \(2/3\). For the union of the four strips
\[
 a/N\le\epsilon,\quad j/N\le\epsilon,\quad
 1-(a+j)/N\le\epsilon,\quad j/N\ge1/2-\epsilon,
\]
that proof gives the absolute rate
\[
 \frac{2143}{2826}+\frac{117}{250000}<\frac{19}{25}.
\]
Each term is counted once in this union. Consequently
\[
 \sup_{u\in\mathbb R}|Z_N^{\mathrm{tail}}(u)|
       \le CN^A e^{19N/25},\qquad
 \sup_{|\Im u|\le1/100}|Z_N^{\mathrm{tail}}(u)|
       \le C'N^{A+1}e^{77N/100}.                        \tag{20}
\]
For the second bound, this entire tail is a trigonometric polynomial
of degree at most \(D\); bound each Fourier coefficient by the real
supremum and sum. Both rates are strictly below (10).

There is also a source-level bound after attachment to any fixed
controlled exterior. If an exterior trigonometric polynomial
\(A_N(t)\) has angular Fourier degree at most \(sN\), with \(s\)
fixed, and real supremum at most
\(C_A N^{d_A}e^{NM_A}\), then for every fixed signed \(n\),
\[
 |\phi_N(R^n Z_N^{\mathrm{tail}} A_N)|
                      \le C_n N^{d_n}e^{N(M_A+19/25)}. \tag{21}
\]
Indeed the exact physical trace differentiates
\(\sin t\,C_{N,n}e^{inNt^2/(4\pi)}Z_N^{\mathrm{tail}}(t)A_N(t)\)
at all \(N\) nodes. The carrier and chirp have modulus one there.
The first derivatives of the two trigonometric polynomials cost at
most their degrees times their real suprema; the chirp derivative
costs \(O_n(N)\). Summing all original nodes proves (21). This is
not an estimate for a distinct-root trace.

No comparison of \(M_A+19/25\) with the final filled volume is
automatic. Equation (21) retains the actual exterior and states
exactly the available bound, rather than declaring its contribution
negligible in every closure.

## 6. What remains for the finite sum

The exact source, its regular critical point, a nonzero horizontal
integral, and all original extreme-index tails are controlled here.
Identifying (16) as an asymptotic of (3) additionally requires the
exact lattice representation, its connecting faces, all nonconstant
modes, and its factorial monodromy terms. Those additional steps
are now supplied by the complete boundary theorem linked above.
The opposite signs make the two selected heights opposite as well;
the same-sign full-period cancellation theorem is not substituted
without checking the new multipliers and endpoint orders.

The proved [boundary multiplication theorem](research_boundary_crossing_packet_preservation.md)
gives another exact description of the input to this turn. Locally,
\(R^{-2}H_{2,N}\) has the terminal phase
\(V(t)+i\pi/8-5it^2/(8\pi)\), with its exact scalar
\(C_{N,-2}\), where \(V(t)=\psi(t,0)/2\). But its candidate turn
saddle is far outside the fixed disk supplied by that theorem.
It therefore supplies no shortcut to the missing global transfer.

## 7. Reproduction

Run the exact finite normalization checks and the horizontal
certificate with

```sh
python3 experiments/check_mixed_two_crossing_source.py --precision 120 \
  --output repro/results/research-mixed-two-crossing-source.json
python3 experiments/verify_mixed_two_crossing_horizontal.py --precision 128 \
  --output repro/results/research-mixed-two-crossing-horizontal.json
```

The first [script](../experiments/check_mixed_two_crossing_source.py)
compares the complete original matrix word with every coefficient in
(3), the Gram identity (2), the endpoint value (4), and three complex
boundary values and derivatives, at all levels \(2\le N\le16\).
Its [output](../repro/results/research-mixed-two-crossing-source.json)
is a finite normalization diagnostic. The second script verifies the
finite covering argument used in Theorem 3. Neither calculation
asserts the remaining original-cycle transfer.
