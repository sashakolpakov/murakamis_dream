# Verified terminal fillings followed by independent long fillings

Research theorem, 2 November 2026. This combines the proved boundary
asymptotics for every fixed terminal power of magnitude at least two
with the filling theorem for a general complex boundary phase.
All crossing powers are fixed before the level tends
to infinity. Frozen manuscripts are unchanged.

## 1. The marked diagrams and the statement

Let \(\mathcal T=(V,E)\) be a fixed finite ordered circle tree with at
least one edge, using the original tangle stacks, quarter-turns,
disk frames, strand orientations, reduced cut, and cylindrical
closure of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
There are no unrecorded product junctions. At each vertex retain its
original carrier

\[
\eta_v\in\{-1,0,1\},
\qquad n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z.
\]

The filled primitive slope is \(\mu_v+p_v\lambda_v\). Fix a parity
pattern whose actual strand tracing produces one main component and
no internal closed component.

Choose a subset \(\mathcal L\) of the **original terminal vertices**,
leaving at least one vertex. At each selected leaf fix a physical
power

\[
n_\ell\in\mathscr A
:=\{n\in\mathbb Z:|n|\geq2\},
\qquad n_\ell\equiv\eta_\ell\pmod2.
\]

In particular, powers \(\pm2\) have carrier zero, while powers
\(\pm3\) have their prescribed odd carrier. No carrier is changed
when the corresponding leaf is eliminated. Put

\[
V_0=V\setminus\mathcal L,\qquad
E_0=\{vw\in E:v,w\in V_0\},\qquad
r=|V_0|,\qquad e_0=|E_0|=r-1.
\]

For \(\ell\in\mathcal L\), write \(v(\ell)\in V_0\) for its unique
remaining neighbor.

**Theorem.** There is a finite threshold \(B\), depending on the
fixed marked tree and the chosen fixed terminal powers, such that
every assignment of remaining powers

\[
n_v\equiv\eta_v\pmod2,\qquad |n_v|\geq B
\qquad(v\in V_0)
\]

produces a hyperbolic knot \(K\) and satisfies

\[
\langle K\rangle_N
=\Omega_N N^{3/2}D\,e^{NS}
 \left(1+O_{\mathbf n}(N^{-1})\right),
\qquad |\Omega_N|=1,\qquad D\ne0,
                                                        \tag{1}
\]

through all sufficiently large integer levels, with

\[
2\pi\Re S=\operatorname{Vol}(S^3\setminus K).
                                                        \tag{2}
\]

The remaining powers have independent signs and magnitudes.
Their parities remain the originally prescribed ones. The threshold
is not claimed to be uniform over different marked trees or over
different choices of the fixed terminal powers.

The selected leaves must be original leaves. The statement does not
apply successively to vertices that become terminal after another
short filling unless their new joint source has also been proved.
It also does not give a finite-exception theorem for all assignments
on a fixed tree.

## 2. The finite source and the verified analytic inputs

Let \(q=e^{\pi i/N}\), \(d=N-1\), and use the original complete
Newton basis and closing functional. Define

\[
K_N(t,u)=\sum_{k=0}^{d}e_k(-2\cos t)e_k(-2\cos u),
\qquad
H_{n,N}(u)=\sum_{k=0}^{d}\phi(R^n e_k)e_k(-2\cos u).
\]

Exact summation at each chosen terminal leaf leaves the polynomial

\[
B_N(\mathbf t)=
\prod_{vw\in E_0}K_N(t_v,t_w)
\prod_{\ell\in\mathcal L}H_{n_\ell,N}(t_{v(\ell)}).
                                                        \tag{3}
\]

This is an identity in the original finite contraction. It retains
every index and every normal derivative at a repeated spectral
root. The separate degree in \(-2\cos t_v\) is at most
\((\deg_{E_0}v+\#\{\ell:v(\ell)=v\})(N-1)\); this raw polynomial
is not reduced before estimating it.

The relevant source theorems are:

| Fixed terminal power | Boundary theorem |
|---|---|
| \(\pm2\) | [Two-crossing terminal filling](research_two_crossing_terminal_filling.md) |
| \(\pm3\) | [Three-crossing terminal filling](research_three_crossing_terminal_filling.md) |
| \(4\leq |n|\leq31\) | [The common finite-range theorem](research_terminal_powers_four_through_thirty_one.md) |
| \(|n|\geq32\) | [Large fixed terminal powers](research_terminal_large_fixed_powers.md) |

Each theorem concerns the whole finite polynomial. It gives a
nonzero holomorphic leading amplitude on a fixed disk, with a
holomorphic relative \(O(N^{-1})\) error, and a bound

\[
|H_{n,N}(a+ib)|
\leq C_nN^{A_n}
 \exp N\{M_n-c_n(1-\cos a)+B_nb^2\}
                                                        \tag{4}
\]

on a fixed thin strip about the entire real angular period.
For every fixed terminal power in \(\mathscr A\), the leading power
of \(N\) is zero.

The full edge kernel also has a nonzero holomorphic expansion

\[
K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                 (1+O(N^{-1}))
                                                        \tag{5}
\]

on a sufficiently small fixed bidisk, together with a global
angular loss in both variables. Here

\[
\psi(0,0)=\frac{v_{\rm oct}}{\pi},\qquad
\psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}(\tan(t/2)\cos(u/2)).
\]

For clarity, the passage from the retained edge theorem to the full
kernel in (5) is harmless but must be made explicitly. The
[edge theorem](../papers/circle-tree-volume/edge-packet.tex)
uses \(k/N\in[1/5,3/10]\). The
[finite norm estimates](../papers/circle-tree-volume/finite-bounds.tex)
bound its complementary polynomial, uniformly on the whole real
angular square, at rate at most
\(\psi(0,0)-\pi/100\). Chebyshev continuation costs at most
\(N(|\Im t|+|\Im u|)\) in its exponent. Hence that complement
remains exponentially smaller on a sufficiently small fixed bidisk,
giving (5). On a thin strip, combine the retained angular bound
with this fixed complementary loss and decrease the angular
constant. This proves the corresponding full-kernel strip bound.

## 3. The geometric branch for every selected terminal power

The geometry needed here is valid for every fixed \(|n|\geq2\).
The argument below treats the whole range at once.

First take \(n>0\), keep the parent boundary complete, and write
\(t=2a-2ib\). The primitive cone equations with parameter
\(\lambda\in[0,1]\) are

\[
\sin a=\cosh b\,\tanh(nb),
\qquad
na+\arctan\frac{\sinh b}{\cos a}=\pi\lambda.
                                                        \tag{6}
\]

These are the unexponentiated equations
\(\psi_t(t,0)+int/(2\pi)=i\lambda\), on the logarithm
continued from the complete structure.

For every \(0<a<\pi/2\), the first equation has a unique
\(b=b_n(a)>0\), increasing with \(a\). The left side of the
second equation is strictly increasing from zero to
\((n+1)\pi/2\). Since \(n\geq2\), it takes every value
\(\pi\lambda\), \(0<\lambda\leq1\), at a unique interior
point. In particular \(a<\pi\lambda/n\), and \(b>0\).

Put

\[
w=e^{it/2}=e^{b+ia},\qquad
R_0=\sec(t/2)+\tan(t/2)
   =\frac{\cos a-i\sinh b}{\cosh b-\sin a}.
\]

Both \(w\) and \(R_0\) have positive real part. The eight oriented
tetrahedron shapes in the original two-octahedron edge block are

\[
(iR_0,iw,i/R_0,i/w),\qquad
(i/R_0,iw,iR_0,i/w).
                                                        \tag{7}
\]

Every shape has positive imaginary part. These are the same
ordered shapes and rational face identifications used in
[the two-crossing geometric proof](research_two_crossing_terminal_filling.md#8-the-original-marked-geometric-action);
their formulas do not depend on the crossing power. The power
enters the primitive filling equation (6).

The original marked identities retain the carrier:

\[
U=-2\pi\psi_t-i\eta t,\qquad V=2it,\qquad
U+pV=-2\pi\left(\psi_t+\frac{in}{2\pi}t\right),
\qquad n=\eta-2p.
                                                        \tag{8}
\]

Consequently (6) gives primitive cone angle \(2\pi\lambda\)
and positive core length \(-2\Im t\). This uses the original
integer \(p\) and primitive curve \(\mu+p\lambda_{\rm long}\),
where \(\lambda_{\rm long}\) denotes the marked longitude.
The carrier is not replaced by a principal-logarithm choice.
The complete-parent periods remain zero because
\(\psi_u(t,0)=0\).

The full logarithmic periods are continued from the complete
structure along (6), using the face pairings and the log-link
construction of the
[geometric paper](../papers/circle-tree-geometry/main.tex).
More precisely, its equations \(\texttt{ctg:pants}\),
\(\texttt{ctg:primitive-words}\), and \(\texttt{ctg:increment}\)
give the ordered face identifications and original meridian
multipliers. Its equation \(\texttt{ctg:log-link}\) constructs
the logarithmic boundary metric. The integer winding ambiguity
vanishes at the complete end by the argument in “Fixing the
winding integer,” including \(\texttt{ctg:period-limit}\), and
is constant during continuation. Thus (8) holds for the full periods.
At \(\lambda=1\), the primitive cone angle is \(2\pi\), and
the original block has the smooth short filling.

For \(n<0\), take \(t_n=-\overline{t_{-n}}\) on the
real-parent slice. Then \(w\) becomes \(\overline w\) and
\(R_0\) becomes \(1/\overline{R_0}\). All shapes in (7) still
have positive imaginary part and the core length is still
positive. The carrier and the integer slope are retained in (8).

The filled point has a holomorphic continuation in the parent
angle near zero: the leaf Hessian
\[
\psi_{tt}(t,0)+\frac{in}{2\pi}
=\frac{-\sec(t/2)+in}{2\pi}
\]
has negative real part. The implicit function theorem therefore
gives \(t_n(u)\), and positivity persists on a small parent
neighborhood. Define its marked geometric action by

\[
\mathcal G_n(u)=
\psi(t_n(u),u)+\frac{in}{4\pi}t_n(u)^2-it_n(u).
                                                        \tag{9}
\]

## 4. The absolute volume normalization

The additive volume constant is fixed by the cone path, not just
by differentiating (9). Along (6), set

\[
\mathcal G_{n,\lambda}
=\psi(t(\lambda),0)+\frac{in}{4\pi}t(\lambda)^2
                       -i\lambda t(\lambda).
\]

Stationarity gives

\[
\frac{d}{d\lambda}\Re\mathcal G_{n,\lambda}
=\Im t(\lambda).
\]

Schläfli's formula for the actual positive cone block gives
the volume derivative
\(-\tfrac12(-2\Im t)\,2\pi=2\pi\Im t\).
This is the geometric paper's volume differential
\(\texttt{ctg:volume-differential}\) along the primitive cone path;
the positive tetrahedra are the original oriented fundamental
chain, as in \(\texttt{ctg:chain-volume}\).
At \(\lambda=0\), the block consists of the original two
complete regular ideal octahedra:

\[
\operatorname{Vol}_{\lambda=0}=2v_{\rm oct}
      =2\pi\psi(0,0).
\]

Integrating fixes its final volume as
\(2\pi\Re\mathcal G_n(0)\). The same argument applies for
negative \(n\).

For every \(|n|\geq3\), the source action in the
proved terminal theorem is exactly \(\mathcal G_n\). For
\(n=2\sigma\), \(\sigma=\pm1\), the two-crossing proof gives
the precise difference

\[
F_{2\sigma}(u)-\mathcal G_{2\sigma}(u)
=\sigma i\pi/2.
                                                        \tag{10}
\]

Move only this explicitly known constant into the unit scalar.
Thus all selected terminal factors can be written

\[
H_{n,N}(u)=\varepsilon_{n,N}a_n(u)
             e^{N\mathcal G_n(u)}(1+O(N^{-1})),
\qquad |\varepsilon_{n,N}|=1,
                                                        \tag{11}
\]

where

\[
\varepsilon_{2\sigma,N}=e^{\sigma i\pi N/2},
\qquad
\varepsilon_{n,N}=C_{N,n}=q^{nd^2/4}
\quad(|n|\geq3).
\]

The amplitude for \(n=2\sigma\) is the original
\(e^{-\sigma i\pi/4}/(2\sqrt{\cos(u/2)})\).
The other amplitudes are the ones in their respective source
theorems. All are nonzero near zero.

The already short-filled blocks assemble with the remaining
complete edge blocks to a complete partially filled exterior
\(Y'\), with the original main cusps complete. Positivity and
the original face pairings give the metric and its original
marking. Summing the fundamental block chains gives

\[
\operatorname{Vol}(Y')
=2e_0v_{\rm oct}
 +2\pi\sum_{\ell\in\mathcal L}\Re\mathcal G_{n_\ell}(0).
                                                        \tag{12}
\]

The selected terminal edges are distinct original edges, so no
block is counted twice.

## 5. Apply the complex-phase filling theorem

The exact source (3) has local phase

\[
P(\mathbf t)=
\sum_{vw\in E_0}\psi(t_v,t_w)
 +\sum_{\ell\in\mathcal L}
                \mathcal G_{n_\ell}(t_{v(\ell)}),
\]

leading power \(\alpha=-3e_0/2\), and unit scalar
\(\varepsilon_N=\prod_{\ell}\varepsilon_{n_\ell,N}\).
Its amplitude is the product of the nonzero edge and leaf
amplitudes.

At complete parent, let
\(k_n=\cos(t_n(0)/2)\). Then

\[
\mathcal G_n''(0)=-\frac{k_n}{2\pi},
\qquad \Re k_n>0.
\]

Indeed the first derivative of \(t_n(u)\) vanishes at zero by
evenness; the second derivative of the stationary value is
the parent partial derivative
\(\psi_{uu}(t_n(0),0)=-\cos(t_n(0)/2)/(2\pi)\).
Consequently

\[
-\Re P_{vv}(0)=
\frac1{2\pi}
\left(\deg_{E_0}(v)
 +\sum_{\ell:\,v(\ell)=v}\Re k_{n_\ell}\right)>0,
\qquad P_{vw}(0)=0\quad(v\ne w).
                                                        \tag{13}
\]

Every remaining vertex either meets a remaining edge, or is the
single remaining vertex and meets a selected leaf. This proves
the strict inequality in (13).

The product of the whole-source bounds (4) and the full edge
bounds gives a Gaussian strip estimate with positive angular
loss at every remaining vertex. The hypotheses of
[the general complex-phase filling theorem](research_long_fillings_complex_boundary_phase.md)
therefore hold. In particular, no claim that the imaginary
part of \(P\) is quadratic is needed.

For independently sufficiently large fixed remaining powers,
that theorem gives the asymptotic (1), with stationary action

\[
S=P(\mathbf t_*)+
     \frac{i}{4\pi}\sum_{v\in V_0}n_vt_{*,v}^{\,2}
                         -i\sum_{v\in V_0}t_{*,v}.
                                                        \tag{14}
\]

The leading power is
\(\alpha+3r/2=-3(r-1)/2+3r/2=3/2\).
Its Gaussian amplitude is nonzero. The exact unit scalar may
be taken as

\[
\Omega_N
=q^{d^2w(D)/2}
 \left(\prod_{\ell\in\mathcal L}\varepsilon_{n_\ell,N}\right)
 \left(\prod_{v\in V_0}C_{N,n_v}\right),
                                                        \tag{15}
\]

where \(w(D)\) is the writhe of the original diagram. This
retains the original zero-framing correction and both level
parities.

## 6. Complete the remaining primitive fillings

The short-leaf elimination preserves the original marked period
identity at every remaining vertex:

\[
U_v=-2\pi P_v-i\eta_vt_v,\qquad V_v=2it_v,
\qquad
U_v+p_vV_v=
-2\pi\left(P_v+\frac{in_v}{2\pi}t_v\right).
                                                        \tag{16}
\]

Elimination introduces no derivative term from a leaf critical
point, since its own stationarity equation makes that term
zero. All logarithmic periods are continued from \(Y'\); none
is reset to a principal branch.

For \(\lambda\in[0,1]\), solve

\[
P_v(\mathbf t)+\frac{in_v}{2\pi}t_v=i\lambda.
\]

The contraction in the complex-phase theorem is uniform on this
interval. Its solutions stay near zero and have
\(\Im t_v<0\) for \(\lambda>0\), independently of the signs
of the large \(n_v\). The remaining edge shapes and the
holomorphic short-filled blocks remain positive. Equation
(16) gives the original primitive cone angles \(2\pi\lambda\)
and lengths \(-2\Im t_v\). The solid-torus completion from the
geometric paper applies with precisely these periods.

At \(\lambda=1\) the metric is the complete hyperbolic metric
on the knot complement specified by the original strand
matching. Define

\[
\mathcal C(\lambda)=P(\mathbf t(\lambda))
 +\frac{i}{4\pi}\sum_v n_vt_v(\lambda)^2
                   -i\lambda\sum_v t_v(\lambda).
\]

Its real derivative is \(\sum_v\Im t_v\). Schläfli's formula
for the assembled cone metric gives
\(d\operatorname{Vol}/d\lambda=2\pi\sum_v\Im t_v\).
Equation (12) is the initial equality at \(\lambda=0\).
Integration therefore gives

\[
\operatorname{Vol}(S^3\setminus K)
=2\pi\Re\mathcal C(1)=2\pi\Re S,
\]

which is (2). Combining it with the nonzero asymptotic (1)
proves the original Kashaev volume identity for this class.
