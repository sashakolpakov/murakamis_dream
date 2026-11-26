# The complete closed half-period contribution

Research proof, 5 November 2026. The focused exact certificate
passes all 24 cases on 96 rational intervals, without subdivision.
This proves the original cyclic asymptotic on the full closed real
parameter cube \([0,1/2]^m\) of the periodic hybrid contour. It includes
zero coordinates, arbitrary adjacent zero-collar runs, both level
parities and every original Fourier selection. The other half of the
period remains outside this theorem.

## 1. Original source and statement

Fix a cyclic three/four word of length \(m\ge1\), its original
critical reference \(r\), and a collar \(0<\rho\le1/1000\) independent
of \(N\). Use exactly the selection-dependent
[periodic hybrid graph](research_mixed_split_cutoff_hybrid_contour.md).
The original allocated edge rate is
\[
 e_j(u,v)=\Re\phi_{\epsilon_{j-1},\epsilon_j}(u,v)
       +\frac{\sigma_{j-1}}2\chi(u)+\frac{\sigma_j}2\chi(v),
 \qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\},
 \tag{1}
\]
where \(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
All phases have their original zero-logarithmic lifts, chirps and
factorial allocations. Put \(M=\Re\sum_j\phi_j(r_{j-1},r_j)\).

Let \(\mathcal Z_N(D)\) denote the sum of the original selected
integrals restricted to the real parameter region \(D\), with their
unchanged scalars, carriers and graph Jacobians. Write
\(P=[.22,.45]\) and let \(\mathcal I_{N,\varnothing}(P^m)\)
be the original unselected plateau contribution.

**Theorem 1.** For every fixed word and collar, constants \(C,A\)
exist such that at all sufficiently large integer levels,
\[
 \left|\mathcal Z_N([0,1/2]^m)
              -\mathcal I_{N,\varnothing}(P^m)\right|
       \le C N^A e^{N(M-1/8000)}.
 \tag{2}
\]
Thus the complete closed-half contribution retains the proved
nonzero central coefficient, its original exponential carrier and
its original \(N^0\) normalization. No original row or selection
is removed. This does not assert the full-period asymptotic.

## 2. General-angle one-sided boundary bounds

Use
\[
 I_0=[.30,.39],\quad I_1=[.27,.33],\quad
 \nu=-J(.001),\quad\Delta=.001\log2-J(.001),\quad J=\Re g.
 \tag{3}
\]
The original height-zero profile values are
\[
 (A_{00},A_{01},A_{10},A_{11})
       =(.325066,.386681,.460764,.515591),\qquad
 (B_0,B_1)=(.325066,.515591).
 \tag{4}
\]
They bound all moving real angles, not just a neighborhood of a
particular angle, by the
[height-profile theorem](research_mixed_height_resolved_seam_sources.md).

For a left boundary with types \((\alpha,\beta)\), and a right
boundary with types \((\beta,\gamma)\), define
\[
 \begin{split}
 F^L_{\alpha\beta}(a,t)
   &=f_{\alpha\beta}(a,t)-A_{\beta\alpha}
                              -\Delta-\frac\beta2\nu,\\
 F^R_{\beta\gamma}(t,c)
   &=f_{\beta\gamma}(t,c)-B_\gamma
                              -\Delta-\frac\beta2\nu,
 \end{split}
 \qquad f=\Re\phi\quad\hbox{on real arguments}.
 \tag{5}
\]
Here \(a,c\in[.1,.5]\) and \(t\in I_\beta\).
The [seam-run scalar certificate](research_mixed_seam_run_connector_lower.md)
already encloses each individual real phase at the endpoints of
these rectangles. Let \(\mathcal I^L,\mathcal I^R\) be bilinear
interpolations of rational lower bounds for (5) at those endpoints.
Joint real concavity gives \(F^L\ge\mathcal I^L\) and
\(F^R\ge\mathcal I^R\).

We retain the exact side costs \(E_L(a),E_R(c)\) of
[the general-angle isolated-seam proof](research_mixed_general_angle_seam_replacement.md),
equation (13). Each includes the physical height-profile difference,
the neighboring coordinate's cost in its repaired seam block, and
the full reserved fee for its adjoining nonseam edge. The actual
neighbor height and repaired height are denoted \(p,h\);
the maxima include the complete triangle
\((p,h)=(0,0),(0,H),(H,H)\), all permitted height coefficients,
selections and inner cutoffs.

The unselected middle coordinate contributes only one derivative on
a single boundary edge. The
[acute gradient theorem](research_mixed_acute_gradient_height_transfer.md)
gives its signed-height costs
\[
 \begin{array}{c|cc}
 \beta&T^L_\beta(t)&T^R_\beta(t)\\\hline
 0&.01\pi&.015\pi\\
 1&.057\pi(.25-t/2)&.057\pi(.75-t/2).
 \end{array}
 \tag{6}
\]
The superscript indicates the middle coordinate's argument position.
A left boundary uses \(T^R\), and a right boundary uses \(T^L\).
Both real coordinates and all admitted middle heights are retained.

**Lemma 2.** Uniformly in types, selections and these intervals,
\[
 \begin{split}
 -\mathcal I^L_{\alpha\beta}(a,t)
             +E_L(a)+T^R_\beta(t)&<9/100,\\
 -\mathcal I^R_{\beta\gamma}(t,c)
             +E_R(c)+T^L_\beta(t)&<0.
 \end{split}
 \tag{7}
\]
These are upper bounds for the complete raw boundary source minus
its repaired coherent edge, including the reserved exterior fee.
A left boundary may have a deficit; it will be paid by the
internal edge of a nonsingleton run.

Here is the exact finite verification. Each expression in (7) is
affine in \(t\), so test its two endpoints. There are twelve left
and twelve right typed selection cases. Divide the other real
coordinate at \(.1,.12,.22,.45,.5\). On every piece the height cap
\(H=c_0R(x)L_b(x)\) is a polynomial of degree at most two.
With
\[
 K(x)=\pi\{\sigma-d(1/4-x/2)\},
 \tag{8}
\]
the two nonzero vertex options in \(E_L\) or \(E_R\) are
\[
 \begin{split}
 &(p,h)=(0,H): &&2K(x)H+\frac\pi2|H|,\\
 &(p,h)=(H,H):&&K(x)H+\frac\pi2 H_+
                         +A(H)-A(0)\quad\hbox{on the left},\\
 &&&K(x)H+\frac\pi2(-H)_+
                         +B(H)-B(0)\quad\hbox{on the right}.
 \end{split}
 \tag{9}
\]
The zero option is also retained. Each source profile is the
maximum of its affine segment extensions on its fixed selection
band. Thus (9) is the maximum of finitely many cubic polynomials.
Every combined coefficient multiplying \(\pi\) has a nonnegative
value on its permitted height band, so replace \(\pi\) by \(355/113\).
All resulting coefficients are rational.

Degree-three Bernstein coefficients on each of the 96 initial
intervals prove (7). No interval subdivision, optimization, new
root or new dilogarithm evaluation is used. Every real corner floor
is checked against its earlier outward enclosure, and every source
profile and polynomial branch is retained.
The largest certified left and right bounds are respectively
\(2357579149/28250000000<9/100\) and
\(-451093791/45200000000<0\).

## 3. An arbitrary run is paid by its internal edges

First suppose all nonseam real coordinates lie in \([.1,.5]\).
Let \(S\) be any nonempty set of seam positions, with physical
real coordinates in \([0,\rho]\). Replace all of them simultaneously
by \(\Re r_s\) and remove their selections; denote the repaired
hybrid targets by \(z^\#\). This comparison changes no integration
variables.

An internal SS edge has two real physical low arguments. Its raw
rate is
\[
 U^{SS}_{\eta\epsilon}
       =\epsilon/6+2\Delta+(\eta+\epsilon)\nu/2.
 \tag{10}
\]
The seam-run theorem proves that its repaired unselected coherent
rate exceeds (10) by \(1/3\), for arbitrary admitted partial
height resets of either endpoint. Both repaired real coordinates
are their original reference real parts. Every low numerator factor,
both Fourier halves, and both level parities are included in (10).

A proper maximal run of \(k\ge2\) seam positions has \(k-1\)
internal edges, one left boundary and one right boundary.
Adding (7) and (10), including the two full exterior fees, gives
raw-minus-repaired defect at most
\[
 \frac9{100}-\frac{k-1}{3}\le-\frac{3k}{1000}.
 \tag{11}
\]
Indeed the difference between the left-hand reserve and \(3k/1000\)
is \((991k-1270)/3000>0\) for \(k\ge2\).

A singleton run instead uses Lemma 2 of the general-angle
isolated-seam proof: its two incident edges, plus both exterior
fees, have defect at most \(-3/1000\). This local inequality does
not require that other, disjoint runs be singletons. Its allowed
height triangles already contain simultaneous changes caused by
another seam at distance two.

If \(S\) is the entire cycle, every edge is SS and every repaired
target is exactly its reference. The loss is \(m/3\), which is
larger than \(3m/1000\); no artificial run boundary is introduced.

Each remaining AA-edge height change is paid by its adjacent
boundary fee. A nonseam vertex with one seam neighbor has at most
one AA incidence, and a vertex with two seam neighbors has none.
The fees are nonnegative, so reserving fees for absent incidences
is harmless. When both endpoints of one AA edge change, telescope
the rate once through an intermediate target. The one-real-endpoint,
other-complex acute-gradient bound used for the fees is uniform on
the admitted products, so the two incidence fees bound that single
edge difference.

Consequently, before finite-source tolerances,
\[
 \text{raw/coherent physical upper rate}
       \le\sum_j e_j(z^\#_{j-1},z^\#_j)-3|S|/1000
       \le M-3|S|/1000.
 \tag{12}
\]
The last step is the proved deep-half phase bound. Counts refer to
physical edges: a one-cycle with a seam has one diagonal SS edge;
a two-cycle with one seam has two distinct boundary edges. Shared
nonseam vertices and arbitrary adjacent runs introduce no duplicate
Fourier factors or boundary charges.

## 4. Raising other deep-low coordinates preserves an upper envelope

Now allow every nonseam coordinate in the full interval
\([\rho,.5]\). Construct the physical finite-source upper envelope
edge by edge:
SS edges use (10), SA edges use their complete angle-uniform
height-profile ceilings with the seam collar cost, and AA edges
use the established coherent rate (1).

Raise each nonseam coordinate below .1 to .1, leaving the seam
coordinates fixed for this step. This motion stays inside the zero
interval of both slow and fast left cutoffs. Every height is
unchanged: the moving row has its own zero cutoff even though its
own right factor varies, and all neighboring rows see the same
zero cutoff throughout the motion.

For an AA edge incident to a raised coordinate, both arguments
are real. The selected corrections vanish there, since
\(J(x)\le0\) and the selected monomial has unit modulus,
so its logarithmic rate is zero.
The [real low-coordinate monotonicity lemma](research_mixed_deep_low_half_region.md),
Lemma 1, shows that its original coherent phase increases when
either real argument is raised through .1.

No monotonicity of a seam-incident finite kernel is claimed.
Its angle-uniform source ceiling is unchanged: a raised neighboring
coordinate has height zero before and after, and the height-profile
theorem covers every moving real angle in \([0,1]\). SS ceilings
are also unchanged. Thus the mixed raw/coherent upper envelope
can only increase under this raising. Apply (12) to the raised
configuration and then the simultaneous seam replacement.
This proves (12) for all nonseam coordinates in \([\rho,.5]\).

The complete packets on original AA edges are already available.
An edge incident to a deep-low nonseam coordinate has both targets
real in the fixed compact square \([\rho,.5]^2\); the closed
real half-endpoint theorem applies. Every other AA edge is in
the proved nonlow complex source polygons. The argument does not
extend a packet to a physical zero coordinate: those edges were
bounded throughout by literal raw sources.

## 5. The full closed cube and its coefficient

For a real parameter vector in \([0,.5]^m\), let
\(S=\{j:x_j<\rho\}\). The boundary choice at \(x_j=\rho\) has
no effect on the integral, and all estimates hold on the corresponding
closed pieces. If \(S\ne\varnothing\), choose the total finite-source
tolerance below \(1/1000\). Equation (12) leaves loss at least
\[
                   3|S|/1000-1/1000\ge |S|/500.
 \tag{13}
\]
This is uniform down to zero for every fixed collar. Restoring the
original Fourier weights once, their unchanged scalars/carriers,
and the bounded hybrid Jacobian gives
\[
 \left|\mathcal Z_N\{x:\text{some }x_j<\rho\}\right|
                         \le C N^A e^{N(M-1/500)}.
 \tag{14}
\]
There are finitely many seam sets and selections for a fixed word;
their sums are absorbed in \(C\). Polynomial factors are also
absorbed in \(N^A\).

For \(S=\varnothing\), the
[deep-low half-region theorem](research_mixed_deep_low_half_region.md),
Theorem 2, already gives
\[
 \left|\mathcal Z_N([\rho,.5]^m)
           -\mathcal I_{N,\varnothing}(P^m)\right|
                         \le C N^A e^{N(M-1/8000)}.
 \tag{15}
\]
Adding (14) and (15) proves Theorem 1. It retains the exact original
central asymptotic and every Fourier correction. It is not a
replacement integral, an asymptotic inferred solely from a root,
or a claim of noncancellation on the entire real period.

Reproduction:

    python3 experiments/check_mixed_closed_half_period.py
    python3 experiments/check_mixed_closed_half_period.py --input repro/results/research-mixed-closed-half-period.json --output /tmp/research-mixed-closed-half-period-review.json
