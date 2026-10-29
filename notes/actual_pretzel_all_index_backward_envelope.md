# A uniform all-index bound for the actual coherent pretzel inner packet

29 October 2026. The exact original-source Ward recurrence, together
with its proved high-index source anchor, bounds EVERY remaining inner
index. The estimate retains both classical characteristic branches,
every endpoint factorial and both parities. Its prefactor is polynomial
in N, uniformly even at r=0. No rational first-order factorization or
choice of a single growing branch is assumed.

## 1. Literal selected packet and theorem

Use N>=2, q=exp(pi i/N), Q=q^2, M=floor((N-1)/2), and
F_a=(Q;Q)_a. In the EXACT original rotated box, reversing the two
finite sums gives the inner packet

\[
 A_r=\sum_{v=r}^M Q^{-vr}\frac{F_{2v}}{F_v^3F_{v-r}},
 \qquad D_r=Q^{-r^2}\frac{F_{2r}}{F_r^3},
 \qquad U_r=A_r/D_r,\quad 0\leq r\leq M.                \tag{1}
\]

All D_r are nonzero, including r=0 and r=M. These are the same
packets in the [actual coherent inner elimination theorem](actual_pretzel_coherent_inner_gauss_elimination.md),
not an arbitrary solution of their recurrence. That finite source
transformation proves, at BOTH parities,

\[
 |U_r|\leq2N,\qquad \lceil N/4\rceil\leq r\leq M.      \tag{2}
\]

Only this upper bound is needed here; its nonzero amplitude and phase
are not substituted into a different index range. The same theorem
proves the full selected Ward equation, with Y=Q^r,

\[
 QY^2(1-Q^2Y)A_{r+2}
 +Y(2Q^3Y^2+Q+1)A_{r+1}
 -Q(QY+1)(QY^2-1)A_r=0,                              \tag{3}
\]

and actual endpoints A_M=D_M, A_(M+1)=0.

Define the continuous nonnegative envelope

\[
 E(u)=\begin{cases}
 \displaystyle\frac2\pi\int_u^{\pi/4}\log\cot v\,dv,
                           &0\leq u\leq\pi/4,\\
 0,                        &\pi/4\leq u\leq\pi/2.
 \end{cases}                                                   \tag{4}
\]

The integral is finite at zero. The explicit uniform bound is

\[
 \boxed{|A_r|\leq8e^{128}N^{129}|D_r|
                 \exp\{N E(\pi r/N)\},
       \quad N\geq12,\quad0\leq r\leq M.}             \tag{5}
\]

The constants are deliberately coarse and independent of N,r.
In particular the exponential error after this full two-branch
envelope is uniformly o(N). This is a bound for the literal finite
packet BEFORE the original outer Newton sum and Hermite source;
no boundary packet or original current has been dropped.

## 2. Exact factorial cancellation in the normalized recurrence

The adjacent diagonal ratio is

\[
 \frac{D_{r+1}}{D_r}
   =Q^{-1}Y^{-2}\frac{(1-QY^2)(1+QY)}{(1-QY)^2}.       \tag{6}
\]

The factors 1-QY^2 and 1+QY are EXACTLY those in the backward
coefficient of (3). Cancelling them algebraically, rather than
estimating inverse factorials separately, gives

\[
 U_r=p_N(Y)U_{r+1}+q_N(Y)U_{r+2},                      \tag{7}
\]
\[
 p_N(Y)=-\frac{Q^{-2}Y^{-1}(2Q^3Y^2+Q+1)}{(1-QY)^2},
\quad
 q_N(Y)=-\frac{Q^{-4}Y^{-2}(1-Q^3Y^2)(1+Q^2Y)}
                      {(1-QY)^2(1-Q^2Y)}.             \tag{8}
\]

For r=M-1 the numerator of q_N vanishes at BOTH parities:
1-Q^(2M+1)=0 for odd N, or 1+Q^(M+1)=0 for even N. Thus
(7) extends to that last step with any assigned U_(M+1), for
example zero. This is an exact cancellation of the terminal
factorial zero, not division by D_(M+1). The proof below initializes
instead at two genuine high-index U values in (2), so it needs no
choice of a value beyond M.

## 3. Shifted classical matrix and a globally conditioned frame

Put R=ceil(N/4), delta=pi/N, and for 0<=r<R use

    Z=Q^(r+1)=exp(2iu), u=(r+1)delta.

The shifted classical backward matrix is

\[
 T_0(u)=\begin{pmatrix}p_0&q_0\\1&0\end{pmatrix},\qquad
 p_0=-\frac{Z^{-1}(2Z^2+2)}{(1-Z)^2},\quad
 q_0=-\frac{Z^{-2}(1+Z)^2}{(1-Z)^2}.                   \tag{9}
\]

On the unit circle its eigenvalues are

    mu_1=-Z^(-1), mu_2=Z^(-1)c, c=cot(u)^2,
    rho(u)=max(1,c).

They remain DISTINCT even where their moduli meet. Use the normalized
right eigenvector matrix

\[
 V(u)=\left(
  \frac{(-Z^{-1},1)^{\mathsf T}}{\sqrt2},
  \frac{(Z^{-1}c,1)^{\mathsf T}}{\sqrt{1+c^2}}
       \right).                                      \tag{10}
\]

Its column correlation is

    (1-c)/sqrt(2(1+c^2)), whose modulus is at most1/sqrt2.

Therefore, UNIFORMLY for 0<u<pi/2,

\[
 \|V(u)\|_2<\sqrt2,\qquad \|V(u)^{-1}\|_2<2,
                         \qquad \|V'(u)\|_2\leq4.       \tag{11}
\]

For the derivative, write the second column as
(e^(-2iu)cos theta,sin theta), theta=atan(tan(u)^2).
If t=tan u, then theta'=2t(1+t^2)/(1+t^4)<=2, since
1+t^4-t-t^3=(t-1)^2(t^2+t+1)>=0. Its squared derivative
norm is at most8; the first column's is2. Thus the Frobenius bound
is sqrt10<4. This controls the frame all the way toward u=0;
there is no hidden exponentially ill-conditioned change of basis.

## 4. The exact matrix has only a harmonic RELATIVE error

Let T_N(r) be the companion matrix from (7). In the shifted Z
coordinate, its coefficients are

\[
 p_N=-\frac{Z^{-1}(2Z^2+1+Q^{-1})}{(1-Z)^2},\qquad
 q_N=-\frac{Q^{-2}Z^{-2}(1-QZ^2)(1+QZ)}
                       {(1-Z)^2(1-QZ)}.               \tag{12}
\]

For N>=12 and r<R, u<=pi/3 and u+delta<pi/2. In particular
|1+Z|^2>=1 and

    |1-QZ|=2sin(u+delta)>=2sin u>=4(r+1)/N,
    |Q-1|<=2pi/N.

The difference in p is exactly -Z^(-1)(Q^(-1)-1)/(1-Z)^2.
For q use the elementary numerator identity

\[
 (1-QZ^2)(1+QZ)-(1+Z)^2(1-QZ)
                     =(Q-1)Z(2+Z-QZ^2).               \tag{13}
\]

Dividing by rho>=c=|q_0| gives the uniform estimates

    |p_N-p_0|/rho<=2pi/(r+1),
    |q_N-q_0|/rho<=6pi/(r+1).

Hence

\[
 \|T_N(r)-T_0(u)\|_2\leq\frac{8\pi}{r+1}\rho(u).      \tag{14}
\]

Large absolute entries near r=0 have NOT been called small. They
are controlled relative to the full eigenvalue envelope, whose
large second branch is kept. Combining (11), (14) and the step
u->u+delta proves

\[
 \|V(u)^{-1}T_N(r)V(u+\delta)\|_2
       \leq\rho(u)\left(1+\frac{128}{r+1}\right).       \tag{15}
\]

Indeed the frame change contributes at most8pi/N; the error term
contributes at most16sqrt2*pi/(r+1). Their sum is less than
128/(r+1). This argument uses a full operator-norm bound and
therefore allows arbitrary mixing of the two characteristic
branches; it does not posit adiabatic survival of either one.

## 5. Selected high-index boundary to all-index estimate

Write X_r=(U_r,U_(r+1))^T and X_r=T_N(r)X_(r+1).
For N>=12 both R and R+1 are within the high range in (2).
Thus ||X_R||<=2sqrt2 N. Iterating (15), using (11) at both ends,
gives

\[
 |U_r|\leq8N
  \prod_{j=r}^{R-1}\rho((j+1)\pi/N)
                \left(1+\frac{128}{j+1}\right).        \tag{16}
\]

The second product is at most exp(128 H_N)<=e^128 N^128.
The logarithm of the first is the RIGHT Riemann sum of the
nonnegative decreasing function max(0,2log cot u). Even for r=0
it is bounded ABOVE by its finite improper integral:

    sum_(j=r)^(R-1) log rho((j+1)pi/N)
       <=(N/pi) integral_(pi*r/N)^(pi/4) 2log cot u du
       =N E(pi*r/N).

This proves (5) for r<R. Equation (2) proves it for r>=R.
The argument is uniform at all indices, with no epsilon-dependent
unstated endpoint constants.

In particular, after the existing uniform sine-factorial estimate
for D_r is applied, the whole coherent inner packet has precisely
the two-branch upper envelope. Its lower-index excess is E(u);
it is NOT assumed to be zero. Whether the positive outer Newton
profile absorbs that excess is a separate variational inequality.
This theorem supplies the source-faithful estimate needed for that
comparison; it does not alone prove augmented-base survival, a
volume LOWER bound, or a filling theorem.

## 6. Validation

The [audit](../experiments/audit_actual_pretzel_all_index_backward_envelope.py)
checks the original finite sum, selected Ward boundaries, exact
normalized recurrence and endpoint cancellation, both high-range
anchors, shifted coefficient differences, uniformly conditioned
moving frame and its one-step bound, and the full coherent
all-index envelope at both parities. Tests never replace the
selected solution by an arbitrary recurrence branch.
