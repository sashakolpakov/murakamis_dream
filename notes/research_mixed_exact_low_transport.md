# Exact transport of low boundary coordinates

Research deduction, 5 November 2026. A low middle symbol in an incoming
boundary state can be moved exactly to \(1/10\). Its final halo symbol
is irrelevant to the incoming weight. Together with the complete raw
right-row comparison, this removes every nonseam coordinate below
\(1/10\) from the remaining full-period upper-envelope problem. It
does not prove the still-needed right-interface sign.

## 1. A terminal reset identity

Fix an original periodic type word, its actual geometric reference
\(r\), and \(0<\rho\le1/1000\). Use the hybrid contour and the
half-period alphabet \([\rho,1/2]\), with every permitted selection.
The incoming potential and its finite incoming maxima are those of
the [exponential memory theorem](research_mixed_exponential_incoming_memory.md)
and its stated extension to this alphabet. A state at layer \(i\)
consists of positions \(i-2,i-1,i\); transition \(i-1\) evaluates
the physical edge joining positions \(i-2,i-1\). Write
\[
 t_j=w_j+\frac\theta2(\omega_{j-1}+\omega_j),
 \qquad 0<\theta<1,
 \qquad w_j=\Re(\phi_j-\Gamma_j)
       +\frac{\sigma_{j-1}\chi(z_{j-1})+\sigma_j\chi(z_j)}2.
 \tag{1}
\]
Here \(\Gamma_j\) is the original complex tangent and
\(\chi(z)=\max\{\Re g(z),-2\pi\Im z\}\). Types and references
are extended periodically; target symbols at repeated layers remain
independent. Let
\[
 v_x=((y,\tau),(x,\sigma),(z,\kappa)),
 \qquad \rho\le x\le1/10,
 \qquad \rho\le y,z\le1/2.
 \tag{2}
\]
All selections in (2) are permitted by their respective types. Put
\(\alpha=\epsilon_{i-2}\), \(\beta=\epsilon_{i-1}\), and
\[
 f_{\alpha\beta}(u,v)=\Re\phi_{\alpha\beta}(u,v),\qquad
 P^-_i=\phi_{\alpha\beta,b}(r_{i-2},r_{i-1}),
\]
where \(f\) is evaluated at two real targets. For
\(x,x'\in[\rho,1/10]\), define
\[
 T_i(y;x,x')=f_{\alpha\beta}(y,x)-f_{\alpha\beta}(y,x')
                           -\Re P^-_i(x-x').
 \tag{3}
\]

**Theorem 1.** The incoming potential is independent of the last
symbol in (2). Moreover, for every \(x,x'\in[\rho,1/10]\),
\[
 H_i(v_x)-H_i(v_{x'})=T_i(y;x,x').
 \tag{4}
\]
The same assertions hold for each finite incoming maximum
\(A_i^{[h]}\), \(h\ge3\), when the length and initial baseline
layer are the same on both sides.

**Proof.** Both row-dependent left cutoffs are identically zero
throughout \([\rho,1/10]\). A symbol in this interval forces its
own height and those of its two neighbors to zero. In a history
ending at (2), the final evaluated edge therefore has precisely the
real targets \((y,x)\). Changing the final symbol \((z,\kappa)\)
can only change the height of \(x\) in that edge, and that height is
already zero. This symbol's occupation has not yet appeared in a
transition of the history. Neither its selection nor its own target
is evaluated. All preceding transitions are unchanged.

Now change \(x\) to \(x'\) in the same history. The preceding
transition can see \(x\) only through a left cutoff controlling the
height at \(y\), so it remains unchanged. Earlier transitions also
remain unchanged. In the last transition the selected corrections
at \(y,x\) are zero, since both targets are real in the half-period.
The occupation of the middle symbol is the same saturated value
\(1/4000\) for every \(x\in[\rho,1/10]\), regardless of its
permitted selection. The only change is consequently (3).

These modifications are bijections between the histories with the
prescribed terminal states. They preserve the initial baseline and
length. Hence their exact weight difference passes to each finite
maximum. For the unrestricted incoming supremum, prepend whole
baseline periods if necessary to expose the final three appended
symbols; this changes neither phase nor occupation. The same
bijection proves (4). This proof does not identify distinct target
positions when the primitive reference period is one or two.
\(\square\)

Thus one can use the already proved
[low-terminal bound](research_mixed_low_terminal_incoming_bound.md)
only at \(x'=1/10\), and transfer its bound to every lower \(x\)
by the exact term (3). Applying that earlier coarse bound separately
at every \(x\) needlessly discards this information. The identity is
for the coherent phase potential, not for a finite kernel value.

## 2. Monotonicity of every reduced real raw row

Let \(J=\Re g\) on the real period and
\(L(t)=J'(t)=\log(2\sin\pi t)\) for \(0<t<1\). Consider an
edge with one real low target \(x\in(0,1/10]\) and one real right
target \(1/2\). Let \(\eta\in\{0,1\}\) be the type indicator
at the low target and \(\epsilon\in\{0,1\}\) the own type of
the block. Its complete allocated raw row rate is
\[
 Q_{\epsilon,\eta}(u,x)
  =J(u+1/2)+J(u+x)-(2+\epsilon)J(u)
                                -(1+\eta/2)J(x).
 \tag{5}
\]
The full Fourier half at the low target is \(-\eta J(x)/2\):
the true upper branch is \(\max\{-J(x),0\}=-J(x)\).
Selections do not change this expression at height zero. The other
Fourier half at \(1/2\) has upper rate zero. The first-argument chirp
also has unit modulus here. Thus (5) is valid in both orientations.

The [complete complex-neighbor row reduction](research_mixed_complex_right_row_reduction.md)
proves that the full row supremum at these targets equals the
supremum over \(0\le u\le1/2\). For every such fixed row,
\[
 \begin{split}
 \partial_x Q_{\epsilon,\eta}(u,x)
   &=L(x+u)-(1+\eta/2)L(x)\\
   &\ge-\frac\eta2 L(x)\ge0.
 \end{split}
 \tag{6}
\]
Indeed the minimum of \(\sin\pi t\) on
\([x,x+1/2]\) is at an endpoint. Since \(x\le1/10<1/4\),
\[
 \sin\pi(x+u)\ge
       \min\{\sin\pi x,\cos\pi x\}=\sin\pi x,
 \qquad L(x)<0.
 \tag{7}
\]
This also handles the row endpoints \(u=0,1/2\), by continuity
of \(J\). It follows that the complete raw upper rate
\[
                 Q_{\epsilon,\eta}(x)
                   =\max_{0\le u\le1/2}Q_{\epsilon,\eta}(u,x)
 \tag{8}
\]
is nondecreasing on \((0,1/10]\). The derivative comparison is
pointwise in the row; it does not assume a differentiable optimizer
or a numerical bound on its location.

For example, suppose \(x\) is the last A coordinate before a right
run. Keep its preceding terminal symbol \(y\) fixed. Let
\(D_i^{\rm raw}(x)=Q_{\epsilon_i,\epsilon_{i-1}}(x)
-\Re\Gamma_i(x,1/2)\). Original critical stationarity gives
\(P^-_i+\phi_{i,a}(r_{i-1},r_i)=0\). Therefore (4) implies
the exact cancellation
\[
 \begin{split}
 &[D_i^{\rm raw}(x)+H_i(v_x)]
    -[D_i^{\rm raw}(1/10)+H_i(v_{1/10})]\\
 &\quad=Q_{\epsilon_i,\epsilon_{i-1}}(x)
                 -Q_{\epsilon_i,\epsilon_{i-1}}(1/10)
      +f_{\epsilon_{i-2},\epsilon_{i-1}}(y,x)
                 -f_{\epsilon_{i-2},\epsilon_{i-1}}(y,1/10)
       \le0.
 \end{split}
 \tag{9}
\]
The last inequality also uses the strict real monotonicity in
[the deep-low lemma](research_mixed_deep_low_half_region.md), valid
for every other real target in \((0,1/2]\). Thus this exact
common-potential interface contribution is largest at \(x=1/10\).
This conclusion concerns this incoming end of the interface; it does
not assume that an independently relaxed entry/exit bound has the
same monotonicity.

## 3. A global reduction of the mixed upper envelope

Fix a real cyclic configuration in \([0,1]^m\), every permitted
selection, and the same hybrid collar \(\rho\). Give the original
positions the fixed labels
\[
 S=\{j:x_j<\rho\},\qquad R=\{j:x_j\ge1/2\},\qquad
 A=\{j:\rho\le x_j<1/2\}.
 \tag{10}
\]
Labels remain fixed after the comparisons. Use the following sum
\(\mathcal U(x)\) of complete allocated upper rates, in this
order of priority:

* every edge incident to \(R\) uses the complete original raw row
  envelope, including all true Fourier halves;
* every remaining edge incident to \(S\) uses its established
  angle-uniform SS or SA collar profile;
* every remaining edge uses its complete coherent conditional rate,
  including the selected correction in (1).

The raw collar profiles and their finite-source scope are those of
the [closed half-period theorem](research_mixed_closed_half_period.md)
and the [height-resolved source theorem](research_mixed_height_resolved_seam_sources.md).
An SA profile depends on its physical other height, type and selection,
but bounds all its other real angles. In particular it remains fixed
when a real height-zero deep A coordinate moves. All of these rates
retain the original allocated factorial and Fourier normalizations.

First put \(x_j=1/2\) at every position labelled \(R\), retaining
the raw edge labels. By the complete row reduction,
\[
                       \mathcal U(x)\le\mathcal U(x^{1/2}).
 \tag{11}
\]
It applies also to an RS edge: the other target is real in
\([0,\rho]\), including zero, which is within the raw reduction's
closed domain. Its Fourier upper factor is fixed during the right
angle comparison. Every other target is unchanged, since both the
old right coordinate and \(1/2\) have left cutoff one and height
zero.

Now replace each deep A coordinate in \([\rho,1/10]\) by \(1/10\),
one at a time, obtaining \(\widehat x\). Both left cutoffs stay
zero throughout each motion. The complete height vector is unchanged;
the moving target and both its neighbors are real. An incident AA
coherent edge increases by the real deep-low lemma. An incident AR or
RA raw edge increases by (6)--(8). An incident SA collar profile is
unchanged by its angle-uniformity. All other rates are unchanged.
Consequently
\[
           \boxed{\mathcal U(x)\le\mathcal U(x^{1/2})
                                      \le\mathcal U(\widehat x).}
 \tag{12}
\]
At the right side of (12), all nonseam nonright real coordinates
lie in \([1/10,1/2]\), while every right coordinate is \(1/2\)
and still uses its raw envelope. All seam coordinates, selections,
target heights and edge source allocations are the original ones.

If rates are expressed as defects from their original complex
tangents, (12) holds after summing all edges. For each moved target,
the two tangent derivatives sum to zero by actual reference
stationarity. Individual tangent-subtracted edge bounds need not
be monotone. For a one-cycle one counts the two derivatives of its
single diagonal edge; for a two-cycle one retains both parallel
edges. Thus neither comparison loses a repeated incidence.

## 4. A uniform cutoff for long right runs

The [direct long-run theorem with zero contacts](research_mixed_long_right_runs_with_zero_contacts.md)
uses exactly the R-priority envelope of Section 3. Its restricted
nonseam domain is \([1/10,1/2]\); on that domain a proper right run
of length at least 352 pays its two boundary costs and retains phase
loss \(1/100\) per right coordinate. Its seam comparison also retains
loss \(3/1000\) per seam coordinate, without invoking a coherent
packet at zero.

**Corollary 2.** Allow arbitrary original real coordinates on the full
period, with the fixed labels (10). Suppose \(R\) is nonempty and
every proper R-run has length at least 352. Then
\[
 \mathcal U(x)\le M-\frac{|R|}{100}-\frac{3|S|}{1000}.
 \tag{13}
\]
For an all-R cycle the stronger loss \(m/50\) holds without a
length restriction. The original selected finite-product upper rate,
after one total tolerance less than \(1/1000\), is at most
\[
                    M-\frac{|R|}{200}-\frac{|S|}{500}.
 \tag{14}
\]

Indeed (12) preserves both sets and all their incidences. It puts
every nonseam nonright target in the direct theorem's restricted
domain. Apply that theorem to \(\widehat x\), still using raw bounds
on the positions labelled R, and then use (12). This proves (13).
The total tolerance is smaller than the unused loss in passing from
(13) to (14), since \(|R|\ge1\). The case \(R\) equal to the
entire cycle is the direct theorem's internal-edge comparison.
Shared neighbors, zeros and all selections retain their physical
halfweights throughout. A mixed two-cycle has two boundary edges;
it does not satisfy the proper-run length condition and is not
silently included. The all-R one- and two-cycles are included.

## 5. Source scope and what remains

All coherent targets in this comparison stay in the completed source
domains. An edge incident to a moving deep A target is wholly real
on the fixed compact square \([\rho,1/2]^2\) unless it is already
assigned a raw collar or R bound. Its full real conditional packet
therefore applies. At a real \(1/2\) endpoint only the proved upper
Fourier bound is needed. The raw R and collar estimates include every
physical row, both parities, and the forced Fourier contribution.
They are not deduced from a continued saddle at a right argument.

For each fixed word and fixed \(\rho>0\), the established finite
estimates give a polynomial prefactor and any prescribed positive
total exponential tolerance above \(\mathcal U\). Spend that
tolerance once over the physical edges. The comparisons (4) and (12)
are statements about their rates; they are not a monotonicity theorem
for individual finite kernels, a contour substitution, or an added
auxiliary source product.

Thus any uniform comparison established for this same labelled
envelope on the reduced domain also bounds the original full-period
envelope. In particular the reduced short right-interface problem
has no deep-low angular variables left. Its required negative sign
still needs proof. No full-period asymptotic or enlarged knot-family
theorem is asserted here.

The [bounded diagnostic archive](../repro/diagnostics/2026-11-05-low-terminal-right-interfaces/README.md)
records the distinction between exact transport and the earlier
constant-surplus relaxation. That relaxation has positive test values
near zero; after applying the exact reduction it still has a smaller
positive test at \(x=1/10\). These are failures of that sufficient
upper proxy, not counterexamples to the common-potential inequality,
the finite source or the conjectured asymptotic. Neither scan is part
of the proof or the focused checker.

Reproduction:

    python3 experiments/check_mixed_exact_low_transport.py

The checker verifies the exact row/tangent and dependency identities,
source bindings and inherited run arithmetic. It does not recompute
any root or source cover, optimize an incoming history, or certify a
short-interface sign.
