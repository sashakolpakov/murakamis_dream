# The endpoint packet for every signed Gaussian crossing power

Research note, 2 November 2026.

The exact Gaussian functional calculus already represents every signed
power of the original crossing. The scalar endpoint reduction in
[the Gaussian source note](actual_coherent_filling_gaussian_chirp.md),
equations (15)--(16), concerns even powers. For odd powers the Gaussian
has an additional sign change in its endpoint values. This produces
a spectral idempotent as well as the derivative term.

Here we compute that extra term, keep the original turn and half
crossing, and give its exact Newton expansion. Its coefficient mass is
logarithmic in the level. We also evaluate its spectral values and first
derivatives exactly, obtaining a quadratic bound in the full Hermite
norm. This is a source-preserving identity and an upper estimate for a
specific boundary packet. It gives no lower bound
for a filled-knot period and does not identify a general contour
remainder with this packet.

## 1. Original data and the endpoint algebra

Fix \(N\ge2\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad
 \rho=q-q^{-1},\quad \kappa=q^{D^2/2},\quad
 P_N(z)=2T_N(z/2)+2 .
 \tag{1}
\]
The Chebyshev notation has its ordinary meaning. The original crossing
is \(R=\kappa r_N(\Omega)\), in the full algebra
\(\mathcal A_N=\mathbb C[z]/(P_N)\). For every signed integer \(n\),
let \(f_n\) be the canonical polynomial representing \(r_N^n\).
Negative powers exist since the crossing is a unit.

Set \(c_j=q^{2j+1}+q^{-2j-1}\). The node \(c_0=c_D\) is double,
also at \(N=2\). Let \(\Pi_0\) be its full spectral idempotent:
it has value one and derivative zero at \(c_0\), and all its other
prescribed values and first derivatives vanish. Let \(\Xi_0\) have
value zero at every node, derivative one at \(c_0\), and all other
prescribed derivatives zero. These specifications determine elements
of the full algebra, including its repeated roots.

They satisfy
\[
 \Pi_0^2=\Pi_0,\qquad
 \Pi_0\Xi_0=\Xi_0,\qquad \Xi_0^2=0.                       \tag{2}
\]
They can be constructed directly. Put
\[
 H(z)=P_N(z)/(z-c_0)^2,\quad
 H(c_0)=\frac{N^2}{4-c_0^2},\quad
 a=\frac{H'(c_0)}{H(c_0)}=\frac{c_0}{4-c_0^2}.
 \]
Then their representatives are
\[
 \Pi_0(z)=\frac{[1-a(z-c_0)]H(z)}{H(c_0)},\qquad
 \Xi_0(z)=\frac{(z-c_0)H(z)}{H(c_0)}.                    \tag{3}
\]
Checking the prescribed values and derivatives proves these formulas
and (2).

There are two distinct linear operations below. The genuine geometric
quarter-turn is denoted \(T\); it reverses the original Newton basis.
The spectral shift is denoted \(\mathcal T\), and is defined on a
canonical polynomial by
\[
 (\mathcal T f)(w+w^{-1})
 =f(Qw+Q^{-1}w^{-1})+f(Q^{-1}w+Qw^{-1}).                \tag{4}
\]
The expression is a symmetric Laurent polynomial, hence a polynomial.
It uses the specified canonical representative before shifting.
It is not a multiplicative operation on arbitrary quotient
representatives.

## 2. The exact Ward identity, with both parity terms

**Theorem 1.** Put \(\epsilon=(-1)^n\). In the original full algebra,
\[
 \boxed{
 \mathcal T f_n(\Omega)-(-q)^n\,2T_n(\Omega/2)f_n(\Omega)
 =(1-\epsilon)\Pi_0+
       \frac{n\{N-1+\epsilon(N+1)\}}{2\rho}\,\Xi_0 .
 }                                                       \tag{5}
\]
Here \(T_{-n}=T_n\). Thus
\[
 \begin{array}{ll}
 n\text{ even}:&
     \mathcal T f_n-q^n2T_n f_n=(nN/\rho)\Xi_0,\\[2mm]
 n\text{ odd}:&
     \mathcal T f_n+q^n2T_n f_n=2\Pi_0-(n/\rho)\Xi_0 .
 \end{array}                                             \tag{6}
\]

**Proof.** Let \(\hbar=2\pi i/N\), and keep the original unwrapped
node logarithms
\[
 x_j=(2j+1)\pi i/N,\qquad 0\le j<N .
 \]
The entire Gaussian
\[
 G_n(x)=q^{-nD^2/4}
          \exp\!\left(\frac{n(x-\pi i)^2}{2\hbar}\right) \tag{7}
\]
uses the fixed convention \(q^a=\exp(\pi ia/N)\), including
fractional exponents; no principal square root of the numerical
value of \(\kappa\) is taken. It has exactly the values and first logarithmic derivatives of
\(g_n(x)=f_n(e^x+e^{-x})\) at these nodes:
\[
 G_n(x_j)=\nu_j^n,\quad
 G_n'(x_j)=-\frac n2(D-2j)\nu_j^n,\quad
 \nu_j=(-1)^j q^{j(j+1)}.                               \tag{8}
\]
At the odd simple node only the value is needed; both logarithmic
derivatives there are zero.

Direct Gaussian translation gives
\[
 G_n(x+\hbar)+G_n(x-\hbar)
            =(-q)^n(e^{nx}+e^{-nx})G_n(x).              \tag{9}
\]
For \(1\le j\le D-1\), both neighboring nodes remain in the original
logarithmic window. The left side of (5) therefore has zero value
and, at every double node among them, zero derivative.

At \(x_0=\pi i/N\), the backward shift leaves that window.
The polynomial \(g_n\) is \(2\pi i\)-periodic, so the actual shifted
value is \(g_n(x_D)=1\). The Gaussian value instead is
\(G_n(-\pi i/N)=\epsilon\). Their difference is \(1-\epsilon\).
For their derivatives the actual value is
\(g_n'(x_D)=nD/2\), whereas the Gaussian derivative at the shifted
point is \(-n(N+1)\epsilon/2\). Thus their difference is
\[
                    \frac n2\{N-1+\epsilon(N+1)\}.
 \tag{10}
\]
Divide by \(dc/dx=\rho\) at \(x_0\) to obtain the second coefficient
in (5). At \(x_D\) the logarithmic derivative and \(dc/dx\) both
reverse sign, giving the same Casimir derivative.

These are all the full Hermite data of the difference. Equations
(2)--(3) therefore prove (5), for either sign of \(n\) and for both
level parities. \(\square\)

The extra term at odd powers is a value defect. It cannot be removed
by keeping only the derivative correction from the even-power
formula.

## 3. The actual odd-box turn

Let \(p,\ell\) be the original cup and cap. With their fixed
normalizations, the earlier physical source calculation gives
\[
 \Xi_0=(-1)^N\rho^2p\ell,\qquad
 T(p\ell)=I,\qquad R^{-1}p=\kappa^{-1}p .
 \tag{11}
\]
The crossing data at \(c_0\) give
\[
 R^{-1}\Pi_0=\kappa^{-1}
        \left(\Pi_0+\frac{D}{2\rho}\Xi_0\right),\qquad
 R^{-1}\Xi_0=\kappa^{-1}\Xi_0.                            \tag{12}
\]
For example the derivative of \(r_N^{-1}\) at \(c_0\) is
\(D/(2\rho)\); multiplying its two-term local expansion by the
idempotent proves the first formula.

Denote the left side of (5) by \(W_n\).
Multiplication by the original \(R^{-1}\) and then the genuine turn
therefore give
\[
 \boxed{
 T(R^{-1}W_n)=
 \begin{cases}
 nN(-1)^N\rho\,\kappa^{-1}I,&n\text{ even},\\[1mm]
 2\kappa^{-1}T\Pi_0+
       (N-1-n)(-1)^N\rho\,\kappa^{-1}I,&n\text{ odd}.
 \end{cases}}
 \tag{13}
\]
This is an identity before any exterior contraction, so arbitrary
spectator tangles and the original marked closure can be retained.
No turn has been commuted through a product.

The additional \(T\Pi_0\) is not a scalar. Otherwise applying the
involutive turn would make \(\Pi_0\) a scalar multiple of \(T1=e_D\),
which is nilpotent. This contradicts its nonzero idempotence.

For fixed \(n\), both scalar coefficients in (13) are bounded
independently of \(N\), since \(|\rho|\le2\pi/N\).

## 4. A logarithmic-size exact packet for the remaining coupon

Use the original normalized Newton basis
\[
 e_j(z)=S_j^{-2}\prod_{r<j}(c_r-z),\qquad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad Te_j=e_{D-j}.
 \tag{14}
\]

**Theorem 2.** With \(\theta=\pi/N\),
\[
 \boxed{
 T\Pi_0=(-1)^N2\cos\theta\,e_0+
       \sum_{k=1}^{N-1}(-1)^{N+k+1}
                    \frac{\sin\theta}{\sin(k\theta)}e_k .
 }                                                       \tag{15}
\]
Its Newton coefficient mass is at most
\[
                         2+\pi H_{N-1}
              \le 2+\pi(1+\log(N-1)),                   \tag{16}
\]
where \(H_j=\sum_{r=1}^j1/r\).

**Proof.** Write \(\Pi_0=\sum_{j=0}^Da_je_j\).
For \(j<D\), the interpolation list \(c_0,\ldots,c_j\) contains
\(c_0\) only once. All its other value and repeated-node derivative
data of \(\Pi_0\) vanish. Its divided difference is therefore
\[
       \Pi_0[c_0,\ldots,c_j]
                   =\frac1{\prod_{r=1}^j(c_0-c_r)} .
 \tag{17}
\]
This can be verified by taking the residue at \(c_0\) of the
interpolating polynomial divided by
\(\prod_{r=0}^j(z-c_r)\); all other residues vanish with their
required multiplicities. Hence
\[
 a_j=\frac{(-1)^jS_j^2}{\prod_{r=1}^j(c_0-c_r)}
             =(-1)^j\frac{\sin\theta}{\sin((j+1)\theta)}
                         \quad(0\le j<D).               \tag{18}
\]
The last equality uses
\(c_0-c_r=4\sin(r\theta)\sin((r+1)\theta)\).
For the last coefficient use the original closure:
\[
 a_D=\phi_N(\Pi_0)=(-1)^D(-c_0)=(-1)^Nc_0.
 \tag{19}
\]
Its derivative at \(c_0\) is zero, so this is exactly the Hermite
closing formula. Reversal of (18)--(19) proves (15).

Finally
\[
 \frac{\sin\theta}{\sin(k\theta)}
       \le\frac{\pi}{2\min(k,N-k)}
 \]
by the chord lower bound for sine. Summing gives (16).
\(\square\)

Consequently, for any scalar exterior functional \(\Lambda\) in this
typed slot,
\[
 |\Lambda(T\Pi_0)|
 \le [2+\pi H_{N-1}]\max_{0\le k<N}|\Lambda(e_k)|.        \tag{20}
\]
The same statement holds with a norm for a vector-valued exterior.
All Newton indices are retained. This is an upper estimate for the
exact current coupon; it neither replaces it by a positive scalar
nor gives a lower estimate for its coherent contraction.

### The full spectral values and first normals

There is a stronger estimate that uses the cancellation in (15).
It controls the actual full Hermite norm, not just its Newton
coefficient mass.

**Theorem 3.** For the distinct double nodes indexed by
\(0\le j<\lfloor N/2\rfloor\), put \(\alpha_j=(2j+1)\theta\).
Then
\[
 \begin{split}
 (T\Pi_0)(c_j)
   &=(-1)^N\left[2\cos\theta+
                         2\sin\theta\sum_{r=1}^j\cot(r\theta)\right],
                                                        \tag{21}\\
 (T\Pi_0)'(c_j)
   &=(-1)^{N+1}\frac{\sin\theta}{4\sin\alpha_j}
                       \sum_{r=j+1}^{N-1-j}\csc^2(r\theta). \tag{22}
 \end{split}
\]
The value formula also holds at the odd simple node, with
\(j=(N-1)/2\). Consequently, for the full norm retaining
values and first derivatives at double nodes and only the value
at an odd simple node,
\[
 \|T\Pi_0\|_{\mathcal J}
 \le 2+2H_{\lfloor(N-1)/2\rfloor}+\frac{N^2-1}{12}.
 \tag{23}
\]
Here \(H_0=0\).

**Proof.** We prove the finite summation identity needed for the
normals, so its use does not depend on an unverified summation
formula. Temporarily let \(q\) vary near the original root,
\(Q=q^2\), and use the same analytic Newton polynomials, with
\[
 c_j=q^{2j+1}+q^{-2j-1},\qquad
 S_k^2=(-1)^kq^{-k(k+1)}(Q;Q)_k^2.
 \]
All their denominators with \(k<N\) remain nonzero near that root.
Define
\[
 G_a(z)=1+\sum_{k=1}^{N-1}
               \frac{1-a}{1-aQ^k}(-q)^k e_k(z).
 \tag{24}
\]
For \(0\le j<N\), direct cancellation of the Newton factors gives
\[
 (-q)^ke_k(c_j)
  =Q^k\frac{(Q^{-j};Q)_k(Q^{j+1};Q)_k}{(Q;Q)_k^2}
 \quad(0\le k\le j),
 \]
and the terms with \(k>j\) vanish. Therefore
\[
                       G_a(c_j)=
                      \prod_{r=1}^j\frac{a-Q^r}{1-aQ^r}.
 \tag{25}
\]
To prove this last finite identity, regard both sides as rational
functions of \(a\). Their possible poles are \(a=Q^{-k}\),
\(1\le k\le j\), all simple for generic \(q\). The residue of
the left side at that pole is
\[
 (Q^{-k}-1)
      \frac{(Q^{-j};Q)_k(Q^{j+1};Q)_k}{(Q;Q)_k^2}.
 \]
Expanding the products on the right gives exactly the same
residue. After subtraction their difference is constant, since
both are bounded at infinity; evaluating at \(a=1\) gives zero.
This proves (25) and its analytic continuation near the original
root. It is the specialized terminating balanced summation
identity, here proved by partial fractions.

Let \(H_q(z)=\partial_aG_a(z)|_{a=1}\). From (25),
\[
                  H_q(c_j(q))=
                      \sum_{r=1}^j\frac{1+Q^r}{1-Q^r}.
 \tag{26}
\]
At the original root this is \(i\sum_{r=1}^j\cot(r\theta)\).
Equation (15), including its signs, is equivalently
\[
                   T\Pi_0=(-1)^N(c_0-\rho H_q).
 \tag{27}
\]
This proves (21).

For a double node, let \(j'=N-1-j\). At the root the values
in (26) for \(j,j'\) coincide. Because the entire polynomial
\(H_q(z)\) varies analytically with \(q\), its ordinary derivative
at their common value is the confluent difference
\[
 H_q'(c_j)=
 \frac{\partial_{\log q}
       [H_q(c_j(q))-H_q(c_{j'}(q))]}
      {\partial_{\log q}[c_j(q)-c_{j'}(q)]}
 \quad\hbox{evaluated at the root}.                       \tag{28}
\]
Terms from differentiating the coefficients of \(H_q\) cancel
because the two arguments coincide there. Differentiating (26)
gives the numerator
\[
 \sum_{r=j+1}^{N-1-j}r\,\csc^2(r\theta)
            =\frac N2\sum_{r=j+1}^{N-1-j}\csc^2(r\theta).
 \]
The denominator is \(4iN\sin\alpha_j\). Substitution into
(27) proves (22). These are the actual first derivatives of the
fixed root polynomial; no physical off-root deformation is being
asserted.

For the bound, \(\cot t\le1/t\) on \(0<t<\pi/2\), and
\(\sin\theta\le\theta\), so (21) has modulus at most
\(2+2H_{\lfloor(N-1)/2\rfloor}\). At the listed double nodes
\(\sin\alpha_j\ge\sin\theta\). Also
\[
                  \sum_{r=1}^{N-1}\csc^2(r\theta)
                          =\frac{N^2-1}{3}.
 \]
One elementary derivation differentiates the logarithm of the
finite sine product for \(\sin Nx\), then takes the constant
term at \(x=0\) after subtracting \(x^{-2}\).
Equation (22) is therefore bounded by \((N^2-1)/12\), proving
(23). \(\square\)

In particular the non-scalar odd current in (13) has polynomial
full Hermite norm for every fixed \(n\). For a commutant exterior
\(A\), the original closing estimate and the product rule give
\[
 |\phi_N(A\,T\Pi_0)|
       \le3N\,\|A\|_{\mathcal J}\|T\Pi_0\|_{\mathcal J}.
 \tag{29}
\]
This is polynomial cost in the actual source norm. It does not
deduce polynomial cost merely from the small coefficient sum (16).
An exponential bound for the exterior remains necessary.

### The whole real boundary

The same formulas give a polynomial bound on every real boundary
angle. Put \(V_N=2+2H_{\lfloor(N-1)/2\rfloor}\). Then
\[
 \boxed{\quad
 \sup_{\theta\in\mathbb R}
       |(T\Pi_0)(2\cos\theta)|
       \le NV_N+\frac{\pi(N-1)}3 .
 \quad}                                                   \tag{30}
\]
This estimate concerns the polynomial itself, including the
cancellation between its Newton terms.

To prove it, write
\(g(\theta)=(T\Pi_0)(2\cos\theta)
  =\sum_{m=-N+1}^{N-1}\gamma_m e^{im\theta}\).
Its coefficients satisfy \(\gamma_{-m}=\gamma_m\).
At the full grid \(\theta_j=(2j+1)\pi/N\), (21)--(22) give
\[
 |g(\theta_j)|\le V_N,\qquad
 |g'(\theta_j)|
 \le D_N:=\frac{\sin(\pi/N)(N^2-1)}6\le\frac{\pi N}6.       \tag{31}
\]
The derivative at the odd simple node is zero by the chain rule.
Set
\[
 V_m=\frac1N\sum_jg(\theta_j)e^{-im\theta_j},\qquad
 U_m=\frac1{iN}\sum_jg'(\theta_j)e^{-im\theta_j}.
\]
For \(1\le m<N\), exact finite Fourier orthogonality gives
\[
 V_m=\gamma_m-\gamma_{m-N},\qquad
 U_m=m\gamma_m-(m-N)\gamma_{m-N};
 \qquad
 \gamma_m=\frac{(N-m)V_m+U_m}{N}.                         \tag{32}
\]
The minus signs arise from \(e^{iN\theta_j}=-1\).
Also \(\gamma_0=V_0\). Hence
\[
 |\gamma_0|+2\sum_{m=1}^{N-1}|\gamma_m|
 \le NV_N+\frac{2(N-1)}N D_N
 \le NV_N+\frac{\pi(N-1)}3.
\]
This proves (30). On a complex angle its right side may be
multiplied by \(e^{(N-1)|\Im\theta|}\), directly from the same
finite Fourier series. No interpolation norm estimate is being
assumed.

## 5. Consequence for the contour strategy

The existing Gaussian resolvent formula has already retained every
signed power, the full repeated-root algebra and a controlled closing
cap. The calculation here specifies the endpoint packet produced by
its elementary logarithmic shift for every power. Even powers give
the known scalar deletion; odd powers give the additional coupon
(15), with the bounded scalar in (13).

One can instead retain a half crossing separately and apply the
older even-power identity to the remaining full twists. Nothing here
invalidates that route. What fails is extending the scalar deletion
formula to the whole odd Gaussian without its value defect.

To use (13) in a global contour proof, one must establish that the
actual contour deformation produces this precise Ward difference,
in its original typed slot. A general Fresnel or resolvent contour
remainder has not been identified with \(W_n\). When that identity
does apply, (15)--(32) provide the exact replacement, its coefficient
cost, its full Hermite norm, and its whole-real-boundary bound.
They do not bound inverse Ward transport or the remaining exterior sum.

In particular, positivity of a doubled numerator cannot by itself
turn (20) into a lower bound for the original period: (15) contains
alternating coefficients, and the original closure is retained
linearly. Any proposed lower bound must control that actual
contraction, rather than the coefficient mass on its right.

The new conclusions are (5), the odd line of (13), and the explicit
packet and full Hermite and real-boundary estimates (15)--(32). The all-integer
Gaussian functional calculus and the even scalar current are prior
repository results.

## 6. Reproducing the finite checks

Run

```sh
python3 experiments/check_signed_gaussian_ward_endpoint_packet.py --precision 100 --output repro/results/research-signed-gaussian-ward-endpoint-packet.json
```

The script compares (5) and the original turned identities (13) against
the original crossing matrix for levels 2 through 10 and ten signed
powers. It independently constructs the spectral idempotent from the
characteristic polynomial, reverses its Newton coefficients, and checks
the coefficients, values and first derivatives in (15), (21), and (22)
through level 32. At each level it also reconstructs the Fourier
coefficients from the full Hermite grid and checks the resulting
polynomial at seventeen off-grid real angles, retaining the bound
(30). Thirteen off-root evaluations check the finite summation identity
used in the confluence argument. These calculations check normalization
and signs; the proofs above supply the statements for every level.

The saved output is
[the full Ward and Hermite check](../repro/results/research-signed-gaussian-ward-endpoint-packet.json).
