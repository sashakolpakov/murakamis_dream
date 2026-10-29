# A cyclotomic diagonal source and an actual endpoint-completed wall ladder

Research proof, 27 October 2026. The degree-N binomial wall row can be
coupled to the original head index by an intrinsic cyclotomic projector
in an actual high integral color. Actual divided powers, together with
their first-normal wrap entries, give an exact classical SL2 action on
the resulting N+1-state string. The coupling is a controlled cyclic
head-shift gauge, rather than an unspecified Kronecker insertion.

This supplies an exact finite source/current realization. It does not
make the projector commute with the original whole crossing. A literal
first-normal charged crossing entry below proves that this stronger
assertion fails. Whole gauge transport is exact if all crossings,
pivots, sources and internal projectors are transported together.

## 1. Actual color, clocks and the diagonal constraint

Use the integral color and constant sign basis of
[the high-color source theorem](high_integral_color_frobenius_wall_source.md)
with r=N. Its dimension is N(N+1), and its basis is w_(R,S),
0<=R<=N, 0<=S<N. Put q=q_N, Q=q_N^2, rho=q_N-q_N^(-1),
delta=1-q^(2N), and let the head index and block index denote the
literal diagonal matrices S and R in this fixed basis. They are actual
color observables: the unwrapped index is J_un=NR+S, while Q^J_un=Q^S
at the root. The distinct root eigenvalues determine S by spectral
interpolation; then R=(J_un-S)/N.

The cyclotomic charge and its zero projector are

\[
 C=Q^{R-S},\qquad
 P=\frac1N\sum_{\ell=0}^{N-1}C^\ell.                 \tag{1}
\]

The root geometric-series identity proves, on each basis vector,
that P selects exactly

\[
 z_j=w_{j,j}\quad(0\le j<N),\qquad z_N=w_{N,0}.        \tag{2}
\]

In particular this is an orthogonal rank-(N+1) projector in the
constant sign basis. P, R and S have unambiguous constant matrix
extensions in the original integral q-family. This extension makes
no claim that their generic-q extensions are quantum intertwiners.

## 2. The wall row, including its endpoint and normalization

Write e_+=psi_+ lambda_+ for the actual Frobenius coherent coupon,

\[
 \psi_+=\sum_{R=0}^{N}v_R,\qquad
 \lambda_+(v_R)=2^{-N}{N\choose R},\qquad
 \lambda_+\psi_+=1.
\]

The original head average is the rank-one coupon
e_h=psi_h phi_h, where psi_h=sum_S v_S and phi_h(v_S)=1/N.
Let e_prod=e_+ tensor e_h. This is the actual divided-coherent
Frobenius source times the original head source; its Frobenius dual
is binomial, and is not silently identified with a uniform average
over the entire high color. Then

\[
 \operatorname{Tr}(e_{\rm prod}P)=\frac1N,\qquad
 e_D=NP e_{\rm prod}P                              \tag{3}
\]

is an idempotent of trace one. Its source and co-source on (2) are
exactly sum_j z_j and sum_j 2^(-N) binom(N,j) z_j^*.

For any array J_0,...,J_N over a commutative coefficient algebra, use
the actual diagonal insertion

\[
 \mathcal J=J(S)+(J_N-J_0)P_{R=N},                    \tag{4}
\]

where J(S) has entries J_0,...,J_(N-1). Its restriction to (2) is
diag(J_0,...,J_N). Consequently

\[
 \frac1N\operatorname{Tr}(e_D\mathcal J)
 =\operatorname{Tr}(e_{\rm prod}P\mathcal J)
 =\frac1{N2^N}\sum_{j=0}^{N}{N\choose j}J_j
 =B_N(J).                                          \tag{5}
\]

This is the wall row from
[the actual Gauss-wall current complex](actual_gauss_wall_cut_current_complex.md),
with both its 1/N and its j=N endpoint. It applies coefficientwise to
the original retained logarithmic/polynomial Green arrays. It is not
a pointwise multiplication of coherent symbols.

In that current complex the original arrays already contain 1/N:
I_mat=N I_raw and J_mat=N J_raw. Thus (5) applies to J_mat; its raw
version is N B_N(J_raw). This factor cannot be silently absorbed.

The normalized source Tr(e_D C) returns the actual high-color knot
scalar when C is its scalar long-knot operator. At the root this is
the original K_N by the already proved all-color periodicity. The
unnormalized wall source returns K_N/N. The old marked ADO/peripheral
line and its full twists are retained; this construction does not
replace them by a fictitious high-level normalization.

There is no exponential source cost at the root. Directly,

\[
 \|\psi_D\|=\sqrt{N+1},\qquad
 \|\lambda_D\|^2=4^{-N}{2N\choose N}\le1,
 \qquad\|e_D\|\le\sqrt{N+1}.                          \tag{6}
\]

The same bound holds for its trace-functional norm. This is a root
bound, not a bound on a growing normal neighborhood or on arbitrary
quantum derivatives.

This bound uses the constant coordinate metric. The
[current/metric audit](frobenius_clock_and_internal_centralizer_map.md)
also proves a polynomial bound for THIS selected anchor in the
explicit tensor coherent metric, by exact binomial cancellation.
It separately proves that the full controlled gauge, and other
points of its real coherent orbit, can be exponentially conditioned
in that metric. Thus (6) is not a uniform bound for an arbitrary
period-line comparison or the whole coherent source family.

## 3. An exact SL2 ladder made from actual divided and normal entries

Let e,f,h be the classical multiplicity matrices of the actual
divided-power theorem, with

\[
 ev_R=(N-R+1)v_{R-1},\quad
 fv_R=(R+1)v_{R+1},\quad hv_R=(N-2R)v_R.
\]

Let V be the cyclic head shift S -> S+1 modulo N. Define the actual
head spectral pseudoinverse

\[
 D^\dagger=\operatorname{diag}(0,[1]^{-1},\ldots,[N-1]^{-1}).
\]

Every displayed denominator is nonzero at the marked root. Integral
divided multiplication and [N+1]_(q_N)=-1 give

\[
 E^{(N+1)}=e\otimes E_{\rm St},\qquad
 F^{(N+1)}=-f\otimes F_{\rm St}.                      \tag{7}
\]

Indeed E^(N)=(-1)^(N-1)e and ordinary E=(-1)^N E_St,
and E^(N)E=[N+1]E^(N+1); the F identity is identical without
the two E signs. The literal first-normal wrap matrices are

\[
 [E_{\rm cross}/\delta]_0
   =(-1)^{N+1}\rho^{-1}e\otimes E_{N-1,0},\qquad
 [F_{\rm cross}/\delta]_0
   =\rho^{-1}f\otimes E_{0,N-1}.                     \tag{8}
\]

Both are regular divisions in the original q-family, not divisions
of zero root matrices. Combining (7) and (8) with the specified
operator orders gives

\[
 \begin{split}
 \widetilde E
 &=E^{(N+1)}(I\otimes D^\dagger)
      +\rho(-1)^{N+1}[E_{\rm cross}/\delta]_0
   =e\otimes V^{-1},\\
 \widetilde F
 &=-(I\otimes D^\dagger)F^{(N+1)}
      +\rho[F_{\rm cross}/\delta]_0
   =f\otimes V,\\
 \widetilde H&=h\otimes I.
 \end{split}                                                   \tag{9}
\]

For example E_St D^dagger is the noncyclic unit backward shift;
the first term misses only S=0, which (8) completes. For F the
pseudoinverse acts on the OUTPUT, exactly as printed. Thus
[Etilde,Ftilde]=Htilde and the other two SL2 relations hold on the
WHOLE actual high-color vector space. All three commute with P.
On its selected string they act as

\[
 \widetilde E z_j=(N-j+1)z_{j-1},\qquad
 \widetilde F z_j=(j+1)z_{j+1}.                       \tag{10}
\]

The missing last bulk link is supplied by the actual normal edges:
F_cross/delta sends z_(N-1) to (N/rho)z_N, and E_cross/delta sends
z_N to ((-1)^(N+1)/rho)z_(N-1). Equations (9)--(10), rather than a
postulated auxiliary representation, therefore realize the entire
N+1 wall-current string. Dividing the nonzero coefficients in (10)
also gives the literal unit forward and backward current shifts,
with their two endpoint projectors retained.

## 4. The coupling is an exact controlled-shift gauge

Define the constant unitary permutation

\[
 G=\sum_{R=0}^{N}P_R\otimes V^R.
\]

Direct multiplication proves the simultaneous identities

\[
 \begin{split}
 G(e\otimes I)G^{-1}&=\widetilde E,&
 G(f\otimes I)G^{-1}&=\widetilde F,\\
 G(I\otimes P_0)G^{-1}&=P,&
 G(e_+\otimes P_0)G^{-1}&=e_D,\\
 GQ^SG^{-1}&=Q^{-R}Q^S,&GQ^RG^{-1}&=Q^R.
 \end{split}                                                   \tag{11}
\]

Thus this is also an explicit finite clock shear: the
head clock becomes the inverse of the cyclotomic constraint charge.
No classical geometric Egorov identification is inferred from (11).

The root Fourier matrix with entries Q^(ST)/N sends psi_h to v_0
and phi_h to v_0^* under the inverse dual map. It maps e_h to P_0.
It is a scalar multiple of a unitary matrix and has condition number
one. Consequently H_0=G(I tensor Fourier) conjugates the divided-coherent product
rank-one source exactly to e_D, including its off-diagonal entries.
If every crossing is replaced by

\[
 R^{H_0}=(H_0\otimes H_0)R_{\rm high}(H_0^{-1}\otimes H_0^{-1}),
                                                               \tag{12}
\]

and pivots, duals, coupons and internal projectors are conjugated
with their endpoint H_0's, the full arbitrary word and all its q-jets
are exactly gauge equivalent. This is ordinary finite matrix basis
change in the actual integral family. It makes no assertion that
P commutes with the original R, or that R^H already has the required
geometric Gaussian/source comparison.

## 5. Literal whole source germs and an off-diagonal Ward adapter

The generic integral divided matrices determine finite source germs
Psi_S(q), Lambda_S(q), u_S(q)=Lambda_S Psi_S exactly as in the
high-color source theorem; u_S(q_N)=1. Put

\[
 \Psi=\sum_S\Psi_S,\qquad
 \Lambda=\frac1N\sum_S\Lambda_S/u_S,\qquad
 e(q)=\Psi\Lambda,\qquad u_P(q)=\Lambda P\Psi.
\]

The distinct residue strings are disjoint, so Lambda Psi=1.
Moreover u_P(q_N)=1/N. Thus the two WHOLE idempotent germs

\[
 a(q)=e(q)P/u_P(q),\qquad
 d(q)=Pe(q)P/u_P(q)                                  \tag{13}
\]

are regular and have trace one. At the root d=e_D. On the actual
generic scalar high-color long-knot operator, both return its exact
scalar, with no discarded quantum jet. This comparison is with the
SAME high color, not an off-root equality with the original color N.

Their off-diagonal difference is an explicit Cartan Ward boundary.
Set Delta=a-d and, in the original unwrapped position basis, define

\[
 B_{ij}=\frac{\Delta_{ij}}{i-j}\ (i\ne j),\qquad B_{ii}=0.
\]

The diagonal of Delta is identically zero, at every q in the germ.
Consequently

\[
 \Delta=[J_{\rm un},B],\qquad
 \operatorname{Tr}(\Delta C)=-\operatorname{Tr}(B[J_{\rm un},C])
                                                               \tag{14}
\]

for EVERY matrix C. Hence the one-sided projected product source
and the compressed source agree on weight-zero actual cut arrays,
while their full off-diagonal Ward discrepancy has not been erased.

The alternative whole germ G e_0(q) G^(-1), obtained by transporting
one original residue-string coupon, has the same root as d(q).
Its higher diagonal source weights generally differ: d samples the
actual S=R mod N string, while G e_0 G^(-1) samples S=0 before
transport. Their source and co-source ratios are regular units with
root one. Those units and u_P must be carried when comparing whole
jets; equality of their numerical root binomial rows does not remove
them.

These source units can also be retained by an EXPLICIT whole-germ
gauge, rather than an unspecified choice of extension. Write v=Psi,
w=Lambda, v_c=Pv and w_c=wP/u_P. Thus wv=w_c v_c=1 and
d=v_c w_c. Put v_t=H_0v, w_t=wH_0^(-1), e_t=v_t w_t and

\[
 K(q)=v_cw_t+(I-d)(I-e_t).                            \tag{14a}
\]

The Fourier normalization specified in Section 4 gives v_t(q_N)=v_c(q_N)
and w_t(q_N)=w_c(q_N), so K(q_N)=I. It is therefore a regular
invertible matrix germ. Direct multiplication, using the four source
normalizations, proves

\[
 Kv_t=v_c,\qquad w_cK=w_t,\qquad
 K e_tK^{-1}=d.                                     \tag{14b}
\]

Consequently H(q)=K(q)H_0 transports that actual divided-coherent whole source
to the compressed source exactly. Conjugating every crossing, pivot,
dual, coupon and internal projector by H(q) gives an exact whole-word
source comparison, including all source-normal derivatives and the
unit u_P. This is a same-color gauge theorem. It neither equates the
high and original low-color q-jets nor establishes the geometric
Gaussian image of the transformed word. Only H(q_N), not its behavior
on a growing q-neighborhood, has the polynomial cost established above.

There is also an explicit adapter if the incoming high-color coupon
is the uniform average in this fixed basis. On the Frobenius factor
put lambda_av(v_R)=1/(N+1), and write lambda_bin=lambda_+. Then

\[
 K_{\rm Fr}=I+\psi_+(\lambda_{\rm av}-\lambda_{\rm bin}),\qquad
 K_{\rm Fr}^{-1}=I-\psi_+(\lambda_{\rm av}-\lambda_{\rm bin}).
                                                               \tag{14c}
\]

The rank-one correction squares to zero, since both rows pair with
psi_+ to one. It fixes the source vector and sends the uniform
coupon to the binomial coupon by conjugation. Both K_Fr and its
inverse have norm O(sqrt(N+1)). Tensoring with the head identity and
using the same near-identity construction (14a) joins the constant
uniform source to the actual divided-coherent WHOLE germ. Composing
it with H(q) therefore retains the precise incoming source, including
all its normal jets. If a different integral/balanced basis is used,
its actual source adapter must first be included; (14c) is not a
license to replace its off-diagonal row by an average. All these
conjugations compare the high color with itself.

## 6. An actual mixed-normal crossing changes the total charge

The entire root crossing commutes with the TOTAL charge C tensor C,
although it need not preserve the individual zero-charge projectors.
The original first-normal crossing need not even preserve total
zero charge. Here is an explicit entry of the actual positive R.

Take input (R_1,S_1)=(1,0), (R_2,S_2)=(N-1,0), and transfer k=1.
Its total root charge is zero. The un-checked output is
(0,N-1),(N-1,1), whose total charge is -1 modulo N. The transfer
coefficient has exactly one normal zero, and

\[
 [R_{\rm entry}/\delta]_0
   =(-1)^{N+1}N\,
       q_N^{H_{N-1}H_{N(N-1)+1}/2}\ne0,              \tag{15}
\]

where H_i=m-2i and the common half-Cartan character is exactly the
one in the original R. This follows directly from the E wrap
coefficient (-1)^(N+1)N/rho, the nonzero F head coefficient [1]=1,
and the k=1 nilpotent coefficient rho. Checked R only swaps its
output factors and has the same total charge defect. Thus deleting
all charged neighbors at first normal order changes an actual
crossing coefficient. A full-source current theorem cannot silently
apply P before and after each original crossing.

There is nevertheless an exact bounded-charge filtration. For any
transfer k=aN+b, 0<=b<N, write the two possible head carries as
c_E=1_(S_1<b) and c_F=1_(S_2+b>=N). Then

\[
 \Delta(R_1+R_2)=c_F-c_E\in\{-1,0,1\},\qquad
 \Delta(S_1+S_2)=-N(c_F-c_E).                         \tag{16}
\]

The total charge change modulo N is therefore c_F-c_E. More precisely
the E^k path has a+c_E simple block zeros, the F^k path has a+c_F,
and the denominator [k]! has a. Thus a nonzero entry has exact
delta-order a+c_E+c_F. In particular every nonzero charge change
costs at least one normal order; this conclusion retains the
denominator zeros rather than counting only numerator edges.
A product of actual crossing
jets of total normal order B can consequently move the total charge
by at most B. The same follows for inverse crossings from the exact
inverse series, since the root crossing and its inverse have charge
zero. For N>2B these neighbors have distinct residue labels.
Diagonal pivots do not change this conclusion. This is a support
statement for actual braid-word jets, not a claim that their
zero-charge component or boundary cohomology vanishes.

The resonant tail E^(N) tensor F^(N) has zero total charge. It does
not cancel the mixed charged entry (15). The actual quadratic
Frobenius-degree theorem in
[the first-normal crossing note](high_color_first_normal_r_and_frobenius_degree.md)
is compatible with this filtration and retains precisely these
mixed terms.

## 7. Exact scope and audit

We have constructed the wall-row source on an intrinsic constrained
subspace of an actual color, its exact endpoint-completed ladder,
its full finite gauge transport, and its literal whole source germ.
Equation (14) keeps the off-diagonal source-current correction.
Equation (15) isolates why the source projector alone is not a
whole-network intertwiner. The missing step is to transport the
actual two framing currents through the resulting charged/source
complex into the geometric Gaussian/relative complex, with the
peripheral endpoint class retained. Neither the normalized source
nor the finite SL2 string alone supplies that map.

[The audit](../experiments/audit_cyclotomic_diagonal_wall_current_source.py)
checks actual integral divided entries and actual first-normal wrap
entries independently, the exact source and gauge identities,
Cartan boundary (14), wall endpoints, and actual charged crossing
entry (15). Its checks are exact finite-field identities, not a
topological or asymptotic inference.

The saved [results](../experiments/cyclotomic_diagonal_wall_current_source_results.json)
pass seven actual colors N=2,...,8 and four full actual crossing
families N=2,...,5. They include 1708 nonzero charged first-normal
entries. Those entries support, rather than remove, the retained
charged-sector obstruction.
