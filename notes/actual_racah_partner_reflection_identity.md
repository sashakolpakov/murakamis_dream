# Exact partner reflection of the normalized Racah root value

29 October 2026. For every supported folded sextuple, the normalized
squared Racah VALUE is unchanged under ANY of the sixty-four independent
reflections j -> N-1-j. The proof uses the actual generic source
normalization, a genuine cyclic turn, a uniform factorial certificate,
and residues of channel projectors on a saturated analytic invariant
lattice. It does not assume a semisimple root quotient or a named 6j
symmetry. All higher normal currents remain present; they are NOT
invariant, as an exact first-normal counterexample below shows.

## 1. Statement and the precise metric convention

Fix N>=2, D=N-1, q=exp(pi i/N). Start with six folded spins
a,b,c,d,e,f in [0,D/2], with all four admissible face sums

    F=(a+b+e,c+d+e,a+d+f,b+c+f) >= D.             (1)

Admissible means the ordinary triangle conditions and integer face
sums. The original graph channels are INTEGER spins; the same proof
allows admissible half-integral spins with the phase stated below.
Let Q=(a+b+c+d,a+c+e+f,b+d+e+f). At generic zeta define

    S=sum_(z=max F)^(min Q) (-1)^z[z+1]!
                          /(product_i[z-F_i]! product_k[Q_k-z]!),
    Delta_F^2=[F-2x]![F-2y]![F-2z]!/[F+1]!,
    mathcal W(zeta)^2=[N]^2 S^2 product_faces Delta_F^2. (2)

The factorials are symmetric quantum factorials, retained GENERICALLY.
For a partner branch replace any subset of the six spins by D-j
in these SAME formulas.

Every branch of (2) has a finite root limit. For INTEGER spins it
is the positive quantity

    W_N^2=R_N^2 product_faces d_F,
    R_N=N sum_(max F<=z<=min(Q,2D))
          s_(z-D)/(product_i s_(z-F_i) product_k s_(Q_k-z)),
    d_F=product_(j in face)s_(F-2j)/(N s_(F-D)),
    s_r=product_(u=1)^r 2sin(pi u/N).             (3)

Then EXACTLY

    W_N^2(j_1,...,j_6)
       =W_N^2(D-j_1,j_2,...,j_6)=...              (4)

under all sixty-four independent partner choices, at both parities
and every composite level. No asymptotic assertion is used.

For admissible half-integral spins the generic squared expression has

    mathcal W(q)^2=(-1)^[2sum_six j] W_N^2.

That sign is unchanged by every partner reflection, since its exponent
changes by 2D-4j, an even integer. Thus both the signed generic metric
value and the positive sine-factorial convention satisfy (4).
No positive-square convention is silently extended to half spins.

## 2. The full actual source fixes a reciprocal trace normalization

Let A=2a,B=2b,C=2c,D0=2d,E=2e,G=2f be INTEGER highest weights.
Use the ACTUAL invariant columns S_E,T_G and inverse source matrix
L_(G,E) from
[the generic all-port source theorem](actual_general_four_port_single_racah_kernel.md).
Write its explicitly proved seven-factorial prefactor as p:

    L_(G,E)^ABCD=p_abcd(e,f) S.

This p includes every actual cup, cyclic sign, monomial and factorial.
The reciprocal coefficient is not obtained by squaring p and guessing
an ordered norm ratio.

Indeed let C_A move the last V_A to the front by its actual snakes,
so it multiplies by (-1)^A K_A. It gives

    C_A S_G^BCDA=T_G^ABCD,
    C_A T_E^BCDA=S_E^ABCD.                       (5)

For the second equality, the two cyclic moves interchange the two
coupled pairs in S_E. Their clock is K_A K_B=K_E, while the internal
cup reversal has ratio

    P_E(E-r)/P_E(r)=(-1)^E zeta^(-E+2r).

The monomial cancels K_E, and the total sign is
(-1)^(A+B+E)=1 by channel parity. This proves (5) on ALL external
colors, not just on a highest corner. It follows that the actual
reciprocal matrix is

    R_(E,G)^ABCD=L_(E,G)^BCDA.                   (6)

The exact source prefactors consequently satisfy

    p_abcd(e,f) p_bcda(f,e)
       =[2e+1][2f+1] product_faces Delta_F^2.     (7)

Here is a uniform own algebraic certificate for (7). In the all-port
theorem, put s=(A+B+C+D0)/2, Gmax=min(A+D0,B+C),
n=(Gmax-G)/2, t0=s-Gmax and M=(Gmax+G)/2+1.
Its finite product V_n can be written

    V_n=zeta^[n+2n(t0+n)]
       F_M F_(s+1-n)F_t0 /
           [F_(G+1)F_(s+1)F_n F_(t0+n)].         (8)

Replace every symmetric factorial by
zeta^[-r(r-1)/2]F_r/(1-Q)^r in the explicit source prefactor
p=chi_E X_E/(b_G J_n S0 V_n). There are FOUR algebraic cases:
the two choices of Gmax and the two choices of the cyclic Emax.
For all four, literal cancellation gives the following ratio to
the right side of (7):

    nonzero F_r exponents: none,
    residual zeta exponent:0,
    residual (1-Q) exponent:0,
    residual sign exponent:
          E+G-3A-2B-C-2D0.                       (9)

This last integer is even because E=A+B mod2 and G=B+C mod2.
The accompanying certificate represents each F_r by its INDEPENDENT
symbolic linear argument in A,B,C,D0,E,G and verifies all four
factor-exponent dictionaries identically. Quadratic zeta exponents
are expanded as polynomial identities. Thus (9) is a finite uniform
factorial proof, not a numerical fit or an assumed orthogonality norm.

Let M_abcd=Inv_K(V_A tensor V_B tensor V_C tensor V_D0), over generic
meromorphic germs K. On this ACTUAL space let Pi_e^S and Pi_f^T be
the generic rank-one channel projectors for the two pairings.
By ordinary matrix trace in the source basis, (6),(7) give

    tr(Pi_e^S Pi_f^T)=R_(E,G)L_(G,E)
       =[2e+1][2f+1] product_faces Delta_F^2 S^2,
    mathcal W^2=[N]^2 tr(Pi_e^S Pi_f^T)/
                                        ([2e+1][2f+1]). (10)

This is the proper source-normalized, gauge-free trace identity.
It uses an ordinary trace on the multiplicity space, not an illicit
replacement of the original marked physical row by a quantum trace.
The all-port source identities already keep that row and any exterior
outside the local recoupling. No original framing or crossing scalar
has been canceled in (10).

There is a corresponding exact GENERIC diagonal bilinear transport,
which fixes the distinction from an incorrectly ordered Clebsch norm.
Write L_(G,E)=a_E b_G S with the actual separable source gauges in
the all-port theorem, and D_E=Delta_abe^2 Delta_cde^2,
D_G=Delta_bcf^2 Delta_daf^2. Equations (6),(7) give

    M_S(E)=a_E^2/([2e+1]D_E),
    M_T(G)=[2f+1]D_G/b_G^2,
    R=M_S^(-1) L^T M_T,
    L^T M_T L=M_S.                              (10a)

The transpose is bilinear, not a Hermitian adjoint. These generic
weights can have zeros, poles and phases at the root, so (10a)
does not supply a positive full confluent metric or a bound on its
source conditioning. It retains the actual source gauges rather
than replacing the reciprocal prefactor by its square.

## 3. Every partner has exactly the needed physical channel collision

For one folded face (x,y,z) with x,y,z<=D/2 and x+y+z>=D, any
subset of partner flips gives

    D<=x'+y'+z'<=2D,
    0<=y'+z'-x'<=D, and its two cyclic versions.  (11)

The minimum of the first expression is the folded sum and its
maximum is three D minus that sum. The minimum of the second over
flips is foldedSum-D, and its maximum is 2D-foldedSum. This proves
(11) before any root calculation, including boundary faces.

Fix ANY partner branch of all six labels. The ACTUAL generic left
channel range is

    I_S=[|a-b|,a+b] intersect [|c-d|,c+d], step1. (12)

Both e and e*=D-e lie in this range by (11). Applying its deficit
bound to BOTH values gives

    max I_S <= D+min(e,e*) < N+min(e,e*).          (13)

All indices in I_S are nonnegative. The root Casimir eigenvalues are

    lambda_j(q)=q^(2j+1)+q^(-2j-1).

Equality to lambda_e means j=e mod N or j=D-e mod N. Equation
(13) excludes EVERY upward alias e+N and e*+N, and there are no
downward aliases because 0<=e,e*<=D<N. Thus the complete collision
class in the FULL actual range (12) is EXACTLY {e,e*}.
The same proof applies to the right range and {f,f*}.

The argument retains all generic high channels in (12); it does not
truncate a channel range to its folded half. Other eigenvalue
clusters can collide too, but none collides with this selected one.

## 4. Saturation makes the residue comparison legitimate

Let O be the analytic-germ ring at zeta=q, K its fraction field,
and V_A(O),... the ordinary highest-weight modules with the original
balanced matrices. Those matrices are holomorphic even for high
partners: their entries contain no divided-factorial denominators.
The actual generic invariant lattice is

    Lambda=Inv_K(V_A(K) tensor V_B(K) tensor V_C(K) tensor V_D0(K))
                  intersect V_A(O) tensor V_B(O) tensor V_C(O)
                            tensor V_D0(O).       (14)

It is a finite free O module. Indeed it is a saturated submodule of
a finite free module over the one-dimensional local analytic DVR;
torsion-free finite modules there have an O basis. The generic rank
is the already proved channel dimension |I_S|=|I_T|.

Each interval Casimir preserves (14): it is an actual holomorphic
Hopf intertwiner and preserves generic invariants, so it preserves
their intersection with the ambient lattice. Consequently its
matrix on Lambda is holomorphic. This is the point that prevents
singular generic source frames from being mistaken for a regular
root basis.

If e!=e*, the eigenvalue gap is a SIMPLE zero:

    D_logzeta(lambda_e-lambda_e*)|q
                     =2N(q^(2e+1)-q^(-2e-1))!=0. (15)

If this factor vanished the node would be -2 and e=e*=D/2.
The unique-collision statement of section3 shows that the pair's
minimal factor is coprime at q to the factors for all other channels.
Finite polynomial Bezout therefore constructs an analytic cluster
projector E_e onto the two selected generic eigenlines. Hence

    Pi_e=E_e (A-lambda_e* I)/(lambda_e-lambda_e*),
    Pi_e+Pi_e*=E_e,                              (16)

where A is the interval Casimir. Each projector has at most a simple
pole on the ACTUAL saturated lattice, and their residues are opposite.
No semisimplicity assumption at the root was used.

If e=e*=D/2, the same Bezout argument constructs its analytic
single-channel projector. The corresponding generic quantum dimension
is exactly [2e+1]=[N], which has one simple zero. For a paired e
the dimension is a root unit and

    [2e*+1]|q=-[2e+1]|q.                         (17)

Identical conclusions hold for f and the other interval Casimir.

## 5. Laurent orders prove the full sixty-four value identity

Let r be the number of PAIRED selected internal channels among e,f.
The preceding saturated-lattice construction gives

    tr(Pi_e Pi_f)=O(t^-r), t=log(zeta/q).

The scalar [N] has a simple zero, and each simple internal channel
contributes exactly one [N] to the denominator of (10). Therefore
the scalar prefactor in (10) has zero order r. The product has a
finite limit, without any deletion of a normal direction.

For a paired e, replace Pi_e by Pi_e*=E_e-Pi_e. The coefficient of
t^-r in the trace changes sign: E_e is analytic and its product with
Pi_f has pole order at most r-1. At the same time the nonzero leading
quantum-dimension factor [2e+1] changes sign by (17).
The signs cancel in (10). The simple case e=e* is tautological.
This proves one internal-edge partner reflection for ANY choice
of the other five partner values, including an odd simple f.
The f proof is identical.

Finally the face/opposite incidence in (2) is invariant under every
tetrahedral vertex relabeling, and this group acts transitively on
the six edges. Any chosen edge can thus be put in the internal e
position of (10). After any previous reflections, (11)--(17) still
hold. Iterating proves ALL sixty-four choices in (4), with no parity
or prime-level exception.

For clarity the root positivity and retained tail can also be read
directly from (2). All seven denominator factorial indices are in
[0,D] by (11) and the opposite-face difference identities. The root
value core z<=2D has common phase and is nonempty since max F<=2D.
The tail z>2D contains the additional factor [2N] and vanishes ONLY
at the value. Thus (3) has strictly positive terms. This is compatible
with, and does not replace, the source/projector proof of its symmetry.

## 6. The full generic normal is retained and is not symmetric

There is an EXACT generic relation in place of an incorrect jet
symmetry. For a paired e write d_j=[2j+1] and let E_e=Pi_e+Pi_e*
be its analytic cluster on the SAME actual source space. Equation
(10) gives, before specialization,

    d_e* mathcal W(e*,f)^2+d_e mathcal W(e,f)^2
                  =[N]^2/d_f tr(E_e Pi_f).       (17a)

The right side is O(t), with t=log(zeta/q), whether f is paired
or simple. If f is also paired, its complete double sum obeys

    sum_(i,j=0,1) d_(e_i)d_(f_j) mathcal W(e_i,f_j)^2
                   =[N]^2 tr(E_e E_f)=O(t^2).     (17b)

Here e_0=e,e_1=e*,f_0=f,f_1=f*. The four terms retain their full
generic gauges and normal currents. Analyticity of the clusters
proves the stated orders. In particular the weighted sum in (17b)
has zero first normal, although its individual summands need not.
These are source/projector conservation identities, not bounds on
the individual cluster trace or an instruction to dephase copies.

Set G(zeta)=(-1)^D S(zeta)/[N]. Termwise removal of the actual
zeros gives the exact local analytic decomposition

    G=C+[2N]T.                                  (18)

Here C contains z<=2D and T contains z>2D, with BOTH [N] and
[2N] removed in its numerator. All true denominator indices are
<N, and z+1<3N on these partner branches, so C,T are analytic.
For the latter bound, every folded opposite sum is >=D; replacing
its four labels gives at most 4D minus that sum, hence <=3D.
This accounts for every numerator zero and loses no tail.

For the logarithmic generic derivative,

    dot G(q)=dot C(q)+4N/(q-q^-1) T(q).           (19)

There are actual partner branches where this additional normal is
nonzero. At N=4, labels (2,2,2,2,2,1) give T(q)=-1 and the missing
current is exactly 8sqrt(2)i. It is not valid to differentiate the
positive value core alone.

Even the COMPLETE normalized squared metric in (2) is not generically
jet-symmetric. An exact cyclotomic certificate at N=4 maps
q->762 modulo the prime 1009 (q^4=-1), with all remaining denominators
units. In the coordinate t=log(zeta/q), the root values for

    folded (1,1,1,1,1,1) and single partner (2,1,1,1,1,1)

are both 2. Their first Taylor coefficients reduce respectively to
994 and 426, a difference 441!=0 modulo 1009. Thus the actual
algebraic first derivatives differ over C; the certificate is a
nonvanishing proof, not a numerical trend. The audit retains the
full C+[2N]T and every face-normalization jet in this comparison.

The theorem is therefore an EXACT ROOT VALUE symmetry, not a
generic-q symmetry or a bound on all partner normal jets. Controlling
those currents in a coherent metric remains a separate analytic
step. Raw source coefficients transform with their explicit source
prefactors; they are not declared invariant. Original exterior,
marking and crossing/peripheral factors remain where the actual
all-port theorem places them. This reflection of internal Casimir
branches is not an auxiliary-meridian deformation or a graph
identification.

Audit: [uniform generic source cancellation and exact partner checks](../experiments/audit_actual_racah_partner_reflection_identity.py).
The proof is the genuine cyclic source identity, four uniform
factorial certificates, full source-lattice collision argument and
Laurent-order comparison above. Exact finite checks supplement it;
they do not infer sixty-four symmetry from sampled knots.

The reflection tests do not establish equality of generic jets or a full-graph estimate.

No positive Hermitian transport or generic-jet invariance follows from the reflection identity.