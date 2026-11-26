# The exact middle amplitude on the outgoing upper half-disk

Private written source proof, 8 November 2026. No mathematical numerical
evaluation, saved-value arithmetic, or frozen-source edit is used.

After the already paid small internal indices are removed, the exact
normalized physical-index amplitude is uniformly bounded throughout
the outgoing upper unit half-disk. In the outgoing scaled index this
allows every nonnegative imaginary height, while the internal index
may vary in a fixed small complex neighborhood of its real interval.
All finite tail products remain inside the exact amplitude. No bound
for the remaining two-index observation is asserted.

## 1. An exact polynomial in the outgoing exponential

Keep
\[
L=\lfloor N/6\rfloor,\qquad U=\lfloor N/2\rfloor-1,
\qquad \eta=j/N,\qquad T=e^{2\pi it}.
\tag{1}
\]
Use the exact fixed-end function in
[the analytic-amplitude theorem](research_mixed_next_middle_exact_analytic_amplitude.md).
For \(x=n/N\), put
\[
\begin{split}
\mathcal R_{n,N}(\eta,T)
={}&e^{i\pi/N}
 \frac{\sin\pi(x-\eta)\sin\pi(x+\eta+1/N)}{\sin^2\pi x}
 \frac{e^{i\pi x}-T e^{-i\pi x}}{2i\sin\pi x},\\
\mathcal A_N(\eta,T)
={}&\sum_{\ell=0}^{U-L}
               \prod_{h=0}^{\ell-1}\mathcal R_{U-h,N}(\eta,T).
\end{split}
\tag{2}
\]
Every denominator is a fixed nonzero real number. These functions
are entire in \(\eta\), and \(\mathcal A_N\) is a polynomial in
\(T\) of degree at most \(U-L\). The exact identity
\[
e^{i\pi(t+1/N)}\sin\pi(x-t)
 =e^{i\pi/N}\frac{e^{i\pi x}-e^{2\pi it}e^{-i\pi x}}{2i}
\tag{3}
\]
shows that
\(\mathcal A_N(\eta,e^{2\pi it})=\mathfrak G_N(\eta,t)\).
There is no limiting approximation in this equality.

In particular, at the original integer indices,
\[
W_{jk,N}=q^{-(k+1)U}a_U^{j,k}\,
                       \mathcal A_N(j/N,e^{2\pi ik/N}),
\quad
a_U^{j,k}=\frac{S_U^3}{S_{U-j}S_{U+j+1}S_{U-k}}.
\tag{4}
\]
The literal sine zeros in (2) still terminate the products at
\(\max(L,j,k)\), exactly as in the cited theorem. Both parity
amplitudes, the genuine lower cutoff, and all original phases
are retained.

Let
\[
\mathbb D_+=\{T\in\mathbb C:|T|\le1,\ \Im T\ge0\},
\qquad I=[1/64,1/2].
\tag{5}
\]

**Theorem.** There is a fixed open complex neighborhood
\(\mathscr V\) of \(I\) such that, uniformly over both parities
and all sufficiently large levels,
\[
\sup_{\eta\in\mathscr V,\ T\in\mathbb D_+}
                       |\mathcal A_N(\eta,T)|\le C.
\tag{6}
\]
More precisely, on the same set after a possible shrink of
\(\mathscr V\),
\[
\mathcal A_N(\eta,T)
 =\frac1{1-\tfrac12\cos^2(\pi\eta)(1+T)}+O(N^{-1}).
\tag{7}
\]
The limiting denominator is uniformly separated from zero, and
\(\mathcal A_N\) is uniformly separated from zero for large \(N\).
Every fixed \(\eta\)-derivative is bounded on a smaller fixed
neighborhood. In particular (6) applies to
\[
0\le\Re t\le1/2,\qquad \Im t\ge0,
\tag{8}
\]
with no upper restriction on \(\Im t\).

The exact bound (6), rather than replacement by (7), is intended
for the remaining source. It introduces no coefficientwise error
into a subsequent canceling observation.

## 2. The global boundary tail

Retain the odd one-periodic real primitive
\[
J(x)=\int_0^x\log|2\sin\pi s|\,ds,
\qquad
V_\eta(x)=J(x+\eta)+J(x-\eta)-2J(x).
\tag{9}
\]
The established
[real-period Newton comparison, Lemma 2](research_three_crossing_real_period_newton_bound.md)
gives
\(V_\eta(x)>0\) for \(0<\eta\le1/2\) and \(0<x<1/2\).
This is \(V_{\pi-2\pi\eta}(x)\) in that source. Strictness
follows from its strict real-angle monotonicity and its value
zero at the angle \(\pi\).

For real \(\eta\in I\), the logarithmic modulus of a weighted
product from \(x\) to \(1/2\) is
\[
\Psi_T(x;\eta)=-V_\eta(x)+K_T(x),\qquad
K_T(x)=\int_x^{1/2}
 \log\frac{|1-T e^{-2\pi is}|}{2\sin\pi s}\,ds.
\tag{10}
\]
We prove \(K_T(x)\le0\) on the entire boundary of
\(\mathbb D_+\), for \(1/6\le x\le1/2\).

On the upper semicircle put \(T=e^{2\pi it}\),
\(0\le t\le1/2\). Then exactly
\[
K_T(x)=J(x)-J(x-t)+J(1/2-t).
\tag{11}
\]
For \(t>0\), this is strictly negative when \(0<x<1/2\):
if \(x\ge t\), its length-\(t\) logarithmic-sine interval is
strictly below the terminal interval ending at \(1/2\); if
\(x<t\), it is the sum
\(J(x)+J(t-x)+J(1/2-t)\) of nonpositive terms with the first
strictly negative. At \(t=0\), it is zero. These are the two
exact comparisons proved in Section 2 of the analytic-amplitude
theorem.

On the nonnegative diameter, \(0\le T\le1\), one has
\[
|1-e^{-2\pi is}|^2-|1-T e^{-2\pi is}|^2
 =(1-T)\{1+T-2\cos(2\pi s)\}\ge0,
\quad 1/6\le s\le1/2.
\tag{12}
\]
Here \(\cos(2\pi s)\le1/2\). Thus the integrand in (10)
is nonpositive pointwise, proving the assertion on this part
of the diameter.

For the negative diameter write \(T=-r\), \(0\le r\le1\).
Convexity of the squared modulus in \(r\) gives
\[
|1+r e^{-2\pi is}|
 \le\max\{1,\,2\cos(\pi s)\},\qquad 0\le s\le1/2.
\tag{13}
\]
Accordingly the logarithmic integrand in (10) is at most
\[
h(s)=
\begin{cases}
\log\cot(\pi s),&1/6\le s\le1/3,\\
-\log(2\sin\pi s),&1/3\le s\le1/2.
\end{cases}
\tag{14}
\]
Let \(H(x)=\int_x^{1/2}h(s)\,ds\). For
\(1/3\le x<1/2\), \(H(x)=J(x)<0\). For
\(1/6\le x\le1/3\),
\[
H(x)=\int_x^{1/3}\log\cot(\pi s)\,ds+J(1/3).
\tag{15}
\]
Its derivative is negative up to \(1/4\) and positive
thereafter, so its maximum on this interval is at an endpoint.
Those endpoint values both equal \(J(1/3)<0\): the integral
from \(1/6\) to \(1/3\) is zero under the reflection
\(s\mapsto1/2-s\), which changes \(\log\cot\) to its
negative. Hence \(K_T(x)\le H(x)<0\) on the negative
diameter, including all its endpoints by continuity.

For any fixed \(0<d<1/12\), (9)--(15) now give a uniform
strict margin
\[
\Psi_T(x;\eta)\le-\nu_d<0,
\quad 1/6\le x\le1/2-d,\quad
\eta\in I,\quad T\in\partial\mathbb D_+.
\tag{16}
\]
Indeed the minimum of \(V_\eta(x)\) on this compact real
set is strictly positive. The boundary parameter \(T\) does
not weaken that margin.

## 3. Exact finite tails and maximum modulus

The zero-safe one-sided mesh estimate proved in Section 3 of
the analytic-amplitude theorem applies to both sine factors
in (2). It also applies uniformly to the circle factor
\(\log|1-T e^{-2\pi is}|\) for \(|T|\le1\).
For \(|T|\ge1/2\), factor this into a complex-shifted sine;
the shift is bounded and its constant factor is included on
both sides of the mesh estimate. For \(|T|\le1/2\), the
logarithm has uniformly bounded derivative and no zero, so
the ordinary mesh error is bounded. Thus this assertion
includes every unit-circle numerator zero, the diameter endpoints
\(T=1,-1\), and the center \(T=0\), without division by a
vanishing factor.

For \(x=(U-\ell)/N\), this gives on the boundary
\[
\log\left|\prod_{h=0}^{\ell-1}
                      \mathcal R_{U-h,N}(\eta,T)\right|
\le N\Psi_T(x;\eta)+C\log N.
\tag{17}
\]
The integer lower endpoint may lie below \(1/6\) by less
than \(1/N\). Extend its integral to \(1/6\); the original
uniform integrated-log modulus of continuity costs only
\(O(\log N)\) in (17). The displacement of \(U/N\) from
\(1/2\), and the explicit \(1/N\) in (2), have the same
already retained cost.

Allowing \(\eta\) in a small fixed complex neighborhood
preserves a strict version of (16). A small real displacement
uses uniform continuity of the integrated logarithms.
For its imaginary part, the exact nonnegative sine-period
increment
\[
\int_0^1\bigl\{\log|2\sin\pi(s+ih)|
                 -\log|2\sin\pi s|\bigr\}\,ds=\pi|h|
\tag{18}
\]
shows that the two sine numerators cost at most
\(2\pi N|\Im\eta|\). Choose the neighborhood small enough
to preserve, for instance, a strict rate \(-\nu_d/2\).
All finite mesh constants are uniform on it.

Each fixed product in (17) is a polynomial in \(T\).
The maximum-modulus principle on the upper half-disk therefore
extends its entire boundary estimate to every \(T\in\mathbb D_+\),
with the same constants. This step is applied to the exact
finite product, before any sum or source observation. It
does not extend an estimate of individual ratios from the
boundary.

## 4. Near-endpoint contraction and the exact amplitude

At the upper endpoint, the limiting weighted ratio is
\[
\mathcal R_{1/2,\infty}(\eta,T)
 =\tfrac12\cos^2(\pi\eta)(1+T).
\tag{19}
\]
On the full real set \(\eta\in I,T\in\mathbb D_+\),
its modulus is at most \(\cos^2(\pi/64)<1\).
Compact continuity gives a fixed \(d>0\), a fixed complex
neighborhood of \(I\), and \(r_0<1\), such that
\[
|\mathcal R_{n,N}(\eta,T)|\le r_0
\quad\hbox{for }1/2-2d\le n/N\le1/2,
\quad T\in\mathbb D_+,
\tag{20}
\]
for all large \(N\). Choose this \(d\) first and shrink
only the complex neighborhood to make Section 3 applicable.

Products with \(\ell\le dN\) are bounded by \(r_0^\ell\).
Every longer exact product is bounded, by (16)--(18) and
maximum modulus, by \(CN^C e^{-N\nu_d/2}\). Their complete
finite sum is still exponentially small. This proves (6).
In particular no growth as \(\Im t\to+\infty\) is hidden
in a separated exponential-sine factor: the exact polynomial
expression (2) remains bounded all the way to \(T=0\).

For (7), use the exact finite geometric-defect identity with
the constant ratio (19), retaining its final \(L\)-endpoint.
The near-endpoint ratio error is \(O((\ell+1)/N)\), uniformly
in \(T\in\mathbb D_+\). Summing it against (20) gives
\(O(N^{-1})\). All farther products and the endpoint are
bounded by Section 3; a term at the integer split is already
exponentially small by (20). The limiting denominator stays
uniformly nonzero, so division proves (7). Cauchy's formula
on a smaller \(\eta\)-neighborhood gives its stated derivative
bounds. The same uniform approximation proves nonvanishing.

## 5. Original-source scope

The [restored middle source](research_mixed_next_three_restored_middle_large_indices.md)
keeps
\(j>\lfloor N/64\rfloor\), so \(j/N>1/64\); the present
domain includes all its remaining internal indices. The
old \(L,U\) and both exact parity amplitudes are unchanged.
The removal and legitimate restoration of the physical
near-half band use its complete attached observation together
with the separately paid small-index subsets; no bound for
an arbitrary partial sum is inferred from a bound for its
whole physical node.

In the exact two-index source, this theorem allows the factor
\(\mathcal A_N(\eta,e^{2\pi it})\) to remain intact on an
upward outgoing-index contour, while the internal index is
real or in its small fixed complex neighborhood. The endpoint
factorials, outgoing polynomial, two chirps, complete inner
Hermite kernel, original scalar \(\kappa(-q)^D/N\), and all
outer contour corrections still require their own combined
estimate. This theorem does not supply such a deformation,
pay its endpoints or aliases, or assert a bound for the
complete coupled sum.

## 6. Exact reflection and the downward-height cost

The proof above actually gives the stronger absolute-product bound
\[
\sum_{\ell=0}^{U-L}|P_{\ell,N}(\eta,T)|\le C,
\qquad
P_{\ell,N}(\eta,T)=
       \prod_{h=0}^{\ell-1}\mathcal R_{U-h,N}(\eta,T),
\quad \eta\in\mathscr V,\ T\in\mathbb D_+.
\tag{21}
\]
Indeed the near-endpoint products sum geometrically by (20),
and each long product has its own exponentially small bound
from Section 3 before their absolute values are summed.
This conclusion includes the fixed complex \(\eta\)-neighborhood.

Each polynomial in (21) has the exact form
\[
P_{\ell,N}(\eta,T)
 =c_{\ell,N}(\eta)\prod_{h=0}^{\ell-1}
                  (T-e^{2\pi i(U-h)/N}),
\tag{22}
\]
with the empty-product convention at \(\ell=0\).
The coefficient is allowed to vanish; nothing below divides by it.
For \(\Im T\ge0\) and \(|T|>1\), put
\(T^\#=1/\overline T\in\mathbb D_+\). The unit modulus of
every displayed root gives exactly
\[
|P_{\ell,N}(\eta,T)|
 =|T|^\ell |P_{\ell,N}(\eta,T^\#)|.
\tag{23}
\]
The same \(\eta\) is used on both sides, even when it is
complex. Summing (23) and using (21) proves the corollary
\[
\boxed{\quad
|\mathcal A_N(\eta,T)|
 \le\sum_{\ell=0}^{U-L}|P_{\ell,N}(\eta,T)|
 \le C\max\{1,|T|^{U-L}\},
\qquad \eta\in\mathscr V,\quad \Im T\ge0.
\quad}
\tag{24}
\]
This is a bound for the entire exact amplitude, not a split-tail
replacement. Since
\(U-L=\lfloor N/2\rfloor-1-\lfloor N/6\rfloor<N/3\),
the exact identification \(T=e^{2\pi it}\) yields, at every
imaginary height,
\[
|\mathcal A_N(\eta,e^{2\pi it})|
 \le C\exp\{2\pi(U-L)(-\Im t)_+\}
 \le C\exp\{(2\pi N/3)(-\Im t)_+\},
\quad 0\le\Re t\le1/2.
\tag{25}
\]
Thus a downward alias may retain this explicit additional rate
\((2\pi/3)(-\Im t)_+\), while upward contours retain (6).
Its payment against the other source factors remains a separate
comparison. Neither nonvanishing nor the limiting formula (7)
is asserted outside the unit half-disk. All original phases,
endpoint factorials, and observation scalars remain unchanged.
