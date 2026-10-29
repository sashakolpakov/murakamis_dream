# A generic all-partner factorial formula for the actual six-head source

29 October 2026. This derives the local nested-cup coefficient and its
ordinary closed trace at GENERIC zeta, for every physical pair channel
0<=j<=d=N-1, including the high partner d-j. The construction uses the
actual Clebsch maps, genuine ordered ribbon duals, and physical cups.
No root factorial reflection, conjugation, or quoted quantum 6j formula
is used. Combining the factors gives a finite double-sum expression
with an explicit root pole on each paired axis. Every actual marked
joint-cluster moment is consequently an explicitly bounded-order
Taylor coefficient, of order at most four.

This supplies the previously missing generic input for the
[actual boundary moments](actual_six_pants_boundary_torsor_and_sewing.md).
The finite double source sum below is now reduced to an exactly
normalized SINGLE generic Racah sum in
[the actual source-column identity](actual_generic_trivalent_racah_source_identity.md),
including all high partners and normal tails.
It does not prove that their ratios, the boundary Gram, or recoupling
maps have polynomial or subexponential conditioning.

## 1. Generic modules and literal duality

Fix N>=2, d=N-1. In this note Q=zeta^2 is GENERIC, and

    F_k=(Q;Q)_k, F_0=1.

The highest-weight L module, in its divided-F basis |u>, has

    F|u>=(1-Q^(u+1))|u+1>,
    Ecal|u>=zeta^(-L-1)(1-Q^(L+1-u))|u-1>,
    K|u>=zeta^L Q^(-u)|u>.

Use Delta(F)=F tensor I+K^(-1) tensor F and
Delta(Ecal)=Ecal tensor K+I tensor Ecal. The canonical cup is

    P_L(u)=(-1)^u zeta^[u(L-u-1)] F_u F_(L-u)/F_L,
    p_L(u,L-u)=P_L(u), ell_L=p_L^(-1).             (1)

Its first coefficient is one. The physical cup is pV=cV p_d,
cV=N zeta^(-d^2), exactly the regular lift of the original cup.
All generic formulas below are rational identities, so their stated
continuations do not assume denominators remain nonzero at the root.

For every j=0,...,d set l=d-j and define

    h_j(u)=(-1)^u zeta^(-du)
       Q^[u(l-1)-u(u-1)/2] F_(j+u)F_(d-u)/(F_j F_d),
          0<=u<=l,
    W_j|r>=Delta(F)^r h_j/F_r, 0<=r<=2j.          (2)

The highest E equation gives (2) directly. The E,F commutator gives
every interior covariance equation. The last F equation follows
either from the endpoint below or from the full-column-rank physical
E matrix above degree d. Thus W_j is the ACTUAL generic intertwiner
from the ordinary highest-weight 2j module, without restricting j
to the root low fold.

Here is a useful formula with ONLY physical factorial denominators.
For 0<=A,B<=d and A+B=l+r,

    W_j[r](A,B)=F_A F_B sum_u
       h_j(u) zeta^(-dt) Q^(ut)
                    /[F_u F_(l-u) F_t F_(r-t)],
    t=B-l+u,
    max(0,l-B)<=u<=min(l,A), 0<=t<=r.             (3)

Outside these ranges the entry is zero. Indeed, write Delta(F)=A0+B0
with A0 B0=Q^(-1)B0 A0, expand with the finite Gaussian binomial,
and cancel F_r. The two physical moves have lengths t and r-t;
therefore ALL four denominator indices in (3) are <=d, even when
r>=N. Formula (3) proves the entire W_j matrix is holomorphic at
zeta=q=exp(pi i/N), including the high partner channels.

Let P exchange the two physical legs. The actual right ribbon dual is

    DW_j=p_(2j)^T W_j^T(ellV^T tensor ellV^T)P,
    DW_j[r;u,v]=P_(2j)(2j-r)
       W_j[2j-r](d-v,d-u)/[pV(d-v)pV(d-u)].        (4)

There is no Hermitian conjugation in (4). The swaps and inverse cup
coefficients are fixed by the actual nested arcs.

## 2. Own endpoint and projector normalization

The generic lowest endpoint is EXACTLY

    W_j[2j](j+u,d-u)=zeta^[j(d-2j)]h_j(u).        (5)

Proof. The lowest F equation and the highest E equation have the same
coefficient ratio, so it suffices to take u=0 in (3). The remaining
finite sum is

    sum_s (-1)^s Q^[s(s-1)/2]
                  F_(d-s)/[F_s F_(l-s)F_(j-s)]=Q^(lj).

For an own finite verification, rewrite it as
F_d/(F_l F_j) times
2phi1(Q^-j,Q^-l;Q^-d;Q,1). The finite identity

    sum_(s=0)^n (Q^-n;Q)_s(b;Q)_s
         (cQ^n/b)^s/[F_s(c;Q)_s]=(c/b;Q)_n/(c;Q)_n

follows from the already
[finite-binomial proof](actual_half_color_quadratic_source_transform.md),
section2, by replacing Q,b,c with Q^(-1),b^(-1),c^(-1) and clearing
the displayed finite powers. Substitution n=j,b=Q^-l,c=Q^-d gives
the endpoint constant in (5). This is a finite summation proof,
not an assumed recoupling formula.

The exact generic norm is

    DW_j W_j=n_j I,
    n_j=(-1)^(d+j)cV^(-2)
       zeta^[j(j+1)-d(2j+1)]
                      F_(d+j+1)/[F_(d-j)F_(2j+1)]. (6)

To prove its scalarity directly, DW_j W_j commutes with the generic
ordinary K,F: its distinct K weights force diagonality, and nonzero
interior F arrows force equal entries. Take its first entry, apply
(5), and insert the cups (1). The only sum remaining is

    sum_(u=0)^l Q^[-(j+1)u]
             [j+u choose j]_Q[d-u choose j]_Q
       =Q^[-(j+1)l][d+j+1 choose l]_Q.

After multiplication by Q^((j+1)l), this is the coefficient of z^l
in 1/[(z;Q)_(j+1)(zQ^(j+1);Q)_(j+1)]. Expanding the reciprocal
finite products by their inductive coefficient formula proves it.
All remaining factors give (6).

Consequently

    e_j=W_j DW_j/n_j, j=0,...,d                   (7)

are the genuine generic pair projectors and sum to the physical
identity. Indeed they are intertwiners with distinct ordinary highest
weights; (6) gives their own nonzero retractions, and their dimensions
sum_j(2j+1)=N^2. Their pair Casimir eigenvalues are

    c_j(zeta)=zeta^(2j+1)+zeta^(-2j-1).

## 3. Finite factorial source corner and full closed trace

Take ANY ordinary triangle a,b,c in 0,...,d. Put

    J=a+b+c, r=b+c-a, r1=a+b-c, r2=a+c-b.

The original six-head source is pV_16 pV_23 pV_45. Apply DW_a,DW_b,
DW_c on consecutive physical pairs and extract ordinary output
(2a,r,0). Define the following completely explicit analytic sum:

    B_abc=sum_(k=0)^(d-max(a,c))
       h_a(d-a-k) h_c(d-c-k)
       *W_b[r1](d-c-k,a+k)
       /[P_d(d-a-k)P_d(k)P_d(d-c-k)].              (8)

Each W entry in (8) is the physical finite sum (3). Hence (8) is
a finite DOUBLE quantum-factorial sum, with at most N^2 terms;
every denominator factorial index is <N. In particular B_abc is
holomorphic on a fixed neighborhood of each chosen root, including
when a,b,c are high partners.

The literal source corner is

    sDW_abc=cV^(-3) zeta^[c(d-2c)-2c]
                                P_(2b)(r1) B_abc. (9)

To check (9), the three source cup constraints reduce the contributing
physical indices to

    (u1,u2,u3,u4,u5,u6)
       =(d-k,a+k,d-a-k,c+k,d-c-k,k).

In (4), the first W is its highest column, the third is its lowest
column (5), and the middle is W_b[r1]. Three of the six physical
inverse cups cancel the three actual source cups. The remaining
three give precisely (8). This derivation retains every original
port and source coefficient.

Let Theta_abc be the genuine ordinary invariant with corner
Theta_abc(2a,r,0)=1. The generic ordered pairing already derived by
finite Vandermonde in the
[marked two-vertex note](actual_trivalent_all_channel_marked_contraction.md),
section2, is valid WITHOUT a low-fold restriction:

    Xi_abc=D(Theta_cba)Theta_abc
       =(-1)^r1 zeta^[2c-r1(r-1)]
       F_(2b)F_r2 F_(J+1)
         /[(1-Q)F_r F_(2a)F_r1 F_(2c)].             (10)

The original ordinary closure with projectors e_a,e_b,e_c is therefore

    T_abc=sDW_abc sDW_cba Xi_abc/(n_a n_b n_c).

The reversed labels in its second factor are necessary: white is
the genuine ordered dual, not a same-order adjoint. Outside ordinary
triangle support T_abc=0 identically.

Combining ALL cups and norms yields the simpler exact formula

    T_abc=(-1)^d zeta^E/(1-Q)
       *F_r F_r1 F_r2 F_(J+1)
       *product_(j=a,b,c) [F_(d-j)(1-Q^(2j+1))/F_(N+j)]
       *B_abc B_cba,
    E=d(3a+2b+3c+3)-4a^2-4c^2+2ac-2J.            (11)

This is an actual generic source trace, not a tetrahedron assigned
by name. For a direct normalization check, multiply the two ordinary
cup factors in (9) by (10): their surviving factorials are
F_r F_r1 F_r2 F_(J+1)/[(1-Q)F_(2a)F_(2b)F_(2c)].
Division by (6) replaces F_(2j+1)/F_(2j) by 1-Q^(2j+1).
All physical scales cV cancel. The total sign is (-1)^d, since
r1+J is even, and the remaining zeta exponent is E. Formula (11)
keeps the ordinary quantum dimension and every high-partner term.

## 4. A nonsingular coefficient formula for every marked cluster moment

Now specialize near the principal root q=exp(pi i/N), using the
NORMAL COORDINATE

    Z=1-zeta^(2N), zeta=q(1-Z)^(1/(2N)), zeta(0)=q. (12)

This specifies the analytic germ; it is not a free physical-color
parameter. For each folded label l_i<=floor(d/2), take branches

    J_i={l_i,d-l_i} if 2l_i<d,
    J_i={l_i}       if 2l_i=d.

Let r0 be the number of paired axes. It is fixed for all <=8 branch
triples. Each denominator F_(N+j) in (11) contains exactly one
factor Z. On an odd simple axis, 1-Q^(2j+1)=Z cancels it. Therefore

    G_abc(Z):=Z^r0 T_abc(zeta(Z))                  (13)

is EXPLICITLY holomorphic, by replacing each F_(N+j) by F_(N+j)/Z
and each odd simple numerator 1-Q^(2j+1) by 1. No cancellation of
large singular matrices is needed to evaluate this formula.

Use the literal root polynomial L_N(z)=(-1)^d U_d(z/2). A legitimate
generic lift of the actual root eta on an axis is L_N(Omega(zeta))
times its analytic full cluster projector. At a paired branch j,

    L_N(c_j(zeta(Z)))=Z ell_j(Z),
    ell_j(Z)=(-1)^d zeta^[-d(2j+1)]
       *[sum_(v=0)^(2j) (1-Z)^v]
                      /[1-zeta^(4j+2)].           (14)

The denominator in (14) is a root unit on every paired axis. This
is the finite character identity, not an omission of a Hermite jet.

For I a subset of the paired axes, define

    H_I(Z)=sum_(a,b,c)in(J_1,J_2,J_3)
                  G_abc(Z) product_(i in I) ell_(j_i)(Z),
    k_I=r0+1-|I|, 1<=k_I<=4.                      (15)

Then the ACTUAL original marked boundary moment is EXACTLY

    m_I=(-1)^d(q-q^(-1)) [Z^k_I] H_I(Z).          (16)

In particular the top-circle moment needs one normal; the empty
moment can require four. All lower moments, high fold partners and
their cancellations are retained. This formula applies outside the
regular saturation region too; no unsupported cell has been deleted.

Proof of the coherent cancellations. At the root, distinct Casimir
nodes coalesce only in the pairs j,d-j. The finite-dimensional Riesz
projector for such a whole cluster is analytic and equals e_j+e_(d-j)
generically; at a simple node it is e_j. This can equally be written
by finite polynomial Chinese remainders. Thus the original closed
physical lift with selected circles is the REGULAR function

    F_I(Z)=Z^(|I|-r0)H_I(Z).

Keep the original globally exposed marked outer cap (16); the other
caps are ordinary. Cutting it and bending with the SAME physical cup
gives a generic Hopf endomorphism of V_N. Its distinct generic K
weights and nonzero F arrows force a scalar z_I(zeta)I. The open
maps are regular because the FULL cluster projectors and all actual
physical maps are regular. Its ordinary trace is

    F_I(Z)=D_N(zeta) z_I(zeta),
    D_N=(-1)^d[N]_zeta
       =(-1)^(d+1) zeta^(-N) Z/(zeta-zeta^(-1)).

Hence H_I is divisible by Z^k_I, exactly. The original unrestricted
marked row applied to the original cup is one, so m_I=z_I(q).
Taking the coefficient gives (16), since q^(-N)=-1. It agrees with
the t-normal formula F_I'(0)/nu_N for zeta=q exp(t), but removes
all apparent negative Laurent orders before computing that normal.

This is a regular Hopf lift of the prescribed ROOT moment. It does
not identify a formal continuation of a root scalar with the actual
moving-q circle or colored-source family. Lift independence follows
from the exposed physical scalar cut and its identical root maps.
A bare marked row at an arbitrary nested white cap is not substituted
for this cut; see the corrected hypothesis in the
[first-normal source theorem](actual_nc_morse_graph_first_normal_source_reduction.md).

## 5. Bounded jets and the remaining analytic gate

Equations (3),(8),(11)--(16) give a finite algorithm with no matrix
minor inversion. There are <=8 branches, each B has <=N^2 terms,
and every needed jet order is <=4, independently of N. The generic
qdim has not been canceled before the actual marked quotient, nor
have the first normals of paired circles been replaced by values.

The formulas also admit explicit factorial ENVELOPES for their fixed
jets. Divide every root-zero factor out first. On |Z|<=c/N^2, each
remaining quantum factor with index<=3N changes by relative O(1/N),
uniformly, because its nonzero root magnitude is >=2sin(pi/N), while
the change of its exponent is O(|Z|). The product of O(N) factors
is therefore bounded by a constant times its root product. Powers
zeta^E, |E|=O(N^2), have the same property. Cauchy's coefficient
bound multiplies this envelope by at most C_k N^(2k) at fixed order k.
The finite character in (14) costs an additional polynomial factor.
Applying this termwise to the explicit finite sums gives genuine
bounded-normal factorial upper bounds, with only polynomial jet cost.

This does NOT prove that m_I/m_top or the boundary square-root unit
has polynomial growth. The absolute factorial envelope can exceed
the coherent top moment, and (16) retains cancellations between
different high/low branches and different summands. A quantitative
comparison for that EXACT coefficient remains necessary for a tame
source-aware Gram or general graph sewing theorem.

Audit: [generic full physical and root-normal comparisons](../experiments/audit_actual_generic_six_head_tetrahedral_source.py).
The audit checks 11 generic finite-field families, all j=0,...,d,
784 literal source corners, and 134 full physical ordinary closures.
It also checks 14 actual root joint-cluster families through N=7,
all marked moments on each cluster, including unsupported triples,
and exact cancellation of every pole and ordinary trace constant.
These finite checks supplement the derivations and do not establish
conditioning or a new graph volume limit.

Internal review: the primary agent and the independent conditioning
agent read the full finite source and marked-normal derivation. The
latter also replayed the audit and independently checked the complete
phase in (11), all high-partner pole cancellations, the Z/nu_N sign,
and the required orders in (16). Both reviews passed. This records
internal proof review, not external peer review or a conditioning theorem.
