# A local gluing test for positive coherent source contours

Research note, 6 November 2026. The exact adapted cycles of
[coherent polarization transport](research_actual_coherent_polarization_transport.md)
give legitimate representatives of the original finite contraction
through a regular complex critical configuration. They do not by
themselves give a negative restricted Hessian. This note extracts
an invariant one-wire obstruction and a composition rule from the
literal coherent resolution. The latter reduces positivity to
specified local coupon inequalities and the linearized gluing
relation, without a loss proportional to the number of internal
resolutions.

Neither inequality is asserted for every original signed crossing.
The known geometric channel Hessian supplies only a separate block.
Moreover, transporting lossless positive metrics around a complete
geometric peripheral loop is impossible: its actual nontrivial
parabolic holonomy is not nonexpansive in any positive metric.
This last obstruction concerns that proposed metric construction,
not the existence of a contributing complex saddle.

## 1. What the original resolution contributes

Use the exact kernels and measures of
[the compact source, Sections 1–2](compact_coherent_source_period.md).
There is one pair \((w_e,z_e)\) per resolved internal head edge.
Every edge occurs once as a row variable and once as a column
variable of the adjacent coupon kernels. The literal contraction
has one factor \(N\) per resolution and a factor
\((1+w_ez_e)^{-N-1}\) in its local measure. All actual turns,
pivots, boundary states, factorial frames and source lines remain
in the coupon tensors. The original external trace normalization
is unchanged.

Center an adapted frame at the specified point on every edge.
Suppose a chosen local principal phase \(\phi_v\) of each actual
coupon has been established in these frames. Then its assembled
phase is
\[
 F=\sum_v\phi_v-\sum_e\log(1+w_ez_e).
 \tag{1}
\]
In particular, the resolution contributes exactly
\(-\sum_e w_ez_e\) to the quadratic part. Using \(N-1\)
instead of \(N\) for a kernel's homogeneous degree changes its
amplitude, not this limiting coefficient. The two remaining
powers in the measure also remain in the amplitude.

Equation (1) is a consequence of the finite source factorization;
it is not a claim that arbitrary growing matrix kernels have a
uniform single-phase expansion. The same Hessian bookkeeping is
an exact finite identity with
\(N^{-1}\log K_{v,N}\) wherever these logarithms exist, with
the literal measure coefficient \((N+1)/N\). Establishing a
selected principal phase near the adapted geometric point remains
an analytic input. Centering that point at \((0,0)\) in a new
frame does not make it an original physical head endpoint.

## 2. A frame-invariant one-wire test

Let the original assembled phase be critical at the origin.
Fix all but one coherent wire and write
\[
 a=F_{ww},\qquad b=F_{wz},\qquad c=F_{zz}.
 \tag{2}
\]
All positive coherent spheres through this point have tangent
\(z=\lambda\overline w\), \(\lambda>0\), by the exact
classification in the preceding note. Its real second variation is
\[
 q_\lambda(w)=
 \Re\{(a+\lambda^2\overline c)w^2\}
                    +2\lambda\Re b\,|w|^2.
 \tag{3}
\]

**Proposition 1.** Some positive coherent tangent has a strictly
negative restriction on this wire if and only if
\[
             \boxed{\ \Re b+|\Re\sqrt{ac}|<0.\ }
 \tag{4}
\]
The square root's sign has no effect. For several wires, (4) is
necessary separately on each wire for a strictly negative product
restriction. It need not be sufficient when wires are coupled.

Indeed the maximum of (3) on \(|w|=1\) is
\(2\lambda\Re b+|a+\lambda^2\overline c|\). Also
\[
 \inf_{\lambda>0}\frac{|a/\lambda+\lambda\overline c|^2}{4}
     =\frac{|ac|+\Re(ac)}2
     =|\Re\sqrt{ac}|^2.
 \tag{5}
\]
When \(a,c\ne0\), the infimum is attained at
\(\lambda^2=|a|/|c|\). If exactly one vanishes it is approached
at an end of the positive half-line; the strict inequality in
(4) still gives a finite admissible \(\lambda\). If both vanish,
the conclusion is immediate. These cases prove the equivalence,
including the failure of strict negativity at equality.

After a fixed frame centers the coherent point, the remaining
frame changes preserving it are diagonal. Their action has form
\(w=r\widetilde w,z=r^{-1}\widetilde z\), \(r\ne0\).
Thus \(a\) changes to \(r^2a\), \(c\) to \(r^{-2}c\), and
\(b\) stays fixed. Both \(ac\) and (4) are invariant. Failure
of (4) therefore cannot be repaired by choosing another positive
metric sphere through the same point. This is a test of the
actual phase jets; complex nondegeneracy and the existence of a
positive tetrahedral phase do not imply it.

## 3. Local coupon defects compose with the exact edge budget

Choose positive numbers \(\lambda_e\), and write
\[
 w_e=u_e/\sqrt{\lambda_e},\qquad
 z_e=\sqrt{\lambda_e}\,\overline{u_e}.
 \tag{6}
\]
These are precisely the allowed product tangents. Treat each
\(u_e\) as two real coordinates. Let \(\iota_v u\) denote the
row and column perturbations incident to coupon \(v\), in their
actual order, including repeated occurrences when present.
For an internal port of that coupon define its quadratic defect by
\[
 q_v(u)=\Re\{(\iota_vu)^t\phi_v''(\iota_vu)\}
                   -\sum_{\text{internal ports at }v}|u_e|^2.
 \tag{7}
\]
Exterior arguments are fixed in this definition. If they are to
be varied, keep the corresponding half-port costs explicitly
instead of declaring them internal.

Each internal edge has exactly two ports. Differentiating (1)
therefore gives the exact identity of real quadratic forms
\[
                   \Re F''[\iota u,\iota u]=\sum_v q_v(u).
 \tag{8}
\]
No extra diagonal penalty has been inserted: the two port costs
are precisely the \(-2|u_e|^2\) furnished by its original
resolution. Linear terms cancel by the assembled stationary
equations, even when an individual coupon is not stationary.

**Proposition 2 (local gluing criterion).** Suppose each original
coupon satisfies, in the same edge weights (6),
\[
                  q_v(u)\le-\eta_v\|L_vu\|^2,
                           \qquad\eta_v>0,
 \tag{9}
\]
where \(L_v\) is a specified real linear map describing its
linearized port relation. Suppose the stacked map
\(L=(L_v)_v\), with the original exterior conditions imposed,
is injective on the retained integration variables. Then the
restricted Hessian is strictly negative. Quantitatively, if
\(s\) is the least singular value of this stacked map,
\[
            -\Re F''[\iota u,\iota u]
                     \ge (\min_v\eta_v)s^2\|u\|^2.
 \tag{10}
\]
The proof is just (8) and summation of (9). In particular the
gluing constants are those of the assembled linearized problem;
no separate error or exponential norm loss is introduced by
this Hessian identity. Metric norm estimates still have the
conditioning cost recorded in Section 6.
They can depend on the fixed word. No uniform positive lower
bound as the word length grows is asserted.

There is an equivalent qualitative version. If every \(q_v\)
is negative semidefinite and its kernel is exactly the specified
local gluing relation, the kernel of their sum is exactly the
intersection of those relations. On a finite-dimensional space,
injectivity of the assembled relation then gives (10) with some
positive constant. Both nonpositivity and the assertion about
the local kernels must be proved from the original coupons;
transversality alone supplies neither one.

This criterion is stable under assembling short components.
For an open component, include one \(|u_e|^2\) port cost
also at each variable boundary port. This records its boundary
normalized form, not its bare external phase. Gluing two such
ports gives exactly the two costs of the new internal resolution;
no boundary cost is discarded. Write the summed form as
\(-\|Cu\|^2\), split internal and
boundary variables, and assume its internal restriction is
strictly negative. Maximizing this quadratic form over the
internal real variables produces a nonpositive Schur form on
the boundary. Its kernel consists exactly of boundary variations
that extend to a vector in \(\ker C\). This follows from the
least-squares minimum: it vanishes precisely when all local
defects vanish. Consequently local relations and their defect
forms can be composed before a final transverse closure.
This is real quadratic elimination on the stated tangent, not
an assertion about integrating the original finite source.

The identity coupon gives an exact source check of the budget.
Its kernel is \((1+w_{\rm out}z_{\rm in})^{N-1}\).
With matching weights on its two ports, (7) is
\[
                    q_I=-|u_{\rm out}-u_{\rm in}|^2.
 \tag{11}
\]
Its kernel is precisely the linearized identity relation.
Frame insertions followed by their inverses satisfy the same
identity in the transported frames. This does not identify an
original crossing or a quantum turn with an identity coupon.
Their actual phase jets, including every chirp, must be used
in (7).

## 4. The coupon test can be read from its original canonical derivative

Consider an input-output coupon on a regular selected phase chart.
Its row/output and column/input ports are independent here, before
any self-loop or identification of repeated edges is imposed.
Write its phase as \(\phi(w_o,z_i)\), with output row variables
\(w_o\) and input column variables \(z_i\). Its coherent
generating equations, in the normalization of (1), are
\[
 \phi_{w_o}=\frac{z_o}{1+w_oz_o},\qquad
 \phi_{z_i}=\frac{w_i}{1+w_iz_i},
 \tag{12}
\]
componentwise. These are the stationarity equations of the two
adjacent literal resolutions. Identifying this selected phase
relation with the original crossing graph uses its actual
principal generator correspondence; an arbitrary algebraic
critical branch is not substituted for the selected phase.

Center all input and output points. Put
\(\phi''=\left(\begin{smallmatrix}A&B\\B^t&C\end{smallmatrix}\right)\).
Then (12) linearizes to
\[
 z_o=A w_o+B z_i,\qquad w_i=B^t w_o+C z_i.
 \tag{13}
\]
For the positive port weights, let
\[
 T_\lambda=\operatorname{diag}(\lambda_o^{-1/2},
                                      \lambda_i^{1/2}),\qquad
 H_\lambda=T_\lambda\phi''T_\lambda.
 \tag{14}
\]
Here the diagonal notation includes every input and output wire.
With \(\xi=(u_o,\overline{u_i})\), the boundary-normalized
coupon defect is exactly
\[
 q_v=\Re(\xi^tH_\lambda\xi)-\|\xi\|^2,
 \qquad
       q_v\le0\ \Longleftrightarrow\ \|H_\lambda\|_2\le1.
 \tag{15}
\]
For completeness, the real symmetric matrix for
\(\Re(\xi^tH_\lambda\xi)\) is
\(\left(\begin{smallmatrix}\Re H_\lambda&-\Im H_\lambda\\
 -\Im H_\lambda&-\Re H_\lambda\end{smallmatrix}\right)\).
It anticommutes with multiplication by \(i\), and its square
has the singular values of \(H_\lambda\) squared as
eigenvalues, each twice. Its largest eigenvalue is therefore
\(\|H_\lambda\|_2\), proving (15). After ports are identified,
their perturbations may occupy only a proper real subspace of
the independent port space. The norm condition remains sufficient
for the pulled-back defect, but is then not asserted necessary.

If (15) holds, the kernel of \(q_v\) is its real gradient
kernel. Differentiating the displayed quadratic gives precisely
(13) restricted to
\(z_i=\lambda_i\overline{w_i}\) and
\(z_o=\lambda_o\overline{w_o}\). Thus the kernel clause in
the qualitative version of Proposition 2 follows from the
original canonical relation. It is not an independent
transversality assumption once that relation and the local
nonpositivity test are established.

The Hessian in this test can be recovered directly from the
linearized original map, without computing second derivatives
of an unspecified action. For a coupon with equally many input
and output wires, write that map as
\(w_o=P w_i+Q z_i,\ z_o=R w_i+S z_i\). On a generating
chart where \(P\) is invertible, (13) gives
\[
 \phi''=
 \begin{pmatrix}
 RP^{-1}&P^{-t}\\
 P^{-1}&-P^{-1}Q
 \end{pmatrix}.
 \tag{16}
\]
The original symplectic identities make both diagonal blocks
symmetric and give \(S-RP^{-1}Q=P^{-t}\). If \(P\) is
singular, this particular generating chart is unavailable;
no inverse or local single-phase conclusion is assigned to it.

Equations (14)–(16) are consequently a concrete algebraic
test on the original regular Hurwitz/coupon derivative:
seek positive diagonal edge weights with all these local
symmetric matrices contractive, then impose the original
boundary-fixed linearized closure. Proposition 2's proof supplies
negativity when the closure is transverse. Invertibility of
the complex canonical map alone does not give (15), and this
note does not establish (15) for all actual signed crossings.

## 5. What the existing geometric block estimates supply

The [actual augmented-plat channel calculation](actual_augmented_plat_channel_hessian.md),
Sections 2–4, proves at a regular complete geometric endpoint,
after its specified internal root reduction and retained integer
characters,
\[
 F_{\xi,y}=0,\qquad
 F_{\xi_i\xi_j}=-\delta_{ij}\frac{4\pi i}{\tau_i},
 \qquad
 \Re\left(-\frac{4\pi i}{\tau_i}\right)
            =-\frac{4\pi\Im\tau_i}{|\tau_i|^2}<0.
 \tag{17}
\]
Here \(\tau_i\) is the actual oriented primitive cusp shape.
Thus physical real channel directions supply a negative block.
Because its magnetic mixed block is zero, this block cannot
repair a nonnegative magnetic tangent direction. Its physical
folded endpoint, logarithmic character and source coefficient
still require the original endpoint treatment. Nor does (17)
prove (9) for an arbitrary signed magnetic crossing.

There is a separate framing issue before demanding injectivity
in Proposition 2. The original closed coefficient phase has the
two-complex-dimensional framing radical proved in
[the actual geometric normal-period theorem, Sections 3–4](actual_geometric_normal_period.md).
If a holomorphic Hessian in complex dimension \(d\) has complex
rank \(d-r\), the real part of its quadratic form has positive
and negative indices both \(d-r\). To see this, take a complex
congruence to \(\operatorname{diag}(I_{d-r},0)\), then split
real and imaginary coordinates. It cannot be negative definite
on a real \(d\)-dimensional contour when \(r>0\).

Accordingly the full closed coefficient phase cannot acquire
an isolated negative Gaussian merely by changing its real
contour. A regular local Fourier/stationary presentation that
preserves this critical scheme also preserves its radical.
The [actual Fourier partial family](actual_fourier_polarized_geometric_normal_block.md)
does fix external variables and supplies a nondegenerate
transverse block; its remaining scalar summation is still part
of the actual source. A gauge-fixed Hessian test must retain that
external pairing, rather than replacing it by evaluation in a
chosen frame.

The positive geometric tetrahedral chart gives a different,
genuinely negative angular contour in
[the Legendre construction](general_legendre_rivin_contour.md).
The existing actual-character identification transports its
critical scheme and regulator, not an off-critical identity
between that angular contour and the product tangents (6).
That is why its Hessian positivity cannot yet be substituted
for the coupon inequalities (9).

## 6. Flat lossless positive metrics fail at the actual parabolic loop

One tempting way to obtain (9) is to assign positive Hermitian
forms at transported geometric flags and declare every original
geometric transport nonexpansive in those forms. The following
elementary obstruction applies to that construction.

Suppose invertible two-dimensional transports \(g_e\) along
an oriented closed loop satisfy
\[
                       g_e^*H_{e+1}g_e\le H_e,
                  \qquad H_e>0,\quad H_{\rm final}=H_0.
 \tag{18}
\]
Multiplication gives \(P^*H_0P\le H_0\) for its actual ordered
holonomy \(P\), hence \(\|P^k\|_{H_0}\le1\) for all positive
integers \(k\). If
\[
                 P=\pm(I+T),\qquad T^2=0,\quad T\ne0,
 \tag{19}
\]
choose \(v\) with \(Tv\ne0\). Then
\(\|P^kv\|_{H_0}\ge k\|Tv\|_{H_0}-\|v\|_{H_0}\), a
contradiction. The actual complete geometric meridians and
nontrivial peripheral translations have exactly (19), with
their original central signs. Therefore no such positive
lossless metric can close around their loop.

This statement uses the actual geometric \(2\times2\)
transport. It does not claim that an original quantum crossing
equals the symmetric power of a meridian matrix. It rules out
the proposed inference from a flat positive geometric metric
to automatic coupon positivity. An adapted contour with a
negative real Hessian need not satisfy (18), so it is not
excluded by this argument.

The cost of allowing nonisometric frame transport remains
exponential. In the induced binomial head metric,
\[
          \|\operatorname{Sym}^{N-1}g\|=\|g\|^{N-1},
 \qquad
 \operatorname{cond}(\operatorname{Sym}^{N-1}g)
                          =\operatorname{cond}(g)^{N-1}.
 \tag{20}
\]
For a fixed positive metric a nontrivial parabolic has norm
strictly greater than one, by the same power argument. Its
normalization cost therefore cannot be declared polynomial.
There is no metric-independent positive lower bound for this
cost: conjugating a unipotent can make its off-diagonal entry
arbitrarily small, while the conjugating metrics degenerate.
Exact internal frame factors cancel in the full scalar; separate
positive norm estimates must keep (20).

## 7. The remaining actual calculation is local and specific

The new finite-dimensional task is to calculate the original
selected crossing and turn Hessians in adapted coherent frames,
first check the invariant obstruction (4), and then seek common
positive edge weights for (7)–(9). If that succeeds and the
appropriate boundary-fixed linearized gluing is injective,
Proposition 2 proves a negative product restriction for the
whole fixed short component. A uniform local phase expansion
and a strict upper bound for the complement of this exact source
cycle remain necessary before concluding a nonzero scalar
geometric contribution.

The present deductions do not verify (9) for arbitrary signed
crossings, identify a whole-source geometric coefficient, or
establish the finite-exception theorem. They give a composable
source-normalized test and isolate why positive geometric
gluing and bounded meridians alone do not discharge it.
