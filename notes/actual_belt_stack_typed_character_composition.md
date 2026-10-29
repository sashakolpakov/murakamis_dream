# Typed belt-stack character composition and marked peripherals

29 October 2026. The actual mixed inner packet has a regular character
lift through the complete pair-Casimir value -2. This note proves the
signed crossing/box composition, including the sharp box's meridian
flag, and the exact ordinary-cup outer dictionary. It constructs the
marked deformed representation of the actual signed belt stack.
Every incident mixed crossing is transported through the SAME
original Hopf-duality adapters. The outer dictionary is NOT inferred
from a Hessian or from relabeling indices while leaving coupons fixed.

## 1. Regular pair frame at the actual complete source

Use the [regular local port chart](actual_belt_stack_regular_parabolic_port_chart.md).
Set c=w+w^(-1), w=-exp eta, and

    a=-[[1,1],[0,1]], b=-[[1,0],[c-2,1]],
    A=ba=[[1,1],[c-2,c-1]].                              (1)

These main meridians have trace -2. The central signs do not affect
their PSL classes; both signs in their product cancel. They form an
irreducible pair near c=-2, including that point.

For the source-selected local z=mathscrR(R^(-1)L_(N-h)) branch,
let X,Y,H,L,U be the literal stationary functions of
[the mixed local source lift](actual_pretzel_mixed_regular_character_lift.md),
continued through the quarter point using the newly proved actual
auxiliary-color packet. They satisfy

    U=(wY-1)/(w-Y), L=(H-X)/(1-HX),
    (1+YL)/(1+Y/L)=L^2/H.                               (2)

The regular centralizer K_z of A constructed in the linked chart
has determinant1, eigenratio U on the ordered A-eigenvalues
(w,w^(-1)), and gives the rotated map

    (a,b) -> (K_z a K_z^(-1),K_z b K_z^(-1)).           (3)

Put P=aK_z a^(-1)K_z^(-1)=b^(-1)K_z bK_z^(-1).
Then Tr P=-L-L^(-1). With Delta=(1+YL)(1+Y/L),

    J=(I-YP)/sqrt(Delta), C=(YI-P)/sqrt(Delta), JC=-P.   (4)

The branch of sqrt is its regular complete branch. The ACTUAL
unrotated ports are incoming (K_z bK_z^(-1),b^(-1)) and outgoing
(K_z a^(-1)K_z^(-1),a). Formula(4) gives exactly the threaded
negative half-twist group relations. On the P-eigenflag with
eigenvalue lambda=-L^(-1), C has the source-prescribed positive
auxiliary meridian eigenvalue M=H^(-1/2). This is the local literal
port/flag theorem, not a trace-only assertion.

## 2. The bare crossing in THIS bent frame

It is essential not to apply the ordinary downward positive-Hurwitz
rule to the bent (a,b) coordinates without transporting the ports.
The FULL physical turn identity is mathscrR(R^(-1))=R, including
kappa and every Casimir normal, by
[the exact four-port turn calculation](actual_pair_casimir_commutant_and_rotated_trace.md#3-literal-turn-rotation-agrees-with-the-charge-block-formula).

Here is its group-side port calculation. For a general turned box
with input(a,b), output(a',b'), unrotation gives incoming
(b',b^(-1)) and outgoing((a')^(-1),a). The unrotated bare R^(-1)
uses the negative Hurwitz rule (u,v)->(v,vuv^(-1)). It follows
immediately that

    a'=b, b'=bab^(-1).                                  (5)

Thus the actual source R in the bent frame is negative Hurwitz.
No branch is selected by an eigenphase comparison. Define

    J_R=[A-(c-1)I]/sqrt(2-c), K_R=J_R^(-1).             (6)

Direct multiplication gives det J_R=1,
J_R b=a J_R and J_R^2=-A^(-1). Consequently (5) is simultaneous
conjugation by K_R. Its eigenratio on the ordered A-eigenvalues
is -w; that of R^(-1) is -w^(-1). Both matrices are regular at
c=-2. This agrees with the source's actual nodal Gaussian,
but the group rule was proved FIRST from the literal turn.

## 3. The sharp box has its own actual positive-half meridian

Write f^#(eta,chi)=conjugate(f(conjugate(eta),conjugate(chi)))
for holomorphic Schwarz reflection. The source action of the
literal sharp box obeys G_+=-G_-^#. Since the color logarithm
z=Log H=2i chi has z^#=-z, while eta^#=eta, the chain rule gives

    partial_eta G_+=-(partial_eta G_-)^#,
    partial_z G_+=(partial_z G_-)^#.

The effective stationary variables are therefore

    U_+=1/U_-^#, Y_+=1/Y_-^#, L_+=L_-^#,
    K_+=(K_z^#)^(-1).                                  (7)

The reciprocal of Y is essential: its stationary index is the
Schwarz-reflected u, and Y=exp(2iu). At completeness both effective
Y values are i. Merely conjugating K or declaring a different
peripheral color would give the wrong source action.

Form P_+=aK_+a^(-1)K_+^(-1), Delta_+ and
J_+=(I-Y_+P_+)/sqrt(Delta_+) exactly as above. Trace invariance
under K inversion, together with the old trace relation, gives
Tr P_+=-L_+-L_+^(-1). For the literal POSITIVE unrotated half twist
the actual meridian is

    C_+=J_+^(-1).                                       (8)

Indeed J_+ a_orig=a J_+ gives C_+^(-1)a_orig C_+=a,
which is the second output of the positive-Hurwitz threaded box;
the common product relation gives its first output. This checks
the full port equations, not only their traces.

On the P_+-eigenflag lambda_+=-L_+^(-1),

    eigen(C_+)^2=(1+Y_+L_+)/(1+Y_+/L_+)=H^(-1).        (9)

To verify the last equality, Schwarz-reflect(2):
(1+Y_-^#L_+)/(1+Y_-^#/L_+)=L_+^2 H, then substitute
Y_+=1/Y_-^#. Its regular square-root branch is precisely
H^(-1/2). Thus the sharp box retains the SAME physical meridian
color and has preferred lambda_+=-L_+^(-1), with all original
ordinary-pivot spin signs. At completeness C_+ is J^(-1), while
C_- is C; they are not assumed to be plain conjugate matrices.

## 4. Composition of every signed source piece

The original stack pieces have full sources f_-=Rz and
f_+=z^sharp R^(-1). Their literal mirror/reversed identification
was proved in the stack cut certificate. The port maps above give
simultaneous conjugation by

    K_(piece,-)=K_R K_z,
    K_(piece,+)=K_(box,+) K_R^(-1),                    (10)

where K_(box,+) is the sharp BOX centralizer K_+ in(7).
All matrices are specified functions of the SAME A, so they
commute as actual centralizers; no arbitrary strand gauge is
inserted between pieces. Their source-selected gains are

    gain(f_-)=(-w)U_-, gain(f_+)=U_+(-w)^(-1).

After p plus,q minus pieces and an actual outer R^a, put
n=p+q,m=q-p+a. The complete port map is conjugation by

    K_tot=K_R^m product_(plus)K_+ product_(minus)K_z,
    gain(K_tot)=(-w)^m product_i U_i.                   (11)

These are full regular matrix identities through w=-1. To see
their noncentral complete limit, let N_0=A+I, N_0^2=0. The actual
selected local values are K_z=K_+=I-iN_0/2, K_R=I-N_0/2. Hence

    K_tot=I-(m+in)N_0/2.                               (12)

In particular this complete outer meridian candidate never
collapses to I when n>0. The matrix data retain the local regular
octahedron flags, not only a cusp Hessian.

## 5. The literal outer-cut dictionary, with all coupons transported

The actual outer dictionary is

    (a,b)=(beta_phys^(-1),alpha_phys^(-1)),
    C_0=K_tot, preferred P_0=beta_phys alpha_phys=A^(-1). (13)

Here is its source/collar check. Keep the unrestricted ORIGINAL
marked closure, pivot and single1/N on their original side. The
physical cup and ordinary cap matrices are

    p_(a,b)=N x^(-b) delta_(a+b,d),
    ell_(a,b)=x^a/N delta_(a+b,d).

Their literal snakes satisfy

    sum_b p_(a,b)ell_(b,c)=delta_(a,c),
    sum_b ell_(a,b)p_(b,c)=delta_(a,c).                 (13a)

The one nonzero term has matching complement indices and all N/x
factors cancel EXACTLY. Insert TWO noncrossing nested head snakes
in the thin main-wire collar between the stack and outer loop;
their arcs are disjoint from the auxiliary cut and closing pivot.
For W=V tensor V the contravariant dual is ordered
(second*,first*): the nested evaluation pairs first with fourth
and second with third. Each actual cup takes its meridian path
to the inverse. The explicit table on the outer side is therefore

    standard main port1 alpha_phys <-> bent port2 b^(-1),
    standard main port2 beta_phys  <-> bent port1 a^(-1),
    auxiliary C_0 and its original closing pivot stay UNCHANGED.

Every mixed crossing incident to these ports is transported through
the SAME snakes by ORIGINAL Hopf duality. A dual matrix port is
partially transposed and conjugated by p and ell: its coupon is
NOT held fixed while its indices are renamed. Equivalently
(S tensor id)(R_universal)=R_universal^(-1) and
(id tensor S^(-1))(R_universal)=R_universal^(-1) move that
strand through its evaluation. This includes the full
q^(H tensor H/2), with S(H)=-H, and both finite nilpotent factors.
Their literal endpoint zeros give no cyclic wrap term. The ordinary
auxiliary object is not dualized or cut again. This is an all-port
identity for an arbitrary exterior; the original co-source remains
outside the move.

For clarity, let U be the FULL unflipped universal-R matrix between
the complete physical head and any ordinary color j. If the N-head
is FIRST, the actual left/right bend identities are

    U=(p^T tensor I)(U^(-1))^(t_1)(ell^T tensor I),
    U^(-1)=(p tensor I)U^(t_1)(ell tensor I).

If it is SECOND they are

    U=(I tensor p)(U^(-1))^(t_2)(I tensor ell),
    U^(-1)=(I tensor p^T)U^(t_2)(I tensor ell^T).

The superscript t_i means the partial transpose on that physical
head. Both original half-Cartan factors and finite nilpotent factors
are in U. The indicated transpose of p is fixed by which actual
side of the cup is bent; exchanging p with p^T arbitrarily is
false. These identities transport both crossing signs in either
tensor position. They are not a same-coupon index permutation.

For an explicit tensor-index version, let P_ord denote reversal
of ABSTRACT dual tensor ordering, not a physical braid. Then

    J_W=(p tensor p)P_ord, E_W=P_ord(ell tensor ell),
    J_W E_W=E_W J_W=I_(V tensor V).                    (13b)

Indeed its full index sum is
sum_(s,t)p_(a,t)p_(b,s)ell_(t,c)ell_(s,d)=delta_(a,c)delta_(b,d).
No R, curl or framing shear implements P_ord. Transporting the
coupons through these literal nested adapters is precisely the
bent port convention used in sections1--3, including(5).

The consequence is elementary and exact: conjugating the standard
[2,1,1,2] loop map by this dictionary gives main map Ad(C_0^(-1))
and closing relation [C_0,A]=1. Its preferred disk word is A^(-1),
with no additional C_0 power: substitute
A_orig=b^(-1), B_orig=a^(-1) in the original disk word B_orig A_orig.
Main inversion/reversal commutes with common conjugation, so the
same Ad(C_0^(-1)) is obtained when returning to (a,b). No argument
from equality of L_j polynomials is used to choose this orientation.

Outer closure gives Ad(C_0^(-1)K_tot)(a,b)=(a,b). Since a,b
remain irreducible, their common centralizer is scalar in SL and
trivial in PSL. Hence C_0=K_tot in PSL, with its SL sign fixed by
the trace+2 complete branch. Reversing BOTH peripheral generators
and swapping their common eigenflag is a harmless alternative with
the same positive (M,lambda) data; inverting only one is not.

## 6. Actual global peripheral and source differential

Let z_i=Log H_i,
eta=Log(-w), and let G_i be the source-normalized typed local
actions. The actual outer Fourier phase has

    G_total(eta,z)=sum_i G_i(eta,z_i)+m eta^2/2+z_0 eta
                                      +known real constants. (14)

The real constants retain the kappa/source-spin line and do not
change the marked volume. Its eta stationarity is

    gain(K_tot)=exp(-z_0)=H_0^(-1).

By(13), C_0=K_tot has the positive M_0=H_0^(-1/2) flag on
the A-eigenvalue w branch; preferred P_0=A^(-1) has eigenvalue
w^(-1)=-exp(-eta). Therefore ALL actual cusp coordinates satisfy

    u_i=-z_i/2, lambda_i=-exp(-partial_(z_i)G),
    v_i=pi i-partial_(z_i)G,
    d[G-pi i sum_i z_i]=2 sum_i v_i du_i.               (15)

For inner cusps this was proved locally above; for the outer cusp
it uses the actual preferred word in(13). Hence the source action
has the marked boundary differential, including the spin term.
Its complete imaginary anchor is2n v8. The next section verifies
the complete actual geometric anchor needed to calibrate its
absolute regulator.

As a consistency check, (12),(13) give the actual outer cusp ratio
2i/[n-im] and the two inner ratios sigma+i. These are TWICE the
analytic curvature parameter phi''/(2pi i) when x=h/N; the
geometric logs are u=-pi i x and v=-phi_x. The factor is fixed
by(15), not by relabeling a source Hessian as a cusp modulus.

## 7. The full complete geometric anchor and every surviving main cusp

The [regular cut-piece certificate](actual_belt_stack_regular_parabolic_port_chart.md#6-every-complete-white-and-inner-shaded-face-map)
verifies EVERY white and both inner shaded face maps, not just six
vertex flags. In its bounded frame the vertices are
(0,infinity,1,-1,-i,i). Exact white reflection products give
a,b,a',b',A, and the actual two J a',b'J^(-1) shaded maps send
ALL three vertices of each original inner face correctly. They
are therefore the complete face isometries of the actual cut
two-octahedron quotient. The opposite half uses the same unmarked
cut geometry with its actual meridian J^(-1), not a silent circle
framing change.

The [literal stack collar certificate](actual_balanced_octahedral_belt_stack_volume.md#3a-any-fixed-integer-outer-crossing-power)
glues those pieces with their actual signs and the actual outer
R^a. Section2 has calibrated that crossing in precisely the same
transported bent frame. The local main-port matrices thus agree
across every seam with the regular-cell developing holonomy. At
the final outer loop, the original relation in section5 uniquely
forces its meridian to be K_tot in PSL for BOTH the source lift
and geometric developing map. Its trace+2 branch fixes the SL
choice. Thus this last generator is matched too, not merely its
trace or cusp derivative. The independent oriented pants-path
calculation in the local note section7 gives(A^(-1))ba=I and
checks the preferred outer boundary orientation directly.

The ENTIRE complete representation is consequently the positively
oriented geometric holonomy of the ACTUAL stack exterior, of volume
2n v8. This holds for every fixed sign word and integer a. The
possible simultaneous reversal of a peripheral pair changes neither
the primitive slope nor its selected eigenvalues. All generator
matrices and selected flags vary continuously in bounded charts
for the small complex source colors. The apparent w=-1 diagonal-
frame singularity is absent in the regular matrices(1)--(4).

Every surviving MAIN component has a noncentral parabolic meridian,
being a conjugate of a or b. A peripheral longitude commuting with
that meridian has squared multiplier1, so its small geometric
similarity log is ZERO near the complete point. Hence BOTH logs
at every UNFILLED main cusp stay zero. This includes odd a, where
the two main components merge. No additional main cusp Hessian or
independently imposed main longitude is needed for completion or
for the regulator boundary term.

## 8. Absolute regulator and every independently long integral filling

After eliminating eta by its actual source stationarity, write
G_(z_i)=ell_i for ALL n+1 auxiliary cusps, including ell_0=eta.
The marked norm from(15) is

    D_src=Im G-sum_i Re z_i Im ell_i.                    (16)

Indeed retain Gbar=G-pi i sum_i z_i BEFORE forming the boundary
norm: D_src=Im Gbar-2 sum_i Re u_i Im v_i. The central terms
cancel only in this paired expression. They are not discarded
from the action or physical ordinary-circle character.

For the actual developed fundamental chain of this SAME marked
exterior, the Bloch boundary is delta beta=-2 sum_i M_i wedge
lambda_i. Its Bloch--Wigner differential is therefore

    dD(beta)=2 sum_i[Re v_i dIm u_i-Re u_i dIm v_i]
            =dD_src.

The main cusp terms vanish by section7. Both functions have the
same absolute complete anchor2n v8, so they agree on this connected
source germ. This is the established
[marked fundamental-chain comparison](actual_pretzel_marked_regulator_and_filling_action.md#3-the-geometric-regulator-has-the-same-derivative-and-absolute-anchor)
applied to the explicit global lift. Neither a cusp-Hessian match
nor an unproved equality of dilogarithm lists replaces it.

The [actual outer squared-kernel theorem](actual_outer_color_squared_kernel.md)
and the inner packet/gap theorem supply the WHOLE original
mixed-color packet and its ENTIRE complementary physical-color
cube estimate for these stacks. The
[general original-source filling transfer](general_original_source_long_filling_transfer.md)
then gives a NONZERO full asymptotic for independently sufficiently
long FIXED signed integral fillings at ANY chosen subset I of the
n+1 auxiliary circles. Keep every other auxiliary color literally
h_j=0, hence its original L_N component; do NOT set p_j=0, which
would meridionally fill and remove that circle. The exact packet,
nonzero amplitude, negative real Hessian and entire physical-color
complement gap restrict to the I coordinates. Apply only the
original color-filling functionals indexed by I. The equations are

    z_i+2p_i ell_i=2pi i m_i, m_i=+1 or -1, i in I,
    z_j=0, j not in I.                                 (17)

Separate exact source evenness gives ell_j=0 at every unfilled
auxiliary coordinate, even while filled coordinates vary. Its
peripheral group remains noncentral parabolic near the complete
point, with BOTH small logs zero. These unfilled auxiliary cusps
join the main cusps in section7. No new estimate or geometric
existence premise is required.

The ACTUAL small geometric similarity logs are
U_i=-z_i,V_i=-2ell_i. Thus (17) is precisely
U_i+p_i V_i=-2pi i m_i. It is the primitive2pi branch, not merely
an exponentiated PSL relation. The preferred SL longitude minus
sign has already been retained in(15)--(16).

These equations kill the literal disk slopes mu_i+p_i lambda_i.
The original complete-color twist expansion inserts R^(-2p_i),
including every confluent normal and dimension endpoint; hence
the slope sign is the original disk sign. At the OUTER circle it
can also be checked directly: K_R^2=-A, so R^(-2p) gives
Ad(A^(-p)), exactly the loop action Ad(C_0^(-1)) when
C_0 P_0^p=1 and P_0=A^(-1). For each inner circle the same sign
was proved in the literal mixed-circle longitude certificate,
and the actual quarter-turn transports its disk with the tangle.

Every selected filled coordinate is nonzero. Separate source
evenness makes ell_i divisible by z_i, even when all other colors
vary, so z_i=0 would contradict(17). The small logs exclude an
extra period. The matrices share their selected flags; their
filling products are scalar in SL and identity in PSL. The
[general marked completion theorem](general_source_regulator_hyperbolic_equality.md)
therefore extends this nearby ACTUAL representation to a positive
smooth complete hyperbolic metric on the indicated filled topology.
It is the filled geometric holonomy. The two directions of the
fundamental-class/Gromov-volume comparison identify the regulator
with the actual filled hyperbolic volume, rather than only bounding
it above.

The source filling phase keeps the literal quadratic chirps on I. In
the present eigenlog variables it is, up to the recorded real
constants,

    G_fill=G+sum_(i in I) (z_i-2pi i m_i)^2/(4p_i).

On(17) its added imaginary part is
sum_i 2p_i Re ell_i Im ell_i=-sum_i Re z_i Im ell_i.
Hence Im G_fill=D_src EXACTLY. This verifies the source-to-volume
comparison after filling while retaining all spin and charge data.

We obtain: for every fixed n>=1, every sign word of length n,
every fixed integer outer crossing power a, and ANY subset I of
its n+1 auxiliary circles, independently sufficiently long fixed
signed integral fillings on I obey

    lim_N (2pi/N)log|K_N(filled stack)|
                     =Vol(S^3 minus filled main link). (18)

The empty subset is the already proved COMPLETE stack theorem,
with no slope threshold or filling functional. For a nonempty
subset its threshold may depend on I; for a fixed stack take
the maximum over its finitely many subsets if desired. All N
parities and composite levels are included. The original
single-cut normalization is retained, with no separately modified
dimension at every component. Full twists preserve the main
permutation: when ALL auxiliary circles are filled, the result
is a KNOT for odd a and has TWO components for even a. For a
proper subset the unfilled auxiliary circles remain components:
the total is n+2-|I| for odd a and n+3-|I| for even a.
The threshold depends on this fixed
marked source and its fixed analytic neighborhoods; no numerical
threshold or slope comparability condition is asserted. This is
a cyclic-belt family, not an arbitrary branched-source or arbitrary
fixed-bridge volume theorem.

Audit: [exact signed local matrices, literal nested source snakes and outer word algebra](../experiments/audit_actual_belt_stack_typed_character_composition.py).
The local algebra, nested-duality dictionary and complete matrix
limits have been independently re-derived. The quantum packet,
full-color gaps, exact face/collar topology, primitive completion
and marked regulator invoked above retain their separate proofs
and full-source audits.
