# Actual braid transport has a flat Borel-relative algebra and a divided cap period

Research proof, 27 October 2026. The actual diagonal quantum Borel
action has an explicit free fusion basis. Actual crossing words become
matrices over a finite flat algebra, including at the original nilpotent
source. The pivotal highest-input cap is an explicit Frobenius functional
with its marked density. It is a divided central-F trace on a cyclic
chart; bare semisimple reduction loses a nonzero actual period.

This supplies an actual word AND source comparison, rather than only
an auxiliary source-frame classification. Its target is not identified
with a geometric gluing algebra or the A-polynomial. The central-F
parameter below is not identified with the meridian or Q-normal.

## 1. The actual Borel algebra and its flat central extension

Fix the actual root Q=exp(2 pi i/N), N at least two. On each regular
holonomy splitting module retain K_i=x_i diag(Q^(-j)) and the actual
F_i with F_i^N=phi_i. We can use the original balanced head frame:
its nonwrapping arrow j to j+1 is 1-Q^(j+1), and its wrapping arrow
is phi_i/N. This is exactly the factorial gauge of the regular
module, not an altered representation. Put

\[
 H=(K_1\cdots K_b)/(x_1\cdots x_b),\qquad
 f=\Delta^{b-1}F=\sum_{i=1}^bK_1^{-1}\cdots K_{i-1}^{-1}F_i.
\]

Actual quantum-group multiplication and the root binomial identity give

\[
 H^N=1,\qquad Hf=Q^{-1}fH,\qquad
 f^N=\Phi:=\sum_{i=1}^b(x_1\cdots x_{i-1})^{-N}\phi_i.    \tag{1}
\]

For example for two terms A=F_1,B=K_1 inverse F_2 one has
BA=QAB, so all intermediate coefficients of (A+B)^N vanish.
Iteration proves (1). Every complete center and meridian factor
is retained in Phi.

Define the algebra A_Phi by these three relations, with idempotents

\[
 e_j=\frac1N\sum_{a=0}^{N-1}Q^{ja}H^a,\quad
 z_{a,j}=f^a e_j,\quad 0\leq a,j<N.
\]

It has the EXPLICIT free basis z_(a,j). Multiplication is

\[
 z_{a,j}z_{c,k}
   =\begin{cases}
      \Phi^{\lfloor(a+c)/N\rfloor}
              z_{a+c\bmod N,k},& k=j-c\pmod N,\\
      0,&\text{otherwise}.
     \end{cases}                                            \tag{2}
\]

This formula is associative (it records the shift of the idempotent
and total integer f exponent) and realizes all defining relations,
so it also proves the basis assertion without a dimension guess.
Thus this is a flat rank-N-squared algebra over the WHOLE Phi base.
At Phi=0 its ideal (f) is nonzero, nilpotent and two-sided, with
quotient the N diagonal characters. It is the truncated quantum
Borel algebra, also known as a Taft algebra. It is not Mat_N there.

For Phi nonzero the cyclic module f e_j=e_(j+1) for j<N-1 and
f e_(N-1)=Phi e_0, with H e_j=Q^(-j)e_j, gives Mat_N. The
idempotents and nonzero cyclic arrows exhibit every matrix unit.
After retaining a root rho^N=Phi, the normalized shift f/rho has
Nth power one and gives a cyclic companion frame. This is a
generic cyclic chart, not an extension of its bare matrix algebra
through the nilpotent source.

## 2. Explicit free fusion for any number of actual strands

For b=2 let u=e_0 tensor ones, and define

\[
 \mathcal F:A_\Phi\longrightarrow V_1\otimes V_2,
       \quad z_{a,j}\longmapsto f^a(e_0\otimes e_j).        \tag{3}
\]

This is A_Phi-linear, because e_j u=e_0 tensor e_j. It is an
isomorphism, including on Phi=0. Indeed the unique term with first
output index a is F_1^a(e_0) tensor e_j, with coefficient
(Q;Q)_a. Every other term has first index strictly smaller than a.
No first-leg wrap occurs in fewer than N applications. In order
of first index, (3) is block triangular with diagonal
(Q;Q)_a times I_N. These are original nonzero factorial units.
The determinant is their product, independent of phi_1,phi_2.

For b greater than two, let t=(t_3,...,t_b) index the remaining
physical heads and set u_t=e_0 tensor ones tensor e_t. Then

\[
 A_\Phi\otimes R^{N^{b-2}}\longrightarrow V_1\otimes\cdots\otimes V_b,
        \quad a\otimes t\longmapsto a u_t                 \tag{4}
\]

is again an isomorphism. The projector e_j selects the unique
second index j-sum(t_i) modulo N; all-first-leg f terms give the
same triangular diagonal (Q;Q)_a. Hence the actual tensor module
is a FREE left A_Phi module of rank N^(b-2). This is a non-naive
fusion basis built from the actual coproduct; no proposed product
of two repaired head shifts has been substituted for it.

The inverse is regular in all phi_i because that determinant is
a fixed unit. Every actual matrix, source vector, cap and current
has an exact conjugate under (4). There is no discarded endpoint,
choice of replacement co-source or asymptotic remainder here.

## 3. Actual local R and arbitrary words act on this relative algebra

The actual checked R intertwines the diagonal coproduct. On the
same-color nilpotent section it commutes with H and f. Therefore
(4) takes each actual local crossing and inverse into

\[
           \operatorname{End}_{A_\Phi}(A_\Phi^{N^{b-2}})
                    \cong \operatorname{Mat}_{N^{b-2}}(A_\Phi^{op}).
                                                                  \tag{5}
\]

For two strands it is right multiplication by a unique unit a_R,
computed from R u using (3). It is NOT an unspecified scalar:
the literal actual R matrix, including its half-Cartan and scalar
line, fixes a_R. Composition and every signed braid relation follow
by conjugating the actual word through the same basis change.

The same construction applies to the full actual holonomy Hom
line on its admissible splitting covers in
[the regular holonomy theorem](regular_holonomy_braiding.md).
The checked map preserves the diagonal coproduct, the product of
the marked K roots and Phi in (1). Source and target versions of
(4) give A_Phi-linear maps. Retain the actual Hom line and all
closing root phases; no new global scalar frame is supplied here.
The semicyclic case is the explicit polynomial intertwiner in
[the carry-braiding theorem](semicyclic_carry_braiding.md), including
its transported centers and corrected wrap factor.

Thus (5) is actual root-parameter word transport across central
Phi=0, not an assertion of topological invariance of a new period.
The original selected word and its original source are transported
together. On the nilpotent section their value is exactly the
original invariant with every external normalization retained.

## 4. A regular Frobenius functional is a divided cyclic trace

Define on the WHOLE flat algebra

\[
                  \tau_{top}(z_{a,j})=\delta_{a,N-1}.
\]

Its left-dual basis is explicitly

\[
 d_{a,j}=f^{N-1-a}e_{j+a\bmod N},\qquad
 \tau_{top}(d_{a,j}z_{c,k})=\delta_{a,c}\delta_{j,k}.        \tag{6}
\]

No Phi enters this Gram matrix: a matching product has exponent
N-1 and never crosses a full f cycle. Thus this is a nondegenerate
Frobenius functional on every fiber, including the nilpotent one.
For any actual co-source Lambda on this relative algebra the
marked density is the explicit finite element

\[
 C_\Lambda=\sum_{a,j}\Lambda(z_{a,j})d_{a,j},\qquad
                 \Lambda(a)=\tau_{top}(C_\Lambda a).       \tag{7}
\]

For several strands apply (7) to each relative matrix entry.
Their coefficients are the literal pulled-back pivotal/cut rows
from (4). This gives a concrete relative period for an arbitrary
actual braid, not a replacement regular trace.

For clarity the arbitrary-braid source formula is explicit. Let
s,t index the tail labels of (4), and let a_(t,s) in A_Phi be
the actual relative word matrix: its action is a tensor s to
sum_t a a_(t,s) tensor t. For a closed input tuple (c,s), with
c the second physical input, put k=c+sum_i s_i modulo N. Define
the actual finite rows

\[
 L_{(c,s),t}(z)
  =(\mathrm{ones}^t\otimes e_c^t\otimes e_s^t)
                              \mathcal F(z\otimes t),
\]
\[
 \Lambda_{t,s}(z)
  =\sum_{c=0}^{N-1}\left(g_2(c)\prod_{i=3}^b g_i(s_i)\right)
                                L_{(c,s),t}(e_k z).
\]

The g_i are the original pivotal entries with their actual colors.
The original period, with its assigned external line gamma_beta,
is EXACTLY

\[
 P_\beta=\gamma_\beta\sum_{t,s}\Lambda_{t,s}(a_{t,s})
        =\gamma_\beta\sum_{t,s}\tau_{top}(C_{t,s}a_{t,s}),  \tag{7a}
\]

where C_(t,s) is given by (7). This uses the original INPUT e_0
on the first strand, the SUM over its output, and every other
original pivotal closure. Indeed e_k u_s is the literal input
e_0 tensor e_c tensor e_s. Applying the A_Phi-linear word then
gives this formula entry by entry. All closing identifications
and the root of total K remain on their original cover. On the
cyclic chart (7a) is the sum of Tr_N(f C_(t,s) a_(t,s))/Phi by
(8), with its regular divided extension at Phi=0. No unspecified
cap functional is introduced.

In the N-dimensional cyclic splitting of Section 1, a stronger
WHOLE polynomial identity is

\[
             \operatorname{Tr}_N(fa)=\Phi\,\tau_{top}(a).  \tag{8}
\]

It suffices to check the basis: only a=f^(N-1)e_j contributes,
when f a=Phi e_j. Consequently tau_top is exactly the retained
DIVIDED central-F normal trace Tr(fa)/Phi, regular at Phi=0.
Bare ordinary trace kills the nilpotent ideal and loses this value.
The Frobenius functional is twisted rather than cyclic: its
Nakayama transport is H to QH, f to f. It becomes conjugation
by f only on Phi nonzero. No categorical modified-trace axioms
are claimed solely from (6)-(8).

## 5. The actual two-leg cap density is explicit

On the actual nilpotent same-color section put F_a=(Q;Q)_a,
x=K on e_0 and g_j=(xQ^(-j))^(1-N). For a right multiplication
operator R_a on A_0, the original highest-input pivotal cut is

\[
 \Lambda_{cap}(a)=\sum_{j=0}^{N-1}g_j L_j(e_j a),\quad
 L_j(z)=(\mathrm{ones}^t\otimes e_j^t)\mathcal F(z).        \tag{9}
\]

All zero-framing, full d_N(M) and common crossing lines remain
their original external factors. There is no extra 1/N here.
For the basis z_(a,k), the finite binomial expansion of the ACTUAL
coproduct gives

\[
 \Lambda_{cap}(f^a e_k)=
 \begin{cases}
  x^{1-N-a}Q^{-(k+a)}F_{k+a}/F_k,& k+a<N,\\
  0,&k+a\geq N.
 \end{cases}                                                \tag{10}
\]

For the first case e_j f^a e_k requires j=k+a, and closing the
second output at j forces all a lowering steps onto that leg.
In the second case the required wrap is zero. This proves (10)
with the original pivotal weights rather than an abstract trace.

The density in (7) factors explicitly as C_cap=L R with

\[
 L=\sum_{j=0}^{N-1}\frac{x^j}{F_j}f^j e_{N-1},\qquad
 R=\sum_{k=0}^{N-1}x^{1-N-k}Q^{-k}F_k
                                  f^{N-1-k}e_k.
\]

The multiplication rule (2) gives

\[
 R L=\gamma e_{N-1},\quad C_{cap}^2=\gamma C_{cap},\qquad
                  \gamma=N x^{2-2N}Q\ne0.                 \tag{11}
\]

Thus the cap is a marked primitive projective density, with its
full source character gamma retained. Formula (11) is asserted
on Phi=0 here: modulo the nilpotent ideal C_cap/gamma is the
primitive idempotent e_(N-1), so it is primitive. A generic cyclic cap must keep its actual wrap
coefficients. Neither cyclicity of tau_top nor erasure of gamma
is used to convert it into a preferred modified trace.

## 6. An actual period detects the nilpotent relative source

At N=2, q=i, eta=exp(pi i/4), x=i, direct use of the actual
positive balanced R gives

\[
                       a_R=\eta I+\frac{\eta^{-1}}2 f e_0.
\]

Here (f e_0)^2=0 and the second term lies in the nilpotent radical.
The ORIGINAL cap (9)-(10) satisfies

\[
                 \Lambda_{cap}(I)=0,\qquad
                 \Lambda_{cap}(f e_0)=2.                  \tag{12}
\]

Thus Lambda_cap(a_R)=eta inverse, the actual nonzero one-crossing
cut before its retained external lines. Its entire value comes
from the radical term; semisimple reduction gives zero. More
generally Lambda_cap(a_R^m)=m eta^(m-2) in this example. The
full framing and modified-dimension lines multiply these exact
values and have not been reset.

This is an actual source obstruction to factoring the word period
through the semisimple quotient, not the previously noted failure
of a naive tensor product of repaired shift pairs. The regular
module's ordinary trace also kills the radical, whereas the actual
divided cap functional does not.

## 7. Quantum normal and geometric comparison remain distinct

The flat A_Phi transport is at a fixed original root Q. It does
not by itself extend through a moving Q^N normal. For example,
at N=2 the original finite matrices have

\[
 f_{tot}^2=(1+Q)F_1K_1^{-1}F_2,\qquad
 \left[\frac{f_{tot}^2}{1-Q^2}\right]_{Q=-1}
                    =\tfrac12F_1K_1^{-1}F_2\ne0.          \tag{13}
\]

On the actual highest product source at x=i its all-ones output
value is -2i. A claimed whole Q-normal Taft model setting f^N=0
would erase this real actual current. Its divided-power/endpoint
extension must be kept. The central Phi normal, the meridian
norm and the Q-normal are not equated by their notation.

The construction provides an actual non-naive word/source
transport and an explicit divided-trace period candidate before
jets in the central parameters. It still does not identify that
period with the marked geometric Bloch regulator, prove survival
of its geometric block under the final finite source, or control
its hyperbolic-volume norm. The smooth companion frame alone
does not supply those additional identifications.

There is a further essential distinction. Phi in this note is the
Frobenius-center value of a coproduct power at a FIXED root Q_N.
It is not a coordinate on the q-to-one geometric critical variety.
At the actual M=1 augmentation all root central meridians are I.
The direct Wirtinger induction in
[the closed-braid center calculation](closed_braid_period_line.md),
Section 4, proves that its completed knot-representation germ is
entirely abelian. Consequently deforming this center/source family
locally at that closed augmentation cannot produce the hyperbolic
flat connection. The generic semicyclic comparison remains on its
reducible character locus.

The full holonomy line and this fusion basis can be considered at
other admissible center points, but that does not continue the
specified augmentation frame or identify its selected period on
another component. Any regulator comparison must leave this local
germ by an independently proved global center or q-to-one critical
source transform. The exact socle/divided-trace formula by itself
does neither. In particular its nonzero nilpotent source class must
not be renamed the geometric period or its coefficient.

[Exact actual fusion, R, cap and normal checks](../experiments/audit_actual_borel_regular_fusion.py)
and [saved output](../experiments/actual_borel_regular_fusion_results.json).
