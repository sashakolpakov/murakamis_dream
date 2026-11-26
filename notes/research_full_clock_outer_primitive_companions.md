# Canonical primitive and shift companions on the full-clock outer chart

Private written proof, 18 November 2026.

The fixed-\(\xi\) outer chart extends not only the full marked Borel
source, but also all its canonical primitives and bounded-shift
companions. The primitive factorial survives the joint Cauchy
continuation estimate. It pays the meridian derivatives needed for the
shift semigroup, with the original clocks held fixed.

## 1. Actual companions and the assertion

Use the full original source and the simple-node assumptions of [F].
Keep its coordinates
\[
 b(z,\xi,m)=\mathcal B_h\mathscr W_m(\alpha+z,\xi),\qquad
 W^2=z^2-4\sigma\xi,\quad q=z/W,\quad \psi=Wm.
 \tag{1}
\]
The initial branch has \(W=z\) at \(\xi=0\).
Let \(u=\Log Y=\Log(\alpha+z)\) on the fixed local meridian chart,
and write \(E=\partial_u=Y\partial_Y\), always at fixed \(\xi,m\).
Initially define
\[
 \begin{split}
 B_j&=I_\xi^j b,\qquad j\ge0,\\
 c_s&=\sum_{j\ge0}\frac{s^j}{j!}E^j I_\xi^j b,\\
 C_{a,s}&=\sum_{j\ge0}\frac{s^j}{j!}E^j I_\xi^{j+a}b,
                         \qquad a\ge0 .
 \end{split}
 \tag{2}
\]
Here every \(I_\xi\) is the primitive from the original \(\xi=0\),
and \(I_\xi^0\) is the identity. Since this base is independent
of \(Y,m\), \(I_\xi\) and \(E\) commute on the initial germ.
Thus initially \(C_{a,s}=I_\xi^a c_s\).
These definitions retain the complete primitive histories.

**Theorem.** Fix any bounded ratio disk \(|q|\le Q_0\), with
\(Q_0>1\). On a sufficiently small outer chart \(0<|W|<r\),
all the functions in (2) continue jointly through \(q=0\);
they are entire in \(s\) and every clock \(m\).
The radius \(r>0\) is independent of \(j,a,s,m\).
For fixed constants \(M,C,D>0\),
\[
 |B_j|
       \le M |W|^{2j-1}\frac{D^j}{j!}
                                    e^{C\|Wm\|_1},
 \tag{3}
\]
and, after fixed domain buffers,
\[
 \boxed{\displaystyle
 |C_{a,s}|
       \le M |W|^{2a-1}\frac{D^a}{a!}
                     \exp\!\left(C|sW|+C\|Wm\|_1\right).}
 \tag{4}
\]
For all integers \(r_1\ge0\), on a further fixed buffered chart,
\[
 |E^{r_1}C_{a,s}|
   \le M\,\frac{r_1!D^{a+r_1}}{a!}
          |W|^{2a-r_1-1}
                     \exp\!\left(C|sW|+C\|Wm\|_1\right).
 \tag{5}
\]
The constants in (3)--(5) may be enlarged between displayed
estimates, but do not depend on the displayed orders or parameters.

The actual identities
\[
 \partial_\xi C_{a+1,s}=C_{a,s},\qquad
 \partial_s C_{a,s}=E C_{a+1,s},\qquad C_{0,s}=c_s
 \tag{6}
\]
continue on these charts. In particular \(c_s\) is the continuation
of the canonical Borel germ of
\(\mathscr W_m(h,e^{sh}Y)\), with the same fixed clock vector \(m\).
No scalar factor or new initial condition is inserted.

## 2. Every primitive has the same nonnegative ratio power

Write [F]'s initial family as
\[
 F(z,\eta,\nu)=\sum_{k\ge0}z^kF_k(\eta,\nu),\qquad
 F_0=\frac r w e^{yf},\quad
 w^2=1-4\sigma\eta,\quad f=\frac{1-w}{2\sigma}.
 \tag{7}
\]
Here \(y=\mu\cdot\nu\). The exact cores in [F, Section 2] have
the form
\[
 \nu^\gamma\mathcal J_{b_c,a_c}F_0,\qquad
 k=2b_c-|\gamma|-a_c+T,\quad T\ge0,
 \tag{8}
\]
with \(T\le k\), \(b_c\le2k\), \(a_c\le3k\),
\(|\gamma|\le2k\), and \(a_c-b_c\le k\).

For every \(j\ge0\),
\[
              I_\eta^j\mathcal J_{b_c,a_c}F_0
                         =\mathcal J_{b_c+j,a_c}F_0 .
 \tag{9}
\]
To verify the initial constants when a derivative occurs, note that
\(\partial_y^{a_c}F_0=r f^{a_c}e^{yf}/w\) vanishes to order
at least \(a_c\) at \(\eta=0\). Every derivative removed by
an integration has order at most \(a_c-b_c\le a_c\).
All the intervening initial values are therefore zero.
This proves (9) also when \(b_c+j\) crosses \(a_c\).

Set
\[
 H_{k,j}(q,\psi)=
     q^{k+2j-1}
       (I_\eta^jF_k)(1/q,q\psi).
 \tag{10}
\]
The \(w\)-argument notation means evaluation at
\(\eta=(1-q^{-2})/(4\sigma)\) after the canonical primitive.
In [F]'s scaled endpoint and segment formulas replace \(b_c\)
by \(b_c+j\). Their prefactor is
\(q^{1+a_c-2(b_c+j)}\); after multiplication by
\(q^{k+2j-1+|\gamma|}\) the power is again exactly \(q^T\).
Thus every \(H_{k,j}\) is entire in \(q,\psi\).

The canonical longitudinal density has the same denominator as [F]:
\[
 \chi^{2k}(\chi-g(q))^{3k+1},\qquad
                          g(q)=\frac{q-1}{2\sigma}.
 \tag{11}
\]
Its two polynomial-log numerators have total degree at most
\(13k+2j+2\) in \((q,\chi)\), uniformly in the transverse
clock coefficient. Indeed the derivative order can only decrease
when \(b_c\) is increased. A primitive block gains \(2j\) in
its polynomial degree, since its kernel \(K(q,s)\) in [F, (12)]
has degree two. The transverse clock degree remains at most \(2k\).
There is still no \(q\)-pole.

## 3. The primitive factorial survives continuation

On the original fixed \(\eta\)-disk and a smaller disk if necessary,
[F]'s initial coefficient bound gives
\[
 |I_\eta^j F_k(\eta,\nu)|
       \le M A^k \frac{R_0^j}{j!}e^{C\|\nu\|_1}.
 \tag{12}
\]
This follows from the straight primitive simplex in that disk,
including \(j=0\). On a fixed \(q\)-circle about one,
the factor \(q^{k+2j-1}\) in (10) costs only \(A_1^kD_0^j\).
Choose the same fixed longitudinal and transverse clock coordinates
as in [F]. Optimized transverse coefficient extraction, followed
by the optimized longitudinal derivative estimate, gives for the
canonical exterior density
\[
 \sup_{\text{initial product circle}}
            |\mathcal G_{k,j,\gamma}|
     \le M A_2^k\,\frac{D_1^j}{j!}
                              \frac{c^{|\gamma|}}{\gamma!}.
 \tag{13}
\]
The density is recovered from its negative Laurent moments exactly
as in [F, Section 4]. All constants are independent of \(j,k,\gamma\).
The initial clock exponential type in (12) is independent of \(j\),
so the exterior spectral circle can be chosen once.

Apply the explicit product-contour bound [P, (6)] to the density
class (11). Its total complexity is \(O(k+j+1)\), and its
ratio-coordinate pole order is zero. On every fixed buffered
bounded \(q\)-domain, including \(q=0\), that estimate costs
at most a fixed exponential in \(k+j\). Its homogeneity in the
initial norm preserves both factorials in (13). Consequently
\[
 |[\,\omega^\gamma\,]H_{k,j}(q,\lambda v+J\omega)|
       \le M B^k\frac{D^j}{j!}
                    e^{R|\lambda|}\frac{c^{|\gamma|}}{\gamma!}.
 \tag{14}
\]
The removal at \(q=0\) uses the explicit absence of a \(q\)-pole,
as in [F]; it does not use the coarser maximum in [P, (22)] that
contains an unused inverse-coordinate distance.

Keeping \(|\gamma|\le2k\), sum (14) in \(k,\gamma\) as in
[F, (25)]. The exact source identity is
\[
 \boxed{\displaystyle
 B_j(z,\xi,m)
       =W^{2j-1}\sum_{k\ge0}W^k H_{k,j}(q,Wm).}
 \tag{15}
\]
It holds first on the original overlap by
\(I_\xi^j=z^{2j}I_\eta^j\) at fixed \(z,m\), then by
analytic continuation. On a fixed smaller \(W\)-disk,
the summed bound is (3). In particular its constants are uniform
over every primitive order. No primitive base has been moved to
the outer chart.

## 4. Fixed-\(\xi\) meridian buffers with fixed clocks

Choose \(Q_1>Q_0\) and obtain (3) on that larger ratio chart.
For a center \((z_0,\xi_0)\) with \(|q_0|\le Q_0\) and
\(W_0\ne0\), there is a fixed \(c_0>0\) such that the
log-meridian disk
\[
                  |u-u_0|<c_0|W_0|
 \tag{16}
\]
at fixed \(\xi_0\) stays in \(|q|<Q_1\) and has
\(|W_0|/2<|W(u)|<2|W_0|\).
Here the branch is fixed by \(W(u_0)=W_0\).
For clarity, \(z(u)=e^u-\alpha\) has a bounded derivative on
the fixed meridian neighborhood. Hence
\(|z-z_0|\le c_1|W_0|\) on (16), and
\[
 |W(u)^2-W_0^2|
   =|(z-z_0)(z+z_0)|
   \le c_1(2Q_0+c_1)|W_0|^2.
 \tag{17}
\]
Taking \(c_1\) small gives the analytic square root and comparability;
shrinking it further gives the specified ratio buffer. Take the
center \(W\)-radius small enough that the entire disk also stays
within the larger chart's \(W\)-radius.

The original \(m\), not \(\psi\), is held fixed in (16).
Thus \(\psi(u)=W(u)m\), and comparability gives
\(\|\psi(u)\|_1\le2\|W_0m\|_1\). It changes only the fixed
constant in the clock exponential.
Using (3) on (16) and Cauchy's estimate proves, simultaneously
for \(j,a\ge0\),
\[
 |E^j I_\xi^{j+a}b|
    \le M |W_0|^{j+2a-1}
          D^{j+a}\frac{j!}{(j+a)!}
                                    e^{C\|W_0m\|_1}.
 \tag{18}
\]
The powers of two from comparing \(W(u)\) with \(W_0\), and the
factor \(c_0^{-j}\), have been absorbed into \(D^{j+a}\).
The zero-order case is covered by enlarging \(M\).

## 5. Exact semigroup and all its primitive histories

Insert (18) into the third series in (2). It gives
\[
 \begin{split}
 |C_{a,s}|
  &\le M |W|^{2a-1}D^a e^{C\|Wm\|_1}
        \sum_{j\ge0}\frac{(D|sW|)^j}{(j+a)!}\\
  &\le M |W|^{2a-1}\frac{D^a}{a!}
                      e^{D|sW|+C\|Wm\|_1},
 \end{split}
 \tag{19}
\]
since \((j+a)!\ge j!a!\). This is (4), with the same
positive chart radius for every \(a,s,m\).
Normal convergence on compact parameter sets justifies joint
holomorphy and termwise differentiation. Applying Cauchy once
more on a fixed smaller disk of the form (16) proves (5), with
the clock and \(s\) exponents controlled by the same comparability.

On the initial product germ, commutation of \(E\) with \(I_\xi\)
proves (6) and \(C_{a,s}=I_\xi^a c_s\). It also identifies
\[
 c_s=\mathcal B_h\!\left(e^{shE}\mathscr W_m(h,Y)\right)
      =\mathcal B_h\mathscr W_m(h,e^{sh}Y).
 \tag{20}
\]
For (20), multiplication by \(h^j\) under the stated Borel
convention is exactly \(I_\xi^j\); the initial semigroup series
converges by the same elementary derivative/primitive factorial
estimate. These are identities of the canonical initial Borel
germs. The normally convergent extensions above and analytic
uniqueness carry all these identities to the outer charts.

In particular the original lift \(q=1\), \(\xi=0\), has
\(B_j=0\) for \(j>0\), and \(c_s=b\) there.
This statement is not imposed again at a returned lift of
\(\xi=0\). Any continued primitive constants on that lift are
the values of (15) and (2); resetting them would change the
source. The construction uses no independent homogeneous solution,
classical multiplier, or projection of an endpoint current.

## 6. Complete proof directs and scope

| Label | Complete proof direct | SHA256 |
|---|---|---|
| F | notes/research_full_clock_fixed_xi_outer_chart.md | 01defd9623325819ff96e901565a5d4b632482d52edba39aa043576a60f13f57 |
| P | notes/research_two_variable_polynomial_log_continuation_bound.md | 8d7966c484f535c06421d54a0569ffea6eb572cd4bd5abbc114a876401a3d3a1 |

F supplies the actual full source, exact scaled cores and original
overlap, plus the initial all-clock estimates. P supplies the
whole-density norm bound with explicit exponential dependence on
degree and pole order. The uniform primitive-order factorial,
meridian buffers, canonical semigroup and all its histories are
proved above.

The result supplies actual source companions through the outer
fixed-\(\xi\) chart. It does not construct a marked moving minor,
divide an internal Ward factor, discard a primitive history, or
identify an original physical-cycle coefficient.
Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
