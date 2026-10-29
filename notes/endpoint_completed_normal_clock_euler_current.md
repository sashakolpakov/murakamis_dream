# An endpoint-completed whole Jackson current from actual divided matrices

Research proof, 27 October 2026. The actual high-color divided
raising/lowering currents, with two literal anchored primitives,
recover the WHOLE Jackson differential on the physical unwrapped
clock. Its root value is the clock Euler derivative. The missing
bottom state is repaired explicitly, so the identity holds on
every state, not only in a bulk chart. A rational function and its
shift are retained before matrix evaluation.

This is an actual current/source map on the commutative physical
character subalgebra. The exact off-diagonal correction below shows
why it is not yet a map of all head Hopf currents or a full geometric
Gaussian/source comparison.

## 1. Whole actual matrices and regular anchored inverses

Use the original high integral color with r=N from
[the actual source theorem](high_integral_color_frobenius_wall_source.md).
In its fixed sign frame write w_(R,S), 0<=R<=N, 0<=S<N, and set

\[
 Z=Q^N,\quad\delta=1-Z,\quad J=NR+S,\quad C_Q=Q^J=Q^S Z^R.
\]

Keep the ORIGINAL generic integral divided matrices

\[
 e(q)=\tau E^{(N)}(q),\qquad f(q)=F^{(N)}(q),\quad
 \tau=(-1)^{N^2-1}.
\]

They preserve S and change R by -1 and +1. Their nonzero arrow
coefficients alpha_(R,S)(q), R>=1, and beta_(R,S)(q), R<N,
are regular units near the marked root: their root values are
N-R+1 and R+1. Define actual inverse arrows

\[
 e^\dagger w_{R,S}=\alpha_{R+1,S}^{-1}w_{R+1,S}\ (R<N),
 \quad e^\dagger w_{N,S}=0,
\]
\[
 f^\dagger w_{R,S}=\beta_{R-1,S}^{-1}w_{R-1,S}\ (R>0),
 \quad f^\dagger w_{0,S}=0.
\]

These are whole rational matrix germs of the actual divided
coefficients, not inverses of nilpotent matrices. With P_0,P_N
the two block endpoint projectors, they satisfy EXACTLY

\[
 e^\dagger e=I-P_0,\quad ee^\dagger=I-P_N,\qquad
 f^\dagger f=I-P_N,\quad ff^\dagger=I-P_0.             \tag{1}
\]

Their root operator norms are at most one in the fixed unit basis.
No uniform estimate on a growing q-neighborhood is assumed.
In the actual positive Fr metric ||v_R||^2=binom(N,R), the sharper
bound is ||e^dagger||=||f^dagger||=1/sqrt(N); the two endpoint
projectors still have norm one. This follows from the normalized
inverse arrow 1/sqrt((R+1)(N-R)).

## 2. The whole Jackson identity, with its shifted argument

Let g(Q,t) be a retained Laurent polynomial, or a rational function
whose denominators at BOTH C_Q and ZC_Q are invertible in the chosen
whole matrix chart. Q remains fixed when its t argument is shifted.
Define the actual current

\[
 \mathcal J_Z(g)=\frac{-e^\dagger[e,g(Q,ZC_Q)]
                         +P_0f^\dagger[f,g(Q,C_Q)]}{1-Z}.
                                                               \tag{2}
\]

Then, as an exact whole rational matrix identity,

\[
 \boxed{\ \mathcal J_Z(g)
       =\frac{g(Q,C_Q)-g(Q,ZC_Q)}{1-Z}.\ }            \tag{3}
\]

Proof. The actual block grading gives eC_Q=ZC_Qe and
fC_Q=Z^(-1)C_Qf. The inverse arrows have the opposite degrees.
Keeping operator order and the SHIFTED argument in (2) therefore gives

\[
 e^\dagger[e,g(ZC_Q)]
       =[g(ZC_Q)-g(C_Q)](I-P_0),
\]
\[
 f^\dagger[f,g(C_Q)]
       =[g(C_Q)-g(ZC_Q)](I-P_N).
\]

Since P_0P_N=0, their combination is the full difference, with
no missing endpoint. This proves (3). In particular replacing
g(ZC_Q) by g(C_Q) in the first commutator would give a different
operator and would not prove this identity.

The right side has a regular value at Z=1 whenever the stated
function chart is regular. For every integer k,

\[
 \mathcal J_Z(t^k)=\frac{1-Z^k}{1-Z}C_Q^k,
\]

and it obeys the exact twisted product rule

\[
 \mathcal J_Z(gh)=\mathcal J_Z(g)h(C_Q)
                         +g(ZC_Q)\mathcal J_Z(h).    \tag{4}
\]

Thus the construction is a whole function calculus before its
normal jets are taken. An explicit q-dependent coefficient is
carried unchanged in the difference; its separate q-derivative
is not silently included in a clock derivative.

At the root A=Q_N^S, (3) gives

\[
 \mathcal E(g):=[\mathcal J_Z(g)]_0
                  =A\partial_A g(Q_N,A)\,I_{\rm Fr}. \tag{5}
\]

The shifted argument in (2) has the same leading divided commutator
as its unshifted value, so equivalently
E(g)=[-e^dagger[e,g(C_Q)]/delta+P_0 f^dagger[f,g(C_Q)]/delta]_0.
For every remaining head matrix entry the output of (5) is the
literal multiplication by the indicated head character.

## 3. The normal jet and the literal finite cut

The derivative in (5) is not a derivation of the reduced finite
clock algebra k[A^+/-1]/(A^N-1): it sends A^N-1 to N.
The whole normal datum is essential. More precisely, for frozen
coefficients k containing Q_N, the actual map g(t)->g(C_Q) modulo
delta^2 has kernel

\[
                         (t^N-1)^2.                \tag{6}
\]

Indeed root vanishing implies g=(t^N-1)h. On w_(R,S),
C_Q^N-1=-J delta+O(delta^2). Vanishing at first normal order
then implies J h(Q_N^S)=0 for every R. For each S at least one
of J=NR+S is nonzero, so h vanishes at all N roots. This proves
(6), and the converse follows by squaring the simple normal zero.
Thus (5) is the actual clock conormal-jet derivative

\[
 k[t^{+/-1}]/(t^N-1)^2\longrightarrow
                  k[A^{+/-1}]/(A^N-1),\quad g\mapsto Ag'(A).
\]

It is a derivation relative to the root evaluation, not a discarded
normal direction on the fixed fiber. Write uniquely
g=g_0+(t^N-1)g_1 modulo its square, with both g_i of degree<N.
For the ORIGINAL averaged cut phi_N, the exact source row is

\[
                 \phi_N(\mathcal E(g))=N\phi_N(g_1). \tag{7}
\]

The canonical polynomial g_0 contributes no constant coefficient
after Ag_0'. The factor N in (7) is explicit. An unnormalized Fr
source line multiplies both sides by its retained pairing unit;
normalizing it does not change the head factor.

Apply this linear map coefficientwise to the sourced relative
interval complex R(E) of
[the literal framing transgression](relative_framing_source_transgression.md).
It commutes strictly with the interval differential, its two
endpoint rows and its polynomial contraction. Thus (2)--(7)
give an ACTUAL Fr-current realization of the clock-normal piece
of that relative cut map, with the original averaged co-source.
They do not assign an independent transfer coordinate to the cut.

In particular both geometric compensated fields obey
xi_i(A)=-2A(1-A). Hence the actual current
-2(1-A) E has precisely their common clock component on every
retained character g. The difference of the two geometric fields,
which moves the other framing coordinate, is not determined by
this common component.

## 4. The two primitives have a global P1 realization

On the actual Fr source identify v_j with binom(N,j) z^j in
H^0(P1,O(N)). Then e=partial_z, and the root inverse e^dagger
is exactly the anchored integral integral_0^z, with its degree-(N+1)
tail projected away. This gives (1) with the
constant and top coefficient projectors. The opposite f^dagger
is the corresponding south-chart primitive.

These operators also have explicit global differential lifts.
Writing D=z partial_z, take q_N(D) with
q_N(j)=1/[(j+1)(N-j)] for j<N and q_N(N)=0. Then
e^dagger=F q_N(D), f^dagger=E q_N(N-D) on H^0. Their differential
order generally grows with N; it is NOT the bounded PBW normal-depth
filtration of a crossing. Their identities on the full Cech
resolution hold up the explicit contraction homotopy constructed in
[the global source/co-source complex](global_frobenius_cech_source_and_endpoints.md).
The induced H^0 identities (1)--(3) are literal finite matrices.
Dual Serre residue carries the same endpoint projectors, rather
than deleting the two anchored boundary terms.

All q-dependent arrow inverses and source units in (2) are retained
coefficientwise in this lift. This does not make the chosen cut
pseudoinverses into Hopf intertwiners on arbitrary tensor products.
For example a trivial classical tensor summand is annihilated by
both e and f; no repair using their currents alone can produce the
identity on that summand. A whole-word map must transport the
actual cut projector and mixed coproduct, not blindly tensor (2).

## 5. Exact off-diagonal correction

Let H(q) be a retained head-matrix insertion, and keep its order
to the RIGHT of the clock function. The same current formula
with g(ZC_Q)H and g(C_Q)H has the exact result

\[
 \mathcal J_Z(gH)
 =\frac{g(C_Q)-g(ZC_Q)}{1-Z}\,H
 +\frac{-g(C_Q)e^\dagger[e,H]
                +g(ZC_Q)P_0f^\dagger[f,H]}{1-Z}.     \tag{8}
\]

This follows by the ordered product commutator, using
e^dagger g(ZC_Q)=g(C_Q)e^dagger and
f^dagger g(C_Q)=g(ZC_Q)f^dagger. If H is an actual head operator
whose root commutes with the Fr e,f, the remainder is regular,
but it generally does not vanish. If H contains noncommuting Fr
insertions, regularity itself requires its additional normal
source correction.

Thus (3) does not supply the TRUE head Hopf currents merely by
relabeling a scalar derivative. Their missing terms are the two
explicit inserted moments in (8). The old physical clock and
its whole Fourier-resolvent lift are those in
[the controlled current dictionary](controlled_fourier_current_and_conormal_dictionary.md),
not the distinct new position clock on the diagonal source.
Conjugating (2) and every inverse/projector by the whole source
gauge preserves the identity exactly, including that dictionary.

### The constant-head correction is an explicit inner connection

For a head matrix H kept CONSTANT in q and R, the root remainder
in (8) has a closed form. Define

\[
 \ell_0=0,\qquad
 \ell_S=-\frac12\sum_{k=1}^{S}
                  \frac{q_N^k+q_N^{-k}}{q_N^k-q_N^{-k}},\quad
 L_h=\operatorname{diag}(\ell_S),\quad\Sigma=2P_0-I.
\]

Then the actual divided-arrow matrices give

\[
                    \mathcal E(H)=[\Sigma\otimes L_h,H]. \tag{8a}
\]

To prove this, write alpha_(R,S)=a_R+delta a_(1,R,S)+... and
beta_(R,S)=b_R+delta b_(1,R,S)+..., with a_R=N-R+1,b_R=R+1.
Exact commutation of E^(N) with the ordinary E, and F^(N) with
ordinary F, along adjacent nonzero head arrows gives BOTH recurrences

\[
 \frac{a_{1,R,S}}{a_R}-\frac{a_{1,R,0}}{a_R}=\ell_S,
 \qquad
 \frac{b_{1,R,S}}{b_R}-\frac{b_{1,R,0}}{b_R}=\ell_S.  \tag{8b}
\]

For example the adjacent F ratio has normal increment
-1/2 (q^S+q^(-S))/(q^S-q^(-S)); differentiating the actual
q-integer gives it directly. The E ratio gives the same increment.
On R>=1, -e^dagger[e,H]/delta therefore gives -[L_h,H];
the literal R=0 repair contributes +[L_h,H]. All R-only constants
commute with H. This proves (8a), without setting any individual
arrow derivative to zero. Pairing k and N-k in the sum proves
ell_(N-1)=0. Its root size is O(N log N), and no head endpoint
coefficient has been inverted at a zero.

For the actual normalized paired Fr source, the selected coefficient
is c_N(m)=<Sigma>=2((1+m)/2)^N-1. Thus the original cut evaluates
this correction to c_N(m) Phi_h([L_h,H]). It is an EXPLICIT original
head Ward boundary. Let K=xA^(-1) and let B_cut be the actual
matrix of the Ward contraction, [K,B_cut]=e_h-I/N. Since [K,L_h]=0,

\[
 \Phi_h([L_h,H])=-\operatorname{Tr}([B_{\rm cut},L_h][K,H]). \tag{8c}
\]

This follows by applying the original cut homotopy and Jacobi; the
ordinary head trace of a commutator is zero. Hence this coefficient
part vanishes IDENTICALLY on the actual diagonal Green arrays and
on Ward-closed head partial traces. The endpoint-dependent polynomial
c_N(m), including its values -1 and +1 at m=-1,+1, remains in the
cochain homotopy. The unnormalized scale line multiplies this identity
by its retained pairing rather than being canceled by hand.

Actual q-dependent insertions have an additional specified lift term.
If H=H_0+delta H_1+... with H_0 a constant-head matrix, then

\[
 \mathcal E(H)=[\Sigma L_h,H_0]
       -e_0^\dagger[e_0,H_1]+P_0f_0^\dagger[f_0,H_1]. \tag{8d}
\]

This includes the true block-wrap and mixed Hopf-normal coefficients.
They cannot be removed using only (8c). If the fully closed actual
matrix and its first normal are scalar, every term in (8d) vanishes;
an unsummed current or a Fr-valued moment need not have that property.

## 6. A finite spectrum does not determine the whole Jackson current

Fix a head eigenvalue c=Q^S and write C_s=c Z^R on its N+1 block
states. Retain the actual polynomial FUNCTION

\[
 p_N(t)=\prod_{R=0}^{N}(t-cZ^R).
\]

Although p_N(C_s)=0 identically, its shifted value is

\[
 p_N(ZC_s)=c^{N+1}Z^{N(N+1)/2}
                   \prod_{k=1}^{N+1}(Z^k-1)\,P_N,   \tag{9}
\]

where P_N is the TOP STATE PROJECTOR, distinct from the polynomial
p_N. All lower shifted points remain in the finite spectrum, but
the top point cZ^(N+1) does not. Therefore

\[
 \mathcal J_Z(p_N)
 =-\frac{c^{N+1}Z^{N(N+1)/2}\prod_{k=1}^{N+1}(Z^k-1)}{1-Z}P_N
 =(-1)^N c^{N+1}(N+1)!\delta^N P_N+O(\delta^{N+1}). \tag{10}
\]

Consequently the WHOLE current depends on the retained function
and its shifted observable, not only on the single finite matrix
g(C_s). It is invisible through every normal order B<N in this
example. The degree of p_N is N+1 and grows with N, so this does
not contradict a bounded-presentation cyclotomic rigidity theorem.
It gives a concrete actual-source reason to retain functions
before their finite evaluations and jets.

## 7. The marked Green logarithm has a carry pole, not the regular Euler value

The character theorem must not silently replace the marked logarithmic
torsor. Put h=Log Q near h_N=2pi i/N and retain

\[
       \operatorname{Log}C_Q=hJ,\qquad
       \operatorname{Log}Z=Nh\quad\hbox{near }2\pi i.
\]

This is not the branch of Log Z near zero. A retained polynomial
moment P(J)=P(Log C_Q/Log Q) shifts to P(J+N). The SAME actual
whole current therefore gives the exact identity

\[
 \mathcal J_Z(P(J))=\frac{P(J)-P(J+N)}{\delta}.       \tag{11}
\]

For a coefficient function F, retain F(Q,ZC_Q,J+N) as well as
P(J+N). In particular a Cartan chirp q^(J^2) has root shift
factor (-1)^N; freezing that coefficient while shifting P would
change the actual carry. More generally let T carry every retained
coefficient and the marked index simultaneously. Then the pole
residue is exactly

\[
                  \operatorname{Res}_{\delta=0}\mathcal J_Z
                                    =(I-T_0).       \tag{12}
\]

On a coefficient fixed by this transport, T_0=e^(N partial_J),
and (T_0-I)^(h+1)=0 on moments of degree<=h. On the normalized
index J/N it is translation by one. With a nontrivial coefficient
transport the associated grade retains that transport minus I;
polynomial degree alone does not make it nilpotent.

Equation (11) is the actual divided-current realization of the
bounded Green carry in
[the whole carry source](green_moment_carry_filtration.md).
The pole is absent for the single-valued regular characters in
Section 2, and present for these marked moments. Subtracting it
without its relative endpoint/period class would remove the very
moment repair used in the full scalar certificate. No such
subtraction or global cancellation is inferred here.

[Exact actual-matrix and whole-function audit](../experiments/audit_endpoint_completed_normal_clock_euler.py).
The [results](../experiments/endpoint_completed_normal_clock_euler_results.json)
pass five actual generic-q families, seven actual root-normal
families, 1498 off-diagonal head matrix-unit connection identities,
40 actual marked-clock/carry matrix identities (including a Cartan
chirp), six whole finite-spectrum polynomial defects, and 42
symbolic bounded-moment carry checks. The
[independent whole-function audit](whole_clock_function_algebra_and_endpoint_extension.md)
also checks the endpoint product and distinguishes this retained
function algebra from a fixed finite matrix quotient.
The theorem supplies a clock/source-current component and the
correction (8); it does not prove full sourced geometric support
or a selected-volume limit.
