# Reducing every plateau alias to the smaller central box

Research proof, 4 November 2026. The author interval covers and independent
320-bit saved-witness replay have passed. Frozen manuscripts and completed
source artifacts are unchanged.

This note concerns the full constant-height plateau \([.22,.45]^m\).
The curved parts of the outer contour remain separate.

## 1. The two actual Fourier branches

Write the original conditional effective phase as
\[
 \Psi(\mathbf t)=\sum_v\phi_{\epsilon_v}(t_{v-1},t_v),\qquad
 \phi_\epsilon(a,b)=Q_\epsilon(s_\epsilon(a,b);a,b)
                         -g(a)-(1+\epsilon)g(b),                 \tag{1}
\]
where \(g(z)=[\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6]/(2\pi i)\).
All conditional roots and source packets use the original zero logarithmic
lift on the [transition products](research_mixed_transition_conditional_rectangles.md).

Let \(S\ne\varnothing\) be a subset of the type-four outer variables.
Their heights are \(h=7/500\). Every other height stays at its original
critical value, in \([-.03,.02]\) for type three and
\([-.057,-.02]\) for type four. Put \(M=\Re\Psi(\mathbf t^*)\).
For each \(T\subseteq S\), define the real branch
\[
 F_{S,T}(\mathbf x)=
 \Re\left[\Psi(\mathbf x+i\mathbf h)
                  +\sum_{v\in T}g(x_v+ih)\right]
                        -2\pi h\,|S\setminus T|.                \tag{2}
\]
The maximum of (2) over \(T\) is exactly
\(\Re\Psi-\sum_{v\in S}\min(\nu(x_v+ih),2\pi h)\), where
\(\nu=-\Re g\). Thus the polynomial Fourier forcing branch is retained.
In particular, this argument does not replace the true weight by a
reciprocal factorial near \(x=.45\).

The [plateau pair-form lemma](research_mixed_plateau_accretivity.md)
also applies to every branch (2). A term \(+g(t_v)\) at a four-variable
removes its extra outer term \(-g(t_v)\) in the unsummed phase.
It leaves both positive triangle forms, every inner diagonal, and the
original imaginary chirps. The same complex Schur argument therefore
gives
\[
                 -\Re F_{S,T}''\succeq I_m/2000.                \tag{3}
\]
Here (3) denotes the real-coordinate Hessian at the fixed heights.
No curved-contour concavity is asserted.

## 2. Conditional derivatives and their signs

For a conditional root \(s=s_\epsilon(a,b)\), put
\[
 \begin{split}
 D_{\rm in}&=g'(s+b)-(1+\epsilon)g'(b),\\
 D_{\rm out}&=g'(s+a)+2\pi is-g'(a).
 \end{split}                                                    \tag{4}
\]
The derivative at one outer coordinate is the sum of its incoming
and outgoing expressions in (4). A forcing coordinate additionally
has \(g'(t)\). This counts both incidences, also at cyclic lengths
one and two.

On all four independent transition products the interval certificate
proves
\[
                         \Re\phi_{\epsilon,ab}>1/100.           \tag{5}
\]
The expression is holomorphic in both parameters. Its real part is
bounded on the 64 distinguished-boundary products by exact dyadic
covers; successive harmonic minimum principles give (5) inside.
The original-logarithm affine Newton test precedes every derivative
evaluation. No exponentiated root alone is used.

Consequently, a real-coordinate derivative increases when either
neighbor real coordinate increases while heights stay fixed.
This comparison does not require the neighbors to be independent
in the original cyclic word.

The companion covers establish the following bounds, uniformly in all
allowed type and height choices.

* At a type-four coordinate \(x=.4\), with both neighbor real
  coordinates at \(.45\), the full derivative is negative. This includes
  the forcing term when that coordinate belongs to \(T\).
* For a type-three coordinate \(x=\rho\in[.4,.45]\), with a type-three
  neighbor at \(\rho\) and a type-four neighbor at \(.4\), the derivative
  is negative.
* At \(x=\rho\in[.22,.25]\), with both neighbor real coordinates at
  \(\rho\), every unselected-coordinate derivative is positive.
  At a selected type-four coordinate the derivative exceeds \(-1/50\).

For the last assertion the frequency branch is the worst one:
\[
                  \Re g'(\rho+.014i)>0
                           \qquad(.22\le\rho\le.25).             \tag{6}
\]
Indeed \(R=e^{.028\pi}>1>2\cos(.44\pi)\), so
\(|1-Re^{-2\pi i\rho}|^2>1\).
The forcing branch adds the positive term in (6).

Each marginal in (4) is certified separately, with a common short
interval for the own height when necessary. The two marginal bounds
are then added. This retains the shared own-height dependence instead
of assigning unrelated worst heights to the two incidences.
The covers include the entire neighboring type-four height interval
\([-.057,.014]\); actual unselected and selected heights are a subset.
The exact rational sum tests, rather than decimal extrema, decide all
three assertions above. Their aggregate bounds are
\[
 \begin{array}{c|c}
 \text{lower threshold, type three}&D>2947/12500\\
 \text{lower threshold, unselected four}&D>581/25000\\
 \text{lower threshold, selected four}&D>-123/6250>-1/50\\
 \text{upper four, unselected}&D<-5531/12500\\
 \text{upper four, selected frequency}&D<-71151/100000\\
 \text{upper three threshold}&D<-1029/100000 .
 \end{array}
\]
The selected-four upper face remains strictly negative after adding
\(\Re g'(.4+.014i)\) for its forcing branch.

## 3. Coordinate clamping

Fix one branch (2). First lower every four-coordinate greater than
\(.4\) to \(.4\), keeping all other coordinates fixed in the plateau.
Equation (5) bounds its derivative by the derivative with both
neighbors at \(.45\). The first face bound and own-coordinate
concavity (3) make it negative throughout \([.4,.45]\).
This step can only increase \(F_{S,T}\).

Next decrease a common upper threshold \(\rho\) from \(.45\) to \(.4\),
replacing every remaining type-three coordinate \(x\) by
\(\min(x,\rho)\). At every active coordinate the type-three neighbors
are at most \(\rho\), and the type-four neighbors are at most \(.4\).
Equation (5) and the second face bound again give a negative derivative.
The piecewise differentiable threshold path can only increase the branch.

All coordinates now belong to \([.22,.4]\). Raise a common lower
threshold \(\rho\) from \(.22\) to \(.25\), replacing \(x\) by
\(\max(x,\rho)\). Every active coordinate has neighbors at least
\(\rho\). The third face bound gives a nonnegative contribution at
unselected coordinates and a contribution greater than \(-1/50\)
at selected coordinates. Integration therefore gives
\[
 \max_{[.22,.45]^m}F_{S,T}
 \le \max_{[.25,.4]^m}F_{S,T}
                    +\frac{3}{5000}|S|.                        \tag{7}
\]
There is no loss proportional to the total word length. The threshold
paths have finitely many break points, which do not affect the integral
inequalities. Repeated cyclic incidences are retained in (4).

## 4. The complete finite alias density

The [central alias theorem](research_mixed_central_alias_gap.md) proves,
before its small Fourier tolerance is spent,
\[
 \max_{[.25,.4]^m}F_{S,T}
 \le M-\left\{\frac{721}{10000}
             -\frac{25}{2}\left(\frac{71}{1000}\right)^2\right\}|S|
 =M-\frac{727}{80000}|S|.                                      \tag{8}
\]
Combining (7) and (8) leaves \(679|S|/80000\).

The full canonical conditional packets hold uniformly on the entire
plateau product. For every unselected type-four variable, \(\nu>0\)
on its compact lower strip. The original Fourier polynomial bound,
with its forcing retained, therefore gives the rate (2), with an
arbitrarily small error per four-variable. If their number is \(k\),
choose that error below \(1/[1000\max(k,1)]\). The total error is at
most \(1/1000\), hence at most \(|S|/1000\).
The exact reserve is
\[
 \frac{679}{80000}-\frac1{1000}-\frac1{150}
                         =\frac{197}{240000}>0.                 \tag{9}
\]
All finite scalar factors and level powers have only polynomial modulus
for a fixed word. Thus the complete original alias density satisfies
\[
 |\mathcal D_{S,N}(\mathbf x+i\mathbf h)|
       \le \operatorname{poly}(N)\,
                  \exp N\{M-|S|/150\},
 \qquad \mathbf x\in[.22,.45]^m.                                \tag{10}
\]
This includes every conditional row, every original alias factor, and
the actual \(d_N\), without choosing a half-weight branch.
The absolute plateau integral satisfies the same bound.

Equation (10) is only the plateau part of each nonempty alias.
The tapered outer regions and the full mixed-word source asymptotic
remain separate. No new knot volume theorem follows from this note.

## 5. Reproduction

Run

    python3 experiments/certify_mixed_plateau_alias_clamping.py --precision 256

The author checks 64 distinguished-boundary products for (5), followed by
64 marginal-gradient domains. The complete covers contain 4,459 and
54,162 accepted cells respectively. Every cell stores a rational affine
root witness. Degenerate fixed parameters are omitted from the bisection
coordinates; all nondegenerate parameter intervals are covered exactly.
The record retains all 16 rational group tests, the two Fourier scalar
checks, both exact rate identities, and hashes of the original source
dependencies. Floating polynomial roots propose centers only.
The independent replay verifies every saved witness at 320 bits, without
root proposals or author imports, using the original sine-log equation,
real-coordinate cotangent Hessians and scalar log-modulus marginals.
It checks all 4,459 mixed-derivative cells and 54,162 marginal cells without
refinement, reconstructs every parameter domain and exact cover, and
rechecks the 16 rational groups and both budget identities. Run

    python3 experiments/replay_mixed_plateau_alias_clamping.py --precision 320

The [author record](../repro/results/research-mixed-plateau-alias-clamping.json)
and [independent replay](../repro/results/research-mixed-plateau-alias-clamping-replay.json)
bind the current proof, scripts, source dependencies and immutable input.
