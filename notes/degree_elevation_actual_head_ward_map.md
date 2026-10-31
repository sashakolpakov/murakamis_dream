# Degree elevation preserves the cut and transports the actual head Borel complex

Research proof, 27 October 2026. The uniform co-source obtained by
integrating the paired Fr dual has N+1 states, whereas the original
head has N. A cyclic identification duplicates its endpoint and
does not preserve the head row. The explicit matrix degree elevation
below corrects this on ALL head matrices. Together with retained
whole arrow gauges it gives an actual cut-Ward cochain map, including
the original co-source homotopy. It is not a multiplicative R-network
map or a proof of Gaussian/source descent.

The earlier [degree-elevated wall note](degree_elevated_wall_source_and_divided_ward.md)
constructed the binomial wall row and its fixed-head equivariance
obstructions. It did not construct the full matrix degree elevation,
its uniform-cut identity, or the actual head-current map proved here.

## 1. Full matrix elevation, with both endpoint entries

Put n=N-1. In the actual Fr symbol convention
sigma_r(C)=ell_r(u) C psi_r(t)/(1+tu)^r, where
psi_r(t)_j=t^j and ell_r(u)_i=binom(r,i)u^i, define

\[
 (\mathcal E_NC)_{ij}
   =\frac{N-i}{N}C_{ij}+\frac{i}{N}C_{i-1,j-1},
       \qquad 0\le i,j\le N.                       \tag{1}
\]

Every out-of-range old entry is zero. Both terms are required.
Binomial cancellation gives the exact polynomial identity

\[
 \ell_N(u)(\mathcal E_NC)\psi_N(t)
                  =(1+tu)\ell_n(u)C\psi_n(t),
 \qquad\sigma_N(\mathcal E_NC)=\sigma_n(C).          \tag{2}
\]

The map is injective because the symbol numerator determines every
matrix entry. It is unital and preserves BOTH actual uniform rows:

\[
 \frac{\operatorname{Tr}(\mathcal E_NC)}{N+1}
      =\frac{\operatorname{Tr}C}{N},\qquad
 \frac{\sum_{ij}(\mathcal E_NC)_{ij}}{N+1}
      =\frac{\sum_{ij}C_{ij}}N.                    \tag{3}
\]

Indeed each old entry C_ij occurs with total coefficient
((N-i)+(i+1))/N=(N+1)/N, and the same holds for diagonal entries.
The second identity is the original average rank-one coupon, not
only the ordinary trace.

For a diagonal C the elevated entries are

\[
 \widetilde C_R=\frac{N-R}{N}C_R+\frac RN C_{R-1},
 \quad\widetilde C_0=C_0,\quad\widetilde C_N=C_{N-1}. \tag{4}
\]

Thus the actual paired-Fr interval, whose integrated dual is uniform
1/(N+1), gives the original head average exactly after (4). By
contrast the uncorrected cyclic P_diag insertion repeats C_0 at
R=N; it gives weights 2/(N+1),1/(N+1),...,1/(N+1). For C_R=Q_N^R
its value is 1/(N+1), while the old head average is zero. Formula
(4) is the required endpoint correction, not an identification of
these different rows. The binomial wall B_N remains its separate
co-source with its original factor 1/N.

## 2. Exact classical and whole Cartan covariance

The actual divided Fr matrices on degree r satisfy
e psi=(rt-t^2 partial_t)psi, f psi=partial_t psi and
h psi=(r-2t partial_t)psi, with their corresponding dual formulas.
The normalized commutator fields are independent of r.
Applying them to (2) proves

\[
 \mathcal E_N([x_n,C])=[x_N,\mathcal E_NC],
                    \qquad x=e,f,h.                \tag{5}
\]

This is also checked directly from (1); it is not an assumed
published quantization result. Since both terms of (1) have the
same i-j, for EVERY nonzero whole parameter Q,

\[
 \mathcal E_N(\operatorname{Ad}_{Q^{-J_n}}C)
       =\operatorname{Ad}_{Q^{-J_N}}\mathcal E_NC.    \tag{6}
\]

The image therefore is a global P1 operator/co-source submodule
under the ordinary divided Fr f and whole Cartan dilation. Its
two extreme entries (0,N),(N,0) are identically zero. It is not
the entire End(Sym^N); in particular an arbitrary degree-N wall
current need not belong to it.

## 3. Actual whole head arrows give a strict cut-current map

In a specified original head basis let
K_j=xQ^(-j), F_(j+1,j)=f_j(q), 0<=j<N-1, with all f_j actual
nonzero arrow units near q_N. This includes the original balanced
f_j=1-Q^(j+1) and the integral f_j=[j+1]_q, with their actual
source adapters carried. Define the WHOLE diagonal gauge

\[
 D_0=1,\qquad D_{j+1}/D_j=(j+1)/f_j(q).
\]

Then DFD^(-1)=f_n, the classical degree-n lowering matrix, and
DKD^(-1)=K. Every q-factorial, source and dual in this gauge is
retained; invertibility at fixed N is not an asymptotic norm bound.
Put T_0(C)=E_N(DCD^(-1)). Equations (5)--(6) give the LITERAL
whole matrix cochain identities

\[
 T_0((\operatorname{Ad}_K-I)C)
       =(\operatorname{Ad}_{Q^{-J_N}}-I)T_0(C),\qquad
 T_0([F,C])=[f_N,T_0(C)].                           \tag{7}
\]

Thus the actual two-row cut-Ward complex maps isomorphically onto
its image subcomplex by T_0 in degree zero and the displayed two
row maps in degree one. This is an explicit current map, not a
declaration that two Borel groups are abstractly isomorphic.

The actual Hopf F row is transported too, with its explicit ordered
K-row correction retained:

\[
 \operatorname{ad}_F(C)=[F,C]+K^{-1}[K,C]F,
 \quad [K,C]=((\operatorname{Ad}_K-I)C)K.             \tag{8}
\]

Use this invertible row operation before (7). Its product term is
sent by the LINEAR map T_0 with its full order; T_0 is not applied
to its factors separately.

The target may use the ACTUAL whole divided Fr lowering matrix on
any fixed residue string s. If its arrow is beta_(R,s)(q), set
B_(0,s)=1 and B_(R+1,s)/B_(R,s)=beta_(R,s)/(R+1). These are
regular actual units with root one, and
F^(N)|_s=B_s f_N B_s^(-1). Consequently

\[
                    T_s=\operatorname{Ad}_{B_s}T_0   \tag{9}
\]

has the same strict properties with actual F^(N)|_s in place of
f_N. B_s commutes with the whole memory Cartan Q^(-R). This
Cartan is the specified Fr memory observable; it is not silently
relabeled as the original high-color quantum K, whose root action
is on the head factor. The actual opposite divided generator and
mixed tensor coproduct still require their specified normal rows.

## 4. Original cut co-source and its exact transported homotopy

Conjugations preserve trace, so (3) gives tau_Fr T_s=tau_head.
Before D,B are inserted, (3) also preserves the original average
coupon on ALL matrices. After those gauges the actual source and
dual are transported; a binomial or uniform row cannot simply be
substituted for the conjugated row.

There is nevertheless an explicit comparison of the original head
average Phi_h and the uniform Fr interval row Phi_Fr on the image.
Let B_h be the actual head matrix [K,B_h]=e_h-I/N. In the target
let K_Fr=Q^(-J_N) and put

\[
 (B_{\mathrm{Fr}})_{ij}=\frac1{(N+1)(Q^{-i}-Q^{-j})}
       \quad(i\ne j,\ \{i,j\}\ne\{0,N\}),
\]

with the diagonal and the two extreme corners zero. Every displayed
denominator is a unit near Q_N. The omitted corners of T_s(C) are
IDENTICALLY zero, so the actual trace homotopies give

\[
 \Phi_h(C)-\Phi_{\mathrm{Fr}}(T_sC)
 =-\operatorname{Tr}(B_h[K,C])
       +\operatorname{Tr}(B_{\mathrm{Fr}}[K_{\mathrm{Fr}},T_sC]). \tag{10}
\]

The last commutator equals T_s((Ad_K-I)C) K_Fr. Thus (10) is an
explicit cochain homotopy on the actual cut-Ward complex. It holds
with the whole D and B_s units present, not only at their numerical
root values. On actual diagonal Green arrays these conjugations
do nothing and (3)--(4) preserve the original cut exactly. On
Ward-closed cut matrices the homotopy is zero as well. The raw
Green 1/N normalization remains the one in the original certificate.

The excluded extreme target corners and the complementary operator
subspace cannot be discarded if an arbitrary Fr-valued wall or
normal current leaves the image. This is where an additional
endpoint/mixed-normal source may still occur.

## 5. Scope of this actual map

The source and coefficient complex at the FINAL finite cut is now
explicitly related to global Fr P1 operators, the integrated uniform
Fr co-source, and the actual head Hopf rows. It does not turn T_s
into an algebra homomorphism: already N=2,
E_2(P_0)=diag(1,1/2,0), so E_2(P_0)^2!=E_2(P_0).
Products, R crossings and mixed coproducts must therefore be
transported as whole ordered operators, not factor by factor.

Nor has an internal remaining flow index been identified with this
open cut matrix index. The geometric Gaussian/source comparison
must still map its two retained currents and normal endpoint classes
to the explicit finite complex. The result here is a genuine cut
cochain map and co-source homotopy, not a selected geometric period
or volume limit.

[Exact matrix and coherent-symbol audit](../experiments/audit_degree_elevation_actual_head_ward.py).
The [results](../experiments/degree_elevation_actual_head_ward_results.json)
pass fourteen actual generic-q/root cases N=2,...,8 and 406 full
matrix units. They check the complete symbols and both uniform
rows, whole arrow gauges, the actual Fr divided string, Hopf row
correction and co-source homotopy. These are actual finite cut
identities, not a Gaussian or selected-cycle test.
