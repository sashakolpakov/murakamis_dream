# Exact moderate analytic interpolation of physical row degree

Private written proof, 16 November 2026.

The original physical rows admit an exact analytic interpolation in
their degree on any fixed interval strictly between the endpoint and
the fold. Its size has the original row action, with polynomial loss.
The construction uses the attracting original Riccati equation, an
exponentially accurate discrete primitive, and a localized cardinal
correction. It does not substitute the off-grid full kernel.

The complex height is fixed independently of the level and is bounded
explicitly in terms of the contraction and analytic radii below.
There is one interpolant on the whole degree interval, so subdivision
does not introduce mismatched internal connector functions. The two
outer connectors retain their original action cost. No estimate at
the filled action, or permission to discard those connectors, follows.

The tail-weight extension below also interpolates the literal
terminating consumed-normal coefficient, retaining its action
\(-J_\delta\) and its checkerboard character. It uses a finite
prefix and an explicitly bounded error up to the actual physical
stop; no infinite off-grid tail is substituted.

## 1. Original rows, domains, and canonical action

Put \(N\ge3\), \(\theta=\pi/N\), and
\[
 c_j=2\cos((2j+1)\theta),\qquad
 F_{j,N}(Z)=K_N(c_j,Z),\qquad
 0\le j\le\lfloor(N-1)/2\rfloor .
 \tag{1}
\]
These are the literal physical rows, ordinary polynomials of degree
\(j\) in \(Z\). Their normalization is \(F_{0,N}=1\).
Fix
\[
 0<a<b<\tfrac12,\qquad
 \mathcal W=\{Z:\Re Z\le2-\gamma,\ |Z|\le R\},
 \quad \gamma>0,\ R<\infty .
 \tag{2}
\]
An empty \(\mathcal W\) can be omitted. All exterior derivative
statements use a larger bounded convex open domain
\(\mathcal V\) whose closure is in \(\{\Re Z<2\}\) and which contains
a fixed neighborhood of \(\mathcal W\). When needed, take one more
such enlargement. Every constant below is uniform on its stated
closed exterior domain.

The root-location theorem gives
\[
 F_{j,N}(Z)=\prod_{\nu=1}^j
                \frac{r_{j,\nu}-Z}{r_{j,\nu}-c_0},
 \qquad r_{j,\nu}>2.
 \tag{3}
\]
Thus every anchor used below is a holomorphic unit on \(\mathcal V\),
with the unique logarithm obtained by summing the logarithms of these
right-half-plane factors. It is real for real \(Z<2\). In particular,
anchoring at a physical row does not introduce an arbitrary logarithm
or an unproved nonvanishing assertion.

For real \(0<x<1/2\), put
\[
 p(x,Z)=2+(2-Z)\cot^2(\pi x),\qquad
 \lambda(x,Z)=\frac{p+\sqrt{p^2-4}}2 ,
 \tag{4}
\]
where the root is positive for real \(Z<2\).
On the exterior domain in (2), \(\Re p>2\), the branch is a unit,
and \(\Re\lambda>1\). On a sufficiently small fixed complex
neighborhood of any enlarged real degree interval inside \((0,1/2)\),
these assertions persist uniformly. Use its continued logarithm.
Define the canonical action by
\[
 \Psi(x,Z)=\int_0^x\operatorname{Log}\lambda(u,Z)\,du.
 \tag{5}
\]
The integral first follows the positive real axis and then continues
inside that simply connected degree neighborhood. It converges at zero:
\[
 \operatorname{Log}\lambda(x,Z)
   =\operatorname{Log}(2-Z)-2\log(\pi x)+O(x^2).
 \tag{6}
\]
The original row Riccati theorem, with precisely this normalization,
proves
\[
 \log F_{j,N}(Z)=N\Psi(j/N,Z)+O(\log N)
 \tag{7}
\]
uniformly on compact degree intervals below \(1/2\), with every fixed
exterior derivative. This is the original edge action
\(\psi(\pi-2\pi x,u)\) when \(Z=-2\cos u\), calibrated by
\(\psi(\pi,u)=0\). The half-offset in the actual physical angle can
instead be retained; on the present bulk interval it changes (7)
only by a bounded analytic factor.

## 2. An analytic attracting ratio with exponential nodal accuracy

The exact recurrence is
\[
 \rho_{j+1,N}=\mathscr R_{N,j/N,Z}(\rho_{j,N}),\qquad
 \rho_{j,N}=F_{j,N}/F_{j-1,N},
 \tag{8}
\]
where
\[
 \begin{split}
 A_N(x)&=\frac{[2\sin(\pi x+\theta)]^4}
                   {4\sin(2\pi x+\theta)\sin(2\pi x+2\theta)},\\
 C_N(x)&=\frac{[2\sin(\pi x)]^4}
                   {4\sin(2\pi x)\sin(2\pi x+\theta)},\\
 q_N(x)&=C_N(x)/A_N(x),\qquad
 d_N(x,Z)=(c_0-Z)/A_N(x),\\
 \mathscr R_{N,x,Z}(z)&=1+d_N(x,Z)+q_N(x)(1-z^{-1}).
 \end{split}                                                   \tag{9}
\]
The symbol \(q_N(x)\) here is the Riccati coefficient, not the
cyclotomic root. On each fixed enlarged degree neighborhood,
\[
 A_N=\tan^2(\pi x)+O(N^{-1}),\quad q_N=1+O(N^{-1}),\quad
 d_N=(2-Z)\cot^2(\pi x)+O(N^{-1}).
 \tag{10}
\]
All these are uniform holomorphic estimates.

Here are precise choices of the constants needed later. Choose
\(d>0\) with \([a-4d,b+4d]\subset(0,1/2)\). Shrink a fixed complex
thickening of that interval until, on it and the larger exterior
domain, \(\Re p>2\) and \(\Re\lambda\ge1+3\kappa\) for some
\(\kappa>0\). For all large \(N\), arrange also
\(|q_N|\le1+\kappa\). On each disk
\(|z-\lambda(x,Z)|\le\kappa\), the maps in (9) have Lipschitz
constant
\[
 \vartheta=\frac{1+\kappa}{(1+2\kappa)^2}<1.
 \tag{11}
\]
Taylor's formula and (10) give a constant \(D_0\) such that
\[
 |\mathscr R_{N,x,Z}(\lambda(x,Z))
                     -\lambda(x+N^{-1},Z)|\le D_0/N.
 \tag{12}
\]
Put \(K_0=D_0/(1-\vartheta)\). After increasing the level threshold,
the moving disks of radius \(K_0/N\) are invariant: a point in the
disk centered at \(\lambda(x,Z)\) maps into the disk centered at
\(\lambda(x+N^{-1},Z)\).

Fix \(0<\sigma<d\), let \(m_N=\lfloor\sigma N\rfloor\), and define
\(R_N(x,Z)\) by starting with \(\lambda(x-m_N/N,Z)\) and applying
in order the \(m_N\) maps with degree arguments
\[
             x-m_N/N,\ x-(m_N-1)/N,\ldots,x-1/N.
 \tag{13}
\]
Reserve a fixed complex buffer for all these shifts. The construction
is holomorphic, and
\[
 |R_N-\lambda|\le K_0/N,\qquad \Re R_N>1+2\kappa.
 \tag{14}
\]
It applies on a fixed neighborhood of \([a-d,b+d]\).

At a physical degree \(x=j/N\), the actual ratio at the starting
index \(j-m_N\) is \(O(N^{-1})\) from its chosen root by the
original bulk Riccati theorem. The larger moving disks of radius
\(\kappa\) are also invariant for large \(N\), since
\(\vartheta\kappa+D_0/N<\kappa\). The actual initial ratio lies in
these disks; its \(O(N^{-1})\) constant need not be bounded by
\(K_0\). Contracting the two initial values through (13) proves
\[
 |R_N(j/N,Z)-\rho_{j,N}(Z)|
               \le C N^{-1}\vartheta^{m_N}.
 \tag{15}
\]
This comparison uses the normalized original solution, not merely
the existence of a formal characteristic root. The index \(j-m_N\)
remains in a fixed bulk interval, so the cited estimate applies
uniformly. The same estimate on larger exterior domains supplies
all fixed exterior derivatives by Cauchy.

Put \(l_N=\operatorname{Log}R_N\), using its right-half-plane
logarithm. On a fixed complex neighborhood it is uniformly bounded,
holomorphic, and
\[
 l_N=\operatorname{Log}\lambda+O(N^{-1}).
 \tag{16}
\]
Choose a radius \(r>0\) so that every degree point used next has
its closed \(r\)-disk in that neighborhood, including the shift
buffer already reserved. For a constant \(M\),
\[
                  |l_N^{(k)}|\le M k!r^{-k}.             \tag{17}
\]

## 3. An exponentially accurate analytic discrete primitive

Let \(j_0=\lceil Na\rceil\), \(x_0=j_0/N\), and put
\(p_N=\lfloor\pi rN/2\rfloor\). For sufficiently large \(N\)
define
\[
 \begin{split}
 \mathcal A_N(x,Z)={}&N\int_{x_0}^x l_N(u,Z)\,du
                  +\frac{l_N(x,Z)-l_N(x_0,Z)}2\\
 &+\sum_{k=1}^{p_N-1}
   \frac{B_{2k}}{(2k)!\,N^{2k-1}}
    [l_N^{(2k-1)}(x,Z)-l_N^{(2k-1)}(x_0,Z)],\\
 \widehat F_N(x,Z)={}&F_{j_0,N}(Z)\exp\mathcal A_N(x,Z).
 \end{split}                                                   \tag{18}
\]
The integral is the analytic primitive on the degree rectangle.
Thus \(\widehat F_N\) is a holomorphic unit, with its anchor and
logarithm fixed by (3).

We give the growing-order remainder explicitly. The bound
\(\sup|B_{2p}(\{\cdot\})|\le4(2p)!/(2\pi)^{2p}\), the
Euler--Maclaurin formula for a right-endpoint sum, and (17) give
\[
 \left|\mathcal A_N(j/N,Z)-
             \sum_{h=j_0+1}^j l_N(h/N,Z)\right|
 \le C N\,\frac{(2p_N)!}{(2\pi rN)^{2p_N}}.
 \tag{19}
\]
For clarity, apply the formula through its \(p_N\)-th endpoint
term and add the bound for that term when omitting it in (18).
It has the same or a smaller upper bound. The real interval of
integration has bounded length; \(Z\) can be complex throughout.
Since \(2p_N\le\pi rN\), the elementary inequality
\((2p_N)!\le(2p_N)^{2p_N}\) makes the right side exponentially
small. For all sufficiently large \(N\), it is at most
\(C\exp(-\kappa_{\rm EM}N)\), where one may take
\[
                       \kappa_{\rm EM}=\pi r\log2/4.
 \tag{20}
\]
This uses growing-order derivative bounds on a fixed complex
neighborhood; a fixed-order expansion would not suffice.

Equations (15) and (19), summed over at most \(N\) ratios, imply
\[
 \left|\frac{F_{j,N}(Z)}{\widehat F_N(j/N,Z)}-1\right|
                         \le C e^{-\kappa_0N},
 \quad j_0\le j\le j_1:=\lfloor Nb\rfloor,
 \tag{21}
\]
with, for example,
\[
 \kappa_0=\min\{\sigma|\log\vartheta|/2,\ \kappa_{\rm EM}\}>0.
 \tag{22}
\]
Constants and level thresholds absorb bounded prefactors.

The primitive also has a uniform complex growth bound. The terms
in (18) after the half-endpoint correction sum to \(O(N^{-1})\):
by (17), successive upper bounds have ratio at most \(1/4\)
up to \(p_N\), after increasing the threshold if necessary.
Consequently (16) yields, uniformly for \(x,y\) in a fixed smaller
degree rectangle,
\[
 \log\frac{\widehat F_N(x,Z)}{\widehat F_N(y,Z)}
                 =N[\Psi(x,Z)-\Psi(y,Z)]+O(1).
 \tag{23}
\]
The logarithm here is the difference of the defined primitives.
Using (7) at \(x_0\) gives
\[
 \log\widehat F_N(x,Z)=N\Psi(x,Z)+O(\log N),\qquad
 N^{-C}e^{N\Re\Psi(x,Z)}
 \le|\widehat F_N(x,Z)|\le N^Ce^{N\Re\Psi(x,Z)}.
 \tag{24}
\]
Enlarging a constant covers the omitted bounded factors.

## 4. One exact interpolant on the whole interval

Let \(L\) bound \(|\partial_x\Psi|\) on the degree rectangle and
larger exterior domain used in (23). The following construction
does not require \(b-a\) to be small. Put
\[
 A=\max\{1,4L^2/\kappa_0\},\qquad
 H\le\min\left\{\frac r4,\
       \frac{\kappa_0}{16(\pi+L)},\
       \sqrt{\frac{\kappa_0}{16A}}\right\},\qquad H>0,
 \tag{25}
\]
shrinking \(H\) further if necessary to stay in the reserved
degree rectangle. Let \(\operatorname{sinc}z=\sin(\pi z)/(\pi z)\)
with its removable value at zero, and define
\[
 \begin{split}
 \delta_{j,N}(Z)&=F_{j,N}(Z)-\widehat F_N(j/N,Z),\\
 \mathfrak F_N(x,Z)&=\widehat F_N(x,Z)
    +\sum_{j=j_0}^{j_1}\delta_{j,N}(Z)
       \operatorname{sinc}(Nx-j)
                   \exp[-AN(x-j/N)^2].
 \end{split}                                                   \tag{26}
\]
This is a finite analytic formula. In particular
\[
             \mathfrak F_N(j/N,Z)=F_{j,N}(Z)
                   \quad(j_0\le j\le j_1)                 \tag{27}
\]
as an identity of holomorphic functions of \(Z\). Every exterior
normal at those rows is therefore exact.

We prove the uniform relative bound, which is the reason for the
Gaussian localizer. Write \(x=X+iY\). The identity
\(\operatorname{sinc}z=\frac12\int_{-1}^1e^{i\pi zu}\,du\) gives
\[
 |\operatorname{sinc}(Nx-j)|\le e^{\pi N|Y|}.
 \tag{28}
\]
Equation (23) bounds the ratio of the surrogate at a node to its
value at \(x\) by
\(C\exp\{NL(|X-j/N|+|Y|)\}\). Also
\[
 \left|\exp[-AN(x-j/N)^2]\right|
       =\exp[-AN(X-j/N)^2+ANY^2].
 \tag{29}
\]
Combining these with (21), summing at most \(N\) terms, and using
\(Ld-Ad^2\le L^2/(4A)\) proves
\[
 \left|\frac{\mathfrak F_N}{\widehat F_N}-1\right|
 \le CN\exp\left\{-N\left[
       \kappa_0-\frac{L^2}{4A}-(\pi+L)|Y|-AY^2\right]\right\}.
 \tag{30}
\]
The choices (25) make the three losses at most
\(3\kappa_0/16\). Thus, uniformly on \(|\Im x|\le H\),
and on a small fixed real enlargement of \([a,b]\) contained in
the degree rectangle,
\[
 \left|\frac{\mathfrak F_N}{\widehat F_N}-1\right|
                       \le C e^{-\kappa_0N/2}.             \tag{31}
\]
Increasing the threshold makes this smaller than \(1/2\).
The exact interpolant is a holomorphic unit there, and (24) holds
with \(\mathfrak F_N\) in place of \(\widehat F_N\).
On smaller degree and exterior domains, Cauchy's formula gives the
same exponential conclusion, with a possibly smaller positive
exponent, for every fixed derivative of the relative error.
This includes exterior spectral normals. Derivatives of the
unnormalized function also differentiate its original action;
they are not asserted to have an \(N\)-independent prefactor.

The real enlargement accommodates cutoffs at half-integer degree,
such as \((j_0-1/2)/N\) and \((j_1+1/2)/N\).
The estimate uses the Lipschitz bound for \(\Psi\) on that enlarged
rectangle and is otherwise unchanged.

## 5. The actual terminating tail amplitude

The same correction method also applies to the original consumed-normal
tail weight, with its true exponentially decreasing action. This gives
an amplitude for the actual row sum, rather than only for its incident
kernel rows.

Fix \(0<\delta<1/2\), and now require
\[
       0<a<b<\tfrac12-\delta,\qquad |\alpha|\le A_\alpha<\pi.
 \tag{32}
\]
Put \(m=\lfloor N/2\rfloor\), \(L_N=\lfloor\delta N\rfloor\),
\(\eta=(-1)^{N-1}\), and \(\tau(x)=\pi-2\pi x-\pi/N\).
The original omitted coefficient is
\(\omega_{j,N,L_N}(\alpha)=\eta(-1)^j\gamma_{j,N}(\alpha)\).
Its exact finite lowering formula is
\[
 \gamma_{j,N}(\alpha)
  =T_{0,N}(\alpha,\tau(j/N))
     \sum_{\ell=L_N+1}^{p_j}
       \prod_{r=0}^{\ell-1}\rho_{r,N}(\alpha,\tau(j/N)),
 \qquad p_j=m-1-j.
 \tag{33}
\]
Define
\[
 (u_r,v_r)=
 \begin{cases}
 ((r+\tfrac12)\pi/N,(r+1)\pi/N),&N\ {\rm even},\\
 ((r+1)\pi/N,(r+\tfrac32)\pi/N),&N\ {\rm odd},
 \end{cases}
\]
\[
 \rho_{r,N}(\alpha,t)=
 \frac{[\cos^2u_r+\sinh^2(\alpha/(2N))]
                 [\sin^2(t/2)-\sin^2u_r]}{\cos^4v_r},
 \tag{34}
\]
\[
 T_{0,N}(\alpha,t)=
 \begin{cases}
 N^{-1}\cosh(\alpha/2)\sin t,&N\ {\rm even},\\
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
      {N\cos^4(\pi/(2N))}\sin t\sin(t/2),&N\ {\rm odd}.
 \end{cases}                                                   \tag{35}
\]
These formulas, including the upper stop \(p_j\), are the actual
full-normal tail identity from the pinned outer-row source.
The original normal has already differentiated the omitted radical;
only the values of the remaining spectator are sampled by (33).

Choose \(0<\sigma_\gamma<1/2-\delta-b\), and put
\(k_N=\lfloor\sigma_\gamma N\rfloor\). Define the finite analytic
prefix
\[
 \widehat\Gamma_N(x,\alpha)=T_{0,N}(\alpha,\tau(x))
       \sum_{\ell=L_N+1}^{L_N+k_N}
          \prod_{r=0}^{\ell-1}\rho_{r,N}(\alpha,\tau(x)).
 \tag{36}
\]
For all sufficiently large \(N\), this prefix ends before every
actual stop \(p_j\) with \(j/N\in[a,b]\).

Here is the uniform tail estimate with that stop retained.
At a physical row, \(r<p_j\) implies that both relevant cosines
stay bounded away from zero, uniformly for \(j/N\ge a\).
Using \(\sin^2(\tau(j/N)/2)=\cos^2(\pi(j+1/2)/N)\), the ratio
in (34) differs by \(O(N^{-1})\), uniformly through this entire
physical range, from
\[
       \rho(u,x)=1-\frac{\sin^2(\pi x)}{\cos^2(\pi u)},
       \qquad u=r/N,\quad x=j/N.
 \tag{37}
\]
In that range the limiting ratio is nonnegative up to an
\(O(N^{-1})\) endpoint change and is at most
\(1-\sin^2(\pi a)\). Consequently there is a fixed \(q<1\)
such that all the actual ratios through the stop obey
\(|\rho_{r,N}|\le q\). This remains uniform for bounded complex
\(\alpha\): its contribution to (34) is \(O(N^{-2})\).
This estimate is only used up to the original stop.

On a fixed sufficiently small complex degree neighborhood of
\([a,b]\), the prefix ratios with \(r\le L_N+k_N\) are units,
and also have modulus at most \(q<1\), after enlarging \(q\)
and shrinking the neighborhood. Indeed
\(\delta+\sigma_\gamma<1/2-b\) leaves a strict margin in (37).
Factor the first product out of (36), writing
\[
 \widehat\Gamma_N=T_{0,N}
       \left(\prod_{r=0}^{L_N}\rho_{r,N}\right)G_N.
 \tag{38}
\]
The remaining finite sum satisfies
\[
            G_N(x,\alpha)
              =\frac1{1-\rho(\delta,x)}+O(N^{-1})+O(q^{k_N}).
 \tag{39}
\]
For a direct proof, freeze each subsequent ratio at
\(\rho(\delta,x)\). Its error after \(s\) steps is \(O((s+1)/N)\).
A telescoping product estimate bounds the error of a product of
\(s\) such factors by \(C(s+1)^2q^{s-1}/N\). Their sum is
\(O(N^{-1})\), and the tail of the frozen geometric series is
\(O(q^{k_N})\). All estimates are holomorphic and uniform on the
chosen neighborhood. In particular \(G_N\) is a unit bounded above
and below.

The factors \(T_{0,N}\) are also units there after removing \(N^{-1}\):
\(\sin\tau\) and the odd factor \(\sin(\tau/2)\) stay nonzero,
and \(\cosh(\alpha/2)\) has no zero on the compact disk in (32).
Comparing the remaining actual sum from \(L_N+k_N+1\) through
its literal \(p_j\) with the first product, the bound \(q<1\)
therefore proves
\[
 \left|\frac{\gamma_{j,N}(\alpha)}
                 {\widehat\Gamma_N(j/N,\alpha)}-1\right|
       \le Cq^{k_N}
       \le C e^{-\kappa_\gamma N},\qquad
 \kappa_\gamma=\sigma_\gamma|\log q|/2>0 .
 \tag{40}
\]
No infinite off-grid tail was substituted for the finite source.

Define the real-normalized analytic phase
\[
 \Xi_\delta(x)=\int_0^\delta
       \log\left(1-\frac{\sin^2(\pi x)}{\cos^2(\pi u)}\right)\,du
                 =-J_\delta(x).
 \tag{41}
\]
All factors in this integral are positive on the real rectangle
under consideration and have units on its chosen complex thickening.
Uniform Riemann sums for the logarithm of (34), including both
parity offsets and \(L_N-\delta N=O(1)\), now give
\[
 \log\widehat\Gamma_N(x,\alpha)
                  =N\Xi_\delta(x)-\log N+O(1).
 \tag{42}
\]
The bounded term has a canonical analytic branch obtained from
(35), (38), and (39); only its bounded real part is needed here.
In particular the ratio of values at two degree points is bounded
by \(C\exp\{N L_\gamma|x-y|\}\) along paths in the rectangle, with
\(L_\gamma\) any bound for \(|\Xi_\delta'|\), and with the path
length in place of the distance if necessary.

Choose a fixed analytic buffer \(r_\gamma>0\) inside the degree
neighborhood just constructed. Apply exactly (26)--(31), with
\(\widehat F_N,\delta_{j,N},\kappa_0,L,r\) replaced by
\(\widehat\Gamma_N,\gamma_{j,N}-\widehat\Gamma_N(j/N),
\kappa_\gamma,L_\gamma,r_\gamma\). This produces one analytic
\(\mathfrak G_N(x,\alpha)\), exact at all the physical degree
nodes in \([a,b]\), with
\[
 \mathfrak G_N(j/N,\alpha)=\gamma_{j,N}(\alpha),\qquad
 |\mathfrak G_N|\le C N^{-1}e^{N\Re\Xi_\delta(x)}
 \tag{43}
\]
on the quantitative fixed strip given by (25) with those replacements.
Its relative error from the finite prefix is exponentially small,
including fixed \(\alpha\) derivatives on smaller disks.
The lower bound of the same order also holds there for large \(N\).

## 6. What this permits in the original finite sum

For any \(Z\) in the stated domain and any holomorphic spectator
\(f(x,Z)\), the exact finite sum with these rows is
\[
 \sum_{j=j_0}^{j_1} F_{j,N}(Z)f(j/N,Z)
 =\frac1{2\pi i}\int_\Gamma
       \frac{2\pi iN}{e^{2\pi iNx}-1}
                         \mathfrak F_N(x,Z)f(x,Z)\,dx .
 \tag{44}
\]
Here \(\Gamma\) is any positively oriented contour in the constructed
strip enclosing exactly the displayed degree nodes and no other
kernel pole. The residue of the displayed kernel at each node is
one. Products of finitely many rows at the same consumed-normal
index may be interpolated by the product of their \(\mathfrak F_N\)'s;
the exterior variables and every shared spectator remain independent.
Their actions add, their polynomial costs multiply, and all sampled
mixed exterior normals are still exact.

The exact Gaussian crossing and any integer alias may be kept in
\(f\). For \(n\ne0\), on the Fresnel ray \(x=e^{i\,\operatorname{sgn}(n)
\pi/4}r\),
\[
                  |e^{i\pi nNx^2}|=e^{-\pi|n|Nr^2}.
 \tag{45}
\]
Such a ray can only be used where it lies in the constructed strip;
no continuation to unbounded height is asserted. In particular the
availability of a fixed height in (25) is not permission to rotate
an entire macroscopic ray beyond that height. Equation (45) concerns
only the displayed quadratic factor; all original linear characters,
half-offsets, and scalar carriers stay in \(f\).

For any fixed admissible path \(\Gamma_1\) in the strip, away from
the kernel poles, the literal integral in (44) is bounded by its
length times the supremum of
\[
 C N^C\left|\frac{N}{e^{2\pi iNx}-1}\right|
             \exp\{N\Re\Psi(x,Z)\}\,|f(x,Z)|.
 \tag{46}
\]
With several incident rows, replace \(\Psi\) by their sum. Thus
the interpolation does not add an extensive spectral-band action
to the original row phase. On fixed horizontal heights the kernel
has its explicit geometric-series alias bound; on cutoff segments
at half-integer degree its denominator is \(e^{-2\pi N\Im x}+1\).
Those original kernel and Gaussian factors have not been omitted.

There is only one function (26) across the entire degree interval.
If a contour is subdivided, the artificial common faces cancel
exactly with opposite orientations, including all spectators.
The two external endpoint connectors do not cancel for this reason.
They retain the value of (46) on their actual paths. Nor does the
construction estimate a spectator which has not itself been bounded.
In particular, full traces whose other colors leave the exterior
domain (2) cannot silently be replaced by a norm on that domain.

Finally the interval stays away from both \(x=0\) and \(x=1/2\).
The contraction, analytic radius, and height can deteriorate as
those boundaries are approached. The present theorem does not
supply a uniform endpoint-to-fold interpolation, a filled-action
bound for the outer connectors, a joint relative-cycle transport,
or a nonzero geometric coefficient. It supplies an exact moderate
bulk interpolation with explicit height and decay budgets, which
was not provided by the physical-row asymptotic alone.

Use the minimum of the row and tail strip heights when combining
their interpolants. In the narrower degree interval (32), the actual single-tail row
sum can be placed in the same formula by replacing the interpolated
amplitude by
\[
 \eta e^{i\pi Nx}\mathfrak G_N(x,\alpha)
                   \prod_e\mathfrak F_N(x,Z_e)\,f(x,\mathbf Z).
 \tag{47}
\]
At \(x=j/N\), this is exactly
\(\omega_{j,N,L_N}(\alpha)\prod_eF_{j,N}(Z_e)f(j/N,\mathbf Z)\).
The factor \(e^{i\pi Nx}\), the original Gaussian in \(f\), and the
residue kernel are retained; integer alias changes must preserve
their sampled product. Its noncharacter amplitude has the actual
bound
\[
 C N^C\exp N\Re\left\{-J_\delta(x)
                           +\sum_e\Psi(x,Z_e)\right\}.
 \tag{48}
\]
This also preserves every exterior mixed normal at the sampled
rows. Extra shared endpoint coupons, other coupled traces, and
arbitrary spectators stay in \(f\); no estimate for them follows
from (48). A free color tending to \(2\) is outside the fixed
half-plane gap (2). The left endpoint \(x=0\) and the terminating
tail boundary \(x=1/2-\delta\) are likewise outside the uniform
strip construction. Thus (47)--(48) do not complete the original
paired vertical/current boundary estimate.

## 7. Direct-source readbacks

All three complete direct sources were read and their used statements
checked at the following versions:

* [Physical-row Riccati transport](research_physical_row_riccati_transport.md),
  SHA256 a9d5719e4a3129ad999e511037d87d0a31b70546db7ec24558277739e58bbf4a:
  exact recurrence, physical-ratio attraction on a larger complex
  exterior domain, canonical logarithms, absolute normalization,
  and original phase identification.
* [Original Racah root location](actual_matching_edge_racah_root_location.md),
  SHA256 f84b82d7924a0c92ca803bc4834bcb0f18f63cedebf2bd072d41d0545a9f5793:
  literal physical-row polynomial, roots strictly above two, and
  its normalized canonical logarithm.
* [Actual omitted endpoint rows](research_endpoint_outer_row_decay.md),
  SHA256 85e708606a44cbbbc45a82db0685fcb1d35215c89470ccdc7408790305e55e30:
  exact both-parity lowering products, the true terminating stop,
  consumed-normal functional, and its original graph placement.

The growing-order Euler--Maclaurin bound and the exact correction
are proved above. Only written mathematics, source text reads and
hashes were used; no mathematical program, numerical experiment,
test or compilation was run. Frozen notes and public manuscripts
are unchanged.
