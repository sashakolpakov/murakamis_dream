# Complex third faces and near-opposite MAIN phases in the actual raw cofactor

The raw cofactor theorem applies to the original levels with the specified complex phases. It does not give a shared-volume comparison.

Inputs are the [exact nodal adapter](actual_cross_cofactor_global_angular_gap.md),
section 1; the [uniform complex determinant prefix bound](research_opposite_equal_triangle_determinant_bound.md),
(5a); and the [real integral identity and original interpolation](research_opposite_equal_raw_cofactor_bound.md).
The [full raw cofactor source](actual_cross_cofactor_factorization.md) fixes
the finite recurrence, both parity conventions and every unused factor.

## 1. Statement

Set theta=pi/N, J=floor((N-1)/2), j=J-k for a fixed k>=0. Use the
original cleared cofactor

\[
\begin{aligned}
R_j&=b^j\prod_{r<j}(a_r+u)+s_j^2(x+y)R_{j-1}
+s_js_{j-1}(a_{j-1}+u)xyR_{j-2},\\
a_r&=4\cos^2((r+\tfrac12)\theta),\qquad s_r=2\sin(r\theta),\qquad R_0=1.
\end{aligned}\tag{1}
\]

Absent negative indices are zero. Fix 0<c0<=C<=c1 and a compact set
of COMPLEX third-face values z. Define

\[
\mathcal J_C(z)=\frac1{2\pi}\int_0^\pi
\log\max\{|z+Ce^{it}|,|z+Ce^{-it}|\}\,dt.\tag{2}
\]

Then, uniformly on these compacts and both parities,

\[
\limsup_{N\to\infty}\ \sup_{\substack{C,z\\-4\le u\le0}}
\left\{\frac1N\log|R_{J-k}(-C,C,z;u)|-\mathcal J_C(z)\right\}\le0.\tag{3}
\]

The logarithm of a zero is -infinity. The same bound holds for a fixed
finite collection of k. A degree-j Bernstein extension adds exactly
2pi j |Im delta| when u=-4sin^2(pi delta).

There is also a near-opposite version. For complex x,b with
|x+C|+|b-C|<=h, there is a modulus omega(h)->0 such that

\[
\limsup_{N\to\infty}\ \sup_{\substack{C,z,x,b\\|x+C|+|b-C|\le h\\-4\le u\le0}}
\left\{\frac1N\log|R_{J-k}(x,b,z;u)|-\mathcal J_C(z)\right\}\le\omega(h).\tag{4}
\]

Thus after a common homogeneous phase rotation, (4) applies on an
actual torus whenever the two MAIN arguments have equal radii and
relative phase sufficiently close to pi, with ARBITRARY third-face
phase. No individual coefficient estimate is inferred.

## 2. The exact signed tail and its continuum roots

At every retained lower node u_a=-a_a, 0<=a<=j, the literal identity is

\[
R_j(-C,C,z;u_a)=S_{2a}D_a(-C,C,z)K_{a,j}(-C,z;u_a),
\qquad S_r=\prod_{v=1}^r s_v.\tag{5}
\]

The initial tail vector is (K_(a,a),K_(a,a-1))=(1,0). Its exact
transfer has coefficients

\[
\begin{aligned}
p_r&=s_r^2(z-C),&q_r&=s_rs_{r-1}(a_a-a_{r-1})Cz,\\
K_{a,r}&=p_rK_{a,r-1}+q_rK_{a,r-2}.
\end{aligned}\tag{6}
\]

For complex z there is NO positive sign gauge. Instead, with
alpha=a/N and alpha<=t<=1/2, the transfer converges uniformly on the
ENTIRE closed parameter triangle to [[p,q],[1,0]], where

\[
\begin{aligned}
p&=4(z-C)\sin^2(\pi t),\\
q&=16Cz\sin^2(\pi t)\bigl[\sin^2(\pi t)-\sin^2(\pi\alpha)\bigr].
\end{aligned}\tag{7}
\]

The convergence is O(1/N), uniformly on the stated C,z compacts.
No denominator occurs here. Write rho(t;alpha,C,z) for the maximum
modulus of the two roots of lambda^2-p lambda-q=0.

We will prove the uniform upper

\[
\limsup_{N\to\infty}\ \sup_{a,C,z}
\left\{\frac1N\log|K_{a,J-k}|-
\int_{a/N}^{1/2}\log\rho(t;a/N,C,z)\,dt\right\}\le0.\tag{8}
\]

This is an upper estimate, including zero tails. It does not choose
one scalar phase across a collision or a modulus crossing.

There is also an EXACT finite scalar Jacobi structure. For l=r-a,
normalize k_l=K_(a,a+l)/prod_(v=a+1)^(a+l)s_v^2. Then

\[
\begin{aligned}
k_0&=1,\qquad k_1=z-C,\\
k_l&=(z-C)k_{l-1}+\gamma_lCz\,k_{l-2},\\
\gamma_l&=1-\frac{s_as_{a+1}}{s_{a+l}s_{a+l-1}}\in[0,1],\qquad l\ge2.
\end{aligned}
\]

This is the actual trigonometric tail identity, not a new quantum
level. Formally, or for z!=0 using either square root, set

\[
k_l=(i\sqrt{Cz})^lP_l\!\left(\frac{z-C}{i\sqrt{Cz}}\right).
\]

The square roots cancel by parity. The P_l obey
P_0=1,P_1=w,P_l=wP_(l-1)-gamma_l P_(l-2). Hence P_l is the
characteristic polynomial of the REAL symmetric zero-diagonal Jacobi
matrix with adjacent entries sqrt(gamma_2),...,sqrt(gamma_l).
Its spectrum lies in [-2,2] by the row-sum bound. Pairing its opposite
eigenvalues shows that every zero of k_l as a polynomial in z lies
on |z|=C: each pair contributes
(z-C)^2+lambda^2 C z, and an unpaired zero contributes z-C.
At z=0 the polynomial identity holds by continuation. This proves a
scalar tail structure only; it is NOT a semisimple realization of the
original complete-colored Casimir or of arbitrary coupon observables.
The uniform upper below does not require an empirical zero limit.

## 3. A uniform slow-transfer upper that permits Jordan points

For a compact family of two-by-two matrices T with norm bounded by M,
Cayley-Hamilton gives, for every integer l>=1 and epsilon>0,

\[
\|T^l\|\le C_\varepsilon(l+1)\bigl(\rho(T)+\varepsilon\bigr)^l.\tag{9}
\]

Indeed, if its roots are lambda_1,lambda_2, the coefficient
(lambda_1^l-lambda_2^l)/(lambda_1-lambda_2) is the sum of l monomials,
and has modulus at most l rho^(l-1), also when the roots coincide.
The other Cayley-Hamilton coefficient is bounded by
(l-1)rho^l. Absorbing M/epsilon yields (9), including rho=0.

Divide the actual product into blocks of a FIXED length l. On a block
the factors converge uniformly to one frozen matrix as N grows,
because (7) is uniformly continuous and the finite coefficients have
uniform O(1/N) error. The difference of its block product and T^l is
o(1), uniformly in every parameter and the moving initial row a.
Since rho+epsilon>=epsilon, for fixed l it may be absorbed into the
right side of (9). Multiplication of the block norms gives

\[
\limsup_{N\to\infty}\frac1N\log\left\|\prod_r T_{N,r}\right\|
\le\int_\alpha^{1/2}\log\bigl(\rho(t)+\varepsilon\bigr)\,dt
+\frac{\log(2C_\varepsilon(l+1))}{l}.\tag{10}
\]

The incomplete blocks have bounded length and bounded norm. The
Riemann sums are uniform, since log(rho+epsilon) is continuous on
the compact parameter triangle. First let N tend to infinity, then
l tend to infinity. This proves (10) without its last term.

The epsilon removal is uniform. The root sum and product imply

\[
\begin{aligned}
\rho&\ge\frac{|p|}{2}=2\sin^2(\pi t)|z-C|,\\
\rho&\ge\sqrt{|q|}=4\sqrt{C|z|}\sin(\pi t)
\sqrt{\sin^2(\pi t)-\sin^2(\pi\alpha)}.
\end{aligned}\tag{11}
\]

If |z-C|>=C/2 use the first inequality; otherwise |z|>=C/2 and use
the second. Hence on every stated compact there is c>0 such that

\[
\rho\ge c\sin(\pi t)\sqrt{\sin^2(\pi t)-\sin^2(\pi\alpha)}.\tag{12}
\]

Together with the uniform upper bound, this gives uniform integrability
of log rho. Use
sin^2(pi t)-sin^2(pi alpha)
=sin(pi(t-alpha))sin(pi(t+alpha)); the moving logarithmic endpoints
have uniformly vanishing integrals on intervals of vanishing length.
Consequently the integral of log rho from alpha to 1/2 is continuous
jointly in alpha,C,z, including alpha=0,1/2 and z=0,C. The continuous
integrals of log(rho+epsilon) decrease uniformly to it by compact
monotone convergence. This proves (8). The missing fixed k terminal
rows change the integral by o(1) uniformly, by the same logarithmic
integrability; the finite product was always stopped at J-k.

## 4. Exact complex cancellation with the SYMMETRIC determinant action

Define

\[
\begin{aligned}
L(\alpha)&=\int_0^{2\alpha}\log(2\sin(\pi t))\,dt,\\
D_{\mathrm{sym}}(\alpha;z)&=\int_0^\alpha
\left[\frac12\log|z+Ce^{2\pi it}|+\frac12\log|z+Ce^{-2\pi it}|
-\log(4\cos^2(\pi t))\right]dt.
\end{aligned}
\]

Then the exact identity is

\[
L(\alpha)+D_{\mathrm{sym}}(\alpha;z)
+\int_\alpha^{1/2}\log\rho(t;\alpha,C,z)\,dt
=\frac12\log\max(C,|z|).\tag{13}
\]

Here all terms have their integrable endpoint values. We prove (13)
by a HOLOMORPHIC identity, not by equality of harmonic functions on a
real interval.

For t>alpha put w=z/C and

\[
\gamma=1-\frac{\sin^2(\pi\alpha)}{\sin^2(\pi t)},\qquad0\le\gamma\le1.
\]

After lambda=4Csin^2(pi t) r, the two roots satisfy

\[
r^2-(w-1)r-\gamma w=0.\tag{14}
\]

The discriminant w^2+(4gamma-2)w+1 has all its zeros on |w|=1.
When gamma>0 and the roots have equal modulus, their sum/product
give (w-1)^2/(-gamma w) in [0,4]. Thus w+1/w belongs to
[2-4gamma,2] subset [-2,2]. Off the unit circle, w+1/w can be real
only for real w, where it is outside this interval. Equality of
moduli is therefore impossible for |w|!=1. The case gamma=0 has
roots w-1 and zero and has the same conclusion away from w=1.

There is a holomorphic dominant root r_out on |w|>1, normalized by
r_out/w->1 at infinity, and a holomorphic nonzero root r_in on
|w|<1, with r_in(0)=-1. These are precisely the roots of largest
modulus there. The ratios r_out/w and -r_in have holomorphic
logarithms fixed to zero at infinity and at zero, respectively.
For positive real w>1, r_out is positive; for 0<w<1, r_in is
negative. These signs fix the imaginary constants that matter below.

Inside the circle, define the analytic determinant action by replacing
the pair of log moduli in D_sym with

\[
\log C+\frac12\operatorname{Log}(1+we^{2\pi it})
+\frac12\operatorname{Log}(1+we^{-2\pi it}),
\]

where the logarithms vanish at w=0. Define the tail action using
log(4Csin^2(pi t))+Log(-r_in). These expressions are holomorphic in
the disk and REAL for 0<w<1. On that interval, they are exactly the
real quantities in the real cancellation identity. Their
sum with L(alpha) therefore equals .5 log C as a complex identity
on a real interval. The identity theorem gives that equality on the
entire disk. Taking real parts proves (13) for |z|<C.

Outside the circle, the determinant action uses

\[
\operatorname{Log}z+\frac12\operatorname{Log}(1+w^{-1}e^{2\pi it})
+\frac12\operatorname{Log}(1+w^{-1}e^{-2\pi it}).
\]

The tail uses Log z+log(4sin^2(pi t))+Log(r_out/w).
The TOTAL coefficient of Log z is alpha+(1/2-alpha)=1/2.
Subtracting .5 Log z therefore gives a single-valued holomorphic
function on the exterior, including infinity. It is real and zero
on w>1 by the same real identity. The identity theorem
shows it is identically zero, proving (13) outside the circle.

The endpoint cases in alpha and the circle |z|=C follow by continuity.
For the tail use (12); for D_sym use uniform integrability of the
translated circle logarithm. Thus no lower bound or nonvanishing of
the finite determinants or tails has been introduced.

## 5. From the complex determinant upper to the SAME full envelope

The proved determinant prefix upper uses D_max rather than D_sym:

\[
D_{\max}(\alpha;z)=\int_0^\alpha
\left[\log\max\{|z+Ce^{2\pi it}|,|z+Ce^{-2\pi it}|\}
-\log(4\cos^2(\pi t))\right]dt.
\]

Their exact difference is

\[
E_\alpha(z)=\frac12\int_0^\alpha
\left|\log|z+Ce^{2\pi it}|-\log|z+Ce^{-2\pi it}|\right|dt.\tag{15}
\]

It is nonnegative and nondecreasing in alpha. Equation (13) therefore
gives the nodal upper action

\[
\begin{aligned}
L(\alpha)+D_{\max}(\alpha;z)+I_{\mathrm{tail}}(\alpha;z)
&=\frac12\log\max(C,|z|)+E_\alpha(z)\\
&\le\frac12\log\max(C,|z|)+E_{1/2}(z)=\mathcal J_C(z).
\end{aligned}\tag{16}
\]

For the last identity, the full symmetric determinant integral is
.5 log max(C,|z|), by the circle logarithmic mean, while its denominator
integral is zero. All identities include z=0 and the integrable zeros
on |z|=C. No real cancellation is continued after replacing an average
by a maximum without keeping its explicit extra term.

Combine (5), (8), the uniform determinant prefix upper and

\[
\frac1N\log S_{2a}=L(a/N)+O\!\left(\frac{\log N}{N}\right).
\]

This proves the uniform nodal upper J_C(z) for every 0<=a<=j.
The cofactor has spectral degree at most j. To include the k omitted
nodes of the full J+1-point Chebyshev/Radau grid, interpolate

\[
Q(u)=R_j(u)\prod_{a=j+1}^J(u-u_a).
\]

Its values vanish at the omitted nodes, and its retained values differ
by at most 4^k. The full-grid Lebesgue bound is O(log N). Successive
Markov derivative division by the k factors costs at most a fixed
power of N, also at the roots themselves. This proves (3). All
interpolation is in the genuine degree-j cofactor, not the full
degree-d Hermite numerator.

## 6. Uniform stability of the two MAIN arguments

We give the details needed for (4). The exact nodal identity (5) holds
for arbitrary x,b,z with the same S_(2a). The determinant remains
det[bI+(x/2)H_-+(z/2)H_+], and the homogeneous tail has coefficients
s_r^2(x+z), s_r s_(r-1)(a_(r-1)-a_a)xz.

First the determinant. On eta<=t<=1/2-eta, conjugate the perturbed
transfer by the BASE opposite-equal eigenvector matrices. Their gap
iC tan(pi t), inverse norms and derivatives have the same uniform
bulk control, including every compact complex z. The conjugated norm
is at most

\[
\rho_{D,\mathrm{base}}(t;C,z)+C_\eta h+O_\eta(N^{-1}).
\]

The base rho_D is bounded below on that interval. Hence the logarithmic
cost relative to its base action is at most C'_eta h N+o_eta(N).
The first and final eta N rows retain the same direct bound
O(eta N log(2/eta)+log N), uniformly in the perturbed coefficients.
For prefixes that stop in either endpoint portion, use the same
truncated estimate; the base omitted integrals are uniformly
O(eta log(2/eta)). Thus the perturbed determinant prefix has upper
action D_max(alpha;z)+omega_D(h), uniformly in all alpha, where

\[
\omega_D(h)\le\inf_{\eta>0}\{e(\eta)+C'_\eta h\},
\qquad e(\eta)\longrightarrow0,\qquad\omega_D(h)\longrightarrow0.\tag{17}
\]

Only sufficiently small eta are used; constants depend on the fixed
parameter compacts. No perturbed branch is followed through a crossing.

For the tail, its finite transfer again converges uniformly on the
whole closed triangle. Its limiting coefficients differ from (7) by
O(h). Roots of bounded monic quadratics move by at most O(sqrt h),
so their maximum modulus is at most rho_base+C sqrt h. Apply the
fixed-block argument (9)-(10) to the perturbed matrices, and keep the
base regularization in the resulting upper bound. After epsilon->0,
the tail upper action is at most

\[
\int_\alpha^{1/2}\log(\rho_{\mathrm{base}}+C\sqrt h)\,dt
\le I_{\mathrm{tail,base}}(\alpha)+\omega_K(h),
\qquad\omega_K(h)\longrightarrow0\text{ uniformly}.\tag{18}
\]

The last uniform convergence follows from precisely the continuity,
lower bound and compact monotone convergence proved after (12).
There is no assumption that a perturbed tail is positive or that
its own spectral radius has a uniform positive minimum.

The nodal factors S_(2a) are unchanged. Combining (16)-(18) and the
same exact spectral interpolation proves (4), with
omega=omega_D+omega_K. At each transfer estimate auxiliary parameters
are fixed before N tends to infinity and are then sent to their stated
limits. No N-dependent vanishing neighborhood is substituted for a
fixed face-phase neighborhood. The spectral Bernstein extension has
the same additional 2pi j |Im delta| at these perturbed face arguments.

## 7. The correct full third-face torus envelope

For r>=0 the explicit maximum of (2) on |z|=r is

\[
U_C(r)=\max_\phi\mathcal J_C(re^{i\phi})
=\frac1\pi\int_0^{\pi/2}\log|r+Ce^{it}|\,dt.\tag{19}
\]

For r>0,C>0, write g(t)=log|r+C exp(it)|. This is even and
decreasing on [0,pi]. In the upper half-plane J_C(r exp(i phi))
is (1/(2pi)) integral_(-phi)^(pi-phi) g(t)dt for 0<=phi<=pi.
Its derivative is [g(phi)-g(pi-phi)]/(2pi), so the maximum is at
phi=pi/2. Reflection gives the lower half-plane and the same value.
At r=0 the result follows directly. This proof includes r=C by
integrable limits at the isolated logarithmic zero.

Unlike the real-face formula, (19) generally exceeds
.5 log max(C,r). For example

\[
U_C(C)=\frac12\log C+\frac G\pi,\qquad
G=-\int_0^{\pi/4}\log\tan t\,dt>0.\tag{20}
\]

Thus the correct proven complex envelope has a nonzero phase cost.
Equation (20) is a property of this UPPER envelope; no matching lower
growth for the actual finite cofactor is claimed. It does not prove
that a sharper radial raw-cofactor upper is impossible.

Combining (4) and (19) gives an actual near-opposite-MAIN / arbitrary
third-phase torus estimate with rate U_C(r)+omega(h). All original
targets must still be extracted when this cofactor is used inside a
source. This note neither sums the other cofactor terms nor proves
that the resulting star envelope is at most Phi_D. It also makes no
claim that spectral interpolation preserves a local sector's matrix
covariance: only the exact cofactor polynomial is interpolated.

## scope

No numerical audit or asymptotic sampling is needed or claimed. This is
an upper bound for the original raw cofactor on the stated face and
spectral domains, not a coefficientwise source replacement, a lower
asymptotic, an absolute star or Phi_D comparison, or a filling theorem.
