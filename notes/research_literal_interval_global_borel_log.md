# The continued Borel function of the literal interval defect logarithm

Private written proof, 18 November 2026.

The factorial and color intervals of the original highest-cut source
have an exact Euler--Maclaurin coefficient identity [S]. This note
sums the Borel transform of its defect logarithm globally. The proof
derives the needed Bernoulli identity directly and keeps both endpoint
branches, every fixed integer offset, and the constant Borel term.
It does not continue the full amplitude after quantum exponentiation,
normal products, or hard contraction.

## 1. Exact interval and Borel conventions

Define the Bernoulli polynomials by
\[
 \frac{t e^{ct}}{e^t-1}
       =\sum_{a\ge0}\frac{B_a(c)}{a!}t^a.
 \tag{1}
\]
For an endpoint germ \(F\), with its initial germ at zero retained,
put
\[
 V_c(h;s)=\sum_{a\ge1}h^{a-1}\frac{B_a(c)}{a!}
             \bigl(F^{(a-1)}(s)-F^{(a-1)}(0)\bigr).
 \tag{2}
\]
Derivatives hold all other source parameters fixed. The endpoint
at \(s\) may have been continued; the endpoint at zero in (2) is
the original germ, not the returned value of a loop based there.
Our Borel convention is
\[
 \mathcal B_h\Bigl(\sum_{j\ge0}v_jh^j\Bigr)
                =\sum_{j\ge0}v_j\frac{\xi^j}{j!}.
 \tag{3}
\]

For \(s=hL\), the coefficient identity is
\[
 \sum_{r=0}^{L-1}F(h(r+c))
       =h^{-1}\int_0^sF(t)\,dt+V_c(h;s).
 \tag{4}
\]
Here (4) is formal coefficient regrouping of the finite interval,
not a claim that its right-hand power series converges in \(h\).
It follows directly by testing \(F(t)=e^{qt}\): the finite
geometric sum is
\[
 \frac{e^{qs}-1}{qh}
       \frac{qh e^{cqh}}{e^{qh}-1}.
\]
Expand using (1), then compare powers of \(q\). Linearity gives
(4) for every Taylor coefficient of \(F\). Differences of intervals
retain their respective original endpoint paths.

The actual functions in [S] are
\[
 F_0(t)=\log\frac{e^t-1}{t},\qquad
 F_\pm(Y,t)=\log\frac{1-Y^{\pm1}e^t}{1-Y^{\pm1}},
 \qquad Y\ne0,1.
 \tag{5}
\]
Their initial logarithms vanish at zero. The value of \(F_0\) at
zero is removable. Their singular sets in the \(t\)-plane are
\[
 \Sigma_0=2\pi i\mathbb Z\setminus\{0\},\qquad
 \Sigma_\pm(Y)=\{t:e^t=Y^{\mp1}\}.
 \tag{6}
\]
We first prove a formula for a logarithm \(F=\log G\), where
\(G\) is meromorphic on the plane, regular and nonzero at zero
and at the specified endpoint. The sets of its zeros and poles
are discrete. This includes every function in (5).

## 2. An elementary Bernoulli coefficient identity

Equation (1) gives
\[
 B_0(c)=1,\quad B_1(c)=c-\tfrac12,\quad
 B_a'(c)=aB_{a-1}(c),\quad
 B_a(c+1)-B_a(c)=a c^{a-1}.
 \tag{7}
\]
In particular \(B_a(1)=B_a(0)\) for \(a\ge2\), and
\(\int_0^1B_a(c)\,dc=0\) for \(a\ge1\).
Set \(\omega_n=2\pi i n\). Integration by parts gives, for
\(n\ne0\),
\[
 \int_0^1B_1(c)e^{-\omega_nc}\,dc=-\omega_n^{-1},
 \qquad
 \int_0^1B_a(c)e^{-\omega_nc}\,dc
        =-\frac{a!}{\omega_n^a}\quad(a\ge2).
 \tag{8}
\]
For \(a\ge2\) the series
\(-a!\sum_{n\ne0}e^{\omega_nc}/\omega_n^a\) converges absolutely
and uniformly on the real interval. It has precisely the Fourier
coefficients in (8), including its zero mean.

Here is the uniqueness step without an external Fourier theorem.
If a continuous periodic function has all Fourier coefficients zero,
convolve it with
\[
 K_N(t)=\frac1N\left|\sum_{r=0}^{N-1}e^{2\pi i r t}\right|^2.
\]
This trigonometric polynomial is nonnegative and has integral one;
all these convolutions are zero. For distance at least \(\delta\)
from the integers,
\(K_N(t)\le[N\sin^2(\pi\delta)]^{-1}\). Splitting the convolution
into that set and its complement, and using uniform continuity on
the complement, proves uniform convergence to the original function.
The function is therefore zero. Apply this to the continuous periodic
extension of \(B_a\) minus the displayed uniformly convergent series.
At either endpoint we obtain
\[
 \boxed{\quad
 \frac{B_a(0)}{a!}=\frac{B_a(1)}{a!}
        =-\sum_{n\ne0}\omega_n^{-a}\quad(a\ge2).
 \quad}
 \tag{9}
\]
The separate values \(B_1(0)=-1/2\) and \(B_1(1)=1/2\) have
not been replaced by a conditionally convergent Fourier value.

## 3. Exact continued Borel formula

For \(c=0\) or \(1\), define initially near \(\xi=0\)
\[
\begin{split}
 \widehat V_c(\xi;s)={}&B_1(c)\bigl(F(s)-F(0)\bigr)\\
 &-\sum_{n\ne0}\frac1{\omega_n}
 \left\{F\left(s+\frac\xi{\omega_n}\right)-F(s)
       -F\left(\frac\xi{\omega_n}\right)+F(0)\right\}.
\end{split}
 \tag{10}
\]
The first translated germ starts with the specified branch at \(s\);
the second starts with the original branch at zero. Continue both
along the translated image of the chosen \(\xi\)-path. These choices
are part of (10).

Taylor expansion of each bracket and (9) show that its coefficient
of \(\xi^j\), for \(j\ge1\), is
\[
 \frac1{j!}\frac{B_{j+1}(c)}{(j+1)!}
                         \bigl(F^{(j)}(s)-F^{(j)}(0)\bigr).
 \tag{11}
\]
The constant is the first line of (10). Thus (10) is exactly the
Borel germ (3) of (2), with no scaling or factorial suppressed.

Let \(\Sigma\) be the zeros and poles of \(G\), and put
\[
 \mathcal A_s=
 \bigcup_{n\ne0}\{\omega_n(\tau-s),\ \omega_n\tau:
                                      \tau\in\Sigma\}.
 \tag{12}
\]
If both endpoints avoid \(\Sigma\), this set is locally finite and
does not contain zero. Indeed their distances from \(\Sigma\) have
a positive lower bound \(d\). A point of (12) of modulus at most
\(R\) must have \(2\pi|n|d\le R\), so only finitely many \(n\)
occur. For each such \(n\), only finitely many \(\tau\) occur.

For any fixed compact continued path in
\(\mathbb C_\xi\setminus\mathcal A_s\), all sufficiently large
\(|n|\) have both translated paths inside fixed buffered endpoint
disks. On those disks the mean-value integral bounds the bracket
in (10) by \(C|\xi|/|\omega_n|\). Thus its summand is
\(O(|\xi|/|n|^2)\), uniformly on a small tube of the path.
The finitely many other translated logarithms continue individually.
Consequently (10) converges normally along the path and on nearby
paths. It defines the actual analytic continuation of its initial
Borel germ, on the path cover based at zero.

This proof is joint in source parameters. On a compact continued
endpoint chart with a common positive distance from the singular
sets, the large-\(n\) tail uses common endpoint disks and a common
bound for \(F'\). The finitely many remaining translated paths must
avoid their singular divisors, and then have joint holomorphic
thickenings. In particular, for (5), compact \(Y\)-sets avoid
\(0,1\) and the actual upper-endpoint zeros. The family of candidate
singular divisors is locally finite there. No uniform endpoint buffer
is asserted when an endpoint approaches a zero or pole.

## 4. Meromorphic derivative and exact monodromy

Termwise differentiation in the preceding normal convergence gives
\[
 \partial_\xi\widehat V_c
  =-\sum_{n\ne0}\omega_n^{-2}
        \left\{F'\left(s+\frac\xi{\omega_n}\right)
                     -F'\left(\frac\xi{\omega_n}\right)\right\}.
 \tag{13}
\]
Here \(F'=G'/G\) is single-valued meromorphic. The same endpoint
estimate proves locally normal convergence away from (12). Near any
candidate point only finitely many terms can have poles; all the
others are holomorphic there. Thus (13) is a global meromorphic
function of \(\xi\), with at most simple poles. Write
\(m_\tau=\operatorname{ord}_\tau G\), allowing negative orders.
Its residue at \(q\in\mathcal A_s\) is the finite sum
\[
 \operatorname{Res}_{\xi=q}\partial_\xi\widehat V_c
   =-\sum_{\substack{n\ne0,\ \tau\in\Sigma\\
                         q=\omega_n(\tau-s)}}\frac{m_\tau}{\omega_n}
     +\sum_{\substack{n\ne0,\ \tau\in\Sigma\\
                         q=\omega_n\tau}}\frac{m_\tau}{\omega_n}.
 \tag{14}
\]
Formula (14) retains collisions and cancellations. Thus (12) is a
candidate singular set, not an assertion that every listed point is
singular. The continued function has only logarithmic singularities
at its nonremovable points, and the increment around a closed loop
is \(2\pi i\) times the sum of (14) with the loop's winding numbers.
This also follows by continuing the individual logarithms in (10);
all but finitely many have zero winding. No branch is reset after a
loop. The constant in (10) remains its original endpoint constant.

For the literal functions,
\[
 F_0'(t)=\frac{e^t}{e^t-1}-\frac1t,\qquad
 F_\pm'(Y,t)=-\frac{Y^{\pm1}e^t}{1-Y^{\pm1}e^t}.
 \tag{15}
\]
The first expression is regular at zero; every point in (6) has
residue one. Equations (12)--(15) therefore give their explicit
continued Borel functions and all their finite monodromy increments.

## 5. All fixed integer offsets

For an integer \(c\), use the oriented finite sum notation
\[
 \sum_{d\in[0,c)}^{\mathrm{or}}H(d)=
 \begin{cases}
  \sum_{d=0}^{c-1}H(d),&c>0,\\
  0,&c=0,\\
  -\sum_{d=c}^{-1}H(d),&c<0.
 \end{cases}
 \tag{16}
\]
Shifting the finite interval in (4), or using (7), gives the exact
formal identity
\[
 V_c(h;s)-V_0(h;s)
       =\sum_{d\in[0,c)}^{\mathrm{or}}
                           \bigl(F(s+dh)-F(dh)\bigr).
 \tag{17}
\]
This includes the old lower endpoint and is valid for negative
offsets without an infinite or negative-length factorial.

The Borel transform of a single endpoint translate is
\[
 \mathcal E_d(\xi;t)=
     \sum_{j\ge0}\frac{d^jF^{(j)}(t)}{(j!)^2}\xi^j.
 \tag{18}
\]
On an endpoint disk of radius \(\delta\), Cauchy's estimate gives
\[
              |\mathcal E_d(\xi;t)|
                      \le M\exp(|d\xi|/\delta).
 \tag{19}
\]
Thus (18) is entire in \(\xi\), jointly on each smaller endpoint
chart, with the given endpoint logarithm. It is the Borel transform
of the convergent Taylor germ \(F(t+dh)\), not the substitution
\(F(t+d\xi)\). Equations (10), (17), and (18) give for every
fixed integer offset
\[
 \boxed{\quad
 \widehat V_c=\widehat V_0+
       \sum_{d\in[0,c)}^{\mathrm{or}}
          \bigl(\mathcal E_d(\xi;s)-\mathcal E_d(\xi;0)\bigr).
 \quad}
 \tag{20}
\]
For \(c=1\) the one correction is \(F(s)-F(0)\), precisely the
change from \(B_1(0)\) to \(B_1(1)\) in (10). For all integer
offsets the finite additional terms are entire, so the finite
singularities and their \(\xi\)-monodromy are exactly those of
\(\widehat V_0\), after cancellations already retained in (14).

## 6. Application to the original source and its boundary

The literal signed factorial and color logarithms in [S, Section 2]
are finite differences of (4) with the functions (5), evaluated at
the original linear occupation endpoints and fixed integer offsets.
Their Cartan and natural-meridian drift terms are separately retained
analytic or polynomial corrections. Applying (10) or (20) to each
literal interval, with its sign, therefore continues the actual
scalar defect logarithm beyond its initial small Borel disk. This
uses no critical-point, Alexander-root, or geometric-component
hypothesis. Zero occupation endpoints are allowed: they are regular
for (5), and when both endpoint branches coincide their differences
cancel exactly.

The construction retains the principal integral in (4) separately,
with its original path. It does not alter the highest-cut matching,
pivot, framing, or logarithmic normalization of the finite word.
Those data are unchanged when a scalar entry coefficient is
rewritten by this exact Borel identity.

There is a precise further step before this result controls a full
original-prefix or cap period. Products and exponentials of these
formal logarithms introduce Borel convolutions; the finite stationary
and hard contractions assemble additional quantum coefficients.
Their action sums can have a non-locally-finite projection, so local
finiteness of (12) cannot be transferred to the assembled amplitude
without a separate continuation and path-length estimate. This note
does not assert that transfer, infinite-Laplace growth, or a physical
cycle coefficient. It supplies an explicit global continued Borel
function for each actual literal scalar interval defect.

## 7. Complete proof direct

| Label | Complete proof source | SHA256 |
|---|---|---|
| S | notes/research_actual_marked_minor_regular_source_cover.md | 1f10491c502dcf1781763bc410f4f139b08e899906b748b26db92262428c2ce4 |

The complete source S was read and every used implication checked.
Only its literal functions, exact interval/source identification, and
retention of endpoint branches are used. All Fourier coefficients,
normal convergence, singularity, monodromy, and offset statements are
proved above. No external proof, mathematical program, test, or build
is used. Frozen notes and public manuscripts are unchanged.
