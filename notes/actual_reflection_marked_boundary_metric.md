# Reflection-compatible original cap metrics, and the remaining leg-order test

29 October 2026. The positive complete-circle form controls the ORIGINAL
ordinary and marked boundaries, but with DIFFERENT literal leg flips.
This gives an all-width positive boundary estimate with polynomial dual
cost. It does not yet identify an arbitrary untwisted fully augmented
planar diagram with a Hilbert norm square. A concrete single-leg bend
below shows why that last wiring check cannot be omitted.

## 1. Actual pair sources and the two positive forms

Put N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d. On two original
physical heads retain

\[
 p_{a,b}=Nx^{-b}\delta_{a+b,d},\quad
 \ell_{a,b}=x^{-a}Q^{-a}\delta_{a+b,d}/N,
 \quad m_{a,b}=x^b/N^2.
\]

Let P|a,b>=|b,a> be the literal tensor flip, NOT a crossing.
Write m_d=m times the INTEGER pair-degree-d projector. Since
x^2=Q^(-1), the exact row identities are

\[
 \ell=N^{-2}p^\dagger P,\qquad
 m_d=N^{-3}p^\dagger=N^{-1}\ell P.                         \tag{1}
\]

The original complete crossing circle satisfies the independently
proved [full physical positivity theorem](actual_complete_circle_reflection_positive.md):

\[
 C=PL_N\succeq0,\qquad H=L_NP=PCP\succeq0.
\]

The original Hermite source normal t has ell t=1, m_d t=0,
L_Nt=2Np. Consequently the already derived ordinary-cap identity is
C t=2N^3 ell^dagger and ell C^+ ell^dagger=1/(2N^3).

Conjugating by the TRUE flip P gives the new marked identity

\[
 H(Pt)=2Np,\qquad
 \boxed{\displaystyle
 m_d H^+m_d^\dagger=\frac1{2N^5},\qquad
 m_d^\dagger m_d\preceq\frac H{2N^5}.}                      \tag{2}
\]

Indeed H^+=PC^+P and m_d=ell P/N. Equivalently Pt/(2N^4)
is an explicit inverse solution for m_d^dagger, and its pairing
with m_d is 1/(2N^5). No inverse of L_N or deletion of its radical
is made. Ordinary ell uses C; marked m_d uses H.

Both distinctions matter. Since Cp=0 and m_d p=1, the marked row
is not bounded by C. The UNRESTRICTED m is not bounded by H either:
H|0,0>=0 while m|0,0>=1/N^2. It is the whole-source degree
argument below, not a local marked-row substitution, that permits (2).

## 2. All-width original marked boundary estimate

Consider the original k-cup plat source p^(tensor k) and a full
original signed word W preserving total INTEGER degree. Each cup
has degree d. After the k-1 ordinary output caps have fixed their
pair degrees d, the remaining marked pair is forced to degree d.
Therefore, on the ACTUAL incoming total degree kd,

\[
 (\ell^{\otimes(k-1)}\otimes m)W p^{\otimes k}
   =(\ell^{\otimes(k-1)}\otimes m_d)W p^{\otimes k}.          \tag{3}
\]

Put Lambda=ell^(tensor(k-1)) tensor m_d and

\[
 Q_{\rm top}=C^{\otimes(k-1)}\otimes H,\qquad
 c_k=2^{-k}N^{-(3k+2)}.
\]

Tensor the actual pair dual norms. This gives EXACTLY

\[
 \boxed{\displaystyle
 \Lambda Q_{\rm top}^+\Lambda^\dagger=c_k,\qquad
 \Lambda^\dagger\Lambda\preceq c_k Q_{\rm top}.}             \tag{4}
\]

For the original scalar, with its existing framing/peripheral line
chi_N unchanged, one consequently has

\[
 |K_N|^2\leq|\chi_N|^2c_k
  \langle Wp^{\otimes k},Q_{\rm top}Wp^{\otimes k}\rangle.    \tag{5}
\]

The estimate extends to arbitrary coefficient Hilbert spaces and
keeps every actual pivot already present in ell. It neither assumes
W is unitary nor pays a condition number for its unknown state.
It is a boundary Cauchy theorem, NOT yet a geometric bound for the
positive energy on the right.

On ordinary pairs the original signed same-pair twists are exact
C-isometries. On the marked H pair, their REFLECTED conjugates
P R^a P are H-isometries. Replacing one by the other without the
literal leg interface would not be a source identity.

## 3. Reflection of original crossings and a genuine bend caveat

The full original equal-color balanced crossing is complex symmetric.
In its strict coefficient, reversing input(a,b) and output(b+k,a-k)
leaves the full factorial ratio, x power, and Q exponent unchanged.
The independently checked actual inverse is Rminus=P conjugate(R)P.
Thus

\[
 P R_{\rm minus}P=R^\dagger.                              \tag{6}
\]

This is the correct reflected-adjoint statement; P remains a leg
exchange, not a physical extra braid. Similarly, a reflected ordinary
cap is p^dagger P/N^2, whereas the legitimately restricted marked
one is p^dagger/N^3. These are different boundary orientations.

There is a local obstruction to treating PSD as invariant under
ARBITRARY planar bending. Regard the actual cup as the matrix N U:

\[
 U_{a,b}=x^{-b}\delta_{a+b,d},\qquad
 U^\dagger U=I,\qquad \ell_{a,b}=(U^{-1})_{a,b}/N.
\]

Using these very turns to dualize one physical leg of a four-port
form B gives

\[
 (\mathcal D_2B)_{ab;cd}
  =\sum_{u,v}U_{bu}B_{av;cu}(U^{-1})_{vd},\qquad
 \mathcal D_2B=(I\otimes U)B^{\mathsf T_2}(I\otimes U^{-1}). \tag{7}
\]

The factors N from cup and cap cancel. At N=2 the ACTUAL positive
H=L_2P has its sole nonzero block on |01>,|10> equal to

\[
 \begin{pmatrix}4&-4i\\4i&4\end{pmatrix}.
\]

Its one-leg transpose, and hence the actually turned form (7), has
eigenvalues 4,4,4,-4. Thus a single-leg source duality is NOT in
general a positive Hilbert congruence. A bare ordinary bubble gives
the related warning ell p=0, whereas replacing ell by p^dagger/N^2
would incorrectly give N.

This is a statement about a DIFFERENT bipartition of an already formed
four-port Gram tensor. It is NOT the genuine antiparallel crossing
circle, whose reflection must be transported together with its dual
object. The next section verifies the distinction explicitly.

## 4. Genuine dual objects introduce no local positivity failure

Use standard dual bases for V*. With the original antipode conventions,
the self-duality isometry from V* to V is

\[
 T=U^{\mathsf T},\qquad
 T S(h)^{\mathsf T}T^{-1}=h,
       \quad h\in\{H,K,\mathcal E,F\}.                    \tag{8}
\]

For example S(E)=-EK^(-1), S(F)=-KF. Checking the single nonzero
entry in each raising/lowering column proves (8), including the
endpoints; S(H)=-H and S(K)=K^(-1). The standard coevaluation becomes
the original p/N after I tensor T, and standard evaluation becomes
N ell after T^(-1) tensor I. Thus this is the actual duality, rather
than a guessed rotation of the positive form.

For any choices of the two object orientations, put
D=T^(epsilon) tensor T^(eta), epsilon,eta in {0,1}, and transport
BOTH the circle and its reflection:

\[
 L_{\epsilon\eta}=D L_ND^{-1},\qquad
 P_{\epsilon\eta}=D P D^{-1},\qquad
 L_{\epsilon\eta}P_{\epsilon\eta}=DHD^\dagger\succeq0. \tag{9}
\]

All D are unitary. In particular no negative eigenvalue in (7)
disproves the antiparallel instance of (9).

This transport can be chosen consistently along EVERY oriented
diagram wire: assign the appropriate object isometry to that wire,
and transform a coupon B by D_out B D_in^(-1). Each contracted
internal port cancels a D with its inverse. This elementary tensor
identity holds for arbitrary exteriors and all leg orderings. It
does not require an extra sign or an arbitrary new crossing.

If left and right self-duality conventions are instead identified,
their exact discrepancy is the ORIGINAL pivot. Namely, with
g_a=x^(-d)Q^(-a),

\[
 U^{-1}U^{\mathsf T}=g,\qquad
 U^{\mathsf T}U^{-1}=g^{-1},\qquad UgU^{-1}=g^{-1}.       \tag{10}
\]

These identities are direct antidiagonal multiplication. They show
which unitary clocks must remain when a turn changes sides. Their
existence permits a consistent genuine-dual description; it does
NOT license deleting a pivotal holonomy on a closed component.

The unresolved global check is therefore more specific than an
orientation-sign problem. One must exhibit the projection-plane
cut of the ACTUAL fully augmented tensor graph, with its remaining
wire contractions and original turns, as a common ket/bra pairing
of the transported positive forms (9), or another positive boundary
pairing of polynomial cost. A positive coupon on each face is not
itself that graph identity. The original ordinary bubble, for
example, is ell p=0, whereas replacing its pivotal contraction by
p^dagger p/N^2 would give N.

No proof that a correctly cut reduced fully augmented diagram must
use the bad bipartition (7) is asserted. Conversely no arbitrary
global norm-square theorem follows here merely from (9). Until the
complete wiring identity is proved, (5) and (9) are the supported
all-width source and oriented-local results; the global geometric
energy estimate remains open.

[Audit](../experiments/audit_actual_reflection_marked_boundary_metric.py)
checks eight exact original-module source levels, five tensor-source
widths, seven genuine-dual circle families, and the exact N=2
different-bipartition diagnostic. It also checks the literal full
crossings, all source inverse solutions, original degree restriction,
and both left/right pivotal discrepancies.
