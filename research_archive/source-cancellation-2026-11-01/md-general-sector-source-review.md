# Why endpoint concentration does not localize the original filling functional

1 November 2026. Private proof and source-interface review. The release
`f2076a1b` is unchanged.

The positive endpoint theorem and its small-polydisk extension are genuine
source estimates on their stated original certified flat-plat class. They
do not, by themselves, localize the finite filling functional to that
polydisk. This note proves that limitation inside the exact degree and
node-vanishing space of a one-sided source. The obstruction persists for
every fixed odd signed twist power, however large that power is.
It invalidates an inference from the spectral-polydisk estimate, degree,
divisor, and Hermite functional alone. It does not by itself invalidate a
theorem using a small positive Fejér reference mass before the shared
coefficient is taken.

This is not a counterexample to a closed knot source or its volume limit.
The test polynomial below is a bounded linear combination of actual local
one-sided diagonal coefficients. It has not been realized as the one
shared coefficient of a fixed closed diagram. Thus a useful theorem for
the actual shared source must exploit a restriction beyond the local
degree, divisor, endpoint estimate, and finite functional norm.

## 1. The source statements that can and cannot be combined

The exact homogeneous source and its central/left/right partition retain
the original four-face order, ordinary degree targets \(d=N-1\), and two
protected zero targets. The whole complementary polynomial is

\[
 \mathcal D_N=S_{N,\mathrm{full}}-S_{N,\mathrm C}.
 \tag{1}
\]

It has degree at most \(d\) in each spectral variable and vanishes on the
product of all spectral node sets. This is value vanishing; repeated-node
derivatives generally survive. Applying the exact functional in each
variable inserts the actual signed powers. The finite supremum theorem
controls this operation on the whole real spectral cube. It does not
replace that cube by a neighborhood of the negative endpoint.

For the original certified flat plats in
`actual_fejer_unique_geometric_maximizer.md`, the positive endpoint entropy
has a unique geometric maximizer, separated from every one-sided support.
`actual_fejer_spectral_polydisk_complement.md` then proves a strict bound
for (1) when every spectral variable lies sufficiently close to \(-2\),
including all fixed endpoint derivatives. Both notes explicitly retain
the remaining filling-cycle problem. Neither statement alone supplies a
bound on all the other spectral nodes used by the exact functional.

The general sector-cover method instead bounds the whole real spectral
cube before applying the functional. Its sufficient hypothesis is a
strict shared-radius certificate for every relevant genuine noncentral
string. The 54-region example in
`actual_singleton_sector_envelope_obstruction.md` disproves the universal
existence of this certificate for arbitrary simple matched-sphere Morse
sources: one genuine singleton sector, nonzero at all sufficiently large
even levels, has envelope capacity greater than the complete action by
\(1/5\). That example does not contradict the earlier flat-plat endpoint
theorem. It also does not furnish a signed-source or filled-invariant
lower bound.

Appendix Q is a closure theorem for sources already possessing an
unabridged cover. Its insistence on including locally allowed strings
whose old whole coefficients happen to vanish is essential: gluing can
change that global support. It does not assert that every source has a
cover. There is consequently no logical route from Q alone to a universal
noncentral gap.

## 2. The exact one-variable functional

Set \(N\ge2\), \(d=N-1\), \(m=\lfloor N/2\rfloor\), and

\[
 \chi_N(z)=2T_N(z/2)+2,\qquad
 c_a=2\cos\phi_a,\qquad
 \phi_a=\frac{(2a+1)\pi}{N},\quad 0\le a<m.
 \tag{2}
\]

The \(c_a\) are distinct double roots. When \(N\) is odd, \(-2\) is the
additional simple root. Write

\[
 B_N(z)=\prod_{a=0}^{m-1}(z-c_a),\qquad
 Z_N(z)=\begin{cases}B_N(z),&N=2m,\\
                         (z+2)B_N(z),&N=2m+1.
          \end{cases}
 \qquad \chi_N=Z_NB_N.
 \tag{3}
\]

Every left or right source entry is divisible by \(Z_N\). In particular
the exact one-sided scalar space is contained in, and its diagonal
entries span, \(Z_N\mathbb C[z]_{\le m-1}\). No repeated-root normal has
been removed by taking this space.

For a polynomial \(H\) vanishing at all nodes, the original full-Hermite
functional reduces to

\[
 \mathcal L_N^nH=
 \frac1{N^2}\sum_{a=0}^{m-1}
        (4-c_a^2)f_n(c_a)H'(c_a),
 \tag{4}
\]

where the omitted simple-root value is zero and the crossing multiplier
retains its original lift:

\[
 f_n(2\cos\phi)=
 q^{nd^2/4}\exp\!\left(\frac{inN(\phi-\pi)^2}{4\pi}\right),
 \qquad q=e^{\pi i/N}.
 \tag{5}
\]

These are the formulas in `actual_uniform_filling_supremum_bound.md`,
equations (10), (13), and (22). The derivative of \(f_n\) disappears in
(4) because the numerator value is zero, not because the crossing phase
has been replaced by its absolute value. All values \(f_n(c_a)\) have
modulus one, at both parities and at composite levels.

## 3. A polynomial in the actual one-sided divisor space

Define

\[
 H_N(z)=Z_N(z)\left(\frac{z+2}{4}\right)^{m-1}.
 \tag{6}
\]

Its degree is exactly \(d\). It vanishes at every spectral node. At the
endpoint \(-2\), its vanishing order is \(m-1\) for even levels and \(m\)
for odd levels. Hence every fixed finite list of endpoint derivatives is
identically zero for all sufficiently large \(N\).

The elementary Chebyshev identities are

\[
 \begin{aligned}
 B_{2m}(2\cos\phi)&=2\cos(m\phi),\\
 B_{2m+1}(2\cos\phi)
   &=\frac{\cos((m+\tfrac12)\phi)}{\cos(\phi/2)}
     =U_m(\cos\phi)-U_{m-1}(\cos\phi),\\
 Z_{2m+1}(2\cos\phi)
   &=4\cos(\phi/2)\cos((m+\tfrac12)\phi).
 \end{aligned}
 \tag{7}
\]

The quotient in the second line is its polynomial continuation at
\(\phi=\pi\). Consequently

\[
                 \|H_N\|_{[-2,2]}\le4.
 \tag{8}
\]

There is also a fixed complex neighborhood on which this bounded
polynomial is exponentially small. For \(0<r\le1\), put

\[
 \rho_r=\frac{2+r+\sqrt{r(4+r)}}2,
 \qquad \theta_r=\log\rho_r.
 \tag{9}
\]

If \(|z+2|\le r\), choose \(w\) with \(z=w+w^{-1}\) and \(|w|\ge1\).
The identity

\[
 \lvert z-2\rvert+\lvert z+2\rvert
   =2(\lvert w\rvert+\lvert w\rvert^{-1})\le4+2r.
 \tag{10}
\]

implies \(|w|\le\rho_r\). Using \(B_{2m}=w^m+w^{-m}\), and using the
\(m+1\) and \(m\) terms in the two polynomials \(U_m,U_{m-1}\) for odd
levels, gives

\[
 \sup_{|z+2|\le r}|H_N(z)|
 \le \max(2,Nr)\rho_r^m(r/4)^{m-1}.
 \tag{11}
\]

For example, at \(r=1\), \(\rho_1=(3+\sqrt5)/2<4\). Therefore the
right side is \(\exp(-\gamma N+O(\log N))\), where

\[
 \gamma=\frac12\log\frac{8}{3+\sqrt5}>0.
 \tag{12}
\]

The same upper bound holds on every smaller fixed polydisk after taking
products of these one-variable polynomials.

## 4. This is a bounded combination of literal source coefficients

The original homogeneous face formula gives, for \(0\le a<m\),

\[
 [x^0b^ac^{d-a}y^0]H_{V,\mathrm L}(x,b,c,y;z)
             =\frac{\chi_N(z)}{z-c_a}.
 \tag{13}
\]

Indeed the associated path has identical initial and final row \(a\);
it uses no lowering step and leaves every other diagonal row unused.
Thus (13) includes the full unused-row product and the same scalar
normalization as the original resolvent numerator. It is not a spectral
interpolant substituted for that numerator.

Partial fractions, or Lagrange interpolation of a polynomial of degree
\(m-1\), now give the exact identity

\[
 H_N(z)=\sum_{a=0}^{m-1}\alpha_{N,a}
                   \frac{\chi_N(z)}{z-c_a},\qquad
 \alpha_{N,a}=\frac{((c_a+2)/4)^{m-1}}{B_N'(c_a)}.
 \tag{14}
\]

The derivatives in (7) yield

\[
 \alpha_{N,a}=
 \begin{cases}
 \displaystyle\frac2N(-1)^a\sin\phi_a
                         \cos^{N-2}(\phi_a/2),&N\text{ even},\\[3pt]
 \displaystyle\frac4N(-1)^a\sin\phi_a
                         \cos^{N-2}(\phi_a/2),&N\text{ odd}.
 \end{cases}
 \tag{15}
\]

In particular \(\sum_a|\alpha_{N,a}|\le2\). The coefficients are level
dependent and alternate in sign; they are not asserted to be produced
by one fixed exterior diagram. Their bounded total mass shows that the
obstruction does not arise from exponentially large external scalar
weights.

The exact resolvent/Hermite identity sends each polynomial in (13) to
\(f_n(c_a)\). Equivalently, (4) and the Chebyshev double-root normalization
give

\[
               \mathcal L_N^nH_N=\sum_a\alpha_{N,a}f_n(c_a).
 \tag{16}
\]

This is where the retained normal matters. Replacing the numerator by
its zero values would incorrectly make (16) zero.

## 5. Every fixed odd twist power detects it at polynomial size

Let \(n\in2\mathbb Z+1\) be fixed, positive or negative. Define a unit
phase and a parity factor by

\[
 \xi_{N,n}=q^{nd^2/4}
       \exp\!\left(\frac{inN\pi}{4}-\frac{in\pi}{2}\right),
 \qquad \kappa_N=\begin{cases}2,&N\text{ even},\\4,&N\text{ odd}.
                         \end{cases}
 \tag{17}
\]

At the actual midpoint grid, the linear phase in (5) obeys
\(e^{-inN\phi_a/2}=(-1)^ae^{-in\pi/2}\). It therefore cancels the
alternating sign in (15), exactly, before any estimate. Equations
(15)–(16) become

\[
 \mathcal L_N^nH_N=
 \xi_{N,n}\frac{\kappa_N}{N}
 \sum_{a=0}^{m-1}\sin\phi_a\,
     \cos^{N-2}(\phi_a/2)
       \exp\!\left(\frac{inN\phi_a^2}{4\pi}\right).
 \tag{18}
\]

The sum has the nonzero limit

\[
 \sum_{a=0}^{m-1}\sin\phi_a\,
     \cos^{N-2}(\phi_a/2)e^{inN\phi_a^2/(4\pi)}
       \longrightarrow \frac{2}{\pi-2in}.
 \tag{19}
\]

Here is a direct justification. Put \(t_a=\sqrt N\phi_a\); their spacing
is \(2\pi/\sqrt N\), with the first point at half that spacing. On every
bounded \(t\)-interval,

\[
 \sqrt N\sin(t/\sqrt N)
 \cos^{N-2}(t/(2\sqrt N))
 e^{int^2/(4\pi)}
 \longrightarrow t\exp[-(1/8-in/(4\pi))t^2]
 \tag{20}
\]

uniformly. For \(N\ge4\), \(0\le t<\pi\sqrt N\), the absolute value
of the left side is at most \(t e^{-t^2/16}\): use
\(\sin x\le x\), \(\log\cos(x/2)\le-x^2/8\), and
\(N-2\ge N/2\). Its lattice tails are uniformly summable, as follows
by comparing the eventually decreasing Gaussian bound with its integral.
Midpoint Riemann sums therefore converge to

\[
 \frac1{2\pi}\int_0^\infty
      t\exp[-(1/8-in/(4\pi))t^2]\,dt
          =\frac{2}{\pi-2in}.
 \tag{21}
\]

This proves (19) without an exchange of an infinite Fourier charge sum.
It follows that, separately at either parity,

\[
 \mathcal L_N^nH_N
   =\frac{\xi_{N,n}}N
       \left(\frac{2\kappa_N}{\pi-2in}+o(1)\right),
 \qquad
 \lim_{N\to\infty}\frac1N\log|\mathcal L_N^nH_N|=0.
 \tag{22}
\]

The contribution in (19) comes from \(\phi=O(N^{-1/2})\), hence from
\(z=2-O(N^{-1})\), at the opposite end of the spectrum from the controlled
polydisk. For any fixed closed neighborhood of \(-2\) separated from \(2\), its
restricted derivative-node sum in (18) is exponentially small: on that
part of the grid \(\cos(\phi/2)\) is bounded strictly below one. The odd
simple-node value is zero throughout.

## 6. Exact obstruction and the remaining source question

There cannot be a bound

\[
 |\mathcal L_N^nH|
       \le e^{o(N)}\sup_{|z+2|\le1}|H(z)|
 \tag{23}
\]

valid for every \(H\in Z_N\mathbb C[z]_{\le m-1}\), even with the added
assumptions \(\|H\|_{[-2,2]}\le4\) and vanishing of every fixed number of
endpoint derivatives. The polynomials (6), with (11) and (22), disprove
it for every fixed odd signed \(n\). The same conclusion holds for any
smaller fixed endpoint disk.

Thus the finite filling norm, the true one-sided divisor, repeated-node
normal recovery, and endpoint concentration do not automatically justify
discarding the rest of the spectral grid. Increasing a fixed twist power
does not fix this general functional issue. The actual midpoint phases
can reinforce an alternating one-sided combination at the opposite
endpoint.

There is an additional distinction between spectral locality and the
stronger positive endpoint comparison. The smallness of (6) on the
endpoint disk results from cancellation in (14). It does not imply a
small sum of the corresponding positive Fejér coefficients. Therefore
this example alone does not disprove a source-specific argument using
that positive reference before taking the shared coefficient.

A universal coefficientwise comparison with that reference nevertheless
fails, by a different exact example already present in the
[Fejér entropy sign calculation](actual_fejer_entropy_signs_and_tail_insertion.md).
At \(N=2m\), let \(0\le j\le m-1\), and let \(v_{N,j}(z)\) be the literal
left coefficient of \(x^jc^{d-j}\). Put

\[
 s_r=2\sin(\pi r/N),\qquad
 a_r=4\cos^2(\pi(r+\tfrac12)/N).
 \tag{24}
\]

The single all-\(x\) path and its unused rows give its positive reference
coefficient exactly:

\[
 p_{N,j}=|v_{N,j}(-2)|
       =\frac4{a_0}\prod_{r=1}^j\frac{s_r^2}{a_r}.
 \tag{25}
\]

For the original \(R\) or \(R^{-1}\), equation (10) of the
[homogeneous source formula](actual_homogeneous_casimir_face_source.md)
instead gives

\[
 |\mathcal L_N^{\pm1}v_{N,j}|
       =\frac{N}{S_jS_{d-j}}=1,
 \qquad S_k=\prod_{r=1}^k2\sin(\pi r/N).
 \tag{26}
\]

Here \(S_jS_{d-j}=S_d=N\), and the omitted original lift is a unit
phase. Since this face monomial is strictly one-sided, no central or
right contribution can change (26). If \(j/N\to u\in(0,1/2)\), (25) has
rate \(2\int_0^u\log\tan(\pi t)\,dt<0\). Thus no subexponential
coefficientwise filling cost relative to the positive endpoint reference
holds for all powers. The two powers in (26) are not independently long;
this observation does not decide a statement that uses long powers
together with additional closed-source constraints.

The missing step for an actual closed source remains more specific:
prove a bound for its shared complementary polynomial on the rest of the
grid, or prove cancellation of its exact weighted normal sum with all
original face targets still imposed. The bounded combinations (14) have
not been shown to arise from those targets. They therefore rule out a
generic locality inference, but do not rule out a source-specific
coherent estimate. No claim about hyperbolic volume follows from this
counterexample in either direction.

## 7. Checks and dependencies

The accompanying private script
`md-general-sector-functional-locality-check.py` checks the polynomial
factorization, actual diagonal expansion, full derivative functional and
odd-power phase cancellation exactly at selected small levels. It also
records a short high-precision check of the nonzero constant in (19).
These finite computations do not prove the uniform norm or asymptotic;
their proofs are (7)–(22). Equations (24)–(26) are a comparison with
existing exact source results, not a new numerical experiment.

The only quantum inputs are the written homogeneous source definition,
the one-sided path partition, and the complete Hermite functional with
its original Gaussian lift. The new local polynomial argument is
elementary and uses no geometric or source-capacity assumption. A source
hash manifest records the specific public files read. No public source,
manuscript, or experiment file was changed.
