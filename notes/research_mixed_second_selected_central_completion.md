# A uniform central estimate at the second selected coordinate

Research theorem, 6 November 2026.

The comparison proved here holds for the entire geometric reference
family, rather than at finitely many reference points. The first block
has type four, the second block has type four, and the third may have
type three or four. Only the second retained coordinate is moved to
the selected height. Both original Fourier alternatives then have a
strict central phase deficit, uniform in the remaining real variables
and in the external complex parameter. A common deficit is \(1/3200\).

This is the central estimate needed by the existing finite-product
reduction. For an outgoing type-four block, that reduction already
controls the other rows and contours, so the estimate completes the
local finite product. An outgoing type-three block still requires its
separate half-row comparison. Neither conclusion by itself estimates
the complete knot invariant.

## 1. The reference family and the quantity to estimate

Let
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi i w})-\pi^2/6}{2\pi i},
 \qquad V(s,t)=g(s+t)-g(s)-g(t).
 \tag{1}
\]
Use the original holomorphic branch on \(0<\Re w<1\). All
arguments below remain in that strip. Fix the first flag
\(\alpha=1\), the second flag \(1\), and an outgoing flag
\(\beta\in\{0,1\}\), where zero denotes type three and one
denotes type four.

The [canonical-reference theorem](research_mixed_second_selected_reference_curve.md)
gives a holomorphic solution of the original seven prefix equations.
Write its five coordinates used in the comparison as
\[
 r(c)=(a_*(c),u_*(c),z_*(c),v_*(c),b_*(c)).
 \tag{2}
\]
The complex number \(c=s_4^*\) is the next external leg: it is
attached at word length four and ordinary at greater lengths.
It is distinct from the imaginary part of \(z_*\). The two other
prefix coordinates are retained when certifying (2), even though they
do not occur explicitly in the following allocated phase:
\[
 \begin{split}
 F(a,u,z,v,b)={}&V(u,a)+V(u,z)+V(v,z)+V(v,b)\\
 &-g(u)-\beta g(v)-g(z)-\tfrac12g(a)-\tfrac\beta2g(b)
       +2\pi i au+2\pi i zv.
 \end{split}
 \tag{3}
\]
At the reference, \(F_u=F_z=F_v=0\). The two boundary
derivatives, which need not vanish, are
\[
 \begin{split}
 p_L(c)&=g'(a_*+u_*)-\tfrac32g'(a_*)+2\pi i u_*,\\
 p_R(c)&=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \end{split}
 \tag{4}
\]
In particular the outgoing halfweight has not been dropped from
\(p_R\).

Put \(H=1/100\), \(P=[.22,.45]\), and
\[
 X_\beta=P\times[1/8,1/2]\times P
                    \times[\ell_\beta,1/2]\times P,
 \qquad \ell_0=3/20,\quad\ell_1=1/8.
 \tag{5}
\]
For \(x=(x_a,x_u,x_z,x_v,x_b)\in X_\beta\), define
\[
 w=(x_a+i\Im a_*,\ x_u+i\Im u_*,\ x_z+iH,
                 \ x_v+i\Im v_*,\ x_b+i\Im b_*).
 \tag{6}
\]
The factorial alternative is indexed by \(\nu=1\), and the
forced alternative by \(\nu=0\). Their phases and deficits are
\[
 \begin{split}
 \Psi_\nu(w)&=F(w)+(1-\nu)g(w_z)+2\nu\pi i w_z,\\
 D_\nu(c;x)&=\Re\{\Psi_\nu(w)-F(r(c))
       -p_L(c)(w_a-a_*)-p_R(c)(w_b-b_*)\}.
 \end{split}
 \tag{7}
\]
Thus the selected Fourier factor contributes the original debit
\(-2\nu\pi H\). Both complex boundary derivatives and the
original reference value are retained.

The external parameter belongs to one of the two clipped disks
\[
 \begin{split}
 K_3={}&\{|c-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4={}&\{|c-(.30-.052i)|\le.060\}
       \cap\{-.108\le\Im c\le-.001\}.
 \end{split}
 \tag{8}
\]
All terminating decimals in this note denote exact rational numbers.
The canonical solution is holomorphic on a neighborhood of each
domain by the original existence and uniqueness theorem on the
larger disks. For a mixed word of length at least four, these two
domains contain its actual next coordinate with its prescribed type.

**Theorem 1.** For each \(\beta\in\{0,1\}\), each
\(c\in K_3\cup K_4\), and every \(x\in X_\beta\),
\[
                 \max_{\nu=0,1}D_\nu(c;x)<-\frac1{3200}.
 \tag{9}
\]
For \(\beta=0\), the right-hand side may be replaced by
\(-1/100\). For \(\beta=1\) and \(c\in K_4\), it may
be replaced by \(-1/200\).

The quantifiers include all five real target variables and the
entire complex parameter domain. They do not assert that every
parameter is realized by the suffix of a finite word.

## 2. Bounds on the complete boundary

The calculation uses the [rational boundary charts](research_mixed_second_selected_external_boundary_charts.md).
There are five charts for \(K_3\) and four for \(K_4\): the two
semicircles, the horizontal clipping segments, and, for \(K_3\),
the oblique clipping segment. Both flags give eighteen interval
trees. An excluded interval is certified to miss its domain by a
strict rational geometric inequality. Every other terminal interval
has a reference enclosure, a phase bound for both alternatives, and
a bound for
\[
        \mathcal B(c)=|p_L'(c)a_*'(c)|+|p_R'(c)b_*'(c)|.
 \tag{10}
\]
Primes in (10) mean differentiation with respect to the complex
external coordinate \(c\), not to a chart parameter.

The [completed record](../repro/results/research-mixed-second-selected-external-boundary-attempt01.json)
has 3072 tree nodes and 1545 terminal intervals. Of the latter,
1431 carry estimates and 114 have geometric exclusion witnesses.
There are no pending or unresolved intervals. Each of the eighteen
trees has a prefix-free terminal partition of total binary mass one;
chart junctions are retained. The separate bounds over each entire
boundary imply the following conservative rational table:

| Outgoing flag | Domain | Boundary deficit \(\gamma\) is greater than | Response bound \(B_0\) is less than | \(R^2/2\) |
| --- | --- | ---: | ---: | ---: |
| 0 | \(K_3\) | .01634 | 1.645 | .0034445 |
| 0 | \(K_4\) | .01510 | 2.055 | .0018 |
| 1 | \(K_3\) | .00504 | 1.369 | .0034445 |
| 1 | \(K_4\) | .00817 | 1.677 | .0018 |

Here \(D_\nu\le-\gamma\) for both alternatives on the entire
boundary, uniformly in (5), and \(\mathcal B\le B_0\) there.
The minimum phase deficit and maximum response are taken separately
over all accepted intervals for the same domain and flag. Bounds
from favorable but different parts of the boundary are not paired.

The reference enclosures use the original logarithmic gradient, its
proved coercivity, and the [residual-localization estimate](research_mixed_prefix_residual_localization.md).
A numerical root is only a proposed center. An outward residual
bound and the existing existence theorem enclose the canonical
solution throughout the interval. The analytic Jacobian and its
certified inverse then enclose its derivative. The response in (10)
uses those same coordinate and derivative enclosures.

The [directional scalar estimate](research_mixed_second_selected_directional_budget.md),
with its [proved curvature improvements](research_mixed_second_selected_curvature_evaluation.md),
bounds the factorial alternative on all \(x_z\in P\) and the
forced alternative on \([.4,.45]\). The fixed identity
\[
 D_1-D_0=-\Re g(x_z+iH)-2\pi H>0
                  \qquad(.22\le x_z<.4)
 \tag{11}
\]
supplies the forced bound on the rest of \(P\). The index barriers
used by these estimates are proved on the original product (5),
so their restricted optimizations bound the original maxima. This
step does not replace a sum of Fourier alternatives by their minimum.

## 3. Extension from the boundary to the whole domain

Every accepted interval also proves the strict height conditions
\[
 \begin{gathered}
 -.102<\Im u_*<-.001,\qquad -.078<\Im a_*<.021,\\
 (\Im v_*,\Im b_*)\in
 \begin{cases}
 (-.065,.068)^2,&\beta=0,\\
 (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{12}
\]
Each coordinate is holomorphic near the closed domain. Its imaginary
part is harmonic, and the finite boundary cover gives strict margins.
The maximum and minimum principles therefore extend (12) throughout
the domain. The [horizontal concavity theorem](research_mixed_second_selected_horizontal_concavity.md)
now applies to the entire target product (5)--(6):
\(-\Re\Psi_\nu''\) is positive definite there. All arguments
of (1) stay strictly inside the original strip.

Fix a target \(x\) before differentiating the external parameter.
The [boundary-extension identity](research_mixed_stationary_reference_boundary_extension.md)
gives
\[
                    \Delta_c D_\nu\ge-2\mathcal B(c).
 \tag{13}
\]
The internal equations \(F_u=F_z=F_v=0\) are why only the two
boundary responses occur in (10). Each product in (10) is holomorphic,
so its modulus is subharmonic. The boundary bound implies
\(\mathcal B\le B_0\) throughout the domain.

For the containing disk with center \(c_0\) and radius \(R\), put
\[
                 q(c)=\frac{B_0}{2}(R^2-|c-c_0|^2).
 \tag{14}
\]
Then \(\Delta q=-2B_0\), so \(D_\nu-q\) is subharmonic.
The function \(q\) is nonnegative on the clipped disk, including
its straight boundary segments. Consequently the maximum principle
and the complete boundary estimates give
\[
             D_\nu(c;x)\le-\gamma+\frac{B_0R^2}{2}.
 \tag{15}
\]
This is an estimate for the original phase at each fixed target.
Taking a supremum in \(x\) afterward requires no differentiation
of a target optimizer or of a clipped numerical bound.

The conservative table gives, in its displayed row order, the
following strict lower bounds for \(\gamma-B_0R^2/2\):
\[
 .0106737975,\qquad .011401,\qquad
 .0003244795,\qquad .0051514.
 \tag{16}
\]
The smallest of these is greater than \(1/3200=.0003125\).
The first two are greater than \(1/100\), and the fourth is
greater than \(1/200\). Equation (15) proves Theorem 1.

## 4. Certificate and remaining scope

The completed calculation is specified in
[the boundary evaluation note](research_mixed_second_selected_external_boundary_evaluation.md)
and implemented by
[the standalone driver](../experiments/certify_mixed_second_selected_external_boundary.py).
The saved record has SHA-256
`2b720b596209b1c2f86f2a40d6cc4e946b3470e3e905a609a54bfe42ffbff5d7`.
It binds the 76 input files used by the calculation and retains the
whole interval trees, reference residuals, derivative enclosures,
response bounds and both original scalar alternatives. Acceptance
uses exact directed rational endpoints. The four rounded rows above
are only convenient weaker bounds on those endpoints.

The [saved-data checker](../experiments/check_mixed_second_selected_external_boundary_record.py)
reconstructs the rational charts and tree partitions independently,
checks every strict exclusion and accepted association, and recomputes
the separate boundary extrema and the four corrections. Its
[compact record](../repro/results/research-mixed-second-selected-external-boundary-saved-audit.json)
has SHA-256
`38971e851765e3a9df8be5aed447bf036110e7dc0a34e5c4885e5f59f3825f23`.
It performs no new root or phase evaluations. These consistency checks
supplement the analytic and outward-arithmetic arguments above; they
do not independently replace those arguments.

For a word of length at least four beginning with types four, four,
four, combine (9) with Theorem 1 of the
[outgoing type-four completion](research_mixed_second_selected_outgoing_four_half_row_completion.md).
Its two remaining central comparisons are precisely (7). Its other
profiles already have strict bounds. Thus, for every \(\tau>0\),
the original two-factor finite product satisfies
\[
 \mathcal B_{23,N}
 \le C_\tau N^{A_\tau}
       \exp\{N(\Lambda_{23}-1/3200+\tau)\}.
 \tag{17}
\]
Here \(\Lambda_{23}\) is the original geometric action with
both boundary affine terms, and the finite product and its powers
are exactly those in that completion theorem. The assertion retains
both level parities and all original finite rows. For sufficiently
large \(N\), (17) in particular gives a strict gap \(1/6400\):
choose \(\tau=1/12800\), and absorb the polynomial factor with
an additional exponent \(N/12800\).

For an outgoing type-three block, Theorem 1 supplies its central
comparisons but not the two main/half-row comparisons. A first block
of type three uses a different reference family. Selecting both
first coordinates changes the local product and its boundary data.
Those cases, other end positions, and estimates outside the retained
plateau remain separate requirements for the complete open source.
No finite-exception or new full knot-family conclusion is asserted
by this note.
