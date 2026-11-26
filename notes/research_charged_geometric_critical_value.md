# Geometric critical points and marked values of the actual charged source

Private written comparison, 19 November 2026.

The complete geometric representation already has an actual physical
braid critical point. This note identifies its coordinates in the
alternating charged source, including the full leading action and its
integer alias. The charged five-shape Bloch sum is the previously
calibrated physical fundamental class. Its marked critical action
therefore has real part equal to hyperbolic volume divided by \(2\pi\).

This is a classical comparison of the original source function. It
does not prove that its finite residue cycle contains that critical
point with nonzero coefficient. In particular the proved exterior
fiber neighborhood is not identified with every geometric offset.
The actual Gauss-clock inequalities needed for its positive chamber
are stated explicitly below.

The complete directs are C, D, J, M and B, listed at the end.
The comparison uses their written proofs, not their numerical audits
or any imported representation-volume theorem.

## 1. The exact charge-to-physical correspondence

Fix an actual connected alternating closed-braid diagram of an
oriented hyperbolic knot, with at least one crossing. Use C's
physical signs \(\sigma_j\), its original closure, and
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x_0=-q^{-1}.
 \tag{1}
\]
Its integer crossing charges are \(u_j,z_j,A_j,B_j\), with
\[
 A_j=u_{a(j)},\quad B_j=z_{b(j)},\quad
 u_j+z_j=A_j+B_j,\qquad u_j,z_j\ge0,\quad u_j+z_j\le d.
 \tag{2}
\]
The maps a,b are C's literal port permutations. At that crossing
define physical over-input, over-output, under-input and transfer by
\[
 I_j=d-u_j,\qquad V_j=z_j,\qquad J_j=B_j,\qquad
 \delta_j=d-u_j-z_j .
 \tag{3}
\]
The under-output is \(J_j+\delta_j=d-A_j\).
These are the original bounded physical colors: (2) implies
\[
 0\le V_j\le I_j\le d,\quad
 0\le J_j\le J_j+\delta_j\le d.
 \tag{4}
\]
There is no analytic interpolation in this assertion.

Here is the global bijection, including the closure. In an alternating
diagram an under-segment starts at an over-output, passes one
undercrossing, and ends at an over-input. C's incoming charge on that
segment is \(B_j\), and its outgoing degree is \(d-A_j\).
Thus (3) gives exactly its physical transfer and matching degrees.
Any intervening closing adapters transmit \(B_j\) before the
underpass and \(d-A_j\) after it, precisely C's closing rule.
Conversely, from a conserved physical color path take
\(u_j=d-I_j\), \(z_j=V_j\). Its transfer and segment matching give
every equation in (2). Both constructions are inverse.
The original pivot and averaged first cut have not been replaced.

At principal scale use the same lower-case letters for integer
charges divided by N. Then (3) reads
\[
 I=1-u,\quad V=z,\quad J=B,\quad
 \delta=1-u-z,\quad J+\delta=1-A .
 \tag{5}
\]
The difference between d and N remains in the exact source and its
subprincipal factors; it is not removed from finite formulas.
On the complexified affine conservation space (5) is an invertible
affine change of physical-flow coordinates. C's integral face
coordinates, with one black face fixed, are an honest lattice basis
for this space. In particular its Fourier characters are the original
integral characters, not a larger rational character lattice.

There is no additional obstruction to lifting a nonzero multiplicative
flow to these face logarithms. Orient the dual edges from white to
black and give them their multiplicative charges. The product around
each dual quadrilateral is one by (2). The same dual-sphere path
integration as C therefore gives nonzero face potentials, unique after
one gauge is fixed. Choose logarithms of those potentials and form
the edge logarithms by their differences, or black/white sums in C's
convention. They satisfy the additive conservation equations exactly.
Their difference from any previously chosen edge logs is an integral
\(2\pi i\) vector, which is retained in the subsequent alias marking.

## 2. Equality of the full physical and charged actions

Let
\[
 {\cal J}(v)=\int_0^v\operatorname{Log}(2\sin\pi s)\,ds
 \tag{6}
\]
with its positive-real mark on \(0<v<1\), continued on the common
regular logarithmic cover. J proves from the literal signed crossing
that its variable-dependent principal action is
\[
 \begin{split}
 G_\sigma(\delta,V,J)={}&
 {\cal J}(\delta+V)+{\cal J}(J+\delta)
       -{\cal J}(V)-{\cal J}(J)-{\cal J}(\delta)\\
 &+i\pi\sigma\{-J-V+2VJ-\delta/2
                         +\delta(J+V)+\delta^2/2\}.
 \end{split}                                                   \tag{7}
\]
This is the action whose exponential scale is N, not \(N/c_0\),
where \(c_0=2\pi i\).

Substitute (5). Reflection \({\cal J}(1-v)=-{\cal J}(v)\)
and the conservation law \(A+B=u+z\) give, term by term,
\[
 \begin{split}
 G_\sigma={}&{\cal J}(u+z)-{\cal J}(u)-{\cal J}(z)
                         -{\cal J}(A)-{\cal J}(B)\\
 &+\frac{i\pi\sigma}{2}
           \{(z-u)(B-A)-(u+z)\}.
 \end{split}                                                   \tag{8}
\]
For the quadratic identity, expand the braces in (7) after
\(\delta=1-u-z\); the result is
\((z-u)B+(u^2-z^2-u-z)/2\), which is the second line of (8).
Thus no stationary equation or geometric assumption was used in
this simplification.

Summing over the whole diagram, the A and B permutations give
\[
 \begin{split}
 \Psi_{\rm ch}(u,z)={}&
 \sum_j\{{\cal J}(u_j+z_j)-2{\cal J}(u_j)-2{\cal J}(z_j)\}\\
 &+\frac{i\pi}{2}\sum_j\sigma_j
       \{(z_j-u_j)(B_j-A_j)-(u_j+z_j)\}\\
 ={}&\sum_jG_{\sigma_j}.
 \end{split}                                                   \tag{9}
\]
The equality first holds on the physical real interior, where all
primitives have their stated marks. It holds on every common analytic
continuation of that marked identity. Resetting a logarithm or
discarding its induced integral linear term is not permitted.

There is also a source-level reason this is the physical action:
J's finite clock elimination reconstructs the original signed
crossings and their closing factors, with every clock cap retained.
Its independent primitive calibration (27e)--(27g) fixes the clock
alias and additive constant. Thus (9) is not an identification based
only on an exponentiated stationary scheme.

For a general signed braid the singleton source in J has the same
physical-flow and regular clock elimination, including all prefix
histories. Hence its regular critical comparison with M is available
without alternation. The simpler post-clock coordinates (2), and the
exterior fiber below, are asserted here only for the actual alternating
closed diagram of C. A braidification or filling operation is not
assumed to preserve that presentation hypothesis.

## 3. The geometric point in these source coordinates

M's physical symbols, in a consistent factorial frame, give
\[
 {\cal G}_i=
 \begin{pmatrix}K_i&e_i\\K_if_i&K_i^{-1}+e_if_i\end{pmatrix},
 \qquad K_i+K_i^{-1}+e_if_i=-2
 \tag{10}
\]
at complete color. Let
\[
 b_{-,i}=\begin{pmatrix}1&0\\-K_if_i&K_i\end{pmatrix},\qquad
 {\cal B}_{-,j}=b_{-,j}\cdots b_{-,1}.
 \]
The actual meridians are
\[
 \mu_i=-{\cal B}_{-,i-1}^{-1}{\cal G}_i{\cal B}_{-,i-1}.
 \tag{11}
\]
M proves by the three triangular factorization identities that the
literal signed crossing maps become the Hurwitz meridian maps.
Its inverse is also explicit: for partial meridian products P,
take their triangular Gauss decomposition, and obtain the successive
K's from ratios of their upper-left entries, with the prescribed
central signs.

For the original closed word the positions and momenta are periodic.
The common nonzero momentum scale may be normalized at the cut; in
M's factorial frame this sets the first marked momentum to one.
J proves that this normalization loses no physical equation, since
the crossing relations determine every momentum ratio and the
diagram is connected. M then identifies the regular critical
scheme with the augmented representation scheme whose selected
meridian flag is 1. Its actual meridian eigenvalue is \(M^{-1}\);
at complete color both meridian eigenvalues coincide.

In particular choose the oriented complete geometric representation.
M's finite forbidden-line argument supplies a frame preserving that
flag in which all partial-product Gauss entries, required e's and f's,
and crossing denominators are nonzero. Its proof avoids finitely
many covector eigenlines and then finitely many vector lines; it
does not use a positive-shape assertion. Equations (3)--(5) therefore
give a regular complex charged critical point. Conversely, the
regular charged critical equations, together with the retained
momentum marking, recover that same representation through (11).

Choose the integer face logarithms w of D, so a physical lattice
point is \(w=c_0v/N\). Let \(U_j,Z_j,\mathsf A_j,\mathsf B_j\)
be its charge linear forms; for example \(U_j=c_0u_j\).
The geometric point has a definite integer critical character:
\[
                  \nabla_w W_*(w_*)=c_0 n,\qquad
                        n\in\mathbb Z^{c+1}.
 \tag{12}
\]
Here W is D's calibrated potential below. Equation (12) is the
ordinary exponentiated stationary equation with its logarithmic
lift restored. The alias-corrected critical potential is
\[
                       W_*^{[n]}(w)=W_*(w)-c_0 n\cdot w .
 \tag{13}
\]
No assertion is made that the original finite residue cycle gives
this character a nonzero coefficient. In D's convention
\(W_*+c_0m\cdot w\), this same character is \(m=-n\).

## 4. The calibrated critical value

D fixes, from the exact source factorials and all finite q shifts,
\[
 \begin{split}
 W_*(w)={}&\sum_j\{2\operatorname{Li}_2(e^{U_j})
       +2\operatorname{Li}_2(e^{Z_j})
       +\operatorname{Li}_2(e^{-U_j-Z_j})
                         -5\operatorname{Li}_2(1)\}+Q_*(w),\\
 Q_*={}&\sum_j\left\{\tfrac34U_j^2+\tfrac12U_jZ_j+
       \tfrac34Z_j^2+\tfrac{\sigma_j}{4}
           (Z_j-U_j)(\mathsf B_j-\mathsf A_j)
       -\tfrac{c_0(3+\sigma_j)}4(U_j+Z_j)\right\}.
 \end{split}                                                   \tag{14}
\]
The marked third logarithm is \(c_0-U_j-Z_j\). It is the
factorial index \(L_j+1\); its exact shift factor
\(1-e^{-U_j-Z_j}\) remains in D's amplitude. The real constant
\(-5c\operatorname{Li}_2(1)\) has not been chosen after evaluating
a geometric point. On the marked physical strip,
\[
                         W_*=c_0\Psi_{\rm ch}.
 \tag{15}
\]
One can verify (15) directly using the sine primitive (6), its
reflection, and dilogarithm inversion with
\(\operatorname{Log}(-e^{c_0s})=c_0s-\pi i\) for \(0<s<1\).
The quadratic terms then give exactly (14). D proves the stronger
exact factorial-function identity, including the pivot and d shift.

Let \({\cal D}\) denote the Bloch--Wigner function. Define the
charged rational pre-Bloch sum
\[
 \beta_{\rm ch}=\sum_j
       \{2[e^{U_j}]+2[e^{Z_j}]+[e^{-U_j-Z_j}]\}.
 \tag{16}
\]
This is the actual physical Bloch sum at complete color. To check
it locally, in M's factorial-basis positive crossing write the
physical multiplicative input/transfer coordinates as
\[
 a=e^{-U},\qquad b=e^{\mathsf B},\qquad t=e^{-U-Z}.
 \]
Its five-term class is
\([b]+[t]+[a^{-1}]-[bt]-[t/a]\).
Since \(\mathsf A+\mathsf B=U+Z\), it equals
\[
 [e^{\mathsf B}]+[e^{-U-Z}]+[e^U]
                      +[e^{\mathsf A}]+[e^Z]
 \tag{17}
\]
by rational inversion \([z^{-1}]=-[z]\).
For a negative crossing the physical input order is under,over;
M's independently derived inverse symbol gives the same expression
(17) in that physical port convention. There is no additional sign
inserted into its already oriented inverse symbol. The factorial
frame's input/output Bloch coboundaries cancel on shared strands
and the actual closed cut. Finally the A and B permutations turn
the whole sum of (17) into (16).

B gives a complete, degree-one diagram fundamental-cycle proof for
this physical class at the complete geometric representation. It
retains the central meridian signs, both crossing orientations,
the actual peripheral torus and preferred-longitude writhe shear.
Consequently
\[
               {\cal D}(\beta_{\rm ch}(w_*))
                              =\operatorname{Vol}(M).
 \tag{18}
\]
This uses B's explicit three-five-term certificate and face pairing,
not just equality of peripheral wedges.

Here is the exact action-to-regulator identity needed to apply (18).
For affine logs \(\ell_j=a_jw+ib_j\) with real a,b, and
\(w=\rho+i\theta\),
\[
 {\cal D}(e^{\ell_j})
   =\operatorname{Im}\operatorname{Li}_2(e^{\ell_j})
       -\rho\cdot\operatorname{Im}
                \nabla_w\operatorname{Li}_2(e^{\ell_j}).
 \tag{19}
\]
Indeed \(\operatorname{Log}|e^{\ell_j}|=a_j\rho\) and
\(\nabla\operatorname{Li}_2(e^{\ell_j})
       =-a_j\operatorname{Log}(1-e^{\ell_j})\).
For a real quadratic plus a pure imaginary linear term, its imaginary
part equals \(\rho\) times the imaginary gradient. Its real constant
has no imaginary part. Thus (14) and (19) give
\[
 \operatorname{Im}W_*(w)-\rho\cdot\operatorname{Im}\nabla W_*(w)
                            ={\cal D}(\beta_{\rm ch}(w)).
 \tag{20}
\]
This identity is preserved on the marked logarithmic cover:
dilogarithm monodromy adds an integral \(2\pi i\) linear log term
and a real period; its two contributions to the left cancel.
The pure imaginary affine offsets add only real constants to that
monodromy calculation.

At (12), equations (13),(18),(20) prove the calibrated value
\[
 \boxed{\displaystyle
       \operatorname{Re}\frac{W_*^{[n]}(w_*)}{c_0}
                       =\frac{\operatorname{Vol}(M)}{2\pi}.}
 \tag{21}
\]
This is the real part of the source's marked principal critical
action. It is not an estimate of its summed period.
The external factor is still exactly
\(\chi_N\kappa^{\mathrm{wr}}(x_0/s)^{b-1}N^{2c-1}\), as in C.
At the root the displayed \(\kappa\) and \(x_0/s\) are unit phases;
their extensive constants are not reinterpreted as volume.
The dimension/framing line \(\chi_N\) stays in its original
normalization. Likewise the exact pivot in D is
\(e^{-t^{\mathsf T}w}e^{c_0t_0/N}\), with its actual integer
closing forms, and stays in the amplitude. Replacing that pivot
by another logarithmic lift changes an alias mark and must be
accompanied by the corresponding linear action term.

## 5. The actual geometric exterior fiber

There is a direct way to test geometric membership without assigning
independent ideal angles to a crossing. In the original finite
physical basis \(K=x_0Q^{-a}\). Formula (3) gives exactly
\[
                  Q^{u_j}=x_0K_{j,\rm in},\qquad
                  Q^{z_j}=x_0K_{j,\rm out}^{-1},
 \tag{22}
\]
where in/out refer to the overstrand in its physical order.
At principal scale this becomes
\[
          e^{U_j}=-K_{j,\rm in},\qquad
          e^{Z_j}=-K_{j,\rm out}^{-1},\qquad
          e^{-U_j-Z_j}=K_{j,\rm out}/K_{j,\rm in}.
 \tag{23}
\]
The last finite source logarithm still has its \(L+1\) mark:
its finite exponential is \(QK_{\rm out}/K_{\rm in}\).

Fix the actual rightmost exterior circuit. Its crossing signs are all
\(\varepsilon\): position b is untouched between successive
\(\sigma_{b-1}\) occurrences, and their alternating under/over port
order forces their signs to agree. To choose analytic offset coordinates,
select one moving port as reference. For a positive circuit put
\[
     u_i=a_i,\quad z_i=b_i+y,\quad b_{i_0}=0;
 \]
for a negative circuit put
\[
     z_i=a_i,\quad u_i=b_i+y,\quad b_{i_0}=0.
 \tag{24}
\]
The lower-case a,b here are scaled offsets, not port permutations.
At physical integer data the reference can be a minimum moving
charge, giving the canonical nonnegative representative. At a
complex geometric point there is no operation “take the minimum”:
the reference and all logarithmic lifts in (24) are transported.

Restricting (9) to this genuine source direction yields, up to its
y-independent outside factor, the exterior action
\[
 \begin{split}
 \Psi_\varepsilon(y)={}&
 \sum_i\{{\cal J}(a_i+b_i+y)-2{\cal J}(b_i+y)\}\\
 &+i\varepsilon\pi\{k y^2/2+
                  y(\sum b_i-\sum a_i-k/2)\}.
 \end{split}                                                   \tag{25}
\]
This follows by differentiating (9) along the actual port cycle:
the fixed a terms are constant, and the A/B permutation sums on
that cycle reduce its quadratic term to the displayed expression.
The original pivotal shift is subprincipal and remains in the finite
fiber; it is not omitted from the finite polynomial.

For a full geometric critical point its derivative is
\[
                       \Psi_\varepsilon'(y_*)=2\pi i m,
                              \qquad m\in\mathbb Z,
 \tag{26}
\]
where m is the pairing of the full character n with this primitive
integer circulation. In particular exponentiation gives the following
explicit necessary equations on the geometric Gauss data:
\[
 \begin{array}{ll}
 \displaystyle\prod_{i\in I}
  \frac{1-K_{i,\rm out}/K_{i,\rm in}}
       {(1+K_{i,\rm out})^2}=1,&\varepsilon=+1,\\[3mm]
 \displaystyle\prod_{i\in I}
  \frac{1-K_{i,\rm in}/K_{i,\rm out}}
       {(1+K_{i,\rm in})^2}=1,&\varepsilon=-1 .
 \end{array}                                                   \tag{27}
\]
For verification write \(Y=e^{c_0y}\),
\(\alpha_i=e^{c_0(a_i+b_i)}\), \(\beta_i=e^{c_0b_i}\).
The sine derivative of (25) gives respectively
\[
 (-1)^ke^{c_0\sum(b_i-a_i)}Y^k
       \prod_i\frac{1-\alpha_iY}{(1-\beta_iY)^2},
 \qquad
       \prod_i\frac{1-\alpha_iY}{(1-\beta_iY)^2}.
 \]
Substitution of (23),(24) proves (27), including its signs.
Equations (27) forget the integer m in (26); that integer must
still be used in the selected finite cotangent phase.

## 6. A precise positive-sector test and the remaining cycle gate

D's five-shape chamber is, on the actual marked logs,
\[
 0<\operatorname{Im}U_j,\operatorname{Im}Z_j<\pi,\qquad
             \pi<\operatorname{Im}(U_j+Z_j)<2\pi .
 \tag{28}
\]
By (23), this is the concrete common-frame criterion
\[
 \operatorname{Arg}(-K_{j,\rm in}),
 \operatorname{Arg}(-K_{j,\rm out}^{-1})\in(0,\pi),
 \quad\text{their marked sum belongs to }(\pi,2\pi).
 \tag{29}
\]
There is no requirement that the K's have modulus one.
Nevertheless M's forbidden-line argument establishes nonvanishing,
not these simultaneous inequalities. A positive triangulation of the
manifold is likewise not a proof that these particular five diagram
shapes are positive in one actual source frame.

In fact the complete critical comparison proves a stronger exclusion.
No regular complete geometric critical point can satisfy (28), on
any of the original integer aliases. The reason is the retained
framing orbit, not failure of a particular radial estimate.

Here is the full proof. The selected meridian flag is fixed to 1.
Its projective stabilizer \(B_1\) has dimension two. For a
non-elementary boundary-parabolic representation, conjugation by
this stabilizer is locally free: an infinitesimal centralizer
would fix the distinct flags of three conjugate noncentral
parabolics, and a projective vector field with three zeros is zero.
M's regular chart is open, so this two-dimensional orbit stays in
it near the given point.

The orbit remains faithful after taking physical positions and
transfers, and hence after (5). Indeed if such a tangent fixes all
positions and transfers, the local generating relations make every
logarithmic momentum variation the same on the connected diagram.
The normalized first momentum makes that common variation zero.
Every physical generator and every meridian reconstructed by (11)
is then fixed. Local freeness forces the original tangent to be zero.
Thus there are two independent charged tangents to this orbit.

On a sufficiently small logarithmic neighborhood of that orbit the
integer vector n in (12) is constant, by continuity. Differentiating
(12) gives
\[
                  \dim\ker W_{*,ww}(w_*)\ge2 .
 \tag{30}
\]
The linear alias term (13) does not change this Hessian. No rigidity
or smoothness assertion about the unframed character variety is
needed for this argument.

On the other hand, D's five logarithmic row matrix is real and
injective on the fixed face coordinates. On (28) one has
\[
 \operatorname{Im}W_{*,ww}
     ={\cal A}^{\mathsf T}
        \operatorname{diag}_j\operatorname{Im}
                  \frac{e^{\ell_j}}{1-e^{\ell_j}}\,{\cal A}>0.
 \tag{31}
\]
Every diagonal term is positive and the source quadratic has real
Hessian. A complex symmetric matrix with positive definite imaginary
part has no nonzero complex kernel: pair a putative kernel vector
with its conjugate transpose and take the imaginary part.
This contradicts (30), proving the exclusion for every alias and
every regular common frame.

The mechanism has earlier coverage in
research_geometric_framing_excludes_acute_source.md for the
one-cut acute singleton chart. The proof here uses only the full
M/J framing and critical identities and D's distinct post-clock
Hessian; it does not import a contour conclusion from that coverage.
Fixing only one physical cut still leaves at least one of the two
null directions tangent to that cut. Two independent transverse
conditions are necessary to remove this particular framing
degeneracy. Imposing them is not yet a source-preserving operation.

This does not exclude the proved partial exterior coefficient.
For a one-variable critical point with fixed exterior offsets, whose
varying rows are positive, the logarithmic circulation direction h has
\[
 \operatorname{Im}\partial_h^2W_*
    =\sum_{\text{five rows}}(a_jh)^2
               \operatorname{Im}\frac{e^{\ell_j}}{1-e^{\ell_j}}>0.
 \tag{32}
\]
On each occurrence the moving charge supplies two slopes +1 and
one slope -1, so h is detected; the real source quadratic contributes
no imaginary second derivative. With the other coordinates fixed,
the imaginary action is strictly convex in its radial variable.
At the finite critical point its target slope is strictly inside
the interval of limiting slopes, since every positive shape supplies
a strictly interior beta angle. Its growth on both ends is therefore
positive linear. This proves a unique proper radial minimum on that
slice. Equivalently, in the physical y variable the horizontal
quadratic part of (25) has strictly negative real part.

The one-variable Legendre construction consequently has a nonzero local
Jacobian and strict boundary gap on a compact positive interval
calibrated at that critical radial coordinate, by the proof in D.
It does not compare the original physical cap and its alias
connectors with that calibrated interval. That comparison is exactly
what the completed fiber theorem proves on its specified neighborhood;
it has not been proved on all of (28).

Thus the regular complete geometric point and its correct volume
value are identified for the actual charged function. The positive
full five-shape chart cannot contain it merely by changing its
common frame or integer character. A continuation route must instead
retain the framing directions in a larger domain, or perform an
actual source-compatible reduction or polarization before using a
strictly positive full Hessian. Transport of the original capped
relative cycle still requires all endpoint and alias currents.
Neither the algebraic correspondence nor (21),(32) supplies its
coefficient for arbitrary fixed short partial fillings.
No meridian normal, off-grid physical operator, global noncancellation
or new volume-conjecture case is inferred.

## Complete direct sources

* C: notes/research_alternating_charged_checkerboard_polarization.md,
  435 lines, SHA256
  c7102909f30c008e45a8e7040a225f1de4164187709c5548ff316d49954f1098.
* D: notes/research_affine_legendre_actual_checkerboard_function.md,
  504 lines, SHA256
  d5b138e3537fe6c4eafe161e74c8be0cf7d861abfa0b2a8b6a3b0c7e13d46569.
* J: notes/research_joint_clock_phase_equations.md, 774 lines,
  SHA256 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867.
* M: notes/marked_braid_holonomy.md, 529 lines, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* B: notes/crossing_fundamental_cycle.md, 389 lines, SHA256
  0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f.

All five complete sources were read in this author sequence. The new
coordinate, phase, Bloch and sector comparisons are written above.
No programs, mathematical computations by code, tests or frozen-source
edits were used.
