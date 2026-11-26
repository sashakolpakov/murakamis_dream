# The complete knot source has no regular real interior saddle

Private written deduction, 15 November 2026. No mathematical code,
numerical calculation, test, or saved numerical evidence is used.
Frozen notes and public manuscripts are unchanged.

The selected local clock amplitude does not initialize a positive
real saddle of the complete closed source. For every nonempty braid
whose closure is a knot, the full incidence action has no real
interior stationary point, even after any integer Fourier character
is retained. The same statement holds with the original cut degree
fixed. This is an exact consequence of the source's clock equations
and integral transfer lattice; it is not an abstract cancellation
example.

For alternating generator signs, the central incidence packet also
has an actual midpoint-rectangle deformation with a strict exponential
loss, including both cotangent lips. This local contour statement is
recorded separately from the stronger scalar upper bound already
available by cut peeling.

The statement does not exclude a complex geometric saddle or a
source-preserving deformation to it. It identifies where such a
deformation must do more than multiply the positive local clock
initializers.

## 1. The complete source and its real interior

Use the physical sign convention of the
[joint clock phase](research_joint_clock_phase_equations.md).
At crossing \(j\), let its sign be \(\sigma_j\), its adjacent
head index be \(i_j\), and its normalized physical coordinates be
\(U_j,V_j,J_j\). The overstrand goes from \(U_j+V_j\) to
\(V_j\), and the understrand goes from \(J_j\) to \(J_j+U_j\).
The clock is \(H_j\). Its four normalized incidences are
\[
 (1-U_j-V_j,\ U_j-H_j+V_j,\ H_j-V_j,\ V_j).
 \tag{1}
\]
The closing row on head \(i\) is \((1-A_i,A_i)\).
All wire conservation and the original closing equations remain
imposed. The real regular interior means all incidences in (1)
and all closing incidences are positive.

In this interior every physical head degree lies strictly between
zero and one. To check the under degrees as well as the over
degrees, follow a segment from one over-output or closing event
to the next over-input or closing event. Its intermediate under
degrees increase by the positive transfers \(U_j\). Both endpoint
degrees lie in \((0,1)\), hence so do the intermediate ones.
In particular
\[
 0<U_j<1,\qquad 0<J_j<J_j+U_j<1 .
 \tag{2}
\]

Let
\[
 \mathcal J(x)=\int_0^x\Log(2\sin\pi t)\,dt
 \tag{3}
\]
with its branch real on \((0,1)\). The complete leading action
on the specified source lift is
\[
 \begin{split}
 \mathscr S&=-\sum_{\text{all incidences }e}\mathcal J(x_e)
                       +\pi i\,\varphi,\\
 \varphi&=\sum_j
       \{H_j+\sigma_jH_j(U_j+2J_j)-\sigma_jJ_j\}.
 \end{split}
 \tag{4}
\]
This follows from the full phase (3) of the
[integral midpoint theorem](research_incidence_burau_gauss_reduction.md).
The exact \(N-1\) shifts and the closing pivots contribute the
already specified finite amplitudes; none changes (4).
The closing rows have zero entropy by
\(\mathcal J(1-A)=-\mathcal J(A)\).

Let \(L\) be the homogeneous integral incidence lattice. As in the
source, it is the direct sum of the closed physical-flow lattice
and the independent integral clock coordinates. A real point is
stationary in some integer Fourier lift only if
\[
                 D_\ell\mathscr S\in2\pi i\mathbb Z
                    \quad\hbox{for every }\ell\in L.
 \tag{5}
\]
For the fixed-cut version use the sublattice with \(dA_1=0\).
Condition (5) is necessary independently of the choice of lattice
basis. Subtracting any integral Fourier character changes its
left side by a multiple of \(2\pi i\).

## 2. Transfers are independent integral coordinates after fixing the cut

Let \(b\) be the braid width and \(c>0\) its crossing count.
Write \(y\in\mathbb Z^b\) for its initial head degrees and
\(u\in\mathbb Z^c\) for its transfers, with inequalities temporarily
removed. Let \(P_j\) be the transposition of the two heads at
crossing \(j\), and put \(e_j=e_{i_j}-e_{i_j+1}\). The exact
checked degree dynamics are
\[
                   y^{\mathrm{out}}=P_jy^{\mathrm{in}}
                                         +\sigma_j u_j e_j .
 \tag{6}
\]
For a positive crossing this says
\((I,J)\mapsto(J+u,I-u)\); for a negative crossing it says
\((J,I)\mapsto(I-u,J+u)\). Thus the original role conventions
give (6) at both signs.

Compose these equations. With \(P=P_c\cdots P_1\) and
integer columns \(E_j=\sigma_jP_c\cdots P_{j+1}e_j\),
the closed physical-flow lattice is
\[
                 (I-P)y=Eu .
 \tag{7}
\]
Every column of \(E\) has coordinate sum zero. Because the
closure is a knot, \(P\) is a single cycle, and
\[
 \ker_{\mathbb Z}(I-P)=\mathbb Z\mathbf1,\qquad
 (I-P)\mathbb Z^b=\mathbb Z_0^b .
 \tag{8}
\]
For completeness, writing the coordinates in the order of the
cycle turns \((I-P)y=z\) into successive integral differences.
They can be solved by cumulative sums exactly when
\(\sum z_i=0\); their sole free value adds a constant to every
coordinate. This proves both assertions in (8) without division.

Consequently every \(u\in\mathbb Z^c\) has a closed integral
physical flow. There is a unique one with any prescribed initial
degree \(y_1\). In particular, on the homogeneous fixed-cut
lattice, the transfer map is an isomorphism
\[
              \{ \text{closed integral physical variations},
                      \ dA_1=0\}\ \simeq\ \mathbb Z^c .
 \tag{9}
\]
Every single-transfer variation \(du_j=1,\ du_k=0\) for
\(k\ne j\) is therefore a legitimate integral tangent vector.
At a strictly interior real point, small real multiples of each
such vector stay feasible. The clocks can be held fixed.

## 3. The only possible simultaneous positive clock base slice

At a real point put \(R_j=H_j-V_j\). Differentiating (4) in its
independent clock direction gives
\[
 \partial_{H_j}\mathscr S
  =\log\frac{\sin\pi(U_j-R_j)}{\sin\pi R_j}
      +\pi i\{1+\sigma_j(U_j+2J_j)\}.
 \tag{10}
\]
Here \(0<R_j<U_j<1\). If (5) holds in this direction, its real
part is zero. The identity
\[
 \sin\pi(U-R)-\sin\pi R
       =2\cos(\pi U/2)\sin\pi(U/2-R)
 \tag{11}
\]
then gives \(R_j=U_j/2\). By (2), the midpoint
\(M_j=U_j+2J_j\) belongs to \((0,2)\). The imaginary part
of (10) is an integral multiple of \(2\pi\) only when
\[
                    M_j=1,\qquad H_j=V_j+U_j/2 .
 \tag{12}
\]
These are exactly the central local clock slices, with their
Fourier characters retained.

The integral midpoint theorem identifies the kernel of
\(p\mapsto(U_j+2J_j)_j\) for a knot braid. Its rank is one,
and its initial-head vector is
\[
                     \varepsilon=(1,-1,1,-1,\ldots).
 \tag{13}
\]
This uses the independently proved Burau--Alexander minor
calculation at \(-1\), including even braid width. The constant
flow with every head degree \(1/2\) and all transfers zero has
every midpoint one. Hence every real closed physical flow with
all midpoints one is that flow plus \(\tau\varepsilon\).
The homogeneous zero-midpoint dynamics fix \(\varepsilon\) at
every horizontal slice.

At crossing \(j\) the over-head component of \(\varepsilon\)
is \(\sigma_j\varepsilon_{i_j}\), and its under-head component
is \(-\sigma_j\varepsilon_{i_j}\). Therefore
\[
 \begin{split}
 U_j&=2\tau\sigma_j\varepsilon_{i_j},\\
 J_j=V_j&=\frac12-\tau\sigma_j\varepsilon_{i_j},\\
 H_j&=\frac12 .
 \end{split}
 \tag{14}
\]
The last identity uses (12).

In particular the simultaneous central slice meets the strict
real interior if and only if all signs
\(\sigma_j\varepsilon_{i_j}\) are the same. This is precisely
the alternating generator-sign pattern
\[
                  \sigma_j=\epsilon(-1)^{i_j-1},
                      \qquad \epsilon\in\{1,-1\}.
 \tag{15}
\]
In this case choose \(\tau\) with
\(0<\tau\epsilon<1/2\). All transfers have one common value
\(U=2|\tau|\), and every crossing row is
\[
       ((1-U)/2,\ U/2,\ U/2,\ (1-U)/2).
 \tag{16}
\]
The closing degrees are \(1/2+\tau\varepsilon_i\).
Thus this is a one-dimensional affine slice, not an open
family of physical flows. Fixing the first cut degree fixes
\(\tau\) as well.

## 4. No Fourier lift makes it a full real saddle

**Theorem.** For every nonempty braid with knot closure,
the action (4) has no real stationary point in its regular
interior in any integer Fourier lift. The same assertion
holds on every fixed-cut interior slice.

**Proof.** A purported point must satisfy (12), and hence
(14). Vary only the physical flow, holding all \(H_j\)
fixed. Since \(H_j=1/2\), the differential of the complete
phase is
\[
 \begin{split}
 d\varphi
  &=\sum_j\sigma_j
       \{H_j\,dU_j+(2H_j-1)\,dJ_j\}\\
  &=\frac12\sum_j\sigma_j\,dU_j .
 \end{split}
 \tag{17}
\]
Choose the integral fixed-cut tangent in (9) with a single
\(du_j=1\). The entropy differential is real at the real
point, while (17) gives
\[
                   \operatorname{Im}D_\ell\mathscr S
                                      =\sigma_j\pi/2 .
 \tag{18}
\]
This is not in \(2\pi\mathbb Z\). Subtracting an integer
Fourier character cannot change that fact. It contradicts
(5), proving both versions. \(\square\)

The fixed-cut qualification uses the actual operator scalarity
before insertion, as in
[marked-cut observability](research_incidence_marked_cut_observability.md).
It does not replace the prescribed cut in a separate clock
sector. The proof of (18) is on the whole conserved lattice
and keeps the original closing equations.

The earlier
[alternating real-phase obstruction](alternating_braid_real_phase_obstruction.md)
already excludes a real saddle through a particular consecutive
opposite-sign variation of the cyclic source. The theorem above
is a different, general calculation on the full singleton
incidence lattice: it covers every nonempty knot braid and
every regular real interior point, including every fixed cut.
It does not make a claim about boundary strata.

## 5. The actual complex chart still available

This exclusion does not remove the complex interpolation.
Let \(G_N\) be the exact sine-factorial function of
[the factorial source](exact_factorial_interpolation_and_complex_contours.md),
with \(G_N(a)=S_a\) at the original integers. The selected clock
sum has the following specified extension in all its physical
variables:
\[
 \widetilde C_{\sigma,N}(U,V,j)
  =\frac{G_N(N(j+U))}
          {G_N(Nj)G_N(NU)}
       \exp\left[
        N\sigma\pi i\{V(U+2j-1)+jU+U^2/2-U/2\}
           +\sigma\pi i(V+U/2)\right].
 \tag{19}
\]
For \(NU=u,\ NV=v\) integral, this is exactly the finite
clock sum of the
[selected-amplitude theorem](research_exact_clock_selected_amplitude.md),
for every complex \(j\) in its domain. Indeed the exact
functional equation of \(G_N\) turns its first ratio into
\(\prod_{r=1}^u2\sin\pi(j+r/N)\); the displayed phase
is exactly the marked Pochhammer phase and \(a_{\sigma,N}^v\).
Thus the equality fixes the continuation and its marks
rather than choosing a new saddle normalization.

Multiplying (19) by the remaining exact row factors gives
\[
 \widetilde{\mathcal R}_{\sigma,N}
  =\kappa^\sigma
     \frac{G_N(N(U+V))}{G_N(NV)}
       e^{-\sigma\pi i(N-1)j}\,
                    \widetilde C_{\sigma,N}.
 \tag{20}
\]
This is holomorphic and nonzero on the convex tube
\[
 \begin{gathered}
 0<\Re U<1,\qquad 0<\Re V<\Re(U+V)<1,\\
 0<\Re j<\Re(j+U)<1 .
 \end{gathered}
 \tag{21}
\]
The exact factorial expansion supplies its nonzero local
complex symbol uniformly on compact subsets, with the
original finite Cartan and framing phases. Products of
these row charts retain the literal physical wire equations.
This is the existing factorial interpolation expressed in
the coordinates of the new exact clock contraction.

The original cycle is still the sum of residue tori around
the actual allowed physical lattice states, with every
endpoint state included. Points on its boundary are not
contained in fixed compact subsets of (21). The theorem
does not transform that cycle into a geometric descending
cycle or bound the side currents of such a transformation.
The raw positive Fourier charts also have the independently
proved [sewing obstruction](research_rivin_jones_positive_chart_sewing_obstruction.md);
switching to them does not supply the missing transport.

The conclusion for the proposed route is precise. The local
clock contraction has a selected nonzero amplitude, but its
positive real initializer cannot be made a full interior
saddle by the actual conserved-flow equations or by a
Fourier relabeling. A geometric contribution must be located
on a genuinely complex chart or after further source
contractions or boundary reductions. No nonzero intersection
with the original residue cycle has been proved here.
The additional global conditions in
[dominant-saddle transport](research_dominant_saddle_transport.md)
remain to be established for that actual complex source.

## 6. Exponential cancellation of the actual central packet

For the alternating sign class (15), the source obstruction has an
explicit contour realization. This gives a cancellation estimate
in the singleton incidence presentation. It is not a new claim
of a strict crossing-count bound: the older
[cyclic cut peeling theorem](original_source_cyclic_variation_peeling.md),
Section 2, already gives a stronger scalar loss by making the first
and last cut-crossing weights have modulus one. They are the same
crossing if the marked position occurs only once.

Fix a nonempty knot braid satisfying (15), put
\(a_*=1/2+\epsilon/4\), and choose
\(r_N\in\{0,\ldots,N-1\}\) with
\(|r_N-Na_*|\le1/2\). Fix the literal first cut degree to
\(r_N\). The exact marked-cut theorem permits this choice
for the complete sum with its original normalization.
By (9), the remaining \((u,h)\) are independent integral
coordinates, with their original inequalities.

At the limiting point \(z_*=(U,H)=(\mathbf{1}/2,\mathbf{1}/2)\),
the horizontal heads are \(1/2+\epsilon\varepsilon_i/4\).
Every crossing has over-input \(3/4\), under-input and
over-output \(1/4\), and transfer \(1/2\). Its four
incidences are all \(1/4\). The closing incidences are
\(1/4\) or \(3/4\).

The strict row concavity in
[the angle optimization](research_charged_source_angle_optimization.md)
makes this the unique absolute-action maximum on the
fixed-cut limiting fiber, with value
\[
             M_c=-4c\,\mathcal J(1/4)
                          =\frac{c\,v_8}{2\pi}.
 \tag{22}
\]
Here \(v_8\) is the regular ideal octahedron volume.
Uniqueness follows because the crossing incidences recover
all \(U_j,H_j\), and (9) then recovers the physical flow.
Closing rows have zero entropy.

Choose a sufficiently small fixed \(\rho>0\) and retain the
actual rectangular packet
\[
 \mathcal B_N=\{(u,h)\text{ in the allowed fixed-cut fiber}:
        |u_j/N-1/2|\le\rho,\quad |h_j/N-1/2|\le\rho
                          \text{ for every }j\}.
 \tag{23}
\]
For large \(N\), the entire box is feasible, since all
incidence forms are affine and strictly interior at \(z_*\).
Let \(w_N=q^{\Phi_N}/\prod_eS_{n_e}\) be the complete
incidence weight on this fixed-cut slice, including its
original closing pivots.

**Packet theorem.** There are \(C,B,\delta>0\), depending
only on this fixed braid and packet, such that
\[
          \left|\sum_{\mathcal B_N}w_N\right|
                    \le C N^B e^{N(M_c-\delta)}
 \tag{24}
\]
for every sufficiently large \(N\), with no parity or
coprimality restriction. Enlarging \(C\) covers the
finitely many remaining levels as well.

**Proof.** Extend the exact degree forms affinely and use
the specified factorial function \(G_N\). Its exact
reflection contracts each closing denominator:
\[
 \mathcal I_N(u,h)
     =N^{-b}\exp\{\pi i\Phi_N(u,h)/N\}
        \prod_{\substack{j\text{ a crossing}\\0\le k\le3}}
                                  G_N(n_{jk}(u,h))^{-1}.
 \tag{25}
\]
This is the original weight at all integer points.
All \(N-1\) shifts, the difference \(r_N-Na_*\), and
the pivotal phases remain in (25). On a fixed small
complex neighborhood of \(z_*\), its scaled factorial
arguments have real parts strictly between zero and one.
The exact compact complex expansion therefore gives
\[
          |\mathcal I_N(Nz)|
                    \le C N^{B_0}e^{N\Re\mathscr S_*(z)},
 \tag{26}
\]
where \(\mathscr S_*\) is (4) with cut \(A_1=a_*\).
The bounded finite offsets change the exponent by \(O(1)\)
on this compact chart. The exact finite phase shifts are
also retained in the bounded factor. No leading
state-dependent phase is removed.

Choose one crossing \(j\), set \(t=\sigma_j u_j\), and
write \(x=t/N\), centered at \(x_*=\sigma_j/2\).
All other \(2c-1\) coordinates remain real and fixed.
By (17),
\[
                \Im\partial_x\mathscr S_*(z_*)=\pi/2.
 \tag{27}
\]
Shrink \(\rho\) and choose a small fixed height \(\beta>0\)
so that throughout the resulting complex box
\[
           \pi/4\le\Im\partial_x\mathscr S_*\le3\pi/4.
 \tag{28}
\]
The two real faces \(|x-x_*|=\rho\) have a uniform
entropy gap \(\eta>0\) below \(M_c\), by uniqueness
and compactness. Shrink it once to include the
\(O(N^{-1})\) endpoint changes below, and choose
\((3\pi/4)\beta\le\eta/2\).

If the integers \(t\) in the packet run from \(A_N\) to
\(B_N\), take the positively oriented rectangle with
vertical sides \(A_N-1/2,\ B_N+1/2\) and horizontal
sides \(\Im t=\pm N\beta\). Holomorphy gives exactly
\[
 \sum_{t=A_N}^{B_N}\mathcal I_N(t,\ldots)
   =\frac1{2\pi i}\int_{\partial\mathcal R_N}
        \mathcal I_N(t,\ldots)\,
                         \pi\{\cot(\pi t)-i\}\,dt .
 \tag{29}
\]
The subtraction is \(\pi i\), not \(i\); its contour
integral is zero. Every original integer residue in the
interval remains, also when \(t\) ranges over negative
integers for the negative sign.

On the upper lip the cotangent factor is bounded, and
(28) lowers \(\Re\mathscr S_*\) by at least
\(\pi\beta/4\). On the lower lip the density increases
by at most \(3\pi\beta/4\), but its exact kernel obeys
\[
                   |\cot(\pi t)-i|
                              \le C e^{-2\pi N\beta}.
 \tag{30}
\]
The combined exponent there is at most
\(M_c-5\pi\beta/4\). On a half-integer vertical side,
\(|\cot(\pi t)-i|\le2\), and the entropy gap with
(28) bounds the exponent by \(M_c-\eta/2\).
The contour length is \(O(N)\). Equations (26)--(30)
therefore bound this one-variable sum by a polynomial
times \(e^{N(M_c-\delta)}\), uniformly in the other
coordinates, with
\(\delta=\min(\pi\beta/4,\eta/2)>0\).
There are only polynomially many choices of those real
integer coordinates. Summing proves (24). \(\square\)

The complement of (23) has a strict absolute entropy
gap below \(M_c\): otherwise compactness gives another
maximum with some transfer or clock separated from
\(1/2\). The endpoint-uniform factorial estimate and
the exact margin \(N-1\) control this complement with
a polynomial prefactor. Combining it with (24)
recovers a strict scalar gap after multiplication by
the known original external source factor. As already
noted, cyclic cut peeling gives a stronger scalar
bound; the additional assertion here is the explicit
complex deformation and loss of the central incidence
packet itself.

The cotangent kernel is essential. Its lower density
may grow while its exact source factor decays. Thus
the proof does not give a low-modulus deformation
for all individual lattice evaluations. It retains
the prescribed packet period and does not identify
the surviving geometric contour. In particular
\(\delta\) is not compared with the difference
between the crossing envelope and hyperbolic volume.

## Direct written source versions

| Source | SHA-256 |
| --- | --- |
| research_joint_clock_phase_equations.md | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |
| research_incidence_burau_gauss_reduction.md | 7ca4c1534d3dd4c75e4200b8b221c5b92cae8c2835487b2c97f9014fdbdda1d6 |
| research_incidence_marked_cut_observability.md | c0b9f010a8ab4b69b96bbcb0a32a6b8dad6ed8c39fca1029834f2ba74c13cbfc |
| research_exact_clock_selected_amplitude.md | a94cdff7db9a704af71f1794bf969d6c00809b7ac13b776f153034a10e1fb617 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| alternating_braid_real_phase_obstruction.md | 954628d08257f57559fd130f5ac5b0d69271852b751eac71399f55e7d2f646d5 |
| research_rivin_jones_positive_chart_sewing_obstruction.md | 7809489b46a1eb50accca9910428ca929fd98622734060e39b42e1e2070c7910 |
| research_dominant_saddle_transport.md | 413940497a23e884d726b91f9c0ebc01994fef8216811ed2c6fb0838fc80bb04 |
| research_charged_source_angle_optimization.md | 45b21fabb9cb65512bc3e576eb3d659b6fe14c3dcd90b4164bfdb12b8cedea64 |
| original_source_cyclic_variation_peeling.md | a050e02461edd0ae5d7da1caf1ad673b81921c5a5acebcd6a0153f39e13aca1a |
