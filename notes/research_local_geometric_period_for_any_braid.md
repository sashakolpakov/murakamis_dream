# A local geometric period chart for the original knot state

Private written proof, 18 November 2026.

For every hyperbolic knot and every fixed finite braid presenting it,
the original reduced state has an exact finite residue-period
presentation whose integrand has a nonzero local amplitude at a
regular geometric principal critical point. Its corrected principal
action has the hyperbolic volume. The representation uses the
literal factorial crossing coefficients, rather than their
additional coherent occupation transforms.

This is a local statement about an exact presentation. It does not
show that its original residue cycle has a nonzero component at
that critical point. The centralizer direction, other source
boundaries and equal-rate aliases are still present.

The complete proof directs are **A**, the literal slit-chart
amplitudes; **F**, the common framing and complex cut; and **V**,
the actual critical-action volume calibration. Their pins appear
below. The ordinary binomial and residue-kernel steps are proved
here.

## 1. The exact lattice and its coordinates

Fix a braid of a hyperbolic knot, with \(c\) signed crossings.
Put \(N\ge2\), \(d=N-1\), \(h=2\pi i/N\), and \(c_0=2\pi i\).
Keep the original crossing scalars, tail pivots and prescribed
zero framing.

View its closed diagram as the directed crossing graph. It has
\(2c\) wire arcs and \(c\) vertices. Integer occupation on its
wires satisfies input sum equals output sum at each crossing.
The graph is connected and Eulerian. Choose a spanning tree
avoiding the cut edge, which is not a bridge. The \(m=c+1\)
chord-wire occupations
\[
                         k=(k_1,\ldots,k_m)
 \tag{1}
\]
are integral coordinates for its entire circulation lattice.
Indeed integer values on the chords determine the tree values
uniquely by leaf elimination of the conservation equations.
No finite-index sublattice or determinant factor is introduced.
One of the chords is the cut edge.

At each positive crossing the transfer is \(n=c_{\rm out}-b_{\rm in}\);
at a negative crossing it is \(n=b_{\rm in}-c_{\rm out}\).
Thus all wire and transfer indices are integral linear forms in
(1). Let \(S_N\subset\mathbb Z^m\) be the original finite support:
every wire index is between \(0\) and \(d\), with the actual signed
crossing inequalities on \(n\). Nothing extends this support to a
cube of independent occupations.

Let \(W_N(k)\) be the original summand for the unnormalized diagonal
partial trace \(C_N(M)_{aa}\), before the cut average. A trace-one
diagonal probe therefore inserts its weight directly into \(W_N\).
If one instead starts with the old \(1/N\) cut-averaged summand,
the insertion is \(N\) times that weight. These are the same
normalization; an extra \(1/N\) is not retained.

## 2. A frame in which every local length is admissible

F supplies a regular complete geometric frame, arbitrarily near
the midpoint frame, for which every required wire and transfer
clock has modulus different from one. It repairs the wire
logarithms by an integer spanning-tree flow while preserving the
chosen cut logarithm. Choose its cut parameter
\[
 \theta=\frac{\zeta_{\rm cut}}{c_0},\qquad
              \theta\ \hbox{near }1/2,\quad \Im\theta\ne0.
 \tag{2}
\]
Use F's exact complex-binomial cut
\[
 \beta_{\theta,a}=\binom da\theta^a(1-\theta)^{d-a}.
\]
Its weights sum to one. The actual scalar endomorphism identity
therefore gives, exactly at every level,
\[
 K_N=\sum_{k\in S_N}\beta_{\theta,a(k)}W_N(k)
 \tag{3}
\]
in the original reduced zero-framed convention. All original
external factors in that convention remain in \(W_N\).
The marked-cut difference is F's explicit Ward commutator;
(3) does not assert equality of arbitrary marked families.

Set \(x_j=\zeta_j/c_0\) for the chosen chord logarithms.
At the framed geometric point \(x_*\), every chord \(x_j\)
is nonreal: its wire clock is off the unit circle.
Every affine crossing factorial length is also nonreal,
including both numerator and denominator lengths in A.
There is consequently a fixed small polydisc \(U\) about
\(x_*\) on which

* every such length lies in a common compact subset of
  \(\mathcal D=\mathbb C\setminus((-\infty,0]\cup[1,\infty))\);
* each chord imaginary part has a fixed nonzero sign and
  absolute value at least some \(\delta>0\);
* the cut coordinate stays near \(\theta\), with its real
  part strictly between zero and one.

The frame, \(\theta,U,\delta\) are fixed independently of \(N\).
They may depend on the knot and diagram. The finite offsets
involving \(d=N-1\) remain in the literal formulas.

## 3. The local amplitude includes the actual cut weight

Interpolate the cut binomial by its ordinary Gamma ratio:
\[
 b_{N,\theta}(y)=
 \frac{\Gamma(N)}
      {\Gamma(y+1)\Gamma(N-y)}
             \theta^y(1-\theta)^{N-1-y}.
 \tag{4}
\]
The logarithms of \(\theta\) and \(1-\theta\) are the compatible
ones near \(1/2\). This equals \(\beta_{\theta,a}\) at every
allowed integer cut occupation \(a\).

Ordinary Gamma Stirling expansion, on the closed sectors
about the positive real directions used in A, gives uniformly
for \(z\) near \(\theta\)
\[
 b_{N,\theta}(Nz)=
 N^{-1/2}
 \frac{1-z}{(1-\theta)\sqrt{2\pi z(1-z)}}
 \exp\{N\,b_\theta(z)\}(1+O(N^{-1})),
 \tag{5}
\]
\[
 b_\theta(z)=-z\log z-(1-z)\log(1-z)
                        +z\log\theta+(1-z)\log(1-\theta).
\]
To check the finite correction, use
\(\binom{N-1}{Nz}=(1-z)\binom N{Nz}\) and factor
\((1-\theta)^{-1}\) from the last power in (4).
This proves the factor \((1-z)/(1-\theta)\) in (5).
All logarithms and square roots are continued together.
The amplitude is a holomorphic unit on a smaller compact
neighborhood. Bounded affine index offsets only add the
corresponding nonzero exponential of a logarithmic derivative,
as in A's shift calculation.

Interpolate each crossing in \(W_N\) by A's same marked
quantum-factorial ratios. Its exact monomial is kept, including
the common Cartan scalar. Each crossing then has a nonzero
\(N^{-1/2}\) local amplitude on \(U\). Combining the \(c\)
crossings and (5) gives the literal interpolated summand
\[
 I_N(Nx)
   =N^{-(c+1)/2}\,a(x)\,
              e^{N\phi_\theta(x)}(1+O(N^{-1})),
 \qquad a(x)\ne0\quad(x\in U),
 \tag{6}
\]
with the explicitly retained normalizing powers understood
if an alternative external normalization is supplied.
For the reduced diagonal partial-trace convention of Section 1
there is no further old cut-average factor.
All exact monomial, pivot and framing exponentials are included
in the specified principal action and its remaining unit
amplitude. Their root phases have not been replaced by moduli.

Equation (6) concerns the same interpolated lattice summand
whose supported values occur in (3). It is not a theorem
about the additional coherent crossing sums. A supplies the
uniform error and every fixed holomorphic derivative on
smaller compacts.

## 4. An exact period with a locally nonzero residue-kernel amplitude

For each \(N\), let \(\Gamma_N\) be the oriented sum of small
product circles about the points of \(S_N\). Choose them small
enough to enclose no other integer or factorial poles.
The interpolant is holomorphic at these supported points:
every physical factorial length is between zero and \(N-1\),
and common endpoint ratios mean the cancelled finite product.
For an integer vector \(n\in\mathbb Z^m\), define
\[
 \Omega_{N,n}(z)=\frac1{(2\pi i)^m}
       e^{-c_0n\cdot z}I_N(z)
                          \prod_{j=1}^m\pi\cot(\pi z_j)\,dz_j .
 \tag{7}
\]
At an integer state the new character is one, and each
cotangent factor has residue one. Multivariable residues
therefore prove the exact identity
\[
                         \int_{\Gamma_N}\Omega_{N,n}=K_N.
 \tag{8}
\]
All support and source data are the original ones.
The character is part of a specified alternate interpolant,
not an assertion that the two meromorphic forms agree
off the integer lattice.

The cotangent factors also have a nonzero uniform local
amplitude in the chart \(U\). The elementary exponential
formula for cotangent gives
\[
 \pi\cot(\pi N x_j)=
       -i\pi\,\operatorname{sgn}(\Im x_j)
                         +O(e^{-2\pi\delta N}).
 \tag{9}
\]
This is uniform with fixed derivatives after shrinking \(U\);
polynomial differentiation factors are absorbed by a slightly
smaller exponential constant. Thus the actual residue
kernel, not just the factorial summand, is a holomorphic
unit there for all sufficiently large \(N\).
Scaling \(z=Nx\) in (7) gives a local density
\[
 \Omega_{N,n}(Nx)=
  N^{m-(c+1)/2}\,\widetilde a(x)
    e^{N(\phi_\theta(x)-c_0n\cdot x)}
                  (1+O(N^{-1}))\,dx_1\cdots dx_m ,
 \qquad \widetilde a(x)\ne0.
 \tag{10}
\]
The constant factors in (7), (9) are included in
\(\widetilde a\). No pole or zero of the cotangent
kernel has been suppressed near this point.

## 5. Critical action and volume

Write the actual principal action as
\[
 S_\theta(\zeta)=S_0(\zeta)+g_\theta(u),\qquad
 \phi_\theta(x)=S_\theta(c_0x)/c_0,\qquad
 g_\theta(c_0z)=c_0 b_\theta(z).
 \tag{11}
\]
Here \(S_0\) includes all original crossing, pivot and
framing terms. A's reversed factorial products can express
some dilogarithms with reciprocal arguments compared with
V's five-shape notation. The inversion identity changes
their Gaussian part by a real quadratic polynomial,
an imaginary linear polynomial and a real constant;
\(D(z^{-1})=-D(z)\) gives the same crossing regulator.
Thus the bare-state logarithmic identity used below has
the same normalization for this literal factorial phase.
F proves that the geometric point is a
regular exponentiated principal critical point, with
\(u=c_0\theta\). On compatible logarithms let
\[
 \partial_{\zeta_j}S_\theta(\zeta_*)=c_0 n_j,
                         \qquad n_j\in\mathbb Z.
 \tag{12}
\]
Choose precisely this vector in (7). The exponent in
(10) then has zero first derivative at \(x_*\).
This is additive principal stationarity in an exact
period presentation, not just an exponentiated equation.

At this point \(g_\theta=g_\theta'=0\) on the matching
sheets. V supplies the bare-state regulator identity
\[
 D(\beta)=\Im S_0
       -\sum_j\Re\zeta_j\,\Im\partial_{\zeta_j}S_0
 \tag{13}
\]
at \(M=1\), and the degree-one crossing fundamental-chain
comparison \(D(\beta)=\operatorname{Vol}(S^3\setminus K)\).
Consequently
\[
 \Im\left(S_\theta-c_0\sum_jn_j\zeta_j\right)_{\zeta_*}
                     =\operatorname{Vol}(S^3\setminus K).
 \tag{14}
\]
The cut coordinate is included in this subtraction.
Its real part need not be zero for the complex cut.
Thus (10) has the calibrated geometric exponential rate.
Compatible changes of entropy or dilogarithm sheets carry
their corresponding integer character and retained real
constant, as in V; they are not arbitrary shifts of the
imaginary action.

The original external modified-dimension factor, if supplied,
remains its whole function. At \(M=1\) its specified value
is a unit phase times \(1/N\); it changes the explicit power
and phase, not (14). No meridian normal is deleted.

## 6. What the theorem does not say

The point \(x_*\) need not lie on a contributing deformation
of \(\Gamma_N\). The principal critical family retains its
centralizer direction, so this is not an isolated Gaussian
saddle theorem. Even the nonzero local density in (10)
does not fix its relative-cycle coefficient.

Changing the integer character changes the off-lattice
integrand and its possible boundary behavior. Equation (8)
is exact on the stated original small-circle cycle; it
does not permit a subsequent unrecorded contour change.
All other source boundaries, support walls, escaping
decorations and equal-rate aliases still require their
own comparison. No scalar lower bound or new
volume-conjecture knot case is asserted.

Where the underlying finite coefficients have their specified
analytic parameter germs, the residue equality also preserves
those germs. For genuine fixed-color quantum normals one
uses the original path \(M=-q^N\), with \(d=N-1\) fixed,
as in A. A fixed-\(M\) auxiliary array is not identified
with a generic-\(q\) representation by scalarity alone.

## Complete proof-source pins

* A: notes/research_literal_crossing_slit_chart_amplitude.md,
  SHA256 c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.
* F: notes/research_literal_factorial_common_slit_frame.md,
  SHA256 9764a2b77469c7fad402b9b8e609b304a79083bde18fb139031c06fd93650ca8.
* V: notes/research_soft_cut_critical_action_volume.md,
  SHA256 10db12845523ab5700e870e5a896ac003a6c29c3892d4618ddf043d3a5891689.

All three complete unchanged directs were read in the current
author sequence, every used implication checked and all
matching pins renewed. The binomial correction, coordinate
count, exact residue character and cotangent amplitude are
proved here. Only written mathematics and text/hash
operations were used. Frozen and public files are unchanged.
