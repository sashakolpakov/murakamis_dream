# A global bound for the preparation error in the full adjacent source

The exact factorial preparation of the three-crossing column can
be carried through the entire remaining boundary contraction.
Its error has exponential rate strictly less than \(3/2\) on a
fixed complex neighborhood of the complete boundary value.
The bound includes every original color and ordinary boundary
derivative. It uses the original finite matrices, so there are
no contour corrections or Fourier aliases to estimate for this
error.

This removes one error term from the boundary problem. The separate
[full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
proves the nonzero asymptotic of its prepared main term.

## 1. The exact source decomposition

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
the original Newton crossing matrix \(M\) and reversal \(J\).
Write
\[
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w),\qquad S_0=1.
 \tag{1}
\]
Let \(\mathbf e(w)=(e_0(w),\ldots,e_D(w))^T\). Transposition
in a polynomial evaluation does not mean Hermitian adjunction;
the elementary bound
\(|\mathbf e(w)^Tv|\le\|\mathbf e(w)\|_2\|v\|_2\)
nevertheless applies.

The exact preparation in
[the next-step theorem](research_three_crossing_next_step_profile.md)
is
\[
 \alpha=M^3e_0=\kappa^3 A_Nh+\delta_N,\qquad
 h_j=q^{j(j+2)}S_j^2,\qquad
 \|\delta_N\|_2=O(N^{3/2}).
 \tag{2}
\]
Here \(A_N\) is the specified exact partial reciprocal-factorial
sum at a maximum of \(S_j^2\), not just its leading asymptotic.
All scalar powers have their original values and
\(|\kappa|=1\).

The whole original boundary polynomial and its preparation error
are therefore
\[
\begin{split}
 F_N(w)&=\mathbf e(w)^TJM^3J\alpha,\\
 F_N^{\mathrm{prep}}(w)&=
       \kappa^3A_N\,\mathbf e(w)^TJM^3Jh,\\
 \mathcal E_N(w)&=F_N(w)-F_N^{\mathrm{prep}}(w)
                     =\mathbf e(w)^TJM^3J\delta_N.
\end{split}                                                    \tag{3}
\]
These are exact polynomial identities in the original quotient
algebra; no repeated-root normal coordinate has been removed.

Put
\[
 \mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt,\quad
 G=\sum_{m\ge0}\frac{(-1)^m}{(2m+1)^2},\quad
 b_2=\frac{2G}{\pi},\quad c=2\mathcal J(5/6).
 \tag{4}
\]
The sharp original one-crossing norm exponent is \(c\), as
proved in Section 4 of the cited next-step theorem.

## 2. The sharper two-crossing matrix bound

**Lemma 1.** The original matrix satisfies
\[
          \lim_{N\to\infty}\frac1N\log\|M^2\|_2=b_2.
 \tag{5}
\]
In particular \(\|M^2\|_2\le C N^A e^{Nb_2}\), with fixed
constants, and
\(\|M^3\|_2\le C'N^{A'}e^{N(b_2+c)}\).

**Proof.** The exact full two-crossing formula is
\[
 (JM^2)_{ij}
   =Nq^{(i-j)^2}\frac{(Q;Q)_{i+j}}
                       {(Q;Q)_i^2(Q;Q)_j^2}
              \quad(i+j<N),
 \tag{6}
\]
and is zero otherwise. Its proof from the original finite
crossing matrix is in
[the two-boundary formula](research_degree_two_power_two_formula.md).
Since \(|(Q;Q)_j|=S_j\), the uniform factorial bound gives
\[
 \log|(JM^2)_{ij}|
   =N\{\mathcal J(x+y)-2\mathcal J(x)-2\mathcal J(y)\}
                                      +O(\log N),
 \quad x=i/N,\ y=j/N.                                          \tag{7}
\]
The error is uniform up to every end of the supported triangle.

At fixed \(s=x+y<1\), the expression in braces has derivative
\[
       2\log\frac{\sin\pi(s-x)}{\sin\pi x}
\]
with respect to \(x\). The sine subtraction formula makes
this positive before \(s/2\) and negative after \(s/2\).
Thus its maximum at fixed \(s\) is
\(\mathcal J(s)-4\mathcal J(s/2)\).
The derivative of this last function is
\(\log\cot(\pi s/2)\). Its maximum occurs at \(s=1/2\),
where the value is
\[
           -4\mathcal J(1/4)=\frac{2G}{\pi}.
 \tag{8}
\]
Continuity covers the closed triangle.
The largest matrix entry bounds the operator norm from
below, and \(N\) times the largest entry bounds it from
above. Integer indices near \(i=j=N/4\) give the matching
lower limit at both parities. This proves (5) and the
polynomial upper bound. Finally
\(\|M^3\|_2\le\|M^2\|_2\|M\|_2\).
\(\square\)

The use of (5) matters: replacing it by the weaker estimate
\(\|M^2\|\le\|M\|^2\) would lose the gap needed below.

## 3. All Newton colors near the complete boundary

**Lemma 2.** For every fixed \(\rho>0\), uniformly on
\(|w+2|\le\rho\),
\[
 \|\mathbf e(w)\|_2
   \le C_\rho N^{A_\rho}
       \exp\left\{N\left[
          b_2+\operatorname{arcosh}(1+\rho/2)\right]\right\}.
 \tag{9}
\]
Also
\[
             \lim_{N\to\infty}
                    \frac1N\log\|\mathbf e(-2)\|_2=b_2.
 \tag{10}
\]

**Proof.** Every \(c_\nu+2\) is nonnegative. The actual
numerator product in (1) therefore gives
\[
 |e_j(w)|
 \le S_j^{-2}\prod_{\nu<j}(c_\nu+2+\rho).
 \tag{11}
\]
At positive \(\rho\) its logarithm is a smooth midpoint
Riemann sum, including every \(0\le j<N\). Together with
the uniform sine-factorial estimate,
\[
 \log|e_j(w)|\le N V_\rho(j/N)+O_\rho(\log N),
 \quad
 V_\rho(x)=\int_0^x
       \log(2+\rho+2\cos 2\pi t)\,dt-2\mathcal J(x).
 \tag{12}
\]
There is no division by a boundary value or a nodal derivative.

At \(\rho=0\), the integral in (12) exists across its
logarithmic zero. It has derivative
\[
                    V_0'(x)=2\log|\cot\pi x|.
 \tag{13}
\]
Both endpoint values \(V_0(0),V_0(1)\) are zero. Thus
\(V_0\) attains its global maximum at \(x=1/4\), with
value \(b_2\). This includes the upper half of the original
Newton indices, where some odd-level value factors vanish.

The pointwise logarithmic difference in the integrands is
nonnegative. Its entire-period integral is
\[
\begin{split}
 0\le V_\rho(x)-V_0(x)
 &\le\int_0^1
       \log\frac{2+\rho+2\cos2\pi t}{2+2\cos2\pi t}\,dt\\
 &=\operatorname{arcosh}(1+\rho/2).
\end{split}                                                    \tag{14}
\]
For an elementary evaluation, differentiate the full-period
logarithmic mean at positive \(\rho\). The substitution
\(\tan(\theta/2)\) in its reciprocal integral gives
\[
 \frac1{2\pi}\int_0^{2\pi}
               \frac{d\theta}{2+\rho+2\cos\theta}
       =\frac1{\sqrt{\rho(\rho+4)}}.
 \]
Integration from \(0\) to \(\rho\), using the integrable
logarithmic endpoint, proves (14).
Equations (12)--(14), followed by the Euclidean sum over
all \(N\) coordinates, prove (9).

For (10), use (9) for arbitrarily small fixed \(\rho\)
to obtain the upper limit. Indices \(j/N\to1/4\) lie
away from the numerator zero and give the lower limit
directly from (1). \(\square\)

## 4. The whole preparation error

**Theorem 3.** Define
\[
 \sigma(\rho)=\frac{4G}{\pi}
                  +c+\operatorname{arcosh}(1+\rho/2).
 \tag{15}
\]
For every fixed positive \(\rho\),
\[
 \sup_{|w+2|\le\rho}|\mathcal E_N(w)|
                    \le C_\rho N^{A_\rho}e^{N\sigma(\rho)} .
 \tag{16}
\]
In particular, with the explicit radius \(\rho_0=10^{-6}\),
\[
 \limsup_{N\to\infty}\frac1N
      \log\sup_{|w+2|\le\rho_0}|\mathcal E_N(w)|
       \le\sigma(\rho_0)<\frac32.                              \tag{17}
\]
For every fixed derivative order \(m\), the same strict
rate bound holds for
\(\sup_{|w+2|\le\rho_0/2}|\partial_w^m\mathcal E_N(w)|\).
The limit superior is over every integer level, with no
parity subsequence.

**Proof.** Reversal is unitary in the coefficient norm, so
the exact identity (3) gives
\[
 |\mathcal E_N(w)|
     \le\|\mathbf e(w)\|_2\,
          \|M^2\|_2\,\|M\|_2\,\|\delta_N\|_2 .
 \tag{18}
\]
Apply (2), Lemmas 1--2, and the original one-crossing
norm bound. This proves (16).

Here is an explicit rational verification of (17). The
existing one-crossing estimate and elementary constant
bounds give
\[
 c<\frac{286009121}{861616000},\qquad
 G<\frac{229}{250},\qquad \pi>\frac{157}{50}.
 \tag{19}
\]
For \(G\), the first sixty-five terms of its alternating
series form an upper bound smaller than \(229/250\).
The bound for \(c\), including its positive-series tail,
is proved in the next-step theorem. Thus
\[
 \frac{4G}{\pi}+c
      <\frac{1291410721}{861616000}.
 \tag{20}
\]
Since \(\cosh s>1+s^2/2\) for \(s>0\),
\[
 \operatorname{arcosh}(1+\rho_0/2)<\sqrt{\rho_0}=\frac1{1000}.
 \]
The explicit gap is
\[
 \frac32-\left[
     \frac{1291410721}{861616000}+\frac1{1000}\right]
                 =\frac{151663}{861616000}>0.                  \tag{21}
\]
Finally \(\mathcal E_N\) is an ordinary polynomial.
Cauchy's formula on a radius-\(\rho_0/2\) circle gives
the derivative bound, with factor
\(m!(2/\rho_0)^m\), independent of the level.
\(\square\)

For negative crossing powers, conjugate the original
matrices and the boundary variable. Their norms and the
disk in (17) are unchanged. Thus the same theorem holds
for the reflected source.

## 5. What this removes from the remaining contour problem

The [exact closing-action certificate](../experiments/verify_three_crossing_closing_action.py)
and its
[saved result](../repro/results/research-three-crossing-closing-action.json)
prove that the canonical local stationary action \(W\) at
the marked geometric point satisfies
\[
                    \Re W(-2)>\frac{153}{100}.                 \tag{22}
\]
The local saddle is nondegenerate, so \(W(w)\) is holomorphic
near \(-2\). On a sufficiently small fixed boundary disk,
contained in \(|w+2|\le\rho_0/2\), continuity therefore gives
\[
                  \Re W(w)-\sigma(\rho_0)>\frac3{100}.
 \tag{23}
\]
The whole preparation error is exponentially smaller than
this stationary exponential, uniformly on that disk, with
the same conclusion for fixed derivatives on a smaller disk.
The certificate uses rational outward dilogarithmic
enclosures; a numerical match of action and volume is not
an input to (22).

Consequently the nonzero prepared asymptotic proved in the
[full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
also holds for the entire original boundary polynomial. The
error itself cannot cancel that contribution.

The error estimate here is independent of that later theorem.
The separate
[action-volume calibration](research_three_crossing_action_volume_calibration.md)
identifies the stationary real value with the original partial-exterior
volume divided by \(2\pi\); the exact contour identity and its
boundary estimates prove the contribution coefficient. No conclusion
about the finite source is inferred solely from the stationary point
or the representation-volume gap.

The rational comparisons (19)--(21) are reproduced by
[check_three_crossing_preparation_error_constants.py](../experiments/check_three_crossing_preparation_error_constants.py).
Their [saved exact result](../repro/results/research-three-crossing-preparation-error-constants.json)
retains the constants and script/dependency hashes.
The original matrix identities are the previously proved
finite identities cited in Sections 1--2, not numerical
premises of this norm argument.

## 6. Removing the outer real color ranges

The same estimates allow a useful restriction of the exact prepared
double sum before any contour deformation. Write
\[
 B_N=JM^2,\qquad \gamma=MJ\alpha,\qquad
 \gamma^{\rm prep}=\kappa^3A_NMJh .
 \tag{24}
\]
The two color coordinates are \(x=j/N\) for \(\gamma_j\) and
\(y=i/N\) for the Newton factor \(e_i(w)\). Retain
\[
 \frac1{10}\le x\le\frac12,\qquad
 \frac1{10}\le y\le\frac25 .
 \tag{25}
\]
Integer endpoints may be rounded in either direction; the change
is at most \(1/N\). The support condition \(i+j<N\) remains in force.

**Proposition 4.** The sum of the omitted terms of
\(\mathbf e(w)^TB_N\gamma^{\rm prep}\) is at most
\[
 \exp\left\{N\left(\frac{4507}{3000}+o(1)\right)\right\},
 \qquad |w+2|\le10^{-6}.
 \tag{26}
\]
The error is uniform on this disk. The same exponential bound holds
for every fixed ordinary boundary derivative on the half-sized disk.
In particular this is strictly below the selected rate \(153/100\).

**Proof.** Set
\[
 A(x)=\Re I(x)-2\mathcal J(x),\quad
 B(x)=\Re I(x)-\mathcal J(x),\quad
 g(y)=\mathcal J(2y)-4\mathcal J(y)\quad(0\le y\le1/2).
 \tag{27}
\]
The original endpoint solution and
[its global coefficient bounds](research_three_crossing_next_crossing_fourier.md)
give
\[
\begin{split}
 \limsup N^{-1}\log\max_{j/N\le1/10}|\gamma_j|&\le A(1/10),\\
 \lim N^{-1}\log\|\gamma\|_2&=\max A,\\
 \limsup N^{-1}\log\max_{j/N\ge1/2}|\gamma_j|&\le B(1/2).
\end{split} \tag{28}
\]
For clarity, the last bound includes the equality-of-moduli point.
For any fixed \(\varepsilon>0\), the right endpoint solution controls
\(j/N\ge1/2+\varepsilon\). On the intervening interval the bounded
transfer matrices give rate at most
\(A(1/2-\varepsilon)+2\varepsilon\log K+o(1)\), with \(K\)
independent of \(\varepsilon\) near zero. Take the upper limit in
\(N\), then let \(\varepsilon\) decrease to zero. This gives
\(A(1/2)=B(1/2)\), without continuing a dominant real branch through
that point.

On \(y\le1/2\), the Newton rate \(V_0(y)\) in (12) equals \(g(y)\).
It is increasing up to \(1/4\), satisfies
\(g(1/2-y)=g(y)\), and is zero at \(0,1/2\).
On \(y\ge1/2\), \(V_0(y)\le0\).
Consequently both omitted Newton ranges, \(y<1/10\) and \(y>2/5\),
have rate at most \(g(1/10)\). The boundary perturbation adds at most
\(\Delta=\operatorname{arcosh}(1+10^{-6}/2)<1/1000\).

For \(x<1/10\), apply the two matrix norm bounds to the first line
of (28). Its contribution has upper rate
\[
 A(1/10)+2b_2+\Delta<\frac{4507}{3000}.
 \tag{29}
\]
For either omitted \(y\) range, use its restricted Newton norm,
\(\|B_N\|_2\), and the full \(\|\gamma\|_2\). The upper rate is
\[
 g(1/10)+b_2+\max A+\Delta<\frac{299}{200}.
 \tag{30}
\]
All restrictions here are coordinate projections, so their operator
norms are one.

For \(x\ge1/2\), the triangular support forces \(y<1/2\).
The exact entries (6), the third line of (28), and (12) give the
termwise upper rate
\[
 B(1/2)+\mathcal J(x+y)-2\mathcal J(x)
                  +\mathcal J(2y)-6\mathcal J(y)+\Delta .
 \tag{31}
\]
Now \(\mathcal J(x)\ge0\) for \(x\ge1/2\), and
\(\mathcal J(x+y)\le\mathcal J(5/6)=c/2<1/6\).
The scalar certificates in
[Section 5 of the prepared-sum note](research_three_crossing_prepared_boundary_sum.md)
therefore bound (31) by
\[
 \frac{43}{100}+\frac16+\frac9{10}+\frac1{1000}
                         =\frac{4493}{3000}.
 \tag{32}
\]
At most \(N^2\) terms occur; this does not change an exponential rate.

These estimates initially concern the exact vector \(\gamma\).
On any product of two color ranges, replacing it by
\(\gamma^{\rm prep}\) costs at most
\[
 \|\mathbf e(w)\|_2\,\|M^2\|_2\,\|M\|_2\,\|\delta_N\|_2,
 \tag{33}
\]
because coordinate projections have norm one and
\(\gamma-\gamma^{\rm prep}=MJ\delta_N\).
Its rate is less than \(3/2\) by Theorem 3. Partition the omitted
set into the two \(x\) tails and the two \(y\) tails with \(x\)
retained. Equations (29)--(33) prove (26) for the prepared source.
Cauchy's formula proves the derivative assertion. \(\square\)

This truncation estimates sums over real lattice colors.
It does not estimate an individual face integral created by a later
complex contour deformation; those face integrals still require
their own bounds.
