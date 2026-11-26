# Actual Casimir pair localization of the reduced closing source

Private written proof, 18 November 2026.

The reciprocal Cartan pairs in the reduced first-jet formula
have actual analytic central projectors on the original tensor
module. Each pair cancels its own source residue. For a braid
word the literal color turnover also reflects the two reduced
block traces, including their meridian derivatives.

These are finite source identities. The projectors retain
the generalized Casimir eigenspaces at the root. They neither
select a geometric state inside a multiplicity space nor
prevent cancellation between different pairs. The complete
directs are H, R and Y, pinned below.

## 1. The exact reduced blocks and the total Casimir

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
Use \(m\ge2\) actual heads with common meridian \(M\)
near one, at this fixed \(q\). Write \(r=m-1\),
\(x=-M/q\), \(x_0=-q^{-1}\), and
\[
 K_{\rm r}(M)=M^rK_0,\qquad
 \varepsilon=(-1)^{(N+1)r},\qquad K_0^N=\varepsilon I.
 \tag{1}
\]
Let \(\mathcal X\) be the \(N\) distinct eigenvalues of
\(K_0\), with their constant occupation-space projectors
\(P_\chi\) and spaces \(U_\chi\). Inversion preserves
\(\mathcal X\). For an analytic family \(W(M)\) of total
intertwiners, R gives the actual algebra map
\[
 B(W)=p_0S_m^{-1}W i_0,\qquad
 S_m^{-1}WS_m=\sum_{n=0}^{d}F_1^n\otimes B_n(W),
 \qquad [B(W),K_{\rm r}]=0.
 \tag{2}
\]
Set
\[
 t_\chi^W(M)=\operatorname{Tr}_{U_\chi}B(W(M)).
 \tag{3}
\]
The derivative of (3) always includes the dependence of
the actual \(S_m(M)\). No cut or coupon is reset.

Use the scaled lowering operator \(E\) in H. Thus
\[
 [E,F]=(q-q^{-1})(K-K^{-1}),\qquad
 \Omega=FE+qK+q^{-1}K^{-1}.
 \tag{4}
\]
The ordered total Casimir has the exact expression
\[
 \boxed{\quad
 S_m^{-1}\Omega_\Sigma S_m
       =F_1E_{\rm r}-(MK_{\rm r}+M^{-1}K_{\rm r}^{-1}).
 \quad}
 \tag{5}
\]
For completeness, H gives
\(S_m^{-1}E_\Sigma S_m=E_{\rm r}+L_1b_A\), where
\(b_a=MK_{\rm r}Q^{-a}-M^{-1}K_{\rm r}^{-1}\).
The diagonal part of \(F_1L_1b_A\) on first occupation
\(a\) is \((1-Q^a)b_a\). Adding
\(q xQ^{-a}K_{\rm r}+q^{-1}x^{-1}Q^aK_{\rm r}^{-1}\)
gives the negative diagonal term in (5), including
the vacuum row.

Consequently the spectrum of \(\Omega_\Sigma(M)\) is
contained in
\[
 \lambda_\chi(M)=-M^m\chi-M^{-m}\chi^{-1},
                          \qquad \chi\in\mathcal X.
 \tag{6}
\]
Every value occurs: (5) is triangular in the first
occupation, with the displayed diagonal on every row.
For every polynomial \(p\), the algebra map in (2) gives
\[
 B(p(\Omega_\Sigma)W)
  =p(-MK_{\rm r}-M^{-1}K_{\rm r}^{-1})B(W).
 \tag{7}
\]
No remaining Casimir is specialized to a scalar.

## 2. Analytic paired projectors and their internal residue

At \(M=1\), equality
\(\lambda_\chi(1)=\lambda_\psi(1)\) is equivalent to
\(\psi=\chi\) or \(\psi=\chi^{-1}\).
Let \(\mathfrak o\) run over inversion orbits in
\(\mathcal X\). Around the corresponding distinct
number \(-\chi-\chi^{-1}\), choose disjoint small
positively oriented circles \(\Gamma_{\mathfrak o}\).
For \(M\) sufficiently close to one define
\[
 \mathcal Q_{\mathfrak o}(M)
   =\frac1{2\pi i}\int_{\Gamma_{\mathfrak o}}
                         (zI-\Omega_\Sigma(M))^{-1}\,dz.
 \tag{8}
\]
All contours and neighborhoods here may depend on \(N,m\).
The finite resolvent is holomorphic in \(M\) along them.
Its elementary spectral integral is an idempotent,
the projectors are disjoint and sum to \(I\), and they
commute with all total generators and all total
intertwiners. For example these assertions follow by
integrating the resolvent identity; on a Jordan block
the integral is \(I\) or zero according to whether
its eigenvalue lies inside the contour.
Thus no root Jordan directions have been removed.

Triangularity in (5) applies also to the resolvent.
Its constant diagonal block is
\((z+MK_{\rm r}+M^{-1}K_{\rm r}^{-1})^{-1}\).
It follows exactly that
\[
 B(\mathcal Q_{\mathfrak o})=P_{\mathfrak o}
           :=\sum_{\chi\in\mathfrak o}P_\chi,\qquad
 B(\mathcal Q_{\mathfrak o}W)=P_{\mathfrak o}B(W).
 \tag{9}
\]
In particular \(\mathcal Q_{\mathfrak o}W\) is an
analytic actual intertwiner family, with its original
highest cut and tail pivot. These projectors localize
that source, not just an auxiliary scalar polynomial.

H's exact residue equation, applied to (9), gives
\[
 \sum_{\chi\in\mathfrak o}
            (\chi-\chi^{-1})t_\chi^W(1)=0.
 \tag{10}
\]
For a two-element orbit this says
\[
                         t_\chi^W(1)=t_{\chi^{-1}}^W(1).
 \tag{11}
\]
It holds for every analytic total intertwiner, without
a braid or reflection assumption. A singleton orbit
\(\chi=\pm1\) gives no additional constraint.

There is also a purely polynomial proof of (10).
Apply H's residue to \(p(\Omega_\Sigma)W\), using (7).
The result is
\[
 \sum_{\chi\in\mathcal X}
  (\chi-\chi^{-1})p(-\chi-\chi^{-1})t_\chi^W(1)=0
                         \quad\text{for every }p.
 \tag{12}
\]
Interpolation on the distinct numbers indexed by
\(\mathfrak o\) isolates one orbit. Formula (8) adds
the actual holomorphic projector through the collision,
which polynomial interpolation only at \(M=1\) would
not by itself specify.

## 3. Literal turnover of the reduced braid traces

For this section \(W=W_\beta\) is the actual unmarked
same-color braid word, with its common crossing scalars.
On one balanced head put
\[
 C(M)w_a=c_a(M)w_{d-a},\qquad
 c_a(M)=\prod_{j=1}^a\frac{MQ^j-M^{-1}}{1-Q^j},
 \qquad c_0=1.
 \tag{13}
\]
The map goes from the head at \(M^{-1}\) to the head
at \(M\) with its Chevalley action. It is holomorphic
and invertible near one: \(c_a(1)=(-1)^a\).
Directly from the literal arrows,
\[
 \begin{split}
 C(M)E(M^{-1})&=F(M)C(M),\\
 C(M)F(M^{-1})&=E(M)C(M),\\
 C(M)K(M^{-1})&=K(M)^{-1}C(M).
 \end{split}
 \tag{14}
\]
For instance the consecutive ratio in (13) is
\((MQ^a-M^{-1})/(1-Q^a)\); substitution verifies
both nonzero arrows. The forced extreme arrows also
match. With the branch
\(\alpha=d+\log M/\log q\), the weight operator is
sent to its negative, since the reflected color has
\(\alpha'=2d-\alpha\).

The Chevalley map \(E\leftrightarrow F\),
\(K\leftrightarrow K^{-1}\) reverses the coproduct
order and fixes the Casimir (4). Let \(\mathsf J\)
reverse the \(m\) tensor factors, and put
\(\mathscr C(M)=C(M)^{\otimes m}\mathsf J\).
The actual universal crossing in Y has its Cartan
factor unchanged by changing both weight signs;
its nilpotent term \(E^n\otimes F^n\) becomes
\(F^n\otimes E^n\) with the same coefficient.
Tensor reversal restores the checked crossing.
This proves, for both signs,
\[
 \begin{split}
 \mathscr C(M)W_{\beta^{\rm rev}}(M^{-1})
                         \mathscr C(M)^{-1}&=W_\beta(M),\\
 \mathscr C(M)\Omega_\Sigma(M^{-1})
                         \mathscr C(M)^{-1}&=\Omega_\Sigma(M),
 \end{split}
 \tag{15}
\]
where \(\beta^{\rm rev}\) replaces each
\(\sigma_i^{\pm1}\) by \(\sigma_{m-i}^{\pm1}\),
without reversing the order of the word.
This is a finite matrix identity, not ordinary
symmetric-power covariance.

For explicit scalar bookkeeping, the full common
crossing factor is \(q^{\alpha^2/2}\). The full
Cartan operator is \(q^{H_1H_2/2}\), so (15)
retains that factor rather than stripping it.
The zero-framing twist
\[
             \theta(M)=q^{(\alpha^2-2d\alpha)/2}
 \tag{16}
\]
obeys \(\theta(M^{-1})=\theta(M)\).
The original modified-dimension line
\(\eta_N/D_N(M)\) is likewise reciprocal.
Thus their prescribed external products introduce
no missing multiplier in the stated unmarked
turnover. Any other external line remains explicit.

To extract reduced traces, first take generic \(M\)
where the values (6) are distinct, and let
\(\Pi_\chi(M)\) be the individual total-Casimir
spectral projector. From (5) and (2), every first
occupation diagonal block of
\(S_m^{-1}\Pi_\chi W S_m\) is \(P_\chi B(W)\).
Positive powers of \(F_1\) cannot return to that
diagonal. Therefore
\[
             \operatorname{Tr}_{\rm full}(\Pi_\chi W)
                            =N\,t_\chi^W(M).
 \tag{17}
\]
This auxiliary full trace computes a reduced block
trace; it does not replace the highest-cut pivotal
source by an ordinary trace.

Since \(\lambda_{\chi^{-1}}(M^{-1})=\lambda_\chi(M)\),
(15)--(17) imply
\[
 t_\chi^{W_\beta}(M)
                =t_{\chi^{-1}}^{W_{\beta^{\rm rev}}}(M^{-1}).
 \tag{18}
\]
The Artin half twist \(\Delta_m\) conjugates
\(\sigma_i\) to \(\sigma_{m-i}\). Its usual triangular
word verifies this using the braid relations.
Hence \(\beta^{\rm rev}=\Delta_m\beta\Delta_m^{-1}\).
R's algebra map sends this to conjugation by the
invertible \(B(W_{\Delta_m})\), which commutes with
each \(P_\chi\). The block traces are unchanged.
All \(t_\chi\) are holomorphic through one, so (18)
extends to the whole local germ and becomes
\[
 \boxed{\qquad
 t_\chi^{W_\beta}(M)=t_{\chi^{-1}}^{W_\beta}(M^{-1}).
 \qquad}
 \tag{19}
\]
In particular
\[
        t_\chi(1)=t_{\chi^{-1}}(1),\qquad
        t_\chi'(1)=-t_{\chi^{-1}}'(1).
 \tag{20}
\]
A singleton \(\chi=\pm1\) has \(t_\chi'(1)=0\).
No root-only formula was differentiated: (19) is
an equality of the actual fixed-\(q\) meridian germs.

## 4. The original closing row on one pair

Define the actual localized source by
\[
       \Phi_{\mathfrak o}(M)
                   =\Phi_0(\mathcal Q_{\mathfrak o}(M)W(M)).
 \tag{21}
\]
It sums exactly to the original source. H gives
on a punctured meridian disk
\[
 \Phi_{\mathfrak o}(M)
 =\frac{D_N(M)}
         {\varepsilon(M^{mN}-M^{-mN})}
   \sum_{\chi\in\mathfrak o}
       (M^m\chi-M^{-m}\chi^{-1})t_\chi(M).
 \tag{22}
\]
Its removable value is the corresponding portion of
H's first-jet row:
\[
 \Phi_{\mathfrak o}(1)
 =\frac1{2\varepsilon}\sum_{\chi\in\mathfrak o}
              (\chi+\chi^{-1})t_\chi(1)
  +\frac1{2\varepsilon m}\sum_{\chi\in\mathfrak o}
              (\chi-\chi^{-1})t_\chi'(1).
 \tag{23}
\]
For an actual braid and a two-element orbit, (20)
reduces this to
\[
 \boxed{\quad
 \Phi_{\{\chi,\chi^{-1}\}}(1)
   =\frac{\chi+\chi^{-1}}{\varepsilon}t_\chi(1)
     +\frac{\chi-\chi^{-1}}{\varepsilon m}t_\chi'(1).
 \quad}
 \tag{24}
\]
A singleton is counted only once and contributes
\(\chi t_\chi(1)/\varepsilon\).
The exact normal coefficient and the derivative of
the entire reduced word have both been retained.

There is a useful elementary insertion consequence.
If \(a(M)\) is a holomorphic scalar, then
\[
 \Phi_0(a\,\mathcal Q_{\mathfrak o}W)(1)
                       =a(1)\Phi_{\mathfrak o}(1).
 \tag{25}
\]
In the first-jet calculation the extra term would be
\(a'(1)\sum_{\chi\in\mathfrak o}
(\chi-\chi^{-1})t_\chi(1)/(2\varepsilon m)\);
it vanishes by the internal residue (10).
This does not say that an arbitrary short tangle
acts as a scalar on this multiplicity space.

## 5. Exact scope of the localization

The weights group total occupations modulo \(N\).
If \(k=\sum a_j\), then
\(\chi_k=x_0^rQ^{-k}\); complementing every occupation
gives \(\chi_{rd-k}=\chi_k^{-1}\).
Nevertheless (19) is a trace identity on the whole
\(U_\chi\), not an asserted equality separately for
each integer degree \(k\). Nor does the actual
turnover become simple occupation complementation
after the triangular reduction.

For inserted coupons, literal conjugation by
\(\mathscr C(M)\) still gives their exact turnover,
with its meridian dependence. To identify the
result with the same unmarked braid in (19), those
coupons would also need the corresponding covariance.
Nonintertwining marks retain their original Ward
defects and are not put into H's homogeneous
first-jet formula by definition.

The finite projectors in (8) need not be uniformly
bounded as \(N\) grows. They retain whole generalized
Casimir blocks, not a geometric line within them.
All actual \(\chi\)'s lie on the unit circle; these
identities alone do not continue a physical weight
to an off-circle loxodromic eigenvalue.
Even different internally regular pair contributions
can cancel in their final sum. For instance the
identity has \(t_\chi= \dim U_\chi\), derivative zero,
and its complete pivotal source is zero.
No positivity or nonzero geometric coefficient is
inferred from (24).

The result is an exact source-compatible finite
localizer and an actual sector turnover, with the
highest cut, pivotal line, root Jordan data and
first meridian normal preserved. Quantum normals
and ordinary-color closed jets still require their
whole original adapters.

## Complete proof-source pins

* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* Y: notes/actual_weyl_descent.md,
  SHA256 cf3add0dd88bcf413e04a595bfa52198b3d1a96c123ae6e356c994510f7093c4.

All three complete sources were freshly read nontruncated
in this active author sequence. Every used implication
was checked. Only written mathematics and text/hash
operations were used; frozen and public files were
not edited.
