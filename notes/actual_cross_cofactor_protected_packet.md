# A relative packet for the cleared cofactor at a protected middle face

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. Internally reviewed. This concerns the actual
fixed-root lower cofactor with b=0. It is not a whole-source saddle,
filling-cycle or genuine-q theorem. All products below stay at level N.

## 1. Exact recurrence and statement

Let x,y range in a sufficiently small fixed complex neighborhood of ANY
fixed positive pair, let u range in a sufficiently small complex disk
about 0, and put A=x+y, P=xy. Write h=1/N, s_j=2sin(pi*j/N),
a_j=4cos^2(pi*(j+1/2)/N). The original cleared cofactor recurrence at b=0
is

 R_0=1, R_(-1)=0,
 R_j=s_j^2 A R_(j-1)+s_j s_(j-1)(a_(j-1)+u)P R_(j-2).

Set L_j=R_j/(product_(r=1)^j s_r). Then EXACTLY

 L_j=s_j A L_(j-1)+(a_(j-1)+u)P L_(j-2),
 (L_0,L_(-1))=(1,0).                                      (1)

The normalization causes no loss at j=1: its second term multiplies
L_(-1)=0. Fix 0<t_0<1/2 and take t_0 N<=n<=N/2. Define

 T_h(t)=[[2sin(pi*t) A, P(4cos^2(pi*(t-h/2))+u)],[1,0]],
 lambda_+(t), lambda_-(t)=its two eigenvalues,
 g(t)=lambda_+(t)-lambda_-(t).

The square-root branch has g>0 at real x,y>0,u=0. Write lambda_(j,+)
for lambda_+(j/N), and similarly for minus and g. The matrix at t=0
is only a reference eigenbasis; it does not change the initial vector.
For all sufficiently large N these branches are holomorphic and

 C_j=(lambda_(j-1,+)-lambda_(j,-))/g_j =1+O(h),
 A_(N,n)=lambda_(n,+)/g_0 product_(j=1)^n C_j,
 E_(N,n)=product_(j=1)^n [s_j lambda_(j,+)].

Then uniformly on the stated FIXED complex neighborhood,

 R_n(0;x,y;u)=A_(N,n) E_(N,n) [1+O(N^-1)].          (2)

The explicit amplitude A_(N,n) is holomorphic, uniformly bounded and
bounded away from zero. The same relative error has fixed parameter
derivative bounds on every smaller neighborhood, by Cauchy. The
finite-N product E retains all endpoint factors and parity dependence;
no scalar normalization is discarded.

## 2. The eigenvalues have an algebraic gap even at the lower endpoint

For positive real x,y, u=0 and h=0, the discriminant is

 4sin^2(pi*t)A^2+16cos^2(pi*t)P>0,  0<=t<=1/2.

Its minimum and lambda_+ are positive on this compact interval.
They remain uniformly separated from zero for sufficiently small
complex parameter perturbations and small real h>=0. In particular
|g|>=c and |lambda_+|>=c. All derivatives needed below are uniformly
bounded on a small extension of this interval. lambda_- may vanish;
no inverse of lambda_- is used.

Put r(t)=lambda_-(t)/lambda_+(t). At t=0, r(0)=-1 EXACTLY, also for
complex parameters. Since lambda_++lambda_-=2sin(pi*t)A,

 r'(0)=2pi A/lambda_+(0).

Its real part is uniformly positive near the positive real parameters.
Therefore |r(t)|<=exp(-c t) for 0<=t<=epsilon with uniform c>0,
after shrinking the parameter neighborhood. On [epsilon,1/2], the
real unperturbed |r| is strictly less than1; compactness extends a
bound |r(t)|<=exp(-c t) there as well. These estimates are uniform
in sufficiently small h. Equality of the eigenvalue MODULI at t=0
therefore does not imply coalescence: |1-r| stays uniformly positive.

## 3. A one-step normal form, including the initial negative branch

Use E(t)=[[lambda_+(t),lambda_-(t)],[1,1]]. For the state vector
v_j=(L_j,L_(j-1))^T, set w_j=E(jh)^(-1)v_j. The exact update is

 w_j=diag(lambda_(j,+),lambda_(j,-)) B_j w_(j-1),
 B_j=E(jh)^(-1)E((j-1)h).

Here (B_j)_(++)=C_j. Divide out product lambda_(j,+) C_j, so the
normalized update has the form

 M_j=diag(1,d_j)+F_j,
 d_j=r(jh)(B_j)_(--)/C_j,
 F_j diagonal entries 0, offdiagonal entries O(h).

These matrices are samples of smooth functions of t, with
F'(t)=O(h), |1-d(t)|>=c, and |d_j|<=exp(Ch-c*j*h).
Choose the offdiagonal near-identity correction X_j by

 (X_j)_12=-(F_j)_12/(1-d_j),
 (X_j)_21= (F_j)_21/(1-d_j), diag X_j=0.

Then X_j=O(h), X_j-X_(j-1)=O(h^2). Direct multiplication gives

 (I+X_j)^(-1) M_j (I+X_(j-1))
                 =diag(1,d_j)+O(h^2).                  (3)

Only 1-d_j is divided out. This remains valid when d_j=0 and when
r(0)=-1. The diagonal product norms are at most exp(Cnh), and the
same holds for the corrected matrices, since each step has norm
at most exp(Ch)+O(h^2). Telescoping their n-fold products in operator
norm gives an O(nh^2)=O(h) error from the diagonal product. Meanwhile

 |product_(j=1)^n d_j|<=exp(Cnh-c h n(n+1)/2)=O(exp(-c' N))

for t_0 N<=n<=N/2. Thus the initial negative branch is retained and
then proved exponentially suppressed; it is not discarded by fiat.

The initial eigenvector coordinates are exactly (1/g_0,-1/g_0).
The near-identity corrections change them by O(h). Inverting the final
basis yields

 L_n=[product lambda_(j,+) C_j] lambda_(n,+)/g_0 [1+O(h)],

uniformly, since lambda_(n,+)/g_0 is bounded away from zero. This is (2).
The amplitude product is bounded and nonzero because every C_j=1+O(h)
and n=O(N). Uniform holomorphy proves the asserted Cauchy bounds.

## 4. Scope and exact degenerate outer faces

If b=0 and exactly one of x,y vanishes, the original recurrence is
instead the EXACT monomer product

 R_n=(x+y)^n product_(j=1)^n s_j^2,

independent of u. No limiting inverse of xy is used. If both outer
faces vanish and n>0, the same original recurrence is zero; this is
not part of the positive geometric triangle chart.

For x,y>0 the terminal ratios following from (2), uniformly on a
smaller neighborhood, are

 R_n/R_(n-1)=s_n lambda_(n,+) [1+O(N^-1)]

when n is m or m-1, m=floor(N/2). The limiting ratio is

 Lambda_*=2[A+sqrt(A^2+uP)].

Consequently E(b)/D(b) tends to u/Lambda_* at this protected middle,
with absolute O(N^-1) error. The case u=0 retains its actual small
finite-N factor a_(m-1); the displayed limit does not replace that
factor in any exact source identity.

No claim is made here for an independently summed positive starting
row b>0, the original shared face torus, or the original Gaussian
filling period. Those require additional arguments.

Root and two independent reviewers checked the complete normal-form proof. The finite diagnostic below compares the actual recurrence and explicit product at 40 positive/complex parameter and level choices; it does not establish the uniform theorem by itself.

[Focused audit](../experiments/audit_actual_cross_cofactor_protected_packet.py) · [Recorded output](../experiments/actual_cross_cofactor_protected_packet_results.json). These finite checks supplement the written proof and retain the scope recorded in their output.
