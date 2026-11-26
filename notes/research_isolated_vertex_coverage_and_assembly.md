# Isolated fillings: the boundary theorem and its finite coverage

The original source at one filled vertex has a full boundary theorem
for every integer degree and signed power satisfying
\(d+|n|>2\). Its inputs include all terminal powers, every nonzero
degree-two power, every zero power at degree at least three, the
existing large-degree or large-power theorem, and a completed
certificate for the remaining 6,369 positive parameter pairs.

Every pair passed all nineteen contour domains. The independent
archive check then verified the complete integer coverage, every
rational subdivision and all proof-engine hashes. The resulting
theorem concerns one original filled vertex with all its neighbors
left open. It does not supply a theorem for arbitrary adjacent
short-filled regions.

## 1. The source and the coverage set

Use the original complete algebra and Frobenius trace
\[
 \mathcal A_N=\mathbb C[z]/P_N(z),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=N-1}.
 \tag{1}
\]
Here \(T_N\) is the standard Chebyshev polynomial and \(e_i\) is
the original Newton basis. Equivalently,
\[
 \phi_N(f)=(-1)^{N-1}N^2[z^{N-1}]
                         \operatorname{rem}_{P_N}f.
 \tag{2}
\]
Repeated roots and their first normal derivatives are retained.
Set
\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u),\qquad
 P_{d,n,N}(\mathbf u)=
 \phi_N^{(t)}\left[R^n\prod_{j=1}^{d}K_N(t,u_j)\right].
 \tag{3}
\]
The degree \(d\ge1\), signed power \(n\), and all physical
markings are fixed before \(N\to\infty\). The outside variables
\(\mathbf u=(u_1,\ldots,u_d)\) are independent. The polynomial
has degree at most \(N-1\) in each \(-2\cos u_j\).

The selected positive isolated geometry exists exactly when
\[
                             d+|n|>2.
 \tag{4}
\]
Define the remaining positive parameter set
\[
 \mathscr R=
 \{(d,n)\in\mathbb Z^2:
       d\ge3,\ n\ge1,\ d^2+n^2<\max(1024,128d)\}.
 \tag{5}
\]
It has 6,369 elements, all in \(3\le d\le127\),
\(1\le n\le63\). Let \(\mathscr C\subseteq\mathscr R\)
denote the pairs with a completed successful report from
[the parameterized certificate](research_generic_isolated_contour_certificates.md),
including every required surface, root, Hessian and tail
inequality. A numerical root proposal, a partial report, or
a successful neighboring pair does not put a pair in
\(\mathscr C\).

The covered set \(\mathscr V\) consists of:

| Original degree and power | Complete boundary-source proof |
|---|---|
| \(d=1,\ |n|\ge2\) | [all terminal powers](research_uniform_terminal_family_and_star_fillings.md) |
| \(d=2,\ n\ne0\) | [every nonzero degree-two power](research_all_nonzero_degree_two_fillings.md) |
| \(d\ge3,\ n=0\) | [the zero-power theorem](research_zero_power_internal_boundary_theorem.md), also the singleton case of the [zero-subtree theorem](research_all_zero_subtree_newton_packet.md) |
| \(d\ge3,\ n\ne0,\ d^2+n^2\ge\max(1024,128d)\) | [the degree-and-power theorem](research_high_degree_short_internal_vertex.md) |
| \((d,|n|)\in\mathscr C\) | the successful finite certificate and [trace-first lifting](research_scaled_wire_contour_lifting.md) |

The completed exhaustive run is recorded in
[its manifest](../repro/results/research-isolated-scaled-all-manifest.json).
The [independent archive check](../repro/results/research-isolated-scaled-all-integrity.json)
verifies all 6,369 pairs, all 121,011 surface domains and their
6,389,640 accepted rational boxes. Consequently
\(\mathscr C=\mathscr R\), and the table covers exactly every
integer pair satisfying (4).

## 2. The assembled boundary theorem

The original geometric action is
\[
 G_{d,n}(\mathbf u)=
 \operatorname{stat}_{t}
 \left[\sum_{j=1}^{d}\psi(t,u_j)+\frac{int^2}{4\pi}-it\right],
 \quad
 \psi(0,0)=M_\infty=\frac{4G}{\pi},
 \tag{6}
\]
on the positive primitive cone branch; \(G\) in \(4G/\pi\)
is Catalan's constant. The continued edge derivative is
\[
 \psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}(\tan(t/2)\cos(u/2)).
 \tag{7}
\]
Let \(t_{d,n}\) be the selected critical angle at
\(\mathbf u=0\), and \(M_{d,n}=\Re G_{d,n}(\mathbf0)\).

**Theorem 1.** For every integer \(d\ge1\), \(n\in\mathbb Z\)
with \(d+|n|>2\), the
original polynomial (3) has
\[
 P_{d,n,N}(\mathbf u)
 =\epsilon_{d,n,N}N^{-3(d-1)/2}
       A_{d,n}(\mathbf u)e^{NS_{d,n}(\mathbf u)}
                                  (1+O_{d,n}(N^{-1}))
 \tag{8}
\]
on a fixed complex polydisk about zero, through both
parities of the level. The amplitude is holomorphic and
nonzero. The normalized error is holomorphic, with the
same order for fixed derivatives on smaller polydisks.
The phase is separately even and satisfies
\[
 dS_{d,n}=dG_{d,n},\qquad
 \Re S_{d,n}(\mathbf0)=M_{d,n},\qquad
 (S_{d,n})_{u_i u_j}(\mathbf0)
    =-\delta_{ij}\frac{\cos(t_{d,n}/2)}{2\pi}.
 \tag{9}
\]
Its real Hessian is negative definite. There are
positive constants \(c,B,b,C\) and a finite exponent
\(a\), allowed to depend on the fixed pair, such that
\[
 |P_{d,n,N}(\mathbf x+i\mathbf y)|
 \le CN^a\exp N\left\{
 M_{d,n}-c\sum_{j=1}^{d}(1-\cos x_j)
                       +B\sum_{j=1}^{d}y_j^2\right\}
 \tag{10}
\]
for \(|x_j|\le\pi\), \(|y_j|\le b\).

The exact phases and unit scalars in (8) may be chosen
by the following table. Put \(D=N-1\) and
\(C_{N,n}=\exp(\pi i nD^2/(4N))\), using the stated
logarithm of \(q=e^{\pi i/N}\).

| Pair | \(S_{d,n}\) | \(\epsilon_{d,n,N}\) |
|---|---|---|
| \(d\ge3,\ n=0\) | \(G_{d,0}\) | \(1\) |
| \(d\in\{1,2\},\ n=2\sigma,\ \sigma=\pm1\) | \(G_{d,2\sigma}\) | \(e^{\sigma i\pi N/2}\) |
| \(d=2,\ n=\sigma=\pm1\) | \(\psi(u_1,u_2)-\sigma i(u_1^2+u_2^2)/(4\pi)\) | \(1\) |
| All other covered nonzero pairs | \(G_{d,n}\) | \(C_{N,n}\) |

The unit-power row uses the
[direct geometric derivative comparison](research_degree_two_unit_power_geometry.md);
its action differs from \(G_{2,\sigma}\) only by a purely
imaginary constant. No unknown constant has been assigned
to its quantum normalization. At powers \(2\sigma\) in
degrees one and two, the exact imaginary shift from the
direct source phase is known and is displayed in the scalar.
These exceptional conventions are retained when blocks
are multiplied or filled further.

**Coverage.** The equality \(\mathscr C=\mathscr R\) has been
verified by the exhaustive certificate and the separate
archive check. Together with the other rows of the table,
it proves the stated full range (4). No assertion for an
untested parameter or a neighboring knot is used.

## 3. Normalization, including zero power

The power of \(N\) in (8) is the same in all rows.
This is a normalization statement about the original
trace, not a change of source.

For a nonzero pair treated by the scaled contour,
the original trace has factor \(N^2\). Its \(d\)
wire sums have factor \(N^d\); their \(d\) Newton
products have factor \(N^{-2d}\); the joint Gaussian
has \(d+1\) variables. Thus
\[
 N^2N^dN^{-2d}N^{-(d+1)/2}
                             =N^{-3(d-1)/2}.
 \tag{11}
\]
At complete parents its leading coefficient is
\[
 \frac{i(2\pi)^{(d+1)/2}}{\pi4^d}
 \frac{\sin t_{d,n}}
      {\sin^{2d}(\pi x_{d,n})\sqrt{\det(-H_{d,n})}},
 \tag{12}
\]
where \(H_{d,n}\) is the full Hessian in the \(d\)
wire variables and the trace angle, with the convergent
Gaussian branch. The lifting theorem proves this
coefficient is nonzero. The small-saddle proof gives
the same power by first taking the \(d\) edge
Gaussians and then the angular Gaussian.

At zero power, for \(d\ge3\), the full-circle proof
uses
\[
 h_d=2\operatorname{arsinh}\tan(\pi/d),\qquad
 t_{d,0}=-ih_d.
 \tag{13}
\]
Its \(d\) full edge factors contribute \(N^{-3d/2}\),
the original trace \(N^2\), and its one angular Gaussian
\(N^{-1/2}\). The result is again (11). There is no
crossing chirp and \(C_{N,0}=1\). Its explicit positive
coefficient is
\[
 A_{d,0}(\mathbf0)=
 \frac{4^{1-d}}{\sqrt d}\tan\frac\pi d
                  \left(\sec\frac\pi d\right)^{(3-d)/2}.
 \tag{14}
\]
For \(d=3\) this gives \(A_{3,0}=1/16\) and the
power \(N^{-3}\).

The primitive Newton theorem checks the same normalization
independently. For a singleton zero-filled region the
number \(b\) of outgoing edges is exactly \(d\), so
its exponent \(N^{-3(b-1)/2}\) is (8). More explicitly,
there are \(d\) leaf densities of order \(N^{-1}\),
\(d-2\) product densities of order \(N^{-3/2}\),
and \(2d-3\) primitive lattice coordinates. Summation
and their Gaussian give \(N^{(2d-3)/2}\). Hence
\[
 -d-\frac32(d-2)+\frac12(2d-3)
                             =-\frac32(d-1).
 \tag{15}
\]
The complementary Frobenius pairing in (1) already
includes the normalization (2); no additional \(N^2\)
is inserted into (15). Its primitive lattice has
covolume one. Both level parities and the actual
\(D=N-1\) offsets are retained by that theorem.

The special degree-three zero-power argument is essential.
The elementary omitted-wire envelope has zero strict gap
there. The zero-source theorem instead proves the missing
gap from positive Newton multiplication, including its
high-index sector. It is not an application of the
nonexceptional uniform wire-gap bound.

Finally, the terminal row has exponent \(N^0\),
as (8) requires at \(d=1\). The exact unit-power
degree-two reduction starts from the bare-edge factor
\(N^{-3/2}\); canonical boundary multiplication
preserves that factor. These check the remaining
normalizations in the table.

## 4. What an accepted finite report supplies

For \((d,n)\in\mathscr C\), the full
[generic certificate proof](research_generic_isolated_contour_certificates.md)
first identifies the selected root of
\[
          (-i)^d(w+i)^d+w^n(w-i)^d=0,\qquad
          w=e^{it/2}.
 \tag{16}
\]
The root is certified by Rouché's theorem on an
exact rational disk. A separate logarithmic residual
fixes the original unit angular charge. The literal
phase derivatives are also enclosed in a disk that
excludes every nonzero logarithmic winding.

Along the positive cone path, write \(t=2a-2ib\) and
\(\arctan\cos(a-ib)=\theta+i\beta\).
For \(d\ge3,n>0\) the real cone equations give
\(a<\pi/4\), and
\[
 \tanh(2\beta)
 =\frac{2\sin a\,\sinh b}{\cosh^2b+\cos^2a}
 \le\tan a\,\tanh b<\tanh b.
 \tag{17}
\]
Thus the two trace factorial arguments stay on their
original opposite sides of the cut throughout the
path. Their positive real parts at the selected
endpoint are verified separately. This fixes the
absolute action continuation without assuming a
bulk condition along the entire path.

The nineteen inequalities control the main horizontal
maximum and Hessian, negative real trace angles,
lower-wire aliases, angular endpoints, wire endpoints
and their independently raised nested combinations.
The shared trace charge remains once, while every
wire penalty is multiplied by \(d\) in the scaled
phase. Exact averaging then controls all \(d\)-wire
combinations. The original rational Fourier weights
and endpoint currents remain in the finite identity.

For the common interval \([1/128,63/128]\),
[the uniform wire-gap theorem](research_uniform_isolated_wire_gap.md)
gives a strict omitted-index gap greater than \(1/60\).
[The outer-angle theorem](research_all_degree_outer_angle_gap.md)
gives a strict real trace gap greater than \(d/30\)
at \(|t|\ge2\pi/3\), for every retained subset.
These are estimates before taking the original
normal trace. Uniform reciprocal-factorial bounds
handle the moving zeros; exact degree bounds extend
the discarded terms to a small complex boundary disk.
The accepted report and the lifting theorem therefore
prove (8)--(10) for the original full polynomial,
not a retained model.

## 5. The original geometric meaning

For every pair in \(\mathscr V\), the original
[isolated-vertex construction](research_isolated_internal_vertex_geometry.md)
has a positive primitive cone path. If the original
carrier is \(\eta\in\{-1,0,1\}\) and
\(n=\eta-2p\), its periods satisfy
\[
 U=-2\pi\sum_{j=1}^{d}\psi_t(t,u_j)-i\eta t,
 \qquad V=2it,\qquad
 U+pV=-2\pi i\lambda .
 \tag{18}
\]
The longitude is primitive and occurs once; it is
not multiplied by the degree. All neighboring cusps
remain complete at \(\mathbf u=0\). The old face
pairings and their logarithmic winding are retained.

At charge zero the \(d\) original edge blocks
contribute \(2d\) regular ideal octahedra, giving
volume \(2\pi dM_\infty\). The core length is
\(-2\Im t(\lambda)>0\), and the stationary-value
derivative is \(\Im t(\lambda)\). Schläfli's formula
therefore gives the absolute filled volume
\[
                        2\pi M_{d,n}.
 \tag{19}
\]
Equations (9) identify the outside period derivatives
with the source phase. The complete geometry and all
outside boundary maps extend holomorphically on a
small fixed polydisk. At degree two and unit power,
the direct geometric lemma keeps the same original
core and boundary labels; drawing its reduced
diagram still requires the proper half-turn and
both neighboring crossing shifts.

## 6. A consequence that does not require adjacent short fillings

Consider a fixed original marked circle tree, with
its original component and framing conventions.
Choose an independent set \(S\) of vertices, leaving
at least one free vertex. At each \(s\in S\), fix a
power satisfying \(d_s+|n_s|>2\), with its prescribed
carrier parity.
Let \(r\) be the number of free vertices, and \(e_0\)
the number of original edges with both ends free.
Exact summation of the selected vertices leaves
\[
 \prod_{\substack{vw\in E\\v,w\notin S}}K_N(t_v,t_w)
 \prod_{s\in S}P_{d_s,n_s,N}((t_w)_{w\sim s}).
 \tag{20}
\]
Shared free boundary variables remain shared in
this formula. Because selected vertices are not
adjacent, no original edge is used twice.

The local phase is the sum of the known edge and
boundary phases. Their nonzero amplitudes multiply,
and every free variable receives positive real
curvature from an incident factor. Their global
angular losses add with those same shared variables.
The degree in a free spectral variable can exceed
\(N-1\); the original full trace handles that product
without first replacing it by distinct-node values.

The tree count gives
\[
 e_0+\sum_{s\in S}(d_s-1)=r-1.
 \tag{21}
\]
Hence (20) has factor \(N^{-3(r-1)/2}\).
The proved
[further-filling theorem](research_long_fillings_complex_boundary_phase.md)
applies when the remaining fixed signed powers are
independently sufficiently long. Its \(r\) original
traces contribute the net factor \(N^{3r/2}\);
the final invariant has a nonzero \(N^{3/2}\)
leading coefficient, with all displayed unit
scalars and writhe factors retained. The marked
positive charts and (18)--(19) identify its real
action with the hyperbolic knot-complement volume,
provided the original strand tracing gives one knot.

This consequence allows every isolated pair satisfying
(4) in that independent set. The remaining-power
threshold may depend on the fixed tree and its selected
powers.

Two adjacent selected vertices do not give the product
in (20): they share an internal kernel and its
summation variable. Their joint source needs its own
proof. Therefore the theorem does not remove all infinite
short-coordinate slices of a fixed template. The
finite-exception problem still requires control of
those connected short-filled regions.
