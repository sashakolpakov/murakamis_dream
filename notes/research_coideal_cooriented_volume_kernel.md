# Every cooriented coideal crossing has a positive volume amplitude

24 November 2026. Research note. Written proof.

The actual mixed coideal coefficient is nonzero throughout the strict
cooriented domain, at both index parities. Its calibrated phase is the
same quadratic height phase as before, and its logarithmic magnitude
is the volume of the sewn ideal octahedron, with a universal logarithmic
error over all allowed labels. The unresolved parity is settled by a
positive Dirichlet problem for the actual crossing recurrence.
Its lower boundary is an exact finite quadrature and its upper boundary
is a balanced finite Sears sum with positive terms. A finite forest
comparison transfers the already proved neighboring-parity rate.

This is a local source-kernel theorem. The original input, marked closing,
external scalar and coherent intermediate sums are still required for
an assembled word.

## 1. Actual coefficients and the statement

Use the complete source conventions
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \delta=\pi/N,\quad \kappa=e^{i\pi d^2/(2N)},\quad
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N.
 \tag{1}
\]
Every Pochhammer in this proof is finite. Sort the simple roots as
\(\lambda_t=2\sqrt q\cos\alpha_t\),
\(\alpha_t=(t+\tfrac12)\delta\), \(0\le t\le d\), with
\(\sqrt q=e^{\pi i/(2N)}\). Define
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
  =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                 -q(1-Q^a)^2D_{a-1}(\lambda;\sigma),\qquad
 \Phi_{rs}(z)=\sum_{a=0}^d D_a(\lambda_r;\lambda_s)z^a/F_a.
 \tag{2}
\]
Write
\[
 \Sigma(r,v;t,s)=\sum_{a=0}^d
    \overline{D_a(\lambda_r;\lambda_v)}D_a(\lambda_t;\lambda_s)
                                                /|F_a|^2,
 \quad f_j=e^{i\delta j(j+1)/4},\quad
 \gamma_{ij}=e^{i\pi d/4}f_i/f_j,
 \quad J(r,t;v,s)=\Sigma(r,v;t,s)/(\overline\gamma_{rv}\gamma_{ts}).
 \tag{3}
\]
Strict coorientation means
\[
             \max(r,t)+\max(v,s)\le N-2.
 \tag{4}
\]
C's self-inversivity and central-coefficient identity imply that J is
real and symmetric separately in r,t and in v,s. This uses the actual
finite coefficients, not a positive-metric adjoint: if
\(P=[z^d](\Phi_{rv}\Phi_{ts})\), then
\(J=P/(\gamma_{rv}\gamma_{ts})\); P is separately symmetric in the
middle and neighboring labels. Reality follows by conjugate reversal.
Positivity will be proved below.

Put \(a_1=\cos\alpha_r,a_2=\cos\alpha_t\),
\(b_1=\cos\alpha_v,b_2=\cos\alpha_s\), and define
\[
 x_*={a_1a_2-b_1b_2\over a_1+a_2+b_1+b_2},\quad
 \Theta_*=\arccos x_*,\quad
 \psi_i={\pi-\alpha_i-\beta_i\over2},\quad
 u_i={\Theta_*-\alpha_i\over2},
\]
where \((\alpha_1,\alpha_2)=(\alpha_r,\alpha_t)\) and
\((\beta_1,\beta_2)=(\alpha_v,\alpha_s)\). Set
\[
 V={1\over2}\sum_{i=1}^2 2\{\Lambda u_i+
 \Lambda(\alpha_i+u_i)+\Lambda(\psi_i-u_i)
                         +\Lambda(\psi_i+\beta_i-u_i)\},
 \quad \Lambda(z)=-\int_0^z\log|2\sin w|\,dw .
 \tag{5}
\]
The odd, pi-periodic extension is understood.
Q's supporting-face proof uses only strict coorientation: V is the
volume of its sewn convex ideal octahedron. On the closed cooriented
domain define V/pi as one half of the maximum of the two summed
mean-zero energies on the nonempty closed common arc. This agrees
with (5) in the strict domain and defines all collapsed and repeated
wall equalities, including points where the displayed x_* ratio is 0/0.

**Theorem.** There is a universal C such that at every level and every
quadruple (4),
\[
                  J(r,t;v,s)>0,\qquad
              |\log J(r,t;v,s)-NV/\pi|\le C\log N.
 \tag{6}
\]
No discriminant inequality or index parity remains.

## 2. Exact finite boundary quadratures

We recall precisely the finite grid facts used here. On either parity
of the raw q-grid, the zeros of Phi_rs are the step-two interval
\[
 L_r^p=\begin{cases}1-r,&p=1-r\pmod2,\\r+2,&\text{otherwise},\end{cases}
 \qquad
 U_s^p=\begin{cases}N+s-1,&p=N+s-1\pmod2,\\N-s-2,&\text{otherwise}.
 \end{cases}
 \tag{7}
\]
An upper endpoint equal to the lower endpoint minus two means an empty
string. All root lifts on both grids lie between 1-r and N+s-1.
These are the exact two finite product strings of Q and T.
Finite Parseval on either N-point grid is exact, since exponent
differences of the two degree-d polynomials lie in [-d,d].
On the common negative component the mixed phase is exactly
\(\overline\gamma_{rv}\gamma_{ts}\).

If \(N+\max(r,t)+\max(v,s)\) is even, Q's root union deletes all
samples outside that component, giving J as a strictly positive sum.
We need the following two additional lower-boundary cases when this
index parity is odd. Put \(R=\max(r,t),S=\max(v,s)\).

If r=t, choose p=r. The selected root intervals have lower endpoint
r+2, and the S-polynomial supplies upper endpoint N+S-1; cross
coorientation joins the intervals. Thus the survivors are
\(k=-N+S+1,-N+S+3,\ldots,r\).
Beyond the common negative component, they cross only the opposite-grid
roots from 1-r through r+1. Every such root belongs to both polynomials:
the other upper endpoint is at least r+1 by coorientation. The two
phase signs therefore flip together. Every surviving mixed sample
has the original common phase and nonzero magnitude. Finite Parseval
again gives J as their strictly positive average.

If \(|r-t|=1\), choose p=R. The smaller middle label R-1 supplies
lower endpoint 2-R, while the S-polynomial supplies upper endpoint
N+S-1. Their intervals overlap or touch, by (4). The survivors are
\(k=-N+S+1,-N+S+3,\ldots,-R\). All are strictly before the first
possible actual root 1-R, hence in the same common negative component.
Their mixed products again have the same phase and positive magnitude.
These arguments include empty secondary strings and all small levels.

Here is the uniform rate argument, repeated so no ledger estimate is
an input. Every surviving nonroot q-grid node is at distance at least
delta from every actual root. Compare each root-string logarithmic
sum with integrals over centered cells of length 2delta. The boundedly
many cells nearest a logarithmic singularity have sample and average
-log N+O(1), even at an endpoint; the other cells have total variation
O(log N) from the integral of absolute cotangent. Thus the comparison
is two-sided with universal O(log N) error at every survivor.
The finite endpoint shift costs the same amount, because Lambda has
uniform modulus C|h|log(e/|h|).

For the usual rotated variable z=q^{-1/2}e^{i theta}, let E be the sum
of the two mean-zero energies in Q(16). On the common negative arc
its unique maximum is 2V/pi. A surviving node is within delta of that
maximum. In the equal-label case the extra nodes extend only through
[-alpha_r,+alpha_r]. There cos(theta)>=cos(alpha_r), and Q(17)
gives E'<0, so they add no larger maximum. In the adjacent-label case
the last node is at most delta beyond the continuum gap endpoint;
Lambda's modulus costs only O(log N). The same cell estimates and
one surviving node therefore prove (6) for the good parity and for
both lower-boundary strips just established.

We will also use the consequence
\[
 |V(\mathbf a)-V(\mathbf a')|
       \le C h\log(e/h)\quad
       \text{when the four angles differ by at most }h,\quad
                         0<h\le\pi/2 .
 \tag{8}
\]
This holds uniformly on the closed cooriented domain: express V/pi
as one half of the maximum of E on the closed common arc. Lambda's
modulus bounds changes of E, and the arc endpoints move by at most h.
It remains valid at the equality boundary used next.

## 3. The equality-wall coefficient is positive

By neighbor symmetry assume 0<=v<=s=S. Fix input r with
r+S<=N-2 and put u=d-S, so lambda_u=-lambda_S. This is one step
past the strict output interval. Define
\[
 \Psi_S=\Phi_{u,S}
 =(-q^{1-S}z;Q)_S(-q^{S+2}z;Q)_{d-S},\qquad
 C_j={(q;Q)_j\over F_j},\qquad
 z_j=-q^{S-2j}\quad(0\le j\le S).
 \tag{9}
\]
On the parity grid p=N+S, Psi_S is supported at exactly these S+1
nodes. This follows directly from its two zero strings, or by cancelling
zeros in
\(\Psi_S(z)=\Psi_0(q^S z)(-q^{1-S}z;Q)_S/
(-q^{-S}z;Q)_S\), where \(\Psi_0(z)=\sum_{a=0}^d(-z)^a\).
Its surviving values have the exact scalar
\[
                   \Psi_S(z_j)=Nq^j C_j C_{S-j}.
 \tag{10}
\]
Indeed the two finite factors evaluate to
\((qQ^{-j};Q)_S F_{d-j}/F_{S-j}\).
Use \(F_{d-j}=N(-1)^jQ^{j(j+1)/2}/F_j\) and
\((qQ^{-j};Q)_j=(-q)^jQ^{-j(j+1)/2}(q;Q)_j\).
These give (10), without a removable-root normalization choice.

Use the finite notation
\({}_4\phi_3[A,B,C,D;E,F,G;Q,Q]
=\sum_{j\ge0}(A,B,C,D;Q)_j Q^j/(Q,E,F,G;Q)_j\),
terminated at the displayed integer termination. Finite Parseval and
(10) give the literal equality-wall coefficient
\[
 \Sigma(r,v;u,S)=\overline{\Phi_{rv}(-q^S)}\,C_S\,\mathcal F,
\]
\[
 \mathcal F={}_4\phi_3\left[
 q,Q^{-S},q^{1-S+v},q^{-S-v};
 qQ^{-S},-q^{1-S-r},-q^{2-S+r};Q,Q\right].
 \tag{11}
\]
Here is a direct ratio check. If A,B are the two lengths of Phi_rv,
then at z_j its arguments are q^{S+1-v}Q^{-j} and
q^{S+v+2}Q^{-j}. Product reversal gives
\[
 {\overline{\Phi_{rv}(z_j)}\over\overline{\Phi_{rv}(z_0)}}
 ={(q^{1-S+v},q^{-S-v};Q)_j\over
                  (-q^{1-S-r},-q^{2-S+r};Q)_j},\qquad
 {C_{S-j}\over C_S}
   =q^j{(Q^{-S};Q)_j\over(qQ^{-S};Q)_j}.
 \tag{12}
\]
For the first formula the unconjugated reversal includes Q^j;
self-inversivity at these unit-circle nodes removes it on conjugation.
Substitution into (10) proves (11), including its source phase.
All denominator factors are nonzero: the first denominator is an odd
q-power string; the two negative strings have exponents strictly
between -N and N at every used index, by r+S<=N-2.

Put
\[
 n=\begin{cases}(S-v-1)/2,&S-v\text{ odd},\\
                 (S+v)/2,&S-v\text{ even},\end{cases}
 \quad e=-q^{1-S-r},\quad f=-q^{2-S+r},
 \quad P=q^n{(e/q,f/q;Q)_n\over(e,f;Q)_n}.
 \tag{13}
\]
Thus 0<=n<=S, and one of the original numerator parameters is Q^-n.
More explicitly, (7) shows Phi_rv(z_j)=0 for every sampled j>n:
if S-v is odd the selected upper root endpoint is N+v-1, and if
even it is N-v-2. The first such j is n+1, and coorientation
places the lower root endpoint at most N-S. Thus (11) is truncated
at n, with n=0 interpreted as the one-term sum.

Apply the complete finite identity S139 with retained parameter a=q,
b=Q^-S, d=qQ^-S, and c the remaining numerator. The balance is exact.
Its factor is P after finite product reversal, and it gives
\[
 \mathcal F=P\sum_{j=0}^n U_j,\qquad
 U_j={(Q^{-n},Q^{-n},q,q;Q)_j Q^j\over
 (Q,qQ^{-S},-q^{S-2n+r+2},-q^{S-2n-r+1};Q)_j}.
 \tag{14}
\]
This uses an own finite polynomial proof of Sears, not an infinite
summation at a root. Only the final denominators need be nonzero.

For n=0, P=1 and the transformed sum is1. The following factor
checks concern n>0 and only factors that occur; an unused
denominator parameter may equal1.
Every U_j is strictly positive real. The two numerator sine strings
are squared. The first denominator sine string is strictly negative,
the Q string positive, and the other two strings are positive cosines.
Their cosine exponents range inside (-N,N): the first ends at S+r,
the second at S-r-1, and their lower endpoints exceed -N.
The balanced phase contributes (-1)^j, cancelled by the j negative
sines. The two cosine-ratio products in P are positive too; their
q^{-1/2} phases cancel q^n. This proves positivity for both gap parities,
including n=0. No terminating numerator is cancelled against a zero
denominator.

We record polynomial bounds for later use. Define
\[
 R_j=\prod_{h=1}^j{\sin(h\delta)\over\sin((h-\tfrac12)\delta)},
                     \qquad 1\le R_j\le N\quad(0\le j\le d).
 \tag{15}
\]
For a short proof, R is unimodal with maximum at floor(N/2), and
R_d=N sin(delta/2)>=1. On the lower half, decreasing sinc bounds
R_m by \(\prod_{h=1}^m h/(h-1/2)\le2\sqrt m\le N\) for m>=1;
R_0=1 separately. The middle inequality follows by induction after squaring: the ratio
of consecutive squared products divided by m is
m(m+1)/(m+1/2)^2<1. This proves (15) also at N=2.

Let m=n-k. From (14),
\[
 {U_{k+1}\over U_k}
 ={\sin^2(m\delta)\sin^2((k+1/2)\delta)\over
 \sin((S-k-1/2)\delta)\sin((k+1)\delta)\cos A_k\cos B_k},
\]
where
\(\cos A_k\cos B_k=
[\cos\alpha_r+\cos((S-2m+3/2)\delta)]/2\).
Coorientation bounds this below by
\(\sin((S-m+3/2)\delta)\sin(m\delta)\).
The ideal ratio
\[
 T_k={\sin(m\delta)\sin((k+1)\delta)\over
          \sin((S-k)\delta)\sin((S-n+k+1)\delta)}\le1
 \tag{16}
\]
has denominator minus numerator
\(\sin((S+1)\delta)\sin((S-n)\delta)\ge0\).
The cumulative discrepancy between the actual ratio bound and T_k is
\(R_j^{-2}(R_S/R_{S-j})
 (R_{N-S+n-1}/R_{N-S+n-j-1})\), at most N^2.
Thus \(1\le\sum U_j\le N^3\). Each cosine-ratio product in P is
an integer/half-grid sine interval ratio or its reciprocal, so (15)
gives \(N^{-2}\le P\le N^2\). In particular
\[
                         N^{-2}\le\mathcal F\le N^5.
 \tag{17}
\]

The phase of (11) is the required one. At z_0 take raw angle
vartheta_0=pi+S delta. Every Phi_rv root lift xi satisfies
0<vartheta_0-xi<2pi. Hence
\(\Phi_{rv}(z_0)=(-1)^d\gamma_{rv}
 e^{id\vartheta_0/2}|\Phi_{rv}(z_0)|\).
Since \(C_S=q^{-S/2}/R_S\) and
\((-1)^d e^{-id\vartheta_0/2}q^{-S/2}=i^{d-S}
=\gamma_{uS}\), the wall amplitude is exactly
\[
             J(r,u;v,S)={|\Phi_{rv}(-q^S)|\over R_S}\mathcal F>0.
 \tag{18}
\]
The wall pair has identically zero continuum energy because
alpha_u+alpha_S=pi. The rotated point z_0 is exactly the collapsed
common-arc point. It is a nonroot grid point of Phi_rv. The two-sided
cell estimate from Section 2 and (15)--(17) therefore prove the
universal volume estimate (6) for this wall value as well.

## 4. The actual sorted crossing recurrence

By the exact separate symmetries of J, assume r<=t and v<=s=S.
Put y=cos(alpha_r), a=cos(alpha_v), b=cos(alpha_S). Thus a>=b.
For a variable output index t, write theta=alpha_t and x=cos(theta).
Away from the two sorted folds, the actual crossing equation is
\[
 c_t^+ j_{t+2}+d_t j_t+c_t^-j_{t-2}=2y j_t,
 \quad j_t=J(r,t;v,S),
\]
\[
 c_t^\pm={(\cos(\theta\pm\delta)+a)
                (\cos(\theta\pm\delta)+b)\over
                  \sin\theta\sin(\theta\pm\delta)},\qquad
 d_t={-2[x(1+ab)+(a+b)\cos\delta]\over
                         \sin^2\theta-\sin^2\delta}.
 \tag{19}
\]
We spell out its source typing. N proves the finite cyclic difference
relation from the functional equation of Phi. With U_sigma the actual
continuant eigenmatrix, X=diag(lambda), and
K_sigma=U_sigma^{-1}diag(Q^{-h})U_sigma, the same entry calculation,
with c replaced by the actual external root nu, gives the following.
Here nu=lambda_v and sigma=lambda_S.
\[
 J_{\nu,\sigma}
 =-{K_\sigma X+XK_\sigma+2q\sigma I\over1+Q}
                                      -q^{-1}\nu K_\sigma,
 \qquad J_{\nu,\sigma}B^+=B^+X.
 \tag{20}
\]
Here B^+=kappa U_sigma^{-1}diag(q^{-h})overline(U_nu), as in T.
For N>=3 division by 1+Q is legitimate. Insert N's explicit cyclic
coefficients, sort lambda_t=2sqrt(q)cos(alpha_t), and conjugate the
output column by \((-1)^t\sin\alpha_t/f_t\). A cyclic step becomes
a sorted step by two. The two adjacent entries divided by sqrt(q)
are exactly c_t^+ and c_t^- in (19); the diagonal is d_t.
Thus (19) is the actual phase-removed face equation, not a recurrence
postulated from the volume.
The bad solved rows lie in 2<=t<=N-3. The good comparison may also
use t=N-2 when S=0, hence nu=sigma=c. There the actual upper
folded edge is exactly zero by N's source cut identity; the diagonal
and lower coefficient remain (19), with the outgoing term omitted.

The following exact row identity is useful:
\[
 \omega_t=2y-d_t-c_t^+-c_t^-
 =2\left[y+\cos\delta-
                   {(1-a)(1-b)\over\cos\delta+x}\right].
 \tag{21}
\]
It follows by a common denominator and sine addition. In the strict
output range r<=t<=T=N-S-2, every edge coefficient used between
solved nodes or their Dirichlet boundaries is positive. At the good
terminal node T the unused outgoing coefficient c_T^+ is zero.
Moreover y>=x and a>=b, and
x>=-cos((S+3/2)delta). Therefore
\[
 \omega_t\ge4\sin(\delta/2)
           [\sin((S+1)\delta)-\sin(\delta/2)]\ge cN^{-2}.
 \tag{22}
\]
Indeed x+cos(delta) exceeds 1-b by at least
2sin(delta/2)[sin((S+1)delta)-sin(delta/2)]. Substitute this in
2[(x+cos(delta))^2-(1-b)^2]/(x+cos(delta)).
The last inequality uses sin((S+1)delta)>=sin(delta).
Also omega_t<=4. Nonzero c-coefficients lie between cN^{-4} and CN^2,
by the elementary nonzero root-grid sine bounds.

## 5. A no-fold Dirichlet problem proves positivity

The class N+t+S even is already settled by Q. For the other class set
\[
 t_0=\begin{cases}r,&N+r+S\text{ odd},\\r+1,&N+r+S\text{ even},\end{cases}
 \qquad u=d-S=T+1.
 \tag{23}
\]
If t_0>T-1, there is no unresolved output and this case is finished.
All outputs under consideration are t=t_0,t_0+2,...,T-1.
The value at t_0 is a positive equal- or adjacent-label boundary from
Section 2. The value at u is the positive wall (18). If there is no
index strictly between t_0 and u there is nothing further to solve.
Otherwise write (19) on the interior nodes t_0+2,...,T-1.
The matrix has diagonal 2y-d_t, off-diagonals -c_t^+,-c_t^-, and
positive row defect omega_t, with boundary exits added at its ends.
Its right side consists of the two positive boundary values multiplied
by their positive incident coefficients.

This is a real strictly diagonally dominant M-matrix. For completeness,
divide by its positive diagonal. The off-diagonal transition matrix
is nonnegative with every row sum less than one; its finite-dimensional
Neumann inverse is nonnegative. Connectivity makes the response to
these boundary data strictly positive at every interior node.
The maximum principle and (22) also give
\[
                  \|M^{-1}\|_\infty\le CN^2.
 \tag{24}
\]
The actual j column satisfies this same Dirichlet system, so uniqueness
identifies it with that positive solution. This proves noncancellation
for every strict cooriented quadruple. At N=2 the sole cooriented
quadruple is already in Q; the small empty branches likewise need no
use of (20). No folding or unproved boundary sign is concealed.

## 6. A finite positive Green comparison

We give the exact finite argument that transfers the rate without a
stationary-point approximation. For a killed directed path write a row
as
\(\kappa_i e_i^T+\sum_{i\to j}w_{ij}(e_i-e_j)^T\), with all
kappa_i,w_ij positive. Row multilinearity expands its determinant into
positive rooted-forest monomials. A chosen directed cycle gives dependent
rows; an acyclic assignment ending at chosen roots has determinant one
by topological elimination. For adj(M)_ij replace row j by e_i^T.
The same expansion contributes one exactly when the path from i ends
at the free root j, and zero otherwise: along this path e_i differs
from e_j by chosen difference rows. Thus every inverse numerator has
a positive forest expansion as well.

It follows that if corresponding positive weights of two paths obey
\[
       \sum_{\text{all weight types}}
             |\log(w_{\rm first}/w_{\rm second})|\le L,
 \tag{25}
\]
then corresponding determinant and adjugate ratios lie between e^-L
and e^L. Every inverse-entry ratio lies between e^{-2L} and e^{2L}.
This is a finite identity/comparison, with no positivity assumption
on an unknown source vector.

Apply it to our bad-parity interior nodes and the good-parity nodes
one index larger. The bad nodes t_0+2,...,T-1 correspond to the good
nodes t_0+3,...,T, with the same number of vertices. In the latter
system the outgoing coefficient at T is zero, because
cos(alpha_T+delta)+b=0. Thus the actual positive good column g solves
that system with its left boundary value at t_0+1 as its only forcing.
For the bad system the wall exit is included in its final killing
weight. Each first-row left exit is included in its killing weight.

The matched interior factor ratios in (25) have total logarithm
O(log N), uniformly over all allowed parameters. Indeed each half
interval theta to theta+delta is disjoint from the next. The logs of
cos(theta+/-delta)+a,b are monotone, with polynomial nonzero upper and
lower bounds. The logs of the sine denominators have one maximum and
the same bounds. Their total variations are O(log N). The killing
omega(theta) in (21) is decreasing and lies in [cN^{-2},4], so it has
the same variation bound. Adding the two endpoint exits changes only
a bounded number of positive killing weights, by polynomial ratios.
Consequently all corresponding Green entries obey
\[
                   N^{-C}G^{\rm good}_{ij}
       \le G^{\rm bad}_{ij}\le N^CG^{\rm good}_{ij}.
 \tag{26}
\]
Both path lengths one and larger are covered by the forest formula.
Empty paths were already excluded in Section 5.

## 7. Polynomial comparison proves the uniform volume rate

Index the two matched interior paths by i=1,...,L. Put
l_b=j(t_0), l_g=g(t_0+1), w=j(u), and let beta_b,beta_g be the
positive left incident coefficients, eta_b the bad right incident
coefficient. The exact two systems give
\[
 g_i=\beta_g l_gG^{\rm good}_{i1},\qquad
 j_i=\beta_b l_bG^{\rm bad}_{i1}
                          +\eta_b wG^{\rm bad}_{iL}.
 \tag{27}
\]
Every incident coefficient here and its inverse is polynomial in N.
The universal boundary estimates of Sections 2--3 and (8) imply
\[
        N^{-C}\le l_b/l_g\le N^C,\qquad
                       N^{-C}\le w/g_L\le N^C.
 \tag{28}
\]
For the second comparison, the last good output T and the equality
output u differ by one angle step delta. The closed-domain maximum
energy definition handles repeated vanishing cross sums as well.
For the first comparison the two lower outputs also differ by delta.
There is no compactness or Hessian requirement in (28).

The left term in (27) and (26) immediately bound j_i below by
N^{-C}g_i and bound that same term above by N^C g_i.
The right term is controlled without an unknown boundary amplitude.
The normalized last Green column satisfies
\[
             {G^{\rm good}_{iL}\over G^{\rm good}_{LL}}
                              \le {g_i\over g_L}.
 \tag{29}
\]
To prove this, fix value one at the last vertex and compare the first
L-1 equations. The normalized Green column has zero left exterior
boundary, whereas g/g_L has a positive left boundary. Their difference
is nonnegative by the same M-matrix inverse. For L=1 the assertion is
an equality. Also G_good_LL<=CN^2 by (24).
Substitute (26), (28), and (29) into the right term of (27). It is at
most N^C g_i. We have proved the actual uniform comparison
\[
                         N^{-C}g_i\le j_i\le N^C g_i.
 \tag{30}
\]
The good output corresponding to i is exactly one angle step above
the bad output. Q's positive quadrature, with the universal cell proof
in Section 2, gives its logarithmic volume rate. Formula (8) changes
its N-scaled action by O(log N). Equation (30) therefore proves (6)
for every remaining parity and every cooriented label. Together with
the empty-path and small-level cases, the proof is complete.

No rate was inferred merely from the polynomial norm (24).
The positive forest identity, matched total variation, and the two
source-calibrated boundary rates are all necessary in this argument.
Nor were extra absolute-circle peaks compared with the gap maximum:
finite orthogonality controls the good branch and positive recurrence
controls the other one.

## 8. Both actual signs, full neighboring weights and scope

For sorted input, output and neighboring indices r,t,v,s satisfying
(4), the original same-frame entries are exactly
\[
 B^+_{t,r}=(-1)^t\sin\alpha_t
                  {f_vf_s\over f_tf_r}J(r,t;v,s),\qquad
 B^-_{t,r}=\overline{B^+_{t,r}}.
 \tag{31}
\]
C's scalar identity kappa q^{d/2}i^{-d}=1 uses the specified lift;
no original framing or crossing factor has been replaced by its
modulus. The sine and its inverse have polynomial size. Thus both
actual signed entries have the same uniform sewn-volume rate.

Let \(h_N(\xi,\zeta)=\sum_{a=0}^d
|D_a(\xi;\zeta)/F_a|^2\). In the complete physical nested joint Haar
frame, the additional positive factor is exactly
\[
 \left[{h_N(\lambda_v,\lambda_t)h_N(\lambda_t,\lambda_s)
             \over h_N(\lambda_v,\lambda_r)h_N(\lambda_r,\lambda_s)}
                                                        \right]^{1/2}.
 \tag{32}
\]
Both incident weights are compulsory. T's uniform two-label profile
supplies their four-term volume correction as before. This normalization
is distinct from the removed-head tail-pair form. All finite maps retain
the complete channels and Casimir normals.

The theorem removes the discriminant and parity restrictions on this
one local coefficient. It does not prove that an arbitrary geometric
character produces rotated-real coideal heights, or that every
intermediate quartet of an actual word is cooriented. The original
input and last marked closing must be transformed with the same full
source maps, and the original external factor chi_N remains.
The quadratic single-height phases in (31) do not by themselves align
all coherent sums or determine an original contour intersection.
No arbitrary-exterior scalar lower bound or finite-exception theorem
after arbitrary fixed short partial fillings is asserted.

The earlier notes provide the full source kernels, fixed-parity exact
orthogonality, phase calibration and sewn geometry. S139 gives its own
finite proof of the balanced identity used at the wall. The additions
are the calibrated positive wall sum, the no-fold source Dirichlet
problem, and the positive finite comparison that resolves the other
index parity with the same uniform rate. No novelty for abstract
M-matrices, finite forest expansions or basic hypergeometric notation
is claimed.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| Q | [Exact parity quadrature](research_coideal_parity_quadrature_volume.md) | 408 | e5e56ebf3354d57cbd80ac59d4b05b3ac2d03c1818687ead7f7951206286ef98 |
| C | [Signed coideal chamber](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| T | [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| N | [Marked source difference equation](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| S | [Own finite balanced Sears proof](finite_balanced_sears_operator_proof.md) | 139 | 4b32a5c71f5cc4484f773007e34d980266e0ba9688b0237d30f108e8a8e4ab8d |

Only written mathematics, complete source reads and text/hash operations
were used. Earlier final notes, the ledger and public manuscripts remain unchanged.
