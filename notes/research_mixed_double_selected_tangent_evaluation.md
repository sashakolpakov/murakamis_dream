# Evaluating the simultaneous-selection tangent bound

Research calculation specification, 6 November 2026.

The remaining simultaneous-selection estimates can be tested without
subdividing the six real target variables. The
[concavity theorem](research_mixed_double_selected_concave_profile_budget.md)
proves that each profile is concave on its entire original target box.
The [boundary-extension theorem](research_mixed_double_selected_boundary_extension.md)
then extends a complete comparison on the external parameter boundary
to its interior. This note records how the calculation uses those
written results. The complete pass and its saved-data check have now
finished; their resulting theorem is stated in
[the completion proof](research_mixed_double_selected_tangent_completion.md).

## 1. Input and scope

The input is the previously completed first-type-four
[reference bank](../repro/results/research-mixed-second-selected-boundary-reference-bank.json),
with SHA-256
3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb.
It has 1,431 accepted reference cells. Together with its 114 strict
geometric exclusions, they partition eighteen rational boundary charts.
The two outgoing block types are treated separately.

Every accepted cell retains its original coordinates, external parameter
association, and previously computed outgoing derivative product.
No new reference equation or reference derivative is solved. The
complete pass visits each accepted cell once, evaluating sixteen
profiles when the outgoing type is three and eight when it is four.
There are 785 and 646 such cells, respectively, hence 17,728 profile
evaluations. The outgoing type-four half row has already been removed
by a pointwise comparison. The outgoing last-row profiles have the
separate proved gap \(3/1000\).

## 2. A trial is a proposal, not a stationary-point certificate

For each cell and profile, the driver may use a double-precision
optimizer to propose a real trial point. The proposal is rounded to
twelve decimal places, interpreted as an exact rational point, and
clipped to the exact original box. Fixed cut coordinates remain
exactly \(e=.27\) or \(v=.5\).

The optimizer's convergence flag and function value are recorded but
are not used to accept a mathematical inequality. The supporting-plane
bound holds at every trial in the box. An unsuccessful optimizer can
still supply a valid trial; it may give an unhelpful upper bound.
There is no retry with a different source, reference, or target domain.

For a profile \(f\), real box \(\prod_i[l_i,r_i]\), and trial \(y\),
the exact bound is
\[
 \sup_x f(x)\le f(y)+
     \sum_i\max\{f_i(y)(l_i-y_i),f_i(y)(r_i-y_i)\}.
\]
The evaluator encloses \(f(y)\) and every real derivative with Arb at
192 bits, using the whole original reference cell. If a derivative
lies in \([p_i^-,p_i^+]\), its support contribution is bounded by the
maximum of the four rational endpoint products. Fixed coordinates
contribute zero. The trial value, derivative intervals, four products,
and final rational sum are retained separately.

## 3. Original phases and branches

The evaluator uses the original primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad J(z)=g(z)-\frac{i\pi}{2}z(1-z).
\]
Every primitive argument is checked to lie strictly in \(0<\Re z<1\).
The complete cap uses its original auxiliary branch
\[
 \xi(e)=\frac1\pi
   \arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2}.
\]
The real part of the square-root discriminant must be positive.
The arguments \(\xi,e-\xi,\frac12-\xi\) are also checked against
the regular strip. This evaluates the established explicit cap branch;
it is not a new critical-point solve.

The full reference action is evaluated on its certified coordinates.
The sole outgoing marginal remains
\[
 p_R=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
\]
Both selected weights and their four Fourier alternatives are retained.
The main, cap-cut, and outgoing half-row targets have exactly the
heights specified in the concavity theorem. The cuts have height zero,
while the reference subtraction still uses its original complex
private and ordinary coordinates.

## 4. Whole-boundary aggregation

For each of the four pairs \((\beta,K_\sigma)\), take the largest
profile upper bound over every accepted cell and required profile.
Separately take the largest saved upper bound for
\(B_R=|p_R'b_*'|\) over that entire boundary. If these numbers are
\(U\) and \(B\), the interior upper bound is
\[
 U+\frac{R_\sigma^2}{2}B,\qquad
 \frac{R_3^2}{2}=\frac{6889}{2000000},\quad
 \frac{R_4^2}{2}=\frac9{5000}.
\]
The phase and response extrema are not paired cell by cell.
Strict negativity of all four rational totals, complete boundary
coverage, absence of unresolved evaluations, and unchanged inputs are
required for a completed result.

The driver verifies the inherited reference dependencies before the
pass and rechecks their hashes afterward. Its code, evaluator,
proposal helper, and the written concavity and extension proofs are
recorded as inputs. A saved-data checker can verify the cell
associations, exact support arithmetic, profile inventory, boundary
partitions, response maxima, and input bindings without repeating an
analytic evaluation.

## 5. Diagnostic and complete runs

The
[first diagnostic](../repro/diagnostics/research-mixed-double-selected-profiles-attempt01.json)
contains 96 floating-point optimizations at eight prescribed reference
midpoints. These are candidate maxima, not bounds. One optimizer
reported an unsuccessful line search; that status is preserved.

The
[interval diagnostic](../repro/diagnostics/research-mixed-double-selected-tangent-boundary-attempt01.json.gz)
uses those same trials on the eight whole reference cells. All 96
outward bounds and all four aggregated corrections are strictly
negative. This subset calculation proves no full boundary comparison.

The complete run is:

    python3 experiments/certify_mixed_double_selected_tangent_boundary.py \
      --output repro/results/research-mixed-double-selected-tangent-boundary-attempt01.json.gz

The prescribed pass completed with all 17,728 bounds strictly negative,
no unresolved evaluations, and no changed inputs. The
[saved-data check](../repro/results/research-mixed-double-selected-tangent-boundary-saved-audit.json)
verifies the full arithmetic and coverage. The driver records any
finite or positive bound as such; it does not refine a cell or replace
a failed inequality.
