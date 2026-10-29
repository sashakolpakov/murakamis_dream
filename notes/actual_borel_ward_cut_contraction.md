# A literal Borel Ward contraction for the actual finite cut

Research construction, 27 October 2026. This derives an explicit split
Ward complex and its cut functional from the actual root matrices.
It identifies exactly what unknot normalization fixes. It does not
yet map the partially summed geometric Gaussian block into that
complex or prove a selected global geometric contribution.

## 1. The two actual matrices already determine the scalar Ward kernel

Fix N>=2, Q primitive of order N, x=-M/q!=0. In the original
balanced basis w_a=v_a/(Q;Q)_a, 0<=a<N, the actual generators are

    K_aa=k_a=x Q^(-a),
    F_(a+1,a)=f_a=1-Q^(a+1), 0<=a<N-1,

with all other F entries zero. Distinct k_a and nonzero f_a are
units at every M!=0, including the complete value M=1. No E
coefficient is inverted, so no color-reducibility wall is removed.

For C in End(V) put

    delta(C)=([K,C],[F,C]),
    p(C)=Tr(C)/N, i(c)=c I.                         (1.1)

Define two explicit maps on a pair (X,Z) of matrices. Let H_K(X)
have zero diagonal and off-diagonal entries

    H_K(X)_(a,b)=X_(a,b)/(k_a-k_b), a!=b.

Put d_r=Z_(r+1,r)/f_r and define the diagonal matrix

    H_F(Z)_aa=(1/N)sum_(r=0)^(N-2)(N-1-r)d_r
                                -sum_(r<a)d_r.    (1.2)

Then, for every matrix C,

    C=i p(C)+H_K([K,C])+H_F([F,C]).               (1.3)

For the off-diagonal entries this is immediate. On the diagonal,
[F,C]_(r+1,r)/f_r=C_rr-C_(r+1,r+1); cumulative summation gives
the diagonal minus its average, proving (1.3).

In particular ker delta=k I. Define the actual Ward complex to be

    W^0=End(V) --delta--> W^1=im(delta).

The map h(X,Z)=H_K(X)+H_F(Z) satisfies

    h delta=I-i p, delta h=I on W^1,
    p h=0, h delta i=0.                          (1.4)

Thus it is an explicit strong contraction onto k I in degree zero.
There is no claim that the unrestricted codomain End(V)^2 has
vanishing higher cokernel; W^1 is the actual image subspace.

These are matrix identities, independent of any irreducibility,
semisimplicity, Haar integration, or modified-trace existence theorem.

## 2. The original marked cut is cohomologous to the normalized scalar row

In this same balanced basis the prescribed source and co-source
are psi=(1,...,1)^t and phi=(1/N)(1,...,1). Hence

    e=psi phi, e_(a,b)=1/N, Phi(C)=Tr(e C).

The original pivot is g=K^(1-N), and its marked defect is
D=g^(-1)e; thus the actual expression is Phi(C)=Tr(g D C).
Neither the pivot nor the full external modified-dimension line
d_N(M) is dropped.

There is an explicit matrix B_cut, with zero diagonal, such that

    (B_cut)_(a,b)=1/[N(k_a-k_b)], a!=b,
    [K,B_cut]=e-I/N.                              (2.1)

Consequently, for every C,

    Phi(C)-p(C)=-Tr(B_cut[K,C]).                  (2.2)

Thus the degree-one row b(X,Z)=-Tr(B_cut X) is an exact cochain
homotopy Phi-p=b delta on the Ward complex. In particular the
original rank-one cut and the scalar normalized trace agree
exactly on Ward-closed matrices. Their common value on I is one.
This is the literal unknot normalization, rather than a comparison
of two quantities that only have the same norm.

The pivot's ordinary trace is still zero; (2.2) does not replace
the marked defect D by an ordinary pivotal closure. At the root
D^2=0, gD=e and DgD=D, as in
[the actual relative source](relative_framing_source_transgression.md).
The equality of cut rows is an equality on the Ward complex,
with the defect retained.

## 3. The actual closed tangle is Ward closed

The prescribed R matrices intertwine the actual coproduct, and
the cups and pivotal caps are the explicit Hopf maps already
checked in [the duality calculation](relative_pivotal_duality.md).
Composing these identities around the closed strands shows that
the original (1,1)-tangle endomorphism C commutes with K and F.
It therefore lies in ker delta and equals p(C)I by (1.3).

This proves the finite scalar/cut conclusion directly from the
actual matrices. It also gives an exact target for any proposed
framing reduction: a map of actual partial-source complexes into
W, with the cut row (2.2) and its homotopy transported, would
reduce that framing problem to its scalar Ward class.

The global intertwining identity alone does not construct such a
map for a partially summed array. A remaining external internal
index is not an open-tangle matrix index. Moving F through the
unsummed network generally produces currents in those remaining
flow coordinates. Their exact finite boundary, canonical carries
and normal source must be retained to identify its complex with W.

## 4. Actual coproduct symbols and the two cut-framing currents

There is a direct principal-symbol comparison, using the already
proved actual moment-map identity. On the tensor product put

    K_tot=Delta^(b-1)K, Ecal_tot=rho^2 Delta^(b-1)E,
    F_tot=Delta^(b-1)F, rho=q-q^(-1).

In balanced wave coordinates A=Q^a and S f(A)=f(QA), their local
input matrices have symbols

    K=x/A, e=(1-x^2/A)p/x, f=(1-A)/p.

The actual finite Ecal is the truncated matrix, including its
rank-one endpoint subtraction; only its interior symbol is used
in this display. The actual coproducts are

    Delta K=K tensor K,
    Delta Ecal=Ecal tensor K+1 tensor Ecal,
    Delta F=F tensor 1+K^(-1) tensor F.

Writing the classical prefix product as P=[a b;c d], its exact
Gauss factorization gives

    symbol(K_tot)=a, symbol(Ecal_tot)=b,
    symbol(F_tot)=c/a.                            (4.1)

Indeed the upper triangular products multiply their off-diagonal
entries by E_1K_2+E_2, while the lower triangular product gives
F_1+K_1^(-1)F_2. Taking B_-^(-1)B_+ gives P with precisely
the three entries in (4.1).

For simultaneous conjugation A xi and the actual symplectic form,
[the uniform moment-map calculation](quantum_source_bridge_extension.md)
proves

    iota_(A xi) Omega=(2u da+v dc+w db)/a,
    xi=u h+v e_sl+w f_sl,

where h=diag(1,-1), e_sl=E_12, f_sl=E_21. With the convention
iota_(X_H)Omega=dH, equation (4.1) therefore yields

    X_logK=A(h/2),
    X_F=A(e_sl-(c/(2a))h),
    X_Ecal=A(a f_sl).                            (4.2)

The cut stabilizer is ker ell, ell(h,e_sl,f_sl)=(2,1,-1).
Thus K,F alone describe a different Borel. Its actual cut basis
h+2f_sl, e_sl+f_sl is instead obtained from

    A(h+2f_sl)=(2/a)(X_K+X_Ecal),
    A(e_sl+f_sl)=X_F+(c/a^2)X_K+(1/a)X_Ecal.     (4.3)

These relations also give literal quantum Ward identities with
a specified operator order. For any full tensor endomorphism J
commuting with the actual coproduct generators, both

    W_1(J)=2 K_tot^(-1)([K_tot,J]+[Ecal_tot,J]),
    W_2(J)=[F_tot,J]+F_tot K_tot^(-1)[K_tot,J]
                              +K_tot^(-1)[Ecal_tot,J]          (4.4)

vanish exactly. Their first commutator symbols divided by H=Log Q
give the two vector fields in (4.3). No quantum Log K is needed.
The coefficients in (4.4) multiply on the left; interchanging their
order introduces genuine additional quantum terms.

Equations (4.3)--(4.4) identify the principal cut-framing currents,
but are not by themselves a quantum representation of the cut Borel
Lie algebra. The Hopf-adjoint presentation below removes their
variable-coefficient ambiguity at the finite matrix level.

### The Hopf adjoint gives constant conjugation fields

For h in the actual quantum group define its actual action on matrices
by ad_h(C)=sum rho(h_1) C rho(S h_2). The displayed coproduct and
antipode formulas give, exactly,

    (ad_K-I)(C)=[K,C]K^(-1),
    ad_Ecal(C)=[Ecal,C]K^(-1),
    ad_F(C)=[F,C]+K^(-1)[K,C]F.                  (4.5)

In the tensor formulas K,Ecal,F are their actual total coproducts.
The first commutator symbols divided by H are therefore

    (ad_K-I)/H -> A(h/2),
    ad_Ecal/H -> A f_sl,
    ad_F/H -> A e_sl.                            (4.6)

For F, the extra term contributes (c/a)X_logK, canceling the
h component in (4.2). Thus

    2(ad_K-I)+2ad_Ecal,
    ad_F+ad_Ecal                                (4.7)

are literal quantum Ward operators with principal fields
A(h+2f_sl), A(e_sl+f_sl). They use the actual truncated E,
including its endpoint, and no logarithm of K. The conventional
opposite sign of fundamental conjugation vector-field brackets
agrees with the Ecal-to-f_sl and F-to-e_sl correspondence.
No exact two-generator Lie or coideal presentation is being
inferred solely from these first symbols.

The K,F Hopf Ward rows and the rows in (1.1) are related by an
invertible exact row operation:

    X_H=X K^(-1), Z_H=Z+K^(-1)X F,
    X=X_H K, Z=Z_H-K^(-1)X_H K F.               (4.8)

Hence (1.4) transfers to the Hopf Ward complex by substituting
the second line of (4.8) into h. Its cut homotopy is

    Phi-p=-Tr(K B_cut (ad_K-I)(C)),             (4.9)

with B_cut from (2.1). This is an actual cochain row transformation.

### Pivotal partial trace is an exact Hopf-adjoint chain map

For two actual modules V,W let

    ptr_W(C)=Tr_W((I tensor g_W)C),
    g_W=K_W^(1-N).

Then for every matrix C, not only for invariant intertwiners,

    ptr_W(ad_h C)=ad_h(ptr_W C).                 (4.10)

One exact proof identifies End(V tensor W) with
V tensor W tensor W* tensor V* and contracts W tensor W* by the
actual right pivotal cap w tensor phi |-> phi(g_W w). This cap
is a Hopf map by the checked antipode identities. The resulting
contraction is literally the displayed weighted partial trace.

There is also a generator check with no categorical premise.
For K, cyclicity of the W trace and commutation of g_W with K_W
give the assertion. For Ecal, expand

    [Ecal_V K_W+Ecal_W,C] * (K_V K_W)^(-1).

The V terms give the
right side, and the two W terms cancel because K_W^(-1)g_W
is central. For F, expand the third formula of (4.5) for
F_tot=F_V+K_V^(-1)F_W. Again the V terms give the right side;
the W terms cancel by

    K_W F_W g_W K_W^(-1)=g_W F_W,

which follows from the same centrality. The generator identities
extend by composition to every h. Iterating gives every original
pivotal closed-strand contraction.

Thus the degree-zero map ptr and its rowwise degree-one map
give an exact map from the full finite tensor Hopf-Ward complex
(using its actual image as degree one) to the cut Hopf-Ward
complex. The scalar contraction and the actual cut homotopy are
now attached to that finite diagram.

This does not yet identify scalar partial Gaussian elimination
with that operator-valued diagram. It must transport the E endpoint,
the diagonal K poles, cumulative F carries, and the chosen normal
source. A remaining flow index is not automatically an open
matrix index. That is the remaining algebraic comparison, rather
than a consequence of Schur scalarity or (4.10).

## 5. Uniform size and regularity of the actual contraction

For the prescribed unit-circle root,

    |Q^(-a)-Q^(-b)|>=4/N for a!=b,
    |1-Q^(r+1)|>=4/N.

These follow from sin(pi/N)>=2/N. With the maximum entry norm,

    ||H_K(X)|| <= N ||X||/(4|x|),
    ||H_F(Z)|| <= N(N-1)||Z||/4.                 (4.1)

The coefficients in (1.2) each have modulus at most one, giving
the second bound. Hence the actual Ward contraction is regular
at M=1 and has polynomial bounds in N on compact meridian sets
away from zero. This estimate does not involve d_N(M); that
separate marked line keeps all its original divisors and jets.

Polynomial control of a projection does not imply that its value
on a given nonzero vector has a nonzero exponential rate. Its
kernel contains many nonzero matrices. The bound is useful only
after the actual source class has been shown to survive the map.

## 6. What this does and does not settle about the geometric block

The partially summed actual family has a nonzero transverse formal
geometric block and an actual bulk operator with geometric support,
as proved in
[the partial support construction](partial_geometric_support_theorem.md).
The remaining two-index framing functional has not thereby been
identified with the contraction (1.4), nor with the sourced
centralizer transgression. That identification requires explicit
Ward currents from the local R coproduct identities after partial
elimination, and a map retaining the chosen source and normal row.

If a nonzero formal geometric class were proved to map into ker
delta as a nonzero endomorphism, then its cut would be nonzero
algebraically: ker delta=k I and Phi(I)=1. This is a precise
reduction of the needed normalization problem, not a proof of that
embedding or its nonzero scalar coefficient.

Ward identities plus unknot normalization alone cannot prove that
coefficient is nonzero for every knot: arbitrary scalar families
C_K=c_K I satisfy both commutator equations, with c_unknot=1 and
c_K=0 allowed elsewhere. The missing source map must supply more
information than the universal commutant calculation. No global
cycle, Stokes, or volume inference is made here.

The [cyclic Ward completion](cyclic_ward_norm_adapter.md) also
computes the missing raising edge, its full Frobenius determinant
character, and a literal quantum-factorial affine source equation.
This retains the complete d_N(M) adapter. It is a further exact
source datum for the missing Gaussian/adjoint comparison, rather
than a replacement for that comparison.

## 7. Subsequent currents and an exact divided-normal realization of the cut

The [literal local R currents](local_r_ward_transfer_currents.md)
now give the unsummed E and F Ward divergence formulas with the full
missing-edge source and inserted moments. Their ordinary closed
wall source cancels exactly, so a locally nonzero wall entry cannot
by itself certify the global geometric contribution.

On the genuine complete integral-color lift there is a different
specified normal operator: the
[true divided Hopf adjoint](divided_adjoint_marked_edge_pairing.md)
J_ad=[(ad_Ecal)^N/(1-Q^N)]_root. For the literal missing edge
W=E_(N-1,0), direct calculation gives

    J_ad(W)=-N sum_(a=0)^(N-2) E_(a,a+1),
    Phi(J_ad(W))=-(N-1).

Therefore the normalized row

    Phi_div(C)=-Phi(J_ad(C W))/(N-1)

has Phi_div(I)=1 and obeys the exact all-matrices homotopy
Phi_div-Phi=(Phi_div-Phi)h delta. It returns the original invariant
on every actual closed tangle. Generic pivotal naturality before
division also gives an explicit full-network realization, with
the ordered insertion T(W_cut tensor I) retained. This supplies
an actual divided-normal cut, rather than a conjectural scalar
normalization.

The [complete-color theorem](complete_color_divided_ward_and_fusion.md)
keeps its q-normal distinct from the fixed-root meridian normal,
and retains the pivot and framing derivatives. Its one-sided
fusion correction is a finite exponential with nilpotence bounded
by tensor length. The opposite divided Ward actions contain an
SL_2 block, so a nilpotent whole gauge group is not asserted.
The Gaussian/source comparison and selected volume norm remain
the additional theorem.

The [subsequent complete-color residual theorem](residual_gaussian_ward_currents.md)
now computes the dual cut rows explicitly and transports their
currents through the actual nondegenerate transverse Gaussian.
Their two compensated framing fields have precisely the source
covariance of Omega_cut, and their formal ideal is the flat line
of that actual Gaussian amplitude. This supplies an all-order
interior formal ideal, while preserving the distinction from the
whole finite relative-source complex. The
[finite-cut source audit](finite_cut_euler_source_obstruction.md)
shows explicitly why such local formal closure alone cannot
prove nonzero selected source survival.

[Exact matrix audit](../experiments/audit_actual_borel_ward_cut_contraction.py).
[Results](../experiments/actual_borel_ward_cut_contraction_results.json).
