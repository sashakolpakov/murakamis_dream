# Subexponential variation and the actual microscopic observation

Research deduction, 6 November 2026.

The microscopic observation needed for joint meridian growth is weaker
than convergence of a normalized profile. A subexponential ratio between
the total variation of an exact paired-factor source and its complete
value suffices. No concentration of the private indices is needed for
this upper bound. The canonical ordinary-color subtraction and division
remain valid through every fixed microscopic resonance.

A second elementary fact makes the size of the fixed microscopic disk
irrelevant at exponential rate. This permits a source estimate proved
on a small disk to feed the
[fixed-disk observation theorem](research_regularized_microscopic_disk_growth.md).
Neither fact establishes the required variation bound for arbitrary
composed knot sources. Existing actual tensor formulas give specific
obstructions to deriving it by entrywise absolute values.

## 1. Every fixed positive microscopic radius has the same upper rate

Let \(R_N(Y)\) be Laurent polynomials with fixed linear degree window
and exponential circle bound:
\[
 \operatorname{supp}R_N\subset[-AN,AN],\qquad
                       \|R_N\|_{|Y|=1}\le e^{GN}.
 \tag{1}
\]
Enlarge \(A,G\) if necessary to cover all sufficiently large levels.
Put
\[
 f_N(\zeta)=R_N(e^{\zeta/N}),\qquad
 \mathcal M_N(r)=\max\left(1,\sup_{|\zeta|\le r}|f_N(\zeta)|\right).
 \tag{2}
\]
These are whole functions of \(\zeta\), even when \(R_N\) has
negative Laurent powers.

**Lemma 1.** For every fixed \(0<r<R<\infty\), there is a constant
\(C_{r,R}\) such that
\[
 \mathcal M_N(r)\le\mathcal M_N(R)
       \le\mathcal M_N(r)\exp\!\left(C_{r,R}\frac N{\log N}\right)
 \tag{3}
\]
for all sufficiently large \(N\). Consequently
\[
 \limsup_N N^{-1}\log\mathcal M_N(r)
      =\limsup_N N^{-1}\log\mathcal M_N(R).
 \tag{4}
\]
The same equality holds for the two liminf rates. It is an equality
between disk norms, not a statement about the value at their center.

*Proof.* Fix any \(0<\delta<1\). Each Laurent coefficient of \(R_N\)
has modulus at most \(e^{GN}\), by its unit-circle Cauchy integral.
For \(|\zeta|\le\delta N\), negative and positive powers alike obey
\(|e^{j\zeta/N}|\le e^{AN\delta}\). Hence
\[
             \mathcal M_N(\delta N)
        \le (2AN+1)e^{N(G+A\delta)}\le e^{C_\delta N}.
 \tag{5}
\]
The outer disk lies in the fixed logarithmic meridian neighborhood
\(|\log Y|\le\delta\); it is not a disk extending to \(Y=0\).
More generally any actual local exponential bound on this
neighborhood supplies (5).

Hadamard's three-circle inequality says that
\(\log\sup_{|\zeta|\le t}|f_N(\zeta)|\) is convex in \(\log t\).
Taking its maximum with zero preserves convexity. For
\(\delta N>R\), interpolate between \(r\) and \(\delta N\):
\[
 \begin{split}
 \log\mathcal M_N(R)
  &\le \vartheta_N\log\mathcal M_N(r)
             +(1-\vartheta_N)\log\mathcal M_N(\delta N),\\
 1-\vartheta_N&=\frac{\log(R/r)}{\log(\delta N/r)}.
 \end{split}
 \tag{6}
\]
Since \(\log\mathcal M_N(r)\ge0\), (5)--(6) prove (3).
Its normalized logarithmic error tends to zero, proving both
rate assertions. If \(f_N\equiv0\), all the max-one norms are
one and the conclusion is immediate. \(\square\)

Thus the particular radius \(3+2\pi(d-1)\) in the fixed-disk
theorem can be replaced by any fixed positive radius in its
limsup conclusion, under the same recurrence hypotheses. The
classical end-coefficient condition is unchanged. This observation
does not compare a disk norm with \(R_N(1)\); a function can vanish
at its center.

## 2. Subexponential variation suffices for a disk upper bound

Retain the exact paired sine factors of
[the meridian-profile theorem](actual_paired_factor_meridian_profile.md),
Section 1:
\[
 P_{N,n}(\zeta)=\prod_{r=1}^{n}
 \left(1+\frac{\sinh^2(\zeta/(2N))}{\sin^2(\pi r/N)}\right),
       \qquad 0\le n<N.
 \tag{7}
\]
Suppose a specified finite source has the exact representation
\[
 F_N(e^{\zeta/N})
    =\sum_{\sigma\in\Sigma_N}w_{N,\sigma}
               \prod_{\ell=1}^{m}P_{N,n_\ell(\sigma)}(\zeta),
 \qquad
 K_N=F_N(1)=\sum_\sigma w_{N,\sigma},
 \tag{8}
\]
where \(m\) is fixed. Define its total variation in this
representation by
\[
                         V_N=\sum_\sigma|w_{N,\sigma}|.
 \tag{9}
\]
This hypothesis is an exact identity for the source being studied.
It is not asserted for an arbitrary Conway crossing-state expansion.

For each fixed \(T\), the original paired-factor estimate proves
\[
 \sup_{\substack{|\zeta|\le T\\0\le n<N}}
 |P_{N,n}(\zeta)|\le C_T.
 \tag{10}
\]
Indeed the absolute product is bounded by
\(\exp(C_T'\sum_{r=1}^{N-1}\min(r,N-r)^{-2})\).
Thus (8) immediately gives
\[
                \sup_{|\zeta|\le T}|F_N(e^{\zeta/N})|
                              \le C_T^m V_N.
 \tag{11}
\]
There is no interior-index or small-tail hypothesis in this
estimate. Such hypotheses are needed for the stronger normalized
profile convergence in Section 2 of the earlier note, not here.

The same implication holds for a finite complex measure on a
specified exact integration cycle, with \(V_N\) its total
variation, provided the holomorphic multipliers in (8) have (10)
on that cycle. It also holds with any other actual multipliers
having a uniform subexponential disk bound. An estimate for
individual insertions alone is not an estimate for \(V_N\).

## 3. Ordinary subtraction and every fixed resonant zero

Now assume \(F_N\) has the actual canonical ordinary-color
decomposition
\[
 F_N(Y)=S_N(Y)R_N(Y)+P_N^{\rm col}(Y),\qquad
 S_N(Y)=1+\cdots+Y^{N-1},\qquad \deg P_N^{\rm col}\le N-2,
 \tag{12}
\]
with \(R_N\) Laurent polynomial and
\[
 |[Y^j]P_N^{\rm col}|\le2D_N,\qquad
                          D_N\le\operatorname{poly}(N).
 \tag{13}
\]
These are the proved actual bounds in
[regularized periods](regularized_kashaev_period.md); their
normalization is unchanged.

**Proposition 2.** Under (8), (12)--(13), for every fixed radius
\(R>0\) and every fixed derivative order \(k\ge0\),
\[
 N\sup_{|\zeta|\le R}
       \left|\partial_\zeta^k R_N(e^{\zeta/N})\right|
                  \le C_{R,k}\bigl(V_N+N D_N\bigr).
 \tag{14}
\]
The estimate includes all resonances inside the disk.

*Proof.* Choose a larger fixed \(T>R+1\) such that the circle
\(|\zeta|=T\) avoids the zeros of
\[
 H(\zeta)=\frac{2\sinh(\zeta/2)}{\zeta},\qquad H(0)=1.
 \tag{15}
\]
The exact whole identity is
\[
 S_N(e^{\zeta/N})
     =N e^{(N-1)\zeta/(2N)}H_N(\zeta),\qquad
 H_N(\zeta)=\frac{\sinh(\zeta/2)}{N\sinh(\zeta/(2N))}.
 \tag{16}
\]
Its removable values are retained. On the chosen circle,
\(H_N\to H\) uniformly, so \(|S_N|\ge c_TN\).
Equation (13) also gives
\[
       |P_N^{\rm col}(e^{\zeta/N})|
                            \le 2ND_N e^T
                    \qquad(|\zeta|\le T).
 \tag{17}
\]
Divide the full numerator \(F_N-P_N^{\rm col}\) by \(S_N\)
on that circle, using (11) and (17). The result is bounded by
\(C_T(V_N+ND_N)/N\).
The composed quotient \(R_N(e^{\zeta/N})\) is entire because
(12) is an exact Laurent-polynomial identity. Its zeros of
divisibility at the resonances have already been supplied by
the ordinary-color interpolation; no term of (8) is divided
there separately. The maximum principle carries the bound
inside, and Cauchy's formula on smaller circles proves (14).
\(\square\)

In particular the hypothesis
\[
                         V_N\le e^{o(N)}(1+|K_N|)
 \tag{18}
\]
implies the actual microscopic observation bound
\[
 \sup_{|\zeta|\le R}|R_N(e^{\zeta/N})|
                         \le e^{o(N)}(1+|K_N|)
 \tag{19}
\]
on every fixed disk. If \(K_N\ne0\) eventually, the more
familiar assumption \(V_N/|K_N|=e^{o(N)}\) is sufficient
for (18). Formulation (18) does not assume eventual
nonvanishing or a positive complete-value rate.

With the classical end condition in the fixed-disk theorem,
(19) yields
\[
 \max(0,U_0)=
       \max\!\left(0,\limsup_N N^{-1}\log|K_N|\right).
 \tag{20}
\]
The converse inequality needed here uses
\(N R_N(1)=K_N-P_N^{\rm col}(1)\) and its polynomial
subtraction, exactly as in that theorem. This is a conditional
comparison of limsup rates, not a lower bound or a volume identity.
If a source proof supplies (19) only on one smaller fixed disk,
Lemma 1 supplies the disk required by the recurrence theorem
with subexponential loss.

## 4. The ratio is not preserved by entrywise composition

There are two distinct issues: maintaining the exact deformation
identity (8), and controlling the variation of its complete
weights. Existing actual tangle formulas obstruct simple local
solutions to both.

First, the main-meridian deformation changes some multiplication
quotients. It can revive whole tensor terms that are absent at
completeness. The exact
[same-index obstruction](actual_main_meridian_same_index_obstruction.md)
uses the original nine-incidence product trace
\[
 N=5a+1,\quad
 \mathcal Z_a(s)=\phi_s(e_{4a}e_a^8),\qquad
 \Delta_s=2\cos(2\pi s)-2.
 \tag{21}
\]
Here \(\phi_s\) is the full original quotient trace, including
the repeated-root normals. It proves
\[
 \mathcal Z_a(s)=\mathcal Z_a(0)+(-1)^a\Delta_s\mathcal B_a,
 \qquad
 \mathcal Z_a(0)>0,\qquad
 \frac{\mathcal B_a}{\mathcal Z_a(0)}
       \ge\frac1{3(5a+1)}
                  \left(\frac{25000}{6561}\right)^a.
 \tag{22}
\]
For every fixed \(s\) with \(\Delta_s\ne0\), this is an
exponential excess at a single complete-admissible actual
tensor entry, at both level parities. Thus a uniform
same-index bound by a subexponential multiple of the complete
entry cannot supply the bounded multipliers in (8).
It does not refute a whole-source comparison after regrouping.

Second, taking absolute values before a known coherent cap sum
already loses an exponential factor at actual reference points.
The [private-row cap theorem](research_mixed_cap_private_row_triangle_obstruction.md)
retains the literal type-four decomposition
\[
 U_{1,N}(-2,X)=\sum_{i=0}^{N-1}A_{i,N}(X),\qquad
 T_N(X)=\sum_{i=0}^{N-1}|A_{i,N}(X)|
 \tag{23}
\]
and proves, uniformly on its original compact actual endpoint
images,
\[
 \frac{T_N(X)}{|U_{1,N}(-2,X)|}
                  \ge cN^{-1/2}e^{N/12000}.
 \tag{24}
\]
The inner endpoint coefficient in each \(A_{i,N}\) is still
coherent; (24) is not caused by a further triangle estimate
inside it. All private rows and both parities remain present.
At a fixed outgoing reference \(X\), multiplying by any
nonzero adjacent factor independent of that private index
leaves the ratio unchanged. Therefore a composition rule that
requires every such local private-row expansion to have
subexponential variation relative to its coherent value is
false on the actual source.

Neither (22) nor (24) is a counterexample to (18) for the
complete closed knot in a suitably grouped representation.
The first concerns a tensor entry; the second concerns an
actual coherent boundary factor at fixed outgoing data.
They specify steps at which a proposed entrywise proof of
(18) would fail.

Even successful local bounds do not automatically control
the last summation. If a regrouping has coherent channel
values \(c_\tau=\sum_{\sigma\in\tau}w_\sigma\), then its
outer variation ratio is
\[
                 \frac{\sum_\tau|c_\tau|}
                      {|\sum_\tau c_\tau|}.
 \tag{25}
\]
Bounding the variation inside each channel leaves (25)
untouched. A fixed number of composition operations does
not remove this source-specific noncancellation requirement.

## 5. What the existing composition proof actually supplies

There is an existing noncircular way to bypass these local
failures in the already proved long-filling class.
[The general component comparison](actual_main_meridian_general_component_comparison.md),
Sections 3--7, keeps whole multiplication tensors, reflects
one-high differences, and fuses the full neighboring positive
comparisons before bounding their pressure. Its clean part
retains the original deformed boundary arrays and edge factors;
it is not simply the complete invariant at the same indices.
Its grouped errors have a strict exponential loss relative to
the specified source action.

The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md)
then retains the finite phase, and the joint filling analysis
proves its nonzero signed coefficient. As stated in the
component theorem, this is not a variation estimate for the
ungrouped crossing expansion. The resulting actual microscopic
profile is available in the
[filled meridian theorem](actual_main_meridian_filled_volume.md)
for fixed strict literal Conway constructions with all the
specified twists sufficiently long. Its fixed small meridian
disk is enough for Lemma 1. These inherited hypotheses and
the original source normalization remain essential.

**Corollary 3 (the already proved strict long-twist class).**
Fix a literal ordered Conway construction in the class of
Section 1 of the filled-meridian theorem: its original positive
wire domain is strict; endpoints, framings and parities are
recorded; the filled diagram has one knot component and no
internal closed component. Retain the pure-leaf qualification
in the two-leaf knot case. Every fixed signed twist
\(n_i=\epsilon_i-2p_i\) must be independently sufficiently long,
with no bound on ratios between their magnitudes. The twists
and construction are fixed before \(N\) varies.
There is no restriction on the valences, adjacency or path
lengths of the bare components, by the general component theorem.

For this already proved class put
\(\kappa=\operatorname{Vol}(S^3\setminus K)/(2\pi)>0\).
For every fixed \(R>0\), the actual regularized period satisfies
\[
 \sup_{|\zeta|\le R}|R_N(e^{\zeta/N})|
                    \le e^{o(N)}(1+|K_N|),\qquad
 \lim_{N\to\infty}\frac1N
       \log\sup_{|\zeta|\le R}|R_N(e^{\zeta/N})|=\kappa .
 \tag{26}
\]
The limit is through both parities. It is a disk-norm limit,
not a nonvanishing or pointwise profile assertion across
all the resonances.

To check the coordinates, denote the original function of the
meridian \(M\) by \(\mathfrak F_N(M)=F_N(M^2)\).
Set
\[
 M=q_N^s=e^{\zeta/(2N)},\qquad
                  s=\frac{\zeta}{2\pi i}.
 \tag{27}
\]
Choose any fixed \(0<r<2\pi\). The proved source profile,
equation (5) of the filled-meridian theorem, and (16) give
uniformly on \(|\zeta|\le r\),
\[
 R_N(e^{\zeta/N})
   =\frac{K_N}{N}e^{-(N-1)\zeta/(2N)}
       A_N\!\left(\frac{\zeta}{2\pi i}\right)
                        (1+O_r(N^{-1}))
       -\frac{P_N^{\rm col}(e^{\zeta/N})}
                    {S_N(e^{\zeta/N})},
 \qquad
 A_N(s)=q_N^{a(D)s^2/2}.
 \tag{28}
\]
The integer \(a(D)\) is the original fixed framing ledger;
no scalar has been reassigned. On this disk the sine ratio
of that source theorem equals the hyperbolic ratio in (16),
is bounded away from zero, and cancels exactly as displayed.
The scalar \(A_N\) is uniformly bounded, and the final term
has polynomial size by (13). The already proved
all-level complete-value asymptotic has rate \(\kappa>0\).
These facts prove a small-disk upper bound relative to
\(1+|K_N|\). Lemma 1 extends it to every fixed \(R\).
The lower bound in (26) uses the exact central value
\(N R_N(1)=K_N-P_N^{\rm col}(1)\), whose polynomial
subtraction cannot change this positive rate.

The same corollary transfers through the ordered net-twist
and cylindrical/cap-closure reductions admitted in
Section 10 of the filled-meridian theorem, with their
recorded orders and rotations. Every surviving strict
factor must have sufficiently long **net** twists.
For a hyperbolic input in that scope, exactly one strict
knot factor remains and the other factors are unknots.
The reduction transports the zero-framed whole ADO Laurent
family and the marked meridian, so it transports (12) and
(26), not just the complete scalar. Large original twists
with cancelling net sums do not satisfy this condition
automatically.

If a specified actual equation for one of these knots also
satisfies the two classical end conditions of the fixed-disk
theorem, that theorem and (26) give \(U_0=\kappa\).
This last joint-envelope conclusion retains its operator
hypothesis. Neither that hypothesis nor any new volume
limit is proved by the corollary; its all-level input is
the existing complete-value theorem for this same class.

For arbitrary short components, the missing step is an
equally source-preserving regrouping or signed observation
estimate that proves (18) or directly proves (19), with the
correct complete value as its comparison. The paired-factor
lemma alone supplies neither. The present deductions weaken
the required profile conclusion and remove a fixed-radius
restriction; they do not assert a new knot-family volume
theorem or a new all-level lower bound for the complete value.
