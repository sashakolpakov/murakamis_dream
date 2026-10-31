# Zeros of the ADO meridian state approach the complete point

31 October 2026.

For a knot whose Kashaev invariant has positive exponential growth, the
reduced ADO meridian state takes exponentially different values at two
points separated by order $1/N$. Its value at the complete point is the
Kashaev invariant, whereas its value one quantum shift away is exactly
$1$. The state is a Laurent polynomial whose degree grows at most
linearly with $N$. Together these facts force actual zeros within order
$1/N$ of the complete point. This note proves an explicit bound on that
distance, retaining the marked meridian coordinate and the full
modified-dimension factor.

The obstruction to a uniform nonzero scalar asymptotic expression across
the two points was already described in the
[formal A-curve period discussion](formal_a_curve_period_torsor.md#the-actual-peripheral-normalization-includes-a-difference-constant)
and the [regular-period construction](regularized_kashaev_period.md).
The quantitative zero bound below makes that obstruction precise for
the actual knot state. It does not identify a classical A-polynomial
factor. The canonical regular remainder, defined by subtracting the
ordinary-color polar data, remains a separate candidate for such a
comparison.

## 1. The actual state and its two nearby values

Fix a zero-framed knot $K$ for which the actual all-level volume limit is
known. Write $K_N(K)$ for its reduced Kashaev invariant, with the unknot
normalized to $1$, and assume

\[
 q_N=e^{\pi i/N},\qquad
 \lim_{N\to\infty}\frac1N\log|K_N(K)|
       =v=\frac{V}{2\pi}>0.
 \tag{1}
\]

For example, this applies to the fixed long-twist knots covered by the
[strict Conway-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md)
and the [ordered net-twist theorem](actual_conway_net_twist_volume.md).
In either application, the knot and its integer twist weights are fixed
before $N$ tends to infinity. The argument below otherwise uses no
restriction on the knot presentation.

Let $F_N(M)$ be its reduced ADO state. It is the zero-framed cut-tangle
scalar, equivalently the full modified-trace invariant divided by the
modified dimension. The relation between the unrolled color
parameter $\alpha$, its exponential $x$, and the marked meridian
eigenvalue $M$ is

\[
 x=q_N^\alpha,\qquad M=-q_Nx.
 \tag{2}
\]

Thus $\alpha=N-1$ gives $M=1$. The exact
[ADO normalization](kashaev_ado_pointing.md) and
[integer-color specialization](root_orbit_pointing.md) give

\[
 F_N(-q_N^j)=C_j(q_N)\quad(1\le j\le N),\qquad
 F_N(1)=K_N(K),\qquad C_1(q)=1.
 \tag{3}
\]

Here $C_j$ denotes the reduced $j$-dimensional ordinary quantum-group
invariant of the same knot. In particular, its one-dimensional value
is $1$.

The [squared-meridian descent](even_meridian_norm_descent.md) proves
the exact identity

\[
 F_N(-M)=F_N(M)
 \qquad(N\ge2).
 \tag{4}
\]

There is no even-level exception in (4). To recall why the normalization
introduces no sign, choose a $b$-strand braid of writhe $w$ closing to
$K$. Its closure has one component, so the braid permutation is a
$b$-cycle and $w\equiv b-1\pmod2$. The integer
$\kappa_D=w-b+1$ is therefore even. In the exact meridian-shift
insertion, all crossing factors depend on $Y=M^2$. Their product over
the $N$ shifts $Y\mapsto q_N^2Y$ is $1$: the numerator and denominator
products cancel by $\prod_{r=0}^{N-1}(1-q_N^{2r}z)=1-z^N$.
The remaining framing factor has cyclic product
$q_N^{-N\kappa_D}=1$. After $N$ shifts, $M$ has become $-M$, proving
(4). At a vanishing numerator or denominator this is the cancelled
rational identity, not a quotient of separately evaluated zeros.

Equations (3) and (4) now imply, exactly at every level,

\[
 F_N(q_N)=F_N(-q_N)=1.
 \tag{5}
\]

For sufficiently large $N$, (1) also gives $K_N(K)\ne0$. Consequently

\[
 \frac{F_N(q_N)}{F_N(1)}=\frac1{K_N(K)},\qquad
 \lim_{N\to\infty}\frac1N
       \log\left|\frac{F_N(q_N)}{F_N(1)}\right|=-v.
 \tag{6}
\]

The shift in (6) is the actual meridian shift $M\mapsto q_NM$.
Writing $F_N(M)=f_N(Y)$ and $Q_N=q_N^2$, its squared-coordinate form is
$Y\mapsto Q_NY$, with $f_N(Q_N)=1$.

## 2. A two-value estimate for Laurent polynomials

The following elementary estimate explains why a degree bound matters.
For a nonzero Laurent polynomial $P(z)=\sum_{j=m}^{n}a_jz^j$ with
$a_ma_n\ne0$, call $D=n-m$ its exponent spread. Multiplication by a
Laurent monomial changes neither this spread nor the nonzero roots.

**Two-value lemma.** Suppose $z_0,z_1\ne0$ have equal modulus,
$P(z_0)P(z_1)\ne0$, and

\[
 A=\left|\frac{P(z_0)}{P(z_1)}\right|>1,\qquad
 \delta=|z_1-z_0|.
 \tag{7}
\]

Then $D>0$, and some nonzero root of $P$ lies at distance at most

\[
 \frac{\delta}{1-A^{-1/D}}
 \tag{8}
\]

from $z_0$.

To prove this, factor the ordinary polynomial obtained by removing the
lowest Laurent monomial:

\[
 z^{-m}P(z)=a_n\prod_{j=1}^{D}(z-\zeta_j).
 \tag{9}
\]

Its constant coefficient is nonzero, so all $\zeta_j$ are nonzero.
If $D=0$, the equal moduli of $z_0$ and $z_1$ would give $A=1$.
For $D>0$, put $r=\min_j|z_0-\zeta_j|$. If $r\le\delta$, (8)
already follows. Otherwise, the Laurent monomial has modulus ratio
$1$, and the triangle inequality gives

\[
 \begin{aligned}
 -\log A
 &=\sum_{j=1}^{D}\log
        \frac{|z_1-\zeta_j|}{|z_0-\zeta_j|}\\
 &\ge D\log\left(1-\frac{\delta}{r}\right).
 \end{aligned}
 \tag{10}
\]

Solving (10) for $r$ proves (8). The proof retains root multiplicities
and requires no information about their angles or simplicity. A larger
upper bound for $D$ may replace $D$ in (8), giving a weaker valid bound.

## 3. The finite crossing matrices give a linear degree bound

Fix any braid presentation of $K$ with $b$ strands and $L$ crossings.
Let $L_+$ and $L_-$ count the positive and negative crossings, so
$L=L_++L_-$ and $w=L_+-L_-$. Put $d=N-1$.

The [finite cut-state construction](finite_sum_annihilator.md) retains
all indices in $\{0,\ldots,d\}$. The explicit
[positive and negative crossing entries](relative_octahedral_period.md#exact-formulas-for-both-actual-crossings)
make their color dependence particularly transparent. After stripping
the common Cartan scalar, the positive entry with input indices $(a,b)$
and shift $k$ is an $x$-independent coefficient times

\[
 x^{-a-b-k}(Qx^2/Q^a;Q)_k,
 \qquad 0\le k\le\min(a,d-b),\qquad Q=q_N^2.
 \tag{11}
\]

Here $(u;Q)_k=\prod_{r=0}^{k-1}(1-uQ^r)$. The negative entry is an
$x$-independent coefficient times

\[
 x^{a+b-k}(Qx^2/Q^b;Q)_k,
 \qquad 0\le k\le\min(b,d-a).
 \tag{12}
\]

These are the actual checked crossings; the two shift cutoffs are
different and have both been retained. Expanding the finite products
in (11) and (12) gives the respective exponent intervals

\[
 \begin{aligned}
 [-a-b-k,-a-b+k]&\subset[-2d,0],\\
 [a+b-k,a+b+k]&\subset[0,2d].
 \end{aligned}
 \tag{13}
\]

For example, in the positive case $k\le d-b$ bounds $a+b+k$ by
$2d$, while $k\le a$ bounds $-a-b+k$ by $0$. The negative case uses
$k\le d-a$ and $k\le b$. The factorial denominators depend only
on $q_N$, are nonzero for their actual indices below $N$, and introduce
no color denominator.

The common Cartan scalars cancel against the zero-framing twist
correction. What remains of that correction is $x^{wd}$. Each of
the $b-1$ pivotal traces contributes $x^{-d}$ times an $x$-independent
factor. Thus the common remaining monomial is $x^{d(w-b+1)}$.
Products and finite sums cannot enlarge the exponent interval. After
including this monomial, the support of the actual reduced state lies
in

\[
 [-d(L+b-1),\ d(L-b+1)].
 \tag{14}
\]

The substitution $x=-q_N^{-1}M$ only multiplies coefficients by nonzero
constants. It leaves (14) unchanged. In particular the actual Laurent
spread, after any cancellations, satisfies

\[
 D_N\le2L(N-1),\qquad D_N^Y\le L(N-1).
 \tag{15}
\]

The second bound is for $f_N(Y)$: exact evenness (4) divides every
actual exponent and its spread by two. These estimates hold at both
parities and do not require a bound on the number of summands. For
the knots in (1), $L>0$ and both spreads are positive for sufficiently
large $N$, because a Laurent monomial cannot satisfy (6).

## 4. A quantitative zero bound at the complete point

Let

\[
 r_N=\min\{|z-1|:z\ne0,\ F_N(z)=0\},\qquad
 \delta_N=|q_N-1|=2\sin\frac{\pi}{2N}.
 \tag{16}
\]

For all sufficiently large $N$, the two-value lemma applied at $1$
and $q_N$ gives

\[
 r_N\le
 \frac{\delta_N}{1-|K_N(K)|^{-1/D_N}}
 \le\frac{\delta_N}
              {1-|K_N(K)|^{-1/[2L(N-1)]}}.
 \tag{17}
\]

In particular,

\[
 \limsup_{N\to\infty}Nr_N
 \le\frac{\pi}{1-\exp(-V/(4\pi L))}.
 \tag{18}
\]

The squared-meridian coordinate improves the constant. Apply the same
lemma to $f_N$ at $1$ and $Q_N$. Its spread is at most $L(N-1)$,
and $|Q_N-1|\sim2\pi/N$. Hence it has a zero $\zeta_N$ with

\[
 \limsup_{N\to\infty}N|\zeta_N-1|
 \le\frac{2\pi}{1-\exp(-V/(2\pi L))}.
 \tag{19}
\]

Choose the square root $z_N$ of $\zeta_N$ that tends to $1$. It is a
zero of $F_N$, and
$|z_N-1|=|\zeta_N-1|/|z_N+1|$, where $|z_N+1|\to2$. We obtain
the stronger estimate

\[
 \boxed{\displaystyle
 \limsup_{N\to\infty}Nr_N
 \le\frac{\pi}{1-\exp(-V/(2\pi L))}.}
 \tag{20}
\]

Every fixed braid presentation supplies a valid $L$. This is a bound
on zeros of the actual reduced knot state, not an auxiliary polynomial
chosen to have the same complete value. It does not give their number
in the shrinking disk, their limiting directions, or a classical
geometric interpretation of their factors.

## 5. Consequences for shift ratios and the full normalization

There is no fixed complex neighborhood of $M=1$ on which all
sufficiently large $F_N$ are nonvanishing. Moreover, (6) directly rules
out a finite nonzero limit of $F_N(q_NM)/F_N(M)$ at $M=1$.
These are distinct assertions: a zero of $F_N$ need not be a pole of
that quotient, because a shifted numerator zero may cancel it.

For example, a scalar WKB expression on a fixed neighborhood of $1$
would require a holomorphic action $S$ and nonvanishing amplitudes
$a_N$ converging locally uniformly to a nonzero holomorphic function,
with

\[
 F_N(M)=c_N e^{NS(M)}a_N(M),\qquad c_N\ne0.
 \tag{21}
\]

Such an expression would imply
$F_N(q_N)/F_N(1)\to\exp(\pi iS'(1))\ne0$, contradicting (6).
It is also incompatible with (20). This does not exclude expressions
on domains omitting the complete point, or with level-dependent
divisors explicitly retained.

A scalar normalization independent of $M$ changes neither the roots
nor the ratio in (6). A fixed rational or algebraic gauge, on a branch
that is holomorphic and nonzero near $(q,M)=(1,1)$, also cannot remove
the roots and has ratio tending to $1$ between the two points. Gauges
with moving poles or zeros require separate analysis.

The actual full modified-trace state is an important example of the
latter case. Its exact factor is

\[
 \mathcal N_N(M)=d_N(M)F_N(M),\qquad
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 \eta_N=i^{N+3},\qquad d_N(1)=\eta_N/N.
 \tag{22}
\]

At $M=q_N$ the denominator in (22) has derivative $-2Nq_N^{-1}$.
Since $F_N(q_N)=1$, the full state has the uncancelled simple pole

\[
 \operatorname{Res}_{M=q_N}\mathcal N_N(M)
       =\frac{\eta_N(1-q_N^2)}{2N}\ne0
       \qquad(N\ge2).
 \tag{23}
\]

Its value at $M=1$ is nevertheless the regular whole-germ value
$\eta_NK_N(K)/N$. Thus the full normalization does not supply a
holomorphic nonzero scalar packet across these points either. For
sufficiently large $N$, its shift quotient has a pole at $M=1$,
consistent with the exact normalization gauge

\[
 \frac{d_N(q_NM)}{d_N(M)}
       =-q_N^{-1}\frac{q_N^2M^2-1}{M^2-1}.
 \tag{24}
\]

## 6. The canonical regular remainder is a different object

The [regular-period construction](regularized_kashaev_period.md)
subtracts prescribed polar data, rather than applying a nonzero
scalar normalization. Let $P_N^{\mathrm{ord}}$ be the unique polynomial
of degree at most $N-2$ taking the values $C_j(q_N)$ at $Q_N^j$ for
$1\le j<N$. Define

\[
 S_N(Y)=\frac{Y^N-1}{Y-1},\qquad
 R_N^{\mathrm{reg}}(Y)
     =\frac{f_N(Y)-P_N^{\mathrm{ord}}(Y)}{S_N(Y)}.
 \tag{25}
\]

All roots of $S_N$ are simple ordinary-color points. The numerator
vanishes there, so $R_N^{\mathrm{reg}}$ is Laurent polynomial. In the
full state this gives the exact separation

\[
 \mathcal N_N(M)
  =\eta_NM^{N-1}R_N^{\mathrm{reg}}(M^2)
   +\eta_NM^{N-1}\frac{P_N^{\mathrm{ord}}(M^2)}{S_N(M^2)}.
 \tag{26}
\]

The second term contains all finite nonzero polar principal parts.
The ordinary-color bound in the same construction gives
$|P_N^{\mathrm{ord}}(1)/N|=O_K(N^{b-1})$. Therefore

\[
 R_N^{\mathrm{reg}}(1)
   =\frac{K_N(K)-P_N^{\mathrm{ord}}(1)}{N},\qquad
 \lim_{N\to\infty}\frac1N\log|R_N^{\mathrm{reg}}(1)|=v.
 \tag{27}
\]

Its first shifted value is not the ordinary anchor $1$. It is instead

\[
 R_N^{\mathrm{reg}}(Q_N)
  =\frac{f_N'(Q_N)-(P_N^{\mathrm{ord}})'(Q_N)}{S_N'(Q_N)}.
 \tag{28}
\]

Thus the two-value obstruction proved for $F_N$ does not automatically
apply to $R_N^{\mathrm{reg}}$. Nor does (27) prove a neighborhood
asymptotic or a shift-ratio limit for this remainder.

A specified actual all-level annihilator gives the existing affine
equation for the regular remainder, after its fixed rational gauge
and denominator clearing. Its inhomogeneous term has fixed Laurent
support and polynomially bounded coefficients. One possible next
theorem would provide a locally uniform, nonzero shift-ratio limit
for this actual regular state together with a locally uniform
exponential lower bound. On a domain avoiding the fixed coefficient
poles, such bounds would make the inhomogeneous term negligible after
division by the state. The limiting ratio would then satisfy the
homogeneous classical symbol. Its identification with the preferred
geometric longitude would still require the marked geometric
comparison.

The complete scalar volume theorem and the
[pointed quantum A-period and Gram formulas](actual_conway_pointed_quantum_a_volume.md)
remain valid. What changes is the proposed neighborhood statement:
the reduced state has the exponential one-step drop and nearby zeros
proved above, and the full state has a nearby pole. The canonical
regular remainder must be studied with its own affine equation and
its ordinary-color subtraction intact.


## 7. The boundary factor of every polynomial annihilator

The same ordinary-color bounds give an exact algebraic restriction on
the recurrence. The squared-meridian version is the necessity theorem
in [the peripheral normal-period note](peripheral_normal_period.md#2-a-nonzero-complete-column-forces-polynomial-growth).
For the positive-volume knots in (1), its hypothesis is now established.
Here is the corresponding statement without requiring an even operator.

Let

\[
 P=\sum_{i=0}^{d}a_i(q,M)T^i,\qquad TM=qMT,\qquad
 a_i\in\mathbb C[q^{\pm1},M^{\pm1}]
 \tag{29}
\]

be any fixed genuine all-level annihilator of the reduced state, after
clearing its rational denominators. Then

\[
 (q^{2i}M^2-1)\mid a_i(q,M)\quad(0\le i\le d),\qquad
 P=B(M^2-1)
 \tag{30}
\]

for a polynomial quantum-torus operator $B$. This conclusion concerns
all annihilators in the specified integral ring, not just a chosen
minimal generator.

Fix $i$ and evaluate the exact annihilation equation at
$M=\pm q_N^{-i}$, with $N>d$. The $i$th term contains
$F_N(\pm1)=K_N(K)$. Every other term is an ordinary-color value. If
$k=j-i>0$, evenness and (3) give $F_N(\pm q_N^k)=C_k(q_N)$.
If $k<0$, use $q_N^N=-1$ to obtain
$F_N(\pm q_N^k)=C_{N+k}(q_N)$. All these indices lie between $1$
and $N-1$. The fixed-braid bound is uniform over that entire range:
$|C_r(q_N)|\le(N/2)^{b-1}$.

The fixed Laurent coefficients in (29) are bounded on these unit-circle
trajectories. Hence the annihilation equation gives

\[
 |a_i(q_N,\pm q_N^{-i})|\,|K_N(K)|\le C_PN^{b-1}.
 \tag{31}
\]

If the Laurent polynomial $a_i(q,\pm q^{-i})$ were nonzero, its finite
vanishing order $\nu$ at $q=1$ would give a lower bound
$cN^{-\nu}$ at $q_N$ for all sufficiently large $N$. Equation (31)
would then bound $|K_N(K)|$ by a polynomial, contradicting (1).
Thus both trajectory polynomials vanish identically. Their kernels
are the relatively prime ideals generated by $M-q^{-i}$ and
$M+q^{-i}$, proving the divisibility in (30). Finally,
$T^i(M^2-1)=(q^{2i}M^2-1)T^i$, which proves the displayed order of
multiplication. The finite exceptional levels of the annihilator do
not affect this argument.

For a polynomial annihilator in the squared-coordinate ring
$Y=M^2$, with shift $\mathsf S Y=q^2Y\mathsf S$, the statement is
$P_Y=B_Y(Y-1)$. An arbitrary unsquared operator need not itself have
even coefficients. It splits as $P_0(q,Y,\mathsf S)+M P_1(q,Y,\mathsf S)$;
evenness of the state makes the two parts separate annihilators, and
the argument applies to each. Thus the squared polynomial annihilator ideal is contained
in the left ideal generated by $Y-1$. Its cyclic module has the
boundary quotient

\[
 \Delta=\mathcal R/\mathcal R(Y-1),\qquad
 \mathcal R=\mathbb C(q)[Y^{\pm1},\mathsf S^{\pm1}].
 \tag{32}
\]

The commutation rule above is understood in this ring. Localizing to
$\mathbb C(q,Y)$ makes $Y-1$ invertible and kills this quotient. The
boundary information must therefore be retained in a meridian lattice
alongside the localized recurrence. This is a normalization factor of
shift order zero; it is not the sought geometric factor involving the
longitude variable.

One must also keep the change of state when removing the factor:
$B$ annihilates $(M^2-1)F_N(M)$, whose value at completeness is zero.
The knot invariant is its normal derivative,

\[
 K_N(K)=\left.\frac12\frac{d}{d\log M}
                   \bigl[(M^2-1)F_N(M)\bigr]\right|_{M=1}.
 \tag{33}
\]

The peripheral normal-period note develops the corresponding affine
lifting equation and states the additional rank condition under which
its first normal derivative determines the period. Neither (30) nor
the nearby-zero bound proves that rank condition or identifies the
remaining classical characteristic factor with the geometric
longitude. They specify boundary data that such a comparison must
retain.
