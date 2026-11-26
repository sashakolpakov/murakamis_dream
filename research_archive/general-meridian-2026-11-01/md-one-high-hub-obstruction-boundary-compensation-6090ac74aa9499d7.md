# Boundary compensation for the one-high valence-nine obstruction

Private derivation, 1 November 2026. No repository changes.

The exact family in `/private/tmp/md-one-high-admissible-hub-trace-exponential-obstruction.md` disproves a pointwise comparison with the complete tensor at the same indices. It does not exceed the actual geometric pressure when the nine boundary inputs have ordinary rigid profiles. This note records that distinction with the original pressure, and records the separate complete-pressure argument that can be used for more general neighboring regions.

## 1. A whole-junction upper bound at the obstruction indices

Use the fixed complete Newton polynomials \(e_r\), the moving quotient \(P_s\), and the full trace \(\phi_s\). The complete spectral norm \(\mathcal J\) includes first normals. The already proved finite estimates give
\[
 \|e_h\|_{\mathcal J}\le N^C\quad(h>\lfloor(N-1)/2\rfloor),
 \qquad
 \|e_a\|_{\mathcal J}\le N^C e^{Ng(a/N)+O(\log N)}
                                  \quad(a\text{ low}).
\tag{1}
\]
Canonical Hermite interpolation converts these bounds to sup norms on \([-2,2]\) at polynomial cost. For a fixed number of factors, raw polynomial multiplication therefore has that same additive exponential cost. The canonical remainder bound for \(P_s\), followed by its top-coefficient functional, gives
\[
 \sup_{|s|\le R}\left|\phi_s\left(e_he_a^8\right)\right|
                  \le N^{C_R}e^{8Ng(a/N)},\qquad R<1.
\tag{2}
\]
This step uses the proved bounded-degree Chebyshev folding and polynomial norm conversion, not a moving-versus-complete trace comparison. Equivalently it is the high-probe estimate in `notes/actual_main_meridian_source_bounds.md`, Section 3.4, before maximizing the eight low input weights. All first normals and fixed-quotient reductions are retained.

For \(N=5a+1,h=4a\), (2) has rate \(8g(1/5)\). The positive correction in the counterexample can be exponentially larger than its particular complete trace while still obeying this absolute upper bound.

Now attach nine actual or effective boundary modules with the original cone
\[
 |f_{i,N,r}|\le e^{N(c_i+o(1))}
 \begin{cases}e^{Ng(r/N)},&r\text{ low},\\1,&r\text{ high}.
 \end{cases}
\tag{3}
\]
At the specified tuple, the high boundary contributes no positive profile and the other eight contribute \(g(a/N)\) each. Thus its whole weighted contribution, uniformly on the compact meridian disk, has rate at most
\[
                  \sum_{i=1}^9c_i+16g(1/5).
\tag{4}
\]
There is no assertion here that the physical high coefficient is nonzero. If it vanishes, the contribution is smaller still.

## 2. Comparison with the same original pure action

The complete positive reference of this nine-boundary junction is the original scalar \(C(h^9)\), with its constants retained. Choose any one existing boundary as the comparison root; the other eight form the unturned product \(A=h^8\). Let
\[
 \omega_8=\max_{x\le1/2}\{f_8(x)+g(x)\},
 \qquad
 \widehat\omega_8=\max_{x\le1/2}\{f_8(1-x)+g(x)\}.
\tag{5}
\]
The old positive product evaluation gives \(\omega_8=16G_0\), where \(G_0=g(1/4)\). The reflected product-pressure theorem gives
\(\widehat\omega_8>\omega_8\). These are exactly equations (H5)–(H13) in `notes/actual_main_meridian_source_bounds.md`, Sections 3.1–3.2; they are pressure identities of the same positive source, not a sum of independent cap volumes.

Consequently the original complete pressure is
\[
                  F_0=\sum_i c_i+\widehat\omega_8
                         >\sum_i c_i+16G_0.
\tag{6}
\]
Since \(g'(x)=2\log\cot(\pi x)\), its unique maximum on \([0,1/2]\) is at \(1/4\). Hence
\[
 \delta_*:=16\{G_0-g(1/5)\}>0,
 \qquad
 \sum_i c_i+16g(1/5)<F_0-\delta_*.
\tag{7}
\]
The exact counterexample family is therefore exponentially negligible relative to the actual complete geometric budget in this rigid-boundary setting. The already established singleton-hub theorem supplies an even stronger uniform gap for all high boundary tuples. Formula (7) merely exhibits the compensation at the particular witness without changing any boundary labels or introducing a new geometric component.

A sufficiently small fixed neighborhood of the tuple has the same conclusion after reducing \(\delta_*\), by continuity of \(g\) and the closed basis estimates. This statement concerns the rigid low/high boundary cone (3). It is not a comparison to the much smaller complete trace at the identical tuple.

## 3. What changes for a neighboring nonrigid branch

If the high incidence comes from an adjacent completed bare region rather than an L module, its boundary action is not generally the high constant in (3). For example, attaching an old two-leaf product across the physical turn gives the original boundary profile
\[
                        f_{hh}(1-u)
\tag{8}
\]
at covariant high label \(u\), with all its own ordinary leaf contributions retained. It cannot be replaced by its independently maximized norm pressure without accounting for the shared boundary condition. Equations (4)–(7) do not make that replacement.

The coupled complete-pressure comparison in `/private/tmp/md-old-whole-hub-simultaneous-half-pressure.md` does apply to such an old region if all its marked high boundaries are treated jointly. Its hypotheses are: actual hubs have full valence at least three; internal edges are physical turns; at most one marked incidence occurs at each hub; the other boundaries carry the original \(g+c\) profiles. It proves
\[
                     \Psi(\mathbf z)\le\Psi(\tfrac12\mathbf1)
                          \quad(\mathbf z\ge\tfrac12\mathbf1),
\tag{9}
\]
strictly away from the all-half vector. It concerns the complete positive action. A separate moving higher-valence estimate is still required to sew the additional terms at the boundary.

I checked its full derivation against the exact fixed-label support lemma in `notes/actual_conway_reduced_hub_source_normal_form.md`, Section 2. The product interval is
\(\max_i a_i<b<\min(1,\sum_i a_i)\), with pairwise input sums less than one. The extra condition involving the exposed root label enters only when the product is closed. The half/three-eighths assignment is made on physical edges; the fixed-association interval construction supplies every hidden unturned wire. The endpoint descent handles both turn and unturned edges, and the strict gate Hessians give the analytic boundary pressure with negative definite Schur complement. The response induction passes proper product outputs through either edge type and never turns an uncompleted ordinary boundary leaf. Its supporting-gradient calculation therefore proves (9) without an independent-cap substitution.

This supplies a valid coupled tool for a neighboring complete region, but does not yet show how to replace the valence-nine moving tensor by a complete tensor with compatible boundary profiles. The pointwise inequality has been disproved; the actual coupled geometric comparison remains a different question.
