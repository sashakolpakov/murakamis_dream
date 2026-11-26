# Actual physical-row windows on regular positive continuation charts

Private written proof, 16 November 2026.

The full-slit physical-row theorem fixes the actual value and first-normal
normalization on a real bulk window. Here that normalization gives a
moderate scalar mode on a buffered complex degree chart, even where the
selected characteristic root ceases to dominate in modulus. The proof
constructs the mode there; it does not propagate an exponentially small
source error through an uncontrolled growing solution.

An exact one-sided Hermite repair preserves the original window data
without a loss proportional to the designated complex height. The
positive product-domain theorem supplies such charts near every positive
pair whose first angle is nonzero. Connected overlaps with a common
physical seed have exponentially small normalized differences.
All original exterior window currents remain. No whole-grid kernel or
bound on a raw Sears cutoff transition is asserted.

## 1. Actual data and regular charts

Put \(h=N^{-1}\), \(\theta=\pi/N\), and use the centered degree coordinate
\[
 X_j=(j+\tfrac12)h,\qquad C(X)=2\cos(2\pi X),\qquad
 t=\pi-2\pi X,\qquad w(u)=-2\cos u .
 \tag{1}
\]
Thus \(C(X_j)=c_j\), with the original
\(c_j=2\cos((2j+1)\theta)\).
Retain the original physical row and its independent first normal,
\[
 F_j(w)=K_N(c_j,w),\qquad G_j(w)=\partial_zK_N(c_j,w).
 \tag{2}
\]
On the second spectral slit
\(\Omega=\mathbb C\setminus[2,\infty)\), the pinned normal theorem gives
the pole-free representative
\[
 \widehat G_j(w)=
 \frac{c'(0)F_j(w)\widetilde Q_N(w)+R_j(w)}{c'(j)},
 \qquad c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{3}
\]
Here \(R_j\) is the original common-shift Jacobi determinant derivative,
with \(c_0=2\cos\theta\) held fixed. At every physical second endpoint,
(3) has the value and required first normal of \(G_j\). Consequently
its use below is exact under subsequent original traces in that
endpoint, with all spectators and mixed normals retained. It is not a
replacement of an arbitrary free-boundary polynomial.

Choose real intervals
\[
 I\Subset J\Subset(0,1/2)
 \tag{4}
\]
with additional fixed real buffers on both sides. Let \(V\) be a bounded
simply connected angular parameter domain containing a real interval;
use a slightly larger domain and compact buffers whenever estimates
are made. Require \(V\Subset\{|\Re u|<\pi\}\), so that \(w(V)\) lies
in the spectral slit. Domains can be chosen symmetric in \(u\).

For the first degree use bounded simply connected domains
\[
 \overline{\mathcal D_1}\subset\mathcal D_2,\qquad
 \overline{\mathcal D_2}\subset\mathcal D_3,
 \tag{5}
\]
with positive buffer distances, containing the enlarged real interval
in (4). Paths from a real base point to points of these domains have
uniformly bounded length. Finite buffered tubes about a simple path
and a real interval suffice. Require that their closures avoid
\(X=0,1/2\) and the other zeros of \(\sin(2\pi X)\).

On a neighborhood of the buffered product set define
\[
 a=\tan(t/2)=\cot(\pi X),\qquad b=\tan(u/2),\qquad
 q_*^2=1+a^2+b^2,
 \tag{6}
\]
on the original branch, and put
\[
 \lambda=\frac{q_*+a}{q_*-a},\qquad
 \lambda+\lambda^{-1}=2+\frac{4a^2}{1+b^2}.
 \tag{7}
\]
The regular-chart requirements are that \(q_*,q_*+a,q_*-a\) are units
and that
\[
                         |1-\lambda^{-2}|\ge c>0 .
 \tag{8}
\]
The logarithm of \(\lambda\) is the continuation of the physical
real-degree branch. It is single valued on these product domains.
For real \(X\in J\), the same branch has \(|\lambda|>1\), uniformly
on compact second-parameter sets. No such modulus inequality is
required at a nonreal first degree.

Let
\[
                  \Psi(X,u)=\psi(\pi-2\pi X,u)
 \tag{9}
\]
be the original edge action on this continuation, with its real
calibration. It obeys
\[
                         \partial_X\Psi=\operatorname{Log}\lambda.
 \tag{10}
\]
Equivalently, fix its value at a real degree from the actual slit-row
profile and integrate (10). This fixes the constant, not just the
derivative. The two descriptions agree on real degree and hence on
the connected continuation chart.

**Theorem 1.** On every such chart there is a holomorphic unit
\(\mathcal A_N(X,u)\), anchored at an actual physical row
\(X_*=X_{j_*}\in J\), for which
\[
                         \mathcal A_N(X_*,u)=F_{j_*}(w(u)).
 \tag{11}
\]
On compact buffered subsets of \(\mathcal D_1\times V\),
\[
              \log\mathcal A_N-N\Psi=o(N)
 \tag{12}
\]
with compatible logarithms. On the physical window \(X_j\in I\),
\[
 \begin{split}
 \mathcal A_N(X_j,u)/F_j(w(u))-1&=O(e^{-\kappa N}),\\
 \frac{\partial_X\mathcal A_N(X_j,u)
                  -C'(X_j)\widehat G_j(w(u))}
      {F_j(w(u))}&=O(e^{-\kappa N})
 \end{split}
 \tag{13}
\]
for some fixed \(\kappa>0\). All assertions are uniform on the fixed
second-parameter compact, including every fixed exterior derivative.
On second-parameter compacts with \(\Re w<2\), the \(o(N)\) in
(12) is \(O(\log N)\).

There are holomorphic representatives \(\mathcal F_N^\sigma\),
\(\sigma=\pm1\), with the exact window identities
\[
 \mathcal F_N^\sigma(X_j,u)=F_j(w(u)),\qquad
 \partial_X\mathcal F_N^\sigma(X_j,u)
                       =C'(X_j)\widehat G_j(w(u)),
 \tag{14}
\]
and
\[
 e^{-N\Psi}(\mathcal F_N^\sigma-\mathcal A_N)
              =O(e^{-\kappa_1N})
 \quad\text{on }\mathcal D_1\cap\{\sigma\Im X\ge0\}.
 \tag{15}
\]
The estimate holds on every fixed compact part of that half-domain,
with no restriction on its fixed height beyond membership in the
chart. There is also a fixed sufficiently thin opposite collar.
Fixed derivatives cost only polynomial factors, absorbed by decreasing
\(\kappa_1\). In particular the representatives have the own-action
upper bound \(\exp\{N\Re\Psi+o(N)\}\).

At physical second endpoints (14) includes all original required
mixed jets. At its odd simple node only the value is prescribed.
This theorem concerns the bulk window (4), not the whole first grid.

## 2. Constructing a mode without off-real modulus ordering

In centered coordinates the exact coefficients are
\[
 A_h(X)=
 \frac{[2\sin(\pi X+\pi h/2)]^4}
      {4\sin(2\pi X)\sin(2\pi X+\pi h)},\qquad
 C_h(X)=
 \frac{[2\sin(\pi X-\pi h/2)]^4}
      {4\sin(2\pi X-\pi h)\sin(2\pi X)} .
 \tag{16}
\]
They are the original \(A(j),C(j)\) at \(X=X_j\).
The exact physical ratio \(\rho_j=F_j/F_{j-1}\) satisfies
\[
 \rho_{j+1}=f_h(X_j,u,\rho_j),\qquad
 f_h(X,u,z)=a_h(X,u)-b_h(X)z^{-1},
 \tag{17}
\]
where
\[
 a_h=1+(c_0-w(u))/A_h+C_h/A_h,\qquad b_h=C_h/A_h .
 \tag{18}
\]
On the buffered domains these coefficients, their inverses where
used, and their fixed derivatives are uniformly bounded. They have
holomorphic expansions at \(h=0\), with
\[
 b_0=1,\qquad a_0=2+(2-w(u))\cot^2(\pi X).
 \tag{19}
\]
Thus \(\lambda=f_0(X,u,\lambda)\).

We construct \(\mathcal R_N=\lambda+r_N\) such that
\[
 \mathcal R_N(X+h,u)-f_h(X,u,\mathcal R_N(X,u))
                           =O(e^{-cN}),\qquad r_N=O(h).
 \tag{20}
\]
Write \(L=1-\lambda^{-2}\), and define
\[
 \mathcal N(r)=(\lambda+r)-f_0(X,u,\lambda+r)-Lr.
 \tag{21}
\]
It is \(O(r^2)\), with Lipschitz constant \(O(h)\) on
\(|r|\le C_0h\). The shifted equation is equivalent to
\[
 \begin{split}
 Lr={}&[f_h-f_0](X,u,\lambda+r)
       -[\lambda(X+h,u)-\lambda(X,u)]\\
     &-[r(X+h,u)-r(X,u)]-\mathcal N(r).
 \end{split}
 \tag{22}
\]
This is an exact fixed-point equation, not a formal expansion.
Its constant term is \(O(h)\). On domains eroded by
\(\delta\ge2h\), Cauchy's estimate bounds its Lipschitz constant,
after multiplication by \(L^{-1}\), by
\[
                              C(h+h/\delta).
 \tag{23}
\]
All constants are uniform in the buffered exterior parameter.

Choose \(\delta=Mh\), with \(M\) a sufficiently large fixed number.
The map in (22), divided by \(L\), preserves a ball
\(\|r\|\le C_0h\) and contracts successive differences by at most
\(1/2\) between successive eroded domains. Starting from zero,
perform \(K\ge c_0/h\) iterations within a fixed part of the
available domain reserve. The last difference and the residual of
(22) are \(O(e^{-c_1/h})\). Reserve a further fixed buffer for
derivatives. This proves (20), with all fixed derivatives.
The construction is holomorphic in \(u\); evenness in \(u\), when
present in the parameter domain, is preserved at every iteration.

This is the scalar version of the nested-domain analytic graph
construction in the pinned continuation theorem. Its use here rests
on the explicit inverse \(L^{-1}\), not on a stable off-real
eigenvalue or on diagonalizing a varying matrix and ignoring the
coupling terms.

## 3. Real source comparison and the anchored primitive

On a sufficiently thin complex neighborhood of the enlarged real
interval, the actual slit ratio theorem gives
\[
 \rho_j=\lambda(X_j,u)+O(h),\qquad
 |\partial_zf_h(X,u,z)|\le\vartheta<1
 \tag{24}
\]
for \(z\) in the relevant neighborhoods of \(\lambda\).
The centered shift changes the pinned limiting argument by \(h/2\),
which is \(O(h)\); it changes no contraction assertion.

Let \(\mathcal R_N^{\,0}\) be the centered version of the ratio
interpolant in the pinned slit-normal theorem. Both it and (20)
are \(\lambda+O(h)\), both have exponentially small shifted
residual, and both are defined through a fixed earlier real buffer.
Iterating their difference along the common real-direction shifts
on this thin complex neighborhood gives
\[
        \mathcal R_N-\mathcal R_N^{\,0}=O(e^{-c_2N})
 \tag{25}
\]
on a smaller real tube, uniformly in the parameter. The initial
difference is \(O(h)\); its contribution is
\(\vartheta^{cN}O(h)\). The residuals sum to an exponential error.
This is the only use of attraction. It takes place in the actual
real-degree region where (24) is proved.

The unit \(\mathcal R_N\) has a holomorphic logarithm
\(\ell_N\) on the product chart, continued from
\(\operatorname{Log}\lambda\), and
\(\ell_N-\operatorname{Log}\lambda=O(h)\).
Use the same actual anchor \(X_*\) for the two mode constructions.
Define the finite Euler--Maclaurin primitive
\[
 \begin{split}
 L_N(X,u)={}&h^{-1}\int_{X_*}^{X}\ell_N(s,u)\,ds
       +\tfrac12[\ell_N(X,u)-\ell_N(X_*,u)]\\
 &+\sum_{\nu=1}^{p_N-1}
 \frac{B_{2\nu}h^{2\nu-1}}{(2\nu)!}
 [\partial_X^{2\nu-1}\ell_N(X,u)
          -\partial_X^{2\nu-1}\ell_N(X_*,u)],\\
 \mathcal A_N(X,u)={}&F_{j_*}(w(u))e^{L_N(X,u)},
                    \qquad p_N=\lfloor cN\rfloor .
 \end{split}
 \tag{26}
\]
Choose \(c>0\) sufficiently small relative to the fixed analytic
buffer radius. The factorial Cauchy and Bernoulli estimates in
the pinned interpolation proof give
\[
 L_N(X+h,u)-L_N(X,u)
                      =\ell_N(X+h,u)+O(e^{-c_3N}).
 \tag{27}
\]
This estimate applies to complex \(X\): the remainder is estimated
on the segment \([X,X+h]\) and its fixed complex neighborhood.
The higher endpoint terms in (26) have total size \(O(h)\).
The path-length bound and (10) consequently give
\[
 L_N(X,u)=N[\Psi(X,u)-\Psi(X_*,u)]+O(1).
 \tag{28}
\]

At the actual anchor the slit-row theorem gives
\[
 \log F_{j_*}(w(u))
   =N\Psi(X_*,u)+o(N).
 \tag{29}
\]
Its original profile uses \(j_*h=X_*-h/2\). The replacement by
\(X_*\) in (29) costs \(O(1)\) in the logarithm on the fixed
bulk and parameter compacts. The stronger half-plane source
estimate has \(O(\log N)\) in (29).
Equations (28)--(29) prove (12).

On the thin real tube, (25) and the same anchored construction
compare \(\mathcal A_N\) to the actual normalized mode in the
pinned slit-normal theorem with exponential relative accuracy.
Instantiate that earlier construction with the same truncation
order \(p_N\), chosen small enough for both sets of buffers.
For the terms of order growing with \(N\) in (26), Cauchy's
factorial bounds apply to (25) on a reserved larger tube; choose
the truncation constant smaller if needed. Their sum is still
exponentially small. The source's value and derivative conclusions
therefore give (13), including its actual independent normal
anchor. This proof does not assume that a normal is determined by
values alone.

For comparison with the new Sears formula, its exact identity is
\[
 \left.\partial_\alpha
   \sum_{k=0}^{j}T_k(\alpha,\beta)\right|_{\alpha=j}
   =c'(0)F_j(c(\beta))\widetilde Q_N(c(\beta))
                           +R_j(c(\beta)).
 \tag{30}
\]
It is precisely the normal used in (3). Thus the present mode
has the actual local Sears full-jet normalization. Equation (30)
does not identify this mode with the Sears cutoff sum away from
the physical rows. The latter's exact finite flux and diagonal
divisor have not been set to zero.

## 4. Exact repair at arbitrary designated height

Set \(v_N=e^{-N\Psi}\mathcal A_N\). At the nodes in \(I\) define
\[
 \begin{split}
 d_j(u)&=e^{-N\Psi(X_j,u)}F_j(w(u))-v_N(X_j,u),\\
 b_j(u)&=e^{-N\Psi(X_j,u)}
   [C'(X_j)\widehat G_j(w(u))
                 -N\Psi_X(X_j,u)F_j(w(u))]
                          -\partial_Xv_N(X_j,u).
 \end{split}
 \tag{31}
\]
Equations (12)--(13) imply \(d_j,b_j=O(e^{-\kappa N+o(N)})\).
Decrease \(\kappa\) once; these are uniform exponentially small
holomorphic parameter functions with all fixed derivatives.

For \(\sigma=\pm1\), put
\[
 \begin{split}
 \mathcal E_N^\sigma(X,u)
  =\sum_{X_j\in I}\big[d_j(u)
       +(b_j(u)-\sigma2\pi iN d_j(u))(X-X_j)\big]\,
       e^{\sigma2\pi iN(X-X_j)}
                  \operatorname{sinc}^2(N(X-X_j)),\\
 \mathcal F_N^\sigma
                  =e^{N\Psi}(v_N+\mathcal E_N^\sigma).
 \end{split}
 \tag{32}
\]
The value and derivative of the \(j\)-th summand at its own node
are \(d_j,b_j\); every other summand has a double zero there.
This proves (14) as identities of holomorphic functions of \(u\).

The kernel on the second line of the summand in (32) has Fourier
support \([0,2N]\) for \(\sigma=1\), and \([-2N,0]\) for
\(\sigma=-1\), with total absolute coefficient mass one.
Its modulus is at most one in the designated half-plane, and each
fixed \(X\)-derivative costs a power of \(N\). There are \(O(N)\)
terms, and \(X\) remains in a bounded set. This proves (15).
In the opposite half-plane the kernel is bounded by
\(e^{4\pi N|\Im X|}\), giving the stated fixed thin collar.
The repair need not be even in the first angular variable. It is
used in the closed window-contour identity below; no full-lens
replacement is inferred from angular parity.

If the second parameter domain is symmetric, the construction and
repair are even in \(u\). They therefore descend holomorphically
through its spectral fold \(w=-2\). Fixed spectral derivatives
there are obtained by holomorphic even descent and buffered Cauchy
estimates, not division by \(\sin u\).

The action upper bound follows directly from (12) and (15).
The common baseline also retains an exponentially accurate
normalized scalar recurrence: (20),(27) give it for
\(\mathcal A_N\), and finite shifts of the repaired normalized
errors remain exponentially small in the designated half-domain.
This does not make the raw finite Sears boundary small.

## 5. Positive reachability and coherent overlaps

The regular-domain hypotheses above are available at actual positive
configurations, not only on a small rectangle about real angles.
Fix a positive pair \((t_*,u_*)\), in the original
\(|\Re t|,|\Re u|<\pi\) strips, with \(t_*\ne0\).
The pinned product-domain theorem supplies simply connected symmetric
angular domains containing the full real intervals and the target,
on whose product
\[
                         q_*^2\notin(-\infty,0],\qquad \Re q_*>0.
 \tag{33}
\]
Their tangent-coordinate domains are star shaped. Moreover
\[
            (q_*+a)(q_*-a)=1+b^2\ne0,\qquad
            1-\lambda^{-2}=\frac{4q_*a}{(q_*+a)^2}.
 \tag{34}
\]
Thus the only loss of (8) in these domains is \(a=0\), namely
\(t=0\). Nonreal points with \(|\lambda|=1\) are not exceptions.

Connect a small positive real \(t\)-interval to \(t_*\) by a simple
compact path in the first angular domain avoiding zero. Such a
path exists: the real spine and the radial target arm belong to
the open tangent domain, and a small arc around zero joins them.
A thin bounded simply connected neighborhood of this path and the
real interval has closure avoiding zero and the angular endpoints.
Nested neighborhoods and the change (1) give (5), its bounded
path lengths and the coefficient margins in (16).
Choose a bounded buffered second-parameter neighborhood containing
the desired compact target set and a real interval inside the
second product domain. Equations (33)--(34) supply all the
remaining uniform units and logarithms. This construction is
locally uniform in the target pair and uses domains fixed before
\(N\).

The phase in (9) is the original branch on this path, since it
agrees at the real seed and its derivative is (10). No additive
phase is selected from an off-grid factorial endpoint.
If \(t_*=0\) but \(u_*\ne0\), one can interchange the roles for
a local construction. This observation does not make a single
first-degree chart cross its fold. The simultaneous complete point
and a whole first-grid fold neighborhood require their existing
separate constructions.

There is a useful quantitative overlap statement for two charts
using the same first-degree coordinate. Suppose their
constructions have a connected buffered common domain, the same
continued phase, and a common real seed window containing \(cN\)
physical nodes. Suppose the compact target overlap is connected
to that window through this common domain where both normalized
representatives have the bounds just proved. Then
\[
 e^{-N\Psi}(\mathcal F_{N,1}-\mathcal F_{N,2})
                                  =O(e^{-\kappa_{12}N})
 \tag{35}
\]
on that compact overlap, with fixed derivatives.

To prove this, the normalized difference has exact zeros at every
common physical node and has norm \(e^{o(N)}\) on a fixed real
tube. The disk Blaschke estimate used in the pinned normal theorem
therefore gives \(e^{-cN+o(N)}\) on a smaller open seed set.
A finite chain of buffered three-circles estimates propagates this
to the specified compact overlap. The \(o(N)\) upper exponents
remain negligible at each of finitely many steps. Work uniformly
on a slightly larger exterior parameter compact and then use
Cauchy for its derivatives. The same argument applies to the
baselines using their exponentially small nodal errors.

This statement requires the connected common domain and its shared
seed, or an already compared open subset. It does not control a
disconnected overlap, continuation around an unrecorded branch, or
an arbitrary raw cutoff transition merely because its physical
jets vanish. It is a controlled transport of the constructed
normalized modes. Comparison of the two constructions obtained by
interchanging the endpoint roles requires its own joint seed and
overlap argument; it is not included in (35).

## 6. The original window currents and the remaining obligation

Let \(\eta=(-1)^{N-1}\) and
\[
                         D_h(X)=(\pi/h)^2\sec^2(\pi X/h).
 \tag{36}
\]
Take midpoint vertical boundaries surrounding the selected centered
nodes and a window contour contained in the supplied domains.
Let \(P_N^{\rm sp}\) be the entire original remaining spectator,
with all shared variables and crossings, and set
\[
 g_\sigma(X)=\sin(2\pi X)\,
       \mathcal F_N^\sigma(X,u)P_N^{\rm sp}(C(X);\ldots).
 \tag{37}
\]
Write \(P_j^{\rm sp}=P_N^{\rm sp}(c_j;\ldots)\) and
\(P_{Z,j}^{\rm sp}=\partial_ZP_N^{\rm sp}(c_j;\ldots)\),
with every other shared variable held fixed. Define the finite
residue expression
\[
 \Phi_{N,I}^{\sharp}(w;\ldots)
 =\eta\sum_{X_j\in I}
 \left\{(4-c_j^2)
   [\widehat G_j(w)P_j^{\rm sp}
                  +F_j(w)P_{Z,j}^{\rm sp}]
                    -c_jF_j(w)P_j^{\rm sp}\right\}.
 \tag{37a}
\]
The closed two-half residue identity gives, exactly on \(V\),
\[
 \Phi_{N,I}^{\sharp}(w(u);\ldots)
  =-\frac{\eta}{2\pi^2i}
   \left\{\int_{E_-}D_hg_-\,dX+\int_{E_+}D_hg_+\,dX
                +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dX\right\}.
 \tag{38}
\]
Here \(E_-\) goes down the left side, across the lower horizontal
and up the right side; \(E_+\) goes up the right side, across the
upper horizontal and down the left side. Every vertical half-side
is retained. The representatives need not be even in the first
angle: (38) is the closed positive-window residue identity, not a
parity argument replacing an open full lens.

The actual original window trace is the same finite expression
with \(G_j\) in place of \(\widehat G_j\). Since (3) retains
every physical second-endpoint jet, holomorphic division on the
slit gives
\[
 \Phi_{N,I}^{\sharp}(w;\ldots)
 -\phi_{N,I}\big(K_N(Z,w)P_N^{\rm sp}(Z;\ldots)\big)
                        =P_N(w)\,\mathcal B_{N,I}(w;\ldots),
 \tag{38a}
\]
where \(\mathcal B_{N,I}\) is holomorphic on that slit, with all
other original variables retained. The spectator derivative in
(37a) is part of the identity. Equation (38a) preserves every
required mixed physical datum in the second endpoint, and proves
equality after its subsequent complete original trace, including
any further spectator and its normal product rule.

Thus the later complete second trace is taken on the globally
defined finite residue expression (37a), or on a covering which
retains every other second row. A single local \(V\)-contour is
not a whole-second-grid representative. Equation (38) itself
does not assert a free off-grid equality with the original
normal polynomial.

The baseline cancels in the real interface. The elementary identity
for \(D_h(\mathcal E_N^+-\mathcal E_N^-)\) in the pinned one-sided
source theorem has removable singularities at the physical nodes.
It gives, on the real window,
\[
 |D_h(g_+-g_-)|
 \le C e^{N\Re\Psi-\kappa_2N}
               |\sin(2\pi X)P_N^{\rm sp}(C(X);\ldots)|.
 \tag{39}
\]
Polynomial factors are absorbed by decreasing \(\kappa_2>0\).
The actual spectator is still present. This rate is not a
comparison with an unspecified parent action.

Likewise (35) controls seams between the constructed representatives
only with the indicated phase and connected-overlap hypotheses.
It does not delete the original exterior sides in (38), the rows
outside \(I\), a first-degree fold packet, or the finite Sears
flux if that raw representation is used elsewhere.
No claim is made that the positive geometric contour pays the
remaining currents, or that its local contribution survives their
sum. Those are the next whole-source estimates.

## Direct sources and author scope

The complete direct texts and their used implications were read at:

* [Actual slit normal connection](research_physical_row_slit_normal_connection.md),
  SHA256 a5084adb4ff25cb08020e5f9485bd1aaea5b49468c6ab0af311ebc1c0c504d99:
  actual ratios, full-normal anchor, finite analytic primitive and
  real-source comparison, slit bounds and dense-grid smallness.
* [Common baseline and one-sided repair](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_one_sided_characteristic_continuation.md),
  SHA256 1316cfb9ed7fec208a8aa8308ea7015c7cf32534a8662500892f9a62b5e9b475:
  nested-domain analytic iteration, exact one-sided Hermite kernels,
  removable real interface and full original window normalization.
* [Positive product domains](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  original discriminant and fixed product domains containing real
  seeds and positive targets, with all branches retained.
* [Exact Sears full normals](research_finite_sears_full_normal_source.md),
  SHA256 07f9db823f7eee2e5d6b48ecdb8c82875d60915b9c0211d6f375b4b318fc271c:
  exact local degree derivative and mixed-jet normalization, and
  the finite flux and diagonal divisor that remain in a raw cutoff.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
