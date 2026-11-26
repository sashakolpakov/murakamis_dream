# Finite endpoint clusters with every intermediate projector

Private written proof, 18 November 2026.

The finite Euler blocks of a regular endpoint cluster have a uniform
resummation against the actual analytic neighboring integrand. Every
intermediate stage projector survives as an integer path condition
or its original finite Fourier kernel.
The result on a microscopic physical face is a constrained Poisson
series, which need not equal the unrestricted exponential.

The proof uses the literal finite-matrix estimates E, the analytic
environment constructed in J, and L's integral endpoint graph.
The exact source identity is on integer
labels. The asymptotic statement is for the finite endpoint-index
functional on a supplied compatible analytic spectator chart, before
integration on a supplied normal chain. It does not
identify that local contribution with a whole neighboring matrix entry
or assign the original source cycle to this chart. Transfers between
opposite endpoint collars remain exact complementary source terms.

## 1. The actual finite sector

Fix the braid and a finite collection of \(m\) extracted zero Euler
blocks. The number \(m\) does not grow with \(N\). Set
\[
 c_0=2\pi i,\quad h=c_0/N,\quad q=e^{h/2},\quad Q=e^h,\quad d=N-1.
 \tag{1}
\]
Label each block in its literal operator order, absorbing its flip,
Cartan line and diagonal gauge transitions into the neighboring
factors in that same order. Its Euler factor has sign
\(\varepsilon_i=1\) or \(-1\) and transfer \(n_i\). In E's notation
\[
 \Theta_i^{\varepsilon_i}
   =\sum_{n_i=0}^{d}\gamma_{N,n_i}^{\varepsilon_i}
                                      (A_i/h)^{n_i},
\quad
 \gamma_{N,n}^{+}=\frac{(-1)^nq^{n^2}h^n}{F_n(Q)},\quad
 \gamma_{N,n}^{-}=\frac{q^nh^n}{F_n(Q)}.
 \tag{2}
\]
Thus a negative crossing uses its actual inverse factor, not a
positive factor with its input/output labels left unchanged.

At a separated row-type endpoint, choose \(G_F\) on both interfaces
of a zero block; at a column-type endpoint choose \(G_E\). Any
transition to a different gauge elsewhere remains in the environment.
The transfer arrows in these two choices are, respectively,
\[
 \frac{A_i}{h}
   =\frac{\beta_a}{h}S_-\otimes S_+,\qquad
 \frac{A_i}{h}
   =S_-\otimes\frac{\beta_{b+1}}h S_+,
\quad
 \beta_j=-4\sin^2(\pi j/N).
 \tag{3}
\]
The notation records coefficients on the input basis vector.
Both unit shifts have their literal extreme zero:
\(S_-|0\rangle=0\), \(S_+|d\rangle=0\).
No classical unit momentum removes either zero.

Choose a finite-window sector by retaining diagonal projectors at
every specified intermediate stage. Each zero-factor head has its
input and output in the same lower or upper collar of width at most
\(C\sqrt N\). The other stage windows may impose additional physical
or artificial bounds. In particular this sector does not include
an upper-to-lower transfer of order \(N\).

Let \(k\) denote the actual exposed integer coordinates after
choosing the cut and the remaining transfers. The matching equations
make every head occupation an integer affine function of
\((k,\boldsymbol n)\). Retain all physical arrows and all chosen
stage projectors by their exact mask
\[
 \chi_N(k,\boldsymbol n)=
   \prod_{\ell=1}^{L}
       {\bf1}_{d_{\ell,N}(k)+B_\ell\boldsymbol n\ge0},
 \qquad \boldsymbol n\in\mathbb Z_{\ge0}^m.
 \tag{4}
\]
Here the rows \(B_\ell\) are fixed integer rows. The finite list
includes \(n_i\le d\), all physical wire bounds, and every selected
stage window. Repeated or redundant rows are harmless. The integers
\(d_{\ell,N}(k)\) can be negative: the zero-transfer reference point
need not be a supported word state. This convention also retains
affine current states entering a window after a finite shift.

For an allowed path, multiply the actual \(n_i\) successive arrow
coefficients of \(A_i/h\), with all their shifted inputs, to obtain
\(T_{N,i}(k,\boldsymbol n)\). It is a product of \(n_i\) factors.
The coefficient of the whole local sector is exactly
\[
 Z_N(k)=
 \sum_{\boldsymbol n\ge0}
 \chi_N(k,\boldsymbol n)\,
 I_{{\rm env},N}(y_N,h\boldsymbol n)
 \prod_{i=1}^m
       \gamma_{N,n_i}^{\varepsilon_i}T_{N,i}(k,\boldsymbol n).
 \tag{5}
\]
The sum is finite. Formula (5) is matrix multiplication followed by
the original matching constraints. It does not commute a projector
past a crossing.

One can also see the distinction directly in an ordered product:
\[
 P_m\Theta_mP_{m-1}\Theta_{m-1}\cdots P_1\Theta_1P_0.
 \tag{6}
\]
Its path sum contains all the indicated intermediate masks.
It has not been replaced by \(P_m(\prod_i\Theta_i)P_0\), or by
products of independently reset boundary kernels. Expanding
\(1=P_j+(1-P_j)\) at the recorded stages gives an exact finite
decomposition of the original network. Every other projector pattern
is a retained complementary source term.

Monotonicity is used only within one Euler block. Its donor decreases
and recipient increases. If the input and output of its zero-factor
head lie in the same endpoint collar, all intermediate zero-factor
indices lie there too. Moreover
\[
                n_i\le C'\sqrt N\quad\text{whenever }\chi_N=1.
 \tag{7}
\]
The other head's physical input/output inequalities retain the unit
shift's forced zero. Thus (3) is uniformly bounded along every
allowed local path. No assertion is made about a path going from an
upper collar through the bulk to a lower collar.

## 2. The actual analytic environment and its shifted arguments

Use J's buffered endpoint chart, on which all surviving factorial
arguments have been verified in their marked slit domains. Its exact
gauge cancellation gives
\[
 I_{{\rm env},N}(y,\boldsymbol\nu)
    =\Gamma_NN^\alpha a_N(y,\boldsymbol\nu)
                       e^{S(y,\boldsymbol\nu)/h},
 \qquad a_N=a_0+O(N^{-1}),\qquad a_0\ne0.
 \tag{8}
\]
The holomorphic functions and all fixed derivatives are uniform on
smaller fixed neighborhoods. The unchanged scalar line \(\Gamma_N\),
original cut, pivots and Cartan factors are included. Equation (8)
is the actual local integrand statement, not a hypothesis of
independent Gaussian matrix coefficients.

For the asymptotic assertion, consider a family of retained discrete
endpoint data and analytic spectator arguments for which the actual
affine port reconstruction gives the coefficients in (5), the masks
remain those of (4), the reference endpoint indices in (12) are
bounded after division by \(\sqrt N\), and
\(y_N=y_*+N^{-1/2}w_N\), with \(w_N\) in a fixed compact set.
These are conditions on the family to which the estimate is applied.
They do not assert that the geometric chart supplies such an original
lattice sequence. Put
\[
 \zeta_i=\exp(\partial_{\nu_i}S(y_*,0)).
 \tag{9}
\]
For large \(N\), \(I_{{\rm env},N}(y_N,0)\ne0\) on this chart.
Taylor's formula and (7) give the uniform estimates
\[
 \left|
 \frac{I_{{\rm env},N}(y_N,h\boldsymbol n)}
      {I_{{\rm env},N}(y_N,0)}
       \right|\le C D^{|\boldsymbol n|},
 \tag{10}
\]
\[
 \left|
 \frac{I_{{\rm env},N}(y_N,h\boldsymbol n)}
      {I_{{\rm env},N}(y_N,0)}
               -\prod_i\zeta_i^{n_i}\right|
 \le C D^{|\boldsymbol n|}
       \left(\frac{1+|\boldsymbol n|}{\sqrt N}
                     +\frac{|\boldsymbol n|^2}{N}\right)
 \tag{11}
\]
on every allowed path. Here and below
\(|\boldsymbol n|=\sum_i n_i\).
To verify this, the linear phase term differs from
\(\sum_i n_i\log\zeta_i\) by \(O(|\boldsymbol n|/\sqrt N)\).
The quadratic remainder in \(\boldsymbol\nu\), after division by
\(h\), is \(O(|\boldsymbol n|^2/N)\). Both are bounded on (7).
The amplitude ratio is \(1+O((1+|\boldsymbol n|)/N)\).
The elementary integral formula for the difference of two
exponentials proves (10)--(11). This retains, rather than resets,
every shifted argument \(h\boldsymbol n\).

These estimates remain valid when \(H_{\rm env}=\partial_y^2S(y_*,0)\)
is singular. No integration or inverse environmental Hessian has
entered their proof.

The mask remains a condition on literal integer labels \(k\).
At the literal lattice values, (5) is the exact source coefficient.
If regular spectator arguments are analytically continued while the
retained endpoint data remain discrete, (5) defines the corresponding
finite endpoint-index functional only through the specified affine
port map. Complex analytic parameters do not turn indicators into
inequalities on complex numbers. In particular, a generic complex
geometric \(y_*\) is not a limit of \(h\) times a full real integer
chord lattice. Any indicator involving a genuinely continued
occupation must instead retain its original
Fourier/projector/coefficient-extraction representation; the estimate
here does not construct that continuation. Neither a compatible
original occupation contour nor its source chain follows from (8).

### The integral endpoint ports and the continued spectators

Here is an explicit port construction, so the affine map is not an
additional compatibility assumption. Use L's expanded graph and
\(\Lambda=\ker(\partial:\mathbb Z^{E(\Gamma)}\to\mathbb Z^{V(\Gamma)})\).
Let \(I\) consist of its clock-one wire edges and the extracted
zero-transfer edges. In the chosen regular chart these are exactly
the endpoint edges under consideration. By L's tree proof,
\[
 B=\operatorname{im}(\Lambda\longrightarrow\mathbb Z^I)
       =\ker\partial_{\Gamma_I},\qquad
 K=\ker(\Lambda\longrightarrow B).
 \tag{11a}
\]
The cut and transfer edges are primitive chord coordinates of
\(\Lambda\). Consequently the projection
\(B\longrightarrow\mathbb Z^m\) onto the extracted transfer
coordinates is surjective: prescribe those chords arbitrarily in
\(\Lambda\), and then restrict to \(I\).
Let \(B_0\) be its kernel. All these groups are free abelian.
Choose a basis of each quotient and lift its basis vectors; this
proves, constructively, both integral splittings and gives
\[
                  \Lambda\simeq K\oplus B_0\oplus\mathbb Z^m.
 \tag{11b}
\]
The last coordinates are the actual \(\boldsymbol n\). The middle
coordinates are the remaining coupled endpoint ports. No endpoint
edge is declared independent of the incidence constraints.
For the \(\mathbb Z^m\) summand choose the original primitive chord
vectors: one extracted transfer is one and every other chord,
including the cut, is zero. Thus varying \(\boldsymbol n\) at fixed
other ports leaves J's remaining chord variables \(y\) fixed.
Its induced endpoint-wire shifts are still the exact rows in (4).

L proves that the cut is not a bridge after deleting \(I\).
The resulting complementary integral circulation \(c\in K\)
has cut coordinate one. Subtracting the cut coordinate times
\(c\) from each chosen lift makes every \(B_0\) and
\(\mathbb Z^m\) lift have cut coordinate zero. The \(K\) variables
then include the cut spectator and change no endpoint edge.
They are the regular variables that can be continued complex
analytically without making the endpoint inequalities complex.

The upper offset also has an exact integral lift. Write \(b=0\)
for the row assignment and \(b=\gamma|_I\) for the column assignment,
where \(\gamma\) is the oriented knot circulation. Its transfer
coordinates are zero. Choose its lift \(\ell_b\in\Lambda\)
with cut coordinate zero. For a compatible geometric logarithm
vector \(z_*\), L gives
\[
 z_*=c_0\ell_b+z_{\rm comp},\qquad z_{\rm comp}\in K\otimes\mathbb C,
 \qquad
 z_{N,*}=h d\,\ell_b+z_{\rm comp}=z_*-h\ell_b .
 \tag{11c}
\]
Thus the column wire ports have exactly the finite base index
\(d=N-1\), the row ports have base zero, and the cut logarithm is
unchanged. Integral endpoint displacements and the actual transfer
vector are added using (11b). The \(O(h)\) shift in (11c) lies
within the scale used in (10)--(11); it is retained in the affine
arguments rather than discarded. This construction uses no
positivity or nonnegative-flow assertion.

For this hybrid continuation, factor the original discrete mask
as \(\chi_N=\chi_{I,N}\chi_{{\rm reg},N}\): the first factor contains
all endpoint and small-transfer path/window rows, the second all
remaining head projectors. The endpoint factor is independent of
the \(K\) spectators and remains a literal \(0/1\) mask.
The regular projectors remain their exact finite kernels and are not
evaluated as inequalities at complex spectators. Their dependence
on the small transfers must also be retained. For a regular
occupation \(A_\ell(k)+\sum_i B_{\ell i}n_i\) and retained interval
\([L_\ell,U_\ell]\), put
\[
 {\cal P}_{\ell,N}(z_\ell)=
       \sum_{a=L_\ell}^{U_\ell}z_\ell^{-a},\qquad
 \mu_i(\boldsymbol z)=\prod_\ell z_\ell^{B_{\ell i}}.
 \tag{11d}
\]
The elementary constant-term identity is exactly
\[
 \chi_{{\rm reg},N}(k,\boldsymbol n)
 =\operatorname{CT}_{\boldsymbol z}
   \left[
    \prod_\ell{\cal P}_{\ell,N}(z_\ell)z_\ell^{A_\ell(k)}
                      \prod_i\mu_i(\boldsymbol z)^{n_i}
   \right].
 \tag{11e}
\]
It holds for every integer affine occupation, including those outside
the physical range; no reduction modulo \(N\) is made. On the
actual finite head it is also the usual finite Fourier projector.
The upper and lower monomials have both been retained.

Let \(Z_{I,N}(k;\boldsymbol z)\) denote (5) with mask \(\chi_{I,N}\)
and the extra multiplier \(\prod_i\mu_i(\boldsymbol z)^{n_i}\)
inside the transfer sum. Its regular unit arrows have their
preprojector coefficient one; their forbidden extremes belong to
the regular projectors retained in (11e). Then the original discrete
sector is exactly
\[
 Z_N(k)=\operatorname{CT}_{\boldsymbol z}
   \left[
    \prod_\ell{\cal P}_{\ell,N}(z_\ell)z_\ell^{A_\ell(k)}
                         Z_{I,N}(k;\boldsymbol z)
   \right].
 \tag{11f}
\]
Thus retaining a regular projector outside the endpoint functional
means this exact extraction, with all transfer markers still inside;
it does not mean pairing an already evaluated scalar kernel.
On fixed unit circles \(|\mu_i|=1\), and on any fixed compact
polyannulus they are uniformly bounded. All estimates below
therefore apply with \(\lambda_i\) replaced by
\(\mu_i(\boldsymbol z)\lambda_i\), uniformly on such a marker set.

The theorem below applies either to the full discrete mask where
Section 2's hypotheses hold, or to the endpoint finite-index
functional with mask \(\chi_{I,N}\) and these transfer markers,
leaving the regular projector factors and their original extraction
outside that functional.
Both choices retain the collar bounds (7).
Restoring those factors requires their actual extraction or source
chain; no bound for that operation is asserted here. In particular
continuing an exponent \(A_\ell(k)\) off the integer lattice does
not automatically continue its closed constant-term contour.

The integral splittings do not imply a nonempty physical integer
fiber. Directed nonnegative-flow constraints can still kill every
path, including the zero path. Nor do they produce a macroscopic
physical interior or an original contour near a generic complex
\(z_*\). All such constraints remain in the masks and projector
pairings just described.

## 3. Uniform resummation against the exact finite path mask

For each zero block, let \(j_{i,N}(k,0)\) be its zero-factor endpoint
index at the zero-transfer reference point. Its exact convention is
\[
\begin{array}{c|cc}
 &\text{lower collar}&\text{upper collar}\\ \hline
 G_F\text{ donor}&a&N-a\\
 G_E\text{ recipient}&b+1&d-b .
\end{array}                                                     \tag{12}
\]
The \(+1\) and \(d=N-1\) have not been dropped from the finite source.
Set
\[
 \xi_{i,N}=j_{i,N}(k,0)/\sqrt N,\qquad
 t_{i,N}=c_0\xi_{i,N}^{\,2},\qquad
 \lambda_{i,N}=\varepsilon_i\zeta_i t_{i,N}.
 \tag{13}
\]
The exposed compact set keeps all \(\xi_{i,N}\) bounded. This
polynomial reference is used even when the zero-transfer state is
outside a selected window; no negative factorial is evaluated there.

Define the exact-mask polynomial
\[
 {\cal K}_N(k;\boldsymbol\lambda)=
 \sum_{\boldsymbol n\ge0}\chi_N(k,\boldsymbol n)
                         \prod_i\frac{\lambda_i^{n_i}}{n_i!}.
 \tag{14}
\]
Here \(\chi_N\) denotes the chosen retained discrete mask from
Section 2; any complementary regular projector factors remain in
the specified external pairing, with (11d)'s transfer markers
inserted inside this kernel before pairing.
The main estimate is
\[
 \boxed{\quad
 \frac{Z_N(k)}{I_{{\rm env},N}(y_N,0)}
       ={\cal K}_N(k;\boldsymbol\lambda_N)+O(N^{-1/2}).
 \quad}                                                        \tag{15}
\]
It is uniform on the specified compact exposed set, including all
its retained closed discrete faces. The mask in (15) is the exact
\(N\)-dependent mask; no continuous approximation to a projector
is being asserted.

Here is the quantitative proof. E gives, for \(0\le n<N\),
\[
 |\gamma_{N,n}^{\varepsilon}|\le C_1^n/n!,\qquad
 |\gamma_{N,n}^{\varepsilon}-\varepsilon^n/n!|
                              \le C_1^n n^2/(Nn!).
 \tag{16}
\]
For \(0\le j\le C\sqrt N\),
\[
 \frac{-4\sin^2(\pi j/N)}{h}
                    =c_0(j/\sqrt N)^2+O(N^{-1}).
 \tag{17}
\]
The same formula applies at the upper endpoint after replacing the
index by \(N-j\). Actual matching shifts and the position within a
local power change (12) by at most \(C_2|\boldsymbol n|\).
The reference quadratic is Lipschitz on a fixed bounded set.
Every allowed one-step coefficient therefore differs from \(t_{i,N}\)
by at most \(C_3(1+|\boldsymbol n|)/\sqrt N\), and all such
coefficients are uniformly bounded.
Telescoping a product of \(|\boldsymbol n|\) factors yields
\[
 \left|\prod_i T_{N,i}
                   -\prod_i t_{i,N}^{\,n_i}\right|
   \le C_4^{|\boldsymbol n|}
                  \frac{|\boldsymbol n|(1+|\boldsymbol n|)}{\sqrt N}.
 \tag{18}
\]
No division by \(t_{i,N}\) is used; (18) includes the zero faces.
For the full discrete mask, unit arrows equal one on an allowed
path and (4) excludes their forbidden extremes. For the endpoint-only
functional, retained endpoint arrows obey the same rule, while
regular unit arrows have preprojector coefficient one and their
forbidden extremes remain in (11e)--(11f). No forbidden physical
arrow has been assigned coefficient one in the restored source.

Combine (10)--(11), (16), and (18). The error of each summand in
(15) is bounded by
\[
 \frac{C_5^{|\boldsymbol n|}(1+|\boldsymbol n|)^2}
                         {\sqrt N\prod_i n_i!}.
 \tag{19}
\]
Its sum over all nonnegative \(m\)-tuples is finite independently of
\(N,k\), since \(m\) is fixed. This proves (15), including the
large finite transfers in (7). It does not estimate a transfer
sector absent from the same-collar condition.

## 4. The limiting microscopic boundary kernel

Let a family satisfying Section 2 have retained discrete data
\(k_N\) such that, after passage to a subsequence if necessary,
\[
 d_{\ell,N}(k_N)\longrightarrow
             d_\ell\in\mathbb Z\cup\{-\infty,+\infty\},
 \qquad \lambda_{i,N}\longrightarrow\lambda_i.
 \tag{20}
\]
For a finite limiting integer the distance is eventually that
integer. A \(+\infty\) row imposes no restriction on a fixed transfer
vector; a \(-\infty\) row excludes every fixed vector.
Define
\[
 \chi_{\boldsymbol d}(\boldsymbol n)=
  \prod_{\ell:d_\ell\in\mathbb Z}
       {\bf1}_{d_\ell+B_\ell\boldsymbol n\ge0},
 \quad
 {\cal K}_{\boldsymbol d}(\boldsymbol\lambda)
   =\sum_{\boldsymbol n\ge0}\chi_{\boldsymbol d}(\boldsymbol n)
                           \prod_i\frac{\lambda_i^{n_i}}{n_i!}.
 \tag{21}
\]
If a \(-\infty\) row occurs, the kernel is defined to be zero.
Finite projector multiplicities have not been replaced by a
set-theoretic leading face: (21) uses all their integer rows.

Dominated convergence with the majorant in (19) proves
\[
 \frac{Z_N(k_N)}{I_{{\rm env},N}(y_N,0)}
                  \longrightarrow
                    {\cal K}_{\boldsymbol d}(\boldsymbol\lambda).
 \tag{22}
\]
The series is entire in its \(m\) complex arguments and obeys
\[
             |{\cal K}_{\boldsymbol d}(\boldsymbol\lambda)|
                       \le\exp\left(\sum_i|\lambda_i|\right).
 \tag{23}
\]
It can vanish; no scalar lower bound follows from this majorant.

There is nevertheless a uniform anchored statement. If the genuine
\(0/1\) mask retains the zero-transfer path, then
\[
 |{\cal K}_N(k;\boldsymbol\lambda)-1|
       \le e^{\sum_i|\lambda_i|}-1,
 \qquad
 |{\cal K}_{\boldsymbol d}(\boldsymbol\lambda)-1|
       \le e^{\sum_i|\lambda_i|}-1
 \tag{23a}
\]
whenever the limiting mask also retains that path. This follows by
bounding all positive-transfer terms by the unrestricted exponential
series. In particular either kernel has modulus greater than
\(1/2\) when \(\sum_i|\lambda_i|<\log(3/2)\).
For a fixed \(\eta<\log(3/2)\), (15) gives the actual bound
\[
 \left|\frac{Z_N(k)}{I_{{\rm env},N}(y_N,0)}\right|
                \ge 2-e^\eta-CN^{-1/2}>0
 \tag{23b}
\]
for large \(N\), provided \(\chi_N(k,0)=1\) and
\(\sum_i|\lambda_{i,N}|\le\eta\).
Because (13) is quadratic, a sufficiently small bounded scaled
neighborhood has this property whenever its zero-transfer paths
are retained. This is a finite-window kernel statement.
An affine current sector may have \(\chi_N(0)=0\), and a signed
sum of sectors need not have the anchor one. Closing differences
can annihilate its constant term. Neither (23a) nor (23b) is a
lower bound for an integrated or globally assembled current.

A single unit recipient shift at upper distance \(b_{\rm top}\)
retains the condition \(n\le b_{\rm top}\). If that distance tends
to a finite \(\ell\ge0\), its boundary kernel is exactly
\[
                         \sum_{n=0}^{\ell}\lambda^n/n!.
 \tag{24}
\]
A unit donor shift at lower distance \(\ell\) has the same formula.
Repeated transfers through that head retain every intermediate
inequality. For example a jointly monotone budget gives
\(\sum_{n_1+\cdots+n_m\le\ell}\prod_i\lambda_i^{n_i}/n_i!\);
a different stage mask has its own series (21). It cannot be
replaced merely by a final-endpoint condition allowing an excursion
through a forbidden intermediate head.

In contrast, a compatible local quadratic-zero bound \(n_i\le a\)
at fixed \(a\) has \(t_{i,N}\to0\). Its positive-\(n_i\) terms
then vanish in the limiting series. This explains why that
particular bound can become harmless. In a closed matching network
other transfers can occur in the same affine facet row. They
remain in (21); compatible local arrows alone do not remove them.

Precisely, the unrestricted exponential is recovered if the limiting
mask is one for every nonnegative vector supported on indices with
\(\lambda_i\ne0\):
\[
        {\cal K}_{\boldsymbol d}(\boldsymbol\lambda)
                              =\exp\left(\sum_i\lambda_i\right).
 \tag{25}
\]
The interior regime, where all finite-step paths are eventually
retained, is one such case. Equation (25) is not asserted uniformly
across wrong-facing or artificial window boundaries.

## 5. Correlated normal variables and retained currents

Put \(S_*=S(y_*,0)\). J gives, on the exposed scale
\(y_N=y_*+N^{-1/2}w_N\), along
any family with \(w_N\to w\),
\[
 \frac{I_{{\rm env},N}(y_N,0)}
      {\Gamma_NN^\alpha e^{S_*/h}}
 \longrightarrow
       a_0(y_*,0)
          \exp\left\{\frac{w^tH_{\rm env}w}{2c_0}\right\}.
 \tag{26}
\]
Combining (22) and (26) gives the actual local joint profile
\[
 a_0(y_*,0)
    \exp\left\{\frac{w^tH_{\rm env}w}{2c_0}\right\}
                         {\cal K}_{\boldsymbol d}
                                   (\boldsymbol\lambda(w)).
 \tag{27}
\]
This keeps all normal variables together. It requires no independent
Gaussian in the observed occupations and no nonsingular principal
minor of \(H_{\rm env}\). If the additional projector markers are
present, replace \(\lambda_i(w)\) by
\(\mu_i(\boldsymbol z)\lambda_i(w)\) before their extraction.
For the original unmodified character and the interior case (25),
J identifies the combined quadratic form with the geometric one and
retains its flat framing direction. That identification is not
asserted for every independent marker value. On a microscopic face
the correct factor is (21).

On a supplied compact local chain for which the hypotheses and a
common integrable majorant hold, these pointwise statements may be
integrated by dominated convergence. That statement does not place
the original relative cycle on the chain. Nor does it control a
noncompact framing direction or a singular boundary of the supplied
environmental chart.

All identities preceding the limits are finite matrix identities.
Their original quantum/meridian normals are taken before setting
the two head-wall coefficients to zero. No wall factor has been
divided out, and every interface projector stays fixed while the
actual matrices and gauges are differentiated. A new uniform
normal asymptotic for the environment is not supplied by this note:
the application above uses J's central-root expansion. The whole
ordinary pivot/twist adapter is still required for an ordinary
closed-color normal comparison.

The other terms in the exact projector decomposition after (6),
opposite-collar transfers of order \(N\), prefix-zero strata and
infinite framing ends have not been bounded or canceled. This
theorem determines the local finite-window boundary functional
against the analytic neighboring source; it does not prove a
nonzero global contribution or a volume-conjecture lower bound.

## Complete proof sources

* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* J: notes/research_regular_endpoint_joint_geometric_packet.md,
  SHA256 eb1eccb4701685272a71c719cfc2de35d9059956b15ff79a9fc9f4e94a4697b6.
* L: notes/research_regular_endpoint_logarithms_and_slit_chart.md,
  SHA256 dc340b9beef5dcdc2a01a35030515cc36cf5e6a6babad66b3fce03351817dc7b.

All three complete direct texts were freshly read nontruncated in
the current active author/review sequence, including the entire
matching frozen J and L. Every used implication was checked.
Only written mathematics and source/text operations have been used.
Frozen and public files are unchanged.
