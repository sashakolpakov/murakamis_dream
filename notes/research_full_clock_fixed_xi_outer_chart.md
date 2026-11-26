# A fixed-Borel-coordinate outer chart for the actual full-clock source

Private written proof, 18 November 2026.

The finite-core formula has a second useful homogeneity. After scaling
by the outer square-root coordinate, every core has a nonnegative
power of the remaining meridian ratio. A whole-density norm estimate
then sums all cores on a genuine fixed-Borel-coordinate chart through
the Alexander meridian, with all clocks retained.

The result concerns the full canonical source. It does not locate a
moving singular divisor, construct a marked minor, or identify a
physical relative cycle.

## 1. Actual source and the chart

Keep the original highest-cut source, all its independent index clocks,
and the simple two-branch node hypotheses of [O, Section 1].
Use its actual constants \(r\sigma\ne0\), nonzero clock direction
\(\mu\), and fixed decomposition
\[
 \psi=\lambda v+J\omega,\qquad \mu\cdot v=1,\quad \mu J=0.
 \tag{1}
\]
Here \(J\) has columns forming a basis of \(\ker\mu\); empty
transverse coordinates are allowed. Put
\[
 z=Y-\alpha,\qquad
 b(z,\xi,m)=\mathcal B_h\mathscr W_m(\alpha+z,\xi).
 \tag{2}
\]
Initially (2) is the actual convergent Borel germ away from \(z=0\),
with convention \(h^j\mapsto\xi^j/j!\). The initial pole chart is
\[
 F(z,w,\nu)
   =z\,b\!\left(z,\frac{z^2(1-w^2)}{4\sigma},\frac{\nu}{z}\right)
   =\sum_{k\ge0}z^kF_k(w,\nu),\qquad
 F_0=\frac r w
          \exp\!\left((\mu\cdot\nu)\frac{1-w}{2\sigma}\right).
 \tag{3}
\]
Its joint extension and entire clock dependence near \(w=1\)
are those of [O].

Define new coordinates
\[
 W^2=z^2-4\sigma\xi,\qquad q=\frac zW,\qquad \psi=Wm,
 \qquad g(q)=\frac{q-1}{2\sigma}.
 \tag{4}
\]
The initial branch has \(W=z\) at \(\xi=0\).
For \(q\ne0\), set
\[
                    H_k(q,\psi)
                         =q^{k-1}F_k(1/q,q\psi).
 \tag{5}
\]

**Theorem.** Every \(H_k\) in (5) extends to an entire function
of \(q,\psi\). For each fixed \(Q>1\), there are constants
\(M_Q,B_Q,C_Q,c>0\), independent of \(k\) and all clocks, such that
\[
 H_k(q,\lambda v+J\omega)
     =\sum_{|\gamma|\le2k}\omega^\gamma
                                  h_{k,\gamma}(q,\lambda),
 \qquad
 |h_{k,\gamma}|
 \le M_Q B_Q^k e^{C_Q|\lambda|}
                           \frac{c^{|\gamma|}}{\gamma!}
 \quad (|q|\le Q).
 \tag{6}
\]
Consequently
\[
 \mathcal H(W,q,\psi)=\sum_{k\ge0}W^kH_k(q,\psi)
 \tag{7}
\]
converges jointly for \(|W|<B_Q^{-1}\), \(|q|<Q\), and all
\(\psi\). It is entire in the clocks, with a \(W\)-radius independent
of their values. For \(t=B_Q|W|<1\),
\[
 |\mathcal H(W,q,\lambda v+J\omega)|
 \le \frac{M_Q}{1-t}
                \exp\!\left(C_Q|\lambda|
                              +c\sqrt t\,\|\omega\|_1\right).
 \tag{8}
\]
On \(W\ne0\) the exact identity
\[
 \boxed{\displaystyle
 b(z,\xi,m)=\frac1W\mathcal H\!\left(W,\frac zW,Wm\right)}
 \tag{9}
\]
continues the full original source from its initial germ.
In particular this source is jointly holomorphic through \(z=0\)
at every sufficiently small fixed \(\xi\ne0\), on either continued
outer square-root chart, and is entire in all \(m\).

## 2. The exact core homogeneity

Use the actual finite-core formula [C, (4), (18)]. Each term of
\(F_k\) is a constant times
\[
 \nu^\gamma\,\mathcal J_{b,a}F_0(\eta,y)
                  \big|_{y=\mu\cdot\nu},\qquad
 \eta=\frac{1-w^2}{4\sigma},
 \tag{10}
\]
where
\[
 \mathcal J_{b,a}=
 \begin{cases}
 I_\eta^{b-a}\partial_y^a,&b\ge a,\\
 \partial_\eta^{a-b}\partial_y^a,&a>b.
 \end{cases}
\]
The core has mark degree \(A_c=|\gamma|\), quantum order \(b\),
and Taylor order \(T\), with the exact relation
\[
 k=2b-A_c-a+T,\qquad
 0\le T\le k,\quad b\le2k,\quad a\le3k,\quad
 A_c\le2k,\quad a-b\le k.
 \tag{11}
\]
The order \(T\) includes the retained scalar prefactor and regular
propagators. It is not discarded in changing coordinates.

First suppose \(m_0=b-a\ge1\). In [C, (21)] make the substitution
\(\theta=s/q\), after setting \(w=1/q\) and \(y=q\mu\cdot\psi\).
The endpoint becomes \(g(q)\), and the exact kernel is
\[
 K(q,s)=\frac{q^2-1}{4\sigma}-qs+\sigma s^2
       =(g(q)-s)\{q-\sigma(g(q)+s)\}.
 \tag{12}
\]
Thus the core in (5) becomes exactly a constant times
\[
 \boxed{\displaystyle
 q^T\psi^\gamma\,\frac r{(m_0-1)!}
       \int_0^{g(q)} K(q,s)^{m_0-1}s^a
                           e^{(\mu\cdot\psi)s}\,ds.}
 \tag{13}
\]
Indeed the primitive block contributes \(q^{1+a-2b}\), while
the external factor and the clock monomial contribute
\(q^{k-1+A_c}\). Their product is \(q^T\) by (11).
The original primitive path has been changed by this linear
substitution. Its integrand is entire in \(s\), so it may equally
be the straight segment with the displayed endpoints.

For the derivative block put \(l=a-b\ge0\).
There is a useful way to avoid a false chain rule in the varying
ratio \(q\): first hold an auxiliary \(q\ne0\) fixed and write
\(v_0=qw\) before differentiating in \(\eta\).
Then
\[
 \partial_\eta
      =q^2\left(-\frac{2\sigma}{v_0}\partial_{v_0}\right).
 \tag{14}
\]
Only after these derivatives are taken set \(v_0=1\) and
\(y=q\mu\cdot\psi\). The resulting core in (5) is
\[
 \boxed{\displaystyle
 q^T\psi^\gamma
 \left[
  \left(-\frac{2\sigma}{v_0}\partial_{v_0}\right)^l
  \frac r{v_0}
       \left(\frac{q-v_0}{2\sigma}\right)^a
       \exp\!\left((\mu\cdot\psi)\frac{q-v_0}{2\sigma}\right)
 \right]_{v_0=1}.}
 \tag{15}
\]
The prefactor before multiplication by \(q^{k-1+A_c}\) is again
\(q^{1+a-2b}\). Formula (15) includes \(l=0\).
In particular no derivative of \(q\psi\) has been silently added
or removed.

Equations (13) and (15) are entire in \(q,\psi\): \(T\ge0\),
the first integrand is polynomial times an exponential, and the
finite derivatives in the second are evaluated at \(v_0=1\).
They are identities for the original finite-core terms on \(q\ne0\).
Their removable extension proves the first assertion of the theorem.
It also gives, for example,
\[
                         H_0(q,\psi)
                              =r e^{(\mu\cdot\psi)g(q)}.
 \tag{16}
\]
No estimates on the individual core constants are used below.

## 3. A joint Cauchy class without a ratio-coordinate pole

Decompose \(\psi\) by (1). Expand the core polynomial
\(\psi^\gamma\) in \(\lambda,\omega\); its total degree is
at most \(2k\). Multiplication by \(\lambda^e\) is
\((-\partial_\chi)^e\) on the canonical longitudinal Cauchy
density, exactly as in [C, Section 5].

The density of the block (15), before this multiplication, is
\[
 q^T\left[
 \left(-\frac{2\sigma}{v_0}\partial_{v_0}\right)^l
 \frac{r((q-v_0)/(2\sigma))^a}
      {v_0\{\chi-(q-v_0)/(2\sigma)\}}
 \right]_{v_0=1}.
 \tag{17}
\]
It has denominator \((\chi-g)^{l+1}\) and polynomial numerator
of total degree at most \(a+l+T\) in \((q,\chi)\).
After \(e\le2k\) longitudinal multiplications the denominator
exponent is at most \(l+e+1\), without raising that degree bound.

For (13), apply polynomial division to its segment Cauchy transform.
Before multiplication by \(q^T\), the polynomial density has total
degree \(D=2m_0-2+a\le4k-2\). Its transform is a polynomial plus
a polynomial times \(\log(1-g(q)/\chi)\), each of total degree
at most \(D\); this follows from the explicit formula [C, (23)].
Including \(q^T\) and \(e\) longitudinal multiplications gives
denominator \(\chi^e(\chi-g)^e\) and numerator degrees at most
\(D+T+e\).

It follows that, coefficientwise in \(\omega\), the canonical
exterior density of \(H_k\) has the joint form
\[
 \boxed{\displaystyle
 \mathcal G_{k,\gamma}(q,\chi)=
 \frac{P_{k,\gamma}(q,\chi)+
        Q_{k,\gamma}(q,\chi)\log(1-g(q)/\chi)}
      {\chi^{2k}(\chi-g(q))^{3k+1}},}
 \tag{18}
\]
where both numerator total degrees are at most \(13k+2\).
There is no factor \(q\) in the denominator.
To check the conservative degree bound, clearing the denominator
in (17) to (18) gives degree at most
\(5k+a+T-e\le9k\).
For a primitive block it gives at most
\(D+T+5k+1-e\le10k-1\).
The case \(k=0\) is covered by (16).

Every density here has only negative Laurent powers at infinity.
Its moments are the corresponding entire clock function, and its
logarithm initially means the exterior series. Thus the displayed
representative is the canonical moment density, not a representative
modulo an unknown holomorphic summand. Segment banks, scalar
framing contributions and endpoint derivatives are all retained.

## 4. Uniform initial norms and continuation through \(q=0\)

The initial estimates in [O, Section 2] give, after decreasing a
fixed \(q\)-neighborhood of one,
\[
 |H_k(q,\lambda v+J\omega)|
       \le M A^k
              e^{C_\lambda|\lambda|+C_\omega\|\omega\|_1}.
 \tag{19}
\]
Indeed \(1/q\) stays in the original \(w\)-neighborhood,
the clocks there are \(q\psi\), and the remaining factor
\(q^{k-1}\) costs only a fixed exponential in \(k\).
Choose \(0<\epsilon<1\) whose closed \(q\)-disk about one lies
in this neighborhood, and increase both clock constants to at least
one.

For \(\omega^\gamma\) extraction use radii
\(\gamma_i/C_\omega\) for positive \(\gamma_i\), setting unused
coordinates to zero. This preserves the optimized factorial:
\[
 |h_{k,\gamma}(q,\lambda)|
       \le M A^k e^{C_\lambda|\lambda|}
                         \frac{c^{|\gamma|}}{\gamma!},
                         \qquad c=eC_\omega.
 \tag{20}
\]
The elementary estimate used here is
\(\prod_i(eC_\omega/\gamma_i)^{\gamma_i}
\le c^{|\gamma|}/\gamma!\).
Optimized Cauchy estimation in \(\lambda\), using \(n!\le n^n\),
then gives
\[
 |\partial_\lambda^n h_{k,\gamma}(q,0)|
    \le M A^k\frac{c^{|\gamma|}}{\gamma!}(eC_\lambda)^n.
 \tag{21}
\]
The \(n=0\) case follows directly from (20).

Fix \(Q>1\). Choose \(R>eC_\lambda\), with a strict margin
above \(\sup_{|q|\le Q}|g(q)|\) and the initial circle's endpoint
modulus \(\epsilon/(2|\sigma|)\). On
\[
                  |q-1|=\epsilon,\qquad |\chi|=R,
 \tag{22}
\]
the canonical moment series
\(\sum_{n\ge0}\partial_\lambda^n h_{k,\gamma}(q,0)\chi^{-n-1}\)
converges normally and has bound
\[
                    M_1 A^k\,\frac{c^{|\gamma|}}{\gamma!}.
 \tag{23}
\]
It is identical to (18), since their negative Laurent coefficients
at infinity agree.

Apply [P] to the entire expression (18), with its parameter
\(\sigma\) replaced by \(-\sigma\), so that
\(g(q)=(1-q)/(2(-\sigma))\). Its ratio-coordinate pole order
is zero. The degrees and the other two pole orders are \(O(k)\).
On a buffered target product \(|q|\le Q\), \(|\chi|=R\),
the two remaining divisor distances are positive and the exterior
logarithm is uniformly bounded. Therefore [P] gives
\[
 \sup|\mathcal G_{k,\gamma}(q,\chi)|
            \le M_2 B_Q^k\,\frac{c^{|\gamma|}}{\gamma!}.
 \tag{24}
\]
Although [P]'s general statement excludes a zero of its first
coordinate, its proof and estimate have no inverse-coordinate factor
when that pole order is zero. Equivalently apply its bound on the
punctured target, where all constants are independent of the distance
to \(q=0\), and remove the puncture using (18). The logarithm on
this target is its exterior series and is analytic at \(q=0\).
This justifies (24) on the whole product without a hidden loss
as \(q\to0\).

Integrating (24) against \(e^{\lambda\chi}\) on the same outer
circle reconstructs the actual \(h_{k,\gamma}\).
It proves (6), after absorbing its fixed length and taking
\(C_Q=R\). No bound on individual core coefficients or on the
two separate polynomial-log summands has been substituted for the
norm of their sum.

## 5. Summation and the genuine fixed-\(\xi\) source

The transverse degree is at most \(2k\). Hence (6) gives, with
\(t=B_Q|W|<1\),
\[
 \begin{split}
 \sum_{k\ge0}|W|^k|H_k|
  &\le M_Q e^{C_Q|\lambda|}
       \sum_{k\ge0}t^k
             \sum_{|\gamma|\le2k}\frac{c^{|\gamma|}
                                       |\omega^\gamma|}{\gamma!}\\
  &\le \frac{M_Q}{1-t}
       e^{C_Q|\lambda|+c\sqrt t\,\|\omega\|_1}.
 \end{split}
 \tag{25}
\]
A multiindex of degree \(j\) enters at \(k=\lceil j/2\rceil\);
its summed weight is at most \(t^{j/2}/(1-t)\).
The multinomial exponential series gives the second line.
This proves normal convergence on compact clock sets, joint
holomorphy, and the radius independent of all clocks.

On the initial overlap, substituting \(z=qW\) and \(\nu=qWm\)
into (3) is an exact identity:
\[
 \frac1z\sum_{k\ge0}z^kF_k(1/q,qWm)
            =\frac1W\sum_{k\ge0}W^kH_k(q,Wm).
 \tag{26}
\]
Both sides converge there. Analytic uniqueness makes the right
side continuation of the original full source, proving (9).
Different choices of \(Q\) or of a sufficiently large spectral
circle agree on overlaps, first by (26), and also directly by the
canonical exterior moments and normally convergent coefficient
series.

Finally the coordinate map is
\[
             z=qW,\qquad \xi=\frac{(q^2-1)W^2}{4\sigma},
 \qquad
 \det\frac{\partial(z,\xi)}{\partial(q,W)}
                         =-\frac{W^2}{2\sigma}.
 \tag{27}
\]
It is locally invertible whenever \(W\ne0\), including at \(q=0\).
For fixed sufficiently small \(\xi_0\ne0\), choose either locally
continued square root \(W(z)^2=z^2-4\sigma\xi_0\).
Near \(z=0\), \(W(z)\ne0\), \(|W(z)|<B_Q^{-1}\), and
\(|z/W(z)|<Q\). Equation (9) is therefore a genuinely joint
holomorphic source chart through \(Y=\alpha\), not merely a
restriction defined on its \(z=0\) fiber. The substitution
\(\psi=Wm\) is linear in every clock, so all \(m\)-values remain
allowed with the same chart radius.

## 6. Scope and complete proof directs

The chart retains both the even and odd parts of the actual source,
all clocks, and every connector in its Cauchy representation.
It is an outer chart with \(W\ne0\); the allowed radius can depend
on the bounded ratio domain. Nothing here identifies the singular
set at fixed nonzero \(z\), constructs the full marked moving
minor or its multiplicative clock character, or transports an
original cutoff cycle to a physical observation. Primitive histories
and endpoint currents are not discarded by this statement.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| O | notes/research_full_clock_outer_borel_continuation.md | 8bec9e7934ba671d3dee836cb32dde3870113ed3e95348a83c39ac9e33b611f0 |
| C | notes/research_actual_clock_finite_core_volterra_carriers.md | 7c7630796cb2d7ee2e81d0efceb9c9008bbb5214169ce4da5b76f068c0341d9a |
| P | notes/research_two_variable_polynomial_log_continuation_bound.md | 8d7966c484f535c06421d54a0569ffea6eb572cd4bd5abbc114a876401a3d3a1 |

O supplies the canonical coefficient family, its actual initial
whole-clock estimate, and the nonzero clock direction with a fixed
dual. C supplies the exact cores and excess equality, with all
original source operations retained. P supplies the norm estimate
for the whole joint polynomial-log density. The new homogeneity,
absence of a ratio pole, clock-factorial bounds, summation and
fixed-\(\xi\) coordinate interpretation are proved above.

Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
