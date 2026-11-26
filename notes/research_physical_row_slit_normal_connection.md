# Actual first-normal normalization of the physical row interpolant

Private written proof, 16 November 2026.

The analytic interpolation of physical row values has a scalar
first-normal normalization, determined by the original source. On
every compact spectral slit chart that normalization is exponentially
accurate. Its proof uses the common-shift Jacobi derivative, exact
kernel symmetry at the physical grid, and analytic propagation of
smallness. It does not assume a source coefficient from a formal
characteristic equation.

The degree variable remains in a fixed bulk interval. The result
continues the second spectral variable through arbitrary compact
subsets of its slit plane; it does not continue the first degree
variable to an arbitrary height. An exact scalar full-jet interpolant
on a thin degree strip follows, with the original row action. Equality
at its bulk subgrid is not equality in the whole original trace.

## 1. Source, normalization and statement

Put \(h=N^{-1}\), \(\theta=\pi/N\), and
\[
 c(r)=2\cos((2r+1)\theta),\qquad c_j=c(j),\qquad
 C_N(x)=c(Nx)=2\cos(2\pi x+\theta).
 \tag{1}
\]
Use the original kernel \(K_N\), physical rows and normals
\[
 F_j(w)=K_N(c_j,w),\qquad G_j(w)=\partial_zK_N(c_j,w),
 \qquad \Omega=\mathbb C\setminus[2,\infty).
 \tag{2}
\]
Here \(P_N(w)=2T_N(w/2)+2\) and \(s_1=2\sin\theta\).
The first normal \(G_j\) is prescribed only at double nodes.
All rows in a fixed compact degree interval inside \((0,1/2)\)
are double nodes for sufficiently large \(N\).

We retain the actual common-shift Jacobi polynomials
\[
 F_j^{(\varepsilon)}(w)=
 \frac{\det(\mathcal J_j(\varepsilon)-wI)}
      {\prod_{r<j}A(r+\varepsilon)},\qquad
 R_j(w)=\left.\partial_\varepsilon F_j^{(\varepsilon)}(w)\right|_0,
 \qquad D_j(w)=R_j(w)/F_j(w).
 \tag{3}
\]
Here
\[
 A(r)=\frac{[2\sin((r+1)\theta)]^4}
 {4\sin((2r+1)\theta)\sin((2r+2)\theta)},\quad
 C(r)=\frac{[2\sin(r\theta)]^4}
 {4\sin(2r\theta)\sin((2r+1)\theta)},\quad C(0)=0.
 \tag{4}
\]
The diagonal of \(\mathcal J_j(\varepsilon)\) is
\(c_0+A(r+\varepsilon)+C(r+\varepsilon)\); its off-diagonal
is \(-\sqrt{A(r+\varepsilon)C(r+1+\varepsilon)}\).
In particular \(c_0\) is held fixed during this common shift.
The definitions at the left endpoint have their removable values.

Let \(\widetilde Q_N(w)\) be precisely the even logarithmic-factorial
representative of \(Q_0=G_0\) in the pinned residue theorem.
Its spectral descent is holomorphic on \(\Omega\). The pole-free
source normal is
\[
 \widehat G_j(w)=
 \frac{F_j(w)}{c'(j)}
       \{c'(0)\widetilde Q_N(w)+D_j(w)\},\qquad
 c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{5}
\]
This preserves the value and required first \(w\)-normal of \(G_j\)
at every physical second endpoint. It may replace \(G_j\) inside a
subsequent original trace, with all mixed normals and spectators.
It is not an equality of free off-grid polynomials.

For clarity the source term behind (5) is
\[
 \begin{split}
 c'(j)G_j(w)={}&c'(0)F_j(w)Q_0(w)+R_j(w)\\
 &+\frac{c'(0)P_N(w)}{N^2s_1^2}
        F_j(w)[(\mathcal J_j-wI)^{-1}]_{00}.
 \end{split}
 \tag{6}
\]
The last factor multiplied by \(F_j\) is a polynomial cofactor.
It is removed only in the full physical-jet class, and the
replacement of \(Q_0\) is the specified one in (5).

Fix
\[
             0<a<b<1/2,\qquad \mathcal K\Subset\Omega.
 \tag{7}
\]
Every construction below uses one slightly larger degree interval
and a bounded simply connected slit neighborhood of \(\mathcal K\),
with fixed buffers. The neighborhood also contains a fixed real interval
inside \((-2,2)\). These choices precede \(N\). Constants and
positive exponential rates can depend on those choices.

Write
\[
 \lambda(x,w)+\lambda(x,w)^{-1}
       =2+(2-w)\cot^2(\pi x),\qquad
 \Psi(x,w)=\int_0^x\operatorname{Log}\lambda(s,w)\,ds .
 \tag{8}
\]
For real \(0<x<1/2\), select the root \(|\lambda|>1\), positive
for \(w<2\), and its real-normalized logarithm. The integral
converges at zero. Extend \(x\) only to a sufficiently thin
complex neighborhood of the enlarged bulk interval.

**Theorem 1.** There is a holomorphic unit \(A_N(x,w)\) on such
a degree neighborhood times a neighborhood of \(\mathcal K\),
and an actual anchor \(j_*=j_*(N)\), \(x_*=j_*h\), in the
interior of the degree interval, such that
\[
                         A_N(x_*,w)=F_{j_*}(w).
 \tag{9}
\]
Uniformly for \(j/N\in[a,b]\), \(w\in\mathcal K\), and every
fixed number of \(w\)-derivatives,
\[
 \begin{split}
 A_N(jh,w)/F_j(w)-1&=O(e^{-\kappa N}),\\
 \frac{\partial_xA_N(jh,w)-C_N'(jh)\widehat G_j(w)}
      {F_j(w)}&=O(e^{-\kappa N}).
 \end{split}
 \tag{10}
\]
The rate can be decreased when taking derivatives.
The actual scalar connection coefficient is
\[
 \boxed{\quad
 a_N(w)=c'(0)\widetilde Q_N(w)+D_{j_*}(w)
                  -h\,\partial_x\log A_N(x_*,w).
 \quad}
 \tag{11}
\]
It satisfies
\[
                   \partial_w^k a_N(w)=O_k(e^{-\kappa_{\mathcal K}N})
                    \quad(w\in\mathcal K)
 \tag{12}
\]
for every fixed \(k\). Thus no unspecified initial normal remains
in (10).

On the degree neighborhood,
\[
                    N^{-1}\log A_N(x,w)=\Psi(x,w)+o(1)
 \tag{13}
\]
locally uniformly, with the original normalized logarithm.
On compact subsets of \(\Re w<2\), the error in
\(\log A_N-N\Psi\) is \(O(\log N)\). On a general slit compact
only \(o(N)\), or an arbitrary fixed exponential tolerance,
is asserted.

## 2. Uniform nonzero ratios on the whole slit

The exact value recurrence is
\[
 \rho_{j+1}=\mathscr R_{N,jh,w}(\rho_j),\qquad
 \rho_j=F_j/F_{j-1},\qquad
 \mathscr R_{N,x,w}(z)
   =1+\frac{c_0-w}{A(Nx)}
                +\frac{C(Nx)}{A(Nx)}(1-z^{-1}).
 \tag{14}
\]
Both a lower and an upper bound on \(\rho_j\) are needed.
Bounds on determinant values alone would not suffice.

Fix a bulk upper endpoint \(b_0<1/2\). All entries of
\(\mathcal J_j\), for \(j\le b_0N\), are bounded uniformly in
\(N\). This follows directly from (4): away from zero it is a
compact sine-ratio bound; for small \(r/N\), cancel the common
powers using the uniform comparison \(\sin y\asymp y\).
The off-diagonal bound follows from the same bounds for \(A,C\).
The source root-location theorem gives \(\mathcal J_j>2I\).
Consequently its spectrum lies in one fixed interval \([2,L]\).

The last resolvent entry is the Stieltjes transform of a
probability measure on that interval:
\[
 m_j(w)=[(\mathcal J_j-wI)^{-1}]_{j-1,j-1}
       =\int_{[2,L]}\frac{d\mu_j(s)}{s-w}
       =\frac{F_{j-1}(w)}{A(j-1)F_j(w)}.
 \tag{15}
\]
On every compact subset of \(\Omega\), these transforms are
uniformly bounded above and away from zero. To prove the latter,
for a fixed \(w\in\Omega\) the arguments of
\(\{(s-w)^{-1}:2\le s\le L\}\) lie in an open sector of
width less than \(\pi\). Rotate its bisector to the positive
real axis. The real part then has a positive lower bound,
uniform in \(s\), and remains so on a neighborhood of \(w\).
A finite cover of the compact set proves the assertion for
every probability measure \(\mu_j\).

On a bulk interval \(A(j-1)\) is also bounded above and below.
Equation (15) proves
\[
            0<c\le|\rho_j(w)|\le C<\infty
 \tag{16}
\]
on every fixed slit compact. It also proves holomorphy there.
Larger compact neighborhoods and Cauchy's formula give uniform
fixed derivative bounds.

The half-plane ratio theorem retained in the pinned interpolation
source gives \(\rho_j-\lambda(jh,w)=O(h)\) when \(\Re w<2\).
It follows that
\[
                  \rho_j(w)-\lambda(jh,w)\longrightarrow0
 \tag{17}
\]
uniformly on every bulk interval times every slit compact.
Indeed otherwise take \(N_\ell\to\infty\) and
\(j_\ell/N_\ell\to x\) witnessing failure. By (16), the
holomorphic ratios have convergent subsequences on all slit
compacts. On the half-plane each limit is \(\lambda(x,w)\);
the identity theorem gives that limit on the connected slit.
This contradicts the alleged failure.

For real \(x\in(0,1/2)\), the quantity on the right of (8)
cannot lie in \([-2,2]\) for \(w\in\Omega\). Thus the selected
root has \(|\lambda|>1\) throughout the slit. On fixed bulk
and slit compacts its modulus is at least \(1+\delta\).
Small disks around that root and a small complex thickening
in \(x\) give a uniform contraction factor
\[
         |\partial_z\mathscr R_{N,x,w}|\le\vartheta<1.
 \tag{18}
\]
The limiting-root defect is \(O(h)\), uniformly and holomorphically.
Use (17) at a fixed earlier bulk buffer and iterate
\(e_{j+1}\le\vartheta e_j+Ch\). This proves the full-slit
improvement
\[
                         \rho_j-\lambda(jh,w)=O(h).
 \tag{19}
\]
All fixed exterior derivatives follow on smaller compacts.

## 3. The analytic value mode and its shifted residual

The proof in the pinned degree-interpolation source now applies
on the slit compacts just established. Its use of
\(\Re\lambda>1\) was to obtain contraction and a unit logarithm;
(18) and simple connectedness provide these here.
For completeness specify the construction and the residuals
which will be differentiated.

Choose a fixed small \(\sigma>0\) within a left degree buffer and
put \(m=\lfloor\sigma N\rfloor\). Start at
\(\lambda(x-mh,w)\), apply the \(m\) maps in (14) at
\(x-mh,\ldots,x-h\), and call the result \(\mathcal R_N(x,w)\).
Then on buffered complex neighborhoods
\[
 \mathcal R_N=\lambda+O(h),\qquad
 \mathcal R_N(jh,w)-\rho_j(w)=O(e^{-\kappa_0N}),
 \tag{20}
\]
and
\[
 \mathcal R_N(x+h,w)
       -\mathscr R_{N,x,w}(\mathcal R_N(x,w))
                     =O(e^{-\kappa_0N}).
 \tag{21}
\]
For (21), compare the two starting values after aligning their
last \(m\) maps; their difference is \(O(h)\), and the common
maps contract it by \(\vartheta^m\). Equations (20)--(21)
hold on larger fixed neighborhoods before Cauchy differentiation.
Let \(\ell_N=\operatorname{Log}\mathcal R_N\), on the branch
continued from real \(w<2\).

Use the anchored Euler--Maclaurin primitive
\[
 \begin{split}
 L_N(x,w)={}&h^{-1}\int_{x_*}^x\ell_N(s,w)\,ds
             +\tfrac12[\ell_N(x,w)-\ell_N(x_*,w)]\\
 &+\sum_{\nu=1}^{p_N-1}
   \frac{B_{2\nu}h^{2\nu-1}}{(2\nu)!}
   [\partial_x^{2\nu-1}\ell_N(x,w)
       -\partial_x^{2\nu-1}\ell_N(x_*,w)],\\
 A_N(x,w)={}&F_{j_*}(w)e^{L_N(x,w)},\qquad
                         p_N=\lfloor cN\rfloor .
 \end{split}
 \tag{22}
\]
Here \(c>0\) is small relative to the fixed analytic radius.
The anchored integrals can run in either direction in the degree
rectangle. The factorial Cauchy bounds and Bernoulli bounds in the
pinned proof give exponential remainders, uniformly also on a
smaller complex neighborhood. In particular
\[
 \begin{split}
 L_N(x+h,w)-L_N(x,w)
                         &=\ell_N(x+h,w)+O(e^{-\kappa_1N}),\\
 A_N(jh,w)/F_j(w)&=1+O(e^{-\kappa_1N}).
 \end{split}
 \tag{23}
\]
The first identity can equivalently be checked by applying the
Euler--Maclaurin remainder to the single complex segment
\([x,x+h]\); its Cauchy estimates are uniform in \(x\).
All fixed derivatives of these residuals are exponential after
shrinking buffers.

The correction terms in (22) beyond the half-endpoint term are
\(O(h)\), and \(\ell_N=\operatorname{Log}\lambda+O(h)\).
Thus
\[
 \log A_N(x,w)-\log A_N(y,w)
        =N[\Psi(x,w)-\Psi(y,w)]+O(1).
 \tag{24}
\]
At the actual anchor, the all-row slit theorem supplies
\(\log F_{j_*}=N\Psi(x_*,w)+o(N)\), with \(O(\log N)\)
on half-plane compacts. This proves (13), its locally uniform
lower bound as well as its upper bound, and its derivative
versions. Also \(h\partial_x\log A_N=O(1)\) on fixed smaller
neighborhoods.

## 4. Common-shift differentiation and the actual constant

Let
\[
 \rho_j^{(\varepsilon)}
       =F_j^{(\varepsilon)}/F_{j-1}^{(\varepsilon)},\qquad
 u_j=\left.\partial_\varepsilon\rho_j^{(\varepsilon)}\right|_0.
 \tag{25}
\]
The exact determinant recurrence in (3) gives
\[
 \rho_{j+1}^{(\varepsilon)}
    =\mathscr R_{N,jh+h\varepsilon,w}
                         (\rho_j^{(\varepsilon)}).
 \tag{26}
\]
There is no derivative of \(c_0\) in this equation.
Differentiating it gives every common-shift forcing term:
\[
 u_{j+1}=\beta_j u_j+h f_j,\qquad
 \beta_j=\frac{C(j)}{A(j)\rho_j^2},\qquad
 f_j=\left.\partial_x\mathscr R_{N,x,w}(z)
                                      \right|_{x=jh,z=\rho_j}.
 \tag{27}
\]
Also, exactly,
\[
                         D_j-D_{j-1}=u_j/\rho_j.
 \tag{28}
\]
The source determinant bound gives \(D_j=O(N^4)\) on slit
compacts. By (16), \(u_j=\rho_j(D_j-D_{j-1})\) is polynomially
bounded at any starting bulk row.

Differentiate (21) in \(x\) and multiply by \(h\).
The result is the same affine equation as (27) for
\(h\partial_x\mathcal R_N\), up to an exponential residual.
Equations (20), (18) and bounded coefficient derivatives allow
the two affine equations to be compared on a fixed earlier
buffer. Any polynomial initial difference contracts exponentially.
Therefore, throughout the inner bulk interval,
\[
                   u_j-h\partial_x\mathcal R_N(jh,w)
                                =O(e^{-\kappa_2N}).
 \tag{29}
\]
This step retains the actual left-end derivative through its
polynomial initial datum; it does not set that datum to zero.

From (23), (28), and (29),
\[
 \begin{split}
 &[D_{j+1}-h\partial_x\log A_N((j+1)h,w)]\\
 &\qquad-[D_j-h\partial_x\log A_N(jh,w)]
                              =O(e^{-\kappa_2N}).
 \end{split}
 \tag{30}
\]
Summing at most \(N\) steps, and reducing the rate, proves that
this difference is its value at \(j_*\), up to an exponential
error. Consequently
\[
 \frac{c'(j)\widehat G_j(w)}{F_j(w)}
                 -h\partial_x\log A_N(jh,w)
                  =a_N(w)+O(e^{-\kappa_3N}).
 \tag{31}
\]
The function \(a_N\) is exactly (11), not an unspecified
constant of integration. It is holomorphic and polynomially
bounded on every fixed buffered slit neighborhood, with all
fixed derivatives: use \(D_{j_*}=O(N^4)\), the bound for
\(\widetilde Q_N\) in the pinned source, and (22).

## 5. Dense physical symmetry determines the constant

We use two elementary analytic observations. First, suppose
holomorphic functions on a fixed rectangle are bounded by a
fixed power of \(N\), and their values at the equally spaced
nodes \(j/N\) of a fixed interior interval are
\(O(e^{-\kappa N})\). On a smaller neighborhood of a shorter
interior interval they and their fixed derivatives are
\(O(e^{-\kappa' N})\), for some \(\kappa'>0\).

Here is a proof that also handles approximate zeros. Subtract
the finite cardinal sum of the nodal errors using
\(\operatorname{sinc}(Nx-j)\). On a sufficiently thin fixed
strip its size is at most
\(CN^M e^{-\kappa N+\pi N|\Im x|}\), hence exponentially
small. The remainder has exact zeros at all the nodes.
Choose a fixed disk in the rectangle and a smaller concentric
disk containing a positive fraction of those nodes. Factor
the corresponding disk Blaschke factors. On a still smaller
disk each factor has modulus at most a fixed number less
than one, uniformly in the chosen nodes. The maximum principle
then bounds the remainder by \(CN^M e^{-cN}\).
A finite covering and Cauchy's formula prove the observation.

Second, an exponentially small holomorphic family on one fixed
open subset, polynomially bounded on a connected larger domain,
is exponentially small on each compact subset of that domain.
A finite chain of overlapping buffered disks and the
three-circles inequality proves this: at each step the exponent
is multiplied by a fixed positive number, while polynomial
losses remain \(e^{o(N)}\). This assertion concerns compact
paths; it has no uniform boundary or shrinking-buffer content.

Choose a fixed physical second-row interval \(k/N\in[a_1,b_1]\)
strictly inside \((0,1/2)\). Its spectral values lie in the real
interval included in our slit neighborhood. For each such \(k\)
compare, as functions of the complex degree \(x\),
\[
                        A_N(x,c_k),\qquad F_k(C_N(x)).
 \tag{32}
\]
At \(x=jh\), the exact source symmetry
\(F_j(c_k)=F_k(c_j)\), together with (23), makes their
difference exponentially small relative to \(F_j(c_k)\).

Both functions in (32), divided by \(e^{N\Psi(x,c_k)}\), are
polynomially bounded on a sufficiently thin fixed degree
neighborhood, uniformly in \(k\). For the first this is (13)
in a half-plane compact. For the second, apply the pinned
half-plane row bound to \(F_k\) at \(C_N(x)\), which stays
in a compact subset of \(\Re w<2\). The two phase functions
differ by \(O(h)\) there:
\[
                 \Psi(kh,C_N(x))-\Psi(x,c_k)=O(h).
 \tag{33}
\]
To check (33), write \(\Psi\) as the original symmetric
two-real-angle phase and then continue analytically to this
thin neighborhood. The actual two angular arguments each
differ from the corresponding unshifted one by \(\theta\).
They stay in fixed bulk intervals, so their derivatives are
bounded. Thus no endpoint estimate or omitted half-offset
is being used.

Apply the first analytic observation to the normalized
difference in (32), on a degree disk around \(x_*\).
It gives
\[
 \frac{\partial_xA_N(x_*,c_k)
                 -C_N'(x_*)F_k'(c_{j_*})}
          {F_{j_*}(c_k)}
                       =O(e^{-\kappa_4N}).
 \tag{34}
\]
Differentiating the normalizing exponential only introduces
a polynomial factor, absorbed by a smaller rate.
The exact source normal symmetry and the full-jet representative
give
\[
               \widehat G_{j_*}(c_k)
                  =G_{j_*}(c_k)=F_k'(c_{j_*}).
 \tag{35}
\]
Using the exact anchor (9) in (11), equations (34)--(35)
prove
\[
                              a_N(c_k)=O(e^{-\kappa_5N}).
 \tag{36}
\]

Apply the first observation again to
\(a_N(C_N(y))\), on a fixed thin neighborhood of
\([a_1,b_1]\). Its polynomial bound was proved after (31).
Thus \(a_N\) is exponentially small on a fixed open spectral
neighborhood. The second observation propagates this to every
compact subset of the connected slit neighborhood, and hence
to the originally prescribed \(\mathcal K\).
Larger buffers followed by Cauchy's formula give all fixed
spectral derivatives. This proves (12).

Finally (31), (12), the value estimate (23), and
\(C_N'(jh)=c'(j)/h\), with \(|c'(j)|\asymp h\) on the bulk,
give the normal estimate (10). The factors from replacing
\(A_N(jh,w)\) by \(F_j(w)\) are polynomial and are absorbed
by reducing the positive exponential rate. Theorem 1 follows.

## 6. An exact scalar full-jet correction and its scope

The approximate scalar can be corrected without prescribing a
separate incompatible normal function. Put
\(v_N=e^{-N\Psi}A_N\). At the physical degree nodes define
\[
 \begin{split}
 d_j(w)&=e^{-N\Psi(jh,w)}F_j(w)-v_N(jh,w),\\
 b_j(w)&=e^{-N\Psi(jh,w)}
    [C_N'(jh)\widehat G_j(w)-N\Psi_x(jh,w)F_j(w)]
                         -\partial_xv_N(jh,w).
 \end{split}
 \tag{37}
\]
On general slit compacts, (10), (13) show these are
\(O(e^{-\kappa N+o(N)})\); after reducing \(\kappa\) they
are uniformly exponentially small. The same holds for
fixed exterior derivatives. Define
\[
 \begin{split}
 \mathfrak F_N(x,w)=e^{N\Psi(x,w)}
 \bigg[v_N(x,w)+
  \sum_{j:\,jh\in[a,b]}
   \{d_j(w)+b_j(w)(x-jh)\}
                   \operatorname{sinc}^2(Nx-j)\bigg].
 \end{split}
 \tag{38}
\]
The cardinal functions in (38) have respectively value one
and derivative zero, or value zero and derivative one, at
their own node; both required jets vanish at every other node.
Consequently
\[
 \mathfrak F_N(jh,w)=F_j(w),\qquad
 \partial_x\mathfrak F_N(jh,w)
                         =C_N'(jh)\widehat G_j(w)
 \tag{39}
\]
as identities of holomorphic functions of \(w\).
All fixed \(w\)-derivatives of these identities are exact.

Since
\(|\operatorname{sinc}^2(Nx-j)|\le e^{2\pi N|\Im x|}\),
the correction is exponentially small relative to the
normalized action on a sufficiently thin fixed degree strip.
Thus, for every \(\epsilon>0\),
\[
           |\mathfrak F_N(x,w)|
              \le C_\epsilon e^{N(\Re\Psi(x,w)+\epsilon)}.
 \tag{40}
\]
On half-plane compacts one can replace the tolerance by a
polynomial factor. Fixed derivatives obey the corresponding
bound on buffered smaller domains.

At a physical second endpoint, (39) contains the actual
value, both independent first normals, and their mixed normal.
At the odd simple second endpoint only its value is prescribed;
the spectral formulas remain holomorphic through \(w=-2\).
There is no degree-fold or degree-endpoint assertion.

One may symmetrize (38) and its transposed construction on an
overlapping thin two-degree bulk rectangle. The sampled full
jets agree with the symmetric original kernel, so this preserves
all four physical jets and the own-phase upper bound there.
This observation does not extend the domain of either
construction.

The new part is the source-determined normal connection
(11)--(12) throughout compact slit charts. The existing
q-Hahn full-physical complex packet concerns a different
ordinary column with an integer channel; it does not
interpolate this channel or provide (12). The existing
bare-kernel rectangle theorem already covers a larger
central thin box with the actual whole kernel. No replacement
for that theorem is claimed here.

A compact positive second-color path lies in the slit, so
(12) applies along its entirety. Continuing the first degree
mode to a tall positive chart remains a separate problem.
Its selected Riccati root may have modulus one there even
while the two characteristic roots remain distinct. Neither
the present real-degree contraction nor the thin correction
(38) crosses that issue automatically.

Finally (39) only covers the specified bulk subgrid.
A full original trace must retain every other physical row,
its endpoint packets and any contour seams. The replacement
of \(G_j\) by (5) is valid before subsequent complete original
traces, not by deleting the \(P_N\) term of (6) on an
arbitrary open current. There is no whole-kernel positive-chart
bound, global cycle transport, or filled-source estimate here.

## Direct sources

Both complete texts and their used implications were read at
the following versions:

* [Exact analytic degree interpolation](research_physical_row_analytic_degree_interpolation.md),
  SHA256 f7d673e6633c0f46498a6c023512a3c64724d35c53ea168dabbd7f1e59f72d51:
  the exact physical Riccati recurrence and half-plane ratio input,
  exponential finite-iteration approximation, anchored
  growing-order Euler--Maclaurin primitive, and original phase.
* [Complete physical residue packets](research_compact_positive_contour_residue_control.md),
  SHA256 cac1016d5f515510b95071a25c8d97345b334043492a6b430c4e924f87d82bb0:
  the actual common-shift determinant and endpoint-normal
  representative, full physical-jet identity, polynomial
  slit bounds, all-row action and symmetric real calibration.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Frozen notes and public manuscripts are unchanged.
