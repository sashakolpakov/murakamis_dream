# Explicit Gevrey bounds for the original all-root Verma source

Private written proof, 17 November 2026. This note estimates the
same ordinarily pivoted, untruncated graded cut source as [R].
It proves Gevrey-1 bounds at every fixed root, on compact meridian
sets away from its explicit determinant poles. All constants are
given in terms of the word, the meridian annulus, the grading
range, the determinant minimum, and the level N.

The small-grading estimate is uniform in N. Continuing it to
grading one gives a coarser type which can grow exponentially
in N even at the complete meridian. The resulting Borel transform
is locally analytic. No Borel continuation, Laplace summation,
selected-cycle coefficient, or volume lower bound is asserted.

## 1. Source, parameters, and the bound

Fix a braid beta on b>=2 strands whose permutation is one cycle.
Let ell be its number of signed crossings, w its writhe, and put
m=b-1 and c=b-1-w. For N>=2 set
\[
 q_0=e^{\pi i/N},\quad Q_0=q_0^2,\quad
 \delta=1-Q^N,\qquad q=q_0(1-\delta)^{1/(2N)}.
                                                               \tag{1}
\]
The branch at delta=0 is used. Initially x is held fixed. The
literal checked entries from [R, (2)] are
\[
\begin{split}
 R^+_{v+n,u-n;\,u,v}
 &=x^{-u-v+n}Q^{(u-n)v}{u\brack n}_Q
                         (x^{-2}Q^{u-n};Q)_n,\quad 0\le n\le u,\\
 R^-_{v-n,u+n;\,u,v}
 &=x^{u+v-n}Q^{-uv}{v\brack n}_Q
                         (x^2Q^{1-v};Q)_n,\quad 0\le n\le v.
\end{split}                                                    \tag{2}
\]
They are Laurent polynomials; no root-zero factorial is divided.
Their product in the given word order is B_beta. Retain exactly
\[
 V_\beta(q,x;\tau)=x^c
 \sum_{a_2,\ldots,a_b\ge0}\tau^T Q^{-T}
 \langle0,a_2,\ldots,a_b|B_\beta|0,a_2,\ldots,a_b\rangle,
 \qquad T=\sum_{i=2}^b a_i.                                    \tag{3}
\]
Every grading coefficient is finite. Write V_j=[delta^j]V_beta,
first coefficientwise in tau.

For k=x^N use the embedded matrices
\[
 L_+(k)=\begin{pmatrix}1-k^{-2}&k^{-1}\\k^{-1}&0\end{pmatrix},
 \qquad
 L_-(k)=\begin{pmatrix}0&k\\k&1-k^2\end{pmatrix}.
\]
Let A_beta be the first-row-and-column deletion of their product
L_beta and set
\[
 D_N(x,\tau)=\det(I-\tau^N A_\beta(x^N)).
                                                               \tag{4}
\]
The source theorem [R] gives
\[
 V_j(x,\tau)=\frac{P_j(x,\tau)}{D_N(x,\tau)^{2j+1}},
 \qquad P_j\in\mathbb Q(q_0)[x^{\pm1},\tau].
                                                               \tag{5}
\]
At tau=1, D_N=x^{Nc}Delta_K(x^{2N}), with the original normalized
Alexander polynomial. Thus the poles in the estimates below are
specified classical determinant poles, not an unknown source norm.

Choose X>=1, 0<rho<=1/4, and 0<r<1. Define
\[
\begin{gathered}
 A_X=Xe^{2\rho}(2+X^2e^\rho),\qquad
 t_0=rA_X^{-\ell},\qquad \sigma=-\tfrac12\log r,\\
 K_0=X^{|c|}e^{\rho+\sigma}(1-\sqrt r)^{-m},
 \qquad K_1=(\rho\sigma)^{-1},\qquad
 H=(1+3^\ell r^2)^m.                                           \tag{6}
\end{gathered}
\]
In particular t0<1 and all these constants are independent of N.

**Theorem.** On X^(-1)<=|x|<=X and |tau|<=t0,
\[
                         |V_j(x,\tau)|\le K_0 K_1^j j!.
                                                               \tag{7}
\]
For any compact target set E_N in that annulus, with |tau|<=T_max
and
\[
 d_N=\inf_{(x,\tau)\in E_N}|D_N(x,\tau)|>0,\qquad
 L=\max(2,T_{\max}/t_0),\qquad d_0=m(N-1),
\]
one has the explicit continuation estimate
\[
 |V_j(x,\tau)|\le
 \underbrace{2K_0H d_N^{-1}L^{d_0}}_{\mathcal K_N}
 \left(
 \underbrace{K_1H^2d_N^{-2}L^{2Nm}}_{\mathcal C_N}
 \right)^j j!.
                                                               \tag{8}
\]
The same assertions hold for quantum normals at fixed original
meridian M=-qx, and hence at fixed Y=M^2, after replacing X
everywhere in (6) by X exp(rho); in this version X bounds the
root coordinate x0=-M/q0 and D_N in (8) is evaluated at x0.
Section 5 proves this separate normal-path statement.

For b=1 the word is empty and (3) is 1. That case is immediate
and does not require the constants involving m in the proof.

## 2. Actual finite-sector estimate

Fix a total index T. Each intermediate index in (2) lies between
0 and T. Work on the complex disk
\[
                         |\delta|\le\frac{\rho}{T+1}.
                                                               \tag{9}
\]
Here
\[
 |\log|Q||\le\frac{|\log(1-\delta)|}{N}
       \le\frac{4\rho}{3N(T+1)}
       \le\frac{2\rho}{3(T+1)}.                                \tag{10}
\]
The Gaussian polynomial {u choose n}_Q has nonnegative integer
coefficients, sum binom(u,n), and degree n(u-n). These facts
follow by induction from the finite q-Pascal recurrence, including
the endpoint polynomials 1. Consequently its modulus on (9) is
at most
\[
                 {u\choose n}\exp(\rho T/6),
\]
since n(u-n)<=T^2/4. The same estimate holds with v in place of u.
Each Cartan factor in (2) has modulus at most exp(rho T/6):
both (u-n)v and uv are at most T^2/4.

Every exponent of Q in either displayed color product has
absolute value at most T. Therefore each such factor has modulus
at most 1+X^2 exp(rho). The x monomial outside that product has
modulus at most X^T. Summing absolute entries over the allowed
transfer n in one input column, the ordinary binomial theorem
gives
\[
 \sum_{\text{outputs}}|R^\pm_{\text{output};\,\text{input}}|
 \le X^T e^{\rho T/3}(2+X^2e^\rho)^T
 \le A_X^T.                                                    \tag{11}
\]
This is the induced column-sum norm on the finite total-T sector.
It includes the actual negative crossing, not an estimate of an
inverse matrix norm. Spectator indices do not change (11).

The column-sum norm is submultiplicative, so
\[
                         \|B_\beta\|_{1,T}\le A_X^{\ell T}.
\]
The ordinary pivot has |Q^(-T)|<=exp(rho), by (10). There are
binom(T+m-1,m-1) closed input tuples in (3). Thus, writing
v_T=[tau^T]V_beta, on (9) one obtains
\[
 |v_T(\delta,x)|\le
 X^{|c|}e^\rho {T+m-1\choose m-1}A_X^{\ell T}.                  \tag{12}
\]
This estimate retains both the word normalization x^c and the
varying pivot. It is valid also at T=0.

Cauchy's coefficient estimate in the disk (9) now gives
\[
 |[\delta^j]v_T|\le
 X^{|c|}e^\rho {T+m-1\choose m-1}A_X^{\ell T}
                  \left(\frac{T+1}{\rho}\right)^j.              \tag{13}
\]
For every nonnegative integer j and positive sigma,
\[
             (T+1)^j\le j!\,\sigma^{-j}e^{\sigma(T+1)}.
\]
Multiply (13) by |tau|^T, use |tau|A_X^ell<=r, and sum T.
Since r exp(sigma)=sqrt(r),
\[
 \sum_{T\ge0}{T+m-1\choose m-1}(r e^\sigma)^T
                          =(1-\sqrt r)^{-m}.
\]
This proves (7), with absolute locally uniform convergence of
each coefficient series in tau. It does not interchange an
infinite grading sum with an analytic delta germ on a fixed
nonzero disk: the sector disks (9) shrink with T.

## 3. Degree of the exact numerator

The rationality proof in [R, Sections 3--5] supplies the following
useful quantitative refinement:
\[
                    \deg_\tau P_j\le d_0+2jNm.
                                                               \tag{14}
\]
Here is the full degree argument, so no coefficient-size estimate
is being inferred from rationality alone.

For any traced finite-head path, its original head grading is
between 0 and m(N-1). After the closed carries have balanced,
the Frobenius insertion is a degree-zero polynomial differential
operator of order d<=2j. By normal ordering, it is a linear
combination of products of at most d vector fields Z_i partial_j.
In the actual cut trace each such vector field becomes a matrix
directional derivative of
\[
            \det(I-zL_\beta T_0)^{-1},\qquad
 z=\tau^N,\quad T_0=\operatorname{diag}(0,1,\ldots,1).
\]
All the varying matrices have zero first column, because the
directions are left substitutions before L_beta T0. Every
determinant in these directions therefore has z-degree at most
m, including all of its parameter derivatives.

A derivative of the reciprocal determinant of total order d
has denominator D_N^(d+1) and numerator of z-degree at most md.
This follows directly by induction using the quotient rule:
a further derivative multiplies a previous numerator derivative
by D_N or multiplies it by a derivative of D_N. Passing to
denominator D_N^(2j+1) adds degree at most m(2j-d). Thus its
z-degree is at most 2jm. Multiplication by the head grading proves
(14). Finite sums preserve the bound. The cancellation of
temporary x-only factors in [R, Section 5] does not increase
tau degree.

This reasoning uses the actual first-coordinate projector.
Neither T0 nor the deleted Burau matrix is inverted.

## 4. Propagation in the grading variable

On the x annulus, the row-sum norm of each embedded classical
matrix satisfies
\[
 \|L_\pm(x^N)\|_\infty\le3X^{2N},\qquad
 \|A_\beta(x^N)\|_\infty\le3^\ell X^{2N\ell}.
\]
Every eigenvalue is bounded by this norm. Since A_X>=X^3 and
N>=2, on |tau|=t0 we have
\[
 |\tau|^N\|A_\beta(x^N)\|_\infty
 \le3^\ell r^N(X^2/A_X)^{N\ell}\le3^\ell r^2.
\]
It follows that
\[
                       |D_N(x,\tau)|\le H
                        \quad (|\tau|=t_0).                   \tag{15}
\]
No small-circle lower bound on D_N is required.

By (5), (7), and (15), the polynomial P_j satisfies
\[
       \sup_{|\tau|=t_0}|P_j(x,\tau)|
                       \le K_0K_1^j j! H^{2j+1}.               \tag{16}
\]
Equation (5) initially holds near tau=0. Since (7) gives its
holomorphic coefficient series on the small disk, its product
with D_N^(2j+1) agrees with P_j there, so (16) also holds if the
chosen circle contains removable determinant zeros.

For a polynomial p of degree at most d, Cauchy's estimate for
its coefficients gives, when |tau|<=T_max and
L=max(2,T_max/t0),
\[
 |p(\tau)|\le
 \sup_{|s|=t_0}|p(s)|
 \sum_{k=0}^d(|\tau|/t_0)^k
 \le2L^d\sup_{|s|=t_0}|p(s)|.                                 \tag{17}
\]
Apply (17) to (16), use (14), and divide by |D_N|^(2j+1).
This is exactly (8). Only the explicitly stated determinant
minimum enters the continuation cost.

## 5. Original meridian normals

Holding M=-qx fixed is a different operation from holding x
fixed. Put x0=-M/q0. The source on this normal path is
\[
 W_\beta(\delta,M;\tau)
       =V_\beta(q(\delta),x_0(1-\delta)^{-1/(2N)};\tau).
                                                               \tag{18}
\]
On each disk (9), both the modulus of the varying factor in x
and that of its inverse are at most exp(rho). Thus (11)--(13)
apply unchanged with X replaced by X exp(rho), uniformly for
X^(-1)<=|x0|<=X. They prove (7) for the coefficients W_j.

For completeness their rational continuation has the same
numerator-degree budget. At order j, the order-l fixed-x
coefficient in (5) receives at most k<=j-l Euler-x derivatives.
After k derivatives its denominator power is at most 2l+1+k,
and its numerator tau degree is at most
\[
                          d_0+(2l+k)Nm.
\]
The quotient rule gives this by adding at most Nm for each
derivative. Passing to common denominator D_N(x0,tau)^(2j+1)
adds at most (2j-2l-k)Nm. Thus the final numerator again has
degree at most d0+2jNm. Equations (15)--(17), with the enlarged
annulus constant, prove the asserted version of (8).

The exact x parity in [R] makes (18) even in M. Hence the same
statement holds locally and globally in the original squared
meridian Y=M^2. At tau=1 its possible finite meridian poles are
Delta_K(Y^N)=0, apart from Laurent powers. This section changes
the normal path explicitly; it does not identify the two sets
of fixed-coordinate coefficients.

## 6. Local Borel transform and the level cost

Use the convention
\[
       \mathcal B V_N(x,\tau;\xi)
                 =\sum_{j\ge0}V_j(x,\tau)\frac{\xi^j}{j!}.
                                                               \tag{19}
\]
On E_N, (8) proves locally uniform convergence and the bound
\[
 |\mathcal B V_N|
       \le\frac{\mathcal K_N}{1-\mathcal C_N|\xi|}
               \quad (|\xi|<\mathcal C_N^{-1}).                 \tag{20}
\]
Consequently this is a holomorphic Borel germ, jointly with the
meridian and grading on their pole-free open sets. The fixed-M
and fixed-Y versions follow from Section 5. Fixed ordinary
meridian derivatives can also be estimated by Cauchy on a
slightly larger compact pole-free set.

At the complete root coordinate x*=-q0^(-1), [R, (23)] gives
D_N(x*,tau)=1 for every tau. In particular at tau=1 take X=1,
T_max=1, d_N=1 in (8). For any fixed choices rho,r and the fixed
word, all constants except the displayed N powers are fixed:
\[
 \mathcal K_N=2K_0H L^{m(N-1)},\qquad
 \mathcal C_N=K_1H^2 L^{2Nm}.                                  \tag{21}
\]
The guaranteed Borel radius is therefore of the form
constant times exp(-constant N). The same conclusion holds
for the fixed original meridian at M=1, using X exp(rho).
This is an explicit bound, not an assertion that the actual
Borel radius has this decay.

Neither (20) nor (21) supplies Borel continuation along a ray,
growth bounds there, a Laplace sum representing the original
source, or estimates uniform enough to take N to infinity at
the geometric scale. They also do not prove divergence of the
delta series: Gevrey-1 is the upper bound established here.

## 7. Coverage, proof source, and limits

Gevrey statements for quantum knot series already exist.
Garoufalidis--Lê,
[“Gevrey series in quantum topology” (2008)](https://arxiv.org/abs/math/0609618),
Theorems 5--7, state the Gevrey property for the specified
Habiro/Kashaev series of knotted objects. Only their definitions
and theorem statements were consulted for coverage; their proof
is not used. No broad novelty claim for knot-series Gevrey
regularity is made.

The archived research_full_charge_grid_exponential_remainder
proves factorial remainder estimates in a different expansion,
namely 1/N on its specified compact charge/source contours.
It does not supply the finite-sector estimate (12) or the
quantum-normal grading continuation here. It is coverage only,
not a proof premise.

The addition here is the explicit estimate for (3), including
its signed word, varying ordinary pivot, both normal-coordinate
choices, exact determinant pole dependence, and level cost.
Its sole complete proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| R | notes/research_all_root_verma_normal_rationality.md | 46e984e3ce5491ff82a18da6914d89a0e42393fd7e66877dc679190e69b125f6 |

R supplies the actual source and its rational continuation,
bounded closed-carry differential realization, original
meridian normalization, and complete-point determinant identity.
All source estimates, the numerator-degree refinement, and the
analytic continuation bounds used here are proved above.
No mathematical programs or tests are used.

