# The exact degree-elevation residual and its selected endpoint source

Independent proof and source audit, 27 October 2026. Degree elevation
maps the original head cut-Ward complex into the Fr source and
preserves its original cut. Its missing operator channel has an
explicit incidence polynomial. After the two Borel rows are
contracted, one resonant endpoint remains, and its ACTUAL selected
co-source differs exponentially from the uniform interval row.
One-sided clock moments also have an explicit auxiliary correction.

These formulas identify concrete data to compute in the relative
orbit co-source test. They do not construct the internal geometric
Gaussian map or a selected-volume estimate.

## 1. An explicit polynomial detects exactly the missing channel

Use the actual divided Fr basis v_i of Sym^N and put
\[
 b_D(u,t)=\ell_N(u)D\psi_N(t),\qquad
 \mathfrak o_N(D)(u)=u^N b_D(u,-1/u)
   =\sum_{i,j=0}^N(-1)^j\binom NiD_{ij}u^{N+i-j}.    \tag{1}
\]
This is a polynomial of degree at most 2N. The
[degree-elevation map](degree_elevation_actual_head_ward_map.md)
satisfies
\[
 \ker\mathfrak o_N=\mathcal E_N\operatorname{End}(\mathrm{Sym}^{N-1}).
                                                               \tag{2}
\]
Indeed the symbol numerator of E_N(C) is (1+tu)b_C. Conversely,
vanishing in (1) says that the polynomial b_D is divisible by
the irreducible polynomial 1+tu. The quotient has degree at most
N-1 in each variable, hence is the unique symbol numerator of
an old head matrix. Formula (2) is an EXACT image criterion,
stronger than vanishing of the two extreme corners alone.

Every degree 0,...,2N occurs from a matrix unit, so (1) is
surjective. It realizes the full highest-spin quotient directly:
\[
 \begin{split}
 \mathfrak o_N([e,D])&=\partial_u\mathfrak o_N(D),\\
 \mathfrak o_N([f,D])&=(2Nu-u^2\partial_u)\mathfrak o_N(D),\\
 \mathfrak o_N([h,D])&=(2N-2u\partial_u)\mathfrak o_N(D),\\
 \mathfrak o_N(\operatorname{Ad}_{Q^{-J}}D)
                &=Q^N\mathfrak o_N(D)(u/Q).         \tag{3}
 \end{split}
\]
For example the commutator f acts on the normalized symbol by
(-partial_t-u^2 partial_u); it differentiates 1+tu by -u(1+tu).
Restriction to t=-1/u gives exactly the second line of (3).
The other formulas follow the same way or by matrix units.

For the original whole divided string gauge B_s of the head-Ward
map, use instead
\[
          \mathfrak o_{N,s}(D)=\mathfrak o_N(B_s^{-1}DB_s). \tag{4}
\]
All B_s units and their normal derivatives remain present. A Fr
Green/current matrix can use the old head co-source homotopy
precisely when this polynomial vanishes, or after its nonzero
remainder has been accounted for separately.

## 2. Independent contraction of the quotient current complex

In the quotient write weight m=-N,...,N, let B=ad_f raise weight,
and let A=Ad_K-I, K=Q^-J. The actual two-row complex is
\[
 d_0=(A,B),\qquad
 d_1(X,Y)=(\operatorname{Ad}_K-Q^{-1})Y-Q^{-1}BX.     \tag{5}
\]
It is a complex because Ad_K B=Q^-1 B Ad_K. Put
a_m=Q^-m-1 and Bv_m=b_m v_(m+1). Every b_m for m<N is a
nonzero integer in characteristic zero, hence a unit.
For each m<N the three-term summand is
\[
 R\xrightarrow{(a_m,b_m)}R^2
              \xrightarrow{(-Q^{-1}b_m,Q^{-1}a_m)}R,
\]
which contracts using b_m. This works even when a_m=0, so
the other root resonances at m=0 or -N leave no hidden classes.
The remaining bottom degree-one arrow has coefficient
Q^N-Q^-1, a unit near a primitive N-th root for N>=2, and
contracts as well. What remains is EXACTLY
\[
 R\xrightarrow{Q^{-N}-1}R
                \quad\text{in degrees zero and one}.           \tag{6}
\]
The top generator may be taken to be f^N=N!E_(N,0).
With Z=Q^N and delta=1-Z, its differential is
Q^-N-1=delta/Z. Thus the first-normal Bockstein has coefficient
PLUS ONE in the delta convention, or -N in the Log Q normal.
There is no degree-two quotient homology.

This is the quotient theorem for the specified Fr MEMORY Cartan.
It does not identify it with the original high-color quantum K.
For the old physical clock C_Q=Q^S Z^R, the same endpoint changes
Fr block R by N, so its conjugation character is Z^N instead.
Those whole normal characters must not be interchanged because
their root numerical values happen to coincide.

There is an equally explicit root-cycle classification. A matrix
commuting with the regular nilpotent f is a polynomial in f.
Cartan closure at Q_N removes every power f^j except j=0,N.
Thus every scalar-coefficient root cycle is
\[
                  D=aI+cE_{N,0},\qquad c=D_{N,0}.    \tag{6a}
\]
The old degree-elevation image contributes only the scalar part.
With head coefficients the same statement holds entrywise; the
actual selected head co-source must then be applied as well.

The full quotient construction is recorded in
[the complement Bockstein wall](degree_elevation_complement_bockstein_wall.md).
The unit-fork calculation above is an independent proof audit.

## 3. The original selected endpoint co-source is not the uniform row

The uniform rank-one Fr cut and the selected coherent Fr cut give
\[
 \Phi_{\mathrm{uni}}(E_{N,0})=\frac1{N+1},\qquad
 \Phi_+(E_{N,0})=2^{-N},\qquad
 \Phi_{\mathrm{uni}}(f^N)=\frac{N!}{N+1}.                 \tag{7}
\]
These are literal matrix pairings in the actual divided basis.
Under B_s the frozen uniform row acquires the retained whole
factor B_(N,s)/B_(0,s); transporting the row itself compensates
it exactly. The root factor is one, but its normal coefficients
cannot be erased.

E_(N,0) is Ward-closed at the root: it commutes with f, and
its K conjugation character is Q^-N=1. Therefore the difference
of the two co-sources in (7) is NOT Ward-exact on the full Fr
target. Their ratio 2^N/(N+1) cannot be inferred to be a harmless
algebraic normalization. The head-map homotopy applies on the
image (2), where both extreme corners vanish; it does not extend
to this additional endpoint class without its retained source.
An exact source gauge can still compare the two descriptions by
conjugating ALL currents and the endpoint generator too. It does
not justify freezing that generator while replacing its co-source.
In the coordinates (6a), the two root periods are respectively
a+c/(N+1) and a+2^-N c.

This source character is visible as a whole function, not just
as a list of matrix values. For the actual paired Borel coupon
e_(alpha,m)=psi_alpha lambda_m,
\[
 \mathfrak o_N(e_{\alpha,m})(u)
   =\left[(1+u)\frac{(1+m)u-(1-m)}2\right]^N,
 \qquad\Phi_m(E_{N,0})=((1-m)/2)^N.                 \tag{8}
\]
The normalized scale alpha cancels; its UNNORMALIZED power line
alpha^N must still be retained in the original source object.
At the selected m=0 the first polynomial is 2^-N(u^2-1)^N.
The actual interval average over m=-1,...,1 instead integrates
the second character to 1/(N+1). This explains both agreement
on closed scalar cuts and disagreement on the new endpoint.
The whole retained-weight interval comparison in
[the global Cech source](global_frobenius_cech_source_and_endpoints.md)
keeps its density; it does not assert that these two endpoint
co-sources are equal or Ward-homotopic on the entire target.

There is a head-matrix version for the actual coupled coupon e_D.
Write s(i)=i for i<N and s(N)=0. Its Fr blocks are
\[
           (e_D)_{ij}=2^{-N}\binom Nj E_{s(i),s(j)}.
\]
Consequently
\[
 \mathfrak o_N(e_D)(u)=2^{-N}u^N a(u)b(u)^t,          \tag{9}
\]
where a_0=1+u^N, b_0=1+(-1)^N u^-N, and for 1<=S<N,
a_S=binom(N,S)u^S, b_S=(-1)^S binom(N,S)u^-S.
This expression is a polynomial despite its factored Laurent
notation. Its bottom and top coefficients are respectively
(-1)^N2^-N E_00 and 2^-N E_00. In particular the ACTUAL selected
functional satisfies
\[
                 \Phi_{e_D}(E_{N,0}\otimes H)
                                      =2^{-N}H_{00}. \tag{10}
\]
The surviving source cannot be replaced by the uniform interval
row merely because both return the same closed knot scalar.

## 4. Exact one-sided clock and Green moment corrections

Split E=E_0+E_1 using its two terms, so
(E_1C)_ij=(i/N)C_(i-1,j-1). For every retained scalar function g
on the indicated finite spectra,
\[
 \begin{split}
 E(g(J_{\mathrm{head}})C)
       &=g(J_N)E_0(C)+g(J_N-1)E_1(C),\\
 E(Cg(J_{\mathrm{head}}))
       &=E_0(C)g(J_N)+E_1(C)g(J_N-1).               \tag{11}
 \end{split}
\]
The functions at the extra argument -1 may be chosen arbitrarily
where their multiplier is zero; they must be regular wherever
that multiplier is nonzero. These identities follow directly
from the row and column indices. In particular
\[
 E(w^J C)=w^{J_N}\{E(C)+(w^{-1}-1)E_1(C)\},          \tag{12}
\]
and the polynomial moment correction is exactly the backward
difference [p(J_N-1)-p(J_N)]E_1(C). Ad-clock covariance is
strict because the same auxiliary offset cancels between row
and column. One-sided Green moments do not have that cancellation.
For normalized degree-h moments the backward difference contains
the explicit powers N^-s, s=1,...,h; they are retained before
any period/character estimate.

## 5. Whole word strictification retains a genuine auxiliary source

There is a direct positive strictification of (11). On
Sym^(N-1) tensor C^2 define
\[
 \begin{split}
 i_+v_k&=v_k\otimes u_0+v_{k-1}\otimes u_1,\\
 p_+(v_k\otimes u_0)&=(N-k)v_k/N,\\
 p_+(v_k\otimes u_1)&=(k+1)v_{k+1}/N.
 \end{split}
\]
Then p_+i_+=I and E(C)=p_+(C tensor I)i_+. The complementary
projector is I-i_+p_+; it is the Sym^(N-2) channel. EXACTLY,
\[
 E(CD)-E(C)E(D)
  =p_+(C\otimes I)(I-i_+p_+)(D\otimes I)i_+.        \tag{13}
\]
Thus the full auxiliary operator algebra is multiplicative and
preserves an ordered actual word, while a product of upper
compressions omits the displayed lower-channel excursions.
The original head number is J_total minus the auxiliary bit;
its two blocks have total degrees J_N and J_(N-2)+1. This is
the operator explanation of (11)--(12).

An exact source-preserving FINAL CUT choice even has both external
ends in the upper channel. Set
\[
 \Psi=i_+\mathbf1_{N+1}=\mathbf1_N\otimes(u_0+u_1),
       \qquad\Lambda=\frac{\mathbf1_{N+1}^t}{N+1}p_+.
\]
Its auxiliary dual is correlated with the head:
\[
 \Lambda(v_k\otimes u_0)=\frac{N-k}{N(N+1)},\qquad
 \Lambda(v_k\otimes u_1)=\frac{k+1}{N(N+1)}.
\]
It pairs with Psi to one, annihilates the lower channel, and gives
Lambda(C tensor I)Psi=sum(C_ij)/N for EVERY head C. The same
holds for a full ordered word with all internal excursions kept.
A product auxiliary dual is a different source. Closed/pivotal
strands require their actual transported caps and pivot operators;
the unweighted final-cut identity does not substitute for those.
This is an auxiliary matrix-word extension of the old head R, not
an equality with the existing actual high-integral-color R.

## 6. The precise remaining relative source calculation

For the norm-orbit test Lambda_rel omega, the new head map removes
the cut K/F rows on its image by its actual co-source homotopy.
An arbitrary Fr-valued current first has the explicit remainder
(1)/(4). The quotient contraction (6) reduces its cohomological
source obstruction to the one resonant endpoint; its selected
weight is (7)--(10), NOT automatically the uniform row.

This does not prove that the two INTERNAL framing Green currents
land in that head image, or that their remaining relative endpoint
and logarithmic carry classes cancel. A map of those actual
currents must retain (11), all lower excursions in (13), the
physical versus memory-clock distinction, charged normal head
neighbors, the original chirp and full peripheral line. The
explicit residual polynomials and endpoint coefficient are now
finite tests for that map, rather than a general group-theoretic
identification or an assumed scalar normalization.

[Exact residual/source audit](../experiments/audit_degree_elevation_wall_residual.py).
