# A sharp complete-circle nodal energy from the original source

29 October 2026. The actual complete-circle packet has the sharp
physical-node exponent \(v_8/\pi\). This follows from an exact discrete
Chebyshev identity and the already proved NONZERO finite-source
asymptotic on each fixed Bernstein ellipse. It needs no assertion
about the phases of all Newton or monomial coefficients.

Consequently a retained complete belt gives a positive original
source, with an exact rate for every fixed reflected power. This is
an all-channel source theorem. Its interpretation as a family of
geometric belted sums requires a separate literal disk-gluing
certificate; it is not inferred from the rate.

## 1. The unchanged packet and the actual complete belt

Use \(N\geq2,d=N-1,q=e^{\pi i/N},Q=q^2\), and

\[
 M=\lfloor d/2\rfloor,\qquad
 c_a=2\cos((2a+1)\pi/N),\quad 0\leq a<N.
\]

These are the actual pair-Casimir nodes. Write \(m_c=2\) at each
double node and \(m_{-2}=1\) at the odd simple node, so
\(\sum_{c\ \mathrm{distinct}}m_c=N\). Let

\[
 z_N=\mathscr R(R^{-1}L_N),\qquad
 z_N^\sharp=\mathscr R(RL_N),\qquad
 j_0=v_8/\pi.                                             \tag{1}
\]

Here \(R\) is the FULL original checked crossing, \(L_N\) its literal
ordinary auxiliary-circle trace, and \(\mathscr R\) the genuine
unscaled turn. The sharp sign is coefficient conjugation in the
real Casimir variable, realized by the stated actual reflected
diagram. The [complete polynomial proof](actual_pretzel_complete_base_casimir_polynomial.md)
gives \(\deg z_N=M\), at every parity, including every Casimir normal.
The [full-circle sewing theorem](general_augmented_graph_source_extension.md#7-complete-circle-connectors-a-coherent-channel-sum-not-independent-blocks)
proves on the FULL root algebra

\[
 \phi(L_Nfg)=N\sum_{c\ \mathrm{distinct}}m_c f(c)g(c).
                                                               \tag{2}
\]

The positive weights in (2) come from the retained derivatives of
\(L_N\) at its double zeros. Thus (2) does not discard the original
nonsemisimple normal source. In particular the complete belt has not
been replaced by a value-only trace with different normalization.

## 2. Exact discrete Chebyshev sampling, with both endpoint parities

Let \(T_k(\cos\theta)=\cos(k\theta)\). For \(0\leq k,l\leq M\),

\[
 \frac1N\sum_{a=0}^{N-1}T_k(c_a/2)T_l(c_a/2)
 =\begin{cases}1,&k=l=0,\\1/2,&k=l>0,\\0,&k\ne l.\end{cases}
                                                               \tag{3}
\]

Indeed \(\sum_a e^{in(2a+1)\pi/N}=0\) for
\(0<|n|<N\), and \(k+l\leq2M<N\). Product-to-sum proves
(3). Replacing the sum over \(a\) by the distinct-node sum with
weights \(m_c\) is EXACT. The odd endpoint \(-2\) has weight one;
there is no duplicated simple node or omitted even middle node.

For any complex polynomial \(f\) of degree at most \(M\), write

\[
 f(z)=\sum_{k=0}^M a_kT_k(z/2),\qquad
 b(f)=\max_{c\ \mathrm{distinct}}|f(c)|.
\]

Equation (3) gives

\[
 a_0=\frac1N\sum_cm_cf(c),\qquad
 a_k=\frac2N\sum_cm_cf(c)T_k(c/2)\quad(k>0).
\]

Hence \(|a_0|\leq b(f), |a_k|\leq2b(f)\). For fixed
\(\eta>0\),

\[
 \boxed{\quad
 |f(-2\cosh\eta)|\leq(2M+1)e^{M\eta}b(f)
                         \leq N e^{M\eta}b(f).
 \quad}                                                       \tag{4}
\]

This uses \(T_k(-\cosh\eta)=(-1)^k\cosh(k\eta)\), not
an extrapolation of numerical root values. It is stable at all levels.

## 3. Sharp maximum on the actual physical nodes

The [proved finite-source circle theorem](actual_pretzel_coherent_circle_and_period_asymptotic.md),
equations (9),(13)--(15), supplies for EVERY fixed \(\eta>0\)

\[
 z_N(-2\cosh\eta)
   =e^{-i\pi d/4}a(\eta)e^{Nj(\eta)}(1+o(1)),
 \qquad a(\eta)\ne0,                                    \tag{5}
\]
\[
 \limsup_N\frac1N\log\max_{|w|=e^\eta}
          |z_N(w+w^{-1})|\leq j(\eta),\qquad
 \lim_{\eta\downarrow0}j(\eta)=j_0.                    \tag{6}
\]

These are estimates for the literal finite polynomial, not a formal
critical value or an unspecified contour. In particular (5) has a
proved nonzero source amplitude. The limiting value in (6) follows
from the displayed Lobachevsky formula there:
\(j(0)=8\Lambda(\pi/4)/\pi=v_8/\pi\).

Put \(b_N=b(z_N)\). The segment \([-2,2]\) lies inside every
fixed Bernstein ellipse \(z=w+w^{-1},|w|=e^\eta\). The maximum
principle and (6) give

\[
 \limsup_N N^{-1}\log b_N\leq j(\eta).
\]

Conversely (4),(5), and \(M/N\to1/2\) give

\[
 \liminf_N N^{-1}\log b_N\geq j(\eta)-\eta/2.
\]

Let \(\eta\downarrow0\) AFTER these limsup/liminf inequalities.
No estimate uniform in a shrinking ellipse is required. We obtain

\[
 \boxed{\displaystyle
       \lim_{N\to\infty}\frac1N\log
          \max_{c\ \mathrm{distinct}}|z_N(c)|=\frac{v_8}{\pi}.}
                                                               \tag{7}
\]

This does not assert that the maximizing node is always \(-2\),
or that \(z_N(-2)\) has a nonzero limiting prefactor. In particular
it does not require a special odd-level simple-node argument.

### A reusable bandlimited cyclotomic source criterion

The same proof applies to ANY sequence of actual two-port source
polynomials \(f_N\) of degree at most \(\lfloor(N-1)/2\rfloor\).
Suppose that for each fixed \(0<\eta<\eta_0\) an actual finite-source
estimate proves

\[
 \liminf_N N^{-1}\log|f_N(-2\cosh\eta)|\geq j(\eta),
 \qquad
 \limsup_N N^{-1}\log\max_{|w|=e^\eta}|f_N(w+w^{-1})|
                                      \leq j(\eta),
                                                               \tag{7a}
\]

where \(j(\eta)\to j(0)\in\mathbb R\) as \(\eta\downarrow0\).
Then the exact DCT and the maximum principle give

\[
 \lim_N N^{-1}\log\max_c|f_N(c)|=j(0),\qquad
 \lim_N N^{-1}\log\phi(L_N f_N^\sharp f_N)=2j(0).
                                                               \tag{7b}
\]

For the second assertion use (2), with
\(N\max_c|f_N(c)|^2\leq\phi(L_N f_N^\sharp f_N)
\leq N^2\max_c|f_N(c)|^2\).
Thus (7a) is a concrete sufficient source/Fourier criterion for
this complete-belt energy. It requires an actual selected-source
lower estimate, not only a classical algebraic curve or a formal
principal symbol. The verified packet \(z_N\) supplies (7a) by
its finite-source central Gaussian, with no new assumption.

The degree/nonaliasing hypothesis is essential. There are only
\(M+1\) distinct physical nodes. Their product polynomial
\(G_N(z)=\prod_c(z-c)\), of degree \(M+1\), is nonzero in
the FULL Casimir algebra but vanishes at every physical node.
Consequently its retained-belt energy is zero. At even
\(N=2L\), explicitly \(G_N(z)=2T_L(z/2)\), so it has the
nonzero radial exponential rate \(\eta/2\) while its sampled
maximum vanishes identically. Its normal directions have not
vanished in the full algebra; it is the exact complete-belt
functional that pairs them to zero. Neither an arbitrary
degree-near-\(N\) packet nor a saturated classical curve can
be substituted into this bandlimited theorem.

## 4. Exact positive energies for arbitrary fixed reflected powers

For any FIXED integer \(k\geq1\), define the literal complete-belt
source

\[
 \mathcal B_{k,N}
    =\phi\!\left(L_N(z_N^\sharp z_N)^k\right)
    =N\sum_cm_c|z_N(c)|^{2k}>0.                         \tag{8}
\]

Strict positivity at every \(N\) follows already from the exact
nonzero degree-\(M\) polynomial: it cannot vanish at all \(M+1\)
distinct physical nodes. No asymptotic lower estimate is needed
for this finite-level assertion.

All the ports before the final closure remain those of the original
two-strand tangle. Equation (8) consists of \(2k\) actual turned
circle boxes in series, with ONE retained auxiliary complete circle
around their two physical strands, and the original marked closure.
It is not a metric defined from its final scalar. At every fixed \(N\)

\[
 N b_N^{2k}\leq\mathcal B_{k,N}\leq N^2 b_N^{2k}.
\]

Consequently

\[
 \boxed{\displaystyle
  \lim_N N^{-1}\log\mathcal B_{k,N}=2k\frac{v_8}{\pi},
  \qquad
  \lim_N\frac{2\pi}{N}\log\mathcal B_{k,N}=4k v_8.}
                                                               \tag{9}
\]

More generally let \(F_N=R^{e_N}z_N^a(z_N^\sharp)^b\), where
\(a,b\geq0\) are fixed, \(a+b>0\), and \(e_N\) is ANY integer.
The physical nodal values of \(R\) have modulus one, including
even/composite levels. Therefore, EXACTLY,

\[
 \phi(L_NF_N^\sharp F_N)
     =N\sum_cm_c|z_N(c)|^{2(a+b)},
                                                               \tag{10}
\]

and its exponent is \(2(a+b)j_0\), independently of the twist.
This is a source-preserving statement at this particular retained
complete-belt seam. It is not a claim that arbitrary filled exterior
volumes ignore twists: the complete belt cusp is still present.
For the cut box

\[
 f_N=z_N^\sharp R^{-1}
\]

of the verified two-octahedron base, \(f_N^\sharp f_N=z_N^\sharp z_N\)
in the FULL actual algebra, so (8) is also its genuine reflected
complete-belt sewing. Its quantum cut differs from the Newton
reflection cut used to prove that original base's rate.

The one-cut reduced normalization and its recorded component/frame
characters are those of the [complete-point comparison](actual_complete_augmented_source_normalization.md).
They have modulus one, or the stated single \(N^{-1}\) in the
one-cut modified convention. They do not alter (9). No extra
modified dimension is assigned to each auxiliary circle.

## 5. The remaining geometric gluing condition

The [two-octahedron cut certificate](actual_reflected_two_circle_octahedral_base.md)
supplies a concrete base and its actual twice-punctured crossing
disks. The [literal stack and outer-collar theorem](actual_balanced_octahedral_belt_stack_volume.md)
now matches (8) with these actual geodesic pants gluings and proves
its balanced complete-link volume equality. It also gives the metric
for arbitrary fixed sign words and fixed integer outer collars; the
nonzero asymptotic in that broader case uses the separate
[coherent source Gaussian](actual_coherent_octahedral_belt_stack_asymptotic.md),
not the positive-energy argument alone. General tangle or branched
graph sewings do not inherit this particular collar certificate.

In particular (8) must NOT be reinterpreted as a tree of scalar
Frobenius vertices. Such a tree inserts \(L_N^{|E|}\) and vanishes
at every even level when \(|E|\geq2\), as the exact earlier source
calculation shows. A branched physical vertex has six open legs and
its original saturated source kernel; (7) does not replace that
kernel or prove its geometric energy bound. A general graph/filling
volume conjecture remains open here.

Audit: [full physical belt sources and exact discrete sampling](../experiments/audit_actual_complete_circle_nodal_energy_and_belt_sewing.py).

The exact nodal sewing is restricted to the stated seam. It does not establish a geometric or arbitrary-six-port extension.