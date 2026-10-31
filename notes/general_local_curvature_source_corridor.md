# A local curvature certificate for every signed color subset

30 October 2026. Independently reviewed and frozen. At any fixed bridge
width, a local algebraic test on one actual marked circle packing
supplies ALL the shared-radius certificates for a joint signed/unsigned
color corridor. If each varied port's nonzero curvatures differ by at
most a factor3/2, its gap exceeds1/16. The test has O(R) inequalities;
it does not require enumerating the reflected color subsets.

This is a sufficient condition on the original labeled right-angled
certificate. It is not asserted for arbitrary essential diagrams or
claimed to be realized at every bridge number. No far-color, quantum
normal or filled-knot conclusion follows.

## 1. The actual diagram and algebraic test

Fix a connected original flat plat with its labeled simplicial white
triangulation and original marked MAIN edge uv. Let E be any set of
varied crossing-circle ports, with arbitrary retained half twists.
All other ports stay complete with their actual signs. Use the actual
shared marked packing of the [complete-source theorem](general_signed_augmented_source_volume.md):
L_u=L_v=0, and every other curvature L_f is positive. F and G below
are the source-normalized triangle and crossing-magnitude potentials
in [the homogeneous theorem](actual_homogeneous_casimir_face_source.md),
section5.

Let g*=4Lambda(pi/4)/pi=v_oct/(2pi). At each varied original port e,
ignore only the actual marked zeros and require its NONZERO curvatures
x_e,b_e,c_e,y_e to lie in some interval[t_e,rho t_e], with rho<exp(g*).
The t_e may differ: these intervals only describe the SAME original
packing, not separately chosen local frames or radii.

## 2. Every local gap has an explicit lower bound

Then for every varied port

    g_e=F(x_e,b_e,y_e)+F(x_e,c_e,y_e)-G(b_e,x_e,y_e,c_e)
                                         >=g*−log rho>0.       (1)

Proof. The actual simplicial white dictionary makes x,b,c,y distinct.
At most the two marked faces are zero. They cannot be the two outers:
the outer edge xy is MATCHING, whereas the marked edge uv is MAIN.
Hence each of the two triangles has at least one nonzero vertex and
at least one has two. Scale the nonzero quartet by t_e; g is unchanged under this common scale. By monotonicity, bound each
F from below by its equal-nonzero-weight value and G from above by
its equal-nonzero-weight value plus log rho.

The only constants needed are

    F(1,0,0)=0,
    F(1,1,0)=g*,
    G(1,1,0,0)=0,
    G(1,1,1,1)=g*.

The first triangle is flat. The second has center angles
(pi/2,pi/2,0), so the proved source potential gives4Lambda(pi/4)/pi;
its permutations have the same value. With two nonzero equal weights,
the G entropy is identically zero by Lambda(pi-a)=-Lambda(a). With
four equal weights, strict concavity gives the uniform four-angle
maximum and the displayed value g*.

If the quartet has two nonzero faces, at least one triangle supplies
g* and the other supplies at least0, while its G value is0.
If it has three or four nonzero faces, BOTH triangles supply at least
g*, while G is at most g* by monotonicity. This proves(1), including
all actual paired zero patterns such as202/202. No presumed exclusion
of those pairs is used.

An entirely elementary fixed choice is rho=3/2. The Fourier series for
Lambda gives g*=2Catalan/pi. The alternating
series for Catalan gives Catalan>1−1/9=8/9. Also pi<22/7 follows
from the positive integral

    integral_0^1 x^4(1-x)^4/(1+x^2) dx=22/7-pi>0,

and log(3/2)<1/2 follows by integrating1/t<1 on(1,3/2).
Therefore

    g*−log(3/2)>56/99−1/2=13/198>1/16.                 (2)

Thus local contrast≤3/2 gives the same explicit margin1/16 at every
varied port, regardless of width or number of boxes. It is the finite
algebraic test 2L_f<=3L_g for each ordered pair of nonzero face
weights in that port, at most12 comparisons per port. No transcendental
capacity optimization or enumeration of reflected subsets is required.

## 3. One shared radius vector certifies every subset

For the all-subset certificate, choose eta=g*−log rho. At the original
marked packing C_empty=Phi_D. Replace both marked zero face weights by
one sufficiently small FIXED positive value, retaining every ordinary
weight. The source-normalized F,G are continuous on the actual nonzero
boundary quartets. No continuity of I is used: I=-infinity when
b=c=0, and I<=G is applied only after positive regularization. Since
D is fixed, choose the
regularization so that simultaneously

    C_empty−Phi_D<eta/4, and every g_e>eta/2.

For EVERY nonempty subset S of varied ports, with its retained signs,

    C_S<=C_empty−sum_(e in S)g_e
         <Phi_D+eta/4−|S|eta/2<=Phi_D−eta/4,           (3)

using I<=G for unsigned replacements. A single shared radius vector
therefore supplies all of the homogeneous theorem's certificates.
No subset enumeration or smoothing-connectivity assumption is needed.

At these fixed radii all operator constants C_b are finite. Choose a
single delta(D)>0 so their total small-color exponential-rate cost on h_e<=delta N is
less than eta/8, then shrink inside the established core neighborhood.
Precisely, [the homogeneous theorem](actual_homogeneous_casimir_face_source.md),
section6, now gives constants c,delta>0 such that the ORIGINAL mixed
source and its exact complete-image core satisfy

    A_N(N-h_E,N_else)/F_N^E(h)=1+O(exp(-cN))

uniformly for physical integers0<=h_e<=delta N, at both parities.
For h_N/N tending to a real chi in this cube, the
[actual geometric assembly](actual_complete_core_geometric_deformation.md),
section4, gives

    lim_(N->infinity) (2pi/N)log|A_N(N-h_(N,E),N_else)|=Vol(rho_chi).

The other external colors remain N with their original signs. The
right side is the volume of the actual nearby marked representation,
not an asserted complete metric on a filled knot. There is no far-color
or filled-knot conclusion.

The algebraic test concerns local ratios in the original common packing;
it does not impose a diagram-independent global curvature bound. Existence of this or a weaker shared-radius certificate for the
full intended class remains open. This corollary does not solve the
entropy redistribution problem when a mixed maximum has a middle
load greater than1/2.


## 4. Verification scope

The proof uses the existing exact homogeneous source and core theorems;
it introduces no new quantum approximation. [The focused check](../experiments/audit_general_local_curvature_source_corridor.py)
enumerates the ten possible zero-position patterns allowed by the
local distinct-face/marked-edge conditions, verifies the elementary
constant calculation, and bounds all corresponding equal-weight gaps
with outward-rounded Arb arithmetic and analytic Fourier tails. These
checks concern the local inequality; they do not construct a new
family of diagram realizations.


Root full analytical and audit-code review PASS: the actual marked-zero
dictionary, source-normalized equal-weight constants, elementary strict
margin and one shared all-subset regularization were checked.

Independent full analytical/code review and fresh256-bit Arb replay PASS:
all10 allowed zero-position patterns, two exact elementary constant
identities and1024-term outward-rounded Fourier bounds were reproduced.
A separate independent analytical read also passed. These reviews concern
the stated sufficient certificate and its proved corridor consequence;
they do not assert realizability at every width or a far-color/filling
theorem.
