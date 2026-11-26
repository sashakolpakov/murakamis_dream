# A signed coideal seam has a positive volume chamber

24 November 2026. Written research proof.

The actual overlap of two coideal channel frames is a mixed finite
Parseval kernel. On an explicit semialgebraic chamber, its whole signed
integral agrees, up to its known phase and an exponentially small
relative error, with its positive absolute integral. Its exponential
rate is the volume of one convex ideal octahedron obtained by sewing
two tetrahedral halves. The stationary equation closes their common
edge moduli; the halves are not maximized independently.

This gives nonzero coefficients of both actual signed crossings in a
single nested channel frame, with its full neighboring metric weights.
It does not show that an arbitrary component stays in this chamber
or make its prescribed marked closing positive.

## 1. The actual mixed finite kernel

Use T's and K's complete physical conventions
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \sqrt q=e^{\pi i/(2N)},\quad c=1+q,\quad
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N.
 \tag{1}
\]
The original crossing scalar is \(\kappa=q^{d^2/2}\).
The simple coideal roots and monic continuants are
\[
 \mathcal R_N=\{\mu_j=Q^j+qQ^{-j}:0\le j<N\},\qquad
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)),
\]
\[
 D_{-1}=0,\quad D_0=1,\quad
 D_{a+1}(\lambda;\sigma)
 =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                  -q(1-Q^a)^2D_{a-1}(\lambda;\sigma).
 \tag{2}
\]
Here \(T_N\) is Chebyshev. All physical endpoint arrows are retained.
For roots \(\lambda,\sigma\), put
\[
 \Phi_{\lambda,\sigma}(z)
       =\sum_{a=0}^d\frac{D_a(\lambda;\sigma)}{F_a}z^a,\qquad
 h_N(\lambda,\sigma)
       =\sum_{a=0}^d|D_a(\lambda;\sigma)/F_a|^2.
 \tag{3}
\]
T proves the complete degree-\(d\) product, including both parities:
if \(\lambda=\mu_j,\sigma=\mu_l,m=\lfloor N/2\rfloor\), then
\[
 \Phi_{\lambda,\sigma}(z)
 =(-qQ^lz;Q)_A(-q^2Q^{-l}z;Q)_{d-A},\quad
 A=\begin{cases}[m-j-l]_N,&N\ {\rm even},\\
                 [m+j-l]_N,&N\ {\rm odd}.
   \end{cases}
 \tag{4}
\]
In particular every zero lies on the unit circle, on the actual
\(\pi/N\) grid. No infinite product at a root is used. The exact
functional equation is
\[
 (1-\lambda z+qz^2)\Phi_{\lambda,\sigma}(z)
  =(1+q\sigma z+qQz^2)\Phi_{\lambda,\sigma}(Qz).
 \tag{5}
\]

For four roots define the full mixed coefficient and its positive
absolute integral by
\[
 \Sigma_N(\lambda_1,\sigma_1;\lambda_2,\sigma_2)
   =\sum_{a=0}^d
       \frac{\overline{D_a(\lambda_1;\sigma_1)}
                         D_a(\lambda_2;\sigma_2)}{|F_a|^2},
\]
\[
 A_N=\frac1{2\pi}\int_0^{2\pi}
       |\Phi_{\lambda_1,\sigma_1}(e^{it})
                       \Phi_{\lambda_2,\sigma_2}(e^{it})|\,dt.
 \tag{6}
\]
Ordinary finite Parseval identifies \(\Sigma_N\) with the same
integral having integrand
\(\overline{\Phi_{\lambda_1,\sigma_1}}\Phi_{\lambda_2,\sigma_2}\).
Every coefficient and phase is still the actual one.

## 2. An explicit semialgebraic chamber

Write the real root coordinates and principal angles as
\[
 a_i=\lambda_i/(2\sqrt q)=\cos\alpha_i,\qquad
 b_i=\sigma_i/(2\sqrt q)=\cos\beta_i,\qquad
 0\le\alpha_i,\beta_i\le\pi,\quad i=1,2.
\]
Define the following relative open chamber in \([-1,1]^4\):
\[
 a_i+b_j>0\quad(1\le i,j\le2),\qquad
 \Delta=(b_1+b_2-a_1-a_2)^2-8(a_1a_2+b_1b_2)<0.
 \tag{7}
\]
All uniform assertions mean uniformity on an arbitrary compact
subset \(\mathcal C\) of this chamber, for the actual root quadruples
lying there, and all sufficiently large levels. These are explicit
inequalities on the specified finite channels, not a geometric
placement assumption. They imply
\(\alpha_i+\beta_j<\pi\) for every pair.
Set
\[
 A=a_1+a_2+b_1+b_2>0,\qquad
 x_*=\frac{a_1a_2-b_1b_2}{A},\quad \Theta_*=\arccos x_*,
\]
\[
 \psi_i=\frac{\pi-\alpha_i-\beta_i}{2},\qquad
 u_i=\frac{\Theta_*-\alpha_i}{2}.
 \tag{8}
\]
Below we prove \(0<u_i<\psi_i\), uniformly away from their
endpoints on \(\mathcal C\). Let
\[
 \Lambda(v)=-\int_0^v\log|2\sin t|\,dt,\qquad
 W_i(u)=2\{\Lambda u+\Lambda(\alpha_i+u)
                    +\Lambda(\psi_i-u)+\Lambda(\psi_i+\beta_i-u)\},
\]
\[
                         V_{\rm sew}=\frac{W_1(u_1)+W_2(u_2)}2 .
 \tag{9}
\]
The extension of \(\Lambda\) is odd and \(\pi\)-periodic.

**Signed seam theorem.** Define
\[
 z_*=q^{-1/2}e^{-i\Theta_*},\qquad
 \eta_N=
 \frac{\overline{\Phi_{\lambda_1,\sigma_1}(z_*)}
                    \Phi_{\lambda_2,\sigma_2}(z_*)}
      {|\Phi_{\lambda_1,\sigma_1}(z_*)
                    \Phi_{\lambda_2,\sigma_2}(z_*)|}.
 \tag{10}
\]
For sufficiently large \(N\) these values are nonzero.
There are \(C_{\mathcal C},\epsilon_{\mathcal C}>0\) such that
\[
 \boxed{\quad
 \Sigma_N=\eta_N A_N(1+O_{\mathcal C}(e^{-\epsilon_{\mathcal C}N})),
 \qquad
 \log A_N=\frac N\pi V_{\rm sew}+O_{\mathcal C}(\log N).
 \quad}
 \tag{11}
\]
In particular the whole signed coefficient is nonzero and has this
same logarithmic rate. The phase in (10) is a specified finite
product value, not an uncalibrated square root or an unknown source.
The quantity \(V_{\rm sew}\) is the volume of the convex ideal
octahedron constructed in Section 5.

The acute box \(0\le\alpha_i,\beta_i\le\pi/3\) is one uniform
example: all \(a_i,b_i\ge1/2\), and \(\Delta\le1-4=-3\).
It is only an illustration of the single chamber (7).

## 3. The global stationary calculation, including the sign

Use the rotated circle \(z=q^{-1/2}e^{it}\).
T's finite log-cell proof gives the following uniform energies:
\[
 E_i(t)=\frac2\pi\left\{
 -\Lambda\frac{t+\alpha_i}2-\Lambda\frac{t-\alpha_i}2
 +\Lambda\frac{t+\pi-\beta_i}2
 +\Lambda\frac{t-\pi+\beta_i}2\right\}.
 \tag{12}
\]
Each has zero circle mean. The actual arc primitive has \(t+\pi/N\)
in its last two terms; this changes it uniformly by \(O(\log N/N)\).
In particular, with \(E=E_1+E_2\),
\[
 E'(t)=\frac1\pi\log\left|
       \frac{(\cos t-a_1)(\cos t-a_2)}
            {(\cos t+b_1)(\cos t+b_2)}\right|.
 \tag{13}
\]
This formula retains the action constant, not only its derivative.

Here is a global sign proof. Put
\[
 n(x)=(x-a_1)(x-a_2),\qquad d(x)=(x+b_1)(x+b_2).
\]
Their sum and difference satisfy
\[
 n-d=A(x_*-x),\qquad
 n+d=2x^2+(b_1+b_2-a_1-a_2)x+a_1a_2+b_1b_2>0.
 \tag{14}
\]
The strict positivity is exactly the negative-discriminant
condition in (7). Hence the sign of
\(\log|n(x)/d(x)|\) is the sign of \(x_*-x\), off its finite
zeros and poles. All cross sums are positive, so
\[
       \max(-b_1,-b_2)<x_*<\min(a_1,a_2).
 \tag{15}
\]
Indeed at the upper endpoint \(n=0,d>0\); at the lower endpoint
\(d=0,n>0\), and (14) gives the two strict inequalities.
Thus \(-1<x_*<1\) and
\[
       \max(\alpha_1,\alpha_2)<\Theta_*<
                                  \min(\pi-\beta_1,\pi-\beta_2).
 \tag{16}
\]
This proves the claims following (8).

The unique global maximum of \(E\) is \(t=-\Theta_*\);
the unique minimum is \(+\Theta_*\). On \((-\pi,0)\) the
derivative in (13) changes from positive to negative only there;
on \((0,\pi)\) it changes in the reverse direction. Logarithmic
cusps have the same sign on their two sides. They introduce no
additional maximum. In the common root-free interval (15),
\[
 \frac{d}{dx}\log\frac{n(x)}{d(x)}
  =-\sum_{i=1}^2\left\{\frac1{a_i-x}+\frac1{x+b_i}\right\}<0 .
 \tag{17}
\]
The maximum is nondegenerate. Compactness supplies a uniform
negative second derivative near it and a uniform strict loss on
the complement of any sufficiently small fixed-radius neighborhood.

For \(t=-\Theta\) in the common negative arc, put
\(u_i(\Theta)=(\Theta-\alpha_i)/2\).
The periodic primitive in (12) gives, exactly,
\[
 E_i(-\Theta)=W_i(u_i(\Theta))/\pi,\qquad
              \frac12\max E=V_{\rm sew}/\pi.
 \tag{18}
\]
There is no free additive boundary constant.

The sign distinction has a direct finite-kernel meaning.
Writing \(\Phi_i(z)=\prod_{\rho}(1-\rho z)\), every \(|\rho|=1\);
therefore on \(|z|=1\),
\[
 \overline{\Phi_i(z)}
      =(-1)^d\overline{\prod_\rho\rho}\ z^{-d}\Phi_i(z).
 \tag{19}
\]
Consequently the analytic integrand of (6), up to that constant
phase, is \(z^{-d}\Phi_1(z)\Phi_2(z)\). By (5) its exact
\(Q\)-step ratio is
\[
 Q^{-d}\mathcal R_{\lambda_1,\sigma_1}(z)
               \mathcal R_{\lambda_2,\sigma_2}(z),\qquad
 \mathcal R_{\lambda,\sigma}(z)
       =\frac{1-\lambda z+qz^2}{1+q\sigma z+qQz^2}.
 \tag{20}
\]
The principal full-phase stationary equation is \(n(x)=d(x)\),
not merely \(|n(x)|=|d(x)|\). The potential alternative \(n=-d\)
has no real solution in (7), by (14). At the actual maximum each
individual ratio is negative, and their product is positive one.

## 4. Whole-circle phase control and the quantitative lower bound

The actual finite zeros stay away from a neighborhood of
\(-\Theta_*\), uniformly on \(\mathcal C\).
Here is an endpoint check rather than a continuum assumption.
In the rotated variable, the two zero strings in (4) start at
\(\pi-\pi/N\pm\beta_i\) and run down with step \(2\pi/N\)
to the two endpoints \(\pm\alpha_i\), with their last endpoints
excluded. Since \(\alpha_i+\beta_i<\pi\), representatives can be
chosen so both arcs run through the positive half-circle.
They leave the negative interval
\((-\pi+\beta_i,-\alpha_i)\) empty up to \(O(N^{-1})\)
endpoint shifts. The two such gaps have the common interior (16).
Their endpoint margins on \(\mathcal C\) are strictly positive.
This pays the root phase, both string orders and all finite endpoints.

On any connected zero-free arc, (19) says
\(\Phi_i(q^{-1/2}e^{it})e^{-idt/2}\) has constant phase up to
a constant sign. Thus the product
\(\overline{\Phi_1(q^{-1/2}e^{it})}\Phi_2(q^{-1/2}e^{it})\)
has exactly constant phase there. On the common dominant arc this
phase is \(\eta_N\) from (10); there is no residual \(t\)-chirp.

For explicit estimates, T's log-cell comparison yields globally
\[
 \log|\Phi_i(q^{-1/2}e^{it})|^2
                       \le NE_i(t)+C_{\mathcal C}\log N.
 \tag{21}
\]
It remains valid at exact zeros. On a fixed neighborhood \(I_*\)
of \(-\Theta_*\) inside the common gap, the same comparison is
two-sided. The proof removes the finitely many cells closest to
the logarithmic zeros, estimates the rest by
\(\int|\cot(t/2)|=O(\log N)\), and uses the exact \(\pi/N\)
endpoint correction in (12). In \(I_*\) all factors are uniformly
away from zero; no omitted boundary current is used.

Let
\(M=\tfrac12 E(-\Theta_*)=V_{\rm sew}/\pi\).
At the maximum the product magnitude is at least
\(e^{NM}N^{-C_{\mathcal C}}\).
Its logarithmic derivative on \(I_*\) is bounded by
\(C_{\mathcal C}N\), since it is a product of \(2d\)
uniformly nonzero circle factors. Integrating an interval of
width \(N^{-2}\) gives
\[
 N^{-C_{\mathcal C}}e^{NM}
 \le\frac1{2\pi}\int_{I_*}|\Phi_1\Phi_2|\,dt
 \le N^{C_{\mathcal C}}e^{NM}.
 \tag{22}
\]
The global strict loss from Section 3 and (21) give
\[
 \frac1{2\pi}\int_{I_*^c}|\Phi_1\Phi_2|\,dt
       \le N^{C_{\mathcal C}}e^{N(M-\gamma_{\mathcal C})}.
 \tag{23}
\]
Both the signed and absolute complements obey this bound.
On \(I_*\) their phases agree exactly. Dividing (23) by (22),
and decreasing the positive exponent once to absorb the powers
of \(N\), proves (11) for the entire circle.
No local Gaussian prefactor or unproved contour replacement is needed.

The phase has an exact single-height formula. Sort the roots as
\(\lambda_r=2\sqrt q\cos\alpha_r\),
\(\alpha_r=(r+\tfrac12)\delta\), \(0\le r\le d\), \(\delta=\pi/N\).
For a cooriented pair \(r+s\le N-2\), use the RAW circle angle
\(\vartheta\in(-\pi+s\delta,-(r+1)\delta)\). Then
\[
 \Phi_{\lambda_r,\lambda_s}(e^{i\vartheta})
       =\gamma_{rs}e^{id\vartheta/2}
                              |\Phi_{\lambda_r,\lambda_s}(e^{i\vartheta})|,
 \quad
 \gamma_{rs}=e^{i\pi d/4}\frac{f_r}{f_s},\quad
 f_r=\exp\{i\delta r(r+1)/4\}.
 \tag{24}
\]
Here is the sign and branch calculation. The two raw zero strings
start at \(\xi_\pm=\pi-3\delta/2\pm\alpha_s\) and descend with
step \(2\delta\), ending one step before
\(-\delta/2\pm\alpha_r\). Their counts are
\(n_\pm=(d\pm h)/2\), where \(h=s-r\) if \(N+r+s\) is odd
and \(h=s+r+1\) otherwise. They are nonnegative integers.
All unwrapped zeros lie outside the stated negative gap, with
every \(\vartheta-\xi\in(-2\pi,0)\). Each factor therefore has
phase \(+i e^{i(\vartheta-\xi)/2}\). Moreover
\[
 \sum\xi=d\pi-\delta d(d+1)/2+\alpha_s h-\delta h^2/2
       =\pi d/2+\delta\{s(s+1)-r(r+1)\}/2.
\]
Thus \(\gamma_{rs}=i^d e^{-i\sum\xi/2}\), proving (24) at
both parities, including \(N=2\). It also gives
\(D_d(\lambda_r;\lambda_s)/N=\gamma_{rs}^2\).
The common rotation to \(t\) multiplies each individual phase
by \(q^{-d/4}\); it cancels from the mixed phase \(\eta_N\).

For the two pairs in the theorem, (24) gives exactly
\(\eta_N=\overline{\gamma_{r_1s_1}}\gamma_{r_2s_2}\).
By (19) the phase-removed integrand is real on the entire circle,
so \(\eta_N^{-1}\Sigma_N\) is exactly real. The lower bound
above makes it strictly positive for large \(N\).
This is a row/column phase factorization with explicit quadratic
single-height factors. It does not assert a globally compatible
gauge or alignment of the original cup and cap coefficients.

## 5. Sewing four tetrahedra into a convex ideal octahedron

For each \(i=1,2\) take one tetrahedron of each type
\[
 A_i=(u_i,\psi_i-u_i,\pi-\psi_i),\qquad
 B_i=(\alpha_i+u_i,\psi_i+\beta_i-u_i,\psi_i).
 \tag{25}
\]
All their angles are positive. Use the cyclic order
\(A_1,B_1,A_2,B_2\) around a prospective common edge.
Its angles sum to \(2\pi\), since each half contributes \(\pi\).
Unlike the individual octahedra of T, each half here is not
separately required to close its edge moduli.

Put
\[
 z_i=\frac{\sin u_i}{\sin(\psi_i-u_i)}e^{i(\pi-\psi_i)},\quad
 w_i=\frac{\sin(\alpha_i+u_i)}{\sin(\psi_i+\beta_i-u_i)}
                                                        e^{i\psi_i},
\]
\[
 \rho_i=
 \frac{\sin u_i\sin(\alpha_i+u_i)}
      {\sin(\psi_i-u_i)\sin(\psi_i+\beta_i-u_i)}>0 .
 \tag{26}
\]
Then \(z_iw_i=-\rho_i\). The sine product identity and (8) give
\[
 \rho_i=-\frac{x_*-a_i}{x_*+b_i},\qquad
                         \rho_1\rho_2=1.
 \tag{27}
\]
The last equality is exactly \(n(x_*)=d(x_*)\).
Thus the four successive shape ratios \(z_1,w_1,z_2,w_2\)
have product one, including its argument. They develop with poles
\(0,\infty\) and equatorial vertices
\[
       p_0=1,\quad p_1=z_1,\quad
       p_2=-\rho_1,\quad p_3=-\rho_1z_2,\quad p_4=p_0.
 \tag{28}
\]
The ordinary sine rule gives precisely the angle triples (25).

We check all supporting faces. The equator has strictly ordered
arguments with increments
\(\pi-\psi_1,\psi_1,\pi-\psi_2,\psi_2\), each in \((0,\pi)\).
It is a simple star-shaped quadrilateral around zero.
Its link angles at \(\infty\), at the two interior-half vertices
and the two joins respectively, are
\[
 \psi_i+\alpha_i,\qquad
       \frac{\pi+\beta_1-\alpha_2}{2},\quad
       \frac{\pi+\beta_2-\alpha_1}{2}.
 \tag{29}
\]
To see the joins, use \(u_1-u_2=(\alpha_2-\alpha_1)/2\);
for example one is \(\psi_1+\beta_1-u_1+u_2\).
All four angles are in \((0,\pi)\). The quadrilateral is
therefore strictly convex, so its four vertical side planes support.

At the other pole the interior-half angles are
\(\psi_i+\beta_i\); its join angles are
\[
       \frac{\pi+\alpha_1-\beta_2}{2},\qquad
       \frac{\pi+\alpha_2-\beta_1}{2}.
 \tag{30}
\]
They too lie in \((0,\pi)\). Apply the boundary Möbius map
\(z\mapsto-1/z\), exchanging \(0\) and \(\infty\).
The reciprocal equatorial quadrilateral is again simple and
star-shaped by its ordered arguments; (30) and the two remaining
angles make it strictly convex. Its vertical side planes support.
Undoing the isometry gives the four supporting hemispheres at zero.
Hence all eight planes support the six vertices in (28), and the
four positive tetrahedra fill their convex ideal octahedron.

Its volume is the sum of their four ordinary tetrahedral volumes.
The opposite \(\Lambda(\psi_i)\) terms cancel within each half,
giving precisely \(V_{\rm sew}\) in (9). At the common classical
corner \(\alpha_i=\beta_i=0\), one has
\(\Theta_*=\pi/2,u_i=\pi/4,\rho_i=1\); this is the regular ideal
octahedron of volume \(4G_{\rm Cat}\).
This is a genuinely sewn cell: a shared phase variable and the
full equation (27) impose its edge modulus, not independent
maximization of two positive graph weights.

## 6. Both actual crossing signs in one nested physical frame

Let \(U_\sigma\) have columns
\((U_\sigma)_{a,\lambda}=q^{-a}D_a(\lambda;\sigma)/F_a\),
and set \(\mathcal D e_a=q^{-a}e_a\),
\(V_\nu=\mathcal D\overline{U_\nu}\).
T gives the phase-exact conditional crossing
\[
 C_{\nu|\sigma}=\kappa V_\nu U_\sigma^{-1}.
\]
K's normalized inverse row is
\((U_\sigma^{-1})_{\lambda,a}
 =[E_d(\lambda;\sigma)/p_N'(\lambda)]
                                      D_a(\lambda;\sigma)/F_a\).
Here \(E_d\) is the trailing continuant, not a chosen adjoint.
Consequently the positive and negative crossings in the SAME
\(U_\sigma\) coordinates have entries
\[
 B^+_{\lambda',\lambda}
  =\kappa\frac{E_d(\lambda';\sigma)}{p_N'(\lambda')}
       \Sigma_N(\lambda,\nu;\lambda',\sigma),\qquad
 B^-_{\lambda',\lambda}
  =\kappa^{-1}\overline{\frac{E_d(\lambda';\nu)}{p_N'(\lambda')}}
       \Sigma_N(\lambda',\nu;\lambda,\sigma).
 \tag{31}
\]
The second matrix is the exact inverse of the first. No conjugate
phase or common Cartan scalar has been replaced by its modulus.
Conjugate reversal of the tridiagonal minors and the determinant
identity in K give, for any two roots,
\[
 |E_d(\lambda;\sigma)|=N,\qquad
 |p_N'(\lambda)|=N/\sin\alpha_\lambda .
 \tag{32}
\]
Indeed \(E_d=q^d\overline{D_d}\) and \(D_dE_d=q^dN^2\).
Thus their ratios lie between \(\sin(\pi/(2N))\) and one.
They have only polynomial size and inverse size.

Both signs in fact have one common amplitude. Put
\(\mathfrak p_d=[z^d](\Phi_{\lambda',\sigma}\Phi_{\lambda,\nu})\).
Multiplying (5) shows that every product coefficient of degree
\(<N\) is determined successively by \(1-Q^a\ne0\), with
constant term one. The two quadratics on each side are separately
symmetric in \(\{\lambda',\lambda\}\) and \(\{\nu,\sigma\}\).
Thus \(\mathfrak p_d\) is unchanged by either exchange.
If \(L_1,L_2\) are the two unit leading coefficients,
self-inversivity gives
\(\overline{\mathfrak p_d}=\overline{L_1L_2}\mathfrak p_d\).
Using \(E_d=q^dN\overline L\) in (31) now yields, at all channels,
\[
 B^+_{\lambda',\lambda}
       =\frac{\kappa q^dN}{p_N'(\lambda')}
                                      \overline{\mathfrak p_d},
 \qquad B^-_{\lambda',\lambda}=\overline{B^+_{\lambda',\lambda}}.
 \tag{32a}
\]
This is entrywise conjugation in the stated frame; it is not a
physical-adjoint or positive-metric assertion.

For the four roots \((\lambda,\lambda',\nu,\sigma)\), condition
(7) is unchanged by exchanging \(\lambda,\lambda'\).
The sum \(E_1+E_2\), and hence \(V_{\rm sew}\), is also unchanged:
formula (12) separates its two \(\alpha\) and two \(\beta\) terms.
Therefore both entries in (31) are nonzero in this chamber and
\[
             \log|B^\pm_{\lambda',\lambda}|
                    =NV_{\rm sew}/\pi+O_{\mathcal C}(\log N).
 \tag{33}
\]
Their individual phases are specified by (10), (31), not identified
with each other. These are actual signed matrix coefficients.

More explicitly, let the sorted input, output, external and deeper
indices be \(r,r',v,s\), and set
\(\tau_N=\kappa q^{d/2}i^{-d}\). Then
\[
 B^+_{r',r}
  =\tau_N(-1)^{r'}\sin\alpha_{r'}
           \frac{f_vf_s}{f_{r'}f_r}\,J_N,\qquad
 B^-_{r',r}
  =\overline{\tau_N}(-1)^{r'}\sin\alpha_{r'}
           \frac{f_{r'}f_r}{f_vf_s}\,J_N ,
 \tag{33a}
\]
where \(J_N>0\) is their common phase-removed sum, with
\(\log J_N=NV_{\rm sew}/\pi+O_{\mathcal C}(\log N)\).
Indeed \(p_N'(\lambda_{r'})=
Nq^{d/2}(-1)^{r'}/\sin\alpha_{r'}\) and
\(E_d(\lambda_r;\lambda_s)=q^dN/\gamma_{rs}^2\).
Inserting (24) proves both formulas; (32a) equates the positive
amplitudes. Positive metric normalization
below changes no phase in (33a).

For clarity the complete nested metric has both incident weights.
On \(b\) physical heads let \(\nu_b=c\), and choose the successive
suffix heights \(\nu_0,\ldots,\nu_{b-1}\) in \(\mathcal R_N\).
The exact path vector is
\[
 v_{\boldsymbol\nu}
  =\bigotimes_{r=1}^b\left\{
       \sum_{a=0}^d q^{-a}
           \frac{D_a(\nu_{r-1};\nu_r)}{F_a}e_a\right\},\qquad
 \|v_{\boldsymbol\nu}\|_{\rm ph}^2
                     =\prod_{r=1}^b h_N(\nu_{r-1},\nu_r).
 \tag{34}
\]
Tail-up recurrence proves the stated eigenvalues for every nested
suffix. First-coordinate elimination proves completeness: there
are \(N^b\) independent paths. Define the physical joint Haar form
by summing \(P_{\boldsymbol\nu}^*P_{\boldsymbol\nu}\) over these
full joint idempotents. It makes the paths orthogonal, keeping
their displayed physical norms. Its logarithmic radius is \(O_b(N)\),
by the bounded generators, \(|p_N'|\ge N\), and their projector products.

An original \(R_i^\pm\) commutes with every suffix total except
the one starting at head \(i+1\). It changes only \(\nu_i=\lambda\)
to \(\lambda'\), preserving its neighbors
\(\nu=\nu_{i-1}\), \(\sigma=\nu_{i+1}\) and every other height.
Its same-frame entry is (31). Normalizing the path vectors in
this full Haar form therefore multiplies it by
\[
       \left[\frac{h_N(\nu,\lambda')h_N(\lambda',\sigma)}
                    {h_N(\nu,\lambda)h_N(\lambda,\sigma)}\right]^{1/2}.
 \tag{35}
\]
Both neighboring weights are compulsory. T's removed-head
tail-pair form omits the outer edge and is a different metric.
For the normalized entries, (33) and T's uniform two-label rate give
\[
 \log|\widehat B^\pm_{\lambda',\lambda}|
 =\frac N\pi\left\{V_{\rm sew}
   +\frac{\mathcal V(\nu,\lambda')+\mathcal V(\lambda',\sigma)
          -\mathcal V(\nu,\lambda)-\mathcal V(\lambda,\sigma)}2\right\}
       +O_{\mathcal C,b}(\log N).
 \tag{36}
\]
Here \(\mathcal V(\xi,\zeta)\) uses T's folded root angles.

## 7. The original source and the remaining assembly problem

For a paired plat \(b=2k\), K and G retain exactly
\[
 u_0=p^{\otimes k}=L_cz_0,\qquad
 \mathcal K_N=\chi_N\ell_0R u_0
             =\chi_N\ell_0L_c\,R_cz_0 .
 \tag{37}
\]
The saturated regular source lies in the external height
\(\nu_0=c\). Changing to (34), or to its orthonormal Haar frame,
must transform both this exact input and the original marked row.
Other path vectors are not asserted to belong to that source.
All Casimir first normals remain in these full invertible finite maps.

The signed-to-positive comparison (11) concerns the stated complete
local coefficient. Its separable phases do not show that all adjacent
face phases cancel, that the initial coefficients have a positive
sign, or that the original marked cap selects this chamber.
An arbitrary short component need not keep its intermediate four
heights in (7). Its complementary channels and coherent sums remain.
No original closed-scalar lower bound, selected global cycle, new knot-volume class,
or finite-exception theorem is asserted.

A already gives an actual all-entry, phase-bearing reassociation
with affine-angle half-densities and exact charge incidence.
D already retains its mixed doubled Gram and shows why the dephased
path majorant cannot be assumed sharp. T supplies the present finite
coideal kernels and individual graph-volume profiles; K and G retain
their original source. No novelty for recoupling, finite Parseval,
or general Laplace methods is claimed. The additional assertions here
are the explicit semialgebraic signed chamber, its whole-circle
noncancellation estimate with calibrated phase, and the sewn
four-tetrahedron cell for the actual same-frame coefficients.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| T | [Exact coideal crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| G | [Graph Gram and local volume](research_coideal_graph_gram_and_octahedral_volume.md) | 398 | 35ca803fb3262b1f85a08c3aa9b9112bcc2823ce380ce82362ef18bd382d6766 |
| A | [Actual reassociation angle kernel](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_reassociation_angle_kernel.md) | 286 | d24fdbb93c9fecafa3f6b7e47b4962656f421196a8b50048816699e618f879aa |
| D | [Full doubled reassociation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_doubled_reassociation_angle_transfer.md) | 270 | 82350cee3e3905bba19970ab577f2ecc783e98d9f534fba6dceff40239137f12 |

Only written mathematics and text/hash operations were used. Earlier
final notes, the ledger and public manuscripts remain unchanged.
