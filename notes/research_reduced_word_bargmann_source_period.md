# The actual reduced word as a closed finite Bargmann period

Private written proof, 18 November 2026.

The Cartan first-meridian-jet formula has an exact closed
Gaussian period built from the known reduced generators.
Both sides of every interface are specified. The identity
kernel is a finite exponential polynomial; its cutoff and
all upper and lower projectors remain. A paired kernel
estimate gives exponential control of the Gaussian ends
using elementary bounds on the local matrices.

This also places a lower, resolved row endpoint in finite
complex Bargmann coordinates after the actual factorial
gauge. It does not place that point on the original real
cycle or prove that its contribution survives the closed
pairing. The common meridian varies at fixed \(q_N\);
ordinary-color quantum normals are not inferred.

The complete proof directs are R, H, V, D and G, pinned
below. The earlier compact coherent source and its
two-mode realization were read for coverage. The
one-mode normalization and estimates used here are
proved directly.

## 1. Finite kernels, their dual, and the original first jet

Put \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(x=-M/q\).
There are \(r=m-1\) remaining heads. Let
\[
 f_a=(Q;Q)_a,\qquad G_Fw_a=f_aw_a,\qquad
 \mathcal G=G_F^{\otimes r}.
 \tag{1}
\]
All these diagonal entries are nonzero. For the actual
reduced word \(B(M)=\mathcal B_m(W(M))\) of R set
\[
                         T(M)=\mathcal G^{-1}B(M)\mathcal G .
 \tag{2}
\]
The gauge depends on \(q\), not on \(M\). It commutes
with the remaining Cartan. Consequently both \(B\)
and its actual fixed-\(q\) meridian derivative can
be replaced by \(T\) and \(T'\) in H's trace formula.

For any matrix \(A\) on these finite heads define
\[
 \mathcal K_{A,N}(z,w)
       =\sum_{a,b\in\{0,\ldots,d\}^r}
          z^a A_{ab}\frac{(Nw)^b}{b!},\qquad
 d\mu_N(u)=\left(\frac N\pi\right)^r
                         e^{-N|u|^2}\,d^{2r}u .
 \tag{3}
\]
The variables \(z,w\) are independent complex variables.
The dual is exactly \((Nw)^b/b!\), not an unweighted
evaluation row. Angular integration and integration
by parts give
\[
 \int u^a\overline u^{\,b}\,d\mu_N(u)
                     =\mathbf1_{a=b}\frac{a!}{N^{|a|}} .
 \tag{4}
\]
It follows by multiplying the finite sums that
\[
 \int\mathcal K_{A,N}(z,\overline u)
              \mathcal K_{B,N}(u,w)\,d\mu_N(u)
                      =\mathcal K_{AB,N}(z,w),\qquad
 \int\mathcal K_{A,N}(u,\overline u)\,d\mu_N(u)
                      =\operatorname{Tr}A .
 \tag{5}
\]
These are absolutely convergent integrals of finite
polynomials against a Gaussian. No infinite head
or occupation interpolation is involved.

Write
\[
 x_0=-q^{-1},\qquad
 \varepsilon=(-1)^{(N+1)r},\qquad
 \mathcal I_\pm(M)=
       \int\mathcal K_{T(M),N}(Q^{\mp1}u,\overline u)\,d\mu_N(u).
 \tag{6}
\]
The simultaneous rotation acts on every remaining
output coordinate. Since the actual complete Cartan
has eigenvalue \(x_0^rQ^{-\sum a_j}\), (5) gives
\[
 \operatorname{Tr}(K_0^{\pm1}B(M))
                         =x_0^{\pm r}\mathcal I_\pm(M).
 \tag{7}
\]
H's original pointed/pivotal source is therefore
\[
 \boxed{\quad
 \Phi_0(W(1))
   =\frac{x_0^r\mathcal I_+(1)+x_0^{-r}\mathcal I_-(1)}
            {2\varepsilon}
    +\frac{x_0^r\mathcal I_+'(1)-x_0^{-r}\mathcal I_-'(1)}
            {2\varepsilon m}.
 \quad}
 \tag{8}
\]
Its exact residue constraint is
\[
                  x_0^r\mathcal I_+(1)
                       -x_0^{-r}\mathcal I_-(1)=0 .
 \tag{9}
\]
The derivative in (8) is applied to the actual \(T(M)\).
There is no derivative of a reset coupon or of the
frozen complete Cartan in (7). Any separately prescribed
external scalar multiplies the original source unchanged.
For the empty remaining tensor, the integrals mean the
corresponding scalar evaluations.

## 2. A closed integral of known local arrays

Factor \(B=A_L\cdots A_1\) by R's literal reduced
generators: physical signed crossings on the remaining
heads, or \(\kappa S_rD\) and its inverse. Identity
legs, finite pivots, and specified matrix insertions
are included as their actual arrays. Put
\(T_\ell=\mathcal G^{-1}A_\ell\mathcal G\).
Then (6) is the explicit closed period
\[
 \mathcal I_\pm=
 \int
 \mathcal K_{T_L,N}(Q^{\mp1}u_0,\overline u_{L-1})
 \mathcal K_{T_{L-1},N}(u_{L-1},\overline u_{L-2})
 \cdots
 \mathcal K_{T_1,N}(u_1,\overline u_0)
                    \prod_{\ell=0}^{L-1}d\mu_N(u_\ell).
 \tag{10}
\]
For \(L=1\) this means (6). Tensor identities give
the identical formula for a partially factored
network. The number of integration variables is
fixed by the finite word, independently of \(N\).
At fixed \(N\), the entire product is a finite
polynomial times the product Gaussian, so Fubini
and the meridian product rule are legitimate.

More general local gauge choices are also exact,
but their interfaces cannot be omitted. If
\(\mathcal G_\ell\) is the chosen basis on the
\(\ell\)-th interface, use
\[
             T_\ell=\mathcal G_\ell^{-1}
                                      A_\ell\mathcal G_{\ell-1}.
 \tag{11}
\]
For a closed chain take \(\mathcal G_L=\mathcal G_0\).
A diagonal quadratic chirp \(J_a=Q^{a(a-1)/2}\), for
example, must occur on both incident kernels in
this manner. Such \(J\)'s and \(G_F\)'s commute
with the Cartan insertion and are independent of
the fixed-\(q\) meridian derivative. If a chosen
gauge depends on \(M\), differentiate both sides
of (11), including every interface term.

The first-jet reduction (8) requires H's actual
intertwining family. Formula (5) represents arbitrary
marked matrices as well, but it does not promote
a marked nonintertwiner to that family. Its original
Ward/source defects must then be kept separately.

## 3. The finite cap and the donor kernel are both retained

For one head put \(E_d(s)=\sum_{a=0}^d s^a/a!\).
The identity kernel and the individual occupation
projector are
\[
 \mathcal K_{I,N}(z,w)=E_d(Nzw),\qquad
 \mathcal K_{P_a,N}(z,w)=z^a(Nw)^a/a! .
 \tag{12}
\]
Thus all finite windows and their endpoints are
literal sums of these kernels. In particular,
the exact Cauchy representation
\[
 E_d(s)=\frac1{2\pi i}\oint_{|\zeta|=\rho}
       e^{s/\zeta}\frac{1-\zeta^N}{1-\zeta}\,\frac{d\zeta}{\zeta},
                      \qquad \rho>0,\quad \rho\ne1 ,
 \tag{13}
\]
follows by multiplying its two finite/Taylor series.
The quotient at \(\zeta=1\) is removable. Equation
(13) retains its numerator \(1-\zeta^N\); it is
not a replacement by an infinite exponential
projector off the real cycle.

The exact donor result D inserts in (10) without
changing its dual. For a star on \(s\) heads let
the donor be coordinate \(1\) and let
\(b=(b_2,\ldots,b_s)\) be the actual integer
recipient input. D supplies
\[
 \mathcal C^\pm_{N,b}(\lambda,z)
      =P_b\sum_{a=0}^d\frac{\lambda^a}{a!}K_a^\pm(z;b),
 \tag{14}
\]
where \(P_b\) is its exact recipient upper projector.
Consequently the full kernel in (3) is exactly
\[
 \mathcal K_{\mathcal G^{-1}S_s^{\pm1}\mathcal G,N}(z,w)
   =\sum_{b_2,\ldots,b_s=0}^d
       \left(\prod_{j=2}^s\frac{(Nz_jw_j)^{b_j}}{b_j!}\right)
                       \mathcal C^\pm_{N,b}(Nw_1,z).
 \tag{15}
\]
Both the external recipient monomial of D and
its factorial dual are visible in (15). Any
spectator identities are (12), and all neighboring
Cartan or chirp matrices remain in (10)--(11).

D's relative Gaussian estimate applies to each
factored term of (15) when \(|Nw_1|=O(\sqrt N)\)
and the actual integer recipients have its
specified macroscopic upper margin. Outside that
margin the exact \(P_b\) remains. Equation (15)
does not interpolate the \(b_j\)'s to complex
geometric occupations or discard their sum.

## 4. A paired bound and Gaussian end control

The monomial metric underlying (4) is
\[
 H_a=a!/N^{|a|}.
 \tag{16}
\]
Write \(\|A\|_H\) for its operator norm and
\(\Pi_N(z)=\prod_{j=1}^rE_d(N|z_j|^2)\).
Evaluation and its exact dual, followed by
Cauchy--Schwarz in this finite-dimensional metric,
give
\[
 |\mathcal K_{A,N}(z,\overline w)|
                 \le \|A\|_H\sqrt{\Pi_N(z)\Pi_N(w)} .
 \tag{17}
\]
This estimate pairs the two ends of the kernel.
It is not a bound on a coherent column without
its dual. In the closed product (10) every
interface occurs once on each side. Since the
Cartan rotation has modulus one, its absolute
integrand is bounded by
\[
                  \left(\prod_{\ell=1}^L\|T_\ell\|_H\right)
                      \prod_{\ell=0}^{L-1}\Pi_N(u_\ell).
 \tag{18}
\]
The integral of each one-head projector is
exactly \(N\).

For \(R>1\), the one-head mass outside
\(|u|^2\le R\) satisfies
\[
 \int_{|u|^2\ge R}E_d(N|u|^2)\,d\mu_N(u)
       \le N e^{-N I(R)},\qquad I(R)=R-1-\log R.
 \tag{19}
\]
To prove it, set \(s=N|u|^2\). For \(0<\theta<1\),
\[
 \frac1{a!}\int_{NR}^\infty e^{-s}s^a\,ds
       \le e^{-\theta NR}(1-\theta)^{-a-1}.
 \tag{20}
\]
This is the full gamma integral after multiplying
by \(e^{\theta(s-NR)}\ge1\). Take
\(\theta=1-R^{-1}\) and \(a+1\le N\), then sum
the \(N\) terms. A union bound over the \(rL\)
interface coordinates proves that the part of
(10) with some \(|u_{\ell,j}|^2>R\) is bounded
in absolute value by
\[
 rL\,N^{rL}e^{-NI(R)}
                         \prod_{\ell=1}^L\|T_\ell\|_H .
 \tag{21}
\]
The same bound holds for a differentiated product,
with the corresponding one differentiated norm
in each term of its exact product rule.

There is an elementary exponential bound on these
local norms for every fixed word. At the root,
reflection of the sine factors gives
\[
       |f_a f_{d-a}|=N,\qquad
       |f_a|\le2^d,\qquad |f_a|^{-1}\le2^d/N .
 \tag{22}
\]
Indeed the omitted factors in \(f_d=N\) have the
same moduli as the first \(d-a\) factors. Also
\[
 e^{-N}\le a!/N^a\le1\quad(0\le a\le d).
 \tag{23}
\]
For the lower bound use
\(\log(a!)\ge a\log a-a\); the sequence
\(a!/N^a\) is decreasing through \(a=d\), and
\((1-1/N)^{N-1}\ge e^{-1}\).
Thus passing between the original occupation norm,
the \(G_F\) gauge, and (16) costs only \(e^{C_rN}\).

On \(|M-1|\le2\eta/N\), for sufficiently large \(N\),
the finite arrows satisfy
\(\|F\|_2\le2\), \(\|\mathcal E\|_2\le4\),
and all fixed-width Cartan products and inverses
have bounded norms. V's exact positive Euler
series has coefficients
\((-1)^nq^{n^2}/f_n\); its inverse has \(q^n/f_n\).
Their \(n<N\) terms are therefore bounded using
(22) and \(\|\mathcal E_1F_2\|_2\le8\).
The finite sum has norm at most \(N C^N\).
The remaining crossing Cartan and flip have
bounded norms on this collar, apart from their
specified common scalar.

For a reduced star, \(\|F_{\rm tail}\|_2\) is
bounded by a constant depending only on the
fixed width and \(\eta\). Applying (22) to its
series in (2) of R, and to its actual inverse,
again gives \(N C^N\). The diagonal reduced
\(D\) has bounded norm on this collar.
The common crossing scalar is the original
\(\kappa=q^{\alpha^2/2}\), with
\(\alpha=N-1+\log M/\log q\). Thus
\[
 \frac{\kappa(M)}{\kappa(1)}
   =\exp\left((N-1)\log M+
                         \frac{(\log M)^2}{2\log q}\right),
 \tag{24}
\]
and \(|\kappa(1)|=1\). It and its inverse are
bounded on the stated collar. The prescribed
zero-framing powers have the same property.
Any additional external scalar line is still
retained explicitly, with its own domain.

Combining these facts gives constants \(C,p\)
for the unmarked reduced braid word, including
its displayed pivots and interfaces, such that
\[
 \prod_\ell\|T_\ell(M)\|_H\le N^p e^{CN}.
 \tag{25}
\]
Fixed-degree occupation marks add their polynomial
norms. Arbitrary extra matrix insertions retain
their own norms; no bound for them is inferred
from the unmarked word.
Cauchy's formula on the larger meridian collar
gives an additional \(O(N)\) for each fixed
meridian derivative on the smaller collar.
Consequently (21) makes the Gaussian ends
smaller than \(N^{p'}e^{-\Lambda N}\), for any
prescribed \(\Lambda>0\), by choosing one fixed
large \(R\) with \(I(R)>C+\Lambda\).
This is an actual global end estimate. It is
not a volume bound on the compact part of
the period.

## 5. Entire translation of the full cycle

Complexify each interface to independent \(z,w\).
The Gaussian measure is the restriction of
\[
 \left(\frac N{2\pi i}\right)^r
      e^{-Nz\cdot w}\bigwedge_{j=1}^r(dw_j\wedge dz_j)
 \tag{26}
\]
to \(z=u,w=\overline u\), with its original
orientation. The closed integrand is entire
in all these variables. For any fixed vectors
\(\alpha_\ell,\beta_\ell\), the simultaneous
translated cycle
\[
              z_\ell=u_\ell+\alpha_\ell,\qquad
              w_\ell=\overline u_\ell+\beta_\ell
 \tag{27}
\]
has exactly the same period.

Here the ends have a paired estimate as well. Put
\(F_N(v)=e^{-N|v|^2}E_d(N|v|^2)\). For one interface
the exact identity is
\[
 e^{-N\operatorname{Re}(zw)}
          \sqrt{E_d(N|z|^2)E_d(N|w|^2)}
 =e^{N|\alpha-\overline\beta|^2/2}
                         \sqrt{F_N(z)F_N(w)} .
 \tag{28}
\]
This follows from \(z-\overline w=\alpha-\overline\beta\).
Cauchy--Schwarz in the measure \((N/\pi)d^2u\)
and translation invariance of area bound its
full integral by
\(N e^{N|\alpha-\overline\beta|^2/2}\).
If \(|\alpha|,|\beta|\le A\) and \(|u|^2>R\),
both \(|z|\) and \(|w|\) exceed \(\sqrt R-A\).
Equation (19) in the same Cauchy--Schwarz estimate
therefore gives the tail bound
\[
 N e^{N|\alpha-\overline\beta|^2/2}
                e^{-NI((\sqrt R-A)^2)}
                       \qquad(\sqrt R-A>1).
 \tag{29}
\]
Apply these estimates independently to every
interface and use the finite union bound.
The resulting full bound is
\(N^{rL}\exp(\frac N2\sum|\alpha-\overline\beta|^2)
\prod\|T_\ell\|_H\), with the additional tail
factor from (29) for a large-coordinate event.
It is uniform on the compact translation
homotopy. Cutoff Stokes applied to the entire
form now has vanishing end terms, since its
cutoff error is bounded by these integrable
tails. This proves (27). Together with (25)
the same estimates give arbitrarily strong
exponential end control after one sufficiently
large fixed truncation, also for the exact
first meridian derivatives. Replacing the
finite \(E_d\) by the full exponential in
(28) would remove this decay and is not done.

A translation can pass through a specified
finite complex point. This equality moves
the whole cycle and retains every kernel.
It does not show that the point is a
stationary point of a uniform kernel phase,
that its normal cycle occurs with nonzero
coefficient, or that other parts have a
smaller exponential rate.

## 6. The elementary resolved coordinate adapter

There is a precise small-product region where the
finite elementary kernels identify the classical
coordinates. Put \(\tau=zw\) for one head. In the
all-\(G_F\) basis,
\[
 \begin{split}
 \mathcal K_K&=xE_d(NQ^{-1}\tau),\\
 \mathcal K_F&=zE_{d-1}(N\tau),\\
 \mathcal K_L&=z^{-1}\bigl(E_d(N\tau)-E_d(NQ\tau)\bigr),\\
 \mathcal K_{\mathcal E}
  &=z^{-1}\bigl(
       M E_d(NQ^{-1}\tau)+M^{-1}E_d(NQ\tau)
                      -(M+M^{-1})E_d(N\tau)\bigr).
 \end{split}
 \tag{30}
\]
Here \(L\) is the original unilateral lowering
shift. Apparent \(z^{-1}\)'s cancel in these
polynomial kernels. The \(F\) formula retains
its missing top arrow. For the last formula,
its input coefficient is exactly
\((1-Q^a)(MQ^{-a}-M^{-1})\).

For \(|\tau|\le\rho<1\), the exponential tail is
\[
 |e^{N\tau}-E_d(N\tau)|
            \le\frac{(e\rho)^N}{1-\rho}.
 \tag{31}
\]
This follows from the first omitted term and
its successive ratio at most \(\rho\), with
\(N!\ge(N/e)^N\). After division by \(e^{N\tau}\)
the bound is exponentially small whenever
\(1+\log\rho+\rho<0\), for example \(\rho=1/8\).
The same conclusion, with polynomial factors,
holds for \(E_{d-1}\), fixed derivatives, and
the \(Q^{\pm1}\) arguments on a smaller compact
region.

Dividing (30) by its exact identity kernel
and then taking the physical principal limit
on this region, with \(x_{\rm cl}=-M\), gives
\[
 A=e^{2\pi i zw},\quad f=z,\quad
 p=\frac{1-A}{z},\quad K=x_{\rm cl}/A,\quad
 e=(M/A-M^{-1})p .
 \tag{32}
\]
Thus this is the same physical factorial
coordinate as G, with the gauge transported.
Where defined,
\[
 d\log A\wedge d\log p=2\pi i\,dz\wedge dw .
 \tag{33}
\]
The term \(d\log(1-A)\) drops from that wedge.

For a recorded lower logarithmic lift at a
row endpoint, \(A=1,\ \log A=0,\ f\ne0\),
the resolved point is
\[
                         z=f,\qquad w=0 .
 \tag{34}
\]
Its G-coordinate \((A-1)/p\) is \(-z\), so
the flag resolution is retained. This point
is finite and lies in the cap-controlled
local region of (31). It usually lies off
the original real cycle \(w=\overline z\).

More generally a chosen finite logarithm
gives the algebraic assignment
\(z=f,\ w=(\log A)/(2\pi i f)\) on G's
all-\(f\)-unit geometric charts. It lies in
the complexified finite kernel domain, but
(31) need not hold there. In particular an
upper logarithmic lift at clock one is not
the lower point (34). No finite projector
or Fourier sheet is reset to put it there.
The full finite cap remains outside the
stated small-product estimate.

## 7. What the closed pairing still requires

Equation (15) inserts D's actual donor kernel
into (10), but a relative estimate for that
one factored kernel is not a relative estimate
for the whole period. The neighboring dual,
the integer recipient sum and its projectors
remain. For any finite kernel error \(E\),
the safe global contraction estimate is
the corresponding bound (18) with \(\|E\|_H\)
and the other local norms. Pointwise coherent
column control does not automatically give
that norm.

The superexponential donor tails of D can
outweigh exponential factors on a supplied
bounded paired domain with the required
recipient margin; this does not establish
such a domain for the original whole cycle.
The fixed global Gaussian tails (21) and
their translated versions control only the
ends of the exact representation. The
compact part, its factorial caps, and its
geometric intersection remain to be analyzed.
In particular no positivity, geometric
coefficient, or scalar lower bound follows.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* V: notes/balanced_verma_coherent_braiding.md,
  SHA256 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.
* D: notes/research_reduced_euler_donor_coherent_sum.md,
  SHA256 ff35583f203ae7686de4ff7fb91fcb4d4d0190e4f8995bd89a871849bc91d7f4.
* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

All five complete sources were freshly read nontruncated
in the active author sequence and retained unchanged.
Every used implication was checked. The kernels,
pairings, end estimates and coordinate adapter above
are written calculations. No mathematical programs
were run; frozen and public files were not edited.
