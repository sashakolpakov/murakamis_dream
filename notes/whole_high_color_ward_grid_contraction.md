# A whole actual high-color Ward contraction by grid flow

Research theorem, 27 October 2026. Four ACTUAL integral quantum-group
words give a pole-free contraction of the full high-color matrix
Ward complex onto its scalar line. The construction uses two
diagonal spectra and a connected grid of nonvanishing ordinary
and divided arrows. Every denominator is a unit at the marked
root; no power of 1-Q^N is inverted. The original cut source has
an explicit whole cochain homotopy to normalized trace, including
the formerly resonant Frobenius corner.

The result is a finite actual source/current contraction. It does
not identify a partial geometric Gaussian module with this matrix
complex, and does not identify low-color and high-color normal
jets. Whole source units and the frozen pivotal cap correction
remain part of any such comparison.

## 1. Four actual words and the whole coefficient ring

Fix N>=2, r>=1, D=N(r+1), m=D-1. Use the ACTUAL integral Weyl
color D_m(q) in the constant sign basis w_(R,S),
0<=R<=r, 0<=S<N, of
[the high-color construction](high_integral_color_frobenius_wall_source.md).
The integer position is j=NR+S. Write

    K=q^m Q^(-J), Q=q^2,
    F=the original ordinary lowering generator,
    L=F^(N)=F^N/[N]_q!,
    H=tau [E^(N),F^(N)], tau=(-1)^(Nr-1).            (1.1)

The divided matrices in (1.1) are their regular integral Gaussian
matrices, not singular quotients specialized separately. All four
are actual U_q words. In particular their coproducts retain the
mixed ordinary/divided terms; neither H nor L is declared to have
a primitive tensor coproduct.

K is diagonal with entries k_(R,S)=q^(m-2NR-2S). Both divided
matrices preserve S and shift R by one, so H is diagonal for ALL
q; denote its entries by h_(R,S)(q). At the marked root
q_N=exp(pi i/N), Q_N=q_N^2,

    K_0=q_N^m I_Fr tensor diag(Q_N^(-S)),
    H_0=diag(r-2R) tensor I_head,
    F_0=I_Fr tensor F_St,
    L_0=f_r tensor I_head,                           (1.2)

where F_St has entries [S+1]_(q_N), and (f_r)_(R+1,R)=R+1.
The sign basis is the actual one proving (1.2); no additional
q-factorial head gauge is needed.

Work in the rational local coefficient ring at q_N, enlarged only
by the original source units and the following finitely many units:

* k_(R,S)-k_(T,U) for S!=U;
* h_(R,S)-h_(T,S) for R!=T;
* the selected nonwrap F arrows and L arrows below.

Their root values are respectively
q_N^m(Q_N^(-S)-Q_N^(-U)), 2(T-R), [S+1]_(q_N), R+1,
all nonzero. Thus this is a whole rational localization before
normal completion. The wall delta=1-Q^N is never inverted.

## 2. Off-diagonal recovery separates the two actual spectra

For a four-tuple of matrices X=(X_K,X_H,X_F,X_L), define O(X)
to have zero diagonal and

    O(X)_(R,S;T,U)=
      (X_K)_(R,S;T,U)/(k_(R,S)-k_(T,U)),        S!=U,
      (X_H)_(R,S;T,S)/(h_(R,S)-h_(T,S)),        R!=T.  (2.1)

The two cases are disjoint. Consequently, for every matrix C,

    O([K,C],[H,C],0,0)=C_off.                       (2.2)

The K row resolves every different head residue. The H row
resolves the repeated K eigenvalues between different Fr blocks,
including the extreme corner (r,0). Its root gap there is -2r.
This is the whole full-grid extension of
[the actual wall unit](actual_divided_ward_closure_and_green_caps.md).

## 3. Diagonal recovery is an explicit finite tree flow

Choose the comb tree rooted at (0,0). It consists of every
horizontal nonwrap edge

    (R,S)->(R,S+1), 0<=R<=r, 0<=S<N-1,

and the vertical trunk

    (R,0)->(R+1,0), 0<=R<r.

There are D-1 edges and every vertex has a unique root path.
For a horizontal edge e:u->v put a_e(q)=F_(v,u); for a vertical
edge put a_e(q)=L_(v,u). These are exactly the actual units of
Section 1. Define the current gradient

    d_e(X)=(X_F)_(v,u)/a_e      on horizontal edges,
    d_e(X)=(X_L)_(v,u)/a_e      on vertical edges.    (3.1)

Both F and L have one possible incoming and outgoing arrow at
each vertex in their respective direction. Hence, even if C has
off-diagonal entries,

    d_e([K,C],[H,C],[F,C],[L,C])=C_(u,u)-C_(v,v).   (3.2)

No off-diagonal subtraction is needed in this four-row version.

For an edge e let T_e be its child subtree and n_e its number of
vertices. Let Q_e be the diagonal matrix

    (Q_e)_(v,v)=n_e/D-1_(v in T_e).

It has trace zero. The explicit tree-flow primitive is

    G(X)=sum_e d_e(X) Q_e.                           (3.3)

Indeed, if b_v=-sum_(e on root->v) d_e, then
G_v=b_v-D^(-1)sum_w b_w. Applying (3.2) yields

    G(delta C)=C_diag-(Tr C/D)I.                    (3.4)

For this comb, a horizontal edge (R,S)->(R,S+1) has subtree
{(R,U):U>S}, so n_e=N-1-S. A vertical trunk edge
(R,0)->(R+1,0) has every row T>R as its subtree, so
n_e=N(r-R). Thus (3.3) is a fully specified finite formula.

## 4. The actual Ward complex has a strong whole contraction

Define

    delta C=([K,C],[H,C],[F,C],[L,C]),
    p(C)=Tr C/D, i(c)=cI, h(X)=O(X)+G(X).            (4.1)

Equations (2.2) and (3.4) prove the exact WHOLE identity

    h delta=I-i p, p h=0, delta i=0, p i=1.         (4.2)

In particular the common Ward kernel is precisely the scalar line,
without invoking Schur irreducibility. Define the degree-one term
of the Ward complex to be the ACTUAL image

    W^0=End(D_m), W^1=im(delta).

Then delta h=I on W^1, so (i,p,h) is a strong contraction onto
the scalar line in degree zero. The image is a direct summand of
the unrestricted four-row space, since delta h is its explicit
idempotent projector. No claim is made that the unrestricted
codomain End(D_m)^4 has zero cokernel.

Every map is rational and regular at q_N. The same identities
hold after arbitrary finite normal truncation or formal completion,
with all Leibniz convolutions retained. Unlike inversion of a
root memory-Cartan gap, (4.2) is not obtained by inverting delta.

## 5. The original cut is attached by its exact source row

Let Phi_A(C)=Tr(A(q)C) be ANY specified whole actual cut coupon.
Put rho(q)=Phi_A(I)=Tr A. Applying it to (4.2) gives

    Phi_A-rho p=b_A delta, b_A(X)=Phi_A(h(X)).        (5.1)

This retains the original source, dual and every normalization
unit exactly. For an actually normalized coupon, rho=1; if its
raw source uses a normalization unit, that unit is retained in A,
not inferred from its root value. In entries the degree-one row is

    b_A(X)=sum_(S!=U,R,T) A_(T,U;R,S) (X_K)_(R,S;T,U)
                                   /(k_(R,S)-k_(T,U))
          +sum_(R!=T,S) A_(T,S;R,S) (X_H)_(R,S;T,S)
                                   /(h_(R,S)-h_(T,S))
          +sum_e Tr(A Q_e) d_e(X).                  (5.2)

In particular this applies to the original correlated coupon e_D,
whose root source is the literal selected sum over
(R,S)=(R,R mod N) and whose row has coefficients
2^(-N) binom(N,R), for r=N. The diagonal alias at R=0,N and its
old endpoint normalization remain part of A. The root wall has
original value 2^(-N), not the uniform interval value 1/(N+1).
Equation (5.1) makes their difference an ACTUAL Ward boundary
using H, rather than incorrectly declaring it a boundary in the
smaller resonant memory-Borel complex.

The original root row can be made still more explicit. Write
p_R=2^(-N)binom(N,R), S_R=R mod N. Its only two distinct selected
vertices having the SAME head residue are (0,0) and (N,0).
Therefore its H-row part in (5.2) is exactly

    2^(-N)/(2N) * [(X_H)_(0,0;N,0)
                                      -(X_H)_(N,0;0,0)].      (5.3)

This is the original wall weight, with its original sign, rather
than an interval-average substitute. The diagonal-flow coefficient
Tr(e_D Q_e) is also explicit. On the horizontal edge in row R
after S it is

    (N-1-S)/D-p_R 1_(S_R>S),

and on the vertical trunk edge after R it is

    (N-R)/(N+1)-sum_(T>R)p_T.                     (5.4)

The whole formulas remain (5.1)--(5.2) with the actual supplied
source entries and their normalization units; (5.3)--(5.4) only
display their root values, not a chosen off-root extension.

If the network is expressed in the controlled Fourier/source
frame, conjugate all four actual words, all rows, h, and A by
that same whole matrix. Equation (5.1) is preserved. Conjugating
the coupon alone and keeping the old current operators would be
a different source problem.

The ordinary pivotal cap transports the actual Hopf-adjoint rows
with their full divided coproducts. A commutator row is converted
by [rho(h),C]=sum_(h) D_(h_1)(C)rho(h_2). Thus
[the all-word current/cap formulas](actual_divided_ward_closure_and_green_caps.md)
give an explicit global endpoint for each actual word in (4.1).
For the frozen ADO cap retain its whole adapter
chi^(-1)ptr_K M_(Z^J) and its recorded defect rows. This grid
contraction does not make those Green or cap endpoints zero.

## 6. A polynomial root bound in the actual hybrid metric

Use the root positive metric

    ||w_(R,S)||^2=binom(r,R)

with the ordinary integral head basis orthonormal. Give End the
induced Hilbert--Schmidt norm, and the four-row domain the
orthogonal product norm. This is an explicitly stated root metric,
not a bound on an unretained q-factorial change of basis.

K is unitary at the root. Its inverse-gap norm in (2.1) is
at most 1/[2 sin(pi/N)] <= N/4. The H inverse-gap norm is at most
1/2. The two off-diagonal pieces occupy disjoint supports.

For a horizontal tree edge the metric-normalized actual arrow has
size [S+1]_(q_N)>=1. For a vertical edge its size is
sqrt((R+1)(r-R))>=sqrt(r)>=1. Hence the Euclidean norm of the
selected gradient vector is bounded by the combined Hilbert--Schmidt
norms of X_F and X_L.

Before centering, the root-path integration matrix has one entry
-1 for each edge on a vertex path. Its squared Frobenius norm is

    sum_(R=0)^r sum_(S=0)^(N-1)(R+S)
                         =D(r+N-1)/2.

Centering is an orthogonal projection. Since the off-diagonal
and diagonal outputs are orthogonal, this gives, for example,

    ||h_0|| <= max(1/[2 sin(pi/N)], 1/2,
                                      sqrt(D(r+N-1)/2)).        (6.1)

For r=N the bound is O(N^(3/2)). It is uniform in the word length
because h is a cut contraction, not a product of crossing norms.
There is no claim of an N-independent complex neighborhood on
which every whole rational unit has this root bound.

The original root correlated coupon e_D is an orthogonal rank-one
projector in this hybrid metric: its selected source has squared
norm sum_R binom(N,R)=2^N, and its original dual is that metric
dual divided by 2^N. Consequently its functional norm is one.
Equation (5.1) therefore gives

    ||b_(e_D),0|| <= ||h_0||,                       (6.2)

a polynomial source-homotopy bound, INCLUDING the old memory wall.
The full external modified-dimension line multiplies both sides
and is never suppressed. A source comparison through some other
nonunitary whole gauge requires its own norm adapter; the present
bound concerns the specified actual hybrid frame. The original
controlled root head-shift/Fourier matrix with its literal 1/N
normalization is a scalar N^(-1/2) times a unitary map. Its
conjugation is therefore isometric, so simultaneous transport of
operators, current maps and coupon preserves this bound.

## 7. Two actual words suffice, with an explicit row correction

There is also a shorter whole presentation. Put

    A=H+K/2, B=F+L.

At the root A has simple full-grid spectrum. If R!=T then
|Delta H+Delta K/2|>=2|R-T|-1>=1. If R=T and S!=U the gap is
|Q_N^(-S)-Q_N^(-U)|/2>=sin(pi/N). Hence every off-diagonal A
gap is a whole unit. Recover C_off entrywise from [A,C].
Next subtract

    Z=[B,C]-[B,C_off]=[B,C_diag].

The N-step and one-step arrows in B occupy distinct positions
for N>=2. Read the same comb-edge gradients from Z and apply
(3.3). This gives an explicit two-row contraction with the SAME
scalar trace projection. Its off-diagonal subtraction is essential;
simply reading a tree edge of [B,C] can include other entries of C.
The four-row form has the cleaner bound and source formulas above.

Both presentations use actual integral U_q words. They supply a
whole finite Ward target and its original co-source homotopy; a
nonzero map from the sourced geometric current complex into this
target is still the necessary geometric comparison.

Exact audits: [script](../experiments/audit_whole_high_color_ward_grid.py)
and [results](../experiments/whole_high_color_ward_grid_results.json).
The proof has a separate
[independent audit](high_color_wall_source_independent_audit.md).
