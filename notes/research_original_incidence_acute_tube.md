# An acute complex domain for the original knot source

Private written deduction, 15 November 2026. This note concerns the
original complete-color crossing, bends and reduced marked closure. It
uses no numerical calculation or mathematical code.

There is a convex complex domain on which the complete incidence action
has an injective gradient and a nonsingular Hessian, at every imaginary
height. Its existence has a direct diagrammatic characterization: the
chosen knot diagram must alternate between over and under encounters.
The statement applies to a general Morse diagram, so it does not require
an alternating closed-braid presentation. After fixing the cut, an
explicit lower bound for the Hermitian part of the negative Hessian is
independent of the number of crossings.

This constructs a domain for the original action, not a critical point
in that domain. It does not prove that the complete hyperbolic
representation has an acute decoration or that its descending cycle
occurs in the original finite sum.

## 1. The retained Morse source and its cut

Choose a Morse drawing of an oriented knot with \(c>0\) crossings. Each
crossing is read in its actual ordered vertical frame. Its physical
sign \(\sigma_j\) is the sign of that local balanced crossing coupon;
it need not equal the oriented writhe sign after bending the strands.
All original framing factors remain outside the tensor contraction.
Fix \(N\ge2\) and set
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad x=q^d,\qquad
 \kappa=q^{d^2/2},\qquad
 S_r=\prod_{k=1}^r2\sin(\pi k/N),\quad S_0=1.
 \tag{1}
\]
At a crossing the physical overstrand runs from \(I=u+v\) to \(v\),
and the understrand from \(J\) to \(J+u\), in the local downward
reading. The original crossing entry has the exact expansion
\[
 R_\sigma(I,J;v,J+u)
 =\kappa^\sigma N
   \sum_{h=v}^{u+v}
   \frac{q^{[N+\sigma(u+1+2J)]h-\sigma dJ}}
   {S_{d-u-v}S_{u-h+v}S_{h-v}S_v}.
 \tag{2}
\]
The displayed arguments specify the over/under degrees; the checked
matrix orders them as prescribed by \(\sigma\). Formula (2) is the
entrywise clock identity proved in Section 4 of the joint-phase note.
It holds at every level, with both endpoints and the full original
normalization. In particular it can be inserted in a Morse contraction
without first proving a braid formula for that contraction.

In literal left-to-right head order \((i,j)\), the original root bends
are
\[
 p_{ij}=Nq^{-d^2+di}\mathbf1_{i+j=d},\qquad
 \ell_{ij}=N^{-1}q^{di}\mathbf1_{i+j=d}.
 \tag{3}
\]
The exposed marked cap is the original array
\(m_{ij}=x^j/N^2\), without a support restriction imposed on that
array. These are the actual left/right duality maps in their balanced
frames, not new boundary conditions. The general Morse source theorem
keeps the actual module/dual identifications and all crossing frames.
Although the earlier all-MAIN transport statement was phrased for
\(N\ge3\), its pivotal and Morse proof uses only nonvanishing of
\([a]_q\) for \(1\le a<N\). The literal bends, invariant-line
argument and regular lift here also hold at \(N=2\), as follows
directly from the regular-bends proof and physical matrices.
For example, comparison of the ordered right cap with (3) gives
\(q^{-2Ni}=1\) on the integer grid; the corresponding cup comparison
gives \(q^{2N(d-i)}=1\). On continued logarithmic lifts these are
recorded linear Fourier characters. They contribute no Hessian and
must not be used to identify different selected cycles.

There is an exact fixed-cut version of this source. Remove the one
marked cap and call the remaining two-ended tensor \(T\). Integer
weight conservation forces its support to be \(i+j=d\). It is an
invariant tensor, so
\[
                         T=C_Np.                       \tag{4}
\]
For clarity, the invariant line is one-dimensional already at the
root. Pair weight one occurs only at total degree \(d\), putting an
invariant vector in the span of \(|i,d-i\rangle\). The raising
equation then determines consecutive
coefficients from the first, since all its adjacent coefficients are
nonzero. The supported cup in (3) spans that line. Alternatively the
regular pivotal lift in the Morse source proves the same assertion
before specialization. Consequently
\[
 m(T)=C_N,\qquad
 \frac{x^{d-r}}{N}\,T_{r,d-r}=C_N
                  \quad(0\le r<N).                    \tag{5}
\]
The second formula is exactly \(N\) times the corresponding marked
summand, not its replacement by an ordinary cap. It is proved for the
whole invariant tensor before individual clock terms are separated.
It remains valid when \(C_N=0\).

We may therefore use any one chosen cut degree \(r\), expand (2) at
every crossing, and keep every admissible physical flow and clock.
The resulting equality is for the original scalar, including its
chosen framing. Every ordinary bend contributes the monomial in (3),
and the fixed cut contributes exactly the monomial in (5). Their
powers of \(N\) are explicit scalar factors. Their logarithmic phases
are affine functions of the physical degrees. No summation sector,
normal coefficient, or finite Fourier alias has been removed by (2).

## 2. Independent flow coordinates through arbitrary bends

Follow the chosen orientation of the knot. On a vertical segment let
\(\eta=1\) when the traversal is downward and \(\eta=-1\) when it is
upward. For a physical degree \(a\), put
\[
                         X=\eta(a-d/2).                \tag{6}
\]
At a bend the degree changes to \(d-a\) and \(\eta\) changes sign,
so \(X\) is unchanged. Passing an overcrossing changes \(X\) by
\(-u_j\); passing an undercrossing changes it by \(+u_j\). For an
upward traversal both the order of the physical endpoints and the
sign \(\eta\) reverse, giving the same two rules.

Fix the physical degree on the marked cut. Arbitrary integral
transfers \((u_1,\ldots,u_c)\) now determine every physical degree
uniquely by following the knot. On returning to the cut the total
increment is zero, since each crossing has been encountered once
over and once under. There is no additional linear closure equation.
At finite \(N\), the half-integral centering when \(d\) is odd creates
no index condition: propagation uses only integral additions and
the integral replacement \(a\mapsto d-a\).

The clocks \(h_1,\ldots,h_c\) in (2) are independent before their
inequalities are imposed. Thus
\[
                    (u_1,\ldots,u_c,h_1,\ldots,h_c)
 \tag{7}
\]
are integral coordinates on the homogeneous fixed-cut incidence
lattice. The feasible finite states still obey every original degree
bound and \(v_j\le h_j\le u_j+v_j\). We do not assert that this
feasible set is full-dimensional for every finite cut.

For the leading action use scaled variables \(U,V,J,H,A\), and let
\(A_*=A\) be the fixed cut parameter. The limiting crossing
incidences are
\[
 n_j=(1-U_j-V_j,\ U_j-H_j+V_j,\ H_j-V_j,\ V_j).
 \tag{8}
\]
Here all physical degrees, including every \(J_j,V_j\), are real
affine functions of the transfer coordinates and the cut parameter.
The event sums in (8) are one. Here \(n_j\) denotes the limiting
normalized incidence tuple; the finite charges in (2) are integers.
The exact \(d=N-1\) shifts in (2) remain in the finite source and
are not silently changed there.

## 3. When the acute domain exists

On the fixed-cut complex affine space define
\[
 \Omega_{A_*}
   =\{z:\ 0<\Re n_{ja}(z)<1/2
                  \text{ for all }j,\ a=0,1,2,3\}.
 \tag{9}
\]
It is open and convex, and is a tube over its real affine
inequalities. The cut may be complex. Write
\(X_* = \eta_*(A_*-1/2)\), with the traversal sign on the selected
cut segment. The next encounter is the next crossing along the knot;
intervening bends do not count as encounters.

**Theorem 1.** The domain (9) is nonempty if and only if the cyclic
over/under encounter word of this diagram alternates, and
\[
 \begin{cases}
 0<\Re X_*<1/2,&\text{the next encounter is over},\\
 -1/2<\Re X_*<0,&\text{the next encounter is under}.
 \end{cases}                                           \tag{10}
\]
In particular a cut with \(\Re A_*=1/2\) never belongs to this
acute domain. Every alternating knot has a Morse diagram for which
(9) is nonempty after a compatible cut is chosen. This last statement
does not require that the knot have an alternating closed braid.

**Proof.** The first and last inequalities of (8) imply
\[
       1/2<\Re I_j<1,\qquad 0<\Re v_j<1/2.             \tag{11}
\]
In oriented centered degrees, an over encounter therefore takes a
positive real part to a negative one, irrespective of whether that
strand is read upward or downward. If two successive encounters were
both over, the intervening degree would have to be both negative and
positive. Bends cannot change it. Such successive overs are impossible.
There are exactly \(c\) over encounters and \(c\) under encounters
in the cyclic word. The absence of adjacent overs forces each gap
between overs to contain exactly one under encounter. The word
alternates. Equations (11) then also force (10), by following the
segment containing the cut.

Conversely let the word alternate and put
\(\kappa_0=|\Re X_*|\in(0,1/2)\), \(\tau=\Im X_*\).
Give every oriented segment from an under encounter to an over
encounter the value \(X=\kappa_0+i\tau\), and every segment from
over to under the value \(X=-\kappa_0+i\tau\). These agree through
bends by (6) and give the prescribed cut. Every transfer is
\(U_j=2\kappa_0\). On the overstrand at crossing \(j\), with its
traversal sign \(\eta_j\), the physical values are
\[
 I_j=1/2+\kappa_0+i\eta_j\tau,\qquad
 V_j=1/2-\kappa_0+i\eta_j\tau.
\]
Choose \(H_j=1/2+i\eta_j\tau\). The four real parts in (8) are
\[
              (1/2-\kappa_0,\ \kappa_0,\ \kappa_0,
                                      \ 1/2-\kappa_0),
\]
all strictly between zero and one-half. The physical under degrees
have the corresponding values with that strand's traversal sign, so
all crossing conservation equations hold. This constructs a point of
(9). A small Morse perturbation of an alternating drawing preserves
its encounter word, proving the final assertion. \(\square\)

The domain has a direct test in the algebraic incidence coordinates.
Put \(Z_{ja}=e^{2\pi i n_{ja}}\). On the chosen strip
\(0<\Re n_{ja}<1\),
\[
       0<\Re n_{ja}<1/2
                 \quad\Longleftrightarrow\quad \Im Z_{ja}>0.
 \tag{12}
\]
Indeed \(\Im Z=e^{-2\pi\Im n}\sin(2\pi\Re n)\).
Thus the acute test is semialgebraic in the real and imaginary parts
of these exponentials. Their chosen additive lifts and the actual
wire equations remain necessary. Equation (12) does not identify
the incidence exponentials with shapes of a knot-complement
triangulation.

## 4. The full Hessian, including every phase term

Let \(\mathcal J\) be the primitive of
\(\Log(2\sin\pi z)\) on \(0<\Re z<1\), normalized to agree with
the real integral from zero. The sine has positive real part there,
so this logarithm is unambiguous. Reflection gives
\(\mathcal J(z)+\mathcal J(1-z)=0\).

Equations (2)--(3), after the fixed-cut contraction, give the
variable-dependent leading action
\[
 \mathscr S(z)=-\sum_{j,a}\mathcal J(n_{ja}(z))
                        +i\pi\mathcal Q(z),             \tag{13}
\]
where
\[
 \mathcal Q=
   \sum_j\{H_j+\sigma_jH_j(U_j+2J_j)-\sigma_jJ_j\}
                       +B_{\rm bends}.                 \tag{14}
\]
The bend contribution \(B_{\rm bends}\) is the affine expression
with real coefficients specified by their retained monomials before
the cut is fixed, including the fixed-cut
monomial and any recorded linear Fourier characters. There is no
entropy contribution from these bends. If a closing row is inserted
as a pair \((A,1-A)\), its two \(\mathcal J\) terms cancel exactly.
All state-independent framing factors, powers of \(N\), and the
\(N-1\) shifts remain part of the finite expression. Formula (13)
concerns its leading action, not an exact equality of finite amplitudes.

In the real integral coordinates (7), let \(L\) be the real matrix
of the crossing incidence map, so \(dn=L\,dz\). The Hessian
\(\mathcal H=\mathcal Q''\) is real symmetric even if the fixed
cut parameter is complex; that parameter changes only affine terms.
For a Fourier lift \(k\in\mathbb Z^{2c}\), put
\(\mathscr S_k=\mathscr S-2\pi i\,k\cdot z\). Then
\[
 -\mathscr S_k''
   =\pi L^{\mathsf T}\operatorname{diag}
                           (\cot\pi n_e)L-i\pi\mathcal H.
 \tag{15}
\]
No part of the quadratic phase has been omitted in this formula.

**Theorem 2.** On every nonempty domain (9), the Hermitian part of
\(-\mathscr S_k''\) is positive definite. The map
\(-\nabla\mathscr S_k\) is injective there. Thus there is at most
one critical point for each specified Fourier lift, and any such
point has nonsingular Hessian.

If \(\Re\cot(\pi n_e)\ge\mu>0\) throughout a convex subset of
(9), then in the coordinates (7)
\[
        \operatorname{Herm}(-\mathscr S_k'')
                                      \ge\frac{\pi\mu}{3}I.
 \tag{16}
\]
The same lower bound holds for every principal Schur complement of
\(-\mathscr S_k''\). In particular any stationary elimination
within this domain has a nonsingular reduced Hessian.

**Proof.** Directly,
\[
 \Re\cot\pi(x+iy)
       =\frac{\sin(2\pi x)}{\cosh(2\pi y)-\cos(2\pi x)}>0
                         \quad(0<x<1/2).               \tag{17}
\]
The term \(-i\pi\mathcal H\) is skew-Hermitian. Since \(L\) is
real, (15) therefore has Hermitian part
\(\pi L^{\mathsf T}\operatorname{diag}(\Re\cot\pi n_e)L\).
The incidence map detects every coordinate: at crossing \(j\),
\[
 \delta U_j=\delta n_{j1}+\delta n_{j2},\qquad
 \delta H_j=\delta n_{j2}+\delta n_{j3}.
\]
The matrix of these two sums has squared operator norm three.
Consequently, for complex variations as well as real ones,
\[
 \sum_{j,a}|\delta n_{ja}|^2
       \ge\frac13\sum_j(|\delta U_j|^2+|\delta H_j|^2).
 \tag{18}
\]
This proves positive definiteness and (16).

Write \(G=-\nabla\mathscr S_k\). Convexity of (9) gives, for
\(z\ne w\) and \(v=z-w\),
\[
 \Re\bigl(v^*[G(z)-G(w)]\bigr)
  =\int_0^1\Re\bigl(v^*DG(w+tv)v\bigr)\,dt>0.          \tag{19}
\]
Hence \(G\) is injective; its differential is nonsingular by the
same positive quadratic-form test. On a segment where (16) holds,
Cauchy--Schwarz also gives
\[
              |G(z)-G(w)|\ge(\pi\mu/3)|z-w|.           \tag{20}
\]

Finally partition \(M=-\mathscr S_k''\) as
\(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\).
The positive Hermitian part makes \(A\) invertible. For
\(w=(-A^{-1}Bv,v)\),
\[
 w^*Mw=v^*(D-CA^{-1}B)v.
\]
If \(\operatorname{Herm}M\ge\alpha I\), the real part is at
least \(\alpha\|w\|^2\ge\alpha\|v\|^2\). This proves the
Schur assertion, including (16). The usual implicit differentiation
of a stationary eliminated block identifies this Schur complement
with the negative reduced Hessian. \(\square\)

For example a region with
\(\epsilon\le\Re n_e\le1/2-\epsilon\) and
\(|\Im n_e|\le T\), where \(0<\epsilon<1/4\), has
\[
          \mu=\frac{\sin(2\pi\epsilon)}{\cosh(2\pi T)+1}.
 \tag{21}
\]
The constants in (18) and (21) do not depend on the number of
crossings. The estimate applies only while the displayed incidence
bounds hold; it does not assert such bounds for a family of geometric
knot representations.

There is also a finite bound on the Fourier lifts which can have a
critical point anywhere in the tube, including unbounded imaginary
heights. Write the fixed-cut quadratic in the coordinates (7) as
\[
 \mathcal Q(z)=\tfrac12z^{\mathsf T}\mathcal Hz+b^{\mathsf T}z+b_0.
\]
The vector \(b\) may depend on the complex cut. On (9),
\(0<\Re U_j,\Re H_j<1\), and
\(|\Im\Log(2\sin\pi n_e)|<\pi/2\). Therefore a critical point
of \(\mathscr S_k\) must satisfy
\[
 |k_\alpha|\le
 \frac14\sum_e|L_{e\alpha}|
 +\frac12\sum_\beta|\mathcal H_{\alpha\beta}|\,+\,
 \frac12|\Re b_\alpha|.                               \tag{22}
\]
To see this, take imaginary parts of
\(-L^{\mathsf T}\Log(2\sin\pi n)+i\pi(\mathcal Hz+b)=2\pi i k\)
and use the preceding bounds. The right side of (22) depends on the
fixed diagram, cut and recorded lift, not on imaginary height or
the level \(N\). Only finitely many integral \(k\) occur, and
Theorem 2 permits at most one critical point for each. Thus the
entire acute critical set on these Fourier lifts is finite and
nonsingular. This count makes no assertion about critical points
outside (9).

## 5. The clock chart and the remaining existence question

The regular clock graph of the original action is already known
explicitly. On its canonical lift,
\[
 R=H-V=\frac U2-\frac{\sigma i}{2\pi}\mathcal L,
 \qquad
 \mathcal L=\Log(2\sin\pi(J+U))-\Log(2\sin\pi J).
 \tag{23}
\]
The formula is continued with those two logarithms. Its four
incidences are \((1-U-V,U-R,R,V)\). Put \(a=\Re U\).
Substitution in (9) gives the exact acute conditions on this graph:
\[
 \begin{gathered}
 0<\Re V<1/2,\qquad 1/2<\Re(U+V)<1,\qquad 0<a<1,\\
       |\Im\mathcal L|<\pi\min(a,1-a).
 \end{gathered}                                        \tag{24}
\]
Indeed the real parts of \(R,U-R\) are
\(a/2\pm\sigma\Im\mathcal L/(2\pi)\). For real physical
\(U,J\) with \(0<J<J+U<1\), the logarithmic difference is real,
so the last inequality is automatic. The two outer inequalities
are additional restrictions even in that physical strip. At a
complex geometric point the last inequality is also a genuine test.
The known rational clock elimination does not imply it.

Within the acute domain the clock Fourier characters are in fact
forced. All physical wire degrees have real parts in \((0,1)\):
the acute inequalities put both over endpoints there, and the
alternating intervening under encounter and complementary bends
preserve those bounds. Thus \(0<\Re(U+2J)<2\). The clock derivative
has imaginary part
\[
 \arg(2\sin\pi n_1)-\arg(2\sin\pi n_2)
                      +\pi[1+\sigma\Re(U+2J)].
\]
The argument difference belongs to \((-\pi,\pi)\). The displayed
quantity therefore lies in \((0,4\pi)\) for \(\sigma=1\), and
in \((-2\pi,2\pi)\) for \(\sigma=-1\). At a critical point it
must equal \(2\pi k_H\), so necessarily
\[
                         k_H=(1+\sigma)/2.             \tag{25}
\]
Only the physical-flow Fourier characters remain to be checked in
the finite box (22). Formula (25) is relative to the complete source
action (13)--(14); it does not equate unrelated logarithmic lifts.

The earlier cone-chamber theorem already proves univalence by a
positive Hermitian Hessian for the circle-tree edge action. The new
content here is the exact feasibility characterization for the
complete original crossing source, its general Morse and fixed-cut
form, and the quantitative estimate (18). We do not claim a new
general theorem about accretive maps or Schur complements.

Three further conclusions do not follow from this result. First,
(9) being nonempty does not put any prescribed target in the image
of its injective gradient. Second, (17) tends to zero at unbounded
imaginary height, so it gives no coercive bound at infinity; and a
face \(\Re n_e=1/2\) is not a singularity of the logarithm which
could itself prevent an escape. Third, a unique nondegenerate
critical point in (9) would still need a source-preserving contour
deformation and a nonzero intersection coefficient. Neither the
finite fixed-cut identity nor the Schur determinant provides that
coefficient. In particular (12) and (24) are checks on a proposed
geometric decoration, not a proof that every hyperbolic alternating
knot has one satisfying them.

## 6. No real interior saddle of the complete Morse action

There is a distinction between the real positive assignments
constructed in Theorem 1 and a real critical point. In fact the latter
cannot occur for any nonempty knot diagram, even outside the acute
subdomain.

**Proposition 3.** In the regular real physical interior of this
fixed-cut Morse source, the full leading action has no critical
point on any integral Fourier lift.

Here the physical interior requires every crossing incidence and
every physical degree to lie strictly within its original bounds.
The cut is real. The assertion concerns the complete action with
all bend phases; it does not exclude a complex critical point.

**Proof.** The clock coordinates are independent, and bends have no
clock dependence. Put \(R_j=H_j-V_j\). The real part of the clock
equation is
\[
 \sin\pi(U_j-R_j)=\sin\pi R_j.
\]
Since \(0<R_j<U_j<1\), it forces \(R_j=U_j/2\). The imaginary
part, including a possible integral Fourier character, says
\[
        1+\sigma_j(U_j+2J_j)\in2\mathbb Z.
\]
The physical bounds give \(0<U_j+2J_j<2\), so
\(U_j+2J_j=1\) at either sign. In oriented centered degrees each
under encounter consequently runs from \(-U_j/2\) to \(+U_j/2\),
also when traversed upward. Two consecutive under encounters are
impossible. Equal numbers of over and under encounters again force
alternation.

Let the over encounter of crossing \(j\) lie between the under
encounters of crossings \(p(j)\) and \(q(j)\) along the knot. Its
transfer then gives
\[
                  2U_j=U_{p(j)}+U_{q(j)}.              \tag{26}
\]
The directed graph with arrows \(j\to p(j),j\to q(j)\), counted
with multiplicity, has two incoming and two outgoing arrows at every
vertex. Its underlying graph is connected: it is obtained from the
connected cyclic encounter graph by identifying the two occurrences
of each crossing. Such a balanced connected directed graph is strongly
connected. Indeed a source component of its acyclic condensation has
no incoming arrows; balance forces it to have no outgoing arrows,
contradicting connectedness unless it is the only component.
Apply the maximum principle to (26). A vertex of largest \(U_j\)
forces both its successors to have the same value; strong connectivity
then makes all transfers equal. At every over encounter the centered
input and output are now \(+U_j/2,-U_j/2\), so
\(V_j=(1-U_j)/2\) and \(H_j=1/2\).

Hold all clocks fixed at these values and vary the independent
transfer coordinates. The crossing part of (14) has differential
\[
                       \tfrac12\sum_j\sigma_j\,dU_j.  \tag{27}
\]
The \(dJ_j\) terms cancel because their coefficients are
\(\sigma_j(2H_j-1)\). Every physical degree is an integer-affine
function of the transfers and the fixed cut, by Section 2. The root
bend monomials (3) therefore make
\(dB_{\rm bends}\) an integer covector in these transfer coordinates.
The recorded left/right corrections add even integer covectors.
The fixed-cut coefficient is constant under these variations.

The integral tangent with \(dU_j=1\), all other transfers and all
clocks fixed, is allowed in the homogeneous lattice. At the supposed
real critical point the imaginary action derivative on it is
\[
                         \pi(\sigma_j/2+m),\qquad m\in\mathbb Z,
\]
which is never a multiple of \(2\pi\). The entropy derivative is
real. Thus no integral Fourier character can make the full derivative
zero. This contradiction proves the proposition. \(\square\)

This extends the previously derived closed-braid exclusion by using
the actual Morse bends and the free transfer lattice. In particular,
the existence of an acute positive real configuration cannot supply
the missing saddle merely by retaining that real configuration.

## 7. Direct sources

The directly used written statements were read at these versions:

* `research_joint_clock_phase_equations.md`,
  `71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867`:
  Sections 2--5 give the actual crossing degree convention, entrywise
  coherent clock expansion, complete leading action, and canonical
  clock graph used in (2), (8), (13)--(14), and (23).
* `research_arbitrary_main_edge_mark_transport.md`,
  `7a7c9efdca1e9f7907dc5baf5dfe8ba12e2345ee5f2df2ed94240e95ee69112a`:
  Sections 2--5 give the regular actual pivotal lift, Morse rerouting,
  original marked scalar, and all ordered bend coefficients and
  their linear Fourier corrections.
* `research_matched_sphere_morse_source.md`,
  `8fdfde4a0d83220f3709048f00cd9373cfbc9d14b05943e9f16f58ab50777f4f`:
  Sections 4--5 retain the actual module/dual frames in a newly drawn
  Morse network, rather than only in a rerouted flat diagram.
* `research_rivin_jones_regular_bends_and_newton_turn.md`,
  `ced2c87e74c255d68f367d553fb5b36da9432a90d59687823fa6401778b72af0`:
  Sections 1--3 prove invariant bends, their regular physical adapter,
  literal root scalars and marked row.
* `papers/newton-calculus/finite.tex`,
  `2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e`:
  the physical generators, cup and cap, marked closure, and actual
  self-dual turn in Sections 1--2.
* `research_cone_chamber_accretivity.md`,
  `7dd2888717147bd7e48c2d8a08c8ea9819c12329a9b2e83e02c40c27cf8da803`:
  Sections 4--6 give the existing accretive-gradient argument and
  explicitly separate its regional conclusion from cycle transport.

The proof above supplies the new incidence and Morse implications;
no numerical tests or unproved geometric-gluing claim are used.
