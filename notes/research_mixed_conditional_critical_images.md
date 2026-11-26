# Canonical conditional packets at all cyclic mixed critical images

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note concerns one complete conditional index sum. Its parameters
are the correlated neighbors of a universal two-leg block. It retains
every revived row of the canonical finite source, and both signs of the
original cotangent aliases. It does not estimate the remaining outer
torus integral or its wrapped weights.

## 1. Domains and the original source

Put
\[
 \mathcal P_3=\{|z-(.35-.01i)|\le .083\},\qquad
 \mathcal P_4=[.27,.33]+i[-.057,-.001].
 \tag{1}
\]
The [critical height theorem](research_mixed_cyclic_critical_height_bounds.md)
places every leg of every finite cyclic word in \(3,4\) in the interior
of its corresponding set (1). Both sets lie strictly inside the older
typed disks of the
[universal localization theorem](research_mixed_cyclic_critical_localization.md).
Consequently, for every block type \(3+\epsilon\) and external types
\(\tau_a,\tau_b\), the unique original block roots
\((s(a,b),t(a,b))\) are holomorphic on a neighborhood of
\(\mathcal P_{\tau_a}\times\mathcal P_{\tau_b}\). Their equations are
\[
 \begin{split}
 g'(s+t)+g'(s+a)-(2+\epsilon)g'(s)+2\pi ia&=0,\\
 g'(s+t)+g'(t+b)-(2+\epsilon)g'(t)+2\pi ib&=0,
 \qquad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \end{split}
 \tag{2}
\]
The original zero logarithmic lifts and the old output typed disks are
retained. All four legs belong to
\(\mathcal Q=\{.23<\Re z<.45,\ |\Im z|<.12\}\).

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), use the single canonical
finite sum
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)=
 \widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}(r^{N\alpha+1};r)_j
                        (r^{N\beta+1};r)_j}{P_j^{2+\epsilon}}.
 \tag{3}
\]
This is the function in the
[canonical type-three proof](research_mixed_three_canonical_conditional.md)
and [type-four continuation](research_mixed_four_conditional_complex_neighbors.md).
It matches the whole physical conditional sum at every lattice pair;
off the lattice it retains the revived rows.

Define its original central phase and symbol by
\[
 \begin{split}
 Q_\epsilon(z;\alpha,\beta)
   &=g(z+\alpha)+g(z+\beta)-(2+\epsilon)g(z)+2\pi i\alpha z,\\
 A_\epsilon(z;\alpha,\beta)
   &=e^{\pi i(\epsilon z-\alpha-\beta)/2}
     \frac{\sqrt{2\sin\pi(z+\alpha)}\sqrt{2\sin\pi(z+\beta)}}
          {(2\sin\pi z)^{1+\epsilon/2}}.
 \end{split}
 \tag{4}
\]
The square roots use the regular sine branches. These formulas include
all parameter constants and the order-one factorial carrier.

**Theorem 1.** Uniformly on every product in (1),
\[
 \begin{split}
 \mathcal L_{\epsilon,N}(a,t(a,b))
  =N^{(1-\epsilon)/2}
   \frac{\sqrt{2\pi}\,A_\epsilon(s;a,t)}
        {\sqrt{-Q_{\epsilon,zz}(s;a,t)}}
   e^{NQ_\epsilon(s;a,t)}(1+O(N^{-1})).
 \end{split}
 \tag{5}
\]
The analogous formula with \((s,a,t)\) replaced by \((t,b,s)\) holds
at the opposite orientation. The coefficient is holomorphic and nonzero.
Both level parities are included. The normalized expansion admits all
fixed holomorphic derivatives on smaller products and all fixed orders
of stationary phase.

In particular this gives the actual canonical conditional packet at
every cyclic mixed critical configuration. It does not identify the
remaining outer cycle with a knot or give that cycle a nonzero observed
coefficient.

## 2. A finite distinguished-boundary certificate

The boundary of \(\mathcal P_3\) is parametrized by
\(.35-.01i+.083e^{2\pi i\theta}\). The four sides of
\(\mathcal P_4\) are parametrized affinely, counterclockwise, with
\(0\le\theta\le1\). The six unordered block/type cases therefore give
\(2(1+4+16)=42\) two-parameter pieces. Each piece is checked in both
conditional orientations; no ordering of the two external types is
discarded.

The checker covers each parameter square by exact dyadic rectangles.
On every accepted rectangle it verifies the original affine complex
Newton self-map for (2), not a polynomial equation obtained by
exponentiation. It also verifies a point Newton enclosure at the
parameter midpoint. Let
\[
 \ell=3/20,\qquad u=49/100,\qquad h=1/5,
 \qquad M=\Re Q_\epsilon(s;\alpha,\beta).
 \tag{6}
\]
Here \((\alpha,\beta)=(a,t)\), or \((b,s)\) at the other orientation.
The following inequalities are checked outward on every parameter cell:
\[
 \begin{split}
 M-\Re Q_\epsilon(\ell;\alpha,\beta)&>10^{-4},\\
 M-\Re Q_\epsilon(u;\alpha,\beta)&>10^{-4},\\
 M-H_\epsilon(1;\alpha,\beta)&>10^{-4},\\
 M-\Re Q_\epsilon(x\pm ih;\alpha,\beta)+2\pi h&>10^{-3}
                      \quad(\ell\le x\le u).
 \end{split}
 \tag{7}
\]
The entropy \(H_\epsilon\) is the full periodic product entropy (7) of
the [contour reductions](research_mixed_conditional_image_contours.md),
not a continuation of a decreasing physical-support branch.

For clarity, the last-row test is implemented as four holomorphic gap
tests, since
\[
 \begin{split}
 H_\epsilon(1)&=\Re g(\alpha)+\Re g(\beta)
       +2\pi\max(-\Im\alpha,0)+2\pi\max(\Im\beta,0),\\
 M-H_\epsilon(1)
   &=\min_{v,w\in\{0,1\}}\Re\{
       Q_\epsilon(s;\alpha,\beta)-g(\alpha)-g(\beta)
                       -2\pi iv\alpha+2\pi iw\beta\}.
 \end{split}
 \tag{8}
\]
This retains both possible endpoint growth factors exactly.

The right-tail polynomial test (10) of the contour reductions is also
checked. Its interval is divided into twelve intervals; every outward
polynomial bound is strictly below one. Thus the full right real tail
has its maximum at \(u\) or \(1\). Lemma 2 of that note gives
\(-\Re Q_{\epsilon,zz}>1/8\) throughout
\([\ell,u]+i[-h,h]\), for every neighbor in \(\mathcal Q\), and
the whole left real tail increases to \(\ell\). These are analytic
inequalities, not sampled contour tests.

The two-angle mean-value bounds in (7) retain the block dependence.
Writing \(J\) for the two-by-two Jacobian of (2), the exact implicit
derivative is
\[
 D=-J^{-1}\operatorname{diag}\left(
       \frac{2\pi i}{1-e^{-2\pi i(s+a)}},
       \frac{2\pi i}{1-e^{-2\pi i(t+b)}}\right).
 \tag{9}
\]
For a gap \(Q_\epsilon(s;a,t)-Q_\epsilon(c;a,t)\), its derivatives
with respect to \((a,b)\) are
\[
 \left(G_a+G_tD_{ta},\ G_tD_{tb}\right),\quad
 G_a=g'(s+a)-g'(c+a)+2\pi i(s-c),\quad
 G_t=g'(s+t)-g'(c+t).
 \tag{10}
\]
The selected \(s\)-derivative vanishes by the original equation. The
checker uses the analogous derivatives for the four gaps (8), multiplies
by the exact circle or edge derivatives, and integrates their outward
real-part bounds from the midpoint. For the alias test, the full real
\(x\)-interval is covered by eight intervals. These computations keep
the full affine root enclosures and do not replace them by a collection
of point values.

## 3. The complete index contour

Split the literal finite sum (3) at half-grid cuts tending to
\(\ell,u\). Uniform finite-product upper bounds on the full real
period, (7), and the tail-shape test give an exponentially smaller
contribution from every omitted real row. This includes the endpoint
\(j=N-1\), exact physical zero rows and their off-grid revival. The
uniform product upper bounds remain valid at zeros by logarithmic
regularization; a zero decreases a summand and is never divided out.
Half-grid perturbations preserve the strict margins.

On the retained rectangle the exact sine/Pochhammer interpolation gives
the literal lattice summand, and its uniform symbol is
\[
            N^{-\epsilon/2}A_\epsilon(z;\alpha,\beta)
                      e^{NQ_\epsilon(z;\alpha,\beta)}(1+O(N^{-1})).
 \tag{11}
\]
All real parts of its factorial arguments stay in \((0,1)\), so this
is an exact holomorphic interpolant before approximation.

Apply the original counterclockwise cotangent contour. Subtract its
upper/lower constants \(\mp i\pi N\). Their combined contribution
is exactly \(+N\) times the real integral from \(\ell_N\) to
\(u_N\). The remainders on the horizontal sides have the factors
\(e^{-2\pi Nh}\); on half-grid verticals their moduli are bounded by
\(CN e^{-2\pi N|\Im z|}\). Hence the horizontal remainder terms
are covered by the last line of (7).

For a vertical side, \(\Re Q_\epsilon(c+iy)-2\pi|y|\) is convex
on each half interval \([-h,0]\), \([0,h]\), because of (5) in
the contour reductions. Its endpoint values are controlled by the first
two and last lines of (7). Thus the entire original vertical alias
currents are smaller, including their parts next to the real axis.

Deform the zero-mode integral to the horizontal line through the actual
critical index. Strict real concavity gives a unique maximum there.
Each critical index is at distance at least \(.05\) from either
limiting real cut, so the endpoint loss at the critical height is at
least \((.05)^2/16=1/6400\). Height convexity bounds every connecting
vertical segment by its real and critical-height endpoints. These
segments are also smaller. The strict finite margins allow, for example,
a final common loss \(1/20000\) after rounding the cuts.

Ordinary Gaussian stationary phase on this oriented zero mode gives
exactly
\(N\cdot N^{-\epsilon/2}\cdot N^{-1/2}\) and the coefficient (4).
This proves (5) on all 42 distinguished-boundary pieces. It retains all
original contour sides and both alias signs; no moving-support contour
or untracked endpoint current is used.

## 4. Extension to every actual critical image

All factors in the normalized leading term in (5) are holomorphic and
nonzero on the full parameter product: the block branch is holomorphic,
the sine arguments are in their regular strips, and
\(\Re(-Q_{\epsilon,zz})>1/8\). Lemma 1 of the contour reductions
therefore extends the uniform normalized error from the distinguished
boundary to the whole product (1), by two maximum-modulus applications.
The same argument transports each higher-order holomorphic symbol.
This proves Theorem 1.

These are usable local germs in the independent conditional neighbors
as well. The map \((a,b)\mapsto(a,t(a,b))\) has nonzero Jacobian:
from (9),
\[
 \frac{\partial t}{\partial b}
   =-\frac{J_{ss}}{\det J}
                  \frac{2\pi i}{1-e^{-2\pi i(t+b)}}\ne0.
 \tag{12}
\]
Here \(J_{ss}=Q_{\epsilon,zz}\ne0\), \(\det J\ne0\), and the
remaining factor is nonzero on the regular strip. The local inverse
function theorem transfers the packet and its normalized derivatives to
an open neighbor set around every actual critical pair. The actual legs
lie strictly inside (1). Uniqueness of the conditional critical point
and the single canonical sum make these local germs agree on overlaps.

This closes the conditional packet-domain requirement at actual mixed
critical points. Global control of the remaining outer contours,
the explicit wrapped aliases of the exact torus identity, and the
ordinary boundary polynomials are separate requirements.

## 5. Reproduction

Run the outward certificate with:

    python3 experiments/certify_mixed_conditional_critical_images.py

Replay the saved rational witnesses independently with:

    python3 experiments/replay_mixed_conditional_critical_images.py --precision 320

The author run passed all 42 pieces with 4,838 accepted cells at 192
bits. The independent 320-bit replay passed every cell without
refinement, using original sine logarithms and cotangent differences
for the Newton witnesses and the positive-frequency dilogarithm
primitive for the action comparisons.

The record contains all accepted exact dyadic addresses, affine root
witnesses, and the explicit thresholds (7). The script checks exact
coverage separately from its analytic tests and fails on an unresolved
cell or exhausted visit budget. Numerical root proposals are accepted
only through the original complex Newton self-map. Source and proof
dependencies are hashed; no earlier localization cover is silently
recomputed or changed.
