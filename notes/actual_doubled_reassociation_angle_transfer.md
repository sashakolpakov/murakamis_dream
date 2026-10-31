# Coherent doubled reassociation and one-power angle transfer weights

29 October 2026. An actual reassociation packet has an exact doubled
Gram with FOUR one-power affine-angle weights on its diagonal. The
shared-head positive trace has a literal Fourier/Kraus summation and
an unwrapped physical edge constraint. Its off-diagonal terms retain
the two-copy phases; they are not replaced by a product of magnitudes.

An operator Cauchy inequality then gives an explicit positive path
majorant for ANY fixed signed plat, with its original source and
cap supports retained. This is an actual bound, not a new invariant.
The raw path majorant has an
[actual-source oversized closed-route obstruction](actual_closed_pascal_route_energy.md),
so it cannot itself supply the sharp knot-volume bound. The physical
shared-head equation alone is not the ideal edge-angle identification.
The [ordinary-cap coherent collapse](actual_pivotal_cap_reassociation_angle_packet.md)
is a source-specific way to improve it before any such dephasing.

## 1. Literal finite Euler transfers and the source-fixed metric

Keep N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=-q^-1 and
s_a=|(Q;Q)_a|. On an actual physical pair define

    V_12=x^-1 S_1^- F_2,
    S^-|a>=|a-1>, S^-|0>=0,
    F|b>=(1-Q^(b+1))|b+1>, F|d>=0.

The original normalized Borel transfer and its literal inverse are

    C'_12=p_N(V_12),
    (C'_12)^-1=sum_(r=0)^d (-1)^r Q^[r(r-1)/2]V_12^r/F_r,
    p_N(t)=sum_(r=0)^d t^r/F_r, F_r=(Q;Q)_r.                (1)

These are finite nilpotent matrices, not source-free cyclic
completions. Their exact coefficients are

    C'_12|a,b>=sum_r x^-r [b+r choose r]_Q |a-r,b+r>,
    (C'_12)^-1|a,b>
       =sum_r (-1)^r Q^[r(r-1)/2]x^-r
                                  [b+r choose r]_Q |a-r,b+r>, (2)
    0<=r<=min(a,d-b).

The formula follows by applying V_12^r; its F product is
F_(b+r)/F_b. The inverse in(1) follows from the finite Euler
identity modulo V_12^N=0. All endpoint terms and its actual
inverse phases are retained.

Use the physical metric and its coordinate gauge

    h_a=sqrt(N)/s_a=L_a^-1/2,
    B=diag(sqrt(h_a))=L^-1/4.                              (3)

This is a PHYSICAL head metric, not the length-register D_l frame.
Since h_a h_(d-a)=1, the gauge B on paired heads fixes the actual
cups and ordinary caps pointwise; its marked source use retains
the already proved whole-operator degree restriction. Pivots are
diagonal and commute with B. The full original source is therefore
transported as in the physical weighted-Fourier theorem. No ordinary
positive pivotal trace is presumed.

Write hats for conjugation by the appropriate tensor power of B.
Set beta(L,r)=s_L/(s_r s_(L-r)). Directly from(2),(3),

    |C'hat_12[(a-r,b+r),(a,b)]|^2
       =beta(a,r)beta(b+r,r)
       =N^2 w_d(r,a-r,d-a)w_d(r,b,d-b-r),                 (4)
    w_d(i,j,k)=1/(s_i s_j s_k), i+j+k=d.

The inverse has exactly the same diagonal energy weights. This
includes r=0 and all allowed endpoints, with s_0=1. Each w appears
ONCE in the doubled diagonal weight. The original coefficients
were not replaced by positive weights before being squared.

## 2. The actual three-head packet and its complete doubled Gram

Let

    A=(C'_23)^-1 C'_12.                                    (5)

Given input i=(a,b,c), its allowed outputs are

    o=(a-r,b+r-s,c+s),
    0<=r<=min(a,d-b), 0<=s<=min(b+r,d-c).                  (6)

The intermediate state (a-r,b+r,c) is UNIQUE. Consequently

    A[o,i]=(-1)^s Q^[s(s-1)/2]x^[-(r+s)]
                     [b+r choose r]_Q [c+s choose s]_Q.    (7)

This is the whole actual packet, including the inverse's finite
current/wall data. It is not the homogeneous part of a separate
beta expansion. Its exact integer support has not been relaxed.

In the metric(3), write

    Ahat[o,i]=q^[r(b-d)+s(c+s)] sqrt(W(i;r,s)),
    W=N^4 product_(j=1)^4 w_d(t_j),                         (8)

where

    t_1=(r,a-r,d-a),
    t_2=(r,b,d-b-r),
    t_3=(s,b+r-s,d-b-r),
    t_4=(s,c,d-c-s).

The phase in(8) uses the exact identity
[L choose r]_Q=q^[r(L-r)]beta(L,r) and x=q^d. No half integer
modular inverse is used. It is valid at both parities. Its
positive gauge changes no phase.

For an arbitrary boundary matrix D, including a matrix-valued
exterior, the complete doubled contraction is

    (Ahat^* D Ahat)_(i,j)
       =sum_(o,o') conjugate(Ahat[o,i]) D_(o,o') Ahat[o',j]. (9)

Thus mixed copies have their actual phase DIFFERENCE and a square
root of the two diagonal W weights. Formula(9) does not set i=j
or o=o' before the exterior has specified that contraction.

If a different exact factorial presentation uses an explicit
Theta current, substituting its FULL identity into(9) gives the
same Gram, including all cross terms with that current. One must
not add a second independent current to(7), nor keep only its
homogeneous summand. The separate tame-current metric L^(1/2) is
not silently identified with the quarter gauge(3).

## 3. What a shared-head Fourier/Plancherel sum really does

For a positive input density rho define the actual positive map

    E(rho)=Tr_(middle output)[Ahat rho Ahat^*].                (10)

For each physical middle color M=0,...,d, let K_M be the matrix
obtained from Ahat by fixing its middle output to M and retaining
its two outer output ports. Then EXACTLY

    E(rho)=sum_(M=0)^d K_M rho K_M^*.                         (11)

Its term between copies (i,r,s) and (j,r',s') carries

    M=b+r-s=b'+r'-s'.                                      (12)

This is an UNWRAPPED equality, not a permitted extra alias.
It has either exact Fourier expression

    delta_(M,M')=(1/N)sum_(ell=0)^d Q^[ell(M-M')]
      =(1/(2N))sum_(ell=0)^(2N-1)q^[ell(M-M')].             (13)

Both are alias-free here because M,M' lie in0,...,d. Applying
the unitary Fourier matrix to the Kraus list merely replaces
K_M by its Fourier combinations and leaves(11) unchanged.

This is a genuine coherent shared-head sum. It leaves the mixed
outer/input copies of(9) and their phases. It does not assert
that a coherent INTERNAL wire in the original scalar can simply
be traced or phase-averaged: if its actual exterior couples M
and M', that matrix stays in(9). Nor does(12) identify a
triangulation's positive edge sum2d. Such a geometric incidence
requires the separate oriented/source map.

The measure in(11) is a positive Hilbert trace in the doubled
energy, not the ordinary pivotal trace at complete color. All
original pivots and cut rows remain in the external observable.

## 4. A quantitative diagonal-observable inequality

Let D=diag(d_o) with d_o>=0. Every output o of A has at most N^2
possible inputs i: its fixed total degree determines b once a,c
are chosen. Rowwise Cauchy--Schwarz in(9) therefore proves the
operator inequality

    Ahat^* D Ahat <=N^2 diag(T_A^t d),
    (T_A)_(o,i)=|Ahat[o,i]|^2.                              (14)

In particular its explicit column energy is

    E_i=N^4 sum_(r,s satisfying6) product_j w_d(t_j),
    Ahat^* Ahat <=N^2 diag(E_i).                            (15)

This is an actual all-input estimate AFTER the two finite Euler
operators and their current data have been combined into A.
The same proof for one C' or its inverse uses at most N inputs
per output and the two once-power weights(4):

    C'hat^* D C'hat <=N diag(T_(C')^t d).                   (16)

Tensoring spectator identities changes none of these counts.
Equation(14) is an inequality, not a claim that the off-diagonal
Gram terms vanish. It explicitly pays a polynomial factor when
they are estimated. Other coherent packet Grams can improve it.

## 5. A full original signed-plat consequence

The actual Pascal/fusion alphabet proves, without any source-null
remainder,

    R_+=kappa C'_12 D_2 C'_21 (C'_12)^-1,
    R_-=kappa^-1 C'_12 (C'_21)^-1 D_2^-1 (C'_12)^-1,          (17)

where D_2 is the original diagonal Gaussian, of unit modulus at
complete color, and kappa is the original Cartan scalar. This
follows also by C=C'diag(F_a) in the actual Borel factorization;
conjugating its opposite transfer by diag(F_a) gives C'_21.
All factors are the strict physical matrices in(1), including
the top/bottom walls. There is no independent cyclic or ghost
source discarded in(17).

Let the original 2k-head plat have m signed crossings, and write
its literal source as

    P_N=chi_N N^(k-1)<phi,W u>, ||phi||=||u||=1,

with the actual normalized cups u and the actual pivoted cap phi.
The quarter gauge fixes these paired source vectors. Let P_cap
be the diagonal projector onto degree d on EACH final cap pair.
The unit vector phi lies in its range, so

    |phi><phi| <=P_cap.                                     (18)

This retains the actual cap support; it does not replace the
original invariant by an ordinary positive trace.

Expand each crossing by(17), combine any desired exact packets
BEFORE estimating, and apply(14) or(16) backwards to(18).
Gaussian phases act trivially on diagonal observables. If the
uncombined alphabet contains L=3m C' factors, define the explicit
positive physical-path sum

    Z_path=sum_(i_0,...,i_L)
             |u_(i_0)|^2 1_cap(i_L)
                  product_(j=1)^L |C'hat_j[i_j,i_(j-1)]|^2. (19)

Here |u_i|^2=N^-k on the original input cup-complement states
and zero elsewhere. Every physical index lies in0,...,d and
every transfer has its exact unwrapped support. Then

    |P_N|^2 <=|chi_N|^2 N^(2k-2+3m) Z_path.                 (20)

This is a uniform bound for arbitrary fixed braid/bridge width.
It keeps the whole original external line. Each factor in(19)
is exactly N^2 times TWO one-power affine-angle weights, by(4).
Grouping adjacent reassociations replaces two steps by(8),(14)
with their four one-power weights and the corresponding N^2
row count. Other exact contractions can be performed first too.

The resulting positive path space has honest source boundary
conditions and physical conservation laws. This note does not
claim that these are the ideal triangulation's complete edge
constraints, or that its maximum angle volume is Vol(S^3-K).
Those are the remaining geometric-energy requirements. In
particular(20) by itself is not the sharp volume theorem. More strongly,
the [checkerboard closed-route theorem](actual_closed_pascal_route_energy.md)
exhibits, on the authorized original averaged trace source at N=3r+1,
a positive path of squared weight N^(4m)w_d(r,r,r)^(4m) in every
length-m signed word. Its rate 4m v_3/pi can increase under word
normalizations while the knot period is unchanged. Some such routes
cancel even within a local R entry: this is a path-majorant obstruction,
not a nonzero complete clock-sector assertion. Coherent source grouping
must precede a sharp estimate. The pivotal-cap identity linked above
gives one such exact grouping and its one-angle energy.

[Audit](../experiments/audit_actual_doubled_reassociation_angle_transfer.py):
the literal finite inverse, exact four-weight phases, doubled
Kraus/Fourier sum, operator inequalities, and complete original
signed-plat source bounds.

The finite audit checks four exact mixed-copy/Fourier packet families and
four complete original signed-plat source inequalities, with literal
Cartan scalar and pivots retained. The all-level statements follow
from the displayed finite operator identities and Cauchy inequalities.