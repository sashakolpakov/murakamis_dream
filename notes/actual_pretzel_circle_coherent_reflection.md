# Actual pretzel circle sewing: a coherent positive factorization and a half-twist test

29 October 2026. For the specified arbitrary-width pretzel port graph,
the complete circle has an exact source-preserving Kraus/Cauchy
factorization. The half twists remain diagonal unitary channel phases.
The original marked cap produces TWO explicit boundary states; local
positivity alone does not identify them. A level-three exact calculation
rules out a literal positive norm-square identity for the half-twisted
base, even after multiplying by any unit root framing phase. A separate
untwisted calculation shows that the two source states remain different
in the complete positive-circle quotient itself. This excludes their
automatic identification by a choice of positive factor or consistent
unitary duality gauges. It does not rule out another global reflection
pairing for the genuinely untwisted base or a sharp positive majorant.

## 1. Specified original port graph

Let s>=3 be odd, with boxes on adjacent head pairs
(1,2),(3,4),...,(2s-1,2s). The bottom matching and top matching are

    S={(1,2s),(2,3),(4,5),...,(2s-2,2s-1)}.

The outer top pair (1,2s) has the ORIGINAL marked row m; all other
top pairs have the original ordinary cap ell. Put d=N-1,
q=exp(pi i/N), Q=q^2, x=q^d, and retain the original common Cartan
kappa=q^(d^2/2). Use the original physical pair operators R and L=L_N.
Each box considered here is

\[
 B_i=R^{e_i}L,\qquad e_i\in\mathbb Z.                    \tag{1}
\]

The [literal all-width port/source calculation](actual_odd_pretzel_augmented_transfer_source.md)
fixes this graph and its signs. Its augmented odd-pretzel base has
e_i=-1. The genuinely untwisted circle graph has e_i=0. These are
different graphs; removing the half twists is not a scalar framing
operation.

Let p_S be the tensor product of the genuine cups
p_ab=Nx^(-b) delta_(a+b,d), placed on S in its displayed order.
Let P_o swap each ordinary-cap pair (2,3),(4,5),... and leave the
marked outer pair alone. Let P_b swap every box pair. Both are literal
permutations of tensor legs, not added physical crossings.

All boxes preserve total INTEGER physical degree. Thus the total
incoming degree sd and the ordinary caps force the final marked pair
to degree d. Only on this assembled source the top row is

\[
 \Lambda_S=N^{-(2s+1)}p_S^\dagger P_o.                  \tag{2}
\]

Indeed ell=p^dagger P/N^2 and m_d=p^dagger/N^3 on their
respective pairs. The unrestricted marked row has not been replaced
locally on an arbitrary exterior.

Consequently the full raw source scalar, before its existing external
framing/peripheral factor chi_N, is

\[
 Z_N=N^{-(2s+1)}p_S^\dagger P_o
            (B_1\otimes\cdots\otimes B_s)p_S.           \tag{3}
\]

This graph identity is the source input; no geometric triangulation or
hyperbolic volume formula is assumed.

## 2. Full physical coherent channel factorization

Use the canonical full physical positive resolution
[of the original complete circle](actual_complete_circle_reflection_positive.md).
For every physical degree T and admitted distinct Casimir node j, let
v_(T,j) have first component one, embedded in its actual degree block,
and let h_(T,j)>0 be its exact positive CD coefficient. Form a rectangular
matrix F with columns sqrt(h_(T,j)) v_(T,j). Then

\[
 FF^\dagger=H=LP,\qquad R F=F\,\operatorname{diag}
                  (\kappa\nu_j),\quad
 \nu_j=(-1)^j q^{j(j+1)}.                              \tag{4}
\]

Every high physical block is retained by the explicit low-block mirror;
both even paired nodes and the odd simple node are included. This is
not a value-only replacement of a root Jordan block. The original
circle has already selected its entire image, with its actual normal
source, before (4) is used.

Since |kappa nu_j|=1, define the diagonal unitary
U_i=diag((kappa nu_j)^(e_i)). Equations (1) and (4) prove the
ALL-INPUT factorization

\[
 \boxed{B_i=F U_i F^\dagger P.}                         \tag{5}
\]

This retains every half twist and its full Cartan phase. It does not
use the false assertion that the original R is an H-isometry; the
isometry on H would instead involve the correctly leg-exchanged R.

Put F_s=F^(tensor s), U=U_1 tensor...tensor U_s, and define the
two source packets

\[
 u=F_s^\dagger P_b p_S,\qquad v=F_s^\dagger P_o p_S.
\]

Inserting (5) in (3) gives the exact coherent formula and its positive
Cauchy estimate:

\[
 \boxed{Z_N=N^{-(2s+1)}v^\dagger Uu,\qquad
 |\chi_N Z_N|^2\leq |\chi_N|^2N^{-(4s+2)}
                         \|v\|^2\|u\|^2.}             \tag{6}
\]

The two energies are explicit positive original-source contractions:

\[
 \|u\|^2=p_S^\dagger C^{\otimes s}p_S,\qquad
 \|v\|^2=p_S^\dagger P_oH^{\otimes s}P_op_S.            \tag{7}
\]

All original integer labels, cap constraints and CD factors are kept
before these contractions. The local once-power angle coefficient is
the exact h_(T,j), not its independent maximum. Formula (6) works at
arbitrary s and for arbitrary signed e_i; neither packet is defined by
the unknown closed scalar.

For e_i=0, the middle U is the identity, but v and u are still different
specified source packets. A global reflection theorem must supply an
additional relation between them, or another controlled pairing. This
does not follow from FF^dagger>=0 or from a consistent dual-object basis
change. In particular (6) is a structural positive comparison, not a
sharp geometric energy estimate.

For clarity, the equivalent literal transfer entries retain the phases
as follows. If h is the conserved input-left minus output-left charge,
I_h=[max(0,h),min(d,d+h)], T=d+a-a', then

\[
 M_i^h[a,a']=x^{-2a+h}
   \sum_{j\ {\rm admitted\ at}\ T}
       h_{T,j}(\kappa\nu_j)^{e_i}
       v_{T,j}(a-h)\overline{v_{T,j}(d-a')}.             \tag{8}
\]

The total physical degree T varies with the two open transfer indices.
It cannot be replaced by a common fixed degree before contraction.

## 3. Exact half-twisted source certificate at N=3

Take N=3, s=3 and every e_i=-1. Build the literal original factorial
R, the actual coproduct Casimir Omega, and L=Omega^2-I. The complete
source contraction (3), or equivalently the already specified transfer
trace, gives exactly

\[
 \boxed{Z_3=-189+81i\sqrt3=27(-7+3i\sqrt3).}             \tag{9}
\]

This calculation includes kappa=q^2 and the original marked N factors.
The exact transfer trace used to verify it is

\[
 Z_3=\frac{x^4}{3}\sum_{h=-2}^2
       \operatorname{Tr}\{D_h(M^h)^3\},\qquad
 D_h=\operatorname{diag}_{a\in I_h}x^{2a}.
\]

The five traces, in order h=-2,-1,0,1,2, are

    270+243 i sqrt3,
    27-351 i sqrt3,
    2781/2+(189/2) i sqrt3,
    -540+162 i sqrt3,
    -999/2+(27/2) i sqrt3.

Moreover

\[
 Z_3/\overline{Z_3}=(11-21i\sqrt3)/38.                 \tag{10}
\]

This cannot be a root of unity: its rational field trace is 11/19,
whereas a root of unity is an algebraic integer and a rational trace
of an algebraic integer must be an integer. Thus multiplying (9) by
ANY unit root framing phase cannot make it real. In particular the
original half-twisted scalar is not a positive norm square times the
retained framing phase and a positive scalar normalization.

This is an obstruction only to that literal norm-square identity. The
positive comparison (6) remains valid. The certificate is not an
upper-volume counterexample and does not identify a hyperbolic knot or
link from a numerical invariant. The graph without the half twists
(all e_i=0) instead has Z_3=270, consistent with the still-open genuinely
untwisted reflection question. No extrapolation from this calculation
settles arbitrary untwisted fully augmented diagrams.

### 3a. The untwisted source mismatch survives the positive-circle quotient

There is a stronger, source-exact check than merely observing that the
two permutations in Section 2 are different. Set N=3, s=3, and every
e_i=0, with the ORIGINAL cups and the one marked cap as in Section 1.
For ANY factor F satisfying FF^dagger=H, the actual packet Gram is

\[
 \boxed{\quad
 \begin{pmatrix}
    u^\dagger u&u^\dagger v\\v^\dagger u&v^\dagger v
 \end{pmatrix}
   =3^{10}\begin{pmatrix}18&10\\10&119\end{pmatrix}.
 \quad}                                                   \tag{11}
\]

This is an exact quadratic-field calculation directly in the original
physical modules. One can verify it without choosing square roots or
CD columns: put

\[
 p_{a,b,c}=27x^{-(d-a+d-b+d-c)},\qquad
 (i_1,\ldots,i_6)=(a,b,d-b,c,d-c,d-a),
\]

for a,b,c in {0,1,2}. These are precisely the 27 nonzero entries of
p_S. Permute them by P_b or P_o, and contract the two resulting vectors
against H tensor H tensor H. The literal coproduct Casimir gives
L=Omega^2-I and H=LP; their entries, and all the displayed source
coefficients, lie in Q(sqrt(-3)). The three resulting finite contractions
are respectively 18,10,119 times 3^10. The audit performs these operations
in that exact number field, separately from the numerical CD tests.

In particular

\[
 \|u-v\|^2=117\,3^{10}>0,\qquad
 \det\operatorname{Gram}(u,v)=2042\,3^{20}>0.              \tag{12}
\]

The difference therefore survives the actual image quotient: it is not
a radical vector discarded by the positive complete circle. The packets
are not even collinear. The original closed value and the two proposed
canonical packet norms are

\[
 Z_3=3^{-7}v^\dagger u=270,\qquad
 3^{-7}\|u\|^2=486,\qquad 3^{-7}\|v\|^2=3213.             \tag{13}
\]

Every equality (11)--(13) is independent of the Kraus factor: its Gram
depends only on H. Replacing a minimal F by another such factor applies
a common isometry to its channel space and cannot change it. Consistent
unitary physical duality changes, with the original sources transformed
at their ports, likewise leave these closed contractions unchanged.
Consequently removing the half-twist phases and transporting the true
dual objects do NOT turn formula (6) into either canonical norm square.

This is deliberately a limited obstruction. It does not exclude a
different projection-plane cut, a nontrivial global pairing with its
own proved source normalization, or coherent elimination before taking
a norm. The untwisted value in (13) is positive. What fails is the
specific proposed inference that the original marked source identifies
the two positive-circle boundary states after quotienting. In particular
this calculation does not replace a genuine six-port junction by a
two-port Frobenius multiplication.

## 4. Validation and remaining estimate

The [audit](../experiments/audit_actual_pretzel_circle_coherent_reflection.py)
constructs the full original generators, crossings, complete circle,
actual marked/cup source and canonical CD columns. It compares (3)
directly to (6), with all physical box ports still open before their
literal source contraction. A separate exact quadratic-field calculation
reconstructs (9) from the original matrices rather than from guessed
channel phases. It also computes (11) exactly from H and the literal
27-term original cup state; positivity, noncollinearity, and the
quotient-level mismatch are consequences of that exact Gram matrix.

The remaining sharp task is a bound for the ACTUAL constrained packets
(7), or a stronger coherent pairing than their product. Independent
local capacities do not establish this. Neither polynomial duality
transport nor the complete-circle local PSD theorem supplies the missing
global geometric incidence or selected-source energy estimate.
