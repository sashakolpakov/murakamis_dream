# Angle profiles for the first-collar source

Research deduction, 5 November 2026. The original full row sum gives a
concave profile in the second real coordinate, replacing the angle-uniform
ceiling in the first-collar comparison. For a second type-three coordinate,
the profile pays its entire height attenuation together with the already
proved next-edge allowance. For an unselected second type-four coordinate,
its complete first halfweight is retained. The resulting boundary test is
one-dimensional; in the type-three case its maximizer solves an explicit
cubic. No sign for this calibrated test at every actual open reference is
asserted. There is no new root search or parameter cover.

## 1. Literal rows and the profiles

Put \(P=[11/50,9/20]\), and use the original notation
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\quad J(x)=\Re g(x).
\]
For \(x\in P\), \(Y=e^{-2\pi i(x+ik)}\), define
\[
 \begin{split}
 I_k(u,x)&=\int_0^u\log|1-e^{2\pi k-2\pi i(x+t)}|\,dt,\\
 R_\beta(u,x,k)&=I_k(u,x)-(1+\beta)J(u),\qquad 0\le u\le1.
 \end{split}
 \tag{1}
\]
At the exact first seam,
\[
 C_{\beta,N}(1,Y)=\sum_{j=0}^{N-1}\frac{p_j(Y)}{P_j^{1+\beta}}.
 \tag{2}
\]
Every row in (2) remains present. The uniform zero-safe product estimates
of the [whole seam bound](research_mixed_boundary_strip_bounds.md) and
[angle-dependent endpoint support](research_mixed_all_endpoint_support.md)
bound its absolute row sum by a polynomial times
\(\exp\{N\max_u R_\beta(u,x,k)\}\). The estimates include
both level parities, wrapped factors, the endpoints \(u=0,1\), and
the zeros present when \(k=0\).

The two profiles used below are
\[
 \begin{split}
 S_0(x)&=-2J((1-x)/2)-J(x),\\
 S_1(x)&=\max_{0\le u\le1/4}
       \{J(x+u)-\tfrac32J(x)-2J(u)\}.
 \end{split}
 \tag{3}
\]
They are genuine triangle upper bounds for the finite source, not
continuations of a local conditional saddle. In particular the stronger
identity \(C_{0,N}(1,Y)=Nd_N(Y)\) is not extrapolated to a fixed
collar. The profile in (3), rather than that cancellation, will survive
the collar estimate.

## 2. A reflection that retains all upper rows

Let \(k\le0\), \(R=e^{2\pi k}\le1\), and
\(0\le v\le1/2\). Jensen's identity over a full period gives
\(I_k(1,x)=0\), including \(R=1\) by continuity. Hence
\[
 I_k(1-v,x)-I_k(v,x)
 =-\int_{x-v}^{x+v}\log|1-Re^{-2\pi it}|\,dt
 \le-2J(v).
 \tag{4}
\]
To justify the last bound uniformly in the radius, first take \(R=1\).
Among arcs of length \(2v\), the integral of
\(\log(2|\sin\pi t|)\) is smallest on the arc centered at zero,
where it is \(2J(v)\). This follows by the elementary rearrangement
of a function increasing with distance from the nearest integer. For
\(R<1\), the arc integral is the Poisson average of these boundary
arc integrals, and so has the same lower bound. Their integrable boundary
zeros give continuity at \(R=1\).

Since \(J(1-v)=-J(v)\), (4) implies
\[
 R_\beta(1-v,x,k)-R_\beta(v,x,k)
                    \le2\beta J(v)\le0.
 \tag{5}
\]
Any factor depending only on \((x,k)\), such as the second Fourier
halfweight, cancels in this comparison. Thus the complete upper-half
row supremum is bounded by the lower-half one. No individual finite
upper row is asserted to vanish off the physical grid.

## 3. Negative heights are bounded by the zero-height profile

**Lemma 1.** Uniformly for \(x\in P\):

* If \(-.102\le k\le0\), then
  \(\max_u R_0(u,x,k)\le S_0(x)\).
* If \(-.102\le k\le0\), then the unselected source
  \(|C_{1,N}(1,Y)|\,|d_N(Y)|^{1/2}\) has upper rate at most
  \(S_1(x)\), with an arbitrarily small prescribed Fourier tolerance.

*Proof.* Write \(\theta=2\pi u\). The sign of
\(\partial_uR_0\) is the sign of
\[
 D(u)=R^2-1+2(1-R\cos2\pi x)\cos\theta
                    +2R\sin2\pi x\sin\theta.
 \tag{6}
\]
On \(0\le\theta\le\pi\), its trigonometric part first
increases and then strictly decreases. Its values at the two ends
have signs \(+,-\). Thus there is a unique maximum on the lower
half. At \(u_0=(1-x)/2\),
\(D(u_0)=(R-1)(R+1+2\cos\pi x)\le0\), so its maximizing
row lies at \(u\le u_0\).

For those rows every numerator argument satisfies
\(x+t\in[.22,.725]\), where
\(\cos(2\pi(x+t))<1/5\). Also
\(R\ge e^{-.204\pi}>1/2\); the latter follows from
\(.204\pi<2/3<\log2\). Therefore
\[
 \partial_k\log|1-Re^{-2\pi i(x+t)}|
  =\frac{2\pi R\{R-\cos(2\pi(x+t))\}}
                {1+R^2-2R\cos(2\pi(x+t))}>0.
 \tag{7}
\]
Raising the height to zero increases the numerator integral at every
possible maximizing row. At zero height the unique maximizing row is
\(u_0\), and its value is \(S_0(x)\), using
\(J((1+x)/2)=-J((1-x)/2)\). Equation (5) supplies all other
rows. This proves the first assertion.

For \(\beta=1\), every lower row \(u\in[1/4,1/2]\)
has
\[
 \partial_uR_1
 =\log|1-Re^{-2\pi i(x+u)}|-2\log(2\sin\pi u)\le0,
\]
because the numerator is at most two and the squared denominator
is at least two. Thus a maximum occurs in \([0,1/4]\).
Its numerator arguments lie in \([.22,.70]\), so (7) applies
throughout the type-four height interval too.

The actual unselected Fourier upper rate is
\(\tfrac12\max\{-\Re g(x+ik),0\}\). It is precisely
\(-\Re g(x+ik)/2\) here: for \(R\le1\) and
\(0<x<1/2\), the radial integral for the dilogarithm gives
\(\Re g(x+ik)<0\). Its height derivative is
\(\Im g'(x+ik)/2>0\), since
\(1-Re^{-2\pi ix}\) has positive imaginary part on the original
logarithm branch. This halfweight also increases to height zero.
The resulting zero-height maximum is exactly \(S_1(x)\).
The full Fourier theorem retains its forcing alternative in taking
this upper bound; it is not replaced by an equality of finite weights.
\(\square\)

## 4. Positive type-three attenuation and the next edge

For an actual second type-three reference let \(c\le.068\)
be its height, and use the already proved next-edge allowance
\[
 a_c(k)=0\quad(c\le k\le0),\qquad
 a_c(k)=\pi(c-k)\quad(0\le k\le c).
 \tag{8}
\]
The first alternative is for \(c\le0\), the second for
\(c\ge0\). The allowance is for the complete conditional source
on the explicit reference-height source domain in the
[horizontal completion theorem](research_mixed_first_collar_horizontal_completion.md),
or at the unchanged third reference in the
[type-three transport theorem](research_mixed_three_first_source_transport.md).

**Lemma 2.** For \(x\in P\), \(-.065\le c\le.068\), and
\(k\) between \(c\) and zero,
\[
                   \max_uR_0(u,x,k)+a_c(k)
                            \le S_0(x)+\pi c_+.
 \tag{9}
\]

*Proof.* Only \(0\le k\le c\) remains. Now
\(1\le R=e^{2\pi k}<77/50\), and
\(\cos2\pi x<1/5\) on \(P\). Consequently (6) has
\(D(0)>0\) and
\(D(1/2)<(77/50)^2-3+2(77/50)/5=-31/2500<0\).
Its cosine and sine coefficients are positive. Over a full period
it therefore has exactly two zeros: a lower-half maximum and an
upper-half minimum. The global maximum of \(R_0\) is at the
first critical row or the endpoint \(u=1\), whose value is
\(2\pi k\). The radial reciprocal identity gives
\(I_k(u,x)=2\pi ku+I_{-k}(u,x)\). At the first critical row
\(u<1/2\), Lemma 1 bounds its value by \(S_0(x)+\pi k\).
Thus the left side of (9) is at most
\(\max\{S_0(x)+\pi c,2\pi c\}\).

For clarity all scalar estimates needed to remove the second branch
are elementary. Use the trial row \(u=1/4\) at height zero.
On \([x,x+1/4]\subset[.22,.70]\), the logarithm
\(\log(2\sin\pi t)\) is positive, and is at least
\(\tfrac12\log2>1/3\) on a subinterval of length at least
\(.22\). Also
\(-J(1/4)=G/(2\pi)>14/99\), where the alternating Catalan
series gives \(G>1-1/9=8/9\), and \(\pi<22/7\).
Therefore
\[
 S_0(x)>\frac{14}{99}+\frac{11}{150}
       =\frac{1063}{4950}>\frac{17\pi}{250}\ge\pi c.
 \tag{10}
\]
Finally \(R<77/50\) used above follows without a decimal
evaluation: \(2\pi k\le17\pi/125<374/875\), and
\(e^t\le1+t+t^2/[2(1-t/3)]<77/50\) at
\(t=374/875\). The exponential bound follows from
\(n!\ge2\,3^{n-2}\) for \(n\ge2\).
Equations (9)--(10) follow. \(\square\)

## 5. A fixed-collar source bound, with its actual allocations

Take \(0<\rho\le1/1000\),
\(X=e^{-2\pi ix_1}\), \(0\le x_1\le\rho\),
and retain the literal first pair
\[
 \mathcal A_{\alpha\beta,N}
 =|U_{\alpha,N}(w,X)C_{\beta,N}(X,Y)|
       |d_N(X)^\alpha X^{-N\sigma_1}|\,|d_N(Y)|^{\beta/2},
 \qquad \sigma_1\in\{0,\alpha\}.
 \tag{11}
\]
The second coordinate is unselected. For type three this is the only
selection; for type four it is a genuine restriction of this note.
The first selected monomial has modulus one because \(x_1\) is real.
Set
\[
 b_0=101/125,\quad b_1=433/500,\qquad
 C_\alpha(\rho)=2\Delta_\rho+\alpha\omega_\rho,
 \quad\Delta_\rho=\rho\log2-J(\rho),
 \tag{12}
\]
where \(\omega_\rho\downarrow0\) is the established true
Fourier ceiling at the first real collar.

The exact collar product bound
\(|p_j(X)|/|P_j|\le\operatorname{poly}(N)e^{N\Delta_\rho}\)
holds for every row. The factor \(X^{-j}\) has unit modulus.
Combining it with the
[refined cap bound](research_mixed_cap_seam_source_bounds.md)
and Lemmas 1--2 gives, for every prescribed \(\eta>0\),
\[
 \begin{array}{ll}
 \displaystyle
 \mathcal A_{\alpha0,N}
 \le C_\eta N^A\exp N\{b_\alpha+C_\alpha(\rho)
                        +S_0(x)+\pi c_+-a_c(k)+\eta\},
       &k\text{ between }c\text{ and }0,\\[2mm]
 \displaystyle
 \mathcal A_{\alpha1,N}
 \le C_\eta N^A\exp N\{b_\alpha+C_\alpha(\rho)+S_1(x)+\eta\},
       &-.102\le k\le0.
 \end{array}
 \tag{13}
\]
These bounds are uniform for \(x\in P\), both parities, and a
fixed sufficiently small ordinary-color neighborhood. The neighborhood
is chosen before \(N\), using the cap's already proved color
uniformity. Every fixed ordinary-color derivative follows on a smaller
disk. No derivative of the half-modulus weight is asserted.

The zero-safe row integrals, and the maximum of the two Fourier rate
branches, are jointly continuous on this compact family. Thus their
uniform estimates concern the fixed collar in (13), including revived
rows and zeros. They do not use continuity of finite functions to choose
an \(N\)-dependent collar. At the exact seam the neighboring cutoff
is still one; no artificial height reset has been imposed.

## 6. Concavity and the calibrated scalar completion

The type-three profile has
\[
 S_0'(x)=-\log(2\sin(\pi x/2)),\qquad
 S_0''(x)=-\tfrac\pi2\cot(\pi x/2)<0.
 \tag{14}
\]
For type four the function in (3) is jointly strictly concave in
\((x,u)\in P\times(0,1/4]\). Indeed
\(J(x+u)-J(x)-J(u)\) has the negative real triangle Hessian,
and the remaining terms are \(-J(x)/2-J(u)\), with positive
own cotangents. Its maximizer has \(u>0\) and is unique; the
partial maximum \(S_1\) is strictly concave in \(x\). Write
\(t=\cot\pi u\ge1\), \(p_x=\cot\pi x\). Its row equation is
\[
 \sin^2(\pi x)(t+p_x)^2(1+t^2)=4,
 \qquad
 S_1'(x)=2\log(2\sin\pi u)-\tfrac32\log(2\sin\pi x).
 \tag{15}
\]
The left side of the equation is strictly increasing in \(t\ge1\),
and at one it is \(2(\sin\pi x+\cos\pi x)^2\le4\).
This specifies the correct unique quartic branch, with no row grid.

Now assume the complete-source and first-wire hypotheses of the
[horizontal energy theorem](research_mixed_horizontal_boundary_energy.md).
Write the actual second reference as \(a+ic\), let \(p=\Re P_2\)
be the original first-pair marginal, and retain its original allocated
action \(M_{12}\). Explicitly the complex pair phase is
\(\mathcal T_\alpha(r_1,-2)+\phi_{0\beta}(r_1,r_2)-\alpha g(r_1)\).
Its first tangent vanishes; its second tangent is \(P_2\).
Let \(G_c(y)=\Re g(y+ic)\) and
\(B_c(y,a)=G_c(y)-G_c(a)-G_c'(a)(y-a)\), exactly as in
that theorem. Put
\[
 \lambda=1+\beta/2,\qquad
 A_0(c)=\pi c_+,\qquad A_1(c)=13/2000.
 \tag{16}
\]
The type-four constant is the complete next-edge fixed-contour
allowance, not a new cost for the halfweight already in (11).
Combining (13) with the post-pair energy gives the following sufficient
test for a strict first-collar loss:
\[
 \boxed{\quad
 b_\alpha+C_\alpha(\rho)+A_\beta(c)
 +\max_{y\in I}\{S_\beta(y)-p(y-a)-\lambda B_c(y,a)\}
                         <M_{12}.
 \quad}
 \tag{17}
\]
Here \(I\subset P\) is any closed interval containing the actual
second-coordinate projection. The source hypotheses remain imposed
on the original correlated horizontal domain, not on an independent
product of plateau intervals. After (17), choose one total source and
ordinary-color tolerance below its strict reserve. The retained later
energy \((\pi/16)\sum_{j\ge3}d_j^2\) is not charged again.

For \(\beta=0\), even the scalar maximization in (17) is explicit.
Let \(R=e^{2\pi c}\), \(D_y=|1-Re^{-2\pi iy}|\). The derivative
of its strictly concave objective vanishes exactly when
\[
 2\sin(\pi y/2)D_y=D_a e^{-p}.
 \tag{18}
\]
The left side is strictly increasing for \(0<y<1/2\). If its value
at the left end of \(I\) is at least the right side, that end is
the maximizer; if its value at the right end is at most the right
side, the right end is the maximizer. Otherwise there is one root
inside \(I\), and it is the maximizer.
Writing \(t=\cos\pi y\), its square is the cubic equation
\[
 2(1-t)\{(1+R)^2-4Rt^2\}=D_a^2e^{-2p}.
 \tag{19}
\]
For \(\beta=1\), (15) and the strictly decreasing derivative
\(S_1'(y)-p-\tfrac32(G_c'(y)-G_c'(a))\) similarly specify
a unique clipped scalar candidate.

Thus the angle-uniform first-pair ceiling is unnecessary on these
physical height paths. The result supplies a sharper actual-source
criterion; it does not establish its sign for every geometry, enlarge
the admitted post-pair source domain, or remove the middle completion
and boundary pinning conditions of the global reduction. Selected
second-four coordinates are not included in (13) or (17).

