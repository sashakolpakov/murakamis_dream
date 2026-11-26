# The leading amplitude of the canonical cutoff at a fixed meridian

Private written proof, 18 November 2026.

The simple Alexander residue cancels the apparent singularity in the
partner branch's first transport equation. Together with the actual
quadratic reduction and the canonical node initialization, this upgrades
the fixed-meridian rate of [G] to a nonzero leading amplitude.
The source remains the difference of the two specified finite cutoffs.

This is a chosen growing-ray statement. It neither identifies the cutoff
with the original finite invariant nor identifies the operator branch
with the hyperbolic representation component. No local Borel
meromorphicity or exclusion of an essential singularity is asserted.

## 1. Actual source and conclusion

Use the logarithmic coordinate and source conventions of [G]:
\[
 u=\log(Y/\alpha),\qquad
 D_R(h,u)=U_{R,+}(h,\alpha(e^u-1))
                  -U_{R,-}(h,\alpha(e^u-1)).
 \tag{1}
\]
The original finite-shift operator is
\[
 \mathcal P_h=\sum_{\nu\in J}p_\nu(h,u)T^\nu,\qquad
 Tf(u)=f(u+h),
 \quad
 P(u,L)=\sum_\nu p_\nu(0,u)L^\nu,
 \quad
 P^{[1]}(u,L)=\sum_\nu\partial_h p_\nu(0,u)L^\nu.
 \tag{2}
\]
Its coefficients are holomorphic near the node, and its actual source
and gauge are those of [Q] and [C]. In particular
\[
 P(u,1)=0,\qquad P_L(0,1)=0,\qquad
 P_{uL}(0,1)P_{LL}(0,1)\ne0.
 \tag{3}
\]
Let \(\ell(u)\) be the other classical root through one and define
\[
 \kappa=\ell'(0)\ne0,\qquad
 \mathcal A(0)=0,\qquad \mathcal A'(u)=\log\ell(u),
 \qquad \log\ell(0)=0.
 \tag{4}
\]
Fix the same sheet normalization as [C] and [G], so
\[
 C_*=2r\sqrt{-\eta_*}\sqrt\pi\ne0.
 \tag{5}
\]

Define the two analytic functions
\[
 \begin{split}
 d_g(u)&=\ell(u)P_L(u,\ell(u)),\\
 e_g(u)&=P^{[1]}(u,\ell(u))
  +\frac{\mathcal A''(u)}2
       \{\ell(u)P_L(u,\ell(u))+\ell(u)^2P_{LL}(u,\ell(u))\}.
 \end{split}
 \tag{6}
\]
The ratio \(-e_g/d_g\) has a removable singularity at zero.
Consequently the normalization
\[
 a(0)=1,\qquad
 a'(u)=-\frac{e_g(u)}{d_g(u)}a(u)
 \tag{7}
\]
defines a holomorphic nowhere-zero amplitude on a small node disk.

Choose \(\theta\) with \(\Re(\kappa e^{i\theta})>0\), take a sufficiently
small fixed cutoff \(R=\varrho e^{i\theta}\), and set
\(h=e^{i\theta}\varepsilon\), \(\varepsilon>0\). Then there is
\(T_0>0\) such that for every fixed \(0<T\le T_0\), with
\(u_*=e^{i\theta}T\),
\[
 \boxed{\quad
 D_R(h,u_*)=
 C_*h^{-1/2}a(u_*)e^{\mathcal A(u_*)/h}\{1+o(1)\}.
 \quad}
 \tag{8}
\]
The square root of \(h\) is the one fixed on the facing sector of [C].
The limit holds for all sufficiently small positive \(\varepsilon\);
the fixed endpoint is reached exactly, not on a selected subsequence.

## 2. The residue removes the subprincipal pole

The actual unscaled formal source has leading coefficient
\[
 W_0(u)=\frac{r}{\alpha u}+O(1).
 \tag{9}
\]
Indeed [C, (2)] at \(\xi=0\) has \(w=z\), with
\(H(z,z,z)=r+O(z)\), and \(z=\alpha(e^u-1)\).
The supplied operator annihilates this same formal source.
Its order-\(h\) equation, using \(P(u,1)=0\), is exactly
\[
 P_L(u,1)W_0'(u)+P^{[1]}(u,1)W_0(u)=0.
 \tag{10}
\]
No coefficient of the first normal source remains in this equation,
because it is multiplied by \(P(u,1)\).

Put \(b=P_{uL}(0,1)\ne0\). Then
\(P_L(u,1)=bu+O(u^2)\), and (9)--(10) give
\[
                         P^{[1]}(0,1)=b.
 \tag{11}
\]
Factoring \(P\) by \(L-1\) and differentiating the other root gives
\[
 \kappa=-\frac{2b}{P_{LL}(0,1)},\qquad
 d_g(u)=-bu+O(u^2).
 \tag{12}
\]
At zero, the numerator in (6) is therefore
\[
 e_g(0)=b+\frac{\kappa}{2}P_{LL}(0,1)=0.
 \tag{13}
\]
Both functions in (6) are analytic and \(d_g\) has a simple zero.
Their quotient thus extends holomorphically, proving the assertion
preceding (7). Integrating its analytic logarithmic derivative proves
that \(a\) is holomorphic and nonzero.

For later use, the direct shift expansion for
\(f(h,u)=a(u)e^{\mathcal A(u)/h}\) is
\[
 \frac{\mathcal P_h f}{f}
 =P(u,\ell(u))
   +h\left\{d_g(u)\frac{a'(u)}{a(u)}+e_g(u)\right\}
   +O(h^2)=O(h^2).
 \tag{14}
\]
Every remainder here is uniform on a fixed smaller complex \(u\)-disk.
To see this directly, expand
\[
 \frac{f(u+\nu h)}{f(u)}
 =\ell(u)^\nu\left[
   1+h\left(\nu\frac{a'}a+
                    \frac{\nu^2}{2}\mathcal A''\right)+O(h^2)\right].
 \tag{15}
\]
The set of positive and negative integers \(\nu\) is fixed and finite.
All functions being differentiated are analytic on a larger fixed
disk. This is a calculation for the actual operator, including its
subprincipal coefficients and source gauge.

## 3. Retaining the first correction of the actual quadratic reduction

We need more than the \(O(h)\) coefficient estimate stated in [Q].
Its construction gives the following refinement on a fixed disk:
\[
 \mathcal S_h=\mathcal S_0+h\mathcal S_1+O(h^2),\qquad
 \mathcal S_0=T^2-(1+\ell)T+\ell,
 \tag{16}
\]
with \(\mathcal S_1\) of degree at most one in \(T\), analytic in \(u\).
The same construction still gives the actual source equation
\[
 \mathcal S_hD_R=r_h,\qquad
                 |r_h(u)|\le C_R e^{-\varrho/\varepsilon}.
 \tag{17}
\]
The estimate (16) is uniform in \(u\); it does not claim joint
holomorphy of the finite-truncation coefficients at \(h=0\).

Here is the refinement of the proof, with its buffers retained.
As in [Q], multiply the original operator by a fixed \(T^a\) to
make it polynomial, retaining the actual shifted coefficients:
\(\widehat{\mathcal P}_h=T^a\mathcal P_h\). Its classical factorization
is
\[
 \widehat P_0=Q_0S_0,\qquad
 S_0=(L-1)(L-\ell),\qquad Q_0(0,1)\ne0.
 \tag{18}
\]
The coefficient map \((q,s)\mapsto qS_0+Q_0s\) is invertible with
bounded analytic inverse on one fixed original chart, as proved in
[Q, Section 3]. The first residual has the analytic expansion
\[
 \widehat P_h-Q_0\# S_0=hR_1+O(h^2).
 \tag{19}
\]
Solve the first correction with that map. It has the expansion
\((q,s)=h(Q_1,S_1)+O(h^2)\), uniformly on fixed buffered disks.
Because this first correction is analytic in \(h,u\) before any
depth-dependent truncation, its \(u\)-derivative is \(O(h)\) on a
fixed smaller buffer. The residual after this correction is therefore
\(O(h^2)\), not merely the coarser \(O(h)\) bound that would follow
by immediately using a buffer of size \(O(|h|)\).

Now start the eroded-domain iteration of [Q] with this \(O(h^2)\)
residual. Reserve the fixed buffers just used, then take the remaining
depth proportional to the available radius divided by \(|h|\).
At each step [Q, (15)] contracts the residual by at least one half;
all later corrections sum to \(O(h^2)\). Thus the final factors obey
\[
 Q_h=Q_0+hQ_1+O(h^2),\qquad
 S_h=S_0+hS_1+O(h^2),
 \tag{20}
\]
and their exponentially small factorization residual is unchanged
in form. The source type is still \(C|R|\) on a disk of radius
comparable to \(\sqrt{|R|}\). The complementary-factor removal in
[Q, Section 4] therefore applies after decreasing the fixed cutoff
if necessary, and proves (17). In particular the refinement changes
no source, endpoint sheet or forcing.

The reference function in (14) also satisfies
\[
                         \mathcal S_h f/f=O(h^2).
 \tag{21}
\]
This does not follow by dividing a scalar estimate in (14).
Rather, compare the first transport coefficients in the formal
identity \(\widehat P_h=Q_h\# S_h+O(h^2)\).
The order-zero \(S_0(u,\ell)\) is zero. If \(G(u)\) is the
order-\(h\) transport coefficient of \(\mathcal S_h f/f\), that
of \(\widehat{\mathcal P}_h f/f\) is exactly
\(Q_0(u,\ell(u))G(u)\): shifting the already order-\(h\) output
introduces no other term at that order.
On the other hand left multiplication by \(T^a\) multiplies the
vanishing first transport in (14) by \(\ell^a\). Hence
\(Q_0(u,\ell)G=0\). Its coefficient is a unit on a smaller node
disk by (18), so \(G=0\). Taylor expansion using (20) proves the
uniform remainder (21).

## 4. Canonical initialization on an exact landing grid

Choose \(1/3<\beta'<\beta<1/2\). In particular \(3\beta'>2\beta\).
Use the exact grid of [G]:
\[
 m_\varepsilon=
 \left\lfloor\frac{T-\varepsilon^\beta}{\varepsilon}\right\rfloor,
 \quad t_0=T-m_\varepsilon\varepsilon,\quad
 u_n=e^{i\theta}(t_0+n\varepsilon).
 \tag{22}
\]
Then \(\varepsilon^\beta\le t_0<\varepsilon^\beta+\varepsilon\)
and \(u_{m_\varepsilon}=u_*\).
Define the reference
\[
 F(h,u)=C_*h^{-1/2}a(u)e^{\mathcal A(u)/h}.
 \tag{23}
\]
The actual complex overlap [C, (26)], on a disk of radius comparable
to \(t_0\), gives
\[
 D_R(h,u)=C_*h^{-1/2}e^{\mathcal A(u)/h}E_h(u),
 \qquad E_h(u)=1+O(\varepsilon^{3\beta'-1}).
 \tag{24}
\]
Indeed that disk lies in \(|z|\le\varepsilon^{\beta'}\) for small
\(\varepsilon\). Cauchy's estimate on nested such disks and \(a(0)=1\)
give
\[
 \frac{D_R(h,u_0)}{F(h,u_0)}=1+o(1),
 \qquad
 e_0:=
 \frac{D_R(h,u_0+h)}{D_R(h,u_0)}
       -\frac{F(h,u_0+h)}{F(h,u_0)}
 =O(\varepsilon)+O(\varepsilon^{3\beta'-\beta}).
 \tag{25}
\]
In particular \(e_0/t_0\to0\). These are two actual initialized
values, not a prescribed eigendirection.

## 5. Summable Riccati error and the original endpoint forcing

First solve the homogeneous equation for \(\mathcal S_h\) with those
two actual initial values, and call its scalar values \(D_n^0\).
Set
\[
 q_n^F=\frac{F(h,u_n+h)}{F(h,u_n)},\qquad
 q_n=\frac{D_{n+1}^0}{D_n^0},\qquad e_n=q_n-q_n^F.
 \tag{26}
\]
These ratios will be proved defined inductively. The reference ratio
is \(\ell(u_n)+O(\varepsilon)\), uniformly down to \(u_0\).
By (21) its Riccati defect is \(O(\varepsilon^2)\).
The exact difference recurrence is consequently
\[
 e_{n+1}=
   \frac{s_{0,h}(u_n)}{q_nq_n^F}\,e_n+O(\varepsilon^2).
 \tag{27}
\]

Along the chosen ray, \(|\ell(u_n)|\ge1+ct_n\), after shrinking
\(T_0\). Since \(s_{0,h}=\ell+O(\varepsilon)\), whenever
\(|e_n|=o(t_n)\) uniformly, the multiplier in (27) has modulus
at most \(1-c_1t_n\). Thus
\[
 |e_{n+1}|\le(1-c_1t_n)|e_n|+C\varepsilon^2.
 \tag{28}
\]
This condition closes a bootstrap. Replace \(t_n\) on the right
by \(t_0\); the resulting bound is
\[
 |e_n|\le |e_0|+\frac{C\varepsilon^2}{c_1t_0}=o(t_0).
 \tag{29}
\]
Here \(e_0/t_0\to0\), and \(\varepsilon^2/t_0^2\to0\).
Choose the small bootstrap constant first, then \(\varepsilon\)
small; (29) keeps it strictly smaller. Since \(q_n^F\) stays
bounded away from zero, no \(q_n\) or \(D_n^0\) vanishes.

Summing (28), again using \(t_n\ge t_0\), gives
\[
 \sum_{n<m_\varepsilon}|e_n|
 \le \frac{|e_0|+C\varepsilon^2m_\varepsilon}{c_1t_0}
 =O(\varepsilon^{3\beta'-2\beta}
                         +\varepsilon^{1-\beta})=o(1).
 \tag{30}
\]
Therefore the exact product of \(q_n/q_n^F=1+e_n/q_n^F\) tends
to one. With the first equality in (25), this proves
\[
                         D_{m_\varepsilon}^0/F(h,u_*)\to1.
 \tag{31}
\]

It remains to retain the actual additive forcing in (17).
The comparison in [G, Section 5] applies to this refined operator:
it uses only its \(O(h)\) classical coefficient estimate, the same
actual initialization, the gap on this grid, and (17).
Its unrestricted propagator bound controls every forcing vector;
the homogeneous cone has a polynomial relative lower bound.
The initialized growing coefficient has modulus at least one for
small \(\varepsilon\). Consequently its equations (34)--(36) give
\[
 \frac{D_R(h,u_*)-D_{m_\varepsilon}^0}
                         {D_{m_\varepsilon}^0}
       =O(\varepsilon^{-M}e^{-\varrho/\varepsilon})=o(1)
 \tag{32}
\]
for some fixed \(M\). All hypotheses of that argument persist
under (20); no omitted complementary-mode assumption is added.
Equations (31)--(32) prove (8).

## 6. Scope and complete sources

The amplitude \(a\) is fixed by the actual subprincipal operator and
the actual simple-pole normalization. In particular (8) is stronger
than a logarithmic rate or invertibility estimate. It supplies a
nonzero leading coefficient at every sufficiently small fixed target
on the specified growing ray, for the actual finite-cutoff jump.

It does not identify a local fractional Borel module, rule out an
essential odd Laurent tail on the moving divisor, construct an
infinite Laplace sum, or transfer this coefficient to the physical
root-of-unity invariant. The operator branch has not been identified
with the hyperbolic component. The broad arbitrary-short-filling
problem, including cases without an Alexander-pole seed, is unchanged.

The proof uses these complete texts, read in full with the used
implications checked:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_canonical_cutoff_node_regularization_and_profile.md | 8c28a3d3a7b11085c8e2b5966221501b632ea99600aae4db57e8bdf8cd4a9631 |
| Q | notes/research_canonical_cutoff_quadratic_ore_reduction.md | 90db0237f4536495e7150109eae374ebbb12e2f7515b7c577322d07d2b9daae7 |
| G | notes/research_canonical_cutoff_fixed_meridian_growth.md | d05aa1300c5e255ae1291f91fd331e2c78670f64d4d48ee0dedb323692440388 |

Only written mathematics and source-text reads were used. No
mathematical programs, tests or builds were run. Frozen sources
and public manuscripts are unchanged.
