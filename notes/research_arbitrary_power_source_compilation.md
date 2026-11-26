# Exact source compilation with arbitrary crossing powers

Research note, 2 November 2026.

The original pair algebra supplies a compositional description of
every finite Conway expression and every circle-tree source. It
retains arbitrary signed crossing powers, every free boundary
variable, and the first derivatives at the repeated spectral roots.
There are two useful representations. A Newton coefficient
calculation gives factorial sums directly. Restoring the original
vertex traces instead gives a finite Fourier representation in
which every paired internal index can be integrated exactly.

The latter representation removes the internal-index lattice
problem in general. It does not remove the oscillatory vertex
integrals or prove their geometric asymptotics.

The main meridian is at its original complete value, so the
pair relation is \(P_N=0\). Free boundary variables below are
retained auxiliary spectral variables. This note does not
identify a deformed relation \(P_{N,\sigma}\) with \(P_N\),
or remove the additional edge weights in the moving-meridian
source.

## 1. The original operations and their kernels

Fix \(N\ge2\), put \(D=N-1\), and use the algebra, basis, turn,
and trace of
[the finite Newton calculus](../papers/newton-calculus/finite.tex):
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi(e_i e_j)=\delta_{i+j,D},\qquad
 \mathsf T e_i=e_{D-i}.
 \tag{1}
\]
The Newton basis is normalized by
\[
 e_i(z)=S_i^{-2}\prod_{k=0}^{i-1}(c_k-z),\qquad
 S_i=\prod_{k=1}^i2\sin(\pi k/N).
 \tag{2}
\]
All the statements below are in the full algebra, not in its
quotient obtained by dropping nilpotents.

Define the two polynomial kernels
\[
 K_I(z,w)=\sum_{i=0}^D e_i(z)e_{D-i}(w),\qquad
 K_T(z,w)=\sum_{i=0}^D e_i(z)e_i(w).
 \tag{3}
\]
For every \(A\in\mathcal A_N\),
\[
 A(z)=\phi_w(K_I(z,w)A(w)),\qquad
 (\mathsf T A)(z)=\phi_w(K_T(z,w)A(w)).
 \tag{4}
\]
To prove these formulas, write \(A=\sum_j a_je_j\) and
apply (1). The first extracts \(a_i\), the second \(a_{D-i}\).
Thus these are the actual identity and turn operations,
with no unspecified scalar.

The positive physical crossing has multiplication matrix
\[
 M_{kj}=\kappa(-1)^k q^{k(j+1)}
                  \frac{S_k}{S_jS_{k-j}},
 \quad 0\le j\le k<N,\qquad
 q=e^{\pi i/N},\quad\kappa=q^{D^2/2}.
 \tag{5}
\]
The remaining entries are zero. The negative crossing has
the coefficient-conjugate matrix, since
\(R^{-1}=\overline R\) in the real Newton basis.
Consequently every fixed signed power is represented
exactly by \(M^n\), or by a chain of \(|n|\) copies of
the appropriate signed matrix (5).

Multiplication is encoded by the tensor
\[
 \mu_{ijr}=\phi(e_i e_j e_{D-r}).
 \tag{6}
\]
This follows by applying the dual basis in (1) to the
coefficient expansion of \(e_i e_j\). In particular,
the familiar positive factorial formula for \(\mu\)
and its zero support are statements about this tensor
with all normal derivatives included.

## 2. A compositional exact representation

**Proposition 1.** Any finite expression made from
multiplication, the physical turn, multiplication by
specified signed powers \(R^n\), and the original closure
\(\phi\), can be evaluated by a finite network of the
kernels (3), with vertex weights \(R^n\) and the original
traces. Its canonical degree-less-than-\(N\) output is the
same polynomial as that of the expression. If designated
free variables are instead kept as unreduced ordinary
polynomials, the compiler acts only at contracted vertices
and leaves all products in those free variables unchanged.

**Proof.** Replace each identity or turn connection by
the corresponding formula in (4). Replace a multiplication
output by (6). Keep every crossing polynomial as its
original vertex weight. Expanding the finite kernels
then gives the original Newton coefficient calculation
at every step. This is an induction on the expression.
It is an identity in \(\mathcal A_N\), so equality at
the double roots includes the first normal derivative.
No step uses evaluation at only the distinct roots.
At a free variable, no dual-basis contraction is inserted;
expanding the same finite kernels therefore preserves
its entire ordinary polynomial, coefficient by coefficient.
QED.

For a partially filled circle tree there is a particularly
simple form. Associate a spectral variable \(z_v\) to each
original vertex and use \(K_T(z_v,z_w)\) on its original
edges. At a filled vertex apply
\(\phi_{z_v}(R^{n_v}\,\cdot)\). At an unfilled vertex keep
the ordinary polynomial in \(z_v\), without reducing its
product modulo \(P_N\). This is exactly the original
partial source.

The distinction at an unfilled vertex is deliberate.
Products there can have degree greater than \(D\), and
the subsequent filling theorem uses that entire
polynomial. The network construction does not replace
it by its values at the distinct spectral roots or by
a lower-degree representative.

Arbitrary Conway turn patterns use \(K_I\) or \(K_T\)
according to the actual connection. For example, an
output with coefficient \(r\) is paired with \(e_{D-r}\)
as in (6); a turn reverses that index once. These choices
are made by the physical expression, not by a desired
asymptotic sign.

## 3. Restoring a trace resolves the local gate poles

The canonical factorial ratio
\[
 \frac{G_N(i+j)G_N(r)}
 {G_N(i)G_N(j)G_N(r-i)G_N(r-j)G_N(i+j-r)}
 \tag{7}
\]
gives \(\mu_{ijr}\) on its allowed integer support.
It need not be holomorphic on a simultaneous rectangle
in all three continued indices. At \(N=3\) and
\((i,j,r)=(2,2,0)\), the uncancelled divisor has the
local form
\[
 \text{unit}\cdot
 \frac{(\delta i+\delta j)(\delta r-\delta i)
                         (\delta r-\delta j)}
      {\delta i+\delta j-\delta r}.
 \tag{8}
\]
Positive total vanishing order does not remove the
denominator hyperplane.

There is an exact alternative supplied by the original
trace. Let
\[
 B_N(x,t)=
 \frac{N}
 {G_N(D/2-Nx+Nt/(2\pi))
  G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{9}
\]
Let \(\widetilde B_N(x,z)\) be its canonical finite-band
Hermite representative from
[the Fourier-band theorem](research_newton_interpolation_finite_fourier_band.md).
It is an ordinary polynomial in \(z\), entire in \(x\),
and agrees with \(e_i(z)\) at \(x=i/N\).
Define
\[
 \widetilde\mu_N(x,y,r)=
 \phi\!\left(
   \widetilde B_N(x,\Omega)\widetilde B_N(y,\Omega)
                 \widetilde B_N(D/N-r,\Omega)\right).
 \tag{10}
\]
This function is entire in all three continued indices,
and at the index grid it gives precisely (6), including
every zero coefficient outside the multiplication support.
Unlike (7), it has no pole of the form (8).

This interpolation is not selected merely because it is
regular. It comes with an exact original trace cycle.
Put
\[
 \tau_j=\pi-\frac{(2j+1)\pi}{N},\qquad
 \eta=(-1)^D,\qquad
 K_N(t)=\frac{iNe^{iNt}}{e^{iNt}-\eta}.
 \]
The exact derivative-sampling trace gives
\[
 \widetilde\mu_N(x,y,r)=
 \eta\sum_{j=0}^{D}
 \left.\frac{d}{dt}
 \left\{\sin t\,B_N(x,t)B_N(y,t)
                         B_N(D/N-r,t)\right\}\right|_{t=\tau_j}.
 \tag{11}
\]
It retains the original first normal contributions.
Equivalently, for a suitable positively oriented rectangle
\(\Gamma_N\) enclosing these \(N\) points,
\[
 \widetilde\mu_N=
 -\frac{\eta}{2\pi i}\oint_{\Gamma_N}
 K_N'(t)\sin t\,B_N(x,t)B_N(y,t)
                         B_N(D/N-r,t)\,dt.
 \tag{12}
\]
This is integration by parts in the exact residue formula,
not an asymptotic replacement of (7).

One explicit joint domain is useful. Let each index have
real part in
\[
 [-1/(2N),\,1-1/(2N)],
 \]
and take the vertical sides of \(\Gamma_N\) at
\[
 \Re t=\pm\left(\pi-\frac{\pi}{2N}\right).
 \tag{13}
\]
These sides still enclose every \(\tau_j\).
Both the direct and reflected index have the same real
range. Every shifted reciprocal-factorial argument in
(9) has real part strictly between \(-N+1/4\) and
\(N-1/4\); also \(\Re(Nx)\in[-1/2,N-1/2]\).
The divisor theorem therefore makes the three factors
holomorphic on a neighborhood of this product contour,
for arbitrary fixed finite imaginary heights.
No unrecorded pole crosses (12).

## 4. Exact internal-index integration for arbitrary powers

The Fourier-band theorem proves that
\(\widetilde B_N(x,z)\) has exactly the possible frequencies
\[
 -D/2,-D/2+1,\ldots,D/2
 \tag{14}
\]
in \(x\). Reflection \(x\mapsto D/N-x\) preserves this
band. At a traced endpoint, (9) has the same band in
the full quotient, including its first derivatives.

Each edge in the restored network occurs in exactly
two such factors. Its product therefore has integer
frequencies in \([-D,D]\). Since \(D<N\), both its
\(N\)-point average and its full-period integral extract
only the constant coefficient. Thus every internal
edge sum can be replaced exactly by \(N\) times an
integral over a horizontal period of arbitrary height.
The precise simultaneous statement is
[the internal-wire averaging theorem](research_internal_wire_exact_circle_averaging.md).

The arbitrary weights \(R^{n_v}\) do not change any
index band. Consequently this conclusion holds for
every finite network above and every fixed signed
choice of its crossing powers. In this representation
the internal-index side differences and all internal
lattice corrections vanish exactly after the full
vertex traces have been taken.

For a free boundary one has two exact options. Its
original index sum may be left finite; or one may use
the polynomial \(\widetilde B_N(x,z)\) there and apply
the same averaging identity. Both preserve the entire
boundary polynomial. The factorial expression (9)
equals \(\widetilde B_N\) only in \(\mathcal A_N\), so
it must not replace the latter at a free boundary
without an additional argument.

The remaining vertex integrals retain their original
quadratic phases. In (12), a weight \(R^n\) changes
the integrand and scalar to
\[
 -\frac{\eta C_{N,n}}{2\pi i}
 K_N'(t)\sin t\,
      \exp\!\left(\frac{inN}{4\pi}t^2\right)
          \prod_{\text{incident factors}}B_N(\cdot,t),
 \qquad C_{N,n}=q^{nD^2/4}.
 \tag{15}
\]
This is the exact physical trace from
[the complete-trace theorem](research_exact_complete_trace_contour.md).
Its double-pole kernel is essential.

The cancellation of index corrections is not a
pointwise assertion on these continuous angle
contours. Before taking the physical trace, (9)
is not generally periodic in its continued index.
The exact identities concern the full traces, or
the resulting joint integrals with their specified
cycles. Deforming a part of that joint cycle still
requires its own analytic argument.

## 5. A contracted factorial form that really is a source

There is an explicit contracted form for a whole path
whose original vertices all have crossing power \(+2\).
Let the path have \(m\ge1\) edges and \(m+1\) vertices.
Assign an index \(i_j\in\{0,\ldots,D\}\) to each edge.
The two endpoint traces are
\[
 \phi(R^2e_i)=Nq^{i^2}/F_i,\qquad F_i=(q^2;q^2)_i,
 \tag{16}
\]
and each internal degree-two trace is
\[
 \phi(R^2e_i e_j)=
 Nq^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2},
 \tag{17}
\]
with zero value if \(i+j\ge N\). These are the original
full-algebra identities, with their given framing.

Let \(\Gamma\) be the path whose \(m\) vertices correspond
to the original edge indices. For \(m=1\), it has no
edges. Write \(d_\Gamma(j)\) for its degree.
Multiplication of (16)--(17), followed by the identity
\[
 S_r=\mathrm i^{\,r}q^{-r(r+1)/2}F_r,\qquad \mathrm i^2=-1,
\]
gives the exact scalar source
\[
 \begin{split}
 Z_N={}&N^{m+1}
 \sum_{\mathbf i\in\{0,\ldots,D\}^{m}}
 \exp\left\{
   \frac{i\pi}{N}
      \left(\sum_j i_j^2-\sum_{\{j,k\}\in E(\Gamma)}i_ji_k\right)
       +i\pi\left(1-\frac1N\right)\sum_j i_j
       \right\}\\
 &\quad\times
 \frac{\displaystyle\prod_{\{j,k\}\in E(\Gamma)}G_N(i_j+i_k)}
      {\displaystyle\prod_{j=1}^{m}G_N(i_j)^{d_\Gamma(j)+2}}.
 \end{split}
 \tag{18}
\]
There is no denominator zero on the full index cube.
The numerator gives exactly the capacity zeros
\(i_j+i_k\ge N\). Thus (18) has a genuine simultaneous
rectangular extension, for arbitrarily many edges.

For its continued normalized variables \(x_j=i_j/N\),
the quadratic phase is
\[
 i\pi N\left(\sum_jx_j^2-\sum_{\{j,k\}}x_jx_k\right),
 \]
and its linear phase is \(i\pi(N-1)\sum_jx_j\).
In the boundary-order theorem, each coordinate has
\[
 \Delta_j=0,\qquad L_j=N-1,\qquad\kappa_j=1.
 \tag{19}
\]
The mixed terms cancel as well. Thus this is an actual
original source in the balanced capacity class, not
only an abstract factorial example.

Here \(Z_N\) denotes the original framed contraction of
the displayed path. If its diagram defines a knot, the
previously specified zero-framing multiplier must still
be applied to obtain that normalized invariant. Formula
(18) removes no framing scalar and introduces none.

The same statement with every original power equal
to \(-2\) follows by coefficient conjugation, using
the opposite half-plane. Mixed signs do not automatically
have the same lower-end balances; their phases must be
retained separately.

Formula (18) does not extend to a branching original
vertex merely by replacing the path \(\Gamma\) by an
arbitrary graph. At a degree-three vertex the exact
factor is
\[
 \phi(R^2e_i e_j e_k)
     =\sum_r\mu_{ijr}\,\phi(R^2e_r e_k).
 \tag{20}
\]
For example, at \(N=4\), \(i=j=k=1\), it equals
\(\sqrt2(-3+i)\). The proposed single-factor extension
\[
 Nq^{\,i^2+j^2+k^2-2ij-2ik-2jk}
            F_{i+j+k}/(F_i^2F_j^2F_k^2)
 \]
instead equals \(\sqrt2(-1+i)\).
This exact discrepancy rules out that shortcut.
The restored network representation, which keeps the
trace (20), has no such restriction on vertex degree.

The phases and normalization in (18) are reproduced by
[this standalone comparison](../experiments/check_power_two_path_factorial_source.py).
It evaluates the original full Newton crossing matrix
recursively and compares it with the factorial formula.
[The saved results](../repro/results/research-power-two-path-factorial-source.json)
cover levels \(2\) through \(9\) and paths with one through
four edges at 80 decimal digits. These finite checks do
not assert an asymptotic theorem.

## 6. What an ordinary Fourier change cannot remove

The finite Fourier transform of the Newton index is
already built into (14). It is an invertible change
of coordinates on the \(N\)-dimensional space of
coefficients. It does not make multiplication by
the crossing semisimple.

At a double spectral root \(c_j\), write
\(\varepsilon=z-c_j\), \(\varepsilon^2=0\).
For every nonzero integer \(n\), multiplication by
\(R^n\) on this local algebra has the form
\[
 R(c_j)^n
 \begin{pmatrix}1&0\\n\alpha_j&1\end{pmatrix},
 \qquad
 \alpha_j=\frac{R'(c_j)}{R(c_j)}
       =\frac{i(D-2j)}{4\sin((2j+1)\pi/N)}\ne0.
 \tag{21}
\]
These are the original first normal coordinates; the
formula and its obstruction to unitarity were already
recorded in
[the arbitrary-power calculation](research_terminal_powers_qbinomial.md).
In particular the nontrivial Jordan block survives
every similarity transformation.

An ordinary finite Gaussian chirp is diagonal, and
an ordinary unitary finite Fourier or metaplectic
change preserves semisimplicity. Such a change cannot
identify the full operator (21) with a diagonal
chirp while retaining its normal data. A representation
using Gaussian phases and their derivatives is possible
in principle; (15) is the existing exact version here.
Its original finite cycle and endpoint contributions
remain part of the problem.

There is nevertheless a precise finite-level periodicity
with a nilpotent correction.

**Proposition 2.** Set \(\eta=(-1)^D\) and
\[
 U_N=\eta R^{2N}-1.
 \]
Then \(U_N^2=0\), and for every pair of integers \(n,k\),
\[
 R^{n+2Nk}=\eta^k R^n(1+kU_N).
 \tag{22}
\]
In particular, any restored source is separately affine
in a period-shift \(k\) of each original vertex power,
after extracting its explicit factor \(\eta^k\).

**Proof.** The diagonal of (5) gives
\[
 R(c_j)=\kappa(-1)^j q^{j(j+1)},\qquad
 R(c_j)^{2N}=(-1)^{D^2}=\eta.
 \]
Thus \(U_N\) vanishes at every spectral root. The radical
of \(\mathcal A_N\) is square-zero because its local
factors have multiplicity at most two. Hence \(U_N^2=0\).
The binomial identity \((1+U_N)^k=1+kU_N\) holds for
all integers, including negative ones. This proves (22).
Every vertex weight enters the restored source linearly,
which gives its stated dependence on the period shifts.
QED.

The correction is not identically zero:
at a double root, \(U_N'=2N\alpha_j\ne0\).
For a source depending on one original vertex power,
the equivalent finite-difference identity is
\[
 Z_N(n+4N)-2\eta Z_N(n+2N)+Z_N(n)=0.
 \tag{23}
\]
Any external zero-framing scalar is still the specified
one and must be carried separately.

The period in (22) grows with \(N\). It therefore cannot
transfer a fixed-knot volume asymptotic from large
crossing powers by replacing \(n\) with \(n+2Nk\).
That replacement changes the diagram with the level,
outside the fixed-power hypotheses of the filling
theorems.

The structural gain is therefore precise. Arbitrary
Conway and circle-tree sources have an exact restored
description, and internal Newton indices admit
correction-free full-period integration. The remaining
general partial-filling problem is to control the
physical angle periods in (15), together with the
free-boundary polynomial, at the geometric rate.
